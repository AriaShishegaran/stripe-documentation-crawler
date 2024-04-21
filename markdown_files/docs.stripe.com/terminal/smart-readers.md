htmlStripe Terminal smart readers | Stripe Documentation[Skip to content](#main-content)Smart readers[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fsmart-readers)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fsmart-readers)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)# Stripe Terminal smart readers

Learn about Stripe's pre-certified in-person payment readers.### Shop Now

Ready to buy? Browse available readers and accessories.

Stripe Reader S700Get notified when Stripe Reader S700 is available in your country.

Terminal’s smart readers are compatible with the JavaScript, iOS, Android, and React Native SDKs. In addition to the Terminal SDKs, the BBPOS WisePOS E and the Stripe Reader S700 are compatible with server-driven integration. Smart readers communicate with the SDKs and Stripe API over the internet.

ReaderAvailable in[Stripe Reader S700](/terminal/readers/stripe-reader-s700)[BBPOS WisePOS E](/terminal/readers/bbpos-wisepos-e)[Verifone P400](/terminal/readers/verifone-p400)### Reader software updates

Stripe maintains the software that controls smart readers. The readers receive updates automatically from Stripe when not in use. Leave your reader connected to power to receive automatic software updates. This ensures that updates happen at midnight (in the timezone of the assigned location) to avoid interruption to sales. If you unplug the reader at night, an update could start when you turn it back on. To manually check for an update, reboot the reader.

NoteSmart readers restart every day at midnight for PCI compliance, and disconnect from the POS app every morning.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`