htmlBBPOS WisePOS E | Stripe Documentation[Skip to content](#main-content)BBPOS WisePOS E reference[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Freaders%2Fbbpos-wisepos-e)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Freaders%2Fbbpos-wisepos-e)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)[Smart readers](/docs/terminal/smart-readers)# BBPOS WisePOS E

Learn about the BBPOS WisePOS E reader.Available in:![](https://b.stripecdn.com/docs-statics-srv/assets/wisepos-floating-tall.e8478124cda0e088b2e19f503f574f53.png)

The BBPOS WisePOS E is a countertop reader for Stripe Terminal apps. It connects to the Stripe Terminal SDK over the internet.

This reader is compatible with the following integrations: JavaScript, iOS, Android, and React Native SDKs and server-driven.

For BBPOS WisePOS E readers, we recommend the server-driven integration, which uses the Stripe API instead of a Terminal SDK. To view the reader’s parts and features, see the BBPOS WisePOS E product sheet.

## LED status lights

The LEDs above the LCD display show the current status.

### Battery and charging status

When the BBPOS WisePOS E is on, you can check the battery level in the left LED array.

LEDsMeaningCharging or full charge### Contactless and reader status

When you connect to the BBPOS WisePOS E, you can check the reader status in the right LED array.

LEDsMeaningReader is in bootloader mode.Reader integrity check failed or reader tampered.(2 seconds) Reader is experiencing a hard fault and might need replacing. Please[contact support](https://support.stripe.com/contact/).## Troubleshoot the reader

To begin troubleshooting, use the following common scenarios to help diagnose the issue.

### Reader is unable to connect

To check connectivity, go to settings, then select WiFi settings. This displays all available WiFi networks. To see more details about the connection, tap on the connected network name.

- Make sure the network is connected and has internet access.
- The signal strength is good.
- The device has an IP address assigned.
- The subnet matches the one that your application is connected to.

### Reader is unable to connect to Ethernet, even though docked

You must connect both cables before inserting the reader into the dock. Remove the reader and re-insert into the dock.

### Reader is unable to update

If your reader doesn’t update, it’s possible that it can’t connect to Stripe. To check its connectivity to Stripe, go to settings, then select Diagnostics. This displays a list of troubleshooting tests. Check Stripe connectivity and ensure it says “Passed.” If the Stripe connectivity test fails, follow these steps.

NoteIf you use a router, please refer to your router’s manual and reconfigure the networking setup.

### Reader has IP address, but is unable to communicate with Stripe

Here are some common reasons why this happens with corresponding troubleshooting steps.

- Stripe endpoints can’t be accessed:

  - Check your computer’s firewall/deny-list.


- The network source isn’t connected to the internet:

  - In the case of bridged connections, ensure that the selected source is connected to the internet.
  - In the case of router connections, refer to your router’s documentation to restart the network.



### Reader has IP address and can communicate with Stripe, but not with your point of sale application

Make sure the device running your point of sale application and your reader are able to communicate over the local network (typically this means they’re on the same subnet).

Stripe Terminal requires that both the point of sale application and the reader are able to interact with specific domain names, all of which are allowlisted on your network.

Stripe Terminal also requires that your reader be assigned an IP address in one of the private IPv4 address blocks.

Some ISP provided routers only support IPV6 addresses which are not supported by the WisePOS E. Most 3rd party routers support IPV4 and IPV6. You may create a separate network using a 3rd party WiFI router and connect your WisePOS E to the new network.

Some DNS providers block DNS resolution of local IP addresses. You can check whether DNS resolution is successful by going to settings and selecting Diagnostics, and checking the DNS resolution test results. Stripe Terminal uses the partially qualified domain name *.[random-string].device.stripe-terminal-local-reader.net, which resolves to the local IP address of your BBPOS WisePOS E. If your DNS provider blocks local IP resolution, change your network settings to use one of the following DNS providers:

- [Cloudflare DNS](https://1.1.1.1/dns/)(`1.1.1.1`and`1.0.0.1`)
- [Google Public DNS](https://developers.google.com/speed/public-dns)(`8.8.8.8`and`8.8.4.4`)

## Stripe reader software

Stripe maintains the software that controls the BBPOS WisePOS E. The reader receives updates automatically from Stripe when not in use. These can include improvements and required security updates from Stripe and our hardware partners. As reader software updates are made available, update your readers to the latest available version to continue using Stripe Terminal. Failing to install a required update can prevent a reader from accepting payments.

The reader restarts every day at midnight for PCI compliance, and disconnects from the POS app every morning. Leave your reader on and connected to power to receive automatic software updates. This ensures that updates happen at midnight (in the timezone of the assigned location) to avoid interruption to sales. If you unplug the reader at night, an update could start when you turn it back on. To manually check for an update, reboot the reader.

### Reader software version

The BBPOS WisePOS E software consists of four components: the reader application, firmware, configuration, and key identifier. The following table summarizes the latest version of each of these components for the countries where WisePOS E is available. You can find your reader’s versions in the Diagnostics menu by swiping in from the left edge of the screen, tapping Settings, and entering the admin code, 0-7-1-3-9.

CountriesReaderFirmwareConfigurationUnited States`2.22.2.0``5.00.01.26``szzz_us_v13`Canada`2.22.2.0``5.00.04.26``szzz_ca_v11`Australia`2.22.2.0``5.00.01.26.eftpos``szzz_prod_apac_on_v9`MalaysiaNew Zealand`2.22.2.0``5.00.01.26``szzz_prod_apac_on_v4`Singapore`2.22.2.0``5.00.01.26``szzz_prod_apac_off_v3`United KingdomIrelandFinland`2.22.2.0``5.00.01.26``szzz_prod_eu_off_v7`AustriaBelgiumDenmarkFranceItalyGermanyNetherlandsSpainSwedenCzech RepublicLuxembourgPortugalSwitzerlandNorway`2.22.2.0``5.00.01.26``szzz_prod_eu_on_v4`### Reader software changelog

2024-04-18 (version 2.22.2.0)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Fixed: Install error for language packs.
- Updated: 50% battery requirement when performing config or key update on battery.
- Fixed: Issue where readers were attempting to use 2nd Gen AC on contactless EMV.
- Added: Support for connecting to hidden Enterprise WPA or WPA2-EAP network.
- Added: Progress indicator for key, firmware, and config updates.

2024-03-18 (version 2.21.2.0)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Fix: Text size and copy changes and UI modifications for AAA accessiblity compliance
- Update: Payment Intent Support for Magstripe + PIN for EFTPOS
- Fix: Bug fixes to support Payment Intents when using offline mode

2024-02-08 (version 2.20.4.0)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Fix: An issue where iOS SDK 2.x versions returned nil for CardPresent object charges.paymentMethodDetails.cardPresent

2024-02-08 (version 2.20.3.0)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Bug fixes and stability improvements

2023-12-11 (version 2.19.2.0)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Update: SCA Support
- Fix: An issue where network screen running multiple connect calls could cause armada to be unauthenticated
- Update: Added issuer info in PaymentMethod bindings
- Update: Refund by PaymentIntent.id
- Update: Surface detected language from card in PaymentIntent

2023-11-16 (version 2.18.9.0)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Bug fixes and stability improvements

2023-11-08 (version 2.18.5.0)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Bug fixes and stability improvements

2023-10-18 (version 2.17.8.0)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Bug fixes and stability improvements

2023-09-21 (version 2.16.7.0)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Bug fixes and stability improvements

2023-07-12 (version 2.15.5.0)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Fixed: NFC logo missing on cart display
- Fixed: An issue where the reader app crashes during firmware updates
- Update: Improve recovery from an issue that causes the reader to stop responding
- Update: No longer need to check a box when connecting to hidden wifi networks
- Fixed: Disabling the payment tone works as intended on the WisePOS E

2023-06-12 (version 2.14.3.0)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Improved reliability and security of Stripe SDK to reader connectivity.
- Fixed issue where saved networks couldn’t always be forgotten.

2023-04-03 (version 2.12.2.3)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Fixed issue where ROM background downloads were occasionally interrupted.
- Fixed issue where language selection occasionally failed after factory reset.

2023-03-14 (version 2.11.4.0)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Improved reliability and security of Stripe SDK to reader connectivity.

2023-02-06 (version 2.10.2.0)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Devices now have a one hour screen timeout when the reader isn’t connected to a power source.

2023-01-04 (version 2.9.2.0)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Various improvements to animations during payment flow.
- Improved reliability and security of Stripe SDK to reader connectivity.

2022-10-17 (version 2.8.4.0)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Improved performance when processing several payments sequentially.

2022-09-19 (version 2.7.7.0)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Rolled out support for dark/light themes in reader update screen.

2022-06-13 (version 2.4.2.3)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Rolled out new default splash screen.
- Rolled out access to Appearance setting screen to switch between dark and light theme.

2022-04-13 (version 2.2.3.0)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Improved reliability and security of Stripe SDK to reader connectivity.
- Improved support for custom splash screens by applying opacity to status bar.

## Accessories for the reader

You can design your own accessories for the BBPOS WisePOS E. To download the BBPOS WisePOS E mechanical design files (.STP), you must first review and accept our Terminal Design File License Agreement. By downloading the file below, you agree to the terms outlined in the license.

Download Stripe design files

## See also

- [Connect to a reader](/terminal/payments/connect-reader)
- [Collect payments](/terminal/payments/collect-payment)

The BBPOS and Chipper™ name and logo are trademarks or registered trademarks of BBPOS Limited in the United States and/or other countries. The Verifone® name and logo are either trademarks or registered trademarks of Verifone in the United States and/or other countries. Use of the trademarks does not imply any endorsement by BBPOS or Verifone.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[LED status lights](#led-status-lights)[Troubleshoot the reader](#troubleshooting)[Stripe reader software](#stripe-reader-software)[Accessories for the reader](#wpe-accessories)[See also](#see-also)Products Used[Terminal](/terminal)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`