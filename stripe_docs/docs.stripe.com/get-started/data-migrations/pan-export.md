# Request a PAN data export

If you aren’t satisfied with our services, we’d like the opportunity to make things right. Contact us with your concerns and we’ll follow up directly.

[Contact us](https://support.stripe.com/contact?email=true&subject=Migration+away+from+Stripe)

We believe that our customers own the sensitive data they entrust to Stripe, and we work hard to make sure that you have access to this data—even if you’re moving elsewhere. If you decide to leave Stripe for another payment processor, we’ll work with your new processor’s team to securely transfer your credit card data.

To meet PCI compliance obligations, we can only transfer your card data to another PCI DSS Level 1-compliant payment processor. Stripe requires the following information about the processor receiving the data:

[PCI compliance](/security/guide#validating-pci-compliance)

- The processor’s current PCI Attestation of Compliance (AOC), or their listing on Visa’s Global Registry of Service Providers.

The processor’s current PCI Attestation of Compliance (AOC), or their listing on Visa’s Global Registry of Service Providers.

[Visa’s Global Registry of Service Providers](https://usa.visa.com/splisting/splistingindex.html)

- The processor’s PGP public encryption key, which must be 4096 bits or greater in length. This key must be hosted over HTTPS on one of the processor’s domain names referenced in their AOC or Visa Registry listing.

The processor’s PGP public encryption key, which must be 4096 bits or greater in length. This key must be hosted over HTTPS on one of the processor’s domain names referenced in their AOC or Visa Registry listing.

After you let us know who your new payment processor is, we can usually confirm if they meet these requirements.

[let us know](https://support.stripe.com/contact?email=true&subject=Migration+away+from+Stripe)

## Migratable data

Stripe can help you migrate your customer card information to a new payment processor. To do this securely, Stripe prepares an encrypted JSON export file containing your data, including the card details of your customers, email addresses, and any attached metadata. We then arrange a secure transfer with your new processor, who uses this file to import the data into their system. You can start the migration process by contacting us with the name of your new payment processor.

[metadata](/api#metadata)

[contacting us](https://support.stripe.com/contact?email=true&subject=Migration+away+from+Stripe)

Stripe doesn’t export your account’s payment history, subscriptions, or other objects. Instead, use the API or Dashboard to retrieve this information. You can continue to access your data through the Dashboard and API after you migrate and no longer process payments with us, so long as you don’t close or delete your account.

## See also

- Multiple accounts

[Multiple accounts](/get-started/account/multiple-accounts)

- Account checklist

[Account checklist](/get-started/checklist/account)
