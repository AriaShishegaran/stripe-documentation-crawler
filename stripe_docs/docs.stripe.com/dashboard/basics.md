# Dashboard basics

The Stripe Dashboard is the user interface that lets you manage and configure your account. Use it to navigate to account resources, invite team members, monitor you integration, and so on.

## Home

Home provides information about the activity on your account. It contains analytics and charts that provide information about the performance of your business. Home also shows recent activity that might require you to take action, such as unanswered disputes or identity verifications.

[Home](https://dashboard.stripe.com/dashboard)

## Navigate the Dashboard

You can view test data by toggling the Dashboard’s Viewing test data option. Whether a transaction was created in test or live mode depends on which API keys were used to create it.

[API keys](/keys)

The Dashboard is organized by the most common workflows used to manage your business. For example, the Payments tab allows you to manage the flow of money in and out of your account.

[Payments](https://dashboard.stripe.com/payments)

In many cases, you can use the Dashboard to perform specific actions, such as refunding a payment or canceling a subscription without needing to use the API. You can access configuration options and settings from the Dashboard settings.

[subscription](/billing/subscriptions/creating)

[Dashboard settings](https://dashboard.stripe.com/settings)

The Dashboard supports keyboard shortcuts for common actions. Press ? on your keyboard on any page in the Dashboard for a list of available shortcuts.

## Team member access

You can invite team members to access the Dashboard and help manage your business. Each of them can have different levels of access. For instance, you can allow members of your customer service team to access your Dashboard for the purpose of handling refunds and dispute responses.

[team members](/get-started/account/teams)

[refunds](/refunds)

[dispute responses](/disputes/responding#respond)

## Monitor your integration

The Developers Dashboard provides you with information about the performance and health of your integration. You can view your API and webhook usage with real time charts, upgrade your API version, and review API errors that can be filtered by endpoint or type.

[Developers Dashboard](https://dashboard.stripe.com/developers)

[webhook](/webhooks)

Stripe logs every successful or failed request made using your API keys. Each log contains details about the original request, whether it succeeded or failed, the response from Stripe, and a reference to any related API resources.

[logs](https://dashboard.stripe.com/logs)

You can also review every event that takes place on your account in the Dashboard. Events represent a change to an API resource (for example, when you update or create a Charge object), and contain its current information.

[event](/api#events)

[Dashboard](https://dashboard.stripe.com/events)

[Charge](/api/charges/object)

## Reporting and searching

You can filter and export all of your transactional data as reports in CSV format. You can also download a monthly report or QuickBooks-formatted export from your account’s business settings.

[reports](/reports)

[QuickBooks-formatted export](/reports/quickbooks)

You can use Dashboard search to find specific information using different terms and operators to narrow down the number of results. For instance, you can search for a specific payment using the customer’s email address or the last four digits of their card number.

[Dashboard search](/dashboard/search)

For more advanced searches and reporting, Stripe Sigma makes all of your data available as an interactive SQL environment in the Dashboard. You can write queries to generate customized reports without needing to use additional reporting tools.

[Stripe Sigma](https://stripe.com/sigma)

## Browser compatibility

The Dashboard officially supports the following web browsers and mobile environments:

- The last 20 major versions of Chrome and Firefox.

- The last two major versions of Safari and Edge.

- The last two major versions of mobile Safari on iOS.

## See also

- Activate your account

[Activate your account](/get-started/account/activate)

- Start a team

[Start a team](/get-started/account/teams)

- Perform searches

[Perform searches](/dashboard/search)

- Financial reports

[Financial reports](/reports)
