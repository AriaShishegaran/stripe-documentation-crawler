htmlManage payment methods in the Dashboard by default | Stripe Documentation[Skip to content](#main-content)Manage payment methods in the Dashboard by default[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fupgrades%2Fmanage-payment-methods)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fupgrades%2Fmanage-payment-methods)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)
[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)API[API upgrades](/docs/upgrades)# Manage payment methods in the Dashboard by default

Upgrade your API to manage payment methods in the Dashboard by default.On August 16, 2023, Stripe updated the selection process for default payment methods that apply to PaymentIntents and SetupIntents created with the /v1/payment_intents and /v1/setup_intents APIs.

In prior versions of the Stripe API, if you didn’t specify a payment_method_types parameter during the creation request, Stripe would default to using the card payment method for both PaymentIntents and SetupIntents.

Moving forward, Stripe applies eligible payment methods that you manage from your Dashboard to your PaymentIntents and SetupIntents by default if you don’t specify the payment_method_types parameter in the creation request.

To see how your payment methods appear to customers, enter a transaction ID or set an order amount and currency in the Dashboard.

## Update your payment flows

Choose from the upgrade path that matches your current Stripe integration:

ElementsCheckout and Payment LinksAPIIf your integration uses Card Element or individual payment method Elements, we recommend migrating to the Payment Element. This single, unified integration allows you to accept over 25 different payment methods.

### Create the PaymentIntent

In this version of the API, specifying the automatic_payment_methods.enabled parameter is optional. If you don’t specify it, Stripe assumes a value of true, which enables its functionality by default.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1099 \
  -d currency=usd`### Client-side confirmations with Stripe.js

If your integration uses Stripe.js to confirm payments with confirmPayment or by payment method, your existing processes remains the same and requires no further changes.

When you confirm payments, we recommend that you provide the return_url parameter. This allows you to accept payment methods that require redirect.

HTML + JSReactcheckout.js`const form = document.getElementById('payment-form');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const {error} = await stripe.confirmPayment({
    //`Elements` instance that was used to create the Payment Element
    elements,
    confirmParams: {
      return_url: 'https://example.com/return_url',
    },
  });

  if (error) {
    // This point will only be reached if there is an immediate error when
    // confirming the payment. Show error to your customer (for example, payment
    // details incomplete)
    const messageContainer = document.querySelector('#error-message');
    messageContainer.textContent = error.message;
  } else {
    // Your customer will be redirected to your `return_url`. For some payment
    // methods like iDEAL, your customer will be redirected to an intermediate
    // site first to authorize the payment, then redirected to the `return_url`.
  }
});`### Server-side confirmation

If you use server-side confirmation, you must use the return_url parameter in your integration.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1099 \
  -d currency=usd \
  -d confirm=true \
  -d payment_method={{PAYMENT_METHOD_ID}} \
  --data-urlencode return_url="https://example.com/return_url"`Alternatively, you can create the PaymentIntent or SetupIntent with the automatic_payment_methods.allow_redirects parameter set to never. This disables the return_url requirement on confirmation. You can still manage payment methods from the Dashboard, but the payment methods that require redirects won’t be eligible.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1099 \
  -d currency=usd \
  -d confirm=true \
  -d payment_method={{PAYMENT_METHOD_ID}} \
  -d "automatic_payment_methods[enabled]"=true \
  -d "automatic_payment_methods[allow_redirects]"=never`Lastly, you can create the PaymentIntent or SetupIntent with the payment_method_types parameter. This also disables the return_url requirement on confirmation. With this option, you can’t manage payment methods from the Dashboard.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1099 \
  -d currency=usd \
  -d confirm=true \
  -d payment_method={{PAYMENT_METHOD_ID}} \
  -d "payment_method_types[]"=card`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`