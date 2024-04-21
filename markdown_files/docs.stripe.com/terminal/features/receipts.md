htmlProvide receipts | Stripe Documentation[Skip to content](#main-content)Provide receipts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Freceipts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Freceipts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)# Provide receipts

Use Stripe to provide your customers with receipts that meet card network rules.### Receipts in test mode

Receipts for payments created using your test API keys are not sent automatically. Instead, you can view or manually send a receipt using the Dashboard.

Card network rules and local regulatory requirements are different for in-person payments. If you accept payments using Stripe Terminal, you must provide customers with the option to receive a physical or email receipt. Stripe provides everything you need to start offering receipts with your first transaction.

Receipts must contain certain fields to comply with card network rules. You can use Stripe’s prebuilt email receipts, or use receipt data from the Stripe API and your Terminal integration to generate on-brand custom receipts.

## Prebuilt email receipts

Prebuilt email receipts already include all card network-required fields. It’s the simplest way to set up compliant receipts.

### SDK Reference

- [PaymentIntentParameters (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPPaymentIntentParameters.html#/c:objc(cs)SCPPaymentIntentParameters(py)receiptEmail)
- [PaymentIntentParameters (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-payment-intent-parameters/receipt-email.html)
- [PaymentIntentParameters (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#CreatePaymentIntentParams)

If you have the customer’s email, use the receipt_email field when creating a PaymentIntent. When you provide a receipt_email, Stripe automatically emails a compliant receipt to the customer when capturing the PaymentIntent.

To trigger an automatic email receipt after the customer checks out, update the PaymentIntent’s receipt_email with the customer’s email.

For more information about automatic email receipts, see Email Receipts.

![](https://b.stripecdn.com/docs-statics-srv/assets/terminal-pre-built-receipt.64db66739eaf8f8db1f9dd61c463a322.png)

## Custom receipts

You can also customize receipts to include any design and content you want—as long as you list required information. When you accept in-person payments with EMV chip cards, card networks require you to include several fields on the receipts you provide to customers.

The Stripe API allows you to fetch necessary fields for compliance-ready receipts.

The following fields become available in the PaymentIntent object as soon as the payment is confirmed.

FieldNameRequirement`account_type`Account TypeRequired(Optional in US)`application_preferred_name`Application nameRequired`dedicated_file_name`AIDRequired`authorization_response_code`ARCOptional`application_cryptogram`Application CryptogramOptional`terminal_verification_results`TVROptional`transaction_status_information`TSIOptional### SDK Reference

- [payment_method_details](/api/charges/object#charge_object-payment_method_details-card_present-receipt)
- [ReceiptDetails (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPReceiptDetails.html)
- [ReceiptDetails (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-receipt-details/index.html)

You can access these fields server-side using the Stripe API, or client-side using the Stripe Terminal SDKs. When using the JavaScript SDK, the PaymentIntent object matches the API object.

Whether you’re emailing or printing your custom receipts for Terminal payments, be sure to include the required fields to meet card network rules.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Prebuilt email receipts](#prebuilt)[Custom receipts](#custom)Products Used[Terminal](/terminal)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`