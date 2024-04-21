htmlSelect your reader | Stripe Documentation[Skip to content](#main-content)Select your reader[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fpayments%2Fsetup-reader)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fpayments%2Fsetup-reader)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)# Select your reader

Learn about Stripe's pre-certified card readers and Tap to Pay.### Shop Now

Ready to buy?

- [Browse available readers and accessories.](https://dashboard.stripe.com/terminal/shop)
- [Get notified when Stripe Reader S700 is available.](https://dashboard.stripe.com/terminal/s700_notify)
- See Tap to Pay[compatible iPhones](/terminal/payments/setup-reader/tap-to-pay?platform=ios#supported-devices)and[Android devices.](/terminal/payments/setup-reader/tap-to-pay?platform=android#supported-devices)

Stripe readers offer end-to-end encryption by default and remote management tools. Select your form of payment acceptance to learn how to set it up:

![](https://b.stripecdn.com/docs-statics-srv/assets/S700-3D.041eca5dfd580cdc451a41020b4dd45a.png)

Stripe Reader S700

![](https://b.stripecdn.com/docs-statics-srv/assets/wisepos-floating-tall.e8478124cda0e088b2e19f503f574f53.png)

BBPOS WisePOS E

![](https://b.stripecdn.com/docs-statics-srv/assets/stripem2.bf6a7eabd353369bfa596a81ab51ca9a.png)

Stripe Reader M2

![](https://b.stripecdn.com/docs-statics-srv/assets/wisepad-floating-thumb.d6e3015116e0b4295b0106e770b9843e.png)

BBPOS WisePad 3

![](https://b.stripecdn.com/docs-statics-srv/assets/tap-to-pay-on-iphone-lockup.d37d3cf47690036b43af67c3e6cf433e.png)

Tap to Pay

If you don’t have a reader, you can order readers from the Dashboard and have them shipped to a location of your choice. As a Connect platform, you can enable your connected accounts to receive readers and accessories at their business location.

Not sure which reader is right for you? Design your integration and choose a reader that works with your application and physical sales environment.

If you don’t have a physical reader, you can use the simulated reader to build and test your Terminal integration. The simulated reader doesn’t require any setup and you can start by setting up your integration.

To choose a reader or a platform, consult the tables on this page. Or, to explore specific combinations, see Design an integration.

WarningStripe readers aren’t liquid-proof and we recommend that users make appropriate efforts to make sure their devices remain dry. If your device has experienced liquid ingress, we recommend that you stop using the device and let it dry thoroughly before attempting to re-use or charge the device. If your device doesn’t properly operate or charge properly after drying, you need to replace it.

## Reader comparison

This table shows the features of the currently available readers.

Reader[Stripe Reader S700](/terminal/readers/stripe-reader-s700)[Notify me](https://dashboard.stripe.com/terminal/s700_notify)[BBPOS WisePOS E](/terminal/payments/setup-reader/bbpos-wisepos-e)[Stripe Reader M2](/terminal/payments/setup-reader/stripe-m2)[BBPOS WisePad 3](/terminal/payments/setup-reader/bbpos-wisepad3)[Tap to Pay](/terminal/payments/setup-reader/tap-to-pay)Country availability[Supported countries](#availability)Coming soon[Supported countries](#availability)US only[Supported countries](#availability)Non-US[Supported countries](#availability)Device categorysPOSsPOSmPOSmPOS[Compatible iPhone](/terminal/payments/setup-reader/tap-to-pay?platform=ios#supported-devices)s and[Android devices](/terminal/payments/setup-reader/tap-to-pay?platform=android#supported-devices)Payment typesEMV chip cards–Contactless cards and digital walletsMagstripe cards––Reporting and device managementBasic device reporting and monitoringBasic reporting[Terminal Hardware Ordering (THOr) API](/terminal/fleet/placing-orders#use-the-hardware-orders-api)Beta–Integration[iOS](/terminal/payments/setup-integration?terminal-sdk-platform=ios)[Android](/terminal/payments/setup-integration?terminal-sdk-platform=android)[Javascript](/terminal/payments/setup-integration?terminal-sdk-platform=js)–––[React Native](/terminal/payments/setup-integration?terminal-sdk-platform=react-native)Beta[Server-driven integration](/terminal/payments/setup-integration?terminal-sdk-platform=server-driven)–––Custom branding[Custom splash screen](/terminal/fleet/splash-screen)–––On-reader experiences[Tipping](/terminal/features/collecting-tips/on-reader)On receipt tipping onlyBetaUser may implement this functionality within their iOS/Android app[Ability to collect input on-screen](/terminal/features/collect-inputs)Beta––User may implement this functionality within their iOS/Android appAbility to run custom POS appComing soon–––User may implement this functionality within their iOS/Android appAccessoriesStripe-designed accessoriesStripe case, Dock, HubComing soon, Third-party standDockDock, Mount––Device specsApproximate dimensions161.9 x 81.6 x 21.4 mm / 6.375 x 3.187 x 0.875 in188.6 x 76.2 x 32.7 mm / 7.43 x 3 x 1.29 in73.5 x 67 x 19.5 mm / 2.89 x 2.63 x 0.76 in69.7 x 121.7 x 17.7 mm / 2.74 x 4.79 x 0.7 in–Approximate weight318g318g85g / 2.99oz130g / 4.59ozDisplay5.5" IPS LCD display with Gorilla glass, 1920 x 1080, 580 nit5" IPS display capacitive touch screen–2.4" color LCD (320 x 240) with backlight–Battery

Battery capacity: Rechargeable Li-polymer, 3.7V, 4,950mAh

Battery life: 2.5 hours time to charge, 140 hours (standby), 15 hours (active use)

Battery capacity: Rechargeable Li-polymer, 3.7v, 3,200mAh

Battery life: 2.75 hours time to charge, 250 hours (standby), 12 hours (active use)

Battery capacity: Rechargeable Li-polymer, 3.7V, 520mAh

Battery life: 2 hours time to charge, 42 hours (standby), 28 hours (active use)

Battery capacity: Rechargeable Li-polymer, 3.7v, 750 mAh

Battery life: 2 hours time to charge, 20 hours (standby), 15 hours (active use)

–

Memory4GB RAM2GB RAM128kb RAM128kb RAM–Storage64GB16GB1MB1MB–ProcessorOcta Core A53Quad Core Cortex A7Cortex M4 Secure MCUCortex M4 Secure MCU–Charging connectionUSB-C port, Accessory dockMicro-USB port, Accessory dockUSB-C portUSB-C port, Accessory dock–Communication interfaceWiFi, Ethernet (with optional hub)WiFi, Ethernet (with optional dock)Bluetooth, USB (Android SDK only)Bluetooth 4.2 BLE, USB (Android SDK only)–[Offline mode](/terminal/features/operate-offline/collect-payments)Beta–Operating systemAndroid 10Android 9ProprietaryProprietaryiOS 16.0 and later or Android 10.0 and laterCameraFront and rearFuture supportRearNot supported–––Audio jack–––MicrophoneFuture supportFront and rearFront and rear–––Security

End-to-end encryption, P2PE ready, Mail order telephone order (MO/TO) P2PE

PCI listing

End-to-end encryption, P2PE ready , Mail order telephone order (MO/TO) P2PE

PCI listing

End-to-end encryption, P2PE ready

PCI listing

End-to-end encryption, P2PE ready

PCI listing

End-to-end encryption

*Battery life information is only an estimate. Battery life varies depending on a number of factors including product specifications, settings, and applications or deployed features.

## Integration platform comparison

Mobile application SDKs for all reader types:

- [Android SDK](/terminal/payments/setup-integration?terminal-sdk-platform=android)
- [iOS SDK](/terminal/payments/setup-integration?terminal-sdk-platform=ios)
- [React Native SDK](/terminal/payments/setup-integration?terminal-sdk-platform=react-native)

For smart readers only without offline payment support:

- [Server-driven integration](/terminal/payments/setup-integration?terminal-sdk-platform=server-driven), which uses the Stripe API rather than a Terminal client SDK
- [JavaScript SDK](/terminal/payments/setup-integration?terminal-sdk-platform=js)

Choose an integration based on the following factors:

- [Preferred reader](/terminal/payments/setup-reader#reader)
- [Desired features](/terminal/payments/setup-reader#feature-table)
- Your technology stack
- Network setup and[DNS configurations](https://support.stripe.com/questions/the-stripe-terminal-sdk-is-encountering-dns-errors-when-connecting-to-an-internet-reader)(only applicable for BBPOS WisePOS E and Stripe Reader S700)

This table lists the features of the five integration platforms.

### Feature table

[Android](/terminal/payments/setup-integration?terminal-sdk-platform=android)[iOS](/terminal/payments/setup-integration?terminal-sdk-platform=ios)[React Native](/terminal/payments/setup-integration?terminal-sdk-platform=react-native)[JavaScript](/terminal/payments/setup-integration?terminal-sdk-platform=js)[Server-driven](/terminal/payments/setup-integration?terminal-sdk-platform=server-driven)Available in USAvailable in[other supported countries](/terminal/payments/regional)[Bluetooth reader support](/terminal/payments/connect-reader?reader-type=bluetooth)––[Smart reader support](/terminal/payments/connect-reader?reader-type=internet)[Multiparty payments with Connect](/terminal/features/connect)[Collect tips](/terminal/features/collecting-tips/overview)[Save cards for future use](/terminal/features/saving-cards/overview)[Refund transactions](/terminal/features/refunds)[Provide receipts](/terminal/features/receipts)[Display cart details](/terminal/features/display)[Incremental authorizations](/terminal/features/incremental-authorizations)[Extended authorizations](/terminal/features/extended-authorizations)[USB support](/terminal/payments/connect-reader?reader-type=usb)–––[Operate offline](/terminal/features/operate-offline/overview)BetaBeta–––## Global availability

Not all readers are available in every country. This table lists the readers and platforms you can use in each country.

CountriesAndroid**iOS**JavaScriptServer-DrivenUnited States![](https://b.stripecdn.com/docs-statics-srv/assets/84052c4398178d23ae59cfdfd4c1a4e3.png)

Stripe Reader M2Bluetooth or USB![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/cbf74926d4a083809dadd9b11bd16740.png)

Tap to PayEmbedded![](https://b.stripecdn.com/docs-statics-srv/assets/84052c4398178d23ae59cfdfd4c1a4e3.png)

Stripe Reader M2Bluetooth![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/cbf74926d4a083809dadd9b11bd16740.png)

Tap to PayEmbedded![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmartAustria+BelgiumCanadaCzech Republic+DenmarkFinland+GermanyIrelandItalyLuxembourg+Malaysia+Norway+Portugal+SpainSwedenSwitzerland+![](https://b.stripecdn.com/docs-statics-srv/assets/ba9684bdc9a5096c66da38a228968305.png)

WisePad 3Bluetooth or USB![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/cbf74926d4a083809dadd9b11bd16740.png)

Tap to Pay*Embedded![](https://b.stripecdn.com/docs-statics-srv/assets/ba9684bdc9a5096c66da38a228968305.png)

WisePad 3Bluetooth![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700*Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmartUnited Kingdom![](https://b.stripecdn.com/docs-statics-srv/assets/ba9684bdc9a5096c66da38a228968305.png)

WisePad 3Bluetooth or USB![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/cbf74926d4a083809dadd9b11bd16740.png)

Tap to PayEmbedded![](https://b.stripecdn.com/docs-statics-srv/assets/ba9684bdc9a5096c66da38a228968305.png)

WisePad 3Bluetooth![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/cbf74926d4a083809dadd9b11bd16740.png)

Tap to PayEmbedded![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700*Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmartNew Zealand+Singapore![](https://b.stripecdn.com/docs-statics-srv/assets/ba9684bdc9a5096c66da38a228968305.png)

WisePad 3Bluetooth or USB![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/cbf74926d4a083809dadd9b11bd16740.png)

Tap to PayEmbedded![](https://b.stripecdn.com/docs-statics-srv/assets/ba9684bdc9a5096c66da38a228968305.png)

WisePad 3Bluetooth![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700*Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmartAustralia![](https://b.stripecdn.com/docs-statics-srv/assets/ba9684bdc9a5096c66da38a228968305.png)

WisePad 3Bluetooth or USB![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/cbf74926d4a083809dadd9b11bd16740.png)

Tap to Pay*Embedded![](https://b.stripecdn.com/docs-statics-srv/assets/ba9684bdc9a5096c66da38a228968305.png)

WisePad 3Bluetooth![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/cbf74926d4a083809dadd9b11bd16740.png)

Tap to PayEmbedded![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700*Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmartFranceNetherlands![](https://b.stripecdn.com/docs-statics-srv/assets/ba9684bdc9a5096c66da38a228968305.png)

WisePad 3Bluetooth or USB![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/cbf74926d4a083809dadd9b11bd16740.png)

Tap to Pay*Embedded![](https://b.stripecdn.com/docs-statics-srv/assets/ba9684bdc9a5096c66da38a228968305.png)

WisePad 3Bluetooth![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/cbf74926d4a083809dadd9b11bd16740.png)

Tap to Pay*Embedded![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700*Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart+Terminal is currently in beta in this country.*This Terminal integration shape is currently in beta.**Compatibility for this mobile SDK also applies when used with React Native.## Connection to Stripe

Before processing payments, you must connect a Terminal reader to your point of sale application using the Terminal SDK. Each reader can only connect to one instance of the SDK at a time. For example, if you want four mobile readers in your store and your app runs on iOS, you also need four iOS devices. Note that only one reader connects to the SDK at a time.

## Pre-certification

In-person payments must follow strict rules to meet PCI compliance, PCI certifications, and EMV certifications.

Terminal offers pre-certified readers that accept payment details (EMV, contactless, and swiped), encrypt sensitive card information, and return a token to your application through the Stripe Terminal SDK so you can confirm payment.

## Reader software updates

Stripe and our hardware partners periodically release reader software updates, which can include improvements and required security updates. Your application must include support for automatic updates. Failing to install a required update can prevent a reader from accepting payments. Smart readers update themselves automatically when powered on, sufficiently charged, and not in use. Bluetooth readers update themselves automatically upon connection to your point of sale.

## Other supported readers

![](https://b.stripecdn.com/docs-statics-srv/assets/verifone-photo-no-white.4db160423e13297d7665a614bf9bd6f1.png)

Verifone P400

![](https://b.stripecdn.com/docs-statics-srv/assets/bbpos-photo-no-white.bf21912a012f27483d48a968515d723c.png)

BBPOS Chipper 2X BT

Stripe Terminal also supports these readers. If you’re interested in these devices, contact sales to discuss or place an order.

## See also

- [Order readers](/terminal/fleet/placing-orders)
- [Set up your integration](/terminal/payments/setup-integration)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Reader comparison](#reader)[Integration platform comparison](#sdk)[Global availability](#availability)[Connection to Stripe](#connection-to-stripe)[Pre-certification](#pre-certification)[Reader software updates](#reader-software-updates)[Other supported readers](#other-supported-readers)[See also](#see-also)Products Used[Terminal](/terminal)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`