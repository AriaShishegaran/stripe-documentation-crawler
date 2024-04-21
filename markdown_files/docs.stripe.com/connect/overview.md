htmlWhat is Connect | Stripe Documentation[Skip to content](#main-content)What is Connect[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Foverview)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Foverview)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# What is Connect

Build a multi-party integration to enable payments and payouts to your sellers.Marketplaces and software platforms use Connect and its related tools to route payments between sellers, customers, and recipients who need to get paid.

Connect enables you to streamline management and handle payments and payouts across users on your platform or marketplace.

- Onboarding: Onboard and verify sellers using connected accounts with Stripe-hosted flows, or build your own with our APIs.
- Account management: Enable sellers to manage their account with Stripe-hosted dashboards, embedded components, or build your own with our APIs.
- Payments: Integrate payments and route funds to sellers on your platform.
- Payouts: Pay out sellers with a variety of payout options. Enable cross border payouts for global sellers.
- Platform tools: Manage your platform or marketplace with a sophisticated suite of platform tooling for monetization, seller support, risk management, and tax reporting.

### Country availability

## How Connect works

A Connect integration consists of five main components:

- Your platform’s web or mobile application
- Your platform’s Stripe account
- Your users’ connected accounts
- Stripe payments
- Stripe payouts

When onboarding to Connect, you create a Connect application on your platform’s Stripe account. The Connect application allows you to create and access data on your connected accounts. You use your Stripe API keys to make API requests on behalf of your connected accounts.

![An overview of interactions between a Connect platform, customers, and connected accounts](https://b.stripecdn.com/docs-statics-srv/assets/connect-overview.c6c7d0fac01a655bc51523add1eecd21.png)

Connect offers a number of different options for onboarding accounts for your users and creating payments and payouts on these accounts. Providing your users with access to Stripe-hosted dashboards and embedded components enables you to create a customized experience for your users to manage their financial workflows, while minimizing your development time and helping you to launch quickly.

Connect charge types offer different ways to orchestrate payments to your connected accounts, whether that is enabling users to accept payments directly or facilitating payments between multiple sellers. Connect payouts enable you to manage payout timing, destination payout accounts, and payout monetization on your connected accounts.

## Use cases

Connect is highly flexible and designed to support many multi-party use cases:

- SaaS platforms: Enable users to accept payments directly. Platforms such as Squarespace enable businesses to build their own online stores to sell directly to customers.
- Marketplaces: Collect payments and pay out to multiple sellers. Platforms such as Airbnb connect homeowners to potential guests.
- Top-up and pay out: Payout users without accepting payments. Add funds to your platform account and then transfer funds to your users without processing payments on Stripe.
- In-person payments: Add Stripe Terminal to your multi-party integration. Enable your users to accept in-person payments alongside online payments with a single integration.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[How Connect works](#how-connect-works)[Use cases](#use-cases)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`