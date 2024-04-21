htmlReal-time payments | Stripe Documentation[Skip to content](#main-content)Real-time payments[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Freal-time)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Freal-time)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)# Real-time payments

Learn about real-time payments with Stripe.### Real-time payment access

Contact us for access to our exclusive payment method features, to request a new real-time payment method, or to participate in our UPI beta—a preferred payment method in India.

Real-time payment methods let customers directly transfer money from their bank account or alternate funding source using an authenticating intermediary, like a phone number. Because this payment method type increases transaction speeds, it can improve conversion rates. Stripe supports real-time payments in Brazil, Singapore, Thailand, Sweden, and India.

## Payment process

The real-time payment method process is as follows:

1. Stripe sends the customer an identifier that lists the payable amount.
2. The customer makes the payment through their application or third-party service.
3. The application or third-party service communicates with the customers bank to secure the funds.

When a customer uses a real-time payment method, their statement lists the application or third-party service as the payment type.

## Product and country support

The following table lists what products and which countries support each real-time payment method:

Payment methodCustomer countryPayment IntentsCheckoutConnectInvoicingSubscriptions[Pix](/payments/pix)Brazil[PayNow](/payments/paynow)Singapore**[PromptPay](/payments/promptpay)Thailand**[Swish](/payments/swish)SwedenUPIIndia* Invoices and subscriptions only support the send_invoice collection method.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`