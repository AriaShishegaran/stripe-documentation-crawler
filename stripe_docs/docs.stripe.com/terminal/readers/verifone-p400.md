# Verifone P400

This reader is no longer available for purchase. If you’re getting started with Stripe Terminal, we recommend viewing our current reader offerings.

[viewing our current reader offerings](/terminal/payments/setup-reader)

The Verifone P400 is a countertop reader for Stripe Terminal apps. It connects to the Stripe Terminal SDK over the internet.

[connects](/terminal/payments/connect-reader?reader-type=internet)

This reader is compatible with JavaScript, iOS, Android, and React Native SDKs. To view the reader’s parts and features, see the product sheet.

[product sheet](https://www.verifone.com/sites/default/files/2018-01/p400_datasheet_ltr_013018.pdf)

## Troubleshoot the reader

To begin troubleshooting, use the following common scenarios to help diagnose what’s broken.

Stripe provides two debug screens on the reader. Use these screens to help diagnose common connectivity and network issues. To access a debug screen, enter the following key sequences while on the splash screen:

To exit a debug screen, press 0 on the keypad. You can also program your app to re-render the screen by calling any of these functions:

- connectReader()

- collectPayment()

- setReaderDisplay()

Debug screens overlay the reader’s normal screen display, and can trigger only while on the reader screens shown above.

[reader screens](#reader-screens)

If your reader isn’t updating, it’s possible that it can’t connect to Stripe. Check its connectivity.

[connectivity](#checking-connectivity)

The Device Status debug screen shows the reader’s IP address, or No ETH if the device doesn’t have an IP address. Use the following steps to debug a No ETH condition.

[debug screen](#checking-connectivity)

Router networking

If using a router, please refer to your router’s manual, and reconfigure the networking setup.

Other IP-address

If the above steps don’t reveal an IP address on the reader, try these additional steps:

- Unplug and reconnect the Ethernet connection to the network source (that is, the modem for router networking, or your computer for bridged networking).

- Restart the reader with the network source attached to it. You can restart the reader by unplugging and reconnecting the power cable from the connector cable.

- Check the connectors for any broken hardware (such as bent pins).

Remember to connect production deployments to the merchant network through router networking.

The Connectivity debug screen indicates the connection status between the P400 and Stripe. Here are some common reasons for failing this test, with corresponding troubleshooting steps:

[debug screen](#checking-connectivity)

- Stripe endpoints can’t be accessed:Check your computer’s firewall/deny-list.

Stripe endpoints can’t be accessed:

[Stripe endpoints](/ips)

- Check your computer’s firewall/deny-list.

- The network source isn’t connected to the internet:In the case of bridged connections, ensure the selected source is connected to the internet.In the case of router connections, refer to your router’s documentation to restart the network.

The network source isn’t connected to the internet:

- In the case of bridged connections, ensure the selected source is connected to the internet.

- In the case of router connections, refer to your router’s documentation to restart the network.

Make sure your application and your reader are on the same local network.

- If your Verifone P400 is connected through WiFi, make sure the device running your point of sale application and the Verifone P400 can communicate over the local network (typically this means they’re on the same subnet).

- If your Verifone P400 is connected through Ethernet, make sure that your application is connected to the same switch, and that the switch has access to your router.

Stripe Terminal requires that both the point of sale application and the reader can interact with specific domain names, all of which are added to an allow-list on your network.

[specific domain names](/ips#stripe-terminal-domains)

Stripe Terminal also requires that your reader be assigned an IP address in one of the private IPv4 address blocks.

[private IPv4 address blocks](https://en.wikipedia.org/wiki/Private_network)

Some DNS providers block DNS resolution of local IP addresses. Stripe Terminal uses the partially qualified domain name *.[random-string].device.stripe-terminal-local-reader.net, which resolves to the local IP address of your Verifone P400. If your DNS provider blocks local IP resolution, change your network settings to use one of the following DNS providers:

- Cloudflare DNS (1.1.1.1 and 1.0.0.1)

[Cloudflare DNS](https://1.1.1.1/dns/)

- Google Public DNS (8.8.8.8 and 8.8.4.4)

[Google Public DNS](https://developers.google.com/speed/public-dns)

## Stripe reader software

Stripe maintains the software that controls the Verifone P400. The reader receives updates automatically from Stripe when not in use. Read about reader software updates for details. These can include improvements and required security updates from Stripe and our hardware partners. As reader software updates are made available, update your readers to the latest available version to continue using Stripe Terminal. Failing to install a required update can prevent a reader from accepting payments.

[reader software updates](/terminal/payments/setup-reader#reader-software-updates)

The reader restarts every day at midnight for PCI compliance, and disconnects from the POS app every morning. Leave your reader connected to power to receive automatic software updates. This ensures that updates happen at midnight (in the timezone of the assigned location) to avoid interruption to sales. If you unplug the reader at night, an update could start when you turn it back on. To manually check for an update, reboot the reader.

[assigned location](/terminal/fleet/locations)

You can always check the current reader version by pressing 0-4-2-6-8.

For additional instruction on maintaining PCI compliance when installing updates to your Verifone P400 device, refer to the reader PCI implementation guide.

[PCI compliance](/security/guide#validating-pci-compliance)

[implementation guide](https://stripe.com/files/terminal/terminal_implementation_guide.pdf)

The BBPOS and Chipper™ name and logo are trademarks or registered trademarks of BBPOS Limited in the United States and/or other countries. The Verifone® name and logo are either trademarks or registered trademarks of Verifone in the United States and/or other countries. Use of the trademarks does not imply any endorsement by BBPOS or Verifone.
