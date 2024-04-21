htmlCollect tips | Stripe Documentation[Skip to content](#main-content)Collect tips[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Fcollecting-tips%2Foverview)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Fcollecting-tips%2Foverview)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)# Collect tips

Learn about the different ways you can collect tips from customers.Use Terminal to collect tips from your customer before or after authorizing a payment. You can collect voluntary tips in two ways:

- [On-receipt tipping](/terminal/features/collecting-tips/on-receipt): Tips are collected when the payment is captured. This method is most commonly used when collecting tips on printed paper receipts.
- [On-reader tipping](/terminal/features/collecting-tips/on-reader): The card reader suggests tips to customers before collecting payment.

For mandatory tips, you must include the tip amount in the original PaymentIntent amount. You can’t use on-receipt or on-reader tipping.

## On-receipt versus on-reader tipping

The table below outlines some differences between on-receipt tipping and on-reader tipping.

On-reader tippingOn-receipt tippingCountry

BBPOS WisePad 3: Beta

Available in:Stripe Reader S700 Beta and BBPOS WisePOS E:

Available in:Reader

BBPOS WisePad 3

BBPOS WisePOS E

Stripe Reader S700

Any

Integrations/SDKs

BBPOS WisePad 3:

- Android SDK
- iOS SDK
- React Native SDK

BBPOS WisePOS E and Stripe Reader S700:

- All SDKs (JS, iOS, Android, React Native), server-driven

All SDKs (JS, iOS, Android, React Native), server-driven

Merchant categoryAnyRestrictedCard brandAnyVisa, Mastercard, American Express, DiscoverTipping limit[Maximum charge amount](/currencies#minimum-and-maximum-charge-amounts)for the total amount inclusive of the tip, which is eight or nine digits depending on the currency[Maximum charge amount](/currencies#minimum-and-maximum-charge-amounts)for the total amount inclusive of the tipCustomer experienceTips suggested on the readerTips set with custom integration on the point of sale or on a paper receiptCustomer credit card statementShows the payment amount inclusive of the tip, without waiting for settlementShows an initial pending authorization that’s later updated to reflect the initial amount inclusive of the tip## How tips are displayed on-receipt or on-reader

On-receipt and on-reader tipping use the PaymentIntents API, work with all Terminal SDKs (JavaScript, iOS, Android, React Native) and server-driven integrations, and require manual capture.

CautionChoose only one tipping method per PaymentIntent. If you use on-reader tipping, you can’t use the same PaymentIntent for on-receipt tipping.

The table below summarizes the specific API behavior.

On-reader tippingOn-receipt tippingTips in the API requestThe reader automatically adds the customer-selected tip when processing a payment.You add the tip amount and pass the total[amount_to_capture](/api/payment_intents/capture#capture_payment_intent-amount_to_capture)when[capturing a PaymentIntent](/api/payment_intents/capture). The`amount_to_capture`field is inclusive of the tip.Tips and API response amountThe[amount_details](/api/payment_intents/object#payment_intent_object-amount_details)object appears in the API response when processing a payment. The tip amount is returned in the`amount_details`object.Tips aren’t directly represented but can be derived from the[Charge](/api/charges/object)object. The`amount`in the`PaymentIntent`capture response is inclusive of the tip.Tips in the underlying Charge object

Tips aren’t directly represented in the Charge object.

After capture, the fields below all show the same value inclusive of the tip.

- [amount](/api/payment_intents/create#create_payment_intent-amount)
- [amount_authorized](/api/charges/object#charge_object-payment_method_details-card_present-amount_authorized)
- [amount_captured](/api/charges/object#charge_object-amount_captured)

Tips can be derived from the Charge object. You can derive the tip by subtracting amount_authorized from amount.

- `amount_authorized`is the original authorized amount exclusive of the tip.
- `amount_captured`and`amount`are the same and both are inclusive of the tip.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[On-receipt versus on-reader tipping](#on-receipt-versus-on-reader-tipping)[How tips are displayed](#how-tips-are-displayed-on-receipt-or-on-reader)Products Used[Terminal](/terminal)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`