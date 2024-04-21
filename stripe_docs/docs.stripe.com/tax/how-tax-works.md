# How Tax works

To be tax compliant, you need to:

- Understand which locations require you to collect tax

- Register for tax in those locations

- Calculate and collect tax

- Report, file, and remit the tax you collected

# Introduction to indirect taxes with Stripe Tax

Each country handles tax on sold products and services differently, often calling it by a different name. In the US, businesses deal with sales tax. Throughout Europe, it’s called value-added tax (VAT). Canada and most countries in the Asia Pacific region refer to it as goods and services tax (GST).

[VAT](https://en.wikipedia.org/wiki/Value-added_tax)

[GST](https://en.wikipedia.org/wiki/Value-added_tax)

Taxability and tax rates vary by location and category of products you’re selling. For example, children’s footwear is zero rated in Ireland, but adult footwear isn’t. Digital services are usually taxed at the standard rate in most EU countries. However, e-books are subject to the reduced rate.

Stripe Tax uses your business address, tax registrations, product tax codes, customers’ locations, and customer status to determine the correct tax rates for products you sell, in all supported locations. Read more about tax codes and how we calculate for different jurisdictions.

[Stripe Tax](https://stripe.com/tax)

[tax codes](/tax/products-prices-tax-codes-tax-behavior)

[how we calculate](/tax/calculating)

# Monitor your obligations and register

You need to identify the locations where you have sales tax, VAT, or GST obligations and need to register to collect tax. If you sell into multiple locations, you need to be familiar with the tax laws in those locations because the place where your transaction takes place determines where you’re required to collect tax. This can be the seller’s country, the buyer’s country, or another location.

[tax laws in those locations](/tax/supported-countries)

As your business grows and you sell to more locations, you need to register to collect tax in more locations. Stripe Tax tracks your Stripe transactions and helps you monitor your tax obligations. Read more about tax obligation monitoring.

[Read more about tax obligation monitoring](/tax/monitoring)

You must register with the tax authority in a location to collect taxes there. In some countries and states you have to register before your first transaction, while others have a registration threshold (such as the number of sales or sales volume). Take a look at the locations Stripe Tax supports along with the different tax thresholds that apply and links to the tax authority websites.

[locations Stripe Tax supports](/tax/supported-countries)

Stripe Tax tracks your registrations and uses them to calculate and collect taxes. Read more about adding your registrations to Stripe.

[Read more about adding your registrations to Stripe](/tax/registering)

After you have registered to collect tax with a tax authority add your registrations to Stripe in the Registrations tab in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions.

[Registrations tab](https://dashboard.stripe.com/tax/registrations)

# Calculate and collect

After you set up Stripe Tax in the Dashboard, Stripe automatically calculates and collects taxes on your transactions. Alternatively you can use Stripe Tax API to calculate taxes on your own custom payment flows. In either case, to determine which taxes to collect, you or your customers have to provide customer location information. Read more about how Stripe calculates tax.

[set up Stripe Tax in the Dashboard](/tax/set-up)

[Stripe Tax API](/tax/custom)

[Read more about how Stripe calculates tax](/tax/calculating)

If you sell to other businesses, your transactions might be subject to reverse charges. This means that the tax liability shifts to the customer and we don’t charge tax on the transaction. Stripe Tax uses customer tax identification numbers to determine whether a transaction is B2B. Adding a tax identification number to the customer might affect the tax calculation result. Stripe Tax doesn’t validate whether the provided tax identification number exists or is valid. Read about supported tax ID formats.

[Read about supported tax ID formats](/tax/invoicing/tax-ids#supported-tax-ids)

Some individuals or entities might be tax exempt. For example, some US states have a reseller exemption. You can set an exempt status on customers to reflect this. Read more about reverse charges and exempt customers.

[Read more about reverse charges and exempt customers](/tax/zero-tax)

# Report, file, and remit

If you’re collecting taxes, you must report, file, and remit (transfer) the taxes collected in every location that you’re registered in. Make sure you understand and comply with obligations of each state or country and consult your tax advisor if you need help. Stripe Tax supports exporting your transactions in an itemized format to aid with tax reporting. Read more about Stripe Tax reports.

[Read more about Stripe Tax reports](/tax/reports)

Stripe Tax doesn’t currently file or remit taxes on your behalf. Submitting tax returns is key to your tax compliance. You can use TaxJar’s AutoFile solution for filing in the US. In Europe, we recommend Taxually or Marosa. To get started, visit Taxually’s partner page or Marosa’s partner page

[TaxJar’s AutoFile solution](https://go.taxjar.com/2021StripeTaxInquiry_LP-01-Request.html)

[Taxually’s partner page](https://stripe.taxually.com/)

[Marosa’s partner page](https://marosavat.com/stripe-and-marosa/)

[privacy policy](https://stripe.com/privacy)

## See also

- Frequently asked questions

[Frequently asked questions](/tax/faq)

- Stripe Tax guides

[Stripe Tax guides](https://stripe.com/guides/tax-guides)
