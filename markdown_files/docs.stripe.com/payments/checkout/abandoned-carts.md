htmlRecover abandoned carts | Stripe Documentation[Skip to content](#main-content)Recover abandoned carts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fabandoned-carts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fabandoned-carts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Checkout](/payments/checkout)·[Home](/docs)[Payments](/docs/payments)[Checkout](/docs/payments/checkout)# Recover abandoned carts

Learn how to recover abandoned Checkout pages and boost revenue.Customers may leave Checkout before completing their purchase. In e-commerce, this is known as cart abandonment. To help bring customers back to Checkout, create a recovery flow where you follow up with customers over email to complete their purchases. You can do this with webhooks (see below) or with no-code Cart Recovery Emails.

Cart abandonment emails fall into the broader category of promotional emails, which includes emails that inform customers of new products and that share coupons and discounts. Customers must agree to receive promotional emails before you can contact them.

Checkout helps you:

1. Collect consent from customers to send them promotional emails.
2. Get notified when customers abandon Checkout so you can send cart abandonment emails.

[Collect promotional consent](#collect-promotional-consent)Configure Checkout to collect consent for promotional content. See the full guide for more details.

Stripe-hosted pageEmbedded formCommand Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "line_items[0][price]"={{PRICE_ID}} \
  -d "line_items[0][quantity]"=2 \
  -d customer={{CUSTOMER_ID}} \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success" \
  --data-urlencode cancel_url="https://example.com/cancel" \
  -d "consent_collection[promotions]"=auto`If you collect the customer’s email address and request consent for promotional content before redirecting to Checkout, you may skip using consent_collection[promotions].

[Configure recovery](#configure-recovery)A Checkout Session becomes abandoned when it reaches its expires_at timestamp and the buyer hasn’t completed checking out. When this occurs, the session is no longer accessible and Stripe fires the checkout.session.expired webhook, which you can listen to and try to bring the customer back to a new Checkout Session to complete their purchase.

To use this feature, enable after_expiration.recovery when you create the session.

Stripe-hosted pageEmbedded formCommand Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "line_items[0][price]"={{PRICE_ID}} \
  -d "line_items[0][quantity]"=1 \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success" \
  --data-urlencode cancel_url="https://example.com/cancel" \
  -d customer={{CUSTOMER_ID}} \
  -d "consent_collection[promotions]"=auto \
  -d "after_expiration[recovery][enabled]"=true \
  -d "after_expiration[recovery][allow_promotion_codes]"=true`[Get notified of abandonment](#webhook)Listen to the checkout.session.expired webhook to be notified when customers abandon Checkout and sessions expire. When the session expires with recovery enabled, the webhook payload contains after_expiration, which includes a URL denoted by after_expiration.recovery.url that you can embed in cart abandonment emails. When the customer opens this URL, it creates a new Checkout Session that’s a copy of the original expired session. The customer uses this copied session to complete the purchase on a Stripe-hosted payment page.

NoteFor security purposes, the recovery URL for a session is usable for 30 days, denoted by the after_expiration.recovery.expires_at timestamp.

`{
  "id": "evt_123456789",
  "object": "event",
  "type": "checkout.session.expired",
  // ...other webhook attributes
  "data": {
    "object": {
      "id": "cs_12356789",
      "object": "checkout.session",
      // ...other Checkout Session attributes
      "consent_collection": {
        "promotions": "auto",
      },
      "consent": {
        "promotions": "opt_in"
      },
      "after_expiration": {
        "recovery": {
          "enabled": true,
          "url": "https://buy.stripe.com/r/live_asAb1724",
          "allow_promotion_code": true,
          "expires_at": 1622908282,
        }
      }
    }
  }
}`[Send recovery emails](#send-recovery-emails)To send recovery emails, create a webhook handler for expired sessions and send an email that embeds the session’s recovery URL. One customer may abandon multiple Checkout Sessions, each triggering its own checkout.session.expired webhook so make sure to record when you send recovery emails to customers and avoid spamming them.

[Node](#)`// Find your endpoint's secret in your Dashboard's webhook settings
const endpointSecret = 'whsec_...';

// Using Express
const app = require('express')();

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require('body-parser');

const sendRecoveryEmail = (email, recoveryUrl) => {
  // TODO: fill me in
  console.log("Sending recovery email", email, recoveryUrl);
}

app.post('/webhook', bodyParser.raw({type: 'application/json'}), (request, response) => {
  const payload = request.body;
  const sig = request.headers['stripe-signature'];

  let event;

  try {
    event = stripe.webhooks.constructEvent(payload, sig, endpointSecret);
  } catch (err) {
    return response.status(400).send(`Webhook Error: ${err.message}`);
  }

  // Handle the checkout.session.expired event
  if (event.type === 'checkout.session.expired') {
    const session = event.data.object;

    // When a Checkout Session expires, the buyer's email is not returned in
    // the webhook payload unless they give consent for promotional content
    const email = session.customer_details?.email
    const recoveryUrl = session.after_expiration?.recovery?.url

    // Do nothing if the Checkout Session has no email or recovery URL
    if (!email || !recoveryUrl) {
      return response.status(200).end();
    }

    // Check if the buyer has consented to promotional emails and
    // avoid spamming people who abandon Checkout multiple times
    if (
      session.consent?.promotions === 'opt_in'
      && !hasSentRecoveryEmailToCustomer(email)
    ) {
      sendRecoveryEmail(email, recoveryUrl)
    }
  }
  response.status(200).end();
});`[OptionalAdjust session expiration](#adjust-session-expiration)[OptionalTrack conversion](#track-conversion)[OptionalOffer promotion codes in recovery emails](#promotion-codes)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Collect promotional consent](#collect-promotional-consent)[Configure recovery](#configure-recovery)[Get notified of abandonment](#webhook)[Send recovery emails](#send-recovery-emails)Products Used[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`