htmlMigrate to billing meters | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fusage-based-legacy%2Fmigration-guide)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fusage-based-legacy%2Fmigration-guide)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# Migrate to billing meters

Learn how to migrate from usage records to billing meters.Stripe is deprecating usage-records billing. Moving forward, you can migrate to billing meters, our only solution for usage-based billing. Billing meters provide the following advantages:

- High-throughput usage reporting
- One-hour reporting[grace period](/billing/subscriptions/usage-based/pricing-models#grace-periods)for generating invoices
- [Collect usage](/billing/subscriptions/usage-based/recording-usage#recording-usage)before creating a subscription

However, we don’t support the following features:

- `max`,`last_ever`, and`last_during_period`[aggregation](/api/prices/object#price_object-recurring)
- Reporting usage in the Dashboard

You can continue to use usage records as you adopt billing meters.

## Billing meter overview

Billing meters allow you to track usage of a particular event. It supports high-throughput event ingestion and aggregation.

Unlike usage records, billing meters don’t require customers to have subscriptions before reporting usage and a single meter can track usage across multiple customers.

Learn more about billing meters in our implementation guide.

[Create a meter](#create-meter)Create a billing meter. Learn more about configuring meters.

Command Line[curl](#)`curl https://api.stripe.com/v1/billing/meters \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d display_name="Alpaca AI" \
  -d event_name=api_request \
  -d "default_aggregation[formula]"=sum`[Create a new price](#create-price)Create a new price associated with the billing meter. Make sure that the new price is on the same product as your old price.

Command Line[curl](#)`curl https://api.stripe.com/v1/prices \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d product={{PRODUCT_ID}} \
  -d "recurring[interval]"=month \
  -d "recurring[usage_type]"=metered \
  -d "recurring[meter]"={{METER_ID}} \
  -d currency=usd \
  -d unit_amount=100`[Start recording usage](#start-recording-usage)NoteYou must continue to send usage records to Stripe until the migration is completed.

Start reporting usage to the Billing Meter API. Stripe doesn’t reflect this usage on customer invoices until they’re subscribed to the new price.

Command Line[curl](#)`curl https://api.stripe.com/v1/billing/meter_events \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d event_name=api_request \
  -d timestamp=1712096183 \
  -d identifier={{IDEMPOTENCY_KEY}} \
  -d "payload[stripe_customer_id]"={{CUSTOMER_ID}} \
  -d "payload[value]"=1`Learn more about recording usage.

[OptionalQuery reported usage](#query-reported-usage)[Plan subscription schedules](#plan-subscription-schedules)Use subscription schedules to automatically migrate to the new price at the end of the billing cycle. Learn more about subscription schedules.

List the subscriptions associated with the old price.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/subscriptions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d price={{OLD_PRICE_ID}} \
  -d "expand[]"="data.schedule"`Stripe returns a list of subscriptions associated with the old price. For example:

`{
  "object": "list",
  "data": [
    {
      "id": "sub_1P1Y6gDxxK6kAaV0rS7ojBjh",
      "object": "subscription",
      ...
      "items": {
        "object": "list",
        "data": [
          {
            "id": "si_PrGdqMmuM1DGbQ",
            "object": "subscription_item",
            ...
            "price": {
              "id": "{{OLD_PRICE_ID}}",
              "object": "price",
              ...
              "recurring": {
                "aggregate_usage": "sum",
                "interval": "month",
                "interval_count": 1,
                "trial_period_days": null,
                "usage_type": "metered"
              },
              ...
            },
            ...
          }
        ],
        ...
      },
      ...
      "schedule": {
        "id": "sub_sched_1P1XxjDxxK6kAaV0YygN4tf7",
        "object": "subscription_schedule",
        ...
        "current_phase": {
          "end_date": 1714759200,
          "start_date": 1712167200
        },
        ...
        "phases": [
          {
            ...
            "end_date": 1714759200,
            ...
            "items": [
              {
                ...
                "price": "{{OLD_PRICE_ID}}",
                ...
              }
            ],
            ...
            "start_date": 1712167200,
            ...
            "trial_end": 1712772000
          }
        ],
        ...
      },
      ...
    },
    ...
  ],
  "has_more": false,
  "url": "/v1/subscriptions"
}`If a subscription has a schedule, you must update the existing subscription schedule to migrate to the new price at the end of a billing cycle. If no schedule exists for a subscription, create a new one.

Create subscription schedulesUpdate existing subscription schedulesCreate a subscription schedule for each subscription associated with the old price.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d from_subscription={{SUBSCRIPTION_ID}}`Stripe returns a new subscription schedule object:

`{
  "id": "sub_sched_1P1H37DxxK6kAaV0Iggc537m",
  "object": "subscription_schedule",
  ...
  "current_phase": {
    "end_date": 1714693634,
    "start_date": 1712101634
  },
  ...
  "phases": [
    {
      ...
      "end_date": 1714693634,
      ...
      "items": [
        {
          ...
          "price": "{{OLD_PRICE_ID}}",
          ...
        }
      ],
      ...
      "start_date": 1712101634,
      ...
    }
  ],
  ...
  "status": "active",
  ...
}`Update the subscription schedule to add a phase with the new price.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules/sub_sched_1P1H37DxxK6kAaV0Iggc537m \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "phases[0][start_date]"=1712101634 \
  -d "phases[0][end_date]"=1714693634 \
  -d "phases[0][items][0][price]"={{OLD_PRICE_ID}} \
  -d "phases[1][items][0][price]"={{NEW_PRICE_ID}}`## Test the migration

Create a test customer with a subscription associated with the old price.

DashboardAPI1. Navigate to the[Customers tab](https://dashboard.stripe.com/test/customers).
2. Click+ Add customer.
3. Enter the name of the customer.
4. Navigate to the new customer.
5. Next to the Subscriptions header, click+to open the subscription drawer.
6. Select the old price.
7. ClickCreate test subscription.

Create a subscription schedule from the subscription.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d from_subscription={{SUBSCRIPTION_ID}}`Add a phase to the subscription schedule to migrate to the new price.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules/{{SUBSCRIPTION_SCHEDULE_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "phases[0][start_date]"=1710952582 \
  -d "phases[0][end_date]"=1713630982 \
  -d "phases[0][items][0][price]"={{OLD_PRICE_ID}} \
  -d "phases[1][items][0][price]"={{NEW_PRICE_ID}}`Simulate the subscription change with a test clock.

Learn more about testing subscriptions integrations. You can use test clocks to test different scenarios, including mock usage reporting. Learn more about test clocks.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Billing meter overview](#billing-meter-overview)[Create a meter](#create-meter)[Create a new price](#create-price)[Start recording usage](#start-recording-usage)[Plan subscription schedules](#plan-subscription-schedules)[Test the migration](#test-the-migration)Products Used[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`