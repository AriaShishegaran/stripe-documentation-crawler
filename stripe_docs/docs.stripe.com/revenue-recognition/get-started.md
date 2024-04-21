# Recognize revenue with Stripe

You can import your transaction data, set up rules to automate your revenue recognition, generate and customize revenue reports, and test your transaction model before going live.

All Stripe Revenue Recognition features are available from the Dashboard.

[Dashboard](https://dashboard.stripe.com/revenue-recognition)

Stripe offers a 30-day free trial for Revenue Recognition if you want to preview it. When you sign up, turn on test mode to explore all the features for free.

[sign up](https://dashboard.stripe.com/)

[test mode](/test-mode)

If you’re a Connect platform with destination charges, and want to use Stripe Revenue Recognition, create a ticket on our support page to join our destination charges beta.

[create a ticket](https://support.stripe.com/contact/email?topic=financial_reports)

[Set up Revenue Recognition](#set-up)

## Set up Revenue Recognition

Revenue Recognition is already automated for some business use cases but requires additional setup for others. Below is a list of some common billing models. Click them to learn more:

[Generate reports and charts](#generate-reports)

## Generate reports and charts

By default, the Dashboard displays all Revenue Recognition reports and charts by accounting periods (which is defined as the start and end dates of a given month). It takes between 24 - 48 hours for reports to generate and become available for download.

[Revenue Recognition reports and charts](/revenue-recognition/reports#dashboard)

If you’d like to recognize revenue based on custom accounting periods such as the 4-5-4 retail calendar, please create a ticket on our support page to join our beta.

[create a ticket](https://support.stripe.com/contact/email?topic=financial_reports)

Below is a short summary of the reports and charts you can view, download, or both.

[Monthly summary](/revenue-recognition/reports/monthly-summary)

[Revenue waterfall](/revenue-recognition/reports/waterfall)

Sometimes you’ll see mismatches between your accounting reports after you import the data and set up Stripe.

[Test your transaction model](#test)

## Test your transaction model

Use test mode in the Dashboard to generate test revenue reports based on your transactions.

Before going live, you can test the transaction model without your test transactions. Create rules to exclude transactions from specific customers, products, invoices, or payments.

For example, you can exclude all revenues produced by a test customer, named test@example.com. Create a rule that applies to this customer and choose Exclude revenue 100% as the revenue treatment.

[Create a rule](https://dashboard.stripe.com/revenue-recognition/rules/create)

## Other considerations

You might need to handle other considerations like tax revenue, passthrough fees, amortization granularity, and catch-up revenue. You can further set up Revenue Recognition so Stripe can handle it for you.

[tax revenue](#third-party-tax)

[passthrough fees](#passthrough-fees)

[amortization granularity](/revenue-recognition/revenue-controls#amortization-granularity)

[catch-up revenue](/revenue-recognition/revenue-controls#catch-up-revenue)

You can set up rules for Revenue Recognition to automatically calculate your tax revenue if you’re not using Stripe Tax.

First, set the tax amount to the tax parameter of an invoice or an invoice line item. Then, set up a rule to recognize the amount as tax. You can track the revenue from tax in the reports under Tax liability.

[tax](/billing/taxes/tax-rates)

As an example, say you’re using Avalara AvaTax to calculate sales tax for your products. You want to treat the invoice line item for AvaTax as tax so you create this rule:

- Line item description contains all of the following: AvaTax

- Allocation 100%

You can set up rules so Stripe can automatically calculate the passthrough fees and, separately, your revenue on invoice line items or a portion of an invoice line item.

[rules](/revenue-recognition/rules)

[invoice line items](/api/invoices/line_item)

For example, say you have an invoice line item Service A that costs 100 USD. You want to recognize 10 USD as passthrough fees and recognize 90 USD as revenue, so you create this rule:

[create this rule](https://dashboard.stripe.com/revenue-recognition/rules/create)

Service A includes passthrough fees

Invoices

- Line item description contains all of the following: Service A

Defer upon event & amortize over line item service period

- Allocation 90%

- Defer from finalized time and amortize over line item service period

Treatment as passthrough fees

- Allocation 10%

While Stripe Revenue Recognition is designed to work out-of-the-box for many business types, we understand that each business might have unique needs. We offer advanced configurations on your revenue recognition reporting through our Controls page, where you can easily adjust for settings like revenue amortization granularity and catch-up revenue treatment.

[Controls](/revenue-recognition/revenue-controls)

## See also

- Subscriptions and Tax

[Subscriptions and Tax](/billing/taxes)
