htmlAsynchronous Capture | Stripe Documentation[Skip to content](#main-content)Asynchronous Capture[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-intents%2Fasynchronous-capture)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-intents%2Fasynchronous-capture)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)
[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[About the APIs](/docs/payments-api/tour)[Payment Intents API](/docs/payments/payment-intents)# Asynchronous Capture

Learn how to use Asynchronous Capture to enable faster PaymentIntent confirmations.Asynchronous capture reduces the latency of PaymentIntent confirmations by making the capture operation take place in the background. After making the capture request, your integration receives a successful response, and Stripe completes payment capture in the backend. To use these faster PaymentIntent captures, set the capture_method=automatic_async parameter when confirming a PaymentIntent.

[Opt in to asynchronous capture](#opt-in-async-capture)To upgrade your existing integration and add support for asynchronous capture, use automatic_async as the capture method when creating a PaymentIntent:

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d amount=2000 \
  -d currency=usd \
  -d "payment_method_types[]"=card \
  -d payment_method=pm_card_visa \
  -d capture_method=automatic_async \
  -d confirm=true`You might need to make additional changes when you opt into asynchronous capture since the API response and some webhooks have different behavior than with other capture methods.

For all payments, the balance_transaction is null on the following objects. For Connect payments, the transfer and application_fee are also null on the following objects:

- attached[Charge](/api/charges/object)object of the API response
- [charge.succeeded](/api/events/types#event_types-charge.succeeded)webhook
- [payment_intent.succeeded](/api/events/types#event_types-payment_intent.succeeded)webhook

Modified Charge object on the charge.succeeded webhook:

`# Charge Object
{
    "id": "ch_123",
    "object": "charge",
    "amount_captured": 1000, # the capture has happened
    "application_fee_amount": 100,
    "captured": true,
    "balance_transaction": "txn_123", # applicable to all charges.
    "transfer": "tr_123",         # applicable to destination charge only.
    "application_fee": "fee_123", # applicable to destination charge only.
    "balance_transaction": null,  # object might not be created yet, might be shown as nil.
    "transfer": null,             # object might not be created yet, might be shown as nil.
    "application_fee": null,      # object might not be created yet, might be shown as nil.
    ...
}`Modified API response and payment_intent.succeeded webhook: (different based on API version)

[API version 2022-11-15 or later](#)`# PaymentIntent Object
{
  "id": "pi_123",
  "object": "payment_intent",
  "capture_method": "automatic_async",
  "status": "succeeded",
  "latest_charge": "ch_**" # if expanded, this is the Modified Charge object above
}`[Listen to webhooks to get notified when additional data is available](#listen-webhooks)WarningOur SLA for the charge.updated webhook is 1 hour after the successful PaymentIntent confirmation.

You can listen to webhooks to check the status of objects that are initially null when using asynchronous capture.

- To get the[balance_transaction](/api/balance_transactions), subscribe to the[charge.updated](/api/events/types#event_types-charge.created)webhook event.
- To get the[application_fee](/api/payment_intents/create#create_payment_intent-application_fee_amount), subscribe to the[application_fee.created](/api/events/types#event_types-application_fee.created)webhook event.
- To get the[transfer](/api/charges/object#charge_object-transfer), subscribe to the[transfer.created](/api/events/types#event_types-transfer.created)webhook events.

Webhooks for Asynchronous Capture

`# charge.updated events
{
  "data": {
    "id": "ch_123",
    "object": "charge",
    "amount": 100,
    "balance_transaction": "txn_123", # applicable to all charges.
    "transfer": "tr_123",         # applicable to destination charge only.
    "application_fee": "fee_123", # applicable to destination charge only.
    ...
  },
  previous_attributes: {
   "balance_transaction": null, # applicable to all charges.
   "transfer": null,          # applicable to destination charge only.
   "application_fee": null,   # applicable to destination charge only.
  }
}``# transfer.created events
{
  "data": {
    "id": "tr_123",
    "object": "transfer",
    "amount": 1000,
    ...
  }
}``# application_fee.created events
{
  "data": {
    "id": "fee_123",
    "object": "application_fee",
    "amount": 100,
    ...
  }
}`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Opt in to asynchronous capture](#opt-in-async-capture)[Listen to webhooks to get notified when additional data is available](#listen-webhooks)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`