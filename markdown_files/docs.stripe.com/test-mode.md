htmlTest mode | Stripe Documentation[Skip to content](#main-content)Test mode[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftest-mode)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftest-mode)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)
[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)Testing# Test mode

Use test mode to test your Stripe integration before going live with payments.Stripe’s test mode allows you to test your integration without making actual charges or payments. Test mode is a testing environment that simulates creating real objects without the risk of affecting real transactions or moving actual money.

In test mode, you can charge test credit cards as well as create test products and prices. You can also use test mode to simulate transactions to make sure that your integration works correctly. This feature helps to identify any bugs or errors in your Stripe implementation before you go live with actual payments.

After you create a Stripe account, you can find a set of test API keys in the Stripe Dashboard. You can use these API keys to create and retrieve simulated data by making requests to the Stripe API. To start accepting real payments, you need to activate your account, toggle off test mode, and use the live API keys in your integration.

Impact on live modeIn the Dashboard, changing settings in test mode might also change them in live mode. Many Dashboard pages have a white notification box and disable live mode settings while in test mode. In this case, any settings still enabled are safe to use. If there’s no white callout, assume any changes made in test mode affect live mode settings (unless you see an orange test data banner).

## Test mode versus live mode

All Stripe API requests occur in either test mode or live mode. API objects in one mode aren’t accessible to the other. For instance, a test-mode product object can’t be part of a live-mode payment.

TypeWhen to useObjectsHow to useConsiderationstest modeUse test mode, and its associated test API keys, as you build your integration. In test mode, card networks and payment providers don’t process payments.API calls return simulated objects. For example, you can retrieve and use test`account`,`payment`,`customer`,`charge`,`refund`,`transfer`,`balance`, and`subscription`objects.Use[test credit cards and accounts](/testing#cards). You can’t accept real payment methods or work with real accounts.[Identity](/identity)doesn’t perform any verification checks. Also, Connect[account objects](/api/accounts/object)don’t return sensitive fields.live modeUse live mode, and its associated live API keys, when you’re ready to launch your integration and accept real money. In live mode, card networks and payment providers do process payments.API calls return real objects. For example, you can retrieve and use real`account`,`payment`,`customer`,`charge`,`refund`,`transfer`,`balance`, and`subscription`objects.Accept real credit cards and work with customer accounts. You can accept actual payment authorizations, charges, and captures for credit cards and accounts.Disputes have a more nuanced flow and a simpler[testing process](/testing#disputes). Also, some[payment methods](/payments/payment-methods)have a more nuanced flow and require more steps.The Test mode toggle in the Dashboard doesn’t affect your integration code. Your test and live mode API keys affect the behavior of your code.

## Test card numbers

Stripe provides a set of test card numbers that you can use to simulate various payment scenarios. You can use these test card numbers to create simulated payments in test mode without processing actual payments or charges.

When you use test card numbers, you can enter any expiration date in the future and any three-digit CVC code to simulate a successful payment. If you want to simulate a failed payment, you can use specific test card numbers and CVC codes provided by Stripe.

Test card numbers are only valid in test mode. Don’t use them for real payments.

## Delete test data

To delete all of your test data from your Stripe account, complete the following steps:

1. [Log in to the Dashboard](https://dashboard.stripe.com/)using your existing Stripe account.
2. While in test mode, clickDevelopersand scroll down to the bottom of theOverviewtab.
3. ClickDelete all test data…The ensuing dialog gives you a list of all of your existing test data objects.
4. ClickStart deletionto initiate the deletion process. You can’t undo the deletion of your test data.

Test mode is temporarily unusable while the deletion process occurs.

## Test email

By default, Stripe won’t send an email to customers in test mode. If you want to verify emails for invoices and receipts, you can set the email address for your Team on the Customer object or receipt_email attribute on the PaymentIntent.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Test mode versus live mode](#test-versus-live-mode)[Test card numbers](#test-card-numbers)[Delete test data](#delete-test-data)[Test email](#test-email)Related Guides[Testing](/docs/testing)[API keys](/docs/keys)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`