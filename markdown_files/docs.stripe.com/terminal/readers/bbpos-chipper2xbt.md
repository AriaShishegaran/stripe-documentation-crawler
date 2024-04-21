htmlBBPOS Chipper 2X BT | Stripe Documentation[Skip to content](#main-content)BBPOS Chipper 2X BT reference[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Freaders%2Fbbpos-chipper2xbt)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Freaders%2Fbbpos-chipper2xbt)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)[Bluetooth readers](/docs/terminal/bluetooth-readers)# BBPOS Chipper 2X BT

Learn about the BBPOS Chipper 2X BT reader.NoteThis reader is no longer available for purchase. If you’re getting started with Stripe Terminal, we recommend viewing our current reader offerings.

![](https://b.stripecdn.com/docs-statics-srv/assets/bbpos-photo-no-white.bf21912a012f27483d48a968515d723c.png)

The BBPOS Chipper 2X BT is a handheld reader for use with mobile applications. It uses Bluetooth Low Energy (LE) or USB (Android only) to connect to the Stripe Terminal SDK on a mobile device.

This reader is compatible with iOS, Android, and React Native SDKs. To view the reader’s parts and features, see the BBPOS Chipper 2X BT product sheet.

## LED status lights

The LEDs on the reader show the current reader and NFC status.

### Reader status

When you turn on the BBPOS Chipper 2X BT, the LED located beside the power button shows the reader’s current status.

LightMeaningNoneThe reader is off.Flashing blue every secondThe reader is on and ready to connect to a device. (Will turn off after 5 min.)Multicolored flashingThe reader has been discovered using Bluetooth Proximity or USB (Android only) and is ready to connect.Steady blueThe reader is connected to a device.Flashing blue every 5 secondsThe reader is in standby mode. (Will remain in standby indefinitely.)Alternating red and magentaThe reader is charging.Flashing redThe reader’s battery is low.Rapidly flashing blue and orangeThe reader has finished installing a software update. If the reader is unresponsive after the update completes, restart the reader by turning it off and on.### NFC status

The LEDs above the NFC marking show the NFC reading status.

LEDsMeaning(flashing) The reader is connecting to the POS terminal.The reader is ready for tapping a card.(LEDs on in consecutive order) The reader is reading card information.(LEDs and one beep sound) The reader has successfully read the card.(No LEDs and one beep sound) The transaction is complete.(No LEDs and two beep sounds) Retry tapping a card.### Reader software releases

### SDK Reference

- [deviceSoftwareVersion (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPReader.html#/c:objc(cs)SCPReader(py)deviceSoftwareVersion)
- [softwareVersion (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-reader/software-version.html)

The software on the BBPOS Chipper 2X BT consists of a firmware version, configuration name, and key identifier. The reader software version joins these three components with underscores into a single string.

Note there are 3 different revisions to the BBPOS Chipper 2X BT. The first 6 characters in the serial number identifies which revision you have.

CHB20CHB20YCHB20ZLatest Version`1.00.03.50-SZZZ_Generic_v47-300001`Firmware versions![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

VersionRelease DateDescription`1.00.03.50``2023-07-24`Maintenance updates.`1.00.03.49``2022-08-30`Maintenance updates.`1.00.03.48``2022-05-05`USB connectivity improvements and maintenance updates.`1.00.03.47``2022-02-23`Bluetooth connectivity improvements and maintenance updates.`1.00.03.34.921a53dc``2021-10-20`Updates reader CAPK keys. You must install before December 31, 2021 to continue accepting payments.`1.00.03.34``2018-11-29`Adds the ability for the reader to beep when a card is inserted.`1.00.03.32``2018-09-20``1.00.02.31``2018-08-02``1.00.02.30`The initial firmware version available for this device.Configurations![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

NameRelease DateDescription`SZZZ_Generic_v47``2023-07-24`Updates production configuration for this device.`SZZZ_Generic_v46``2021-09-13`Enables contactless during`collectSetupIntentPaymentMethod`.`SZZZ_Generic_v45``2020-08-06`Fixes a bug in which the Chipper 2X BT no longer gave audible feedback on chip transactions`SZZZ_Generic_v44``2020-06-25`Updates American Express CVM contactless limit to $200 due to Covid-19.`SZZZ_Generic_v40``2019-05-29`Fixes an issue where certain Amex contactless transactions could not be read.`SZZZ_Generic_v37``2018-11-20`Enables beeps when a card is inserted, the transaction is complete, and when a card is left in the reader.`SZZZ_Generic_v36``2018-09-28`Enabled card insert and removal detection outside of a transaction.`SZZZ_Generic_v35`The initial configuration available for this device.Key identifiers![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

IdentifierRelease DateDescription`30000`The initial key identifier available for this device.`300001``2020-06-30`An alias for`30000`that may be visible in newer Terminal SDK versions.The BBPOS and Chipper™ name and logo are trademarks or registered trademarks of BBPOS Limited in the United States and/or other countries. The Verifone® name and logo are either trademarks or registered trademarks of Verifone in the United States and/or other countries. Use of the trademarks does not imply any endorsement by BBPOS or Verifone.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`