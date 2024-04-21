# Collect tax in the United Kingdom

In the United Kingdom, Stripe Tax supports calculation and collection of VAT.

[VAT](https://www.gov.uk/how-vat-works)

## When to register for tax collection

Use the Thresholds tab to get insights about your potential tax registration obligations in the United Kingdom. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

[Thresholds tab](https://dashboard.stripe.com/tax/thresholds)

[monitoring tool works](/tax/monitoring)

If you’re based outside the United Kingdom, you must register in the UK within 30 days of performing the first taxable transaction there. You’re also liable to register if you have reasonable grounds to believe that you’ll perform taxable transactions within the next 30 days. A taxable transaction is any sale made in the UK that’s neither exempt from VAT nor subject to reverse charge. Taxable transactions include those that are zero-rated for VAT purposes.

For example, if you’re based in the US and sell digital services to overseas customers, you must register in the UK as soon as you have reasonable grounds to believe that a UK consumer will purchase your services. If a UK consumer has actually bought your digital services, you must register within 30 days of performing the sale. However, if you only sell to UK businesses, you don’t need to register because such sales are subject to reverse charge and don’t constitute taxable transactions for UK VAT purposes.

The HMRC VAT Notice 700/1 Who should register for VAT provides more information on registration in the UK.

[Who should register for VAT](https://www.gov.uk/government/publications/vat-notice-7001-should-i-be-registered-for-vat/vat-notice-7001-should-i-be-registered-for-vat#Exempt-supplies)

Threshold: 1 transaction in the UK.

Included transactions: Any taxable transactions that reverse charge doesn’t apply to.

## Register to collect tax

Find more information on how to register for VAT in the United Kingdom on the government website:

- General information about UK VAT

[General information about UK VAT](https://www.gov.uk/how-vat-works)

- How to register

[How to register](https://www.gov.uk/register-for-vat)

After you’ve registered to collect tax in the United Kingdom, add your registrations to Stripe in the Registrations tab in the Dashboard. This turns on tax calculation and collection in Stripe for your transactions in the United Kingdom.

[Registrations tab](https://dashboard.stripe.com/tax/registrations?location=gb)

Learn more about how to add your registration in the Dashboard.

[how to add your registration](/tax/registering#track-your-registrations-in-the-tax-dashboard)

## How we calculate taxes

Stripe calculates VAT for your transactions in the United Kingdom.

Generally, most transactions are taxable in the jurisdiction where your customer is. Stripe assumes the sale of most goods or services to be taxable unless specifically exempted.

In the United Kingdom, there are some territories outside of the scope of the standard tax system and might have different rules that apply. Stripe won’t calculate tax for customers based there, even if you’ve added a registration for the UK. Learn more about how Stripe handles excluded territories. This applies to the following locations:

[excluded territories](/tax/zero-tax?#excluded-territories)

- British Virgin Islands

- Channel Islands (Guernsey and Jersey)

- Falkland Islands

Northern Ireland applies its own special VAT rules. If you sell goods into Northern Ireland, you have to follow the same rules as other European Union countries. But if you sell services, you have to charge taxes based on the laws of the United Kingdom. Stripe Tax doesn’t support sales of goods to Northern Ireland.

## Report and file your taxes

Stripe provides reports of your completed tax transactions. To access these reports, navigate to the Registrations tab. Learn more about the different types of reports.

[Registrations tab](https://dashboard.stripe.com/tax/registrations)

[the different types of reports](/tax/reports)

You’re responsible for filing and remitting your taxes to the United Kingdom. Stripe doesn’t file taxes on your behalf. However, we do have trusted partners who can help manage your filing and remittance.
