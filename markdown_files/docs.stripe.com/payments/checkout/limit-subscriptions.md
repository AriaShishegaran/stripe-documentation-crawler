htmlLimit customers to one subscription | Stripe Documentation[Skip to content](#main-content)Limit customers to one subscription[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Flimit-subscriptions)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Flimit-subscriptions)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Checkout](/payments/checkout)·[Home](/docs)[Payments](/docs/payments)[Checkout](/docs/payments/checkout)# Limit customers to one subscription

Direct customers to manage their subscription when they already have one.You can redirect customers that already have an active subscription to the customer portal or your website to manage their subscription. This redirection works with Checkout (including the pricing table) and Payment Links.

Stripe uses either the Customer object (if you provide it in the checkout session) or the email address to detect if a customer already has an active subscription.

![Manage subscription](https://b.stripecdn.com/docs-statics-srv/assets/manage-subscription.47036dfee120d3651fc3819c8b7abfbb.png)

## Direct your customers to the customer portal or your website

Customer portalYour website1. [Activate the no-code customer portal](/customer-management/activate-no-code-customer-portal)to allow your customers to log in and manage their subscriptions. You need to keep the login link for the customer portal enabled to keep this feature enabled. Disabling the login link disables this feature, which means that customers can create multiple subscriptions.
2. Enable redirecting your customers to the customer portal in your[Checkout and Payment Links settings](https://dashboard.stripe.com/settings/checkout#subscriptions).

![Subscription settings](https://b.stripecdn.com/docs-statics-srv/assets/subscription-settings.28f8c4efc7a1ca0efceeee8ebeae4786.png)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`