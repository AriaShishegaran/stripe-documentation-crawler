htmlUpgrade and downgrade subscriptions | Stripe Documentation[Skip to content](#main-content)Upgrade and downgrade subscriptions[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fupgrade-downgrade)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fupgrade-downgrade)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Subscriptions](/docs/subscriptions)[Manage subscription cycles](/docs/billing/subscriptions/change)# Upgrade and downgrade subscriptions

Learn how to upgrade and downgrade subscriptions by changing the price.### Customer portal

This guide focuses on using the Subscriptions API to manage customer subscriptions.

You can also implement the customer portal to provide a Stripe-hosted Dashboard where customers can manage their subscriptions and billing details.

When a customer changes their subscription, you must change the subscription item to reflect the new selection. For example, a customer might upgrade to a premium tier or downgrade to a basic tier, prompting you to replace the underlying price of that subscription item. You can do this using a few different methods.

## Retrieve the identifiers

Regardless of the method you choose, you’ll need to provide identifiers for the objects you’re updating. Use the list subscriptions method with a relevant filter (such as the customer ID) to find the subscription and item to update.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/subscriptions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}}`The returns the set of subscriptions for the specified customer, from which you can retrieve the subscription ID (id), any subscription item IDs (items.data.id) and the subscription items price ID (items.data.price.id).

Retrieve subscriptions response sample`{
  "object": "list",
  "url": "/v1/subscriptions",
  "has_more": false,
  "data": [
    {
      "id": "su_1NXPiE2eZvKYlo2COk9fohqA",
      "object": "subscription",
      "application": null,
      "application_fee_percent": null,
      "automatic_tax": {
        "enabled": false
      },
      "items": {
        "object": "list",
        "data": [
          {
            "id": "si_OK3pbS1dvdQYJP",
            "object": "subscription_item",
            "billing_thresholds": null,
            "created": 1690208774,
            "metadata": {},
            "price": {
              "id": "price_1NOhvg2eZvKYlo2CqkpQDVRT",
              "object": "price"
            }
          }
        ]
      }
    }
  ]
}`## Update the subscription

Update a subscription by specifying the subscription item to apply the updated price to.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscriptions/sub_xxxxxxxxx \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "items[0][id]"={{SUB_ITEM_ID}} \
  -d "items[0][price]"={{NEW_PRICE_ID}}`Common mistakeYou must specify the subscription item to replace the current price with the new price. Failing to do so results in adding the new price so both prices are active for the subscription.

Alternatively, you can delete the current subscription item and create a new subscription item with the updated price.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscriptions/sub_xxxxxxxxx \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "items[0][id]"={{SUB_ITEM_ID}} \
  -d "items[0][deleted]"=true \
  -d "items[1][price]"={{NEW_PRICE_ID}}`## Update the subscription item

You can update a subscription item to modify the subscription item directly. Use this option if you don’t need to make any other changes at the subscription level.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscription_items/si_xxxxxxxxx \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d price={{NEW_PRICE_ID}}`## Billing periods

If both prices have the same billing periods (combination of interval and interval_count), the subscription retains the same billing dates. If the prices have different billing periods, the new price is billed at the new interval, starting on the day of the change. For example, switching a customer from one monthly subscription to another doesn’t change the billing dates. However, switching a customer from a monthly subscription to a yearly subscription moves the billing date to the date of the switch. Switching a customer from one monthly subscription to another monthly subscription while introducing a trial period also moves the billing date (to the conclusion of the trial).

## Metered billing

If you have metered billing subscriptions, the subscription item retains usage upon updating the price. If you wish to update the price without retaining any of the existing usage, set subscription.items.clear_usage to true.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscriptions/sub_xxxxxxxxx \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "items[0][id]"={{SUB_ITEM_ID}} \
  -d "items[0][price]"={{NEW_PRICE_ID}} \
  -d "items[0][clear_usage]"=true`## Proration

Changing a subscription often results in a proration to apply the new price to the remaining days in the billing period. You can prepare your customer for any additional expense resulting from a price change by previewing a proration. Alternatively, you can disable prorations.

### Immediate payment

Stripe immediately attempts payment for these subscription changes:

- From a subscription that doesn’t require payment (for example, due to a trial or free subscription) to a paid subscription
- When the billing period changes

When billing is performed immediately, but the required payment fails, the subscription change request succeeds and the subscription transitions to past_due.

To bill a customer immediately for a change to a subscription on the same billing cycle, set proration_behavior to always_invoice. This calculates the proration, then immediately generates an invoice after making the switch. Combine this setting with pending updates so the subscription doesn’t update unless payment succeeds on the new invoice.

### Credits for downgrades

When invoicing immediately for a downgrade, the customer might be owed a credit, which is added to their credit balance to be applied to future invoices. To refund your customer, issue refunds and then adjust their account balance back to zero. Learn more about customer refunds on our dedicated support page.

### Handling zero-amount prices and quantities

If you’ve subscribed a customer to a zero-amount price (for example, as a trial), changing the price to a non-zero amount generates an invoice and resets the billing period to the date of the change.

If you’ve subscribed a customer to a price with a non-zero amount and a zero-amount quantity, changing the quantity to a non-zero amount does not generate an invoice or reset the billing period.

## See also

- [Billing cycle](/billing/subscriptions/billing-cycle)
- [Canceling and pausing](/billing/subscriptions/cancel)
- [Update Subscription API](/api#update_subscription)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Retrieve the identifiers](#retrieve-the-identifiers)[Update the subscription](#changing)[Update the subscription item](#update-the-subscription-item)[Billing periods](#billing-periods)[Metered billing](#metered-billing)[Proration](#proration)[See also](#see-also)Products Used[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`