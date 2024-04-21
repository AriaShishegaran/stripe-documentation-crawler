htmlDesign an integration | Stripe Documentation[Skip to content](#main-content)Design an integration[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fdesigning-integration)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fdesigning-integration)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)# Design an integration

Choose a reader and platform and see how they work together.Country:AustraliaAustriaBelgiumCanadaCzech RepublicDenmarkGermanyFinlandFranceIrelandItalyLuxembourgMalaysiaNetherlandsNew ZealandNorwayPortugalSingaporeSpainSwedenSwitzerlandUnited KingdomUnited StatesReader:WisePOS EWisePad 3Architecture:JavaScript SDKiOS SDKAndroid SDKServer-drivenReact Native SDKJavaScript SDKiOS SDKAndroid SDKServer-drivenReact Native SDK![Stripe Reader M2](https://b.stripecdn.com/docs-statics-srv/assets/stripem2.bf6a7eabd353369bfa596a81ab51ca9a.png)

59 USD

Reader instructions

Product sheet

Order readers and accessories

## M2 reader features

- Miniature reader
- Optional dock for countertop or mount for mobile roaming
- Contactless, chip, and swipe payments

Not a coder? Find a Stripe partner who supports Terminal.

## Architecture

Write your application using the Terminal SDK. The application uses the SDK to communicate with the reader, your back end, and the Stripe API.

The structure of the integration looks like this:

![Integration architecture for Bluetooth readers](https://b.stripecdn.com/docs-statics-srv/assets/bluetooth-readers-integration-architecture.9d2a56e6b18d403812709a3e7732e583.png)

You can build a working example of an integration like this using the Terminal Quickstart.

## Organize readers and locations

Before you connect a reader to a Terminal integration, you must create one or more Locations, either in the Dashboard or using the API. Then, when you connect to your reader, specify one of those locations.

Locations represent physical places where your readers operate. Stripe needs location information to process payments correctly and keep your reader up to date. If your business requires you to move your readers frequently, your locations may use addresses that represent a primary place of business.

## Prototyping

When you first begin writing your application, you can test it with a simulated reader and simulated cards. The Terminal Quickstart demonstrates an app at this stage of development.

When you’re ready to work with actual hardware, follow these steps:

1. [Order an M2 reader and physical test cards](https://dashboard.stripe.com/terminal/shop).
2. Connect to the reader[using Bluetooth](/terminal/payments/connect-reader?reader-type=bluetooth)or[USB](/terminal/payments/connect-reader?reader-type=usb).
3. [Test your logic with physical test cards](/terminal/references/testing#physical-test-cards).

## Next steps

- [Set up your integration](/terminal/payments/setup-integration)to start writing code.
- See[Terminal Quickstart](/terminal/quickstart)for a full code example.
- [Order readers, accessories, and test cards](https://dashboard.stripe.com/terminal/shop)when you’re ready to work with physical hardware.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`