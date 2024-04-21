htmlSupported card brands | Stripe Documentation[Skip to content](#main-content)Supported card brands[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fpayments%2Fsupported-card-brands)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fpayments%2Fsupported-card-brands)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)# Supported card brands

Learn about the card brands supported by Stripe Terminal.Stripe Reader S700Get notified when Stripe Reader S700 is available in your country.

When you integrate Stripe Terminal, you can begin accepting a diversity of card brands. Your reader will automatically configure itself to accept the brands relevant for its region.

## In-person brand capabilities

The following table describes some of the different features and restrictions of each card brand in-person, including limitations on countries where Stripe users can accept the brand (Stripe Account Country), support for different reader types, and card presentment modes. Terminal is currently available in 23 countries.

When processing an in-person transaction, Terminal requires that you use local currency. Terminal supports NFC-based mobile wallets (Apple Pay, Google Pay, and Samsung Pay).

Card brandTerminal location and Stripe account countryReader typesCard presentment modeVisaAll countries where Terminal is supportedAllAllMastercardAll countries where Terminal is supportedAllAlleftposAustraliaWisePad 3, WisePOS E, Stripe Reader S700, and Tap to Pay on iPhoneAllAmerican ExpressAll countries where Terminal is supported, except MalaysiaAllAllDiscover & DinersUnited States, Canada, and United KingdomUS: Verifone P400, Stripe M2, Chipper 2X BT, and Tap to Pay on iPhoneUS, CA, GB: WisePad 3, WisePOS E, and Stripe Reader S700All[Interac](/terminal/payments/regional?integration-country=CA#interac-payments)CanadaWisePad 3, WisePOS E, Verifone P400, and Stripe Reader S700AllMaestroAll non-US countries where Terminal is supportedWisePad 3, WisePOS EAllWas this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`