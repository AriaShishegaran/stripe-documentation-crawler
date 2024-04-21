htmlSubscription schedules use cases | Stripe Documentation[Skip to content](#main-content)Use cases[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fsubscription-schedules%2Fuse-cases)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fsubscription-schedules%2Fuse-cases)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Subscriptions](/docs/subscriptions)[Subscription schedules](/docs/billing/subscriptions/subscription-schedules)# Subscription schedules use cases

Learn how to use subscription schedules.To understand subscription schedules, imagine a fictional newspaper company called The Pacific. It offers two subscription options:

- Print, where customers receive the physical paper
- Digital, where customers get access to exclusive content on The Pacific’s website

Both subscriptions bill monthly. Browse possible options for subscription schedules below.

## Start a subscription in the future

By default, new print subscriptions start on the first day of the next month. To accomplish this, the start_date is set to a point in the future. The code below creates a subscription that starts in the future:

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d start_date=1690873200 \
  -d end_behavior=release \
  -d "phases[0][items][0][price]"={{PRICE_PRINT}} \
  -d "phases[0][items][0][quantity]"=1 \
  -d "phases[0][iterations]"=12`## Backdate a subscription

When customers subscribe to the digital plan, The Pacific backdates their subscriptions to the first day of the current month. Backdating charges for time in the past and allows digital subscribers to access the website immediately.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d start_date=1688194800 \
  -d end_behavior=release \
  -d "phases[0][items][0][price]"={{PRICE_DIGITAL}} \
  -d "phases[0][items][0][quantity]"=1 \
  -d "phases[0][iterations]"=12`## Add a schedule to an existing subscription

The Pacific may discover that some of their original customers are on subscriptions without schedules. Because these subscriptions exist already, the subscription IDs can be passed in the from_subscription attribute to add a schedule. Passing the subscription IDs in this way creates a schedule with one phase that’s based on the current billing period of the subscription.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d from_subscription={{SUBSCRIPTION_ID}}`While adding these schedules, some customers decide to get a print subscription so The Pacific adds a second phase to the schedule to start the print plan one month from now. The following use case shows an example of this process.

## Upgrade subscriptions

The Pacific offers an option to start with a print subscription for one month, then automatically add the digital option. Some customers prefer this because they can test out the print publication first and then decide if they want to continue or cancel their subscription.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d start_date=now \
  -d end_behavior=release \
  -d "phases[0][items][0][price]"={{PRICE_PRINT}} \
  -d "phases[0][items][0][quantity]"=1 \
  -d "phases[0][iterations]"=1 \
  -d "phases[1][items][0][price]"={{PRICE_PRINT}} \
  -d "phases[1][items][0][quantity]"=1 \
  -d "phases[1][items][1][price]"={{PRICE_DIGITAL}} \
  -d "phases[1][items][1][quantity]"=1 \
  -d "phases[1][iterations]"=11`## Downgrade subscriptions

The Pacific also offers an option to start a subscription with both the print and digital publications, and then downgrade to only the print publication for the rest of the subscription. Customers use this option to test out both publications to see how they like them.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d start_date=now \
  -d end_behavior=release \
  -d "phases[0][items][0][price]"={{PRICE_DIGITAL}} \
  -d "phases[0][items][0][quantity]"=1 \
  -d "phases[0][items][1][price]"={{PRICE_PRINT}} \
  -d "phases[0][items][1][quantity]"=1 \
  -d "phases[0][iterations]"=1 \
  -d "phases[1][items][0][price]"={{PRICE_PRINT}} \
  -d "phases[1][items][0][quantity]"=1 \
  -d "phases[1][iterations]"=11`## Change subscriptions

The Pacific offers two print subscription options, a basic option with advertisements or a premium option without advertisements. Some customers on the premium option decide they want to change to the basic option with advertisements at the next billing cycle. Create a schedule using the existing subscription and then update the schedule with the basic option with advertisements as a new phase.

server.rb[Ruby](#)`# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

# Create a subscription schedule with the existing subscription
schedule = Stripe::SubscriptionSchedule.create({
  from_subscription: 'sub_ERf72J8Sc7qx7D',
})

# Update the schedule with the new phase
Stripe::SubscriptionSchedule.update(
  schedule.id,
  {
    phases: [
      {
        items: [
          {
            price: schedule.phases[0].items[0].price,
            quantity: schedule.phases[0].items[0].quantity,
          },
        ],
        start_date: schedule.phases[0].start_date,
        end_date: schedule.phases[0].end_date,
      },
      {
        items: [
          {
            price: '{{PRICE_PRINT_BASIC}}',
            quantity: 1,
          },
        ],
        iterations: 1,
      },
    ],
  },
)`## Increase the quantity

You can also schedule increases to the quantities on a subscription. The schedule below starts with one instance of the digital publication for one month. In the second phase, the quantity is increased to 2 for 11 more months.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d start_date=now \
  -d end_behavior=release \
  -d "phases[0][items][0][price]"={{PRICE_ID}} \
  -d "phases[0][items][0][quantity]"=1 \
  -d "phases[0][iterations]"=1 \
  -d "phases[1][items][0][price]"={{PRICE_ID}} \
  -d "phases[1][items][0][quantity]"=2 \
  -d "phases[1][iterations]"=11`## Use coupons

Sometimes The Pacific runs subscription specials. The schedule below starts the customer on the print publication at 50% off for six months. The schedule removes the coupon from the subscription in the second phase, which entails the remaining six months.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d start_date=now \
  -d end_behavior=release \
  -d "phases[0][items][0][price]"={{PRICE_ID}} \
  -d "phases[0][items][0][quantity]"=1 \
  -d "phases[0][iterations]"=6 \
  -d "phases[0][coupon]"={{COUPON_ID}} \
  -d "phases[1][items][0][price]"={{PRICE_ID}} \
  -d "phases[1][items][0][quantity]"=1 \
  -d "phases[1][iterations]"=6`## Change tax rates

The Pacific operates in several jurisdictions, and some of them have unique tax rates for subscription based businesses. One of these jurisdictions requires two tax rates: one for the first month when a customer initially subscribes, and one for recurring billings.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d start_date=now \
  -d end_behavior=release \
  -d "phases[0][items][0][price]"={{PRICE_ID}} \
  -d "phases[0][items][0][quantity]"=1 \
  -d "phases[0][items][0][tax_rates][0]"=txr_2J8lmBBGHJYyuUJqF6QJtaAA \
  -d "phases[0][iterations]"=1 \
  -d "phases[1][items][0][price]"={{PRICE_ID}} \
  -d "phases[1][items][0][quantity]"=1 \
  -d "phases[1][items][0][tax_rates][0]"=txr_2J8lmBBGHJYyuUJqF6QJtbBB \
  -d "phases[1][iterations]"=11`## Release a subscription from a schedule

You can release a subscription from a schedule as long as the status of the schedule is not_started or active. Releasing a subscription leaves it in place but removes the schedule and any remaining phases.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/subscription_schedules/{{SUBSCRIPTION_SCHEDULE_ID}}/release \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`## Cancel a schedule and subscription

You can cancel a subscription schedule and its associated subscription immediately (if the subscription schedule has an active subscription). A subscription schedule can only be canceled if its status is not_started or active.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/subscription_schedules/{{SUBSCRIPTION_SCHEDULE_ID}}/cancel \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`## Reset the billing cycle anchor

The Pacific bills their long-time print customers on whichever day of the month they originally subscribed. This day is their billing cycle anchor.

If these customers transition to the digital edition, The Pacific schedules their transition date for the 1st day of the following month. They also reset the billing cycle anchor to that same date.

You can verify that the billing cycle anchor gets reset by creating a subscription using the sample code below. Look at the subscription in the Dashboard, and notice that the Upcoming Invoice is scheduled to bill the customer as soon as the digital subscription starts on the 1st.

To see what happens if you don’t reset the anchor, run the sample code again, but remove the line that sets the billing cycle anchor to phase_start. Without that line, the Upcoming Invoice in the Dashboard waits to bill the customer until a full month from today, despite the transition that occurs on the 1st.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d start_date=now \
  -d "phases[0][items][0][price]"={{PRICE_PRINT}} \
  -d "phases[0][items][0][quantity]"=1 \
  -d "phases[0][end_date]"=1690873200 \
  -d "phases[1][items][0][price]"={{PRICE_DIGITAL}} \
  -d "phases[1][items][0][quantity]"=1 \
  -d "phases[1][iterations]"=11 \
  -d "phases[1][billing_cycle_anchor]"=phase_start`## Installment plans

Installment plans allow customers to make partial payments for a set amount of time until the total amount is paid. For example, when The Pacific buys new printing presses, they sell the used ones to other publications. Smaller publications rarely have enough funds to pay for a printing press upfront, so they pay using an installment plan instead.

For most presses, The Pacific charges 1,000 USD per month so a reusable price is created:

Command Line[curl](#)`curl https://api.stripe.com/v1/prices \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d unit_amount=100000 \
  -d currency=usd \
  -d product=prod_Hh99apo1OViyGW \
  -d "recurring[interval]"=month`Depending on the make, model, and age of the printing press, The Pacific charges different amounts. This example charges 1,000 USD each month for 6 months, for a total of 6,000 USD.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d start_date=now \
  -d end_behavior=cancel \
  -d "phases[0][items][0][price]"={{PRICE_ID}} \
  -d "phases[0][items][0][quantity]"=1 \
  -d "phases[0][iterations]"=6`The number of iterations is multiplied by the price’s interval—6 monthly payments in this example—to determine the number of times the customer is charged. end_behavior determines what happens to the subscription after the last iteration is complete. In an installment plan, the subscription isn’t needed anymore so end_behavior is set to cancel.

In rare cases, The Pacific charges less than the usual 1,000 USD per month. In these scenarios, they use price_data to create a single-use price. This example creates a 500 USD price, and charges monthly for 6 months:

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_schedules \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d start_date=now \
  -d end_behavior=cancel \
  -d "phases[0][items][0][price_data][currency]"=usd \
  -d "phases[0][items][0][price_data][product]"=prod_Hh99apo1OViyGW \
  -d "phases[0][items][0][price_data][recurring][interval]"=month \
  -d "phases[0][items][0][price_data][unit_amount]"=50000 \
  -d "phases[0][items][0][quantity]"=1 \
  -d "phases[0][iterations]"=6`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Start a subscription in the future](#start-subscription-future)[Backdate a subscription](#backdating-subscription)[Add a schedule to an existing subscription](#existing-subscription)[Upgrade subscriptions](#upgrading-subscriptions)[Downgrade subscriptions](#downgrading-subscriptions)[Change subscriptions](#changing-subscriptions)[Increase the quantity](#increasing-quantity)[Use coupons](#upgrade-downgrade-coupons)[Change tax rates](#changing-tax-rates)[Release a subscription from a schedule](#releasing-subscription)[Cancel a schedule and subscription](#cancel-schedule-and-subscription)[Reset the billing cycle anchor](#resetting-anchor)[Installment plans](#installment-plans)Products Used[Billing](/billing)[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`