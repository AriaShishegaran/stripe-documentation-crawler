htmlCharges versus Payment Intents APIs | Stripe Documentation[Skip to content](#main-content)Compare to Charges[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-intents%2Fmigration%2Fcharges)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-intents%2Fmigration%2Fcharges)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)
[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[About the APIs](/docs/payments-api/tour)[Payment Intents API](/docs/payments/payment-intents)# Charges versus Payment Intents APIs

Learn about the differences between Stripe's two core payment APIs and when to use them.## Understanding the Stripe payment APIs

There are three ways to accept payments on Stripe today:

- Stripe Checkout
- Charges API
- [Payment Intents API](/payments/payment-intents)

Stripe Checkout is a prebuilt payment page that you can redirect your customer to for simple purchases and subscriptions. It provides many features, such as Apple Pay, Google Pay, internationalization, and form validation.

The Charges and Payment Intents APIs let you build custom payment flows and experiences.

The Payment Intents API is the unifying API for all Stripe products and payment methods. While we are not deprecating Charges, new features are only available with the Payment Intents API.

For a full feature comparison, see the table below:

Charges APIPayment Intents APIUsed by businesses with customers primarily in the US / Canada who want a simple way to accept cards.Required for businesses that accept multiple payment methods and cards requiring authentication (for example, due to[Strong Customer Authentication](/strong-customer-authentication)in Europe).Works on Web, iOS, and Android.Works on Web, iOS, and Android. Can also be used to accept in-store payments with Terminal.Supports cards and all payment methods on the[Sources API](/sources).Supports cards, cards requiring 3DS, iDEAL, SEPA, and[many other payment methods](/payments/payment-methods/overview).Isnot SCAready[Is SCA ready](/strong-customer-authentication)## Migrating code that reads from charges

If you have an application with multiple payment flows and incrementally migrating each one from the Charges API to the Payment Intents API, you should first update any code that reads from the Charge object. To help with this, the charge object has two additional properties, payment_method_details and billing_details, which provide a consistent interface for reading the details of the payment method used for the charge.

These fields are available on all API versions and on charge objects created with both the Charges API and the Payment Intents API.

The following table shows commonly used properties on a charge and how the same information can be accessed using the additional properties:

Cards and bank accountsSourcesDescriptionBeforeAfterDetails about the payment method used to create a charge`charge.source``charge.payment_method_details`ID of the payment method used for the charge`charge.source.id``charge.payment_method`Type of payment method used`charge.source.object`(for example,`card`or`bank_account`)`charge.payment_method_details.type`Billing information for the charge (for example, billing postal code)`charge.source.address_zip``charge.billing_details.address.postal_code`Name of the cardholder`charge.source.name``charge.billing_details.name`Last 4 digits of the card used`charge.source.last4``charge.payment_method_details.card.last4`Fingerprint of the card`charge.source.fingerprint``charge.payment_method_details.card.fingerprint`CVC verification status for the charge`charge.source.cvc_check``charge.payment_method_details.card.checks.cvc_check`Card brand values`charge.source.brand`can be one of:`American Express`,`Diners Club`,`Discover`,`JCB`,`MasterCard`,`UnionPay`,`Visa``charge.payment_method_details.card.brand`can be one of:`amex`,`diners`,`discover`,`jcb`,`mastercard`,`unionpay`,`visa`Google Pay enum value`charge.source.tokenization_method`is`android_pay``card.wallet.type`within`charge.payment_method_details`is`google_pay`## See also

- [Migrate to Payment Intents](/payments/payment-intents/migration)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Understanding the Stripe payment APIs](#understanding-the-stripe-payment-apis)[Migrating code that reads from charges](#read)[See also](#see-also)Products Used[Payments](/payments)[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`