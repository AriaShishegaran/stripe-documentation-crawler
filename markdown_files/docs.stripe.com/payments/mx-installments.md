htmlAccept installment card payments in Mexico | Stripe Documentation[Skip to content](#main-content)Mexico installments[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fmx-installments)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fmx-installments)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Buy now, pay later](/docs/payments/buy-now-pay-later)# Accept installment card payments in Mexico

Learn about credit card payments using an installment plan.Available in:Installments (meses sin intereses) are a type of credit card payment in Mexico that allows customers to split purchases over multiple billing statements. You receive the full amount (minus a fee) as if it were a normal charge, and the customer’s bank handles collecting the money over time.

Stripe supports installment payments for Stripe Mexico accounts using the Payment Intents and Payment Methods APIs, Checkout, Invoicing, Payment Element, and Payment Links.

Get started with accepting installments.

## Connect compatibility

You can use Stripe Connect with installments to process payments on behalf of connected accounts. As a platform, you can set the default installment configuration for your connected accounts in Mexico. Standard connected accounts can override these settings in the Dashboard.

## Connectors and plugins

A variety of connectors and plugins that integrate with Stripe also support installments. These connectors provide no-code and low-code solutions for accepting a wide range of local payment methods using Stripe, including installments.

For example, the latest version of the Stripe Connector for Adobe Commerce has built-in support for accepting payments with installments. For information regarding setup instructions and features for specific plugins, contact the plugin developers directly.

If you use a plugin that doesn’t yet support installments, you can contact our support team to let us know, and we’ll do our best to see if we can enable installments for that plugin.

## Fees

When you accept a payment with installments, an additional fee is added to the standard credit card transaction fee. The fee varies according to the number of installments, or months, applied to the transaction.

Installment Plan DurationDefault Minimum Transaction AmountAdditional Fee %3 months300.00 MXN5%6 months600.00 MXN7.5%9 months900.00 MXN10%12 months1,200.00 MXN12.5%18 months1,800.00 MXN17.5%24 months2,400.00 MXN22.5%## Requirements

There are restrictions on which transactions and cards can use meses sin intereses. You don’t need to implement these rules yourself. Stripe automatically determines meses sin intereses eligibility after you set up the payment method.

- Stripe only supports installments for Stripe Mexico accounts.
- The payment method must be a credit card issued in Mexico.
- The card must be a consumer card–installments don’t support corporate cards.
- The card must be issued by one of our[supported issuers](/payments/mx-installments#supported-cards).
- The currency value must be MXN (pesos).
- The total payment amount must be above a[minimum transaction amount](/payments/mx-installments#fees). Stripe provides a minimum transaction amount based on the number of months in the plan selected. You can specify which installment plans you want to enable and define your own custom minimum and maximum transaction amounts by[configuring custom installment settings](/payments/meses-sin-intereses/accept-a-payment#custom-settings)in the Dashboard.

## Supported cards

You can accept payments in Installments on cards from the following issuers:

- Afirme
- American Express
- BanBajío
- Banjercito
- BBVA
- Banca Mifel
- Banco Azteca
- Banco Famsa
- Banco Invex
- Banco Multiva
- Banorte
- Banregio
- Citibanamex (3-, 6-, 9-, and 12-month plans only)
- Falabella
- Hey Banco
- HSBC
- Inbursa
- Konfio
- Liverpool
- NanoPay
- Nubank
- RappiCard
- Santander
- Scotiabank

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Connect compatibility](#connect-compatibility)[Connectors and plugins](#connectors-and-plugins)[Fees](#fees)[Requirements](#requirements)[Supported cards](#supported-cards)Products Used[Payments](/payments)[Payment Links](/payments/payment-links)[Checkout](/payments/checkout)[Elements](/payments/elements)[Invoicing](/invoicing)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`