htmlSet up BBPOS WisePOS E | Stripe Documentation[Skip to content](#main-content)BBPOS WisePOS E[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fpayments%2Fsetup-reader%2Fbbpos-wisepos-e)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fpayments%2Fsetup-reader%2Fbbpos-wisepos-e)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)[Select your reader](/docs/terminal/payments/setup-reader)# Set up BBPOS WisePOS E

Learn how to set up the BBPOS WisePOS E.Available in:![](https://b.stripecdn.com/docs-statics-srv/assets/wisepos-floating-tall.e8478124cda0e088b2e19f503f574f53.png)

The BBPOS WisePOS E is a countertop reader for Stripe Terminal apps.

The Stripe Terminal SDK connects to the reader over the internet or LAN. This reader is compatible with the following integrations:

- JavaScript SDK
- iOS SDK
- Android SDK
- React Native SDK
- Server-driven

For BBPOS WisePOS E readers, we recommend the server-driven integration, which uses the Stripe API instead of a Terminal SDK. To view the reader’s parts and features, see the BBPOS WisePOS E product sheet.

WarningStripe readers aren’t liquid-proof and we recommend that users make appropriate efforts to make sure their devices remain dry. If your device has experienced liquid ingress, we recommend that you stop using the device and let it dry thoroughly before attempting to re-use or charge the device. If your device doesn’t properly operate or charge properly after drying, you need to replace it.

## Turn the reader on and off

When you first receive the device, install the battery. With the back of the device facing you, lift up from the indentation at the bottom left corner to detach the back cover. Insert the battery by sliding it into the exposed slot with the gold connectors at the top aligned. After the battery is in place, charge the reader by using an outlet or the optional ethernet dock. Connect the reader to power by plugging the provided cable into the port with the lightning bolt symbol.

![](https://b.stripecdn.com/docs-statics-srv/assets/wisepos-power.97a74f498008baacd6b6d88a30cd5dfc.jpg)

After the reader is fully charged, hold down the power button on the right hand side until the screen turns on. After the device powers on, press the power button to sleep or wake the device. To fully power off the device, hold down the power button until the power off option is shown on the screen, then select it.

In a countertop deployment, leaving the device on for extended periods is expected. With a full charge, you can expect the battery to last about eight hours.

NoteEven when it’s not in use, leave the BBPOS WisePOS E plugged in and powered on to receive automatic software updates.

## Access settings

To open the settings menu, swipe right from the left edge of the reader screen to reveal a Settings button. Tap the Settings button and enter the admin PIN 07139. From here, you can update your WiFi settings or generate a pairing code for device registration. Battery status is displayed at the top right of this screen. To close the settings menu, click the back arrow in the top left corner.

![](https://b.stripecdn.com/docs-statics-srv/assets/wisepos-settings-panel.527bfcfb5009c6fe05b374b6f717fa00.png)

Settings button

![](https://b.stripecdn.com/docs-statics-srv/assets/wisepos-pin-screen.9a2fe095ebd9ef5bbfe92a12e405411e.png)

Admin PIN screen

![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-settings-panel.4b22ea6d170de5988f950d72ef86f03a.png)

Settings menu

## Screen timeout

The screen times out when the reader isn’t connected to a power source. The default timeout of 1 hour is to improve battery performance. To update this value, go to the settings, select Appearance, then select a new screen timeout from the dropdown. The device screen turns on automatically after a device interaction occurs (such as touching the screen), or when the device enters the payments flow and a payment is initiated.

![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-settings-panel.4b22ea6d170de5988f950d72ef86f03a.png)

Settings menu

![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-appearance-menu.4abf84bd3fe14a1061eaed8b93d4bd70.png)

Appearance menu

![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-timeout-menu.1b82032fea1418ca99c72a71c071b713.png)

Timeout menu

## Connect the reader to the internet

Because the BBPOS WisePOS E is a smart reader, its reader software communicates directly with Stripe. Your point of sale application communicates with the reader through either a LAN (using a Terminal SDK) or the internet (using the server-driven integration). When communicating with the reader through the LAN, the reader must connect to the same local network as your point of sale application. If you’re running into issues connecting your reader to the internet, follow the troubleshooting steps to diagnose the issue.

### WiFi

To connect to WiFi or switch networks, go to settings, then select WiFi settings to choose the network and connect. Attempting to join a new network disconnects the reader from any existing wireless connection.

Your WiFi network must use WPA-Personal or WPA2-Personal encryption and be password protected. The BBPOS WisePOS E does not support non-password-protected networks, enterprise networks, or IPV6 networks. Follow the troubleshooting steps to diagnose issues with IPV6 networks. If needed, you can set a static IP on the device from the Wireless settings screen.

### Ethernet

Ethernet connectivity requires the use of an optional dock, which provides wired Ethernet connectivity and keeps your smart reader fully charged using the included charging cable. You can purchase the dock separately through the Stripe dashboard. The Ethernet Dock features a 10/100 Ethernet port and rubber feet for stable countertop use.

To set up the dock:

- Connect the Ethernet cable from your dock to your router.
- Connect the dock to power. It has a minimum power requirement of 5V-2A (10W) and includes a charging cable, which you can plug into any USB-A power adapter (not included).
- When both cables are connected, insert the reader into the dock.

To confirm that the reader is properly docked, verify the reader is charging and the Ethernet icon is visible in the status bar.

![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-battery-icon.d1e81d69ea61041f809e60d79e25be54.png)

Charging icon

![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-ethernet-icon.c5ae0533a503eb51ee9c8d587a854af0.png)

Ethernet icon

NoteThe dock’s charging cable must be USB-A to USB-C. The dock doesn’t work with a USB-C to USB-C connection.

The reader obtains an IP address using DHCP. As soon as the network cable is plugged in, the reader attempts to establish communication with Stripe.

![](https://b.stripecdn.com/docs-statics-srv/assets/wisepos-ethernet-dock.340a1e6d1be6fcab4fd2d577d79e5939.png)

## Network priority

The BBPOS WisePOS E prioritizes connecting through Ethernet if possible. Even if previously configured for WiFi, the reader switches to using an Ethernet connection when connected to the dock with a plugged-in Ethernet cable. If you remove the reader from the dock, it switches back to the WiFi connection.

The BBPOS WisePOS E resets its priority to Ethernet when rebooting. Even if previously configured for WiFi, the reader switches to Ethernet if it detects an Ethernet cable connection while starting up.

If the you dock the reader, but there is no Ethernet cable plugged in, it uses WiFi. Regardless of connectivity while docked, you can still connect to WiFi and manage networks on the device.

## Change the UI appearance

By default, the user interface of your BBPOS WisePOS E reader uses a dark theme.

![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-splash-screen.319df062b5b694a4ec91e1c309c48e48.png)

Welcome screen

![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-darkmode-pay.fdf5e2100ca53b54e100a28b8589b1d1.png)

Payment screen

![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-darkmode-subtotal.50779461be74aa98f600aef3e7715a16.png)

Tipping selection screen*

![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-darkmode-total.eb4f25263c136bed268f68a6f5e82933.png)

Total screen

![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-darkmode-approved.6eb33af4ca019de7621d07363e24dd8e.png)

Approved screen

*The tipping selection screen appears if on-reader tipping is configured.

You can change the appearance of the UI to use a different theme in the settings menu. Go to settings, then select Appearance, and select a new theme from the dropdown.

![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-settings-panel.4b22ea6d170de5988f950d72ef86f03a.png)

Settings menu

![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-appearance-menu.4abf84bd3fe14a1061eaed8b93d4bd70.png)

Appearance menu

![](https://b.stripecdn.com/docs-statics-srv/assets/wpe-theme-menu.fc7bd14827a7767e62c9f1bcd49110fa.png)

Theme menu

## Change the default reader language

The BBPOS WisePOS E supports changing the reader language in the settings menu. Swipe right across the screen to access the settings menu, and select your language.

## Accessories for the reader

You can design your own accessories for the BBPOS WisePOS E. To download the BBPOS WisePOS E mechanical design files (.STP), you must first review and accept our Terminal Design File License Agreement. By downloading the file below, you agree to the terms outlined in the license.

Download Stripe design files

## See also

- [Set up your integration](/terminal/payments/setup-integration)
- [WisePOS E reference](/terminal/readers/bbpos-wisepos-e)

The BBPOS and Chipper™ name and logo are trademarks or registered trademarks of BBPOS Limited in the United States and/or other countries. The Verifone® name and logo are either trademarks or registered trademarks of Verifone in the United States and/or other countries. Use of the trademarks does not imply any endorsement by BBPOS or Verifone.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Turn the reader on and off](#power)[Access settings](#settings)[Screen timeout](#screen_timeout)[Connect the reader to the internet](#connecting-to-the-internet)[Network priority](#network-priority)[Change the UI appearance](#ui-theme)[Change the default reader language](#default-reader-language)[Accessories for the reader](#wpe-accessories)[See also](#see-also)Products Used[Terminal](/terminal)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`