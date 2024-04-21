htmlSubscription schedules | Stripe Documentation[Skip to content](#main-content)Subscription schedules[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fsubscription-schedules)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fsubscription-schedules)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Subscriptions](/docs/subscriptions)# Subscription schedules

Learn about subscription schedules and how to use them.Use subscription schedules to automate changes to subscriptions over time. You can create subscriptions directly through a schedule or you can add a schedule to an existing subscription. Use the phases attribute to define the changes you want to make to the subscription. After a schedule completes all of its phases, it completes based on its end_behavior.

Some changes you might want to schedule include:

- Starting a subscription on a future date
- Backdating a subscription to a past date
- Upgrading or downgrading a subscription

Subscription schedules are available in both the Stripe Billing Dashboard and the API. Here’s a quick video of how subscription schedules work in the Dashboard:

Subscription schedules in the Dashboard

The rest of this document explains subscription schedules in more detail. To see a list of examples, see the use cases page.

## Phases

When creating a subscription schedule, use the phases attribute to define when changes occur and what properties of the subscription to change. For example, you might offer a coupon for 50% off for the first three months of a subscription. In this scenario, you’d create a subscription schedule where the first phase is three months long and contains the 50% off coupon. In the second phase, the subscription would be reverted to the normal cost and the coupon would be removed. Phases must be sequential, meaning only one phase can be active at a given time.

### Set the length of a phase

The interval of a price determines how often to bill for a subscription. For example, a monthly interval is billed every month. Phases have an iterations attribute that you use to specify how long a phase should last. Multiply this value by the interval to determine the length of the phase. If a subscription schedule uses a price with a monthly interval and you set iterations=2, the phase lasts for two months.

The end_date of one phase has to be the start_date for the next phase. Using iterations automatically sets the start_date and end_date properly. You can set these values manually, but Stripe recommends using iterations instead. Because manually setting the start and end dates is prone to errors, only use it for advanced use cases.

### Transition to the next phase

Phase transitions happen automatically after the end_date on a phase is reached. When a phase starts, Stripe updates the subscription based on the attributes of the next phase. You can optionally enable proration to credit the user for unused items or time on the plan.

### Use trials

You can add trial periods by setting trial end on a phase. If you want the entire phase to be a trial, set the value of trial_end to the same time as the end_date of the phase. You can also set trial_end to a time before the end_date if you want to make only part of the phase a trial. When scheduling updates, you must specify the new trial_end on each phase.

### Complete a schedule

Subscription schedules end after the last phase is complete. At this point, the subscription is left in place and is no longer associated with the schedule. If you want to cancel a subscription after the last phase of a schedule completes, you can set end_behavior to cancel.

### Phase attribute inheritance

When a phase becomes active, all attributes set on the phase are also set on the subscription. After the phase ends, attributes remain the same unless the next phase modifies them, or if the schedule has no default setting. You can set some attributes on both schedules and phases. This includes:

Schedule attributePhase attribute[default_settings.billing_thresholds](/api/subscription_schedules/object#subscription_schedule_object-default_settings-billing_thresholds)[phases.billing_thresholds](/api/subscription_schedules/object#subscription_schedule_object-phases-billing_thresholds)[default_settings.collection_method](/api/subscription_schedules/create#create_subscription_schedule-default_settings-collection_method)[phases.collection_method](/api/subscription_schedules/create#create_subscription_schedule-phases-collection_method)[default_settings.default_payment_method](/api/subscription_schedules/create#create_subscription_schedule-default_settings-default_payment_method)[phases.default_payment_method](/api/subscription_schedules/create#create_subscription_schedule-phases-default_payment_method)[default_settings.invoice_settings](/api/subscription_schedules/create#create_subscription_schedule-default_settings-invoice_settings)[phases.invoice_settings](/api/subscription_schedules/create#create_subscription_schedule-phases-invoice_settings)If one of these attributes is defined on the schedule, it becomes the default for all phases. When the same property is defined on both the schedule and the phase, the phase attribute overrides the schedule attribute. This behavior is explained more below:

Schedule attribute presentPhase attribute presentOutcomeNoNoDefaults to the customer or account settingsYesNoSchedule attribute setYesYesPhase attribute setNoYesPhase attribute set### Use phase metadata

You can use subscription schedule phases to set metadata on the underlying subscription. This allows you to control the metadata on a subscription with scheduled updates.

APIDashboardTo use phase metadata with the API, set metadata on the phases of a subscription schedule. When the underlying subscription enters a phase:

- Metadata from the phase with non-empty values areaddedto the metadata on the subscription if the keysaren’talready present in the latter.
- Metadata from the phase with non-empty values are used toupdatethe metadata on the subscription if the keysarealready present in the latter.
- Metadata from the phase withempty valuesare used tounsetthe corresponding keys in the metadata on the subscription.

To unset all keys in the subscription’s metadata, update the subscription directly or unset every key individually from the phase’s metadata. Updating the underlying subscription’s metadata directly doesn’t affect the current phase’s metadata.

The following example illustrates a subscription schedule with two phases, where each phase has its own metadata:

`{
  ...
  "object": "subscription_schedule",
  "phases": [
    { // Phase 1
      ...
      "metadata": {
        "channel": "self-serve",
        "region": "apac",
        "upsell-products": "alpha"
      },
    },
    { // Phase 2
      ...
      "metadata": {
        "channel": "sales",
        "churn-risk": "high",
        "upsell-products": ""
      },
    }
  ],
}`When this schedule creates a new subscription and the subscription enters Phase 1, the three keys in Phase 1 metadata are added to the subscription’s metadata. Hence, the subscription in Phase 1 has the following metadata:

`{
  ...
  "object": "subscription",
  "metadata": {
    "channel": "self-serve",
    "region": "apac",
    "upsell-products": "alpha"
  },
}`When the subscription enters Phase 2, the subscription’s metadata is updated:

- The value of`channel`is updated because a value is specified on the phase’s metadata and the subscription already has metadata with that key.
- The value of`region`is unchanged because it’s not specified on the phase.
- `churn-risk`is added because this is a new key.
- `upsell-products`is unset because an empty value is specified on the phase.

Hence, the subscription in Phase 2 has the following metadata:

`{
  ...
  "object": "subscription",
  "metadata": {
    "channel": "sales",
    "region": "apac",
    "churn-risk": "high"
  }
}`Learn how to copy subscription metadata onto subscription invoices.

## Create subscription schedules

The use cases page has more thorough examples but below is a basic example of creating a subscription schedule using a customer. Creating a schedule this way automatically creates the subscription as well.

NoteUnlike when you create a subscription directly, the first invoice of a subscription schedule with collection_method set to charge_automatically behaves like a recurring invoice and isn’t immediately finalized at the time the schedule’s subscription is created. The invoice begins in a draft status and is finalized by Stripe about 1 hour after creation.

This means that, for example, creating a charge-automatically subscription schedule with start_date=now also creates a subscription and an invoice in the draft status. This gives you a 1-hour window to make edits to the invoice. Later, the invoice is auto-advanced into the open or paid status depending on the outcome of the asynchronous payment attempt at finalization time.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer=cus_GBHHxuvBvO26Ea \
  -d start_date=now \
  -d end_behavior=release \
  -d "phases[0][items][0][price]"=price_1GqNdGAJVYItwOKqEHb \
  -d "phases[0][items][0][quantity]"=1 \
  -d "phases[0][iterations]"=12`This schedule:

- Starts as soon as it’s created.
- Sets the subscription to one instance of the product at`price_1GqNdGAJVYItwOKqEHb`.
- Goes through 12 iterations and then releases the subscription from the schedule.

You can also create subscription schedules by passing a subscription ID:

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d from_subscription=sub_GB98WOvaRAWPl6`Creating a schedule this way uses attributes on the subscription to set attributes on the schedule.

Similar to other Stripe APIs, you can retrieve and update subscription schedules. You can also cancel and release them. Cancelling a subscription schedule cancels the subscription as well. If you only want to remove a schedule from a subscription, use the release call.

### Create subscription schedules without code

You can create multi-phase subscription schedules without using code in the Stripe Billing subscription editor. To do so, follow these steps:

1. In the Dashboard, open the[subscription editor](https://dashboard.stripe.com/subscriptions?create=subscription).
2. Add a customer.
3. Add a price to the product selection dropdown.
4. Set a duration for the first phase of the subscription schedule.
5. Click+ Add phase.
6. Select your next phase duration, or justforeverto keep the subscription going.
7. Make the required changes to your new phase. You can change the quantity, change the price, add or remove coupons, reset the billing cycle date, change proration behavior, or update metadata. If you change the metadata in a phase, it updates the subscription’s metadata when that phase activates.
8. Save the new phase.
9. Add any additional phases as needed.
10. Create a subscription.

## Update subscription schedules

You can only update the current and future phases on subscription schedules. You need to pass in all current and future phases when you update a subscription schedule. You also need to pass in any previously set parameters that you want to keep. Any parameters that were previously set are unset for the existing phase unless you pass those in the update request. You still receive information in the response about past phases.

You can include up to 10 current or future phases. Updating the active phase updates the underlying subscription as well. For example, this call maintains the existing start and end dates, but updates the quantity to two:

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules/{{SUBSCRIPTION_SCHEDULE_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "phases[0][items][0][price]"={{PRICE_ID}} \
  -d "phases[0][items][0][quantity]"=2 \
  -d "phases[0][start_date]"=1577865600 \
  -d "phases[0][end_date]"=1580544000`You can also end the current phase immediately and start a new phase. This moves the active phase to the past and immediately applies the new phase to the subscription. The example below ends the current phase and starts a new phase:

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules/{{SUBSCRIPTION_SCHEDULE_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "phases[0][items][0][price]"={{PRICE_ID}} \
  -d "phases[0][items][0][quantity]"=1 \
  -d "phases[0][start_date]"=1577865600 \
  -d "phases[0][end_date]"=now \
  -d "phases[1][items][0][price]"={{PRICE_ID}} \
  -d "phases[1][items][0][quantity]"=2 \
  -d "phases[1][start_date]"=now \
  -d "phases[1][end_date]"=1580544000`To add additional phases to a subscription schedule, pass in the current phase, and then define your new phases:

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules/{{SUBSCRIPTION_SCHEDULE_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "phases[0][items][0][price]"={{PRICE_ID}} \
  -d "phases[0][items][0][quantity]"=1 \
  -d "phases[0][start_date]"=1577865600 \
  -d "phases[0][end_date]"=1580544000 \
  -d "phases[1][items][0][price]"={{PRICE_ID}} \
  -d "phases[1][items][0][quantity]"=2 \
  -d "phases[1][iterations]"=1`### Update subscription schedules without code

You can update existing subscriptions to have future subscription schedule phases using the Stripe Billing subscription editor. To do so, follow these steps:

1. In the Dashboard, go to the[Subscriptions](https://dashboard.stripe.com/subscriptions)page, select an existing subscription, and clickActions>Update subscription.
2. Set a duration for the current phase of the subscription schedule by selecting an end date.
3. Click+Add phase.
4. Select your next phase duration, or just selectforeverto keep the subscription going.
5. Make the required changes to your new phase. You can change the quantity, change the price, add or remove coupons, reset the billing cycle date, change proration behavior, or update metadata. If you change the metadata in a phase, it updates the subscription’s metadata when that phase activates.
6. Save the new phase.
7. Add any additional phases as needed.
8. Create a subscription.

## Preview an invoice

Use the schedule parameter in the upcoming invoice API to preview the next invoice for a subscription schedule.

Command Line[curl](#)`curl https://api.stripe.com/v1/invoices/create_preview \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d schedule={{SUBSCRIPTION_SCHEDULE_ID}}`### Previewing schedule creation and updates

Use the parameters in schedule_details to preview creating or updating a subscription schedule. Pass an existing schedule to tell Stripe whether it’s a creation or an update.

Pass all of the current and future phases you’re previewing.

For example, the following code previews the first invoice for a subscription schedule with 1 phase that lasts for 12 billing periods.

Command Line[curl](#)`curl https://api.stripe.com/v1/invoices/create_preview \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "customer_details[address][line1]"="920 5th Ave" \
  -d "customer_details[address][city]"=Seattle \
  -d "customer_details[address][state]"=WA \
  -d "customer_details[address][postal_code]"=98104 \
  -d "customer_details[address][country]"=US \
  -d "schedule_details[phases][0][start_date]"=now \
  -d "schedule_details[phases][0][items][0][price]"={{PRICE_ID}} \
  -d "schedule_details[phases][0][items][0][quantity]"=1 \
  -d "schedule_details[phases][0][iterations]"=12`## Dashboard limitations

You can create and update subscription schedules without code in the Dashboard.

In the Dashboard, you can set the following settings globally across all phases, but not on a per phase basis:

- Billing thresholds
- Payment methods
- Invoice settings
- Subscription description
- Trial days (only works with the first phase)

The following parameters aren’t supported in the Dashboard:

- Subscription schedule metadata
- Phase item metadata
- Currency
- All Connect parameters

## See also

- [Subscription Schedules use cases](/billing/subscriptions/subscription-schedules/use-cases)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Phases](#subscription-schedule-phases)[Create subscription schedules](#managing)[Update subscription schedules](#updating)[Preview an invoice](#preview-an-invoice)[Dashboard limitations](#dashboard-limitations)[See also](#see-also)Products Used[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`