# Query Connect data

[account types](https://stripe.com/docs/connect/accounts)

[platform controls](https://stripe.com/docs/connect/platform-controls-for-standard-accounts)

Connect platforms can report on their connected accounts using Sigma or Data Pipeline. You can write queries that run across your entire platform in much the same way as your own Stripe account.

[Connect](/connect)

Additional groups of Connect-specific tables within the schema are located in the Connect sections of the schema. If you don’t operate a Connect platform, these tables are not displayed.

## Connected account information

The connected_accounts table provides a list of Account objects with information about connected accounts. This table is used for account-level information across all accounts on your platform, such as business name, country, or the user’s email address.

[Account](/api#account_object)

[business name](/api#account_object-business_name)

[country](/api#account_object-country)

[email address](/api#account_object-email)

The following example uses the connected_accounts  table to retrieve a list of five Custom accounts for individuals located in the US that have payouts disabled because Stripe does not have the required verification information to verify their account.

[payouts](/payouts)

[required verification information](/connect/required-verification-information)

[verify their account](/connect/identity-verification)

All the required fields for individual Custom accounts in the US are retrieved as columns. This allows you to see what information has been provided, and what is needed, for each account. This can be seen in the example report below (some columns have been omitted for brevity).

## Accounts with requirements

The connected_accounts table also contains information about the requirements and future_requirements for connected accounts. Use the table to retrieve lists of accounts that have requirements currently due and will be disabled soon. Use the future_requirements columns to handle verification updates.

[handle verification updates](/connect/custom/handle-verification-updates)

The following example uses the connected_accounts table to retrieve a list of accounts that have upcoming verification updates.

The requirements_past_due, requirements_currently_due, requirements_eventually_due, future_requirements_past_due, future_requirements_currently_due, and future_requirements_eventually_due are comma-separated lists of requirements on the account.

## Transactional data for connected accounts

Sigma and Data Pipeline include a variety of query templates for Connect platforms. Use these to get started with reporting on your connected accounts.

[query templates](https://dashboard.stripe.com/sigma/queries/templates)

Transactional and subscription data for connected accounts is contained within the connected_account_ tables. The available data for connected accounts is organized and structured in the same way as data for your own account.

[Transactional](/stripe-data/query-transactions)

[subscription](/stripe-data/query-billing-data)

For instance, the balance_transactions table, located in the Payments section, contains balance transaction data for your Stripe account. The connected_account_balance_transactions table, located in the Connect - Payments section, contains balance transaction data for your connected accounts. Each Connect-specific table has an additional account column containing the identifier of a connected account. This can be used when joining tables to build advanced queries.

The following example is based upon the default query that’s loaded into the editor. Instead of retrieving the ten most recent balance transactions on your account, it does so across all of your platform’s connected accounts.

Refer to our transactions and subscriptions documentation to learn more about querying transactional and subscription data. You can then supplement or adapt your queries with Connect-specific information to report on connected accounts.

[transactions](/stripe-data/query-transactions)

[subscriptions](/stripe-data/query-billing-data)

Use Sigma or Data Pipeline to report on the flow of funds to your connected accounts. How you do this depends on your platform’s approach to creating charges.

## Direct charges

If your platform creates direct charges on a connected account, they appear on the connected account, not on your platform. This is analogous to a connected account making a charge request itself. Platforms can use the Connect-specific tables (for example, connected_account_charges or connected_account_balance_transactions) to report on direct charges.

[direct charges](/connect/direct-charges)

Access the direct charges query template to retrieve itemized information about application fees earned through direct charges, and reports on the connected account, transfer, and payment that is created.

[direct charges query template](https://dashboard.stripe.com/sigma/queries/templates/Direct%20charges)

## Destination charges

If your platform creates destination charges on behalf of connected accounts, charge information is available within your own account’s data. A separate transfer of the funds to the connected account is automatically created, which creates a payment on that account. For example, the destination charges query template reports on transfers related to destination charges made by your platform. One way to analyze the flow of funds from a destination charge to a connected account is by joining the transfer_id column of the charges table to the id column of the transfers table. This example includes the original charge identifier and amount, the amount transferred to the connected account, and the connected account’s identifiers and resulting payment.

[destination charges](/connect/destination-charges)

[destination charges query template](https://dashboard.stripe.com/sigma/queries/templates/Destination%20charges)

Payment and transfer information for Connected accounts is also available within Connect-specific tables (for example, connected_account_charges).

Report on separate charges and transfers using a similar approach to destination charges. All charges are created on your platform’s account, with funds separately transferred to connected accounts using transfer groups. A payment is created on the connected account that references the transfer and transfer group.

[separate charges and transfers](/connect/separate-charges-and-transfers)

[transfer groups](/connect/separate-charges-and-transfers)

Both the charges and transfers table include a transfer_group column. Payment, transfer, and transfer group information is available within the Connect-specific connected_account_charges table.
