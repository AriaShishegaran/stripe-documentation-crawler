# Set up Stripe Reader S700

Get notified when Stripe Reader S700 is available in your country.

[Get notified](https://dashboard.stripe.com/terminal/s700_notify)

Stripe Reader S700 is an Android-based smart reader for countertop and handheld use. You can customize the on-reader checkout UI using a suite of pre-built and custom elements.

The Stripe Terminal SDK connects to the reader over the internet or LAN. This reader is compatible with the following integrations:

[Stripe Terminal SDK connects to the reader](/terminal/payments/connect-reader?reader-type=internet)

- JavaScript SDK

- iOS SDK

- Android SDK

- React Native SDK

- Server-driven

For Stripe Reader S700 readers, we recommend the server-driven integration, which uses the Stripe API instead of a Terminal SDK. To view the reader’s parts and features, see the Stripe Reader S700 product sheet.

[server-driven integration](/terminal/payments/setup-integration?terminal-sdk-platform=server-driven)

[Stripe Reader S700 product sheet](https://d37ugbyn3rpeym.cloudfront.net/docs/terminal/S700_Product_Sheet_legal_0240314.pdf)

## Turn the reader on and off

Connect the reader to power by plugging the provided USB-C cable into the port on the left side of your reader. Connect the opposite end of the USB-C cable to the provided power adapter and plug it into a power outlet.

Stripe Reader S700

After the reader is fully charged, hold down the power button on the right side until the screen turns on. After the device powers on, press the power button to sleep or wake the device. To fully power off the device, hold down the power button until the power off option appears on the screen, then select it.

In a countertop deployment, leaving the device on for extended periods is expected. With a full charge, you can expect the battery to last about 15 hours.

Even when not in use, leave Stripe Reader S700 plugged in and powered on to receive automatic software updates.

## Access settings

To open the settings menu, swipe right from the left edge of the reader screen to reveal a Settings button. Tap the Settings button and enter the admin PIN 07139. From here, you can update your WiFi settings or generate a pairing code for device registration. Battery status is displayed at the top right of this screen. To close the settings menu, click the back arrow in the top left corner.

Settings button

Admin PIN screen

Settings menu

## Screen timeout

The screen times out when the reader isn’t connected to a power source. The default timeout of 1 hour is to improve battery performance. To update this value, go to the settings, select Appearance, then select a new screen timeout from the dropdown. The device screen turns on automatically after a device interaction occurs (such as touching the screen or picking up the device), or when the device enters the payments flow and a payment is initiated.

[settings](#settings)

Settings menu

Appearance menu

Timeout menu

## Connect the reader to the internet

Because the Stripe Reader S700 is a smart reader, its reader software communicates directly with Stripe. Your point of sale application communicates with the reader through either a LAN (using a Terminal SDK) or the internet (using the server-driven integration). When communicating with the reader through the LAN, the reader must connect to the same local network as your point of sale application. If you’re running into issues connecting your reader to the internet, follow the troubleshooting steps to diagnose the issue.

[server-driven integration](/terminal/payments/setup-integration?terminal-sdk-platform=server-driven)

[troubleshooting steps](/terminal/readers/stripe-reader-s700#troubleshooting)

To connect to WiFi or switch networks, go to settings, then select WiFi settings to choose the network and connect. Attempting to join a new network disconnects the reader from any existing wireless connection.

[settings](#settings)

Your WiFi network must use WPA-Personal or WPA2-Personal encryption and be password protected. The Stripe Reader S700 does not support non-password-protected networks, enterprise networks, or IPV6 networks. Follow the troubleshooting steps to diagnose issues with IPV6 networks. If needed, you can set a static IP on the device from the Wireless settings screen.

## Network priority

The Stripe Reader S700 prioritizes connecting through Ethernet if possible. Even if previously configured for WiFi, the reader switches to using an Ethernet connection when connected to the dock with a plugged-in Ethernet cable. If you remove the reader from the dock, it switches back to the WiFi connection.

The Stripe Reader S700 resets its priority to Ethernet when rebooting. Even if previously configured for WiFi, the reader switches to Ethernet if it detects an Ethernet cable connection while starting up.

If the you dock the reader, but there is no Ethernet cable plugged in, it uses WiFi. Regardless of connectivity while docked, you can still connect to WiFi and manage networks on the device.

## Change the UI appearance

By default, the user interface of your Stripe Reader S700 reader uses a light theme.

Welcome screen

Payment screen

Processing screen

Approved screen

You can change the appearance of the UI to use a different theme in the settings menu. Go to settings, then select Appearance, and select a new theme from the dropdown.

[settings](#settings)

Settings menu

Appearance menu

Theme menu

## Change the default reader language

Stripe Reader S700 supports changing the reader language in the reader settings menu. Swipe right across the screen to access the settings menu, and select your language.

[reader settings](#access-settings)

## Accessories

You can design your own accessories for the Stripe Reader S700. To download the Stripe Reader S700 mechanical design files (.STP), you must first review and accept our Terminal Design File License Agreement. By downloading the file below, you agree to the terms outlined in the license.

[Terminal Design File License Agreement](https://stripe.com/legal/terminal-design)

Download Stripe design files

[Download Stripe design files](https://d37ugbyn3rpeym.cloudfront.net/terminal/Stripe-Reader-S700-Design-File.zip)

## See also

- Set up your integration

[Set up your integration](/terminal/payments/setup-integration)

- Stripe Reader S700 reference

[Stripe Reader S700 reference](/terminal/readers/stripe-reader-s700)
