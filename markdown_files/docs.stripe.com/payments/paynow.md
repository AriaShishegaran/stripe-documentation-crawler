htmlPayNow payments | Stripe Documentation[Skip to content](#main-content)PayNow[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpaynow)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpaynow)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Real-time payments](/docs/payments/real-time)# PayNow payments

Learn about PayNow, a popular payment method in Singapore.PayNow is a Singapore based payment method that allows customers to make a payment using their preferred app from participating banks and participating non-bank financial institutions.

Customers see a QR code when checking out with PayNow. They complete the payment by scanning it using a participating app. You receive confirmation from Stripe instantly when they complete the payment.

Payment method propertiesCountry availability- Customer locations

Singapore


- Presentment currency

SGD


- Payment confirmation

Customer-initiated


- Payment method family

Real-time payments


- Billing support

Yes


- Payout timing

T+1 availability


- Connect support

Yes


- Dispute support

Not applicable


- Refunds / Partial refunds

Yes / Yes


- Pricing

1.3%



[Get started](#refunds)You don’t actually have to integrate PayNow and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- [Checkout](/checkout/quickstart): Our prebuilt, hosted checkout page.
- [Elements](/payments/quickstart): Our drop-in UI components.

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

### Other payment products

The following Stripe products also support adding PayNow from the Dashboard:

- [Invoicing](/invoicing/quickstart-guide)
- [Payment Links](/payment-links)
- [Subscriptions](/billing/subscriptions/overview)

If your integration requires manually listing payment methods, learn how to manually configure PayNow as a payment.

[Refunds](#refunds)You can refund PayNow payments up to 90 days after the original payment. Refunds for PayNow payments are asynchronous and Stripe notifies you of the final refund status using the charge.refund.updated webhook event. When a refund succeeds, the status of the Refund object transitions to succeeded. If a refund fails, the status of the Refund object transitions to failed and Stripe returns the amount to your Stripe balance. At this point, you need to arrange an alternative way of providing your customer with a refund.

[Statement descriptors](#statement-descriptors)Customized statement descriptors aren’t supported by PayNow, the value specified in the statement_descriptor is ignored. Stripe’s company name (STRIPE PAYMENTS SINGAPORE PTE. LTD.) is shown when your customers complete payments on their mobile app. It’s also shown on bank statements along with the amount and a Stripe-generated reference code.

[Repeated payments](#repeated-payments)To prevent your customers from being charged multiple times, after your customer successfully completes a transaction, any subsequent attempts to pay using the same QR code are rejected. The rejection behavior depends on the bank and payment app used by the customer to attempt the transaction. If your customers contact you about repeated payments, you can advise them to check for text messages or notifications from their bank or payment app, which will show that the payment attempt was rejected.

[Billing](#billing)Use Stripe Billing to create PayNow supported subscriptions and invoices.

PayNow payments don’t support automatically charging invoices. You need to configure invoices and subscriptions with send_invoice collection_method.

[Payout Timing](#payout-timing)By default, it takes 1 day from the time of the transaction for the funds to be available in your Stripe balance. Stripe pays out available funds to your bank account according to the payout schedule set on your Stripe account.

For example, if the payment was made on Wednesday, the funds are available in your Stripe balance on Thursday. If you’re on an automatic daily payout schedule, the funds are paid out on Thursday. If you’re on a weekly (Monday) payout schedule, the funds are paid out on the coming Monday.

[Disputed payments](#disputed-payments)PayNow payments have a low risk of fraud or unrecognized payments because the customer must authenticate the payment through participating apps. As a result, there’s no dispute process that can result in a chargeback and funds being withdrawn from your Stripe account.

[Prohibited business categories](#prohibited-business-categories)On top of the categories of businesses restricted from using Stripe overall, the following categories are specifically prohibited from using PayNow.

- Petroleum and Petroleum Products
- Fuel Dealers
- Service Stations
- Automated Fuel Dispensers

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Get started](#refunds)[Refunds](#refunds)[Statement descriptors](#statement-descriptors)[Repeated payments](#repeated-payments)[Billing](#billing)[Payout Timing](#payout-timing)[Disputed payments](#disputed-payments)[Prohibited business categories](#prohibited-business-categories)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`