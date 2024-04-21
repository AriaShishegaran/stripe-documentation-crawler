# Collect tax in Hawaii

## When to register for tax collection

Use the Thresholds tab to get insights about your potential tax registration obligations in Hawaii. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

[Thresholds tab](https://dashboard.stripe.com/tax/thresholds)

[monitoring tool works](/tax/monitoring)

Sellers that meet either the sales or transaction number thresholds must register for a Hawaii sales tax permit, collect sales tax on sales that ship into Hawaii, and remit that sales tax to the state.

Threshold: 100,000 USD or 200 transactions

Period: Previous or current year

Included transactions: Gross sales

Effective date: July 1, 2018

## Register to collect tax

Register for sales tax in Hawaii at the tax authority. Read more about registering for sales tax in the US in our guide.

[tax authority](https://tax.hawaii.gov/)

[sales tax in the US in our guide](https://stripe.com/guides/sales-tax-registration-process-us)

After you’ve registered to collect tax in Hawaii, add your registrations to Stripe in the Registrations tab in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions in Hawaii.

[Registrations tab](https://dashboard.stripe.com/tax/registrations?location=us-hi)

Learn how to add your registration in the Dashboard.

[how to add your registration](/tax/registering#track-your-registrations-in-the-tax-dashboard)

## How we calculate taxes

Stripe calculates the taxes that apply to your customer’s location.

Instead of a traditional sales tax paid by consumers, Hawaii has a tax on businesses called General Excise Tax (GET). Businesses can recover GET by passing it on to their customers. Businesses generally display GET as a separate item on receipts, but they are not required to do so.

Because a business must pay GET on the entire amount paid by a customer, it also owes GET on any GET reimbursement it collects from customers. To cover that additional tax amount, Hawaii allows businesses to pass GET on to customers at a higher rate than the base GET rate. Stripe Tax only supports the maximum pass-on rate, which fully covers a business’ GET liability.

For example:

A product sells for 100 USD and is subject to 4% GET, so the seller owes 4 USD GET. If the seller passes that on to the customer and collects 104 USD, the entire amount is subject to 4% GET. As a result, the seller’s GET liability becomes 4.16 USD.

The seller can recover the entire GET amount from the customer by instead using the maximum pass-on rate, which for a 4% GET rate is 4.166%. That lets the seller charge the customer 4.166%, or 4.16 USD, which covers their entire GET liability. GET rates can vary by county and by business type. To learn more about GET and the maximum pass-on rates, see Hawaii’s tax facts page.

[Hawaii’s tax facts page](https://files.hawaii.gov/tax/legal/taxfacts/tf2015-37-1.pdf)

## Report and file your taxes

Stripe provides reports of your completed tax transactions. To access these reports, navigate to the Registrations tab of the Dashboard.

[Registrations tab](https://dashboard.stripe.com/tax/registrations)

The tax transaction data export provides a comprehensive and aggregated view of transactions by location, including a breakdown of individual tax amounts. Learn more about tax reporting exports.

[tax reporting exports](/tax/reports#exports)

Location reports offer a summary of transaction and refund data for specific US locations and align with Hawaii filing requirements. You have the option to report on an annual, semiannual, quarterly, or monthly basis.

[Location reports](/tax/reports#us-location-reports)

Reporting-specific considerations:

- In Hawaii, wholesalers are required to identify wholesale sales because they’re subject to a lower tax rate instead of being completely exempt. You won’t see a location report for Hawaii if you have any customer-exempt transactions. Use the exports instead for a detailed tax breakdown of each transaction.

[exports](/tax/reports#exports)

You are responsible for filing and remitting your taxes to Hawaii. Stripe doesn’t file taxes on your behalf. For automating filing in the US, we recommend using TaxJar’s AutoFile solution.

[TaxJar’s AutoFile solution](https://go.taxjar.com/2021StripeTaxInquiry_LP-01-Request.html)
