htmlRequest a PAN data export | Stripe Documentation[Skip to content](#main-content)Request a PAN data export[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Fdata-migrations%2Fpan-export)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Fdata-migrations%2Fpan-export)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)
Fraud prevention[Protect against fraud](#)[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Get started](/docs/get-started)PAN data migrations# Request a PAN data export

Securely export sensitive primary account number data.### Thinking about leaving Stripe?

If you aren’t satisfied with our services, we’d like the opportunity to make things right. Contact us with your concerns and we’ll follow up directly.

We believe that our customers own the sensitive data they entrust to Stripe, and we work hard to make sure that you have access to this data—even if you’re moving elsewhere. If you decide to leave Stripe for another payment processor, we’ll work with your new processor’s team to securely transfer your credit card data.

To meet PCI compliance obligations, we can only transfer your card data to another PCI DSS Level 1-compliant payment processor. Stripe requires the following information about the processor receiving the data:

- The processor’s current PCI Attestation of Compliance (AOC), or their listing on Visa’s Global Registry of Service Providers.


- The processor’s PGP public encryption key, which must be 4096 bits or greater in length. This key must be hosted over HTTPS on one of the processor’s domain names referenced in their AOC or Visa Registry listing.



After you let us know who your new payment processor is, we can usually confirm if they meet these requirements.

## Migratable data

Stripe can help you migrate your customer card information to a new payment processor. To do this securely, Stripe prepares an encrypted JSON export file containing your data, including the card details of your customers, email addresses, and any attached metadata. We then arrange a secure transfer with your new processor, who uses this file to import the data into their system. You can start the migration process by contacting us with the name of your new payment processor.

`{
  "customers": [
    {
      "id": "cus_abc123def456",
      "email": "jenny.rosen@example.com",
      "description": "Jenny Rosen",
      "default_source": "card_edf214abc789",
      "metadata": {
        "color_preference": "turquoise",
        ...
      },
      "cards": [
        {
          "id": "card_edf214abc789",
          "number":"4242424242424242",
          "name": "Jenny Rosen",
          "exp_month": 1,
          "exp_year": 2020,
          "address_line1": "123 Main St.",
          "address_line2": null,
          "address_city": "Springfield",
          "address_state": "MA",
          "address_zip": "01101",
          "address_country": "US"
        },
        ...
      ]
    },
    ...
  ]
}`Stripe doesn’t export your account’s payment history, subscriptions, or other objects. Instead, use the API or Dashboard to retrieve this information. You can continue to access your data through the Dashboard and API after you migrate and no longer process payments with us, so long as you don’t close or delete your account.

## See also

- [Multiple accounts](/get-started/account/multiple-accounts)
- [Account checklist](/get-started/checklist/account)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Migratable data](#migratable-data)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`