htmlConnect platforms using the Payment Methods API | Stripe Documentation[Skip to content](#main-content)Connect platforms using the Payment Methods API[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-methods%2Fconnect)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-methods%2Fconnect)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Connect platforms using the Payment Methods API

Considerations for Stripe Connect platforms adding support for new payment methods using the Payment Methods API.Connect platform owners can make use of additional payment methods supported with the Payment Methods API. To learn more about creating payments for connected users, and which approach is best for you, refer to our Connect payments and fees documentation.

You can use the Payment Methods API with Connect in a number of ways if you opt for direct charges.

## Using the Payment Method API with direct charges

Direct charges require creating PaymentMethods on connected accounts. With any of these methods, you must first enable the payment method you intend to use on the connected account.

### Create and attach a PaymentMethod when confirming a PaymentIntent

The recommended way to use the Payment Method API with Connect is to save the payment method details during Payment Intent confirmation. For more information about this process, see Save a card during payment.

With Stripe.js, initialize the Stripe object and set stripeAccount to the connected account’s ID and use the setup_future_usage option when confirming the PaymentIntent. This automatically saves the payment information to the customer for reuse with future charges with that connected account.

See PaymentIntents with Stripe.js for more details about confirming each type of payment method.

`var stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY', {
  stripeAccount: '{{CONNECTED_ACCOUNT_ID}}',
});

(async () => {
  const {paymentIntent, error} = await stripe.confirmCardPayment(
    '{{PAYMENT_INTENT_CLIENT_SECRET}}',
    {
      payment_method: {
        card: card,
        billing_details: {
          name: 'Jenny Rosen'
        }
      },
      setup_future_usage: 'off_session',
    }
  );
})();`If you’re confirming PaymentIntents from the server, you can make use of authentication using the Stripe-Account header with any of our supported libraries. See Confirm a PaymentIntent for additional details.

### Creating PaymentMethods directly on the connected account

You may also create a PaymentMethod directly on a connected account with createPaymentMethod. With Stripe.js, initialize the Stripe object and set stripeAccount to the connected account’s ID.

`// Set the connected Stripe Account on which the PaymentMethod should be created
const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY', {
  stripeAccount: '{{CONNECTED_ACCOUNT_ID}}',
});

(async () => {
  const {paymentMethod, error} = await stripe.createPaymentMethod({
    type: 'card',
    card: cardElement,
    billing_details: {
      name: 'Jenny Rosen',
    },
  });

  // Handle error or paymentMethod
})();`If you’re creating PaymentMethods from the server, you can make use of authentication using the Stripe-Account header with any of our supported libraries.

### Cloning PaymentMethods

You can also create PaymentMethods on your platform and clone them to a connected account to create direct charges. Cloning is currently supported for PaymentMethods which have type set to either card or us_bank_account.

After you create a PaymentMethod and attach it to a Customer, you can clone that PaymentMethod on a connected account using the connected account’s ID as the Stripe-Account header. Read more about the Payment Methods API.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_methods \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d customer={{CUSTOMER_ID}} \
  -d payment_method={{PAYMENT_METHOD_ID}} \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"`If you want to reuse PaymentMethods on a connected account, attach them to Customers before using them with PaymentIntents to create charges. You must provide the Customer ID in the request when cloning PaymentMethods that are attached to Customers for security purposes.

It is possible to clone PaymentMethods to connected accounts without previously attaching them to Customers. However, note that the original PaymentMethod will be consumed, since PaymentMethods that aren’t attached to Customers can only be used once.

## See also

- [Payment Methods API overview](/payments/payment-methods)
- [Stripe.js Payment Intents](/js/payment_intents)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Using the Payment Method API with direct charges](#using-the-payment-method-api-with-direct-charges)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`