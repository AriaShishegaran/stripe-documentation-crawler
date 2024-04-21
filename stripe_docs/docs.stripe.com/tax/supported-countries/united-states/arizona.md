# Collect tax in Arizona

## When to register for tax collection

Use the Thresholds tab to get insights about your potential tax registration obligations in Arizona. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

[Thresholds tab](https://dashboard.stripe.com/tax/thresholds)

[monitoring tool works](/tax/monitoring)

Sellers who exceed the gross sales must register for an Arizona sales tax permit to collect Transaction Privilege Tax (TPT) on sales that ship to Arizona and remit the sales tax to the state. Arizona is the first state to use a graduated approach for their economic nexus threshold.

Threshold: 100,000 USD

Period: Previous or current year

Included transactions: Gross sales

Effective date: October 1, 2019

## Register to collect tax

Register for sales tax in Arizona at the tax authority. Read more about registering for sales tax in the US in our guide.

[tax authority](https://azdor.gov/business/transaction-privilege-tax)

[sales tax in the US in our guide](https://stripe.com/guides/sales-tax-registration-process-us)

After you’ve registered to collect tax in Arizona, add your registrations to Stripe in the Registrations tab in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions in Arizona.

[Registrations tab](https://dashboard.stripe.com/tax/registrations?location=us-az)

Learn how to add your registration in the Dashboard.

[how to add your registration](/tax/registering#track-your-registrations-in-the-tax-dashboard)

## How we calculate taxes

If your origin address is in the US and differs from your customer’s state, Stripe always calculates tax based on your customer’s location.

[origin address](/tax/set-up#origin-address)

If your customer is in Arizona and your origin address is also in Arizona, Stripe applies tax based on your origin address, depending on the type of product or service you sell.

## Report and file your taxes

Stripe provides reports of your completed tax transactions. To access these reports, navigate to the Registrations tab of the Dashboard.

[Registrations tab](https://dashboard.stripe.com/tax/registrations)

The tax transaction data export provides a comprehensive and aggregated view of transactions by location, including a breakdown of individual tax amounts. Learn more about tax reporting exports.

[tax reporting exports](/tax/reports#exports)

Location reports offer a summary of transaction and refund data for specific US locations and align with Arizona filing requirements. You have the option to report on an annual, quarterly, or monthly basis.

[Location reports](/tax/reports#us-location-reports)

Reporting-specific considerations:

- Some areas of Arizona have a different tax rate for purchases of a certain value. The different tax rate can be applied to either the total price of the purchase or only the amount above the triggering price. You won’t see a location report for Arizona if you have these transactions. Use the exports instead for a detailed tax breakdown of each transaction.

[exports](/tax/reports#exports)

- Native American reservations that are located in Arizona might impose Tribal taxes when doing business within their borders. A warning message appears when a report contains a transaction from this location. These taxes are not managed by the state and require separate filing.

You are responsible for filing and remitting your taxes to Arizona. Stripe doesn’t file taxes on your behalf. For automating filing in the US, we recommend using TaxJar’s AutoFile solution.

[TaxJar’s AutoFile solution](https://go.taxjar.com/2021StripeTaxInquiry_LP-01-Request.html)
