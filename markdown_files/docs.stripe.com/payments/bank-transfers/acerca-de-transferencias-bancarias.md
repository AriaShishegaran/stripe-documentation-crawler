htmlMexico bank transfers | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbank-transfers%2Facerca-de-transferencias-bancarias)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbank-transfers%2Facerca-de-transferencias-bancarias)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# Mexico bank transfers

Learn about Mexico bank transfers and its supported features.## What are bank transfers?

Bank transfers are a popular way to pay in Mexico. For merchants, bank transfers help reduce customer decline rates, fraud, and chargebacks, and have lower fees than credit cards. For customers in Mexico that have access to bank transfers in their banking apps, it’s a convenient way to pay.

## Target user segments

In particular, the Stripe bank transfer product serves users that process high average order volume (AOV) and low-frequency payments. This includes B2C Marketplaces with high AOV, B2B SaaS businesses, and fintech businesses.

## Product features

Stripe’s bank transfer product is powered by Citibanamex, the local Mexico unit of Citigroup, Inc. Citibanamex is a member of the SPEI network and provides the necessary basic capabilities for processing bank transfer payments.

Our product addresses key user needs by offering automatic reconciliation and management of partial and over payments, as well as refunds. Importantly, we designed the product knowing that low-code and no-code solutions are critical for users in Mexico, and it allows them to manage bank transfer payments through low-code and no-code solutions such as invoices created in the Dashboard.

Our bank transfer product also offers successful payment confirmation notifications. Stripe provides a message, either in an API response or in a UI message in the Dashboard, indicating that a specific payment intent has been paid. On business days, we expect to provide successful payment confirmation of most payments within 30 minutes of the transfer, and on non-business days, such as a weekend or bank holiday, we provide payment confirmation for most payments on the next business day. For certain payments, you might experience delays of up to several days. Also, in case of online system maintenance, the payment confirmation will be delayed until the system is back online.

As soon as Stripe receives the successful payment confirmation from Citibanamex (based on the timing described above), the Dashboard updates to show the credit or completed payment. Funds can get paid out to the user’s bank account as soon as 3 days after Citibanamex has confirmed the bank transfer.

NoteDue to reporting limitations, our product doesn’t offer immediate payment confirmation notifications or settlements. As a result, our product is better suited for merchants that process high AOV, low-frequency payments, such as B2B businesses rather than consumer retail businesses.

## Get started

Get started with accepting bank transfer payments or learn more about the customer balance.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[What are bank transfers?](#what-are-bank-transfers)[Target user segments](#target-user-segments)[Product features](#product-features)[Get started](#get-started)Products Used[Payments](/payments)[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`