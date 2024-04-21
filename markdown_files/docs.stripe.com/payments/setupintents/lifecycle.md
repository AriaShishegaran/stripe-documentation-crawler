htmlHow SetupIntents work | Stripe Documentation[Skip to content](#main-content)How SetupIntents work[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fsetupintents%2Flifecycle)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fsetupintents%2Flifecycle)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)
[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[About the APIs](/docs/payments-api/tour)[Setup Intents API](/docs/payments/setup-intents)# How SetupIntents work

Learn how SetupIntents work within the payment flow.Asynchronous payment flows can be complex to manage because they depend on customer interactions that happen outside of your application. PaymentIntents and SetupIntents simplify management by tracking the status of the flow.

![](https://b.stripecdn.com/docs-statics-srv/assets/1ab45e9a3dd360cdbbe998626aaa5ca1.svg)

requires_payment_methodWhen the SetupIntent is created, it has a status of requires_payment_method1 until a payment method is attached.

![](https://b.stripecdn.com/docs-statics-srv/assets/requires-payment-method.9a42d8ffd0c94023aa88ba0365a9a648.svg)

![](https://b.stripecdn.com/docs-statics-srv/assets/d93e2a08ffc6bbfe4683e3f7d0fffe32.svg)

requires_confirmationOptionalAfter the customer provides their payment method information, the SetupIntent is ready to be confirmed.

In most integrations, this state is skipped because payment method information is submitted at the same time that the SetupIntent is confirmed.

![](https://b.stripecdn.com/docs-statics-srv/assets/requires-confirmation.d8f1cc949e78a3b65f8a9406977eb77e.svg)

![](https://b.stripecdn.com/docs-statics-srv/assets/94646c1d7332e58bd1d56e6cebd1a40e.svg)

requires_actionIf the setup requires additional actions, such as authenticating with 3D Secure , the SetupIntent has a status of requires_action1.

![](https://b.stripecdn.com/docs-statics-srv/assets/requires-action.a062dfa0d428b32132566ba7ef1d7243.svg)

![](https://b.stripecdn.com/docs-statics-srv/assets/8ccc7708adc370d6365aa5558ee39a62.svg)

processingAfter required actions are handled, the SetupIntent moves to processing. Although some payment methods (for example, cards) can process quickly, other payment methods can take up to several days to process.

![](https://b.stripecdn.com/docs-statics-srv/assets/processing.ca1dd4ab95c0abdb79c0505ff702e7e5.svg)

![](https://b.stripecdn.com/docs-statics-srv/assets/6423ea22ac10bfa6996c6f9db9b0ad1d.svg)

succeededA SetupIntent with a status of succeeded means that the setup is successful.

You can now attach this payment method to a Customer object and use this payment method for future payments.

![](https://b.stripecdn.com/docs-statics-srv/assets/succeeded.0f804b44822542e961f31fa590b8461c.svg)

![](https://b.stripecdn.com/docs-statics-srv/assets/34cbc85e7b2159474edf46422b7762f7.svg)

requires_payment_methodIf the setup fails, SetupIntent’s status returns to requires_payment_method.

![](https://b.stripecdn.com/docs-statics-srv/assets/failed.1e456c37d02886f2a966cb540a9507e8.svg)

![](https://b.stripecdn.com/docs-statics-srv/assets/3eb46c024752a66b38516e0f282b95af.svg)

canceledYou can cancel a SetupIntent at any point before it is processing or succeeded.

![](https://b.stripecdn.com/docs-statics-srv/assets/canceled.51a5426d7a6f048a8b2686fcfe91b554.svg)

1 Versions of the API before 2019-02-11 show requires_source instead of requires_payment_method and requires_source_action instead of requires_action.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`