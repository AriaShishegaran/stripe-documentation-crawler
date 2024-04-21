# Payment Methods API

The Payment Methods API allows you to accept a variety of payment methods through a single API. A PaymentMethod object contains the payment method details to create payments. With the Payment Methods API, you can combine a PaymentMethod:

[PaymentMethod](/api/payment_methods/object)

[PaymentMethod](/api/payment_methods)

- With a PaymentIntent to accept a payment

[PaymentIntent](/api/payment_intents)

- With a SetupIntent and a Customer to save payment details for later

[SetupIntent](/api/setup_intents)

[Customer](/api/customers)

## Supported payment methods

To determine which payment methods to use for specific locales, see the guide to payment methods.

[guide to payment methods](https://stripe.com/payments/payment-methods-guide)

The guide includes available payment methods for different regions, a detailed description of each payment method’s characteristics, and the geographic regions where they are most relevant. You can enable any payment methods available to you in the Dashboard. Activation is generally instantaneous and does not require additional contracts.

[geographic regions](https://stripe.com/payments/payment-methods-guide#payment-methods-fact-sheets)

[Dashboard](https://dashboard.stripe.com/)

## Customer actions

​​Some payment methods require your customer to take additional steps to complete the payment. The PaymentIntent object’s next_action parameter specifies the type of customer action.

Some common actions that customers need to perform are:

- ​​Redirect to their bank’s online service to authenticate and approve the payment.

- Verify ownership of their account by providing a one-time code that you post to the Stripe API (for example, microdeposits).

- Push funds (for example, in the case for bank transfers) through their bank’s online service.

Not all payment methods require additional customer actions. For example, card payments (excluding 3D Secure) require no additional authentication beyond collecting card details.

For payment methods that require customer action, listen to webhooks for notifications on whether a payment has succeeded or not.

[webhooks](#webhooks)

## Immediate or delayed notification of payment success

Some payment methods immediately return payment status when a transaction is attempted (for example, card payments) but other methods have a delay such as ACH debits. For those that immediately return payment status, the PaymentIntent status either changes to succeeded or requires_payment_method. A status of succeeded guarantees that you will receive the funds from your customers.

Payment methods with delayed notification can’t guarantee payment during the delay. The status of the PaymentIntent object will be processing until the payment status is either successful or failed. It’s common for businesses to hold an order in a pending state during this time, not fulfilling the order until the payment is successful.

​​For payment methods with delayed notification, listen to webhooks for notifications on whether a payment has succeeded or not.

[webhooks](#webhooks)

## Single-use or reusable

You can reuse certain payment methods (for example, cards or bank debits) for additional payments without authorizing and collecting payment details again.

You should always set up reusable payment methods for future use to reduce the chance of future declines and payment friction (such as authentication being required). Reusable payment methods can be set up for future use when accepting a payment or set up for future use without taking a payment.

[authentication being required](/strong-customer-authentication)

[set up for future use when accepting a payment](/payments/save-during-payment)

[set up for future use without taking a payment](/payments/save-and-reuse)

Single-use payment methods (for example, some kinds of bank transfers) can’t be attached to customers because they’re consumed after a payment attempt.

## Use webhooks to track payment status

Use webhooks for payment methods that either require customer action or when payment notification is delayed. Stripe sends the following events when the PaymentIntent status is updated:

[webhooks](/webhooks)

[delayed notification](/payments/payment-methods#payment-notification)

​​You can also use the following options instead of building a webhook handler to listen to events:

- Manually track the status of payments in the Stripe Dashboard, if your business accepts a low volume of orders from payment methods with delayed notification. The Dashboard allows you to view all your Stripe payments, send email receipts, handle payouts, or retry failed payments.

[view all your Stripe payments](https://dashboard.stripe.com/test/payments)

- Use polling (for example, repeatedly retrieving a PaymentIntent so that you can check its status). Note that polling is significantly less reliable and may not work at scale. Stripe enforces rate limiting on API requests, so exercise caution if you use polling.

- Use a partner application to handle common business events, like automation or marketing and sales, by integrating a partner application.

[automation](https://stripe.partners/?f_category=automation)

[marketing and sales](https://stripe.partners/?f_category=marketing-and-sales)

## The PaymentMethod object

A PaymentMethod contains reusable payment method details for creating payments (for example, card expiration date or billing address), it doesn’t include transaction-specific information (for example, amount, currency). A PaymentMethod is attached to a PaymentIntent to represent the states of a payment lifecycle. Each PaymentMethod has a type attribute (for example, "type": "sepa_debit" ) and an additional hash whose name matches the type and contains information specific to the PaymentMethod type (for example, "sepa_debit":{}). Example of a sepa_debit PaymentMethod object:

[states of a payment lifecycle](/payments/paymentintents/lifecycle)

[type attribute](/api/payment_methods/object#payment_method_object-type)

To safely handle sensitive payment information and automatically handle customer actions, Stripe recommends that you create payment methods using Stripe.js.

[Stripe.js](/js#stripe-create-payment-method)

## See also

- Guide to Payment Methods

[Guide to Payment Methods](https://stripe.com/payments/payment-methods-guide)

- Payment Methods API reference

[Payment Methods API reference](/api/payment_methods)
