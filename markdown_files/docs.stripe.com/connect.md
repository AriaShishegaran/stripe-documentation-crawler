htmlStripe Connect | Stripe Documentation[Skip to content](#main-content)Overview[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)# Stripe Connect

Learn how to route payments between multiple parties.Business models like marketplaces and software platforms use Connect and its related tools to route payments between businesses, customers, and recipients who need to get paid.

[Get started](/docs/connect/overview)## Get started with no code

[Collect and pay out with Payment LinksNo code requiredCollect payments from customers and automatically pay out a portion to your sellers or service providers.](/docs/connect/collect-then-transfer-guide?platform=no-code)[Pay out moneyNo code requiredAdd money from your bank to pay out your sellers or service providers.](/docs/connect/add-and-pay-out-guide?dashboard-or-api=dashboard)## Route payments and pay out

[Collect payments then pay outCollect payments from customers then pay out to sellers or service providers.Like Lyft, Instacart, or Postmates](/docs/connect/collect-then-transfer-guide)[Enable other businesses to accept payments directlyFacilitate direct payments between other businesses and their own customers.Like Shopify, Xero, or DocuSign](/docs/connect/enable-payment-acceptance-guide)## Collect recurring payments

[Enable connected accounts to create subscriptionsEnable other businesses who use your platform to bill their end customers.](/connect/subscriptions#customer-connected-account)[Create subscriptions to bill platform end customersCollect recurring payments from your end customers, optionally splitting the payment with your sellers or service providers.](/connect/subscriptions#customer-platform)[Create subscriptions to bill connected accountsCharge a recurring fee to other businesses to use your platform.](/connect/subscriptions#connected-account-platform)[View all subscription options](/docs/connect/subscriptions)## Manage your connected accounts

[Collect onboarding informationCreate a Stripe-hosted onboarding experience or create your own custom flow with the Connect API.](/connect/accounts)[Upgrade to dynamic payment methodsIncrease conversion by automatically localizing payment methods to each country you sell in.](/connect/dynamic-payment-methods)[Manage tax forms for your US-based accountsConfigure and send 1099-MISC, 1099-K, or 1099-NEC tax forms to your connected accounts.](/connect/tax-reporting)## Enhance your Connect integration

[Use Stripe Tax with ConnectCalculate, collect, and report taxes for your platform or connected accounts.](/tax/connect)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`