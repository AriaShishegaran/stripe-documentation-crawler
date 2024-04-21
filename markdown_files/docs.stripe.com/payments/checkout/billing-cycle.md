htmlSet the billing cycle date in Checkout | Stripe Documentation[Skip to content](#main-content)Set billing cycle date[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fbilling-cycle)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fbilling-cycle)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Checkout](/payments/checkout)·[Home](/docs)[Payments](/docs/payments)[Checkout](/docs/payments/checkout)# Set the billing cycle date in Checkout

Use Stripe Checkout to set a billing cycle date for subscriptions.You can explicitly set a subscription’s billing cycle anchor to a fixed date (for example, the 1st of the next month) in Checkout.

The billing cycle anchor determines the first full invoice date, when customers are billed the full subscription amount. The billing cycle anchor and the recurring interval of its price also determine a subscription’s future billing dates. For example, a monthly subscription created in Checkout on May 15 with an anchor at June 1 is billed on May 15, then always on the 1st of the month.

For the initial billing period up until the first full invoice date, you can customize how to handle prorations with the proration_behavior parameter. By default, proration_behavior is set to create_prorations, and customers receive a prorated invoice. If proration_behavior is none, customers receive the initial period up to the first full invoice date for free.

## Create a Checkout Session with a billing cycle anchor

To configure a billing cycle anchor, set the subscription_data.billing_cycle_anchor parameter when you create a Checkout Session in subscription mode.

The anchor must be a future UNIX timestamp before the next natural subscription billing date.

Stripe-hosted pageEmbedded formCommand Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "line_items[][price]"={{PRICE_ID}} \
  -d "line_items[][quantity]"=1 \
  -d "mode"="subscription" \
  -d "success_url"="https://example.com/success?session_id={CHECKOUT_SESSION_ID}" \
  -d "cancel_url"="https://example.com/cancel" \
  -d "subscription_data[billing_cycle_anchor]"=1611008505`If the billing cycle anchor is during a session’s active period and a customer attempts payment after it has passed, Checkout displays and charges for the full period starting with the billing cycle anchor instead of the prorated period before the billing cycle anchor.

## Disable prorations

To disable prorations, set the subscription_data.proration_behavior parameter to none when creating a Checkout Session.

Stripe-hosted pageEmbedded formCommand Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "line_items[][price]"={{PRICE_ID}} \
  -d "line_items[][quantity]"=1 \
  -d "mode"="subscription" \
  -d "success_url"="https://example.com/success?session_id={CHECKOUT_SESSION_ID}" \
  -d "cancel_url"="https://example.com/cancel" \
  -d "subscription_data[billing_cycle_anchor]"=1611008505
  -d "subscription_data[proration_behavior]"="none"`Similar to a free trial, the initial period up to the billing cycle anchor is free. Unlike a trial, no 0 USD invoice is generated. Customers receive an invoice with the full subscription amount on the billing cycle anchor date.

In the Checkout Session response object, amounts attached to the line items and total details are always 0 when prorations are disabled. Additionally, the payment status of the Session is set to no_payment_required to reflect that payment is delayed to a future date.

## Current limitations

- You can’t use trials in Checkout with a billing cycle anchor.
- One-time prices can’t be used in Checkout Sessions when`proration_behavior`isnone.
- You can’t apply[amount_off coupons](/api/coupons/create#create_coupon-amount_off)to Checkout Sessions with a default`proration_behavior`ofcreate_prorations.

## See also

- [Setting the subscription billing cycle date](/billing/subscriptions/billing-cycle)
- [Prorations](/billing/subscriptions/prorations)
- [Create Checkout Session](/api/checkout/sessions/create#create_checkout_session)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a Checkout Session with a billing cycle anchor](#create-session)[Disable prorations](#disable-prorations)[Current limitations](#limitations)[See also](#see-also)Products Used[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`