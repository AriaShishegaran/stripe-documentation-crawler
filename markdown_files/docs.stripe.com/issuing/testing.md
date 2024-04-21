htmlTesting Issuing | Stripe Documentation[Skip to content](#main-content)Testing[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Ftesting)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/issuing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Ftesting)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)
[Treasury](#)[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Issuing](/issuing)·[Home](/docs)[Banking as a service](/docs/financial-services)[Issuing cards](/docs/issuing)# Testing Issuing

Learn how to test your integration and simulate purchases.### Testing payments

Learn more about testing your Stripe integration.

You can issue cards and simulate purchases using your own Stripe integration in test mode. This allows you to test your integration before you go live without having to make real purchases. You can only use these cards for testing within your Stripe account and not for external purchases.

CautionWhen testing your authorization endpoint, make sure that you have set the endpoint for test mode in your Issuing settings. Toggle View test data to switch between test and live mode data and settings.

## Fund your test mode Issuing balance

Before you create test mode transactions, you must add test mode funds to the Issuing balance on your account. These aren’t real funds, and you can only use them for simulating purchases in test mode.

### Issuing users in the US

Issuing users in the US use “pull” funding, and use Top-ups to fund their Issuing balance. You can create test mode top-ups in the Dashboard, or with the Top-ups API. Learn more about funding Issuing balances for US users.

### Issuing users in the UK and euro area

To top up their balance, Issuing users in the UK and Europe “push” funds using Funding Instructions. You can do this in the test mode Dashboard, or with the Funding Instructions API. Learn more about funding Issuing balances for UK and euro area users.

Without codeWith codeYou can simulate a card purchase by specifying authorization details in the Dashboard.

[Create a cardDashboard](#without-code-create-card)Use the API or the Dashboard to create a cardholder and card in test mode.

[Create a test purchaseDashboard](#without-code-create-test-purchase)Navigate to the Issuing Cards page in test mode, find your newly-created card, then click Create test purchase.

You can select to create either an Authorization or Transaction by force capture.

Depending on your selection, you can provide a number of properties, such as amount, business data, and so on.

Click Submit to create the purchase. If you selected authorization and have configured your synchronous webhook, you can use it to approve or decline the authorization. The browser redirects to the page for the newly-created authorization.

[Create a captureDashboard](#without-code-create-test-capture)To create a test capture with an authorization in the Dashboard, enter test mode and complete the following steps:

1. Navigate to the[Authorizations](https://dashboard.stripe.com/issuing/authorizations)page underIssued Cards.
2. Click the authorization you want to capture, then clickCapture.

You can capture an authorization for an amount that’s lesser, greater, or equivalent to the authorized total. You can also capture multiple times regardless of the authorization’s current state.

Enter the amount you want to capture, then click Submit to create the capture. The browser redirects you to the Transactions page and selects the newly created transaction.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Fund your test mode Issuing balance](#fund-your-test-mode-issuing-balance)[Create a card](#without-code-create-card)[Create a test purchase](#without-code-create-test-purchase)[Create a capture](#without-code-create-test-capture)Products Used[Issuing](/issuing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`