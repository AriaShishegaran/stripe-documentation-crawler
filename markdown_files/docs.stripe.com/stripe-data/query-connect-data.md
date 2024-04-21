htmlQuery Connect data | Stripe Documentation[Skip to content](#main-content)Query Connect data[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-data%2Fquery-connect-data)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-data%2Fquery-connect-data)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)[Data](#)
[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Data](/docs/stripe-data)# Query Connect data

Use Sigma and Data Pipeline to retrieve information about Connect.### Account types

Connect platforms can work with three different[account types](https://stripe.com/docs/connect/accounts).This content applies to Custom and Express accounts, and Standard accounts with[platform controls](https://stripe.com/docs/connect/platform-controls-for-standard-accounts)enabled.Connect platforms can report on their connected accounts using Sigma or Data Pipeline. You can write queries that run across your entire platform in much the same way as your own Stripe account.

Additional groups of Connect-specific tables within the schema are located in the Connect sections of the schema. If you don’t operate a Connect platform, these tables are not displayed.

## Connected account information

The connected_accounts table provides a list of Account objects with information about connected accounts. This table is used for account-level information across all accounts on your platform, such as business name, country, or the user’s email address.

The following example uses the connected_accounts  table to retrieve a list of five Custom accounts for individuals located in the US that have payouts disabled because Stripe does not have the required verification information to verify their account.

`select
    id,
    email,
    legal_entity_address_city as city,
    legal_entity_address_line1 as line1,
    legal_entity_address_postal_code as zip,
    legal_entity_address_state as state,
    legal_entity_dob_day as dob_day,
    legal_entity_dob_month as dob_month,
    legal_entity_dob_year as dob_year,`See all 23 linesAll the required fields for individual Custom accounts in the US are retrieved as columns. This allows you to see what information has been provided, and what is needed, for each account. This can be seen in the example report below (some columns have been omitted for brevity).

idemailcity…id_provideddocument_idacct_fGtmLlC…jenny.rosen@example.comSan Francisco…truefile_n6RH5Fa…acct_CZNuh5O…sophia.garcia@example.com…falsefile_XXUnow4…acct_IHPVEv1…natalie.davis@example.comSeattle…truefile_9CfufAn…acct_OP31RqV…ella.thompson@example.comAustin…falsefile_JrDWM4S…acct_9TDOYZv…james.smith@example.com…falsefile_8E4RnRV…## Accounts with requirements

The connected_accounts table also contains information about the requirements and future_requirements for connected accounts. Use the table to retrieve lists of accounts that have requirements currently due and will be disabled soon. Use the future_requirements columns to handle verification updates.

The following example uses the connected_accounts table to retrieve a list of accounts that have upcoming verification updates.

`select
  id,
  business_name,
  requirements_currently_due,
  future_requirements_currently_due
from
  connected_accounts
where
  future_requirements_currently_due != ''`The requirements_past_due, requirements_currently_due, requirements_eventually_due, future_requirements_past_due, future_requirements_currently_due, and future_requirements_eventually_due are comma-separated lists of requirements on the account.

idbusiness_namerequirements_currently_duefuture_requirements_currently_dueacct_1DgVkkk7m2hJlTHkRocketRidesbusiness_profile.urlacct_11gFGNKkVhHuQcYrKavholmindividual.email,settings.payments.statement_descriptoracct_1mcOGsX4V50qWFMIFurEverexternal_accountsettings.payments.statement_descriptoracct_1jzJtitG22QWtx3kPashabusiness_profile.urlcompany.tax_id## Transactional data for connected accounts

### Connect query templates

Sigma and Data Pipeline include a variety of query templates for Connect platforms. Use these to get started with reporting on your connected accounts.

Transactional and subscription data for connected accounts is contained within the connected_account_ tables. The available data for connected accounts is organized and structured in the same way as data for your own account.

For instance, the balance_transactions table, located in the Payments section, contains balance transaction data for your Stripe account. The connected_account_balance_transactions table, located in the Connect - Payments section, contains balance transaction data for your connected accounts. Each Connect-specific table has an additional account column containing the identifier of a connected account. This can be used when joining tables to build advanced queries.

The following example is based upon the default query that’s loaded into the editor. Instead of retrieving the ten most recent balance transactions on your account, it does so across all of your platform’s connected accounts.

`select
      date_format(created, '%m-%d-%Y') as day,
      account, -- Added to include corresponding account identifier
      id,
      amount,
      currency,
      source_id,
      type
    from connected_account_balance_transactions -- Changed to use Connect-specific table
    order by day desc
    limit 5`dayaccountidamountcurrencysource_idtype4/21/2024acct_LTGUZwn…txn_0D1HcbO…-1,000usdre_nJdpsP9…refund4/21/2024acct_z8fDHLW…txn_TrJBXMZ…1,000usdch_o141O4Y…charge4/21/2024acct_dB2kL4V…txn_gpmbzyi…1,000usdch_zWOejuH…charge4/21/2024acct_DRPy5hF…txn_BcFNJ7M…1,000eurch_JNYLnsH…charge4/21/2024acct_v5bQvE6…txn_8svGtne…-1,000usdre_VcHhbgp…refundRefer to our transactions and subscriptions documentation to learn more about querying transactional and subscription data. You can then supplement or adapt your queries with Connect-specific information to report on connected accounts.

### Query charges on connected accounts

Use Sigma or Data Pipeline to report on the flow of funds to your connected accounts. How you do this depends on your platform’s approach to creating charges.

## Direct charges

If your platform creates direct charges on a connected account, they appear on the connected account, not on your platform. This is analogous to a connected account making a charge request itself. Platforms can use the Connect-specific tables (for example, connected_account_charges or connected_account_balance_transactions) to report on direct charges.

Access the direct charges query template to retrieve itemized information about application fees earned through direct charges, and reports on the connected account, transfer, and payment that is created.

## Destination charges

If your platform creates destination charges on behalf of connected accounts, charge information is available within your own account’s data. A separate transfer of the funds to the connected account is automatically created, which creates a payment on that account. For example, the destination charges query template reports on transfers related to destination charges made by your platform. One way to analyze the flow of funds from a destination charge to a connected account is by joining the transfer_id column of the charges table to the id column of the transfers table. This example includes the original charge identifier and amount, the amount transferred to the connected account, and the connected account’s identifiers and resulting payment.

`select
  date_format(date_trunc('day', charges.created), '%y-%m-%d') as day,
  charges.id,
  charges.amount as charge_amount,
  transfers.amount as transferred_amount,
  transfers.destination_id
from charges
inner join transfers
  on transfers.id=charges.transfer_id
order by day desc
limit 5`dayidcharge_amounttransferred_amountdestination_id4/21/2024ch_acct_27MyzIO…1,0001,000acct_E0uGaaL…4/21/2024ch_acct_k9rFhdF…800800acct_UlOhP3P…4/21/2024ch_acct_c1EeOPC…1,000800acct_WUSgrSc…4/21/2024ch_acct_EEX8Xie…1,100950acct_dLt2RA2…4/21/2024ch_acct_HtghItq…1,1001,100acct_dg80EMF…Payment and transfer information for Connected accounts is also available within Connect-specific tables (for example, connected_account_charges).

### Separate charges and transfers

Report on separate charges and transfers using a similar approach to destination charges. All charges are created on your platform’s account, with funds separately transferred to connected accounts using transfer groups. A payment is created on the connected account that references the transfer and transfer group.

Both the charges and transfers table include a transfer_group column. Payment, transfer, and transfer group information is available within the Connect-specific connected_account_charges table.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Connected account information](#connected-account-information)[Accounts with requirements](#account-requirements)[Transactional data for connected accounts](#transactional-data-for-connected-accounts)[Direct charges](#direct-charges)[Destination charges](#destination-charges)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`