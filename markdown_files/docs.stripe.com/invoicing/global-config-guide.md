htmlBest practices for setting up invoices in Europe | Stripe Documentation[Skip to content](#main-content)Set up invoices in Europe[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fglobal-config-guide)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/invoicing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fglobal-config-guide)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Invoicing](/docs/invoicing)[Global invoicing](/docs/invoicing/global-invoicing)# Best practices for setting up invoices in Europe

Learn the best practices for setting up invoices in Europe.The invoice compliance process can vary across European countries. Stripe recommends the following as best practices when you make sales to business customers as Business-to-Business (B2B) sales require compliant invoices. There’s no general obligation to issue invoices for Business-to-Consumer (B2C) sales.

NoteOur recommendations are for standard (full) invoices. In most countries, you can also issue simplified invoices for lower amounts, which are subject to less strict legal requirements.

[Key invoice fields](#key-invoice-fields)Stripe doesn’t automatically populate all of the fields on an invoice. In certain European countries, a missed or improperly added field can render an invoice noncompliant. We recommend that you include the noted fields when you prepare your invoices as they’re required throughout most of Europe.

![Key invoice details](https://b.stripecdn.com/docs-statics-srv/assets/invoice-global-config-annotations.97e5b50ca2d6c3a761449564cfe3946f.png)

Key invoice details

[How to add an invoice field](#Invoice-fields)The following table explains the ways that you can populate different invoice fields. To ensure that your invoices are compliant and adhere to geographic and business regulations, Stripe recommends that you consult with your tax and legal advisors.

KeyFieldRequired?How to populate1Invoice numberThis is always required.Stripe populates this by default. You can change how invoices are numbered (customer or account level) in the[Invoice template](https://dashboard.stripe.com/settings/billing/invoice).2Date of issueThis is always required.Stripe populates this by default.3Date dueThere’s no requirement to display the date by which a customer must pay an invoice. However, it’s a best practice.Stripe populates this by default.4aMerchant company nameThis is always required.Stripe populates this by default.4bMerchant company addressSending an invoice to another business always requires this field.Enter yourSupport addressunder[Public business information](https://dashboard.stripe.com/settings/public). You can also default to your business address as listed in your[account settings](https://dashboard.stripe.com/settings/account).5Merchant VAT ID​​Invoices generally require a merchant VAT ID (or tax ID). If you sell goods or services to a business customer in another EU country, you must mention your VAT ID, which is a number that contains a country prefix.Add your relevant tax or VAT ID by navigating toManage tax informationin theInvoice template.6aRecipient nameThis is always required.Stripe populates this by default.6bRecipient addressThis is always required.You can add this field by clicking theAdditional detailsbutton when you first create a customer.7Recipient VAT IDSending an invoice to another business typically requires this field. ​​If you sell goods or services to a business customer in another EU country, you must mention the customer’s VAT ID, which is a number that contains a country prefix.You can add this field by:1. ClickingAdd additional details(just like with the recipient address) when you create a new customer, and scrolling down toTax IDat the bottom of the dialog.
2. Adding it as a custom field underAdvanced optionswhen you create an invoice.

8Name of the good or serviceThis is always required.Stripe populates this by default.9Invoice line item supply dateThis is always required when the supply date of individual line items is different from the invoice send date.You can display line item supply dates by clicking the toggle underItem options.10Price of the good or serviceFor an invoice to be compliant, it must display tax-exclusive prices. For each invoice line item, you must show the following:1. Unit price (excluding VAT).
2. Quantity.
3. Any applicable discounts.
4. Total amount payable (excluding VAT), which is the unit price times the quantity, minus discounts.

You must display tax-exclusive prices to comply with EU invoicing rules.111Invoice line item tax rate percentage2This is always required. It’s sufficient to display the tax percentage amount for an invoice line item. You’re not required to display the cash amount per invoice line item.You can determine the tax to display on an invoice by:1. Using[Stripe Tax](/tax/invoicing)to automatically calculate the tax.
2. ​​Manually adding the tax rate when you are create an item. SelectItem taxes and coupons, enter your desired tax rate, thenCreate a[new tax rate](https://dashboard.stripe.com/test/tax-rates).

12Invoice subtotal (excludes VAT)This is always required.Stripe populates this by default.13VAT amountThis is always required.Stripe populates this by default.14Invoice total (includes VAT)This is always required.Stripe populates this by default.N/ACustom fieldsIn some European countries, you must also display additional information including the business registration number, purchase order (PO), or payment due date.UnderAdvanced optionsin the[Invoice Editor](https://dashboard.stripe.com/invoices/create), clickAdd custom field.1To display tax-exclusive prices with Stripe Tax, select No under Include tax in price to exclude tax. This excludes tax in prices in the invoice PDF, the Invoice Details page, and in the invoice email. You can also select Yes under Include tax in price, then check the Display tax-exclusive prices option in the Items Options dialog of the Items section. This excludes tax in prices in the invoice PDF, but includes tax on the Invoice Details page and in the email. If you’re adding tax rates manually for a business, you can either set Include tax in price to No,  or set Include tax in price  to Yes and check Display tax-exclusive prices in the Items Options dialog. The second approach includes tax on the Invoice Details page and in the email, but not in the invoice PDF.

2​​If a transaction isn’t subject to tax, you must state the reason for not applying it. For example, if the tax liability shifts to your customer (that is, your customer now has to account for tax), you must mention it as a “reverse charge” on the invoice. In the case of an EU business selling to another EU business, you must mention “zero-rated intra-Community supply." To include these references in your invoice,  add a custom field under Advanced options in the Invoice Editor.

[Facilitate customer payment](#facilitate-customer-payment)After you set up your invoices to meet European regulations and requirements, facilitate customer payment by:

- Adding the most popular European payment methods. By accepting a wider range of payment methods, such as SEPA Direct Debit and Bacs Direct Debit, you can lower your costs and ensure that invoices are paid.


- Using the Hosted Invoice Page.


- Picking the right net terms.


- Localizing your Invoice to the language of your customer.



CautionStripe Invoicing doesn’t integrate with the Italian government’s e-invoicing platform.

## See also

- [Customize invoices](/invoicing/customize)
- [Payment methods](/invoicing/payment-methods)
- [Account tax IDs](/invoicing/taxes/account-tax-ids)
- [Tax rates and IDs](/invoicing/taxes/tax-rates)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Key invoice fields](#key-invoice-fields)[How to add an invoice field](#Invoice-fields)[Facilitate customer payment](#facilitate-customer-payment)[See also](#see-also)Products Used[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`