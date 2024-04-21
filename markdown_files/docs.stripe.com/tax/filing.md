htmlFile and remit | Stripe Documentation[Skip to content](#main-content)File and Remit[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Ffiling)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Ffiling)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)# File and remit

Learn about filing and remitting tax you have collected.If you’re a business collecting tax, you must file and remit the tax collected in every location that you’re registered in.

The tax authority in each location determines the rules for reporting and filing taxes. For example, some states in the US want businesses to report at the city, county, or other level when filing, whereas others only need information at a more consolidated or state level. Additionally, each location mandates their own method and timing of remittance, and can vary depending on your volume of sales into that location.

Stripe Tax users can leverage transaction exports and location reports to prepare, file, and remit the tax that was automatically calculated and collected. Stripe Tax doesn’t currently file or remit taxes on your behalf. However, we do have trusted partners who can help manage your filing and remittance needs:

- For automating filing in the US, we recommend using[TaxJar’s AutoFile solution](https://go.taxjar.com/2021StripeTaxInquiry_LP-01-Request.html).
- For Europe, we recommend using[Taxually](https://stripe.taxually.com/)or[Marosa](https://marosavat.com/stripe-and-marosa/).
- For APAC, we recommend[Taxually](https://stripe.taxually.com/)

If you don’t use Stripe Tax but use manual Tax Rates to define and maintain rates on your own, there are specific exports available depending on your integration and use case. You can leverage up to four different reports depending on your integration.

## Downloading data

From the Tax Rates list in the Dashboard, you can export the data files required for tax reporting calculations.

Tax Rates might provide up to four different levels of tax report export files depending on your integration:

- Invoice line item tax export—A lower-level export, this includes details down to the line item level, including per-line-item tax rates, inclusive or exclusive, amounts, and so on.
- Invoice totals export—Shows the aggregate tax collected on the invoice as a whole, including adjustments for any refunds.
- Checkout payment mode line item tax export—A lower-level export, this includes details down to the line item level, including per-line-item tax rates, whether it’s inclusive or exclusive, amounts, and so on.
- Checkout payment mode totals export—Shows the aggregate tax collected on the invoice as a whole, including adjustments for any refunds.

To get your gross sales, use the Invoice or Checkout line item level export. To factor in refunds, use the Invoice total export.

## Filing frequency

The local tax authority specifies the tax filing frequency during the tax collection registration process. Depending on your specific requirements, you might need to remit tax on a monthly, annual, or other designated frequency. Filing frequencies can vary based on factors such as annual revenue and other considerations. Contact your local tax authority to confirm your filing frequency if you’re uncertain.

## Refunds

Exports and reports include refunds. If a refund of tax is issued because of a return of goods, local tax authorities might require an amendment to the original tax return to process the refund. To claim the refund on your tax return, reach out to your local tax authority.

Would you like Stripe to file taxes on your behalf?Enter your email address below if you're interested in being an early participant in the upcoming Stripe Tax Filing beta.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.## See also

- [Tax Rates](/billing/taxes/tax-rates)
- [Checkout taxes](/payments/checkout/taxes)
- [Tax reporting](/tax/reports)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Downloading data](#downloading-data)[Filing frequency](#filing-frequency)[Refunds](#refunds)[See also](#see-also)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`