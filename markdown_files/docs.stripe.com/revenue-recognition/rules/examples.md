htmlRules examples | Stripe Documentation[Skip to content](#main-content)Examples[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Frules%2Fexamples)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Frules%2Fexamples)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)
[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Reporting](/docs/stripe-reports)[Revenue recognition](/docs/revenue-recognition)[Revenue recognition rules](/docs/revenue-recognition/rules)# Rules examples

Learn how to use rules through examples.## Tax treatment

To categorize a tax line item (for example, created by Avalara), you can set one rule like the one in this example:

ComponentsValueApply toInvoices > Line item description contains all of the following: AvaTaxEffective periodStart: All past dates - End: IndefiniteTreatmentsTax (100%)If you have a 10 USD invoice line item with the description “Sales Tax calculated by AvaTax," and the invoice finalizes in April, you’d see the account balances as in the following example:

AccountAprilAccountsReceivable10 USDTaxLiability10 USD## Passthrough fees

To categorize 10% of an amount as a passthrough fee, you can set one rule like the following example:

ComponentsValueApply toInvoices > All line itemsEffective periodStart: All past dates—End: IndefiniteTreatmentsAmortization over line item service period (90%) and Passthrough fee (10%)If you have a 100 USD invoice line item (without a service period) that finalizes in April, you’d see the account balances like the following example:

AccountAprilAccountsReceivable100 USDRevenue90 USDPassthroughFees10 USD## Exclude transactions from a test customer

To exclude all the standalone payments from a test customer, you can set one rule like the following example:

ComponentsValueApply to

Customers > Customer email contains all of the following: test@stripe.com

Other payments > All other payments

Effective periodStart: All past dates—End: IndefiniteTreatmentsExclude revenue (100%)Other payments from the customer, whose email is test@stripe.com, would be excluded from the report completely.

## Exclude standalone payments

To exclude all standalone payments from the report, set a rule like the following:

ComponentsValueApply toOther payments > All other paymentsEffective periodStart: All past dates—End: IndefiniteTreatmentsExclude revenue (100%)If you’re a Billing Scale user, this rule restricts Revenue Recognition to only include transactions managed within Billing Scale (recurring payments and one-time invoice payments). Standalone payments are excluded from the report.

## Amortize revenue over custom time period

In this example, we want to (1) amortize other payments from a small set of customers (for example, cus_AAA and cus_BBB) over one year and (2) amortize the remaining other payments over one month.

We can make two rules and use the order of the rules as shown in the following example:

Rule 1: Amortize other payments over one year

ComponentsValueApply to

Customers > Customer ID matches any of the following: cus_AAA, cus_BBB

Other payments > All other payments

Effective periodStart: All past dates - End: IndefiniteTreatmentsAmortization over custom service period (100%) > Amortization starting 0 days from paid time over 1 yearRule 2: Amortize other payments over one month

ComponentsValueApply toOther payments > All other paymentsEffective periodStart: All past dates - End: IndefiniteTreatmentsAmortization over custom service period (100%) > Amortization starting 0 days from paid time over 1 monthOther payments from cus_AAA or cus_BBB would match Rule 1, and the revenue would be amortized over one year. Other payments from any other customer would match Rule 2, and the revenue would be amortized over one month.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Tax treatment](#tax-treatment)[Passthrough fees](#passthrough-fees)[Exclude transactions from a test customer](#exclude-transactions-from-a-test-customer)[Exclude standalone payments](#exclude-standalone-payments)[Amortize revenue over custom time period](#amortize-revenue-over-custom-time-period)Products Used[Revenue Recognition](/billing/revenue-recognition)[Radar](/radar)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`