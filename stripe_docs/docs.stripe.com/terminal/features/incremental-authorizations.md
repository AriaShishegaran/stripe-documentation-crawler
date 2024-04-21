# Incremental authorizations

Incremental authorizations allow you to increase the authorized amount on a confirmed PaymentIntent before you capture it. This is helpful if the total price changes or the customer adds goods or services and you need to update the amount on the payment.

[amount](/api/payment_intents/object#payment_intent_object-amount)

[PaymentIntent](/payments/payment-intents)

Depending on the issuing bank, cardholders might see the amount of the original pending authorization increase in place, or they might see each increment as an additional pending authorization. After capture, the total captured amount appears as one entry.

## Availability

When using incremental authorizations, be aware of the following restrictions:

- They’re only available with Visa, Mastercard, or Discover.

- Certain card brands have merchant category restrictions (see below).

- You can only increment a transaction made with the POS and reader fully online.

- You have a maximum of 10 attempts per payment.

Use incremental authorizations on payments that fulfill the criteria below. You can find your user category in the Dashboard.

[Dashboard](https://dashboard.stripe.com/settings/update/company/update)

Attempting to perform an incremental authorization on a payment that doesn’t fulfill the below criteria results in an error.

* Excludes MX users and JPY transactions for JP users

[Request incremental authorization supportServer-sideClient-side](#request-incremental-authorization-support)

## Request incremental authorization supportServer-sideClient-side

When you create a PaymentIntent, you can request the ability to capture increments of the payment. Set the request_incremental_authorization_support field to true and the capture_method to manual.

[request_incremental_authorization_support](/api/payment_intents/create#create_payment_intent-payment_method_options-card_present-request_incremental_authorization_support)

[capture_method](/api/payment_intents/create#create_payment_intent-capture_method)

[Confirm the PaymentIntentClient-side](#confirm-payment-intent)

## Confirm the PaymentIntentClient-side

Check the incremental_authorization_supported field in the confirm response to determine if the PaymentIntent is eligible for incremental authorization.

[incremental_authorization_supported](/api/charges/object#charge_object-payment_method_details-card_present-incremental_authorization_supported)

You can only perform incremental authorizations on uncaptured payments after confirmation. To adjust the amount of a payment before confirmation, use the update method instead.

[update](/api/payment_intents/update)

[Perform an incremental authorizationServer-side](#increment-authorization)

## Perform an incremental authorizationServer-side

To increase the authorized amount on a payment, use the increment_authorization endpoint and provide the updated total amount to increment to, which must be greater than the original authorized amount. This attempts to authorize for the difference between the previous amount and the incremented amount. Each PaymentIntent can have a maximum of 10 incremental authorization attempts, including declines.

[increment_authorization](/api/payment_intents/increment_authorization)

[amount](/api/payment_intents/increment_authorization#increment_authorization-amount)

A single PaymentIntent can call this endpoint multiple times to further increase the authorized amount.

An authorization can either:

- Succeed – Returns the PaymentIntent with the updated amount.

- Fail – Returns a card_declined error, and the PaymentIntent remains authorized to capture the original amount. Updates to other PaymentIntent fields (for example, application_fee_amount) aren’t saved.

[card_declined](/error-codes#card-declined)

[application_fee_amount](/api/payment_intents/increment_authorization#increment_authorization-application_fee_amount)

[Capture the PaymentIntentServer-side](#capture-payment-intent)

## Capture the PaymentIntentServer-side

To capture the authorized amount on a PaymentIntent that has prior incremental authorizations, use the capture endpoint. To increase the authorized amount and simultaneously capture that updated amount, provide an updated amount_to_capture.

[capture](/api/payment_intents/capture)

[amount_to_capture](/api/payment_intents/capture#capture_payment_intent-amount_to_capture)

Providing an amount_to_capture that’s higher than the currently authorized amount results in an automatic incremental authorization attempt.

If you’re eligible to collect on-receipt tips, using an amount_to_capture that’s higher than the currently authorized amount won’t result in an automatic incremental authorization attempt. Capture requests always succeed.

[collect on-receipt tips](/terminal/features/collecting-tips/on-receipt)

The possible outcomes of an incremental authorization attempt are:

- Succeed – Returns the captured PaymentIntent with the updated amount.

- Fail – Returns a card_declined error, and the PaymentIntent remains authorized to capture the original amount. Updates to other PaymentIntent fields (for example, application_fee_amount) aren’t saved.

[card_declined](/error-codes#card-declined)

[application_fee_amount](/api/payment_intents/capture#capture_payment_intent-application_fee_amount)

Regardless, when using amount_to_capture we recommend that you always check for potential failures.
