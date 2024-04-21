# Write queries

Anyone on your account with permission to view reports can use the Sigma query editor to compose new or modify existing queries.

[permission to view reports](https://support.stripe.com/questions/can-i-invite-other-team-members-or-my-developer-to-use-my-stripe-account)

[Sigma query editor](https://dashboard.stripe.com/sigma/queries)

## Query resources

The navigator window to the left of the editor provides a set of tools to help you build your query. You can see:

- Your previously saved queries

- Queries saved by your team

- The table schema to search for data sources

- Stripe query templates

The Queries tab shows the lists of queries previously saved by you and your team. The Templates tab provides a set of example queries representing the most common metrics and reports.

Selecting any saved query or template loads it into the query editor, where you can click Run to regenerate and view the results.

To use any saved query or template as a starting point for your own custom report, either click its overflow menu () and choose Make a copy or load it into the editor and click Make a copy. This allows you to modify the content in the editor and save your changes as a new query.

[save](#saving-queries)

## Compose a query

When you open the query editor, you can:

- Write standard ANSI SQL directly into the editor.

- Choose an existing query from your previously saved queries or Stripe’s templates and modify it in the editor to fine-tune the returned data.

The following query uses the balance_transactions table to get information about the five most recent balance transactions related to refunds.

Click Run to execute the query and view the results in a table below the editor. More complex queries might take a few moments longer to complete and display results. Attempting to run an invalid query generates an error message that contains the line number and position of the error.

The results of our sample query return 5 rows, where each row corresponds to a particular balance transaction item, along with the requested information about them.

You can join columns of type Primary key or Foreign key to similar columns in other tables:

- Primary key represents the unique identifier (ID) for each record in a table

- Foreign key represents data that refers to the primary key of another table

For instance, you can join the charge_id column of the disputes table (a foreign key) to the id column of the charges table (a primary key).

Joining tables allows you to return richer results in your datasets. For example, you can modify our balance transaction example to join with the refunds table to provide further information.

This extended query now returns the original charge ID that the refund relates to.

## View and download query results

You can schedule your queries on a daily, weekly, or monthly basis. We send results in an email or a webhook event.

[schedule your queries](/stripe-data/schedule-queries)

[webhook](/webhooks)

Query results display in a table below the editor. You can:

- View a maximum of 1,000 results.

- Sort the results by clicking the column headers.

- Resize each column to make it easier to read the results.

- Adjust the height of the results output.

Amounts express in the lowest available currency unit, such as cents for USD or yen for JPY. For example, an amount of 1,000 with a currency of usd equates to 10 USD.

Click Download CSV to export your results for use in spreadsheet applications or other reporting tools. The downloaded CSV includes all query results, so you’re not limited to the 1,000 viewable results.

## Save queries

To save a query, click its title (labeled New report if it’s a new query) and enter your replacement. Then click Save.

The queries you save are added to the All section and made available to every team member on your account. Each saved query is given a unique URL you can share by clicking Copy link. You can use this link as a shortcut to a particular report you regularly use, or share it directly with other team members on the Stripe account.

You can only share queries with team members. Shared queries are read-only, so other team members can’t modify the queries you create. If a team member wants to make changes to your query, they can make a copy and edit it accordingly.
