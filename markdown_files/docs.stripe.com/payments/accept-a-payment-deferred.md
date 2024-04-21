htmlCollect payment details before creating an Intent | Stripe Documentation[Skip to content](#main-content)Collect payment details before creating an Intent[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Faccept-a-payment-deferred)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Faccept-a-payment-deferred)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)
[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[More payment scenarios](/docs/payments/more-payment-scenarios)# Collect payment details before creating an Intent

Build an integration where you can render the Payment Element prior to creating a PaymentIntent or SetupIntent.WebiOSAndroidReact NativeAccept a paymentSet up a payment methodCreate a subscriptionThe Payment Element allows you to accept multiple payment methods using a single integration. In this integration, learn how to build a custom payment flow where you render the Payment Element, create the PaymentIntent, and confirm the payment from the buyer’s browser. If you prefer to confirm the payment from the server instead, see Finalize payments on the server.

[Set up StripeServer-side](#set-up-stripe)First, create a Stripe account or sign in.

Use our official libraries to access the Stripe API from your application:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`[Enable payment methods](#enable-payment-methods)CautionStripe doesn’t currently support BLIK for this integration path.

View your payment methods settings and enable the payment methods you want to support. You need at least one payment method enabled to create a PaymentIntent.

By default, Stripe enables cards and other prevalent payment methods that can help you reach more customers, but we recommend turning on additional payment methods that are relevant for your business and customers. See Payment method integration options for product and payment method support, and our pricing page for fees.

[Collect payment detailsClient-side](#web-collect-payment-details)You’re ready to collect payment details on the client with the Payment Element. The Payment Element is a prebuilt UI component that simplifies collecting payment details for a variety of payment methods.

The Payment Element contains an iframe that securely sends payment information to Stripe over an HTTPS connection. Avoid placing the Payment Element within another iframe because some payment methods require redirecting to another page for payment confirmation.

The checkout page address must start with https:// rather than http:// for your integration to work. You can test your integration without using HTTPS, but remember to enable it when you’re ready to accept live payments.

HTML + JSReact### Set up Stripe.js

The Payment Element is automatically available as a feature of Stripe.js. Include the Stripe.js script on your checkout page by adding it to the head of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

checkout.html`<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/v3/"></script>
</head>`Create an instance of Stripe with the following JavaScript on your checkout page:

checkout.js`// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');`### Add the Payment Element to your checkout page

The Payment Element needs a place to live on your checkout page. Create an empty DOM node (container) with a unique ID in your payment form:

checkout.html`<form id="payment-form">
  <div id="payment-element">
    <!-- Elements will create form elements here -->
  </div>
  <button id="submit">Submit</button>
  <div id="error-message">
    <!-- Display error message to your customers here -->
  </div>
</form>`When the form above has loaded, create an Elements instance with the mode, amount, and currency. These values determine which payment methods are shown to your customer.

Then, create an instance of the Payment Element and mount it to the container DOM node.

checkout.js`const options = {
  mode: 'payment',
  amount: 1099,
  currency: 'usd',
  // Fully customizable with appearance API.
  appearance: {/*...*/},
};

// Set up Stripe.js and Elements to use in checkout form
const elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElement = elements.create('payment');
paymentElement.mount('#payment-element');`The Payment Element renders a dynamic form that allows your customer to pick a payment method. The form automatically collects all necessary payments details for the payment method selected by the customer.

You can customize the Payment Element to match the design of your site by passing the appearance object into options when creating the Elements provider.

### Collect addresses

By default, the Payment Element only collects the necessary billing address details. To collect a customer’s full billing address (to calculate the tax for digital goods and services, for example) or shipping address, use the Address Element.

[OptionalCustomize the layoutClient-side](#customize-layout)[OptionalCustomize the appearanceClient-side](#customize-appearance)[OptionalDynamically update payment detailsClient-side](#dynamic-updates)[OptionalAdditional elements optionsClient-side](#additional-options)[OptionalCreate a ConfirmationToken](#create-ct)[Create a PaymentIntentServer-side](#create-intent)Run custom business logic immediately before payment confirmationNavigate to step 5 in the finalize payments guide to run your custom business logic immediately before payment confirmation. Otherwise, follow the steps below for a simpler integration, which uses stripe.confirmPayment on the client to both confirm the payment and handle any next actions.

When the customer submits your payment form, use a PaymentIntent to facilitate the confirmation and payment process. Create a PaymentIntent on your server with an amount and currency enabled. In the latest version of the API, specifying the automatic_payment_methods parameter is optional because Stripe enables its functionality by default. You can manage payment methods from the Dashboard. Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow. To prevent malicious customers from choosing their own prices, always decide how much to charge on the server-side (a trusted environment) and not the client.

Included on a PaymentIntent is a client secret. Return this value to your client for Stripe.js to use to securely complete the payment process.

main.rb[Ruby](#)`require 'stripe'
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

post '/create-intent' do
  intent = Stripe::PaymentIntent.create({
    # In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
    automatic_payment_methods: {enabled: true},
    amount: 1099,
    currency: 'usd',
  })
  {client_secret: intent.client_secret}.to_json
end`[Submit the payment to StripeClient-side](#submit-the-payment)Use stripe.confirmPayment to complete the payment using details from the Payment Element.

Provide a return_url to this function to indicate where Stripe should redirect the user after they complete the payment. Your user might be initially redirected to an intermediate site, like a bank authorization page, before being redirected to the return_url. Card payments immediately redirect to the return_url when a payment is successful.

If you don’t want to redirect for card payments after payment completion, you can set redirect to if_required. This only redirects customers that check out with redirect-based payment methods.

HTML + JSReactcheckout.js`const form = document.getElementById('payment-form');
const submitBtn = document.getElementById('submit');

const handleError = (error) => {
  const messageContainer = document.querySelector('#error-message');
  messageContainer.textContent = error.message;
  submitBtn.disabled = false;
}

form.addEventListener('submit', async (event) => {
  // We don't want to let default form submission happen here,
  // which would refresh the page.
  event.preventDefault();

  // Prevent multiple form submissions
  if (submitBtn.disabled) {
    return;
  }

  // Disable form submission while loading
  submitBtn.disabled = true;

  // Trigger form validation and wallet collection
  const {error: submitError} = await elements.submit();
  if (submitError) {
    handleError(submitError);
    return;
  }

  // Create the PaymentIntent and obtain clientSecret
  const res = await fetch("/create-intent", {
    method: "POST",
  });

  const {client_secret: clientSecret} = await res.json();

  // Confirm the PaymentIntent using the details collected by the Payment Element
  const {error} = await stripe.confirmPayment({
    elements,
    clientSecret,
    confirmParams: {
      return_url: 'https://example.com/order/123/complete',
    },
  });

  if (error) {
    // This point is only reached if there's an immediate error when
    // confirming the payment. Show the error to your customer (for example, payment details incomplete)
    handleError(error);
  } else {
    // Your customer is redirected to your `return_url`. For some payment
    // methods like iDEAL, your customer is redirected to an intermediate
    // site first to authorize the payment, then redirected to the `return_url`.
  }
});`[OptionalHandle post-payment events](#web-fulfillment)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up Stripe](#set-up-stripe)[Enable payment methods](#enable-payment-methods)[Collect payment details](#web-collect-payment-details)[Create a PaymentIntent](#create-intent)[Submit the payment to Stripe](#submit-the-payment)Products Used[Payments](/payments)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`