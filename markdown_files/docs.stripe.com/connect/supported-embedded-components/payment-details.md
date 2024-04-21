htmlPayment details | Stripe Documentation[Skip to content](#main-content)Payment details[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fpayment-details)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fpayment-details)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Supported Connect embedded components](/docs/connect/supported-embedded-components)# Payment details

Show details of a given payment and allow users to manage disputes and perform refunds.This component is a subset of payments, which provides the detail overlay of a given payment. The UI rendered by the payment details component is equivalent to the overlay that the payments component renders when the user clicks on a payment row.

Use the payment-details component to invoke the payment details overlay without the need to inline the entirety of the payments list in your website. This allows you to invoke the payment detail overlay from your existing UI (for example, your payments list) and integrate with our detail view to enable your customers to view payment details, issue refunds, and manage disputed payments.

By default, the embedded components offer limited information for destination charges and separate charges and transfers. They don’t provide access to customer information, payment methods, and some charge amount details. The destination_on_behalf_of_charge_management feature allows a connected account to see additional information with destination charges, as well as perform refunds and manage disputes.

When creating an Account Session, enable payment details by specifying payment_details in the components parameter. You can turn on or off an individual feature of the payment details component by specifying the features parameter under payment_details:

Command Line[curl](#)`curl https://api.stripe.com/v1/account_sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d account={{CONNECTED_ACCOUNT_ID}} \
  -d "components[payment_details][enabled]"=true \
  -d "components[payment_details][features][refund_management]"=true \
  -d "components[payment_details][features][dispute_management]"=true \
  -d "components[payment_details][features][capture_payments]"=true \
  -d "components[payment_details][features][destination_on_behalf_of_charge_management]"=false`After creating the account session and initializing ConnectJS, you can render the payment details component in the frontend:

payment-details.js[JavaScript](#)`// Include this element in your HTML
const paymentDetails = stripeConnectInstance.create('payment-details');
paymentDetails.setPayment('{{PAYMENT_OR_PAYMENT_INTENT_ID}}');
// use setOnClose to set a callback function to close payment-details
paymentDetails.setOnClose(() => {
  paymentDetails.remove();
});
container.appendChild(paymentDetails);`NoteFor destination charges and separate charges and transfers, the connected accounts don’t own the payment intent objects associated with the charges. Pass in the ID of the payment object that belongs to the connected account for these charges.

The payment details component shows different information and supports different features for different charge types:

- For direct charges, your connected accounts can view the complete set of information. They can also manage refunds, manage disputes, and capture payments if you enable the corresponding features when creating an account session.
- For[destination charges](/connect/destination-charges)and[separate charges and transfers](/connect/separate-charges-and-transfers), your connected accounts can only see the transfer object associated with the selected charge, which contains limited information.
- For destination charges with the[on_behalf_of](/api/payment_intents/object#payment_intent_object-on_behalf_of)attribute, your connected accounts can view the complete set of information when the`destination_on_behalf_of_charge_management`feature is enabled. When this feature is turned on, you can also enable refund and disputes management by enabling the corresponding features.

### Allow your connected accounts to manage destination charges

When you set the destination_on_behalf_of_charge_management feature to true, your connected accounts can use the payments component to view and manage destination charges that have the on_behalf_of attribute. If you also turn on the dispute_management feature, your connected accounts can participate directly in handling their disputes.

Enabling the destination_on_behalf_of_charge_management feature has the following limitations:

1. You can’t filter by charge status or payment methods.
2. You can’t export certain data columns.

### Dispute management for destination charges

When a dispute occurs on destination charges or separate charges and transfers, the platform is debited the disputed amount and a dispute fee. Connect embedded components don’t reverse the transfer to the connected account regardless of the Account Session features. We recommend setting up webhooks to listen to dispute events. When a dispute is created, you can create an account debit or a transfer reversal on the transfer to your connected account. You can also reverse the transfer to your connected account through the Dashboard. When a dispute is closed, you can then update the balance on your connected account depending on the result of the dispute. If your connected account won the dispute, you can create a transfer to reverse the effect of the account debit or transfer reversal.

When both dispute_management and destination_on_behalf_of_charge_management are enabled, the connected accounts can update and modify dispute evidence, counter disputes, and accept disputes for destination charges with the on_behalf_of attribute set to them.

### Supported parameters

This embedded component supports the following parameters:

HTML + JSReactMethodTypeDescription`setPayment``string`The ID of the payment, charge, or PaymentIntent that displays in the overlay. This should be an ID of the payment, charge, or PaymentIntent on the connected account. If this attribute isn’t defined, the embedded component renders nothing. To obtain this ID, query the[charges API](/api/charges)or use a payment ID that you’ve created or stored in your integration.required`setOnClose``() => void`We send this event when the user closes the overlay.To enable the dismiss behavior of this component, listen to the close event by calling setOnClose.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`