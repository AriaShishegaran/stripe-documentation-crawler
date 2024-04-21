htmlSet up BBPOS Chipper 2X BT | Stripe Documentation[Skip to content](#main-content)BBPOS Chipper 2X BT[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fpayments%2Fsetup-reader%2Fbbpos-chipper2xbt)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fpayments%2Fsetup-reader%2Fbbpos-chipper2xbt)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)[Select your reader](/docs/terminal/payments/setup-reader)# Set up BBPOS Chipper 2X BT

Learn how to set up the BBPOS Chipper 2X BT.NoteThis reader is no longer available for purchase. If you’re getting started with Stripe Terminal, we recommend viewing our current reader offerings.

Available in:![](https://b.stripecdn.com/docs-statics-srv/assets/bbpos-photo-no-white.bf21912a012f27483d48a968515d723c.png)

The BBPOS Chipper 2X BT is a handheld reader for use with mobile applications. It uses Bluetooth Low Energy (LE) or USB (Android only) to connect to the Stripe Terminal SDK on a mobile device.

This reader is compatible with iOS, Android, and React Native SDKs. To view the reader’s parts and features, see the BBPOS Chipper 2X BT product sheet.

## Turn the reader on and off

You can turn on the BBPOS Chipper 2X BT reader by pressing and releasing the power button. The status light turns on to indicate power. The reader waits for a connection for five minutes before turning off.

When the reader connects to a device running your app, its status light shines steady blue. If inactive for more than 30 seconds, it enters standby mode to conserve power, and the status light begins flashing at 5-second intervals. The reader stays connected to your iOS or Android device while in standby and automatically exits standby mode when you resume activity.

The reader automatically turns off after 10 hours of inactivity. You can turn the reader off manually by pressing and holding the power button until the status light goes out. You don’t need to turn off the reader to conserve power.

NoteWith typical usage, you only need to fully charge the reader once per day.

## Status light

When you turn on the BBPOS Chipper 2X BT, the LED located beside the power button shows the reader’s current status.

LightMeaningNoneThe reader is off.Flashing blue every secondThe reader is on and ready to connect to a device. (Will turn off after 5 min.)Multicolored flashingThe reader has been discovered using[Bluetooth Proximity](/terminal/payments/connect-reader?terminal-sdk-platform=ios&reader-type=bluetooth#bluetooth-proximity)or USB (Android only) and is ready to connect.Steady blueThe reader is connected to a device.Flashing blue every 5 secondsThe reader is in standby mode. (Will remain in standby indefinitely.)Alternating red and magentaThe reader is charging.Flashing redThe reader’s battery is low.Rapidly flashing blue and orangeThe reader has finished installing a software update. If the reader is unresponsive after the update completes, restart the reader by turning it off and on.## Charge the reader

To charge the BBPOS Chipper 2X BT, use the included cable or a micro USB cable.

## See also

- [Set up your integration](/terminal/payments/setup-integration)
- [Chipper 2X BT reference](/terminal/readers/bbpos-chipper2xbt)

The BBPOS and Chipper™ name and logo are trademarks or registered trademarks of BBPOS Limited in the United States and/or other countries. The Verifone® name and logo are either trademarks or registered trademarks of Verifone in the United States and/or other countries. Use of the trademarks does not imply any endorsement by BBPOS or Verifone.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Turn the reader on and off](#power)[Status light](#status-light)[Charge the reader](#charging)[See also](#see-also)Products Used[Terminal](/terminal)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`