htmlAPI Worksheet Billing | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fworksheets%2Fbilling)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fworksheets%2Fbilling)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# API Worksheet BillingBeta

Use the in-browser Stripe Shell to practice implementing key business processes.This worksheet covers some of our APIs for creating subscriptions and invoices. API Worksheets help you check your understanding of Stripe’s APIs, they assume that you’ve already learned the fundamentals. If you’re training for Stripe’s Partner Program, these worksheets are a good follow up to the e-learning course material. If you’re learning how to use Stripe on your own, consider first exploring our Quickstart guide on implementing a custom payment flow.

To begin, click the Get Started button on the first section to get your first prompt. Read the prompt text carefully, and submit your response by typing in the input field and pressing the Enter key.

[Subscriptions](#subscriptions)Help Taylor set up a guitar lesson subscription and coupon.

[Invoices](#invoices)Help a local band pay a vocalist to join them for one gig.

[Billing terminology](#billing-terminology)Learn more about the Stripe Billing terminology.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`