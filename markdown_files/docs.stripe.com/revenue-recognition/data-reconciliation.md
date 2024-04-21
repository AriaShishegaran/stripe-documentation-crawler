htmlData reconciliation with Stripe reports | Stripe Documentation[Skip to content](#main-content)Data reconciliation[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Fdata-reconciliation)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Fdata-reconciliation)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)
[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Reporting](/docs/stripe-reports)[Revenue recognition](/docs/revenue-recognition)[Reports and features](/docs/revenue-recognition/reports)# Data reconciliation with Stripe reports

Learn how to reconcile Revenue Recognition data with other financial reports.You can reconcile the cash account from Revenue Recognition and the Balance change from activity report within the same month. Because Revenue Recognition focuses on revenue-generating activities, you must exclude fees, network costs, contributions, and financing paydowns from the Balance change from activity report before reconciling. To get the cash amount in Revenue Recognition, download the balance sheet report in the summary format.

## Example

As an example, the report might look like the following, with a 100 USD amount:

accountcurrencynet changeCashusd+100.00Casheur+15.00To get the cash amount in the Balance change from activity report, set the currency to USD, and the report timezone to UTC.

After downloading the report in the summary format, it might look like the following:

reporting categorycurrencygross`charge`usd+140.00`refund`usd-40.00`refund_failure`usd+20.00`partial_capture_reversal`usd-20.00`fee`usd-10.00`network_cost`usd-10.00`contribution`usd-10.00`financing_paydown`usd-10.00`total`usd+60.00The total gross amount excludes some Stripe fees. After deducting rows for additional Stripe fees, network costs, contributions, and financing paydowns, the calculated cash amount is 100 USD.

## Journal entries

The journal entries in the Debits and credits report don’t consider fees, network costs, contributions, and financing paydowns. However, you can use Stripe fees in your Revenue Recognition reporting to create journal entries for these items.

NoteTo enable Stripe fees support in Revenue Recognition, create a ticket on our support page. When you enable this feature, the journal entries in the Debits and credits report automatically incorporate fees, network costs, and contributions.

With Stripe fees enabled, you can do the following to reconcile Revenue Recognition fees with the Balance change from activity report:

1. Download theBalance change from activityreport in the summary format. Make sure you select these columns:Reporting Category,Gross, andFee.
2. Calculate the total fee by summing the values in these columns:  - Grosscolumn: fee, network cost, and contribution
  - Feecolumn: total



In the following example, you calculate the total fees: -1000.00 + -0.50 + -0.40 + -1.00 to get the sum: -1001.90.

reporting categorygrossfee`charge`100.00-4.00`refund`-100.003.00`platform earning refund`-0.100.00`fee`-1000.000.00`network cost`-0.500.00`contribution`-0.400.00`total`-1001.00-1.00If you download the Debits and credits report in the summary format, you can see 1001.90 debited from the Fees expense account and credited to the Cash account.

debitcreditamountFeesCash1001.90Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Example](#example)[Journal entries](#journal-entries)Products Used[Revenue Recognition](/billing/revenue-recognition)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`