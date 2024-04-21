htmlBuy now, pay later | Stripe Documentation[Skip to content](#main-content)Buy now, pay later[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbuy-now-pay-later)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbuy-now-pay-later)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)# Buy now, pay later

Learn about buy now, pay later methods with Stripe.### Other types of installments

You can also set up installment plans using the Subscription Schedules API. Learn more about other options for accepting payments in installments.

Buy now, pay later methods let customers pay in installments over time. You’re paid immediately and in full and your customers pay nothing or a portion of the total at purchase time. Buy now, pay later methods are often used by:

- Retailers selling high value goods and services like luxury items or travel fares that want to boost conversion.
- Retailers selling low value goods and services that want to increase average cart size and reach new customers who might not have credit cards.
- Regional banks that allow consumers to split credit card payments over multiple billing cycles.

Buy now, pay later methods might not be a good fit for your business if:

- Your customers are businesses. Buy now, pay later methods offered on Stripe are only supported for consumers.
- Your business relies on subscriptions or recurring purchases. Buy now, pay later methods don’t currently support[Invoicing](/invoicing)or[Subscriptions](/billing).

Read our Buy Now, Pay Later Guide for more information.

## Payments

At checkout, the customer chooses to pay with a buy now, pay later service. Then the customer creates or logs into an account with the buy now, pay later provider. Next, the customer accepts or declines the terms of the repayment plan, and then returns to the business’ site.

![](https://b.stripecdn.com/docs-statics-srv/assets/payment_flow.09ed159dfe639622d54b186cc7973db6.svg)

## Product support

Payment methodCustomer countryRepayment optionsTransaction limitPayment IntentsCheckoutConnectPayment ElementPayment LinksMobile Payment ElementInvoicingSubscriptions[Affirm](/payments/affirm)Canada, United States- Pay in 4 interest-free installments
- Monthly payments for up to 36 months

50 USD minimum; 30,000 USD maximum or local equivalent*[Afterpay/Clearpay](/payments/afterpay-clearpay)Australia, Canada, New Zealand, United Kingdom, United States- Pay in 4 interest-free installments
- Monthly USD payments for up to 12 months

1 USD minimum; 4,000 USD maximum or local equivalent[Apple Pay Later](/payments/apple-pay-later)United States- Pay in 4 equal, interest-free installments over 6 weeks

50 USD minimum; 1,000 USD maximum[Klarna](/payments/klarna)Australia, Austria, Belgium, Canada, Czechia, Denmark, Finland, France, Germany, Greece, Ireland, Italy, Netherlands, New Zealand, Norway, Poland, Portugal, Spain, Sweden, Switzerland, United Kingdom, United States- Pay in 3 or 4 interest-free installments
- Pay in 30 days
- Pay now with stored payment details
- Monthly payments for up to 36 months

10 USD minimum or local equivalent. (5,000 USD+ for financing possible; maximum varies by customer)[Beta](#)[Meses sin intereses](/payments/mx-installments)MexicoExtend payments over 3 to 24 months of billing cycles[Minimum transaction](/payments/mx-installments#fees)amount of 100 MXN per month of extension[Zip](/payments/zip)Australia- Zip Pay: Pay using a 1,000 AUD credit, repay in your own time
- Zip Money: Pay in a minimum of 3 monthly interest-free installments

0.01 AUD minimum. 50,000 AUD maximum**- * The maximum credit limit for Affirm is 20,000 USD or 20,000 CAD. However, Affirm supports transactions up to 30,000 USD or 30,000 CAD. These transactions require a down payment from the customer at time of purchase. Term lengths and cart ranges are determined by Affirm and may change at their discretion.
- ** Zip offers two products, Zip Pay with a credit limit of 1,000 AUD and Zip Money with a maximum credit limit of 50,000 AUD depending on the users’ eligibility

## Adding on site messaging to your website

Let your customers know you accept one or more of these payment methods by including the Payment Method Messaging Element on your product and cart pages.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`