htmlSet up Verifone P400 | Stripe Documentation[Skip to content](#main-content)Verifone P400[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fpayments%2Fsetup-reader%2Fverifone-p400)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fpayments%2Fsetup-reader%2Fverifone-p400)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)[Select your reader](/docs/terminal/payments/setup-reader)# Set up Verifone P400

Learn how to set up the Verifone P400.Available in:NoteThis reader is no longer available for purchase. If you’re getting started with Stripe Terminal, we recommend viewing our current reader offerings.

![](https://b.stripecdn.com/docs-statics-srv/assets/verifone-photo-no-white.4db160423e13297d7665a614bf9bd6f1.png)

The Verifone P400 is a countertop reader for Stripe Terminal apps. It connects to the Stripe Terminal SDK over the internet.

This reader is compatible with JavaScript, iOS, Android, and React Native SDKs. To view the reader’s parts and features, see the product sheet.

## Turn the reader on and off

To turn on the Verifone P400, securely plug the P400 connector cable into the port on the bottom of the reader. The cover slides over the port to hold the cable in place. Plug the power adapter into the connector cable and into a power outlet.

![](https://b.stripecdn.com/docs-statics-srv/assets/verifone-connector-cable-horz.d922bf66e6b7b9a405a86ed19a2bcbed.png)

Verifone P400 connector cable

The Verifone P400 automatically turns on when connected to power. In a countertop deployment, leaving the device on for extended periods is expected. If you need to turn the reader off, remove the power source.

NoteEven when it’s not in use, leave the Verifone P400 plugged in to receive automatic software updates.

## Connect the reader to the internet

Because the Verifone P400 is a smart reader, its reader software communicates directly with Stripe, managing connectivity through a LAN. The reader must connect to the same local network as your application. If you’re running into issues connecting your reader to the internet follow the troubleshooting steps to diagnose the issue.

### WiFi  Beta

If you’re setting up a new device, follow the on-screen prompts to connect to the internet using WiFi. To start over, press the red X button on the keypad.

To switch networks, or connect an already online reader to a WiFi network, press 0WIFI (0-9-4-3-4) on the keypad and follow the prompts. Attempting to join a new network disconnects the reader from any existing wireless connection. There’s no fallback to the previously connected network.

Your WiFi network must use WPA-Personal or WPA2-Personal encryption and be password protected. WiFi isn’t supported for non-password-protected networks or enterprise networks.

CautionConnecting over WiFi is a beta feature. For production use, have an Ethernet connection ready as a backup, in case of degraded networks or connectivity issues.

Key mapping![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

To access characters from the keypad, use this multi-tap key mapping scheme. The table shows which characters each key maps to, in the order they’ll appear.

Keypad NumberCharactersKeypad NumberCharacters0`0-+=_!?@$%^&/\()[]{}<>~|`6`6mnoMNO`1`1qz.QZ`7`7prsPRS`2`2abcABC`8`8tuvTUV`3`3defDEF`9`9wxyWXY`4`4ghiGHI`*`*,’␣”`:;`5`5jklJKL`#`#`For example, if your network password is Stripe, enter 7-7-7-7-7-7-7-8-8-7-7-7-4-4-4-4-7-7-3-3-3.

### Ethernet

Connect an Ethernet cable from your router to the Verifone P400, using the ETH port (not the RS232 port).

![](https://b.stripecdn.com/docs-statics-srv/assets/verifone-ethernet.0a73ad6671ff1a871d6d321bd2c5d0ca.png)

Connecting Ethernet cable to Ethernet port

The reader obtains an IP address using DHCP. As soon as the network cable is plugged in, the reader attempts to establish communication with Stripe.

### Network priority

The Verifone P400 resets its priority to Ethernet when rebooting. Even if previously configured for WiFi, the reader switches to Ethernet if it detects an Ethernet cable connection while starting up.

If you connect to WiFi while an Ethernet cable is connected, the reader switches to the WiFi connection. If the reader fails to connect to WiFi on the first attempt, it falls back to Ethernet connection. Otherwise, the reader continues to prioritize WiFi until rebooted.

## Reader screens

The reader has a few screens to indicate its connectivity state. The default splash screen indicates that the reader is connected to Stripe and ready for processing.

You can customize the reader’s default splash screen by setting up locations.

![](https://b.stripecdn.com/docs-statics-srv/assets/frame-1.def28f57601302f767925405e3d7b9d4.png)

Default splash screen

![](https://b.stripecdn.com/docs-statics-srv/assets/frame-2.e65c2a6f9947656319ab13359062c0ed.png)

Downloading update screen

![](https://b.stripecdn.com/docs-statics-srv/assets/frame-3.e506a5f3ddd36501c195a36015946372.png)

Not connected screen

## Default reader language

The Verifone P400 interface displays text in both English and the language of the region the reader is registered in.

## See also

- [Set up your integration](/terminal/payments/setup-integration)
- [Verifone P400 reference](/terminal/readers/verifone-p400)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Turn the reader on and off](#power)[Connect the reader to the internet](#connecting-to-the-internet)[Reader screens](#reader-screens)[Default reader language](#default-reader-language)[See also](#see-also)Products Used[Terminal](/terminal)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`