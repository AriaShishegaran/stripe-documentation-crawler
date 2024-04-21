htmlRecord usage for billing | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fusage-based-legacy%2Frecording-usage)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fusage-based-legacy%2Frecording-usage)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# Record usage for billingLegacy

Learn how to record and report usage for your customers.NoteWe’ve updated the way usage-based billing works. See the updated usage-based billing docs.

Learn how to migrate.

Throughout each billing period, you need to report usage to Stripe so that customers are billed the correct amounts. You can maintain your own system for recording customer usage and provide usage information for subscriptions to Stripe.

You can share usage information with Stripe by creating usage records with a subscription item, quantity used, and a timestamp. How often you report usage is up to you. For example, you can run the code on an interval (for example, every 24 hours) for each active metered subscription. At the end of the billing period, Stripe automatically calculates the total price and invoices for all usage during the billing period.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_items/{{SUBSCRIPTION_ITEM_ID}}/usage_records \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -X POST \
  -d quantity=100 \
  -d timestamp=1713719565 \
  -d action=increment`## Best practices for recording usage

- You need to write some of your own business logic before creating the usage record. Pull a record of a customer from your database and extract the customer’s Stripe subscription item ID and usage for the day. If you aren’t storing subscription item IDs, retrieve the subscription and check for[subscription items](/api/subscriptions/object#subscription_object-items).
- Use[idempotency keys](/api/idempotent_requests)to ensure usage isn’t reported more than once in case of latency or other issues.
- The`timestamp`has to be within the current billing period, otherwise the call fails.
- The default value for the`action`parameter is`increment`. This value assumes that the price is configured with`aggregate_usage=sum`and that you write usage as it occurs, passing it to Stripe with the current`timestamp`.
- A`set`value for the`action`parameter supports the case where you aggregate usage yourself, and configure the price with`aggregate_usage=last_during_period`or`aggregate_usage=last_ever`.
- The usage reporting endpoint is rate-limited, so you might need to exercise caution and avoid making too many separate usage records. It’s important to note that Stripe’s API rate limit is 100 calls per second per account. We can increase this to 200 calls per second per account on request. If you have a service that you expect to burst above this limit, consider “bundling” your product into amounts. For example, if you charge per 1000 requests, consider basing your product on “per 1k transactions” and send 1 usage record per 1000.

### Clock drift

Reporting usage outside of the current billing period results in an error. To account for clock drift between your server and Stripe’s systems, we provide a short grace period in the default aggregation mode (aggregate_usage = sum). For all other aggregation modes, the timestamp must be within the current period.

During the first few minutes of each billing period, you can report usage that occurred within the last few minutes of the previous period. If the invoice for the previous period isn’t finalized, we add that usage to it. Otherwise, we bill that usage in the current period. After the grace period, you can’t report usage from the previous billing period.

Don’t rely on the grace period for reporting usage outside of a billing period. It’s intended only to account for possible clock drift, and we don’t guarantee it.

## Retrieve current usage

To retrieve total usage for the current period, you can retrieve the upcoming invoice for the subscription. The usage is reflected as the quantity of the invoice item for a subscription_item. The total usage value may not be the most up-to-date quantity because slight processing delays can occur.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/invoices/upcoming \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d subscription={{SUBSCRIPTION_ID}}`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Best practices for recording usage](#best-practices-for-recording-usage)[Retrieve current usage](#retrieve-current-usage)Related Guides[Usage-based pricing models](/docs/billing/subscriptions/usage-based-legacy/pricing-models)Products Used[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`