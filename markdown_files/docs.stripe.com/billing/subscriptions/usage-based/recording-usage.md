htmlRecord usage for billing | Stripe Documentation[Skip to content](#main-content)Record usage for billing[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fusage-based%2Frecording-usage)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fusage-based%2Frecording-usage)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Usage-based Billing](/docs/billing/subscriptions/usage-based)# Record usage for billing

Learn how to record and report usage for your customers.NoteWe updated our usage-based billing process. For information on our previous guidance, refer to our legacy usage-based billing documentation.

## Configuring Meter

Make sure that you have properly configured your Meter before recording usage. Meters are immutable, with the exception of the display name.

Event name![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

This is the name of the meter event that you plan to record usage for with this meter. Use this name on the event_name field of the Meter Event when you send usage to Stripe. This makes sure that the usage is ingested and aggregated by the correct meter. You can only use an event name with a single meter.

Event ingestion![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Specify how you want to send events to Stripe. There are two options:

- Raw: Treat all meter events as standalone events. Multiple events sent for the same timestamp don’t overwrite each other and are included in the aggregation. This is the default option if nothing is specified.
- Pre-aggregated (hourly or daily): If you’re sending events pre-aggregated over a specific time interval, either hourly or daily, Stripe only uses the most recent meter event within the hourly or daily window for aggregation. A newer event sent within the same hourly or daily window overwrites the previous one.

Aggregation formula![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Specify how to aggregate the usage over the billing period. Options for that parameter include:

- Sum: Bill based on the sum of all usage values for the billing period.
- Count: Bill based on the count of all usage for the billing period.
- Last (coming soon): Bill based on the most recent usage record for the billing period. If no usage is reported, the bill is based on a usage quantity of 0.
- Max (coming soon): Bill based on the biggest value in the specified bucket of time (second, hour, day) within the billing period. For example, the max number of users who logged in during any day of the billing period, often referred to as “high watermark billing”

Payload key overrides![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Specify which keys in the event payload refer to the customer and numerical usage values.

- value_settings: Define the key that refers to the numerical usage value in the payload of the meter event with this parameter. While the default key is`value`, you can specify a different key, such as tokens.
- customer_mapping: Define the key in the event payload that refers to the[Stripe Customer ID](/api/customers/object#customer_object-id)with this parameter. Although the default key is`stripe_customer_id`, you can specify a different one, such as`customer_id`.

## Recording usage

You can share usage information with Stripe by creating meter events with a customer_id, a numerical value, and optionally a timestamp. How often you report usage is up to you. For example, you can send usage as it occurs or in batches (for example, every day). At the end of the billing period, Stripe automatically calculates the total price and invoices for all usage during the billing period.

To create Meter Events:

Command Line[curl](#)`curl https://api.stripe.com/v1/billing/meter_events \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d event_name=alpaca_ai_tokens \
  -d "payload[value]"=25 \
  -d "payload[stripe_customer_id]"={{CUSTOMER_ID}}`Here are some best practices for recording usage:

- Use[idempotency keys](/api/idempotent_requests)to prevent reporting usage more than one time due to latency or other issues. Every meter event corresponds to an[identifier](/api/billing/meter-event/create#create_billing_meter_event-identifier)that you can specify in your request (if you don’t specify it, we autogenerate one).
- Make sure that the timestamp falls within the past 35 calendar days and isn’t more than 5 minutes in the future (the 5-minute window accounts for clock drift between your server and Stripe’s systems).
- Be mindful of the rate limit; the[Meter Events endpoint](/api/billing/meter-event/create)only allows 1000 calls per second per Stripe account, and one concurrent call per customer per meter. Monitor for`429`status codes and implement a retry mechanism with an exponential backoff schedule to manage request volume. Also, consider incorporating some randomness into the backoff schedule to avoid a[thundering herd effect](https://en.wikipedia.org/wiki/Thundering_herd_problem). If your service might exceed this limit, you can “bundle” your product into amounts. For example, if you charge per 1000 requests, base your product on “per 1k transactions” and send 1 usage record every 1000 times.
- Usage data is crucial for accurate user billing. Make your system resilient to network failures. For example, use a reliable queue like Amazon SQS to push data to Stripe so you can retry if necessary.

Interested in higher rate limits?You can report usage either by dropping it into an S3 bucket or through a bulk endpoint. Contact us at usage-based-billing@stripe.com so we can understand your use case better and provide early access.

## Fix incorrect usage

You can cancel incorrectly reported events using the Meter Event Adjustments. You need an identifier of the meter event to cancel it.

Command Line[curl](#)`curl https://api.stripe.com/v1/billing/meter_event_adjustments \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d type=cancel \
  -d event_name=alpaca_ai_tokens \
  -d "cancel[identifier]"={{METER_EVENT_IDENTIFIER}}`Canceling meter events has the following limitations:

- You can only cancel events that have been sent to Stripe within the last 24 hours.
- We don’t support billing adjustments for canceled usage that we’ve already invoiced a customer for.
- If you cancel usage already included on a finalized invoice, we won’t update that invoice. Additionally, we won’t issue a new correction invoice for the canceled usage.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Configuring Meter](#configuring-meter)[Recording usage](#recording-usage)[Fix incorrect usage](#fix-incorrect-usage)Related Guides[Usage-based pricing models](/docs/billing/subscriptions/usage-based/pricing-models)Products Used[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`