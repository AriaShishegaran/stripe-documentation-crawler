htmlCredit transfers (Sources) | Stripe Documentation[Skip to content](#main-content)Credit transfers (Sources)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fsources%2Fcredit-transfers)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fsources%2Fcredit-transfers)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)# Credit transfers (Sources)

Learn about bank transfers with Stripe.WarningStripe doesn’t recommend using the deprecated Sources API. Use the PaymentIntents and PaymentMethods APIs to integrate with Bank Transfers. Get started accepting Bank Transfer Payments.

Bank transfers let customers send money to you directly from their bank account. Bank transfers are often used by:

- Software or services businesses accepting large, one-off payments from other businesses.
- Businesses that want a low-cost alternative to cards for large one-time consumer payments, like car or auction purchases.

Bank transfers might not be a good fit for your business if:

- You accept many low value transactions. Customers have to initiate bank transfers through their bank account, and can send the wrong amount.
- You need payments to be completed at a specific time. It might take a customer hours or even days to send payment through their bank and bank transfers have varying speeds by market
- You frequently send refunds. Most bank transfer methods don’t support refunds directly. To refund a transaction, Stripe contacts the customer to find the best way to refund them. The customer might not always respond.

## Payment experience

At checkout, you instruct the customer to send funds to an account number provided by Stripe (known as a “virtual account number”). The customer initiates the transfer from their bank’s site, app, ATM, or in-person branch.

![Figure describing the four step payment flow. First, customer elects pay by bank transfer. Next, they receive a virtual bank account number created by Stripe. Then, they send payment through their bank to the virtual account number. Finally, they are notified payment is complete.](https://b.stripecdn.com/docs-statics-srv/assets/payment_flow.eb89dee4d8cf3a2bd038b6c790fd0cf4.svg)

Some bank transfer methods let you control the amount the customer sends, or reuse virtual account numbers.

## Product support

Payment methodCustomer countryPaymentIntentsCheckoutConnectInvoicingSubscriptionsPayment ElementPayment LinksMobile Payment Element[Multibanco (beta)](/sources/multibanco)Portugal## Additional bank transfer methods

Stripe is expanding support for bank transfers to the PaymentIntents API, including automatic reconciliation and refunds. You can read more on Bank Transfer Payments.

- JPY bank transfers in Japan
- GBP bank transfers in the UK
- EUR bank transfers in SEPA countries
- MXN bank transfers in Mexico
- USD bank transfers in the US

Please contact us if you’re interested in joining one of these betas or would like to request another bank transfer method.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`