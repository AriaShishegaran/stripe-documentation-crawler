htmlConnect Your PayPal Account | Stripe Documentation[Skip to content](#main-content)Connect your PayPal account[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpaypal%2Fconnect-your-paypal-account)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpaypal%2Fconnect-your-paypal-account)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Wallets](/docs/payments/wallets)[PayPal](/docs/payments/paypal)# Connect Your PayPal Account

Learn how to activate PayPal payments when you're ready to go live.## Get started

CautionIf you use Connect, first check whether your setup is supported under Connect support. If you think your use case is supported, submit an onboarding request from the Stripe Dashboard to get access to PayPal. Stripe sends email updates about the progress of all requests, and the current status is also reflected in your Payment methods settings.

If you’re not using Connect, you can activate the PayPal payment method directly from the Stripe Dashboard.

1. Go to the[Payment Methods settings page](https://dashboard.stripe.com/settings/payment_methods).
2. Locate PayPal in theWalletssection.
3. ClickTurn on.
4. Select yoursettlement preference. If you selectAdd PayPal funds to your Stripe balance, PayPal money flow is similar to other payment methods at Stripe. If you selectKeep PayPal funds in PayPal balance, you’ll need to manage payouts on PayPal with the option to automate the frequency of payouts. Find more information about[settlement modes](/payments/paypal/choose-settlement-preference).
5. ClickContinue to PayPalto complete the integration. You’ll be offered to connect your Stripe and PayPal accounts. You can connect an existing PayPal account or create a new one as part of the process.*
6. After clickingContinue to PayPal, PayPal redirects you back to Stripe where you can check the status of your integration on the Payment Methods settings page.

NoteIn some cases, you might see your integration appear in a pending state after connecting your Stripe and PayPal accounts, which can happen for the following reasons:

- You haven’t confirmed the email address to activate your PayPal account.
- PayPal needs to perform additional verifications on your account.If you’ve verified all of these possibilities and think they don’t apply to your PayPal account, please[contact Stripe Support](https://support.stripe.com/)and we’ll help you resolve the issue.

* Currently, only PayPal business accounts in the European Economic Area (excluding Hungary), the UK, and Switzerland are supported.

## Start accepting PayPal payments

See how to accept PayPal payments at Stripe.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Get started](#get-started)[Start accepting PayPal payments](#start-accepting-paypal-payments)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`