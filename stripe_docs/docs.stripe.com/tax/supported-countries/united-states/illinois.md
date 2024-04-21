# Collect tax in Illinois

In Illinois, Stripe Tax supports calculation and collection of sales tax.

## When to register for tax collection

Use the Thresholds tab to get insights about your potential tax registration obligations in Illinois. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

[Thresholds tab](https://dashboard.stripe.com/tax/thresholds)

[monitoring tool works](/tax/monitoring)

Sellers that meet either the sales or transaction number thresholds must register for an Illinois sales tax permit, collect sales tax on sales that ship into Illinois, and remit that sales tax to the state.

Threshold: 100,000 USD or 200 transactions

Period: Previous year

Included transactions: Retail sales

Effective date: October 1, 2018

We also support:

- Bloomington Amusement tax—for businesses selling video or audio streaming on a pay-per-use, rental, or subscription basis to customers in Bloomington.

[Bloomington Amusement tax](https://www.bloomingtonil.gov/departments/finance/local-tax-information/amusement-tax)

- Chicago Lease Tax (Personal Property Lease Transaction Tax)—for businesses selling $100,000 or over of software as a service or other leased products into Chicago.

[Chicago Lease Tax (Personal Property Lease Transaction Tax)](https://www.chicago.gov/city/en/depts/fin/supp_info/revenue/tax_list/personal_propertyleasetransactiontax.html)

- Chicago Amusement tax—for businesses selling $100,000 or more of digital entertainment into Chicago, including selling video or audio streaming and online gaming.

[Chicago Amusement tax](https://www.chicago.gov/city/en/depts/fin/supp_info/revenue/tax_list/amusement_tax.html)

- East Dundee Amusement tax—for businesses selling video or audio streaming, or remotely-accessed online games on a pay-per-use, rental, or subscription basis to customers in East Dundee.

[East Dundee Amusement tax](https://eastdundee.net/businesses/streaming_services_amusement_tax.php)

- Evanston Amusement tax—for businesses selling video or audio streaming, or remotely-accessed online games on a pay-per-use, rental, or subscription basis to customers in Evanston.

[Evanston Amusement tax](https://www.cityofevanston.org/how-to/home-rule-taxes)

- Schiller Park Streaming Surcharge—for businesses selling video or audio streaming, or remotely-accessed online games on a pay-per-use, rental, or subscription basis that are delivered to customers in Schiller Park.

[Schiller Park Streaming Surcharge](https://www.villageofschillerpark.com/149/Administration-Department)

Thresholds

- Chicago Lease and Chicago Amusement tax apply to businesses selling specific goods to customers in Chicago, even if you don’t have a physical presence there.

- Bloomington, East Dundee, Evanston, and Schiller Park amusement taxes only apply when there’s a physical presence in those locations.

Transactions for these taxes aren’t included in tax threshold monitoring for Illinois.

## Register to collect tax

Register for sales tax in Illinois at the tax authority or the other taxes we support at the links above. Read more about registering for sales tax in the US in our guide.

[tax authority](https://tax.illinois.gov/research/taxinformation/sales/rot.html)

[sales tax in the US in our guide](https://stripe.com/guides/sales-tax-registration-process-us)

After you’ve registered to collect tax in Illinois, add your registrations to Stripe in the Registrations tab in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions in Illinois.

[Registrations tab](https://dashboard.stripe.com/tax/registrations?location=us-il)

Learn how to add your registration in the Dashboard.

[how to add your registration](/tax/registering#track-your-registrations-in-the-tax-dashboard)

## How we calculate taxes

If your origin address is in the US and differs from your customer’s state, Stripe always calculates tax based on your customer’s location.

[origin address](/tax/set-up#origin-address)

If your customer is in Illinois and your origin address is also in Illinois, Stripe applies tax based on your origin address, depending on the type of product or service you sell.

## Report and file your taxes

Stripe provides reports of your completed tax transactions. To access these reports, navigate to the Registrations tab of the Dashboard.

[Registrations tab](https://dashboard.stripe.com/tax/registrations)

The tax transaction data export provides a comprehensive and aggregated view of transactions by location, including a breakdown of individual tax amounts. Learn more about tax reporting exports.

[tax reporting exports](/tax/reports#exports)

Location reports offer a summary of transaction and refund data for specific US locations and align with Illinois filing requirements. You have the option to report on an annual, quarterly, or monthly basis.

[Location reports](/tax/reports#us-location-reports)

Reporting-specific considerations:

- The location reports don’t include transactions with Bloomington Amusement tax, Chicago Lease Tax, Chicago Amusement tax, East Dundee Amusement tax, Evanston Amusement tax, or Schiller Park Streaming Surcharge as these are filed to the local jurisdiction using a different report. To see transactions with these taxes, you can use the exports.

[exports](/tax/reports#exports)

You are responsible for filing and remitting your taxes to Illinois. Stripe doesn’t file taxes on your behalf. For automating filing in the US, we recommend using TaxJar’s AutoFile solution.

[TaxJar’s AutoFile solution](https://go.taxjar.com/2021StripeTaxInquiry_LP-01-Request.html)
