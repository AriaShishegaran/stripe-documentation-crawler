htmlWrite queries | Stripe Documentation[Skip to content](#main-content)Write queries[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-data%2Fwrite-queries)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-data%2Fwrite-queries)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)[Data](#)
[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Data](/docs/stripe-data)# Write queries

Compose custom queries in standard ANSI SQL for use in a broad range of reporting functions.Anyone on your account with permission to view reports can use the Sigma query editor to compose new or modify existing queries.

## Query resources

The navigator window to the left of the editor provides a set of tools to help you build your query. You can see:

- Your previously saved queries
- Queries saved by your team
- The table schema to search for data sources
- Stripe query templates

### Saved queries and templates

The Queries tab shows the lists of queries previously saved by you and your team. The Templates tab provides a set of example queries representing the most common metrics and reports.

Selecting any saved query or template loads it into the query editor, where you can click Run to regenerate and view the results.

To use any saved query or template as a starting point for your own custom report, either click its overflow menu () and choose Make a copy or load it into the editor and click Make a copy. This allows you to modify the content in the editor and save your changes as a new query.

## Compose a query

When you open the query editor, you can:

- Write standard ANSI SQL directly into the editor.
- Choose an existing query from your previously saved queries or Stripe’s templates and modify it in the editor to fine-tune the returned data.

The following query uses the balance_transactions table to get information about the five most recent balance transactions related to refunds.

`select
  date_format(created, '%Y-%m-%d') as day,
  id,
  amount,
  currency,
  source_id
from balance_transactions
where type = 'refund'
order by day desc
limit 5`Click Run to execute the query and view the results in a table below the editor. More complex queries might take a few moments longer to complete and display results. Attempting to run an invalid query generates an error message that contains the line number and position of the error.

The results of our sample query return 5 rows, where each row corresponds to a particular balance transaction item, along with the requested information about them.

dayidamountcurrencysource_id4/21/2024txn_86Cn63p5nf03VyJ-1,000usdre_moZCXxHENELxbEx4/21/2024txn_TpsoJt5UWHHOOWZ-1,000usdre_IYhwu0njQ5M7MCP4/21/2024txn_v8qOGlG9X7roVwl-1,000usdre_SFAKEInRxOlOEzN4/21/2024txn_fPqsk3jSMZcO4L0-1,000eurre_5lRRDndfc5WIKnD4/21/2024txn_1GXj52ImX3YLjrJ-1,000usdre_m7uPl6Xwk7r24VF### Join tables

You can join columns of type Primary key or Foreign key to similar columns in other tables:

- Primary keyrepresents the unique identifier (ID) for each record in a table
- Foreign keyrepresents data that refers to the primary key of another table

For instance, you can join the charge_id column of the disputes table (a foreign key) to the id column of the charges table (a primary key).

![](https://b.stripecdn.com/docs-statics-srv/assets/disputes.f293434123d316ff4fafe2524e9b2b0d.png)

Joining tables allows you to return richer results in your datasets. For example, you can modify our balance transaction example to join with the refunds table to provide further information.

`select
  date_format(date_trunc('day', balance_transactions.created), '%Y-%m-%d') as day,
  balance_transactions.amount,
  balance_transactions.currency,
  balance_transactions.source_id,
  refunds.charge_id
from
  balance_transactions
inner join refunds -- Joining these tables to retrieve additional information
on balance_transactions.source_id=refunds.id
where balance_transactions.type = 'refund'
order by day desc
limit 5`This extended query now returns the original charge ID that the refund relates to.

dayamountcurrencysource_idcharge.id4/21/2024-1,000usdre_F7memr8sfuD0WnNch_Ez306jJ4PcMyNzd4/21/2024-1,000usdre_kzZ7wG3zD26Irclch_wvew5XRZEtMjGdp4/21/2024-1,000usdre_mPWwG2mOvJrweOKch_QKK1SkSJThJSV8t4/21/2024-1,000eurre_pBwWR1lJgfAzGGech_n6SgU7WmFQ8LPcm4/21/2024-1,000usdre_bOhzXBdUVr9kjkYch_jdVAb4TUqXlTGIy## View and download query results

### Scheduling queries

You can schedule your queries on a daily, weekly, or monthly basis. We send results in an email or a webhook event.

Query results display in a table below the editor. You can:

- View a maximum of 1,000 results.
- Sort the results by clicking the column headers.
- Resize each column to make it easier to read the results.
- Adjust the height of the results output.

Amounts express in the lowest available currency unit, such as cents for USD or yen for JPY. For example, an amount of 1,000 with a currency of usd equates to 10 USD.

Click Download CSV to export your results for use in spreadsheet applications or other reporting tools. The downloaded CSV includes all query results, so you’re not limited to the 1,000 viewable results.

## Save queries

To save a query, click its title (labeled New report if it’s a new query) and enter your replacement. Then click Save.

### Share queries

The queries you save are added to the All section and made available to every team member on your account. Each saved query is given a unique URL you can share by clicking Copy link. You can use this link as a shortcut to a particular report you regularly use, or share it directly with other team members on the Stripe account.

You can only share queries with team members. Shared queries are read-only, so other team members can’t modify the queries you create. If a team member wants to make changes to your query, they can make a copy and edit it accordingly.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Query resources](#query-resources)[Compose a query](#compose-a-query)[View and download query results](#view-and-download-query-results)[Save queries](#saving-queries)Products Used[Sigma](/stripe-data/access-data-in-dashboard)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`