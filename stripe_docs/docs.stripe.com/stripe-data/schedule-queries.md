# Schedule queries

You can automate your Sigma queries by scheduling them to run on a daily, weekly, or monthly basis. Results for each scheduled query are sent with an email to specified team members or as webhook events.

[email](#subscribers)

[webhook events](#receiving-results-as-webhooks)

## Scheduling a query

With a query loaded into the editor, click Schedule. We recommend you uniquely name all your scheduled queries to avoid confusion. If your query doesn’t already have a name (or you wish to modify it), you can update it during the scheduling process.

Each scheduled query can be run on a daily, weekly, or monthly basis. Queries run as soon as the data for that period is available.

## Subscribers

Creators of scheduled queries are added as subscribers to email notifications by default. To notify other team members as well, enter their email addresses. Results sent with an email include the name and date of the scheduled query, and a link to download the results in CSV format. To preview what the email looks like, click Preview email.

[team members](/get-started/account/teams)

You or your team members can stop receiving notifications at any time by clicking the Unsubscribe link in the email. You can also edit the scheduled query in the Dashboard and add or remove subscribers.

Based upon your chosen schedule, the timeline displays the date your query runs next, and the processing date of the data it uses (additional time is required to make your account data available to query).

Managing scheduled queries Upcoming scheduled queries are displayed under Scheduled within the Queries tab. Schedules are grouped based on whether they were created by you or other members of your team.

To edit a scheduled query, select it and click Edit schedule. To delete it, click — and select Delete.

If you make use of webhooks, you can receive notifications for scheduled queries as webhook events. For example, Stripe sends the sigma.scheduled_query_run.created event each time a scheduled query is run. See below for a sample event.

[webhooks](/webhooks)

The data.object.file.url subfield of the webhook payload contains the URL where you can access the results file using your live secret API key.  For example, if your server received the webhook below, it could download the results using this curl command:

For more on how to integrate webhooks, see our webhook documentation.

[webhook documentation](/webhooks)
