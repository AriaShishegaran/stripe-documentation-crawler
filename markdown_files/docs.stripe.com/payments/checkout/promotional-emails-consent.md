htmlCollect consent for promotional emails | Stripe Documentation[Skip to content](#main-content)Collect consent for promotional emails[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fpromotional-emails-consent)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fpromotional-emails-consent)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Checkout](/payments/checkout)·[Home](/docs)[Payments](/docs/payments)[Checkout](/docs/payments/checkout)# Collect consent for promotional emailsUS only

Learn how to collect permission from customers so that you can send them promotional emails.Promotional emails are often sent to inform customers of new products and to share coupons and discounts. For example, you can use them to subscribe customers to company newsletters or send cart abandonment emails.

![Collect consent for promotional emails](https://b.stripecdn.com/docs-statics-srv/assets/promotional-consent-collection.444ead1668bd41537b9a07b2dbdc219a.png)

Collect consent from customers to send them promotional emails

To protect consumers from unwanted spam, customers must agree to receiving promotional emails before you can contact them. Checkout helps you collect the necessary consent, where applicable, to send promotional emails. Learn more about promotional email requirements.

[Collect consent](#collect-consent)You can collect promotional email consent with Stripe Checkout when you create the session:

Stripe-hosted pageEmbedded formCommand Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "line_items[0][price]"={{PRICE_ID}} \
  -d "line_items[0][quantity]"=2 \
  -d customer={{CUSTOMER_ID}} \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success" \
  --data-urlencode cancel_url="https://example.com/cancel" \
  -d "consent_collection[promotions]"=auto`When consent_collection.promotions='auto', Checkout dynamically displays a checkbox for collecting the customer’s consent to promotional content.

NoteWhen the checkbox is shown, the default state depends on the customer’s country and the country your business is based in. Data privacy laws vary by jurisdiction, so Checkout disables or limits this feature when local regulations prohibit it.

[Store consent and email address](#store-consent)The Checkout Session’s consent attribute records whether or not the session collected promotional consent from the customer.

As customers complete purchases, keep track of which customers consent to promotional content. You can create or update an existing webhook handler to do this. Listen to the checkout.session.completed event, check for the consent.promotions status, and then store email addresses for customers who give consent.

[Node](#)`// Find your endpoint's secret in your Dashboard's webhook settings
const endpointSecret = 'whsec_...';

// Using Express
const app = require('express')();

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require('body-parser');

const recordPromotionalEmailConsent = (email, promoConsent) => {
  // TODO: fill me in
  console.log("Recording promotional email consent", email, promoConsent);
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

  // Handle the checkout.session.completed event
  if (event.type === 'checkout.session.completed') {
    const session = event.data.object;
    const promoConsent = session.consent?.promotions;
    const email = session.customer_details.email;

    // Record whether or not the customer has agreed to receive promotional emails
    recordPromotionalEmailConsent(email, promoConsent)

    // Handle order fulfillment
  }
  response.status(200).end();
});`## See also

After you’ve configured Checkout to collect consent for sending customers promotional content, you can recover abandoned carts by following up with leads who left Checkout before completing payment.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Collect consent](#collect-consent)[Store consent and email address](#store-consent)[See also](#see-also)Products Used[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`