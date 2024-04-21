htmlPayment Methods API | Stripe Documentation[Skip to content](#main-content)Payment Methods[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-methods)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-methods)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)
[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[About the APIs](/docs/payments-api/tour)# Payment Methods API

Learn more about the API that powers a range of global payment methods.The Payment Methods API allows you to accept a variety of payment methods through a single API. A PaymentMethod object contains the payment method details to create payments. With the Payment Methods API, you can combine a PaymentMethod:

- With a[PaymentIntent](/api/payment_intents)to accept a payment
- With a[SetupIntent](/api/setup_intents)and a[Customer](/api/customers)to save payment details for later

## Supported payment methods

To determine which payment methods to use for specific locales, see the guide to payment methods.

The guide includes available payment methods for different regions, a detailed description of each payment method’s characteristics, and the geographic regions where they are most relevant. You can enable any payment methods available to you in the Dashboard. Activation is generally instantaneous and does not require additional contracts.

## Customer actions

​​Some payment methods require your customer to take additional steps to complete the payment. The PaymentIntent object’s next_action parameter specifies the type of customer action.

Some common actions that customers need to perform are:

- ​​Redirect to their bank’s online service to authenticate and approve the payment.
- Verify ownership of their account by providing a one-time code that you post to the Stripe API (for example, microdeposits).
- Push funds (for example, in the case for bank transfers) through their bank’s online service.

Not all payment methods require additional customer actions. For example, card payments (excluding 3D Secure) require no additional authentication beyond collecting card details.

NoteFor payment methods that require customer action, listen to webhooks for notifications on whether a payment has succeeded or not.

## Immediate or delayed notification of payment success

Some payment methods immediately return payment status when a transaction is attempted (for example, card payments) but other methods have a delay such as ACH debits. For those that immediately return payment status, the PaymentIntent status either changes to succeeded or requires_payment_method. A status of succeeded guarantees that you will receive the funds from your customers.

Payment methods with delayed notification can’t guarantee payment during the delay. The status of the PaymentIntent object will be processing until the payment status is either successful or failed. It’s common for businesses to hold an order in a pending state during this time, not fulfilling the order until the payment is successful.

Note​​For payment methods with delayed notification, listen to webhooks for notifications on whether a payment has succeeded or not.

## Single-use or reusable

You can reuse certain payment methods (for example, cards or bank debits) for additional payments without authorizing and collecting payment details again.

You should always set up reusable payment methods for future use to reduce the chance of future declines and payment friction (such as authentication being required). Reusable payment methods can be set up for future use when accepting a payment or set up for future use without taking a payment.

Single-use payment methods (for example, some kinds of bank transfers) can’t be attached to customers because they’re consumed after a payment attempt.

## Use webhooks to track payment status

Use webhooks for payment methods that either require customer action or when payment notification is delayed. Stripe sends the following events when the PaymentIntent status is updated:

EventDescriptionNext steps`payment_intent.processing`The customer’s payment was submitted to Stripe successfully. Only applicable to payment methods with[delayed notification](/payments/payment-methods#payment-notification).Wait for the initiated payment to succeed or fail.`payment_intent.succeeded`The payment succeeded.Fulfill the purchased goods or services.`payment_intent.payment_failed`The payment failed.Send an email or push notification to request another payment method.​​You can also use the following options instead of building a webhook handler to listen to events:

- Manually track the status of payments in the Stripe Dashboard, if your business accepts a low volume of orders from payment methods with delayed notification. The Dashboard allows you to[view all your Stripe payments](https://dashboard.stripe.com/test/payments), send email receipts, handle payouts, or retry failed payments.
- Use polling (for example, repeatedly retrieving a PaymentIntent so that you can check its status). Note that polling is significantly less reliable and may not work at scale. Stripe enforces rate limiting on API requests, so exercise caution if you use polling.
- Use a partner application to handle common business events, like[automation](https://stripe.partners/?f_category=automation)or[marketing and sales](https://stripe.partners/?f_category=marketing-and-sales), by integrating a partner application.

## The PaymentMethod object

A PaymentMethod contains reusable payment method details for creating payments (for example, card expiration date or billing address), it doesn’t include transaction-specific information (for example, amount, currency). A PaymentMethod is attached to a PaymentIntent to represent the states of a payment lifecycle. Each PaymentMethod has a type attribute (for example, "type": "sepa_debit" ) and an additional hash whose name matches the type and contains information specific to the PaymentMethod type (for example, "sepa_debit":{}). Example of a sepa_debit PaymentMethod object:

`{
  "id": "pm_123456789",
  "object": "payment_method",
  "billing_details": {
    "address": {...},
    "email": "jenny@example.com",
    "name": "Jenny Rosen",
    "phone": "+335555555555"
  },
  "sepa_debit": {
    "bank_code": "37040044",
    "branch_code": "94832",
    "country": "FR",
    "fingerprint": "ygEJfUjzWMGyWnZg",
    "last4": "3000"
  },
  "type": "sepa_debit",
  (...)
}`NoteTo safely handle sensitive payment information and automatically handle customer actions, Stripe recommends that you create payment methods using Stripe.js.

## See also

- [Guide to Payment Methods](https://stripe.com/payments/payment-methods-guide)
- [Payment Methods API reference](/api/payment_methods)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Supported payment methods](#supported-payment-methods)[Customer actions](#customer-actions)[Immediate or delayed notification of payment success](#payment-notification)[Single-use or reusable](#usage)[Use webhooks to track payment status](#webhooks)[The PaymentMethod object](#payment-method-object)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`