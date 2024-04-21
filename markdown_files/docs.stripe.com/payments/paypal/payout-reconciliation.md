htmlPayPal payout reconciliation | Stripe Documentation[Skip to content](#main-content)Payout reconciliation[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpaypal%2Fpayout-reconciliation)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpaypal%2Fpayout-reconciliation)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Wallets](/docs/payments/wallets)[PayPal](/docs/payments/paypal)# PayPal payout reconciliation

Learn how to reconcile payments made through PayPal, a common payment method in Europe.Reconciliation is the process of matching and verifying payments that have been received and processed with the corresponding PayPal orders. It only applies to customers receiving their funds on PayPal, and not on Stripe. Stripe automatically reconciles PayPal transactions before the payout, whereas this can’t be done if transactions settle outside of Stripe’s platform. When transactions settle outside of Stripe’s platform, you’ll use PayPal reporting available on your PayPal account or with sFTP for reconciliation.

Stripe provides two ways of supporting PayPal transaction reconciliation:

- (Recommended) Using the[reference](#use-reference)field. This is the preferred option if you have a businesses-generated order or invoice ID, which you can put in the reference field. After the payment is made and processed,`my_order_id`appears as`Invoice ID`in the PayPal settlement report.
- Using the[transaction_id](#use-transaction-id)from the[Charge](/api/charges/object#charge_object-payment_method_details-paypal-transaction_id)object.  When the payment is processed,`paypal_capture_id`appears as`Transaction ID`in the PayPal settlement report. This is recommended only if you don’t have a business-generated order ID.

## Use Reference

Use the reference field to populate your own reference for an order on a PayPal payment. One example of this is an Order ID from PayPal. This reference is visible to the buyer and also in the settlement report on your PayPal account. To reconcile funds using a reference, you can include it as part of the payment_method_options parameter when creating a PaymentIntent. You can use this reference to match payments made through Stripe with corresponding transactions in the PayPal settlement report. Any subsequent transactions derived from the original Payment transaction, such as refunds and disputes, are associated with the given reference.

The following code sample shows the creation of a PaymentIntent with the reference set in payment_method_options:

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1099 \
  -d currency=eur \
  -d "payment_method_types[]"=paypal \
  -d "payment_method_options[paypal][reference]"=my_order_id`After the payment is made and processed, my_order_id is reflected as Invoice ID in the PayPal settlement report.

## Use the Charge object’s transaction ID

The transaction_id field contains the ID used by PayPal to identify a transaction. To reconcile funds using a transaction_id, retrieve the transaction_id from the payment_method_details field in the Charge object. The transaction_id is present only if the payment has been captured. It’s used to match payments made through Stripe with corresponding transactions in the PayPal settlement report.

For example, here’s how you can retrieve the transaction_id from the Charge object:

`{
  "amount": 1099,
  "amount_captured": 1099,
  "payment_method_details": {
    "paypal": {
      "transaction_id": "paypal_capture_id",
      "payer_id": "ZA889USQQDD37",
      "payer_email": "jenny@example.com",
      "payer_name": "Jenny Rosen"
    },
    "type": "paypal"
  },
  "balance_transaction": "txn_3MrOPxGsnWT9WMaQ19vg30v3",
  "billing_details": {
    "address": {
      "city": "Co. Kerry",
      "country": "IE",
      "line1": "Skellig Michael",
      "line2": "Great Skellig",
      "postal_code": "12345",`See all 52 linesWhen the payment is processed, paypal_capture_id is appears as Transaction ID in the PayPal settlement report.

## Access your PayPal reports

You can download your PayPal Settlement Report and other reports from paypal.com, or you can enable sFTP reporting by contacting PayPal.

The Settlement Report provides an end-to-end view of all balance-impacting transactions within a 24-hour period. This report is used to reconcile money moving events in a PayPal account with monies that are moved to a linked bank account.

To access the Settlement report:

1. [Log in](https://www.paypal.com/signin)to your PayPal business account.
2. UnderActivity, selectAll Reports.
3. SelectTransactions > Settlement.

Read more about PayPal reports and how to download them.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Use Reference](#use-reference)[Use the Charge object’s transaction ID](#use-transaction-id)[Access your PayPal reports](#access-your-paypal-reports)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`