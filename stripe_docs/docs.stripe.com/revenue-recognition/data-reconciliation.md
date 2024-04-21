# Data reconciliation with Stripe reports

You can reconcile the cash account from Revenue Recognition and the Balance change from activity report within the same month. Because Revenue Recognition focuses on revenue-generating activities, you must exclude fees, network costs, contributions, and financing paydowns from the Balance change from activity report before reconciling. To get the cash amount in Revenue Recognition, download the balance sheet report in the summary format.

## Example

As an example, the report might look like the following, with a 100 USD amount:

To get the cash amount in the Balance change from activity report, set the currency to USD, and the report timezone to UTC.

After downloading the report in the summary format, it might look like the following:

The total gross amount excludes some Stripe fees. After deducting rows for additional Stripe fees, network costs, contributions, and financing paydowns, the calculated cash amount is 100 USD.

## Journal entries

The journal entries in the Debits and credits report don’t consider fees, network costs, contributions, and financing paydowns. However, you can use Stripe fees in your Revenue Recognition reporting to create journal entries for these items.

To enable Stripe fees support in Revenue Recognition, create a ticket on our support page. When you enable this feature, the journal entries in the Debits and credits report automatically incorporate fees, network costs, and contributions.

[create a ticket](https://support.stripe.com/contact/email?topic=financial_reports)

With Stripe fees enabled, you can do the following to reconcile Revenue Recognition fees with the Balance change from activity report:

[Balance change from activity](/reports/balance)

- Download the Balance change from activity report in the summary format. Make sure you select these columns: Reporting Category, Gross, and Fee.

- Calculate the total fee by summing the values in these columns:Gross column: fee, network cost, and contributionFee column: total

- Gross column: fee, network cost, and contribution

- Fee column: total

In the following example, you calculate the total fees: -1000.00 + -0.50 + -0.40 + -1.00 to get the sum: -1001.90.

If you download the Debits and credits report in the summary format, you can see 1001.90 debited from the Fees expense account and credited to the Cash account.
