# Collect tax in Texas

## When to register for tax collection

Use the Thresholds tab to get insights about your potential tax registration obligations in Texas. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

[Thresholds tab](https://dashboard.stripe.com/tax/thresholds)

[monitoring tool works](/tax/monitoring)

Remote sellers with Texas revenues above 500,000 USD must register for a Texas sales tax permit, collect sales tax on sales that ship to Texas, and remit the sales tax to the state.

Threshold: 500,000 USD

Period: 12 months

Included transactions: Gross sales

Effective date: October 1, 2019

## Register to collect tax

Register for sales tax in Texas at the tax authority. Read more about registering for sales tax in the US in our guide.

[tax authority](https://comptroller.texas.gov/taxes/sales/)

[sales tax in the US in our guide](https://stripe.com/guides/sales-tax-registration-process-us)

Remote sellers with no physical presence in Texas can register for the Single Local Use Tax rate. This election (the process of making your choice known to the state) allows you to collect a single local use tax rate in the state. You can collect this tax rate after notifying the Texas Comptroller.

[Single Local Use Tax rate](https://comptroller.texas.gov/taxes/sales/remote-sellers.php)

[Texas Comptroller](https://comptroller.texas.gov/taxes/sales/forms/index.php)

After you’ve registered to collect tax in Texas, add your registrations to Stripe in the Registrations tab in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions in Texas. You’ll be able to indicate which tax election you made in Texas as part of adding your registration to Stripe.

[Registrations tab](https://dashboard.stripe.com/tax/registrations?location=us-tx)

Learn how to add your registration in the Dashboard.

[how to add your registration](/tax/registering#track-your-registrations-in-the-tax-dashboard)

## How we calculate taxes

If your origin address is in the US and differs from your customer’s state, Stripe always calculates tax based on your customer’s location.

[origin address](/tax/set-up#origin-address)

If your customer is in Texas and your origin address is also in Texas, Stripe applies tax based on your origin address, depending on the type of product or service you sell.

Stripe calculates the appropriate tax rate for your registration. If you selected the Single Local Use Tax rate in Stripe then we will calculate and collect the simplified rate. You can change this by editing the tax registration on the Dashboard.

[editing the tax registration](/tax/registering#edit-a-registration)

## Report and file your taxes

Stripe provides reports of your completed tax transactions. To access these reports, navigate to the Registrations tab of the Dashboard.

[Registrations tab](https://dashboard.stripe.com/tax/registrations)

The tax transaction data export provides a comprehensive and aggregated view of transactions by location, including a breakdown of individual tax amounts. Learn more about tax reporting exports.

[tax reporting exports](/tax/reports#exports)

Location reports offer a summary of transaction and refund data for specific US locations and align with Texas filing requirements. You have the option to report on an annual, quarterly, or monthly basis.

[Location reports](/tax/reports#us-location-reports)

Reporting-specific considerations:

- If you chose to collect the Single Local Use Tax, you’ll see ‘Single Local Tax’ on your report instead of any local jurisdictions.

You are responsible for filing and remitting your taxes to Texas. Stripe doesn’t file taxes on your behalf. For automating filing in the US, we recommend using TaxJar’s AutoFile solution.

[TaxJar’s AutoFile solution](https://go.taxjar.com/2021StripeTaxInquiry_LP-01-Request.html)
