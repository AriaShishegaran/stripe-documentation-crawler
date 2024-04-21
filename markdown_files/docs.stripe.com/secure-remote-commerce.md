htmlSecure Remote Commerce program guide | Stripe Documentation[Skip to content](#main-content)Secure Remote Commerce[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fsecure-remote-commerce)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fsecure-remote-commerce)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Wallets](/docs/payments/wallets)# Secure Remote Commerce program guide

Accept payments via Secure Remote Commerce in your existing Stripe integration.Secure Remote Commerce (SRC) is an easy and secure way to pay online and is powered by the global payments industry to protect users’ payment information. Users can add cards from Visa, Mastercard, American Express, and Discover to enable Click to Pay simply and securely. Secure Remote Commerce delivers an enhanced online checkout experience and supports all network brands participating in SRC.

WarningSecure Remote Commerce is only available in the US at this time.

## Integrating the Secure Remote Commerce button

### Need to upgrade?

If you are currently using Visa Checkout or Masterpass to accept payments, we recommend migrating these integrations to SRC, which delivers a unified checkout experience that supports a number of card brands.

To get started, generate your Masterpass Checkout ID in the Dashboard and configure your sandbox and production callback URLs. Note that Mastercard is offering SRC as an update to their Masterpass service, so you will see references to Masterpass within the documentation and code.

To use SRC on your website, add the following script tag to your HTML document:

SandboxProduction`<script type="text/javascript" src="https://sandbox.src.mastercard.com/srci/integration/merchant.js?locale=en_us&checkoutid={checkoutId}"></script>`ParameterDescription`locale`The country (and language) of the merchant.`en_US`is currently the only valid value as SRC is only available to US merchants.`checkoutid`The Checkout ID from Mastercard, copied from the Masterpass section of the[Dashboard](https://dashboard.stripe.com/account/payments/settings)To display the Masterpass button, use one of the following images:

For a button with black Masterpass text

`<img id="mpbutton" src="https://src.mastercard.com/assets/img/acc/global/src_mark_hor_blk.svg?locale=en_us&paymentmethod={acceptedCardBrands}&checkoutid={checkoutId}"/>`For a button with white Masterpass text

`<img id="mpbutton" src="https://src.mastercard.com/assets/img/acc/global/src_mark_hor_blk.svg?locale=en_us&paymentmethod={acceptedCardBrands}&checkoutid={checkoutId}"/>`ParameterDescription`locale`The country (and language) of the merchant.`en_US`is currently the only valid value as SRC is only available to US merchants.`paymentmethod`The list of accepted card brands, comma separated (for example: “master,amex,visa,diners,discover,jcb,maestro”).`checkoutid`The Checkout ID from Mastercard, copied from the Masterpass section of the[Dashboard](https://dashboard.stripe.com/account/payments/settings)Attach a click handler to the image and use it to invoke the masterpass.checkout function with the desired parameters:

`const button = document.getElementById('mpbutton');

button.addEventListener('click', (ev) =>
  masterpass.checkout({
    checkoutId: '{{MASTERPASS_CHECKOUT_ID}}',
    allowedCardTypes: ['master', 'amex', 'visa'],
    amount: '10.00',
    currency: 'USD',
    cartId: '{{UNIQUE_ID}}',
    callbackUrl: '{{CALLBACK_URL}}'
  }));`The masterpass.checkout function requires the following parameters:

ParameterDescription`checkoutId`The Checkout ID for your Masterpass project, copied from the[Dashboard](https://dashboard.stripe.com/account/payments/settings)`allowedCardTypes`A list of the Masterpass-compatible payment providers that you want to support`amount`The amount of the transaction, expressed in decimal format`currency`The currency to use for the transaction`cartId`A unique string that you generate to identify the purchase`callbackUrl`You can use this optional parameter to override the default callbackUrl configured when activating Masterpass.For more details about the masterpass.checkout function and the parameters that it accepts, refer to Mastercard’s documentation.

## Completing the payment

When the user clicks the Masterpass button on your checkout page, it takes them to the Masterpass website where they can select an existing payment method from their account or input a new one. When the user completes the process, Masterpass redirects them to the callback URL that you configured when activating Masterpass, or to the specified callback URL when invoking masterpass.checkout function. It appends an oauth_verifier URL query parameter that your application can use to complete the transaction.

In the route handler for the redirect destination, extract the URL query parameter and use it to confirm the PaymentIntent that you have created at the beginning of the checkout flow. See accept a payment to learn how to manage your checkout flow using Payment Intents.

The following code example demonstrates how to confirm a PaymentIntent with SRC in Node.js with the Express framework:

`app.get('/callback', async (req, res) => {
  // retrieve the PaymentIntent ID created at the beginning of the checkout flow.
  const payment_intent_id = '{{PAYMENT_INTENT_ID}}';

  const payment_intent = await stripe.paymentIntents.confirm(payment_intent_id, {
    amount: 1000,
    currency: 'usd',
    payment_method_data: {
      type: 'card',
      card: {
        masterpass: {
          cart_id: '{{UNIQUE_ID}}',
          transaction_id: req.query.oauth_verifier,
        },
      },
    },
  });

  res.send('<h1>Charge succeeded</h1>');
});`## Testing Secure Remote Commerce

To test your SRC integration against Mastercard’s sandbox, create a new SRC user account during the checkout process on your website. Configure the account to use one of the test cards from the Masterpass documentation. Complete the checkout process as normal, selecting the test card as your payment method. If everything works correctly, Mastercard redirects you back to your application, which creates the charge as expected.

The SRC integration only works correctly when included on an http or https page. Serving from the filesystem is not supported, even during testing.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Integrating the Secure Remote Commerce button](#integrating)[Completing the payment](#completing-the-payment)[Testing Secure Remote Commerce](#testing-secure-remote-commerce)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`