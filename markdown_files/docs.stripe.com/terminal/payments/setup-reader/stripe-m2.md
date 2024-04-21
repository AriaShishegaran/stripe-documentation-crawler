htmlSet up Stripe Reader M2 | Stripe Documentation[Skip to content](#main-content)Stripe Reader M2[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fpayments%2Fsetup-reader%2Fstripe-m2)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fpayments%2Fsetup-reader%2Fstripe-m2)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)[Select your reader](/docs/terminal/payments/setup-reader)# Set up Stripe Reader M2

Learn how to set up the Stripe Reader M2.Available in:![](https://b.stripecdn.com/docs-statics-srv/assets/stripem2.bf6a7eabd353369bfa596a81ab51ca9a.png)

Stripe Reader M2 is a small reader that you can use with mobile applications. It uses Bluetooth Low Energy (LE) or USB (Android only) to connect to the Stripe Terminal SDK on a mobile device.

This reader is compatible with our iOS, Android, and React Native SDKs. To view the reader’s parts and features, see the Stripe Reader M2 product sheet.

WarningStripe readers aren’t liquid-proof and we recommend that users make appropriate efforts to make sure their devices remain dry. If your device has experienced liquid ingress, we recommend that you stop using the device and let it dry thoroughly before attempting to re-use or charge the device. If your device doesn’t properly operate or charge properly after drying, you need to replace it.

## Turn the reader on and off

Turn on the Stripe Reader M2 by pressing and releasing the power button. The status LEDs turn on for 2 seconds and the reader beeps twice. The reader waits for a Bluetooth connection for five minutes before turning off.

When the reader connects to a device running your app, the status LEDs on top of the reader flash four times. After connecting, the first status light begins flashing at five second intervals. The reader stays connected to your iOS or Android device while in standby mode and automatically exits standby mode when you resume activity.

When connected, the reader automatically turns off after 10 hours of inactivity. You can turn off the reader manually by pressing and holding the power button for four seconds. You don’t need to turn off the reader to conserve power. When the reader turns off, the four LEDs light up and then turn off one by one to indicate it has turned off.

NoteWith typical usage, you only need to charge the reader fully once per day.

## Charge the reader

To charge the Stripe Reader M2, use the included cable or a USB 2.0 cable.

## Check the battery status

When the Stripe Reader M2 is on, you can press and release the power button once to check the battery level. The LEDs on top of the reader show the current status.

LEDsMeaningFull charge75% charge50% charge25% charge(flashing) Charging## Accessories for the reader

You can use the Stripe Reader M2 with an optional dock for countertop checkout, or an optional mount for roaming checkout.

You can also design your own accessories for the Stripe Reader M2. To download the Stripe Reader M2 mechanical design files (.STP), you must first review and accept our Terminal Design File License Agreement. By downloading the file below, you agree to the terms outlined in the license.

Download Stripe design files

## See also

- [Set up your integration](/terminal/payments/setup-integration)
- [Stripe M2 reference](/terminal/readers/stripe-m2)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Turn the reader on and off](#power)[Charge the reader](#charging)[Check the battery status](#battery-status)[Accessories for the reader](#m2-accessories)[See also](#see-also)Products Used[Terminal](/terminal)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`