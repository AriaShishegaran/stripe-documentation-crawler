htmlMigrate your basic card integration | Stripe Documentation[Skip to content](#main-content)Upgrade to handle authentication[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-intents%2Fupgrade-to-handle-actions)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-intents%2Fupgrade-to-handle-actions)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)
[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[More payment scenarios](/docs/payments/more-payment-scenarios)[US and Canadian cards](/docs/payments/without-card-authentication)# Migrate your basic card integration

Migrate to an integration that can handle bank requests for card authentication.WebiOSAndroidReact NativeIf you followed the Card payments without bank authentication guide, your integration creates payments that decline when a bank asks the customer to authenticate the purchase.

If you start seeing many failed payments like the one in the Dashboard below or with an error code of requires_action_not_handled in the API, upgrade your basic integration to handle, rather than decline, these payments.

![Dashboard showing a failed payment that says that this bank required authentication for this payment](https://b.stripecdn.com/docs-statics-srv/assets/failed-payment-dashboard.9e22ec31f3c7063665911e26e389c5dc.png)

Use this guide to learn how to upgrade the integration you built in the previous guide to add server and client code that prompts the customer to authenticate the payment by displaying a modal.

NoteSee a full sample of this integration on GitHub.

[Check if the payment requires authenticationServer-side](#update-server)Make two changes to the endpoint on your server that creates the PaymentIntent:

1. Removethe[error_on_requires_action](/api/payment_intents/create#create_payment_intent-error_on_requires_action)parameter to no longer fail payments that require authentication. Instead, the PaymentIntent status changes to`requires_action`.
2. Addthe`confirmation_method`parameter to indicate that you want to explicitly (manually) confirm the payment again on the server after handling authentication requests.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d amount=1099 \
  -d currency=usd \
  -d payment_method_types[]=card \
  -d confirm=true \
  -d error_on_requires_action=true \
  -d payment_method="{{PAYMENT_METHOD_ID}}" \
  -d confirmation_method=manual`Then update your “generate response” function to handle the requires_action state instead of erroring:

Command Line[curl](#)`# If the request succeeds, check the
# PaymentIntent's `status` and handle
# its `next_action`.`[Ask the customer to authenticateClient-side](#update-client)Next, update your client-side code to tell Stripe to show a modal if the customer needs to authenticate.

Use stripe.handleCardAction when a PaymentIntent has a status of requires_action. If successful, the PaymentIntent will have a status of requires_confirmation and you need to confirm the PaymentIntent again on your server to finish the payment.

`const handleServerResponse = async (responseJson) => {
  if (responseJson.error) {
    // Show error from server on payment form
  } else if (responseJson.requiresAction) {
    // Use Stripe.js to handle the required card action
    const { error: errorAction, paymentIntent } =
      await stripe.handleCardAction(responseJson.clientSecret);

    if (errorAction) {
      // Show error from Stripe.js in payment form
    } else {
      // The card action has been handled
      // The PaymentIntent can be confirmed again on the server
      const serverResponse = await fetch('/pay', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ payment_intent_id: paymentIntent.id })
      });
      handleServerResponse(await serverResponse.json());
    }
  } else {
    // Show success message
  }
}`[Confirm the PaymentIntent againServer-side](#update-server-second-confirm)Using the same endpoint you set up earlier, confirm the PaymentIntent again to finalize the payment and fulfill the order. The payment attempt fails and transitions back to requires_payment_method if it is not confirmed again within one hour.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/confirm \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -X "POST"`[Test the integration](#test-manual)Use our test cards in test mode to verify that your integration was properly updated. Stripe displays a fake authentication page inside the modal in test mode that lets you simulate a successful or failed authentication attempt. In live mode the bank controls the UI of what is displayed inside the modal.

NumberDescription4242424242424242Succeeds and immediately processes the payment.4000000000009995Always fails with a decline code of`insufficient_funds`.4000002500003155Requires authentication, which in this integration will fail with a decline code of`authentication_not_handled`.Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Check if the payment requires authentication](#update-server)[Ask the customer to authenticate](#update-client)[Confirm the PaymentIntent again](#update-server-second-confirm)[Test the integration](#test-manual)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`