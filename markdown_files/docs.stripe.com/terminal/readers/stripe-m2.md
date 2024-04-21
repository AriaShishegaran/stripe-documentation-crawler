htmlStripe Reader M2 | Stripe Documentation[Skip to content](#main-content)Stripe Reader M2 reference[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Freaders%2Fstripe-m2)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Freaders%2Fstripe-m2)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)[Bluetooth readers](/docs/terminal/bluetooth-readers)# Stripe Reader M2

Learn about the Stripe Reader M2 Bluetooth reader.Available in:![](https://b.stripecdn.com/docs-statics-srv/assets/stripem2.bf6a7eabd353369bfa596a81ab51ca9a.png)

Stripe Reader M2 is a small, robust reader for use with mobile applications. It uses Bluetooth Low Energy (LE) or USB (Android only) to connect to the Stripe Terminal SDK on a mobile device.

This reader is compatible with our iOS, Android, and React Native SDKs. To view the reader’s parts and features, see the Stripe Reader M2 product sheet.

## LED status lights

The LEDs on top of the reader show the current status.

### Battery and charging status

When the Stripe Reader M2 is on, you can press and release the power button once to check the battery level.

LEDsMeaningFull charge75% charge50% charge25% charge(flashing) Charging### Connectivity and reader status

When you connect to the Stripe Reader M2, you can check the LEDs for the reader status.

LEDsMeaning(flashing, three times) Reader is connected to Bluetooth or USBReader is in bootloader modeReader is in standby mode(flashing, every 0.1 seconds for 30 seconds) Reader tampered(30 seconds) Reader integrity check failed## Reader software releases

### SDK Reference

- [deviceSoftwareVersion (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPReader.html#/c:objc(cs)SCPReader(py)deviceSoftwareVersion)
- [softwareVersion (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-reader/software-version.html)

The software on the Stripe Reader M2 consists of a firmware version, configuration name, and key identifier. The reader software version joins these three components with underscores into a single string.

Latest Version`2.01.00.20-SZZZ_Prod_US_v5-480001`Firmware versions![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

VersionRelease DateDescription`2.01.00.20``2023-10-24`Bug fixes and improvements.`2.01.00.17``2023-04-17`Bug fixes and improvements.`2.01.00.16``2022-10-17`Bug fixes and improvements.`2.01.00.15``2022-03-17`Bug fixes and improvements.`2.01.00.05``2021-07-01`The initial firmware version available for this device.Configurations![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

NameRelease DateDescription`SZZZ_Prod_US_v5``2023-04-17`Updates production configuration for this device.`SZZZ_Prod_US_v1``2021-11-03`Updates production configuration for this device.`SZZZ_Test_US_v6``2021-07-01`The initial configuration available for this device.Key identifiers![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

IdentifierRelease DateDescription`480001``2021-07-01`The initial key identifier available for this device.## Accessories for the reader

You can use the Stripe Reader M2 with an optional dock for countertop checkout, or an optional mount for roaming checkout.

You can also design your own accessories for the Stripe Reader M2. To download the Stripe Reader M2 mechanical design files (.STP), you must first review and accept our Terminal Design File License Agreement. By downloading the file below, you agree to the terms outlined in the license.

Download Stripe design files

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[LED status lights](#led-status-lights)[Reader software releases](#reader-software-releases)[Accessories for the reader](#m2-accessories)Products Used[Terminal](/terminal)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`