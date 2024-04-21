# BBPOS WisePOS E

The BBPOS WisePOS E is a countertop reader for Stripe Terminal apps. It connects to the Stripe Terminal SDK over the internet.

[connects](/terminal/payments/connect-reader?reader-type=internet)

This reader is compatible with the following integrations: JavaScript, iOS, Android, and React Native SDKs and server-driven.

For BBPOS WisePOS E readers, we recommend the server-driven integration, which uses the Stripe API instead of a Terminal SDK. To view the reader’s parts and features, see the BBPOS WisePOS E product sheet.

[server-driven integration](/terminal/payments/setup-integration?terminal-sdk-platform=server-driven)

[BBPOS WisePOS E product sheet](https://d37ugbyn3rpeym.cloudfront.net/terminal/product-sheets/wpe_product_sheet.pdf)

## LED status lights

The LEDs above the LCD display show the current status.

When the BBPOS WisePOS E is on, you can check the battery level in the left LED array.

When you connect to the BBPOS WisePOS E, you can check the reader status in the right LED array.

[contact support](https://support.stripe.com/contact/)

## Troubleshoot the reader

To begin troubleshooting, use the following common scenarios to help diagnose the issue.

To check connectivity, go to settings, then select WiFi settings. This displays all available WiFi networks. To see more details about the connection, tap on the connected network name.

[settings](/terminal/payments/setup-reader/bbpos-wisepos-e#settings)

- Make sure the network is connected and has internet access.

- The signal strength is good.

- The device has an IP address assigned.

- The subnet matches the one that your application is connected to.

You must connect both cables before inserting the reader into the dock. Remove the reader and re-insert into the dock.

If your reader doesn’t update, it’s possible that it can’t connect to Stripe. To check its connectivity to Stripe, go to settings, then select Diagnostics. This displays a list of troubleshooting tests. Check Stripe connectivity and ensure it says “Passed.” If the Stripe connectivity test fails, follow these steps.

[settings](/terminal/payments/setup-reader/bbpos-wisepos-e#settings)

[these steps](#reader-has-ip-address,-but-is-unable-to-communicate-with-stripe)

If you use a router, please refer to your router’s manual and reconfigure the networking setup.

Here are some common reasons why this happens with corresponding troubleshooting steps.

- Stripe endpoints can’t be accessed:Check your computer’s firewall/deny-list.

Stripe endpoints can’t be accessed:

[Stripe endpoints](/ips)

- Check your computer’s firewall/deny-list.

- The network source isn’t connected to the internet:In the case of bridged connections, ensure that the selected source is connected to the internet.In the case of router connections, refer to your router’s documentation to restart the network.

The network source isn’t connected to the internet:

- In the case of bridged connections, ensure that the selected source is connected to the internet.

- In the case of router connections, refer to your router’s documentation to restart the network.

Make sure the device running your point of sale application and your reader are able to communicate over the local network (typically this means they’re on the same subnet).

Stripe Terminal requires that both the point of sale application and the reader are able to interact with specific domain names, all of which are allowlisted on your network.

[specific domain names](/ips#stripe-terminal-domains)

Stripe Terminal also requires that your reader be assigned an IP address in one of the private IPv4 address blocks.

[private IPv4 address blocks](https://en.wikipedia.org/wiki/Private_network)

Some ISP provided routers only support IPV6 addresses which are not supported by the WisePOS E. Most 3rd party routers support IPV4 and IPV6. You may create a separate network using a 3rd party WiFI router and connect your WisePOS E to the new network.

Some DNS providers block DNS resolution of local IP addresses. You can check whether DNS resolution is successful by going to settings and selecting Diagnostics, and checking the DNS resolution test results. Stripe Terminal uses the partially qualified domain name *.[random-string].device.stripe-terminal-local-reader.net, which resolves to the local IP address of your BBPOS WisePOS E. If your DNS provider blocks local IP resolution, change your network settings to use one of the following DNS providers:

[settings](/terminal/payments/setup-reader/bbpos-wisepos-e#settings)

[change your network settings](https://support.stripe.com/questions/the-stripe-terminal-sdk-is-encountering-dns-errors-when-connecting-to-an-internet-reader)

- Cloudflare DNS (1.1.1.1 and 1.0.0.1)

[Cloudflare DNS](https://1.1.1.1/dns/)

- Google Public DNS (8.8.8.8 and 8.8.4.4)

[Google Public DNS](https://developers.google.com/speed/public-dns)

## Stripe reader software

Stripe maintains the software that controls the BBPOS WisePOS E. The reader receives updates automatically from Stripe when not in use. These can include improvements and required security updates from Stripe and our hardware partners. As reader software updates are made available, update your readers to the latest available version to continue using Stripe Terminal. Failing to install a required update can prevent a reader from accepting payments.

The reader restarts every day at midnight for PCI compliance, and disconnects from the POS app every morning. Leave your reader on and connected to power to receive automatic software updates. This ensures that updates happen at midnight (in the timezone of the assigned location) to avoid interruption to sales. If you unplug the reader at night, an update could start when you turn it back on. To manually check for an update, reboot the reader.

[assigned location](/terminal/fleet/locations)

The BBPOS WisePOS E software consists of four components: the reader application, firmware, configuration, and key identifier. The following table summarizes the latest version of each of these components for the countries where WisePOS E is available. You can find your reader’s versions in the Diagnostics menu by swiping in from the left edge of the screen, tapping Settings, and entering the admin code, 0-7-1-3-9.

- Fixed: Install error for language packs.

- Updated: 50% battery requirement when performing config or key update on battery.

- Fixed: Issue where readers were attempting to use 2nd Gen AC on contactless EMV.

- Added: Support for connecting to hidden Enterprise WPA or WPA2-EAP network.

- Added: Progress indicator for key, firmware, and config updates.

- Fix: Text size and copy changes and UI modifications for AAA accessiblity compliance

- Update: Payment Intent Support for Magstripe + PIN for EFTPOS

- Fix: Bug fixes to support Payment Intents when using offline mode

- Fix: An issue where iOS SDK 2.x versions returned nil for CardPresent object charges.paymentMethodDetails.cardPresent

- Bug fixes and stability improvements

- Update: SCA Support

- Fix: An issue where network screen running multiple connect calls could cause armada to be unauthenticated

- Update: Added issuer info in PaymentMethod bindings

- Update: Refund by PaymentIntent.id

- Update: Surface detected language from card in PaymentIntent

- Bug fixes and stability improvements

- Bug fixes and stability improvements

- Bug fixes and stability improvements

- Bug fixes and stability improvements

- Fixed: NFC logo missing on cart display

- Fixed: An issue where the reader app crashes during firmware updates

- Update: Improve recovery from an issue that causes the reader to stop responding

- Update: No longer need to check a box when connecting to hidden wifi networks

- Fixed: Disabling the payment tone works as intended on the WisePOS E

- Improved reliability and security of Stripe SDK to reader connectivity.

- Fixed issue where saved networks couldn’t always be forgotten.

- Fixed issue where ROM background downloads were occasionally interrupted.

- Fixed issue where language selection occasionally failed after factory reset.

- Improved reliability and security of Stripe SDK to reader connectivity.

- Devices now have a one hour screen timeout when the reader isn’t connected to a power source.

- Various improvements to animations during payment flow.

- Improved reliability and security of Stripe SDK to reader connectivity.

- Improved performance when processing several payments sequentially.

- Rolled out support for dark/light themes in reader update screen.

- Rolled out new default splash screen.

- Rolled out access to Appearance setting screen to switch between dark and light theme.

- Improved reliability and security of Stripe SDK to reader connectivity.

- Improved support for custom splash screens by applying opacity to status bar.

## Accessories for the reader

You can design your own accessories for the BBPOS WisePOS E. To download the BBPOS WisePOS E mechanical design files (.STP), you must first review and accept our Terminal Design File License Agreement. By downloading the file below, you agree to the terms outlined in the license.

[Terminal Design File License Agreement](https://stripe.com/legal/terminal-design)

Download Stripe design files

[Download Stripe design files](https://d37ugbyn3rpeym.cloudfront.net/terminal/bbpos_wpe_mechanical_design_files_and_guidelines.zip)

## See also

- Connect to a reader

[Connect to a reader](/terminal/payments/connect-reader)

- Collect payments

[Collect payments](/terminal/payments/collect-payment)

The BBPOS and Chipper™ name and logo are trademarks or registered trademarks of BBPOS Limited in the United States and/or other countries. The Verifone® name and logo are either trademarks or registered trademarks of Verifone in the United States and/or other countries. Use of the trademarks does not imply any endorsement by BBPOS or Verifone.
