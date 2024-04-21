htmlProrations | Stripe Documentation[Skip to content](#main-content)Manage prorations[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fprorations)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fprorations)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Subscriptions](/docs/subscriptions)[Manage subscription cycles](/docs/billing/subscriptions/change)# Prorations

Learn about prorations.Changes to a subscription such as upgrading or downgrading can result in prorated charges. For example, if a customer upgrades from a 10 USD per month subscription to a 20 USD option, they’re charged prorated amounts for the time spent on each option. Assuming the change occurred halfway through the billing period, the customer is billed an additional 5 USD: -5 USD for unused time on the initial price, and 10 USD for the remaining time on the new price.

The prorated amount is calculated as soon as the API updates the subscription. The current billing period’s start and end times are used to calculate the cost of the subscription before and after the change.

NoteProrations are created only for licensed (per-seat) subscriptions because they’re billed at the start of each billing period.

For information about how taxes work with prorations, see Collect taxes for recurring payments.

## Preview a proration

You can retrieve an upcoming invoice to preview changes to a subscription. This API call doesn’t modify the subscription, it returns the upcoming invoice based only on the parameters that you pass. Changing the price or quantity both result in a proration. This example changes the price and sets a date for the proration.

[Ruby](#)`# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

# Set proration date to this moment:
proration_date = Time.now.to_i

subscription = Stripe::Subscription.retrieve('sub_49ty4767H20z6a')

# See what the next invoice would look like with a price switch
# and proration set:
items = [{
  id: subscription.items.data[0].id,
  price: 'price_CBb6IXqvTLXp3f', # Switch to new price
}]

invoice = Stripe::Invoice.upcoming({
  customer: 'cus_4fdAW5ftNQow1a',
  subscription: 'sub_49ty4767H20z6a',
  subscription_items: items,
  subscription_proration_date: proration_date,
})`You can expand the example response below to see:

- The credit for unused time at the previous price on lines 36-38.
- The cost for time spent at the new price on lines 107-109.
- The new subtotal and total for the invoice on lines 276-279.

`{
  "account_country": "US",
  "account_name": "Test account",
  "amount_due": 3627,
  "amount_paid": 0,
  "amount_remaining": 3627,
  "application_fee_amount": null,
  "attempt_count": 0,
  "attempted": false,
  "billing_reason": "upcoming",`See all 284 linesYou can use this information to confirm the changes with the customer before modifying the subscription. Because Stripe prorates to the second, prorated amounts can change between the time they’re previewed and the time the update is made. To avoid this, pass in a subscription_proration_date to the invoice when you preview a change. When you update the subscription, you can pass the same date using the proration_date parameter on a subscription so that the proration is calculated at the same time.

[Ruby](#)`# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

subscription = Stripe::Subscription.update(
  'sub_49ty4767H20z6a',
  {
    items: [
      {
        id: subscription.items.data[0].id,
        price: 'price_CBb6IXqvTLXp3f',
      },
    ],
    proration_date: proration_date,
  }
)`## Disable prorations

Prorating is controlled by the proration_behavior parameter and defaults to create_prorations.

You can disable prorations on a per-request basis by setting the proration_behavior parameter to none. There is no parameter that turns off all future prorations for a Subscription. If you want to disable prorations indefinitely, you need to set proration_behavior to none for every request that generates prorations:

Command Line[curl](#)`curl https://api.stripe.com/v1/subscriptions/sub_49ty4767H20z6a \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "items[0][id]"="si_1AkFf6LlRB0eXbMtRFjYiJ0J" \
  -d "items[0][price]"="price_CBb6IXqvTLXp3f" \
  -d "proration_behavior"="none"`When prorations are disabled, customers are billed the full amount at the new price when the next invoice is generated.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Preview a proration](#preview-proration)[Disable prorations](#disable-prorations)Products Used[Billing](/billing)[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`