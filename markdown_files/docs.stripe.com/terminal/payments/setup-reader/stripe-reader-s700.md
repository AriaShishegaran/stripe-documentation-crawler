htmlSet up Stripe Reader S700 | Stripe Documentation[Skip to content](#main-content)Stripe Reader S700[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fpayments%2Fsetup-reader%2Fstripe-reader-s700)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fpayments%2Fsetup-reader%2Fstripe-reader-s700)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)[Select your reader](/docs/terminal/payments/setup-reader)# Set up Stripe Reader S700

Learn how to set up Stripe Reader S700.Stripe Reader S700Get notified when Stripe Reader S700 is available in your country.

Available in:![](https://b.stripecdn.com/docs-statics-srv/assets/S700-3D.041eca5dfd580cdc451a41020b4dd45a.png)

Stripe Reader S700 is an Android-based smart reader for countertop and handheld use. You can customize the on-reader checkout UI using a suite of pre-built and custom elements.

The Stripe Terminal SDK connects to the reader over the internet or LAN. This reader is compatible with the following integrations:

- JavaScript SDK
- iOS SDK
- Android SDK
- React Native SDK
- Server-driven

For Stripe Reader S700 readers, we recommend the server-driven integration, which uses the Stripe API instead of a Terminal SDK. To view the reader’s parts and features, see the Stripe Reader S700 product sheet.

## Turn the reader on and off

Connect the reader to power by plugging the provided USB-C cable into the port on the left side of your reader. Connect the opposite end of the USB-C cable to the provided power adapter and plug it into a power outlet.

![Side of Stripe Reader S700](https://b.stripecdn.com/docs-statics-srv/assets/s700-side-view.66affe17a0aeac5999a561f44d67bfbc.png)

Stripe Reader S700

After the reader is fully charged, hold down the power button on the right side until the screen turns on. After the device powers on, press the power button to sleep or wake the device. To fully power off the device, hold down the power button until the power off option appears on the screen, then select it.

In a countertop deployment, leaving the device on for extended periods is expected. With a full charge, you can expect the battery to last about 15 hours.

Even when not in use, leave Stripe Reader S700 plugged in and powered on to receive automatic software updates.

## Access settings

To open the settings menu, swipe right from the left edge of the reader screen to reveal a Settings button. Tap the Settings button and enter the admin PIN 07139. From here, you can update your WiFi settings or generate a pairing code for device registration. Battery status is displayed at the top right of this screen. To close the settings menu, click the back arrow in the top left corner.

![](https://b.stripecdn.com/docs-statics-srv/assets/s700-settings-button.6f47bb2572f4ac12b13286dde247ad88.png)

Settings button

![](https://b.stripecdn.com/docs-statics-srv/assets/s700-admin-pin-screen.37e0ae6a621abb2c506db9ae762c8e91.png)

Admin PIN screen

![](https://b.stripecdn.com/docs-statics-srv/assets/s700-settings-menu.e03e2092089fa18470a353da3fdad707.png)

Settings menu

## Screen timeout

The screen times out when the reader isn’t connected to a power source. The default timeout of 1 hour is to improve battery performance. To update this value, go to the settings, select Appearance, then select a new screen timeout from the dropdown. The device screen turns on automatically after a device interaction occurs (such as touching the screen or picking up the device), or when the device enters the payments flow and a payment is initiated.

![](https://b.stripecdn.com/docs-statics-srv/assets/s700-settings-menu.e03e2092089fa18470a353da3fdad707.png)

Settings menu

![](https://b.stripecdn.com/docs-statics-srv/assets/s700-appearance-menu.b83b814d09f1344e1407174e969def1c.png)

Appearance menu

![](https://b.stripecdn.com/docs-statics-srv/assets/s700-settings-timeout.4fa38fc09ee1092d47eb737d46155a15.png)

Timeout menu

## Connect the reader to the internet

Because the Stripe Reader S700 is a smart reader, its reader software communicates directly with Stripe. Your point of sale application communicates with the reader through either a LAN (using a Terminal SDK) or the internet (using the server-driven integration). When communicating with the reader through the LAN, the reader must connect to the same local network as your point of sale application. If you’re running into issues connecting your reader to the internet, follow the troubleshooting steps to diagnose the issue.

### WiFi

To connect to WiFi or switch networks, go to settings, then select WiFi settings to choose the network and connect. Attempting to join a new network disconnects the reader from any existing wireless connection.

Your WiFi network must use WPA-Personal or WPA2-Personal encryption and be password protected. The Stripe Reader S700 does not support non-password-protected networks, enterprise networks, or IPV6 networks. Follow the troubleshooting steps to diagnose issues with IPV6 networks. If needed, you can set a static IP on the device from the Wireless settings screen.

## Network priority

The Stripe Reader S700 prioritizes connecting through Ethernet if possible. Even if previously configured for WiFi, the reader switches to using an Ethernet connection when connected to the dock with a plugged-in Ethernet cable. If you remove the reader from the dock, it switches back to the WiFi connection.

The Stripe Reader S700 resets its priority to Ethernet when rebooting. Even if previously configured for WiFi, the reader switches to Ethernet if it detects an Ethernet cable connection while starting up.

If the you dock the reader, but there is no Ethernet cable plugged in, it uses WiFi. Regardless of connectivity while docked, you can still connect to WiFi and manage networks on the device.

## Change the UI appearance

By default, the user interface of your Stripe Reader S700 reader uses a light theme.

![](https://b.stripecdn.com/docs-statics-srv/assets/s700-welcome-screen.903f1751a4041eefd1840d9a5d2f110f.png)

Welcome screen

![](https://b.stripecdn.com/docs-statics-srv/assets/s700-payment-screen.4dd5fc4be4c989e6af7bd1b2a635ba5d.png)

Payment screen

![](https://b.stripecdn.com/docs-statics-srv/assets/s700-processing-screen.f99410ddc0d26e095ffdda92e953e7ac.png)

Processing screen

![](https://b.stripecdn.com/docs-statics-srv/assets/s700-approved-screen.ae53ca99ba84aefbf2cb1aacf9ef1a2e.png)

Approved screen

You can change the appearance of the UI to use a different theme in the settings menu. Go to settings, then select Appearance, and select a new theme from the dropdown.

![](https://b.stripecdn.com/docs-statics-srv/assets/s700-settings-menu.e03e2092089fa18470a353da3fdad707.png)

Settings menu

![](https://b.stripecdn.com/docs-statics-srv/assets/s700-appearance-menu.b83b814d09f1344e1407174e969def1c.png)

Appearance menu

![](https://b.stripecdn.com/docs-statics-srv/assets/s700-settings-theme.b07df3b6d20482df8790ecb9e19e8893.png)

Theme menu

## Change the default reader language

Stripe Reader S700 supports changing the reader language in the reader settings menu. Swipe right across the screen to access the settings menu, and select your language.

## Accessories

You can design your own accessories for the Stripe Reader S700. To download the Stripe Reader S700 mechanical design files (.STP), you must first review and accept our Terminal Design File License Agreement. By downloading the file below, you agree to the terms outlined in the license.

Download Stripe design files

## See also

- [Set up your integration](/terminal/payments/setup-integration)
- [Stripe Reader S700 reference](/terminal/readers/stripe-reader-s700)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Turn the reader on and off](#turn-the-reader-on-and-off)[Access settings](#settings)[Screen timeout](#screen-timeout)[Connect the reader to the internet](#connect-the-reader-to-the-internet)[Network priority](#network-priority)[Change the UI appearance](#change-the-ui-appearance)[Change the default reader language](#change-the-default-reader-language)[Accessories](#accessories)[See also](#see-also)Products Used[Terminal](/terminal)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`