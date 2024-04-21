htmlCollect tax in Canada | Stripe Documentation[Skip to content](#main-content)Canada[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Fcanada)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Fcanada)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)[Supported countries](/docs/tax/supported-countries)# Collect tax in Canada

Learn how to use Stripe Tax to calculate, collect, and report tax in Canada.The Canadian tax system consists of a combination of federal and provincial taxes. The goods and services tax (GST) applies nationally. The different provinces handle taxes in a variety of ways. Learn more in our guide to tax in Canada.

Provincial sales taxes in New Brunswick, Newfoundland and Labrador, Nova Scotia, Ontario, and Prince Edward Island are combined with the GST to implement the harmonized sales tax (HST), which operates in the same way as the GST.

Separate taxes are collected in:

- British Columbia—provincial sales tax (PST)
- Manitoba—retail sales tax (RST)
- Quebec—Quebec sales tax (QST)
- Saskatchewan—provincial sales tax (PST)

Alberta, Northwest Territories, Nunavut, and Yukon don’t apply any provincial sales tax.

## When to register for tax collection

The Canadian federal government and the four provinces that levy a separate provincial sales tax have their own tax registration thresholds and procedures. Use the Thresholds tab to get insights about your potential tax registration obligations in Canada. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

After you’ve registered to collect tax in a province or with the government, add your registration to Stripe in the Registrations tab in the Dashboard to start collecting tax on your transactions in that location.

### Federal tax threshold

A remote seller supplying goods and services in Canada must register for federal GST/HST when they make sales in Canada exceeding 30,000 CAD within the past four calendar quarters.

Threshold: 30,000 CAD (global)

Time frame: Last four quarters.

Included transactions: Any taxable transaction.

Find more information on how to register for GST/HST on the federal government website.

### British Columbia

British Columbia (BC) requires those making taxable sales of goods or services in the province to register for PST collection. “Small sellers” in BC with sales of less than 10,000 CAD within the previous 12 months are not required to register for PST collection. This exception does not apply if the seller has an established commercial premises in BC.g

Threshold: 10,000 CAD

Time frame: 12 months

Included transactions: Any taxable transaction.

Find more information on how to register for PST on the British Columbia government website.

### Manitoba

Canadian business outside of Manitoba and businesses in foreign countries that perform taxable sales in Manitoba must register to collect RST. The business doesn’t need to register if all transactions it makes are B2B, since the Manitoba’s reverse-charge mechanism applies.

Threshold: 1 transaction

Time frame: 12 months

Included transactions: Any taxable transactions that reverse charge doesn’t apply to.

Find more information on how to register for RST on the Manitoba government website.

### Quebec

Quebec requires those making taxable sales of goods or services in the province to register for QST when their taxable worldwide sales exceed 30,000 CAD within the past four calendar quarters.

Threshold: 30,000 CAD (global)

Time frame: Last four quarters.

Included transactions: Any taxable transaction.

Find more information on how to register for QST on the Quebec government website.

### Saskatchewan

Canadian business outside of Saskatchewan and businesses in foreign countries that perform taxable sales in Saskatchewan must register to collect PST.

Threshold: 1 transaction

Time frame: 12 months

Included transactions: Any taxable transaction.

Find more information on how to register for PST on the Saskatchewan government website.

## How we calculate taxes

Stripe determines whether federal tax (GST or HST), provincial tax (PST, QST, or RST) or a combination of both types of taxes apply to the specific transaction.

Sales of goods and services within Canada are generally taxable at the location of the customer. Sales of goods shipped from Canada to customers in other countries are generally treated as a zero-rated export from the Canadian tax perspective. Sales of services that are provided from Canada to customers in other countries are generally not taxable in Canada but the tax of the customer country may apply.

Sales of services provided to Canadian customers by sellers established in other countries are generally taxable in Canada. While tax is usually collected on sales to private persons, no tax is charged on sales  to business customers who provide the seller with their tax identification number or a certificate of exemption.

## Report and file your taxes

Stripe provides reports of your completed tax transactions. To access these reports, navigate to the Registrations tab. Learn more about the different types of reports.

You’re responsible for filing and remitting your taxes in Canada. Stripe doesn’t file taxes on your behalf.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[When to register for tax collection](#when-to-register-for-tax-collection)[How we calculate taxes](#how-we-calculate-taxes)[Report and file your taxes](#report-and-file-your-taxes)Related Guides[Navigate the tax registration process in Canada](https://stripe.com/guides/tax-registration-process-canada)[Introduction to indirect tax compliance](https://stripe.com/guides/introduction-to-sales-tax-vat-and-gst-compliance)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`