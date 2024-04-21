htmlPayments | Stripe Documentation[Skip to content](#main-content)Payments[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fpayments)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fpayments)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Supported Connect embedded components](/docs/connect/supported-embedded-components)# Payments

Show a list of payments with export, refund, and dispute capabilities.Renders a transaction list for direct charges, destination charges, and separate charges and transfers on the connected account.

By default, the embedded components offer limited information for destination charges and separate charges and transfers. They don’t provide access to customer information, payment methods, and some charge amount details. The destination_on_behalf_of_charge_management feature allows a connected account to see additional information with destination charges, as well as perform refunds and manage disputes.

## Creating an Account Session

When creating an Account Session, enable the payments embedded component by specifying payments in the components parameter. You can turn on or off an individual feature of the payments component by specifying the features parameter under payments:

Command Line[curl](#)`curl https://api.stripe.com/v1/account_sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d account={{CONNECTED_ACCOUNT_ID}} \
  -d "components[payments][enabled]"=true \
  -d "components[payments][features][refund_management]"=true \
  -d "components[payments][features][dispute_management]"=true \
  -d "components[payments][features][capture_payments]"=true \
  -d "components[payments][features][destination_on_behalf_of_charge_management]"=false`The payments component shows different information and supports different features for different charge types:

- For direct charges, your connected accounts can view the complete set of information. They can also manage refunds, manage disputes, and capture payments if you enable the corresponding features when creating an account session.
- For[destination charges](/connect/destination-charges)and[separate charges and transfers](/connect/separate-charges-and-transfers), your connected accounts can only see the transfer object associated with the selected charge, which contains limited information.
- For destination charges with the[on_behalf_of](/api/payment_intents/object#payment_intent_object-on_behalf_of)attribute, your connected accounts can view the complete set of information when the`destination_on_behalf_of_charge_management`feature is enabled. When this feature is turned on, you can also enable refund and disputes management by enabling the corresponding features.

### Allow your connected accounts to manage destination charges

When you set the destination_on_behalf_of_charge_management feature to true, your connected accounts can use the payments component to view and manage destination charges that have the on_behalf_of attribute. If you also turn on the dispute_management feature, your connected accounts can participate directly in handling their disputes.

Enabling the destination_on_behalf_of_charge_management feature has the following limitations:

1. You can’t filter by charge status or payment methods.
2. You can’t export certain data columns.

## Rendering the payments component

After creating the account session and initializing ConnectJS, you can render the payments component in the front end:

payments.js[JavaScript](#)`// Include this element in your HTML
const payments = stripeConnectInstance.create('payments');
container.appendChild(payments);`## Dispute management for destination charges

When a dispute occurs on destination charges or separate charges and transfers, the platform is debited the disputed amount and a dispute fee. Connect embedded components don’t reverse the transfer to the connected account regardless of the Account Session features. We recommend setting up webhooks to listen to dispute events. When a dispute is created, you can create an account debit or a transfer reversal on the transfer to your connected account. You can also reverse the transfer to your connected account through the Dashboard. When a dispute is closed, you can then update the balance on your connected account depending on the result of the dispute. If your connected account won the dispute, you can create a transfer to reverse the effect of the account debit or transfer reversal.

When both dispute_management and destination_on_behalf_of_charge_management are enabled, the connected accounts can update and modify dispute evidence, counter disputes, and accept disputes for destination charges with the on_behalf_of attribute set to them.

## Customizing description

To display a custom description within the payment component for destination charges and separate charges and transfers, follow these steps:

### Destination charges

To update the description on a payment object that’s visible to your platform’s users, you need to use the Stripe API. This applies to all platforms that use destination charges.

1. Find the existing transfer object you created for an account by finding the latest[charge](/api/payment_intents/object#payment_intent_object-charges)created on the[PaymentIntent](/api/payment_intents/object).
2. Use the charge object to find the[transfer](/api/charges/object#charge_object-transfer)object associated with the charge.
3. Use the transfer object to find the[destination_payment](/api/transfers/object#transfer_object-destination_payment)ID that exists on the transfer.
4. Call the[Update Charge](/api/charges/update)API to update the[description](/api/charges/update#update_charge-description)on the destination payment using the`destination_payment`ID.

NoteThe destination_payment object belongs to the connected account, so you’ll need to set the Stripe-Account header to the connected account’s ID to make this call.

Command Line[curl](#)`curl https://api.stripe.com/v1/charges/{{PAYMENT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d description="My custom description"`This description becomes visible on the charge after you’ve written this field.

Learn more about creating destination charges on your platform.

### Separate charges and transfers

To update the description on a payment object that’s visible to your platform’s users, you need to use the Stripe API. This applies to platforms that use separate charges and transfers.

1. Use the transfer object to find the[destination_payment](/api/transfers/object#transfer_object-destination_payment)ID that exists on the transfer.
2. Call the[Update Charge](/api/charges/update)API to update the[description](/api/charges/update#update_charge-description)on the destination payment using the`destination_payment`ID found in the previous step.

NoteThe destination_payment object belongs to the connected account, so you’ll need to set the Stripe-Account header to the connected account’s ID to make this call.

Command Line[curl](#)`curl https://api.stripe.com/v1/charges/{{PAYMENT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d description="My custom description"`This description becomes visible on the charge after you’ve written this field.

Learn more about creating separate charges and transfers.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Creating an Account Session](#creating-an-account-session)[Rendering the payments component](#rendering-the-payments-component)[Dispute management for destination charges](#dispute-management-for-destination-charges)[Customizing description](#customizing-description)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`