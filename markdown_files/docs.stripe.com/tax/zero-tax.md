htmlZero tax amounts and reverse charges | Stripe Documentation[Skip to content](#main-content)Zero tax amounts and reverse charges[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fzero-tax)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fzero-tax)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)[Calculate tax](/docs/tax/calculating)# Zero tax amounts and reverse charges

Learn about cases when Stripe Tax calculates zero tax.NoteLog in or sign up for Stripe to activate Stripe Tax.

Stripe Tax returns a tax calculation result on every request. However, Tax isn’t collected on a transaction in some situations, and the resulting tax amount is zero. For example, if you’re expanding tax_amounts on an invoice, you might see something like:

`{
  "id": "in_1HF0KNFsnTpWVWVzFDgSizOj",
  "object": "invoice",
  ...
  "total_details": {
    "amount_tax": 0,
    "breakdown": {
      "taxes": [
        {
          "amount": 0,
          "taxability_reason": "not_collecting",
          "rate": {
            "id": "txr_1HHwa4Jm3J7Jh9FBnYJ9glJZ",
            "object": "tax_rate",
            "description": "VAT Germany",
            "display_name": "VAT",
            "country": "DE",
            "created": 1597863856,
            "inclusive": false,
            "jurisdiction": "DE",
            "livemode": false,
            "metadata": {},
            "percentage": 0.0,
            "state": null,
            "tax_type": "vat",
            "active": false,
          }
        }
      ]
    },
  },
  ...
}`The API returns the reason for a tax result in the taxability_reason field.

The most common reasons for a zero tax result are the following:

Reasontaxability_reasonExplanationNot registered`not_collecting`You must register before collecting tax in a jurisdiction. You can specify where you’re registered to collect tax on[the Tax settings page](https://dashboard.stripe.com/settings/tax).Exempt or zero-rated products`product_exempt`Certain products are exempt from tax or zero-rated. In both cases the buyer doesn’t pay tax.Reverse charge`reverse_charge`Transactions between two businesses might be subject to reverse charge. In these cases, the buyer is responsible for accounting for the VAT due under the reverse charge.Exempt customers`customer_exempt`Some customers are exempt from paying indirect tax in certain jurisdictions. You can specify when a customer is exempt on the Customer object.Excluded territory`not_supported`Some countries have administrative subdivisions or territories, with the geographic region being outside the scope of the associated country’s VAT system. A list of these excluded territories is below.![](https://b.stripecdn.com/docs-statics-srv/assets/taxability.cfcdfce0aab058702149b65a5804547a.png)

The tax outcome for each payment is available when viewing a payment in the Dashboard under Taxability.

## Situations where Stripe calculates zero tax

Stripe Tax calculates zero tax in the following situations:

### Not registered

Taxing authorities require businesses to obtain a license or otherwise register before starting to collect tax in their jurisdiction. Each jurisdiction has their own rules regarding when you’re obligated to register and begin collecting and remitting tax. Obligations can arise from, but are not limited to, a physical presence in the jurisdiction or from reaching a threshold of sales into a jurisdiction. For example, as of February 2021, for businesses based outside of California (for example, no physical presence), you only need to register when you surpass 500,000 USD in sales.

Stripe automatically aggregates and analyzes your transactions and compares them to local thresholds. You can see these and add your registrations on the Thresholds tab.

Learn more about how to register for sales tax, VAT, and GST in each location and, if you’re a Connect platform, how to use the Registrations API to manage tax registrations.

### Exempt or zero rated products

Products might be exempt or nontaxable in some jurisdictions. For example, as of February 2021, the state of California considers software as a service to be a nontaxable service. The buyer pays no tax and the seller usually can’t reclaim any credits from costs associated with producing the product.

Products can also be zero-rated, meaning while they’re technically taxable, the applied rate is 0%. For example, as of February 2021, children’s clothing is zero-rated in Ireland. The buyer pays no tax, however the seller might be able to reclaim credits from costs associated with producing the product.

The tax treatment of products not only varies by jurisdiction but is subject to change. If you don’t want to collect tax on a given product, you can assign the product tax code Nontaxable (txcd_00000000) to it, to make sure Stripe Tax treats it as a nontaxable product. Otherwise, Stripe Tax automatically determines when a product is exempt or zero rated.

### Reverse charges

While in most transactions, the seller is responsible for collecting and remitting tax owed by the buyer, in a reverse charge transaction the buyer must calculate and remit the tax. In that case, the seller’s invoice specifies that the transaction is a reverse charge and doesn’t include tax in the total amount. A reverse charge is common in cross-border B2B supply of services. For example, for businesses with an origin address in the EU, the following logic applies:

Buyers fromB2CB2BSame EU countryCharge VATCharge VATDifferent EU countryCharge VATNo VAT (reverse charge)Stripe Tax automatically applies the right logic depending on the presence of a tax ID and the jurisdictions involved in the transaction.

For transactions with inclusive tax behavior where reverse charge applies, the buyer pays the full unit_amount Price, but isn’t charged tax. In these cases, a “Reverse Charge” indicator appears in the Stripe Dashboard, and the Invoice reads “Tax to be paid on reverse charge basis” instead of zero.

If you haven’t collected the customer’s tax ID in Stripe, but you want to handle their transactions as reverse charges, set their customer.tax_exempt attribute to reverse. If Checkout creates a one-time payment, the exemption status is instead captured as customer_details in the Checkout Session object. You’re responsible for making sure that customer information is accurate (including a tax identification number).

The following examples show invoices generated with and without a known customer tax ID:

- [Customer’s tax ID automates reverse charge (PDF)](https://stripe.com/files/docs/billing/taxes/example-reverse-charge.pdf)
- [Explicitly set reverse charge (PDF)](https://stripe.com/files/docs/billing/taxes/example-reverse-charge-customer.pdf)

Stripe displays the provided customer tax ID on an invoice, regardless of whether it’s valid. Stripe Tax automatically validates the tax ID format against the expected format and the tax ID value against external tax authority systems for certain countries.

Learn more about Tax IDs

[Exempt customers](#exempt-customers)Exempt customers are those who under a jurisdiction’s rules can make tax-exempt purchases. Each taxing jurisdiction determines the type of individuals or entities who can make tax-exempt purchases. Common examples are nonprofit organizations and government entities. If you have customers that are exempt from paying tax, you can specify this by setting the exempt status of a customer and providing the customer ID when creating a subscription, invoice, or Checkout Session. You can manage customer exempt status using the Dashboard or using the API by setting the customer.tax_exempt field.

For transactions with inclusive tax behavior where the customer is exempt, the buyer pays the full unit_amount Price, but there’s no tax charged. In these cases, an “Exempt” indicator appears in the Stripe Dashboard and the Invoice reads “Customer is tax exempt” instead of zero.

Download example exempt invoice PDF

Stripe Tax automatically calculates an exemption on the transaction when you set the customer.tax_exempt field, but it doesn’t perform any validation of required documentation for supporting an exemption such as customer exemption certificates. You’re responsible for determining and fulfilling any obligation to validate your customer’s exempt status and collect any required documentation such as an exemption certificate.

[Excluded territories](#excluded-territories)NoteStripe Tax fees apply to transactions in excluded territories if you’re registered in the country the territory is located in.

Some jurisdictions contain administrative subdivisions or territories, with the geographic region being outside the scope or “excluded” from the associated country’s VAT system. Although these territories don’t fall under the scope of the tax systems of the associated country, they might have their own tax system and be subject to different tax regulations and rates. If your customer is based in an excluded territory, the resulting tax amount might be zero. Below is the list of supported excluded territories where no tax is calculated, even if you’re registered in the country where the excluded territory is located. Stripe Tax automatically determines if your customer is based in an excluded territory.

CountryExcluded TerritoriesFinland- Åland Islands

France- Wallis and Futuna
- Saint Pierre and Miquelon
- Saint Martin
- Saint Barthélemy

Italy- Vatican City

Norway- Svalbard
- Jan Mayen

Spain- Ceuta
- Melilla
- Canary Islands

United Kingdom- Channel Islands (Guernsey and Jersey)
- British Virgin Islands
- Falkland Islands

## See also

- [Determining customer locations](/tax/customer-locations)
- [Set up Stripe Tax](/tax/set-up)
- [Reporting and filing](/tax/reports)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Situations where Stripe calculates zero tax](#situations-where-stripe-calculates-zero-tax)[Exempt customers](#exempt-customers)[Excluded territories](#excluded-territories)[See also](#see-also)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`