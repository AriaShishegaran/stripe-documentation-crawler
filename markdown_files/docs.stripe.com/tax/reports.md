htmlTax reporting | Stripe Documentation[Skip to content](#main-content)Report[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Freports)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Freports)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)# Tax reporting

Learn about different reporting available in Stripe Tax.NoteLog in or sign up for Stripe to activate Stripe Tax.

Stripe Tax provides reports of completed transactions. These reports include an itemized export showing completed transactions for all locations, an itemized export available by country or state, a summarized export showing an aggregated view of completed transactions by location, and a report showing an aggregated view of completed transactions for US locations. To access these reports, navigate to the Registrations tab of the Dashboard.

## Exports

To export tax transaction data, select a specific date range for completed transactions. These exports are available in CSV format and can be downloaded directly, scheduled, or have a link to the Dashboard sent through email. Typically, the data becomes available within one day of a completed transaction. Each day’s data includes transaction activity that occurs between 12:00am UTC and 11:59pm UTC.

Each export includes breakdowns of individual tax amounts, attributes, reasons for each tax, and tax rates per jurisdiction level (country, state, county, city, district) for each line item in a transaction. This allows you to analyze tax information at different geographic levels and gain a comprehensive understanding of the tax breakdown within each transaction to aid in your tax filings and returns.

### Itemized export

The Itemized transaction export contains the full list of line item level, imposition level, and jurisdiction level information for all of your completed transactions and refunds in CSV format. This export includes all transactions where you enable Stripe Tax. Itemized exports can help with filings that require more detail in the tax information reported. This export can be automated using the scheduling feature.

The Itemized export provides a comprehensive list that details tax breakdowns for each line item in a completed transaction where Stripe Tax is enabled. This export includes refunds and covers multiple jurisdictions. Depending on the specific location, there might be multiple rows per line item. Each row includes important details such as the transaction date and identifiers, jurisdiction location, amounts, tax rates, reasons for taxation, origin and destination addresses, amounts in the filing currency, and selected transaction metadata.

The export also includes transactions for tax situations that are non-taxable. This applies to transactions occurring where you’re not registered, transactions in jurisdictions not supported by Stripe Tax, or transactions where the jurisdiction doesn’t impose tax. You can filter these transactions from your report by selecting the Exclude non-taxable transactions option when exporting. The export still includes transactions for other non-taxable scenarios.

Use this export for US states that require sub-state level reporting.

Download example CSV file

One Stop Shop (OSS)EUIf you’ve registered for the One Stop Shop (OSS) within the European Union, an overview of all your EU transactions can be downloaded. This downloadable content can assist in preparing your VAT OSS return. But please be aware, the Itemized export does include non-taxable transactions (unless purposely excluded) and domestic transactions, both of which aren’t to be reported in an OSS return.

### Summarized export

The Summarized export provides an overview of completed transaction line items, categorized by country, state, jurisdiction, and tax rate, when Stripe Tax is enabled. Each row provides information such as jurisdiction location, applied tax rate, amounts in the filing currency and the presentment currency. In certain cases, there might be multiple rows for the same jurisdiction due to potential variations in tax rates. This export doesn’t include transactions that lack a registration or are classified under unsupported jurisdictions and product tax codes.

Use this export for country-level filings and VAT OSS, as well as for simpler US states.

Download example CSV file

## Imports

We’re holding a beta for a feature that allows you to import a CSV of transaction data from platforms like Amazon, Shopify, eBay, and so on directly into Stripe Tax. It will allow you to have a single, consolidated view of all your sales and tax obligations across platforms. See the signup form below if you’re interested in joining the beta.

After you import a CSV that meets the format requirements, you can:

- See all your sales tax collection in one place.
- Determine how much sales tax you owe for the reporting period—which means you won’t need to perform manual calculations across platforms.
- Make sure you stay compliant by having the most accurate tax liability information.

This feature reinforces our goal to provide the most comprehensive sales tax management solution for Stripe Tax customers. We want to eliminate the need to manage your tax compliance across selling platforms so you can focus on other parts of your business.

Use the following signup form if you want to participate in the beta. If you’re selected for the beta, we’ll contact you with more information about the next steps.

Interested in getting early access to the Stripe Tax third-party import tool?Share your email address to learn more.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.## Location reports (US only)

The Location reports provide a summary of transaction and refund data aggregated for specific US locations. Each report aligns with state filing and formatting requirements and corresponds to the specific filing periods of the online filing portal. You can select the frequency and period within the report, which the state determines.

These reports can only be viewed within the Dashboard and can’t be downloaded.

Stripe Tax currently doesn’t support use cases beyond your transaction data, such as credits, prepayments, discounts, and more. As a result, the final numbers for your business’s filing might vary.

NoteThe reports include transactions starting from January 1, 2023, and support fiscal annual periods beginning from 2024 onwards. You can access and view your transaction data from 2022 in the Itemized and Summarized exports.

### Refunds

Refunds associated with an original transaction period are reported in that same period, even if they occur later.  This can affect the aggregated amounts in a report.  Stripe currently doesn’t allow the reassigning of refunds to alternate periods.

### Tax types

Stripe Tax only supports reporting on transactions that are classified as Sales or Use tax types.

You have the option to view within the Itemized export a detailed tax breakdown of each transaction for this report period including other tax types.

### Location specific considerations

The locations listed below have additional report considerations:

- [Alaska](/tax/supported-countries/united-states/alaska#location-reports)
- [Arizona](/tax/supported-countries/united-states/arizona#location-reports)
- [Florida](/tax/supported-countries/united-states/florida#location-reports)
- [Hawaii](/tax/supported-countries/united-states/hawaii#location-reports)
- [Illinois](/tax/supported-countries/united-states/illinois#location-reports)
- [Kentucky](/tax/supported-countries/united-states/kentucky#location-reports)
- [Tennessee](/tax/supported-countries/united-states/tennessee#location-reports)
- [Washington](/tax/supported-countries/united-states/washington#location-reports)

## Access data using exports and reports

To download or view your Stripe Tax data, navigate to the Registrations tab of the Dashboard.

### Exports

You can export your transaction data into either an itemized or summarized report. These exports contain detailed information at the line item, imposition, and jurisdiction levels. Reports are accessible for all locations where you enable Stripe Tax.

To export transaction data in CSV format:

1. ClickExport transactions.
2. Specify the date range.
3. Select eitherItemized exportorSummarized export.
4. ClickExportto generate and download the file.

Itemized export by location![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

To export itemized transactions for a jurisdiction in CSV format:

1. Navigate to theRegistration detailspage for a location.
2. ClickExport transactions.
3. Specify the date range.
4. ClickExportto generate and download the file.

### Location reports

To view a US location specific report:

1. Navigate to theRegistration detailspage for a location.
2. SelectView Report.
3. To build the report for a state, select theFrequency, then thePeriod.

## Tax calculations recorded in reports

Stripe Tax exports include transactions committed with the Stripe Tax API and operations on Stripe objects with automatic_tax[enabled]=true.

Stripe Tax exports record the following operations, which increase the balance of total tax collected:

- Customer completes a payment in a Checkout Session. This also applies to Checkout Sessions created through[Payment Links](/api/payment_links/payment_links).
- Finalizing an Invoice. This applies to one-off Invoices and Subscription renewal Invoices.[Invoice finalization](/invoicing/integration/workflow-transitions)happens when the Invoice’s state transitions from`draft`to`open`state. This transition happensbeforethe Invoice is paid.
- Transitioning an Invoice’s state from`uncollectible`to`paid`through the[Pay Invoices API](/api/invoices/pay).
- [Voiding](/api/credit_notes/void)a Credit Note.
- [Creating](/api/tax/transactions/create_from_calculation)a tax transaction with the Stripe Tax API.

Stripe Tax exports record the following operations, which decrease the balance of total tax collected:

- [Voiding](/api/invoices/void)an Invoice.
- Marking an Invoice as[uncollectible](/api/invoices/mark_uncollectible).
- [Creating](/api/credit_notes/create)a Credit Note.
- A[Refund](/api/refunds)of a Charge associated with an Invoice or a Checkout Session.
- Creating a[reversal](/api/tax/transactions/create_reversal)(refund) tax transaction with the Stripe Tax API.

Stripe Tax doesn’t record the following operation in Tax exports:

- [Disputes](/disputes)that are upheld by the cardholder’s bank. Stripe Tax doesn’t decrease the balance of the collected total tax.
- Refunds of[uncaptured amounts](/api/payment_intents/capture#capture_payment_intent-amount_to_capture)of a payment. This can happen when performing a[partial capture](/api/payment_intents/capture#capture_payment_intent-amount_to_capture)for payments of Checkout sessions using[capture_method=manual](/api/checkout/sessions/create#create_checkout_session-payment_intent_data-capture_method). When the capture amount is lower than the original amount, Stripe Tax doesn’t reduce the total balance of the collected tax.

## See also

- [Set up Stripe Tax](/tax/set-up)
- [Products, prices, tax codes, and tax behavior](/tax/products-prices-tax-codes-tax-behavior)
- [Registering for tax](/tax/registering)
- [Tax filing and remittance](/tax/filing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Exports](#exports)[Imports](#tax-data-imports)[Location reports](#us-location-reports)[Access and download data](#how-to-access-data-using-exports-and-reports)[Tax calculations recorded in reports](#tax-calculations-recorded-in-reports)[See also](#see-also)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`