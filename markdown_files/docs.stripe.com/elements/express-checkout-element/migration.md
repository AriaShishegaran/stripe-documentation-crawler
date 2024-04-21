htmlMigrate to the Express Checkout Element | Stripe Documentation[Skip to content](#main-content)Migrate to the Express Checkout Element[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Felements%2Fexpress-checkout-element%2Fmigration)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Felements%2Fexpress-checkout-element%2Fmigration)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)
[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Elements](/payments/elements)·[Home](/docs)[Payments](/docs/payments)[Web Elements](/docs/payments/elements)[Express Checkout Element](/docs/elements/express-checkout-element)# Migrate to the Express Checkout Element

Migrate your existing integration with the Payment Request Button Element to the Express Checkout Element.The Payment Request Button Element allows you to accept card payments only through Apple Pay, Google Pay, or Link. When you migrate to the Express Checkout Element, you can accept card or wallet payments through one or more payment buttons, including PayPal. See the comparison guide for more details.

If your existing integration usesDo the following[Payment Intents](/api/payment_intents)API to create and track payments or save card details during a paymentFollow the steps in this guide to use the Express Checkout Element.[Charges](/api/charges)API with tokensMigrate to the[Payment Intents API](/payments/payment-intents/migration#web)before proceeding.[Enable payment methods](#enable-payment-methods)Enable the payment methods you want to support in your payment methods settings. You must enable at least one payment method.

By default, Stripe enables cards and other common payment methods. You can enable additional payment methods that are relevant for your business and customers. See the payment method integration options for product and payment method support and our pricing page for fees.

[Update Elements instanceClient-side](#one-time-update-elements)Next, update your client-side code to pass the mode (payment), amount, and currency. These values determine which payment methods to show to your customers.

For example, if you pass the eur currency on the PaymentIntent and enable OXXO in the Dashboard, your customer won’t see OXXO because OXXO doesn’t support eur payments.

Stripe evaluates the currency, payment method restrictions, and other parameters to determine the list of supported payment methods. We prioritize payment methods that increase conversion and are most relevant to the currency and customer location.

HTML + JSReactBeforeAfter`const stripe =
    Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');
const elements = stripe.elements();``const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');
const options = {
  mode: 'payment',
  amount: 1099,
  currency: 'usd',
};
const elements = stripe.elements(options);`[OptionalSave payment details during a payment](#one-time-save-payment-details)[Update your PaymentIntent creation callServer-side](#one-time-payment-intent)The PaymentIntent includes the payment methods shown to customers during checkout. You can manage payment methods from the Dashboard. Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -H "Stripe-Version: 2024-04-10" \
  -d "amount"=1099 \
  -d "currency"="usd" \
  -d "automatic_payment_methods[enabled]"=true \`If your existing integration supports multiple payment methods or you want to accept payment methods other than cards, you can enable more payment methods in the Dashboard.

[Add the Express Checkout ElementClient-side](#one-time-add-express-checkout-element)If you use React Stripe.js, update to the latest package to use the Express Checkout Element.

Replace the Payment Request Button Element with the Express Checkout Element. The examples below demonstrate how to replace PaymentRequestButtonElement with ExpressCheckoutElement.

You no longer need to create a paymentRequest object. Instead, pass the properties through the click event once.

HTML + JSReactBeforeAftercheckout.html`<div id="payment-request-button">
</div>`checkout.html`<div id="express-checkout-element">
  <!-- Mount the Express Checkout Element here -->
</div>`BeforeAftercheckout.js`const paymentRequest = stripe.paymentRequest({
  country: 'US',
  currency: 'usd',
  total: {
    label: 'Demo total',
    amount: 1099,
  },
  requestPayerName: true,
  requestPayerEmail: true,
});
const paymentRequestButton = elements.create('paymentRequestButton', {
  paymentRequest: paymentRequest,
});
paymentRequestButton.mount("#payment-request-button");
paymentRequest.canMakePayment().then(function(result) {
  if (result) {
    prButton.mount('#payment-request-button');
  } else {
    document.getElementById('payment-request-button').style.display = 'none';
  }
});`checkout.js`const expressCheckoutElement = elements.create("expressCheckout");
expressCheckoutElement.mount("#express-checkout-element");
expressCheckoutElement.on('click', (event) => {
  const options = {
    emailRequired: true
  };
  event.resolve(options);
});`[OptionalRequest an Apple Pay merchant token (MPAN)](#mpan)[OptionalListen to the ready event](#ready-event)[OptionalStyle the Express Checkout Element](#customize-express-checkout-element)[Update the confirm payment methodClient-side](#one-time-update-method)Listen to the confirm event to handle confirmation. To collect and submit payment information to Stripe, use stripe.confirmPayment instead of individual confirmation methods like stripe.confirmCardPayment.

Instead of a PaymentMethod ID, stripe.confirmPayment uses the Elements instance from the Express Checkout Element and the client secret from the created PaymentIntent.

When called, stripe.confirmPayment attempts to complete any required actions, such as authenticating your customers by displaying a 3DS dialog or redirecting them to a bank authorization page. After confirmation completes, users are directed to the return_url that you configured, which corresponds to a page on your website that provides the payment status.

If you want the checkout flow for card payments to redirect only for payment methods that require it, you can set redirect to if_required. This doesn’t apply to the Express Checkout Element.

The example below replaces stripe.confirmCardPayment with stripe.confirmPayment.

HTML + JSReactBeforeAfter`paymentRequest.on('paymentmethod', function(ev) {
  stripe.confirmCardPayment(
    '{{CLIENT_SECRET}}',
    {payment_method: ev.paymentMethod.id},
    {handleActions: false}
  ).then(function(confirmResult) {
    if (confirmResult.error) {
      ev.complete('fail');
    } else {
      ev.complete('success');
      if (confirmResult.paymentIntent.status === "requires_action") {
        stripe.confirmCardPayment(clientSecret).then(
          function(result) {
            if (result.error) {
              // The payment failed -- ask your customer for a new payment method.
            } else {
              // The payment succeeded.
            }
          }
        );
      } else {
        // The payment succeeded.
      }
    }
  });
});``expressCheckoutElement.on('confirm', async (event) => {
  const {error} = await stripe.confirmPayment({
    // `Elements` instance that's used to create the Express Checkout Element.
    elements,
    // `clientSecret` from the created PaymentIntent
    clientSecret,
    confirmParams: {
      return_url: 'https://example.com/order/123/complete',
    },
    // Uncomment below if you only want redirect for redirect-based payments.
    // redirect: 'if_required',
  });

  if (error) {
    // This point is reached only if there's an immediate error when confirming the payment. Show the error to your customer (for example, payment details incomplete).
  } else {
    // Your customer will be redirected to your `return_url`.
  }
});`[Handle post-payment eventsServer-side](#post-payment)Stripe sends a payment_intent.succeeded event when the payment completes. Use the Dashboard webhook tool or follow the webhook guide to receive these events and run actions, such as sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events is what enables you to accept different types of payment methods with a single integration.

In addition to handling the payment_intent.succeeded event, we recommend handling these other events when collecting payments with the Payment Element:

EventDescriptionAction[payment_intent.succeeded](/api/events/types?lang=php#event_types-payment_intent.succeeded)Sent when a customer successfully completes a payment.Send the customer an order confirmation andfulfilltheir order.[payment_intent.processing](/api/events/types?lang=php#event_types-payment_intent.processing)Sent when a customer successfully initiates a payment, but the payment has yet to complete. This event is most commonly sent when the customer initiates a bank debit. It’s followed by either a`payment_intent.succeeded`or`payment_intent.payment_failed`event in the future.Send the customer an order confirmation that indicates their payment is pending. For digital goods, you might want to fulfill the order before waiting for payment to complete.[payment_intent.payment_failed](/api/events/types?lang=php#event_types-payment_intent.payment_failed)Sent when a customer attempts a payment, but the payment fails.If a payment transitions from`processing`to`payment_failed`, offer the customer another attempt to pay.Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Enable payment methods](#enable-payment-methods)[Update Elements instance](#one-time-update-elements)[Update your PaymentIntent creation call](#one-time-payment-intent)[Add the Express Checkout Element](#one-time-add-express-checkout-element)[Update the confirm payment method](#one-time-update-method)[Handle post-payment events](#post-payment)Products Used[Payments](/payments)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`