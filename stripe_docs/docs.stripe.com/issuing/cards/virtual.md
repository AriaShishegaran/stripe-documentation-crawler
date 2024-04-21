# Virtual cards with Issuing

You can retrieve or display virtual card details through the Dashboard, the API, or by using Issuing Elements. PCI-DSS rules protect cardholder data, and not all methods of card information retrieval are PCI-DSS compliant.

[Issuing Elements](/issuing/elements)

[PCI-DSS](https://stripe.com/guides/pci-compliance)

## Display virtual card details to cardholders

You can use Issuing Elements to display virtual card details to your cardholders without this information passing through your servers. This method is fully PCI-DSS compliant, and we recommend it for most Issuing users. Stripe offers Issuing Elements as a part of Stripe.js.

[Issuing Elements](/issuing/elements)

[Stripe.js](/js)

## Retrieve virtual card details

For PCI-DSS compliance, we recommend limiting retrieval of virtual card information to the Dashboard or Issuing Elements. If you use the API to retrieve card information, or if you export virtual card information from the Dashboard, store it in a password manager or otherwise encrypt it.

You can retrieve both the full unredacted card number and CVC from the API. For security reasons, you can only use these fields with virtual cards in live mode, and we omit them unless you explicitly request them with the expand property. You can only retrieve these fields for physical cards in test mode. Additionally, you can only access them through the Retrieve a card endpoint.

[expand](/api/expanding_objects)

[test mode](/keys#test-live-modes)

[Retrieve a card](/api/issuing/cards/retrieve)

## Details about PCI-DSS

If you are generating virtual cards for your own use, you are not required to attain PCI-DSS compliance for Issuing activity. If you are generating virtual cards for use by your users, you may be considered a Service Provider under PCI-DSS rules. Service Providers must be PCI-DSS compliant.

If you accept payments through Stripe, read more about your PCI-DSS obligations. These obligations are in addition to requirements noted above.

[PCI-DSS obligations](https://stripe.com/guides/pci-compliance)
