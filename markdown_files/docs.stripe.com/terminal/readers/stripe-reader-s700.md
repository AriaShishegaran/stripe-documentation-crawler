htmlStripe Reader S700 | Stripe Documentation[Skip to content](#main-content)Stripe Reader S700 reference[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Freaders%2Fstripe-reader-s700)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Freaders%2Fstripe-reader-s700)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)[Smart readers](/docs/terminal/smart-readers)# Stripe Reader S700

Learn about Stripe Reader S700.Stripe Reader S700Get notified when Stripe Reader S700 is available in your country.

![](https://b.stripecdn.com/docs-statics-srv/assets/S700-3D.041eca5dfd580cdc451a41020b4dd45a.png)

The Stripe Reader S700 is an Android-based smart reader for countertop and handheld use. You can customize the on-reader checkout UI using both prebuilt and custom elements.

The Stripe Terminal SDK connects to the reader over the internet or LAN. This reader is compatible with JavaScript SDK, iOS SDK, Android SDK, React Native SDK, and server-driven integrations.

For the Stripe Reader S700, we recommend the server-driven integration, which uses the Stripe API instead of a Terminal SDK. To view the reader’s parts and features, see the Stripe Reader S700 product sheet.

WarningStripe readers aren’t liquid-proof and we recommend that users make appropriate efforts to make sure their devices remain dry. If your device has experienced liquid ingress, we recommend that you stop using the device and let it dry thoroughly before attempting to re-use or charge the device. If your device doesn’t properly operate or charge properly after drying, you need to replace it.

## Battery and charging status

When the Stripe Reader S700 is on, you can check the battery level in the charging LED indicator.

LEDsMeaningThe reader is fully charged with the power cable connected.(flashing) The reader is charging.The reader’s battery level is low (10-20% remaining).The reader’s battery level is critically low (1-9% remaining) or drained (1% remaining).The reader is off, or the reader is on with the power cable disconnected.## Troubleshoot the reader

To begin troubleshooting, use the following common scenarios to help diagnose the issue.

### The reader can’t connect

To check connectivity, go to the reader settings and select WiFi settings. This displays all available WiFi networks. To see more details about the connection, tap the connected network name.

- Make sure the network is connected and has internet access.
- The signal strength is good.
- The device has an IP address assigned.
- The subnet matches the one that your application is connected to.

### The reader won’t update

If your reader doesn’t update, it’s possible that it can’t connect to Stripe. To check its connectivity to Stripe, go to the reader settings, then select Diagnostics. This displays a list of troubleshooting tests. Check Stripe connectivity and make sure it says Passed. If the Stripe connectivity test fails, follow the troubleshooting steps.

If you use a router, refer to your router’s manual and reconfigure the networking setup.

### The reader has an IP address, but can’t communicate with Stripe

Here are some common reasons why this happens, with corresponding troubleshooting steps.

- The reader can’t access Stripe endpoints:

  - Check your computer’s firewall and deny list.


- The network source isn’t connected to the internet:

  - In the case of bridged connections, make sure that the selected source is connected to the internet.
  - In the case of router connections, refer to your router’s documentation to restart the network.



### The reader has an IP address and can communicate with Stripe, but not with your point of sale application

Make sure the device running your point of sale application and your reader can communicate over the local network (typically this means they’re on the same subnet).

Stripe Terminal requires that both the point of sale application and the reader can interact with specific domain names, all of which are allowlisted on your network.

Stripe Terminal also requires that your reader is assigned an IP address in one of the private IPv4 address blocks.

Some ISP-provided routers only support IPV6 addresses, which the Stripe Reader S700 doesn’t support. Most third-party routers support IPV4 and IPV6. You can create a separate network using a third-party WiFi router and connect your Stripe Reader S700 to the new network.

Some DNS providers block DNS resolution of local IP addresses. You can check whether DNS resolution is successful by going to the reader settings, selecting Diagnostics, and checking the DNS resolution test results. Stripe Terminal uses the partially qualified domain name *.[random-string].device.stripe-terminal-local-reader.net, which resolves to the local IP address of your Stripe Reader S700. If your DNS provider blocks local IP resolution, change your network settings to use one of the following DNS providers:

- [Cloudflare DNS](https://1.1.1.1/dns/)(`1.1.1.1`and`1.0.0.1`)
- [Google Public DNS](https://developers.google.com/speed/public-dns)(`8.8.8.8`and`8.8.4.4`)

## Stripe reader software

Stripe maintains the software that controls the Stripe Reader S700. The reader receives updates automatically from Stripe when not in use. These can include improvements and required security updates from Stripe and our hardware partners. As reader software updates are made available, update your readers to the latest available version to continue using Stripe Terminal. Failing to install a required update can prevent a reader from accepting payments.

The reader restarts every day at midnight for PCI compliance, and disconnects from the POS app every morning. Leave your reader on and connected to power to receive automatic software updates. This ensures that updates happen at midnight (in the timezone of the assigned location) to avoid interruption to sales. If you unplug the reader at night, an update could start when you turn it back on. To manually check for an update, reboot the reader.

### Reader software version

The Stripe Reader S700 software consists of four components: the reader application, firmware, configuration, and key identifier. The following table summarizes the latest version of each of these components for the countries where the Stripe Reader S700 is available.

You can find your reader’s versions in the Diagnostics menu by swiping in from the left edge of the screen, tapping Settings, and entering the admin code, 0-7-1-3-9.

CountriesReaderFirmwareConfigurationUnited States`2.22.2.0``1.00.00.16.SZZZ.03``szzz_us_v3`## See also

- [Connect to a reader](/terminal/payments/connect-reader)
- [Collect payments](/terminal/payments/collect-payment)

The BBPOS and Chipper™ name and logo are trademarks or registered trademarks of BBPOS Limited in the United States and/or other countries. The Verifone® name and logo are either trademarks or registered trademarks of Verifone in the United States and/or other countries. Use of the trademarks does not imply any endorsement by BBPOS or Verifone.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Battery and charging status](#battery-charging-status)[Troubleshoot the reader](#troubleshooting)[Stripe reader software](#stripe-reader-software)[See also](#see-also)Products Used[Terminal](/terminal)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`