# Migrate to latest flexible payment scenarios

Stripe now supports several flexible payment scenarios for non-card-present transactions. If you’ve already integrated the private beta version of any of these features, this guide provides details to upgrade to the general release. For new integrations, use see the following guides for the features that interest you:

- Increment an Authorization

[Increment an Authorization](/payments/incremental-authorization)

- Capture more than the Authorized Amount

[Capture more than the Authorized Amount](/payments/overcapture)

- Place an Extended Hold on an Online Card Payment

[Place an Extended Hold on an Online Card Payment](/payments/extended-authorization)

- Capture a Payment Multiple Times

[Capture a Payment Multiple Times](/payments/multicapture)

We’ve incorporated the following feedback-driven improvements to these features:

- Detailed control over the features at the PaymentIntent level.

[PaymentIntent](/payments/payment-intents)

- Clearer expectations regarding feature availability and usage after a confirmation phase.

[confirmation](/api/payment_intents/confirm)

Each of the flexible payment features has different requirements from its private beta integration. Choose the feature you need to upgrade and refer to the note at the top for changes and requirements specific to that feature.

The first step of this integration is now mandatory.

[Request incremental authorization](#request-incremental-auth)

## Request incremental authorization

Your PaymentIntent must include a request for incremental authorization before confirmation.

[PaymentIntent](/payments/payment-intents)

This formerly optional step is now mandatory.

The response now returns the status of the incremental authorization request in the payment_method_details.card.incremental_authorization.status property of the latest_charge. The status values is available or unavailable depending on the customer’s payment method.

[latest_charge](/api/charges/object)

[Incrementally modify the authorized amount](#use-incremental-auth)

## Incrementally modify the authorized amount

No changes have been made to this step in comparison to the beta version.

## Choose how to capture more than initially authorized amount

Two of the flexible payment features allow you to capture an amount larger than initially authorized:

- Over capture up to a certain limit (Capture more than the authorized amount on a payment)

[Capture more than the authorized amount on a payment](/payments/overcapture)

- Increment the existing authorization and then capture the newly authorized amount (Increment an authorization)

[Increment an authorization](/payments/incremental-authorization)

The example below showcases how these features can complement each other in the generally available version.

Upon confirmation of the PaymentIntent, if both features are available, you have options on the next steps to capture a larger amount than initially authorized:

[confirmation](/api/payment_intents/confirm)

- Overcapture if the desired amount is equal or below the maximum_capturable_amount.

- Perform an incremental authorization to the desired amount, then capture.
