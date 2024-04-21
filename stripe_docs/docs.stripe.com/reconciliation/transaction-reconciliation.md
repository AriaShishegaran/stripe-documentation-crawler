# Transaction ReconciliationBeta

Transaction reconciliation enables you to reconcile between your internal records with Stripe processed charges and refunds at an individual transaction level.

Transaction reconciliation is useful for businesses that have:

- High transaction volumes, such as thousands of monthly transactions.

- Multiple payment methods used in a single transaction, such as gift cards and discounts.

- Long transaction life cycles where transactions are spread across multiple periods.

Using transaction reconciliation, you can:

- Track the collections against each individual transaction.

- Ensure high integrity for your revenue assurance process.

- Seamlessly reconcile large volumes of data without the constraints of spreadsheets.

- Save time spent on manual reconciliations.

[Get started](#get-started)

## Get started

To get started with Stripe reconciliation upload your transaction data. Then you can:

- Track the reconciliation status.

- View analytics.

- Download prebuilt reports.

- Generate custom reports.

[Import data](#import-data)

## Import data

To import transaction data:

- Go to the Stripe Dashboard > reconciliation overview page and click Import data.

- Click Browse and select your file. It must be smaller than 70 MB.

- Click Import CSV.

- To track the progress of the import, click View data management.

You are responsible for the data you provide to Stripe. By providing us data to use, you acknowledge that you have received permission to share that data with Stripe and to enable Stripe to use it to provide you the services.

The transaction data must have some required fields to convert it to Stripe’s canonical reconciliation schema. Here is the expected schema:

[Reconciliation statuses](#reconciliation-statuses)

## Reconciliation statuses

After the data is imported, reconciliation starts automatically, and each transaction gets a reconciliation status. The reconciliation status represents the state of the transaction and helps you understand what action to take. Settlement reconciliation and Transaction reconciliation have different statuses.

For reconciliation between settlement and bank data, each settlement is assigned one of the following statuses:

- Completely matched: Both “amount” and “settlement_id” matched with the Bank Statement

- Unmatched:“Settlement_id” not matched/found either in settlement data or Bank data

- Partially matched: “Settlement_id” matched/found in the Bank Statement but difference in “amount” beyond the threshold

You can configure the settlement reconciliation threshold when you compare settlement data to bank deposit data. If the difference in amounts is within the threshold, the settlement ID gets tagged as completely matched. If the difference in amounts is outside of the threshold, the settlement ID gets tagged as partially matched.

Here is an example of how the settlement reconciliation statuses are computed (in this example, the threshold is 1 USD):

Transaction reconciliation (between transaction data and settlement data) has four statuses:

- Settled: The record is present in both datasets and the amount is an exact match. In the case of pay-in reconciliation with three data sets, the settlement reconciliation status needs to be completely matched.

- In process: The record is present in both datasets but the difference in the amounts is beyond the set threshold.

- Open: The record is present in the transaction data but missing in the Stripe settlement data. A transaction can be open even if the settlement reconciliation for the corresponding charge_id is unmatched.

- Foreign: The record is present in the Stripe settlement data but missing in transaction data.

Configure the transaction reconciliation threshold  when comparing the amount expected (transaction data) and the amount processed (Stripe records). If the difference in amounts is within the threshold, the charge ID gets tagged as Settled. If the difference in amounts is outside of the threshold, the charge ID gets tagged as In process.

Here is the sample data showing how the transaction reconciliation statuses are computed (in this example, the threshold is 1 USD):

[View analytics](#view-analytics)

## View analytics

The reconciliation analytics page provides high-level details about the overall money movement of your business. It also includes charts for reconciliation status and aging summaries.

The reconciliation status chart provides a high-level view of the funds received or pending from Stripe. It shows an aggregated view of the amount corresponding to the transactions across four reconciliation statuses: Open, In Process, Foreign, and Settled. The key insight is to understand the amount for each of the reconciliation statuses and take actions based on the insights.

The aging summary chart provides a high-level view of the time it takes Stripe to settle processed transactions. It shows an aggregated view of the transaction amount by settlement days. Use the chart to determine whether Stripe is settling the money on time.

This helps you understand if Stripe is adhering to the agreed-upon SLA (service level agreement). The graph differentiates between the amount settled on or before SLA and after SLA with different colors. Blocks in blue represent the transaction amount settled on or before the SLA. Blocks in red represent the transaction amount settled after SLA.

[Generate reports](#generate-reports)

## Generate reports

Here are the standard reports that you can generate and download from the Stripe Dashboard:

- Transaction reconciliation

- Pay-in reconciliation

- Settlement reconciliation

- Pay-in reconciliation

- Transaction reconciliation

- Pay-in reconciliation

To download a report:

- Go to the Dashboard Reconciliation > Pay-in reconciliation page.

- Go to the Reports tab.

- Click New report.

- Select the report type and filters.

- Click Generate button.

- After the report completes generation, click Download.

Here are the columns in the reconciliation report:

You can add custom metadata from your transaction data to the reconciliation result report as additional columns. For example, if store_id is part of the transaction data, it shows up in the custom metadata section.

To view the available custom metadata, click Show under the columns. The metadata is populated in the report by aggregating based on the reconciliation reference, for example the charge_id. If multiple rows of metadata are found with the same charge_id, they appear as comma-separated values in the report.
