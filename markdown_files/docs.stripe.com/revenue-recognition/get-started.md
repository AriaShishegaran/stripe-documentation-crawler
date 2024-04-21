htmlRecognize revenue with Stripe | Stripe Documentation[Skip to content](#main-content)Get started[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Fget-started)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Fget-started)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)
[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Reporting](/docs/stripe-reports)[Revenue recognition](/docs/revenue-recognition)# Recognize revenue with Stripe

Learn how to use Stripe for your revenue recognition.You can import your transaction data, set up rules to automate your revenue recognition, generate and customize revenue reports, and test your transaction model before going live.

All Stripe Revenue Recognition features are available from the Dashboard.

Try for freeStripe offers a 30-day free trial for Revenue Recognition if you want to preview it. When you sign up, turn on test mode to explore all the features for free.

BetaIf you’re a Connect platform with destination charges, and want to use Stripe Revenue Recognition, create a ticket on our support page to join our destination charges beta.

[Set up Revenue Recognition](#set-up)Revenue Recognition is already automated for some business use cases but requires additional setup for others. Below is a list of some common billing models. Click them to learn more:

### Simple subscriptions

### Metered billing subscriptions

### Third-party recurring billing

### Product bundles

[Generate reports and charts](#generate-reports)By default, the Dashboard displays all Revenue Recognition reports and charts by accounting periods (which is defined as the start and end dates of a given month). It takes between 24 - 48 hours for reports to generate and become available for download.

NoteIf you’d like to recognize revenue based on custom accounting periods such as the 4-5-4 retail calendar, please create a ticket on our support page to join our beta.

Below is a short summary of the reports and charts you can view, download, or both.

Reports and chartsDescriptionRevenue overviewHigh-level bar graphs that show your revenue activity (that is, your net recognized revenue and your ending balance per month) over time.Monthly summaryDetails of the accounting activities for the last month or a specified previous month. See[Monthly summary](/revenue-recognition/reports/monthly-summary)for more information.Revenue waterfallDisplays expected recognizable revenue over time. This is also referred to as a revenue schedule chart. See[Revenue waterfall](/revenue-recognition/reports/waterfall)for more information.Income statementDetails of the revenue and contra revenue by month.Balance sheetDetails of the balance sheet account by month.Debits and creditsDetails of the monthly debit-credit journal entries for accounts with activity.Accounts receivable agingDetails of the monthly and MTD outstanding invoice amounts that affect the accounts receivable ledger account.CorrectionsDetails of the monthly debit-credit correction journal entries for accounts.Sometimes you’ll see mismatches between your accounting reports after you import the data and set up Stripe.

[Test your transaction model](#test)Use test mode in the Dashboard to generate test revenue reports based on your transactions.

Before going live, you can test the transaction model without your test transactions. Create rules to exclude transactions from specific customers, products, invoices, or payments.

For example, you can exclude all revenues produced by a test customer, named test@example.com. Create a rule that applies to this customer and choose Exclude revenue 100% as the revenue treatment.

## Other considerations

You might need to handle other considerations like tax revenue, passthrough fees, amortization granularity, and catch-up revenue. You can further set up Revenue Recognition so Stripe can handle it for you.

### Recognize tax revenue from third-party solutions

You can set up rules for Revenue Recognition to automatically calculate your tax revenue if you’re not using Stripe Tax.

First, set the tax amount to the tax parameter of an invoice or an invoice line item. Then, set up a rule to recognize the amount as tax. You can track the revenue from tax in the reports under Tax liability.

As an example, say you’re using Avalara AvaTax to calculate sales tax for your products. You want to treat the invoice line item for AvaTax as tax so you create this rule:

NameApply toTreatment`Recognize tax revenue from AvaTax`Invoices- Line item description contains all of the following:`AvaTax`

Treat as tax- Allocation`100%`

### Calculate passthrough fees

You can set up rules so Stripe can automatically calculate the passthrough fees and, separately, your revenue on invoice line items or a portion of an invoice line item.

For example, say you have an invoice line item Service A that costs 100 USD. You want to recognize 10 USD as passthrough fees and recognize 90 USD as revenue, so you create this rule:

NameApply toTreatmentService A includes passthrough fees

Invoices

- Line item description contains all of the following:`Service A`

Defer upon event & amortize over line item service period

- Allocation`90%`
- Defer from finalized time and amortize over line item service period

Treatment as passthrough fees

- Allocation`10%`

### Adjust Revenue Recognition controls

While Stripe Revenue Recognition is designed to work out-of-the-box for many business types, we understand that each business might have unique needs. We offer advanced configurations on your revenue recognition reporting through our Controls page, where you can easily adjust for settings like revenue amortization granularity and catch-up revenue treatment.

## See also

- [Subscriptions and Tax](/billing/taxes)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up Revenue Recognition](#set-up)[Generate reports and charts](#generate-reports)[Test your transaction model](#test)[Other considerations](#other-considerations)[See also](#see-also)Products Used[Revenue Recognition](/billing/revenue-recognition)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`