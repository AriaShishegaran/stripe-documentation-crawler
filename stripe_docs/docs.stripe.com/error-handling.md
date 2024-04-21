# Error handling

Stripe offers many kinds of errors. They can reflect external events, like declined payments and network interruptions, or code problems, like invalid API calls.

To handle errors, use some or all of the techniques in the table below. No matter what technique you use, you can follow up with our recommended responses for each error type.

[recommended responses for each error type](#error-types)

[Catch exceptions](#catch-exceptions)

[Monitor webhooks](#monitor-webhooks)

[Get stored information about failures](#use-stored-information)

## Catch exceptions

With this library, you don’t need to check for non-200 HTTP responses. The library translates them as exceptions.

In the rare event you need HTTP details, see Low-level exception handling and the Error object.

[Low-level exception handling](/error-low-level)

[Error](/api/errors)

If an immediate problem prevents an API call from continuing, the Stripe Ruby library raises an exception. It’s a best practice to catch and handle exceptions.

To catch an exception, use Ruby’s rescue keyword. Catch Stripe::StripeError or its subclasses to handle Stripe-specific exceptions only. Each subclass represents a different kind of exception. When you catch an exception, you can use its class to choose a response.

[use its class to choose a response](#error-types)

After setting up exception handling, test it on a variety of data, including test cards, to simulate different payment outcomes.

[test cards](/testing)

## Monitor webhooks

Stripe notifies you about many kinds of problems using webhooks. This includes problems that don’t follow immediately after an API call. For example:

[webhooks](/webhooks)

- You lose a dispute.

- A recurring payment fails after months of success.

- Your frontend confirms a payment, but goes offline before finding out the payment fails. (The backend still receives webhook notification, even though it wasn’t the one to make the API call.)

[confirms](/api/payment_intents/confirm)

You don’t need to handle every webhook event type. In fact, some integrations don’t handle any.

In your webhook handler, start with the basic steps from the webhook builder: get an event object and use the event type to find out what happened. Then, if the event type indicates an error, follow these extra steps:

[webhook builder](/webhooks/quickstart)

- Access event.data.object to retrieve the affected object.

[event.data.object](/api/events/object#event_object-data-object)

- Use stored information on the affected object to gain context, including an error object.

[Use stored information](#use-stored-information)

- Use its type to choose a response.

[Use its type to choose a response](#error-types)

To test how your integration responds to webhook events, you can trigger webhook events locally. After completing the setup steps at that link, trigger a failed payment to see the resulting error message.

[trigger webhook events locally](/webhooks#test-webhook)

## Get stored information about failures

Many objects store information about failures. That means that if something already went wrong, you can retrieve the object and examine it to learn more. In many cases, stored information is in the form of an error object, and you can use its type to choose a response.

[use its type to choose a response](#error-types)

For instance:

- Retrieve a specific payment intent.

- Check if it experienced a payment error by determining if last_payment_error is empty.

[last_payment_error](/api/payment_intents/object#payment_intent_object-last_payment_error)

- If it did, log the error, including its type and the affected object.

Here are common objects that store information about failures.

[Payment Intent](/api/payment_intents)

[An error object](#work-with-error-objects)

[Setup Intent](/api/setup_intents)

[An error object](#work-with-error-objects)

[Invoice](/api/invoices)

[An error object](#work-with-error-objects)

[Setup Attempt](/api/setup_attempts)

[An error object](#work-with-error-objects)

[Payout](/api/payouts)

[A payout failure code](/api/payouts/failures)

[Refund](/api/refunds)

[A refund failure code](/api/refunds/object#refund_object-failure_reason)

To test code that uses stored information about failures, you often need to simulate failed transactions. You can often do this using test cards or test bank numbers. For example:

[test cards](/testing)

- Simulate a declined payment, for creating failed Charges, PaymentIntents, SetupIntents, and so on.

[Simulate a declined payment](/testing#declined-payments)

- Simulate a failed payout.

[Simulate a failed payout](/connect/testing#account-numbers)

- Simulate a failed refund.

[Simulate a failed refund](/testing#refunds)

## Types of error and responses

In the Stripe Ruby library, error objects belong to stripe.error.StripeError and its subclasses. Use the documentation for each class for advice on responding.

Class

Stripe::CardError

[Stripe::CardError](#payment-errors)

- Payment blocked for suspected fraud

[Payment blocked for suspected fraud](#payment-blocked)

- Payment declined by the issuer.

[Payment declined by the issuer](#payment-declined)

- Other payment errors.

[Other payment errors](#other-payment-errors)

Stripe::InvalidRequestError

[Stripe::InvalidRequestError](#invalid-request-errors)

You made an API call with the wrong parameters, in the wrong state, or in an invalid way.

Stripe::APIConnectionError

[Stripe::APIConnectionError](#connection-errors)

Stripe::APIError

[Stripe::APIError](#api-errors)

Stripe::AuthenticationError

[Stripe::AuthenticationError](#authentication-errors)

Stripe::IdempotencyError

[Stripe::IdempotencyError](#idempotency-errors)

[idempotency key](/api/idempotent_requests)

Stripe::PermissionError

[Stripe::PermissionError](#permission-errors)

Stripe::RateLimitError

[Stripe::RateLimitError](#rate-limit-errors)

Stripe::SignatureVerificationError

[Stripe::SignatureVerificationError](#signature-verification-errors)

[webhook](/webhooks)

[signature verification](/webhooks#verify-events)

## Payment errors

Everything in this section also applies to non-card payments. For historical reasons, payment errors have the type Stripe::CardError. But in fact, they can represent a problem with any payment, regardless of the payment method.

[Stripe::CardError](#card-error)

Payment errors—sometimes called “card errors” for historical reasons—cover a wide range of common problems. They come in three categories:

- Payment blocked for suspected fraud

[Payment blocked for suspected fraud](#payment-blocked)

- Payment declined by the issuer

[Payment declined by the issuer](#payment-declined)

- Other payment errors

[Other payment errors](#other-payment-errors)

To distinguish these categories or get more information about how to respond, consult the error code, decline code, and charge outcome.

[error code](/error-codes)

[decline code](/declines/codes)

[charge outcome](/api/charges/object#charge_object-outcome)

(To find the charge outcome from an error object, first get the Payment Intent that’s involved and the latest Charge it created. See the example below for a demonstration.)

[Payment Intent that’s involved](/api/errors#errors-payment_intent)

[latest Charge it created](/api/payment_intents/object#payment_intent_object-latest_charge)

Users on API version 2022-08-01 or older:

[2022-08-01](/upgrades#2022-08-01)

(To find the charge outcome from an error object, first get the Payment Intent that’s involved and the latest Charge it created. See the example below for a demonstration.)

[Payment Intent that’s involved](/api/errors#errors-payment_intent)

[latest Charge it created](/api/payment_intents/object#payment_intent_object-charges-data)

You can trigger some common kinds of payment error with test cards. Consult these lists for options:

- Simulating payments blocked for fraud risk

[Simulating payments blocked for fraud risk](/testing#fraud-prevention)

- Simulating declined payments and other card errors

[Simulating declined payments and other card errors](/testing#declined-payments)

The test code below demonstrates a few possibilities.

Stripe::CardError

e.error.payment_intent.charges.data[0].outcome.type == 'blocked'

[Radar](/radar)

Solutions

This error can occur when your integration is working correctly. Catch it and prompt the customer for a different payment method.

To block fewer legitimate payments, try these:

- Optimize your Radar integration to collect more detailed information.

[Optimize your Radar integration](/radar/integration)

- Use Payment Links, Checkout, or Stripe Elements for prebuilt optimized form elements.

[Payment Links](/payment-links)

[Checkout](/payments/checkout)

[Stripe Elements](/payments/elements)

Radar for Fraud Teams customers have these additional options:

[Radar for Fraud Teams](/radar)

- To exempt a specific payment, add it to your allowlist. Radar for Fraud Teams

- To change your risk tolerance, adjust your risk settings. Radar for Fraud Teams

[risk settings](/radar/risk-settings)

- To change the criteria for blocking a payment, use custom rules. Radar for Fraud Teams

[custom rules](/radar/rules)

You can test your integration’s settings with test cards that simulate fraud. If you have custom Radar rules, follow the testing advice in the Radar documentation.

[test cards that simulate fraud](/radar/testing)

[Radar documentation](/radar/testing)

Stripe::CardError

e.error.code == "card_declined"

Solutions

This error can occur when your integration is working correctly. It reflects an action by the issuer, and that action may be legitimate. Use the decline code to determine what next steps are appropriate. See the documentation on decline codes for appropriate responses to each code.

[documentation on decline codes](/declines/codes)

You can also:

- Follow recommendations to reduce issuer declines.

[Follow recommendations to reduce issuer declines](/declines/card#reducing-bank-declines)

- Use Payment Links, Checkout, or Stripe Elements for prebuilt form elements that implement those recommendations.

[Payment Links](/payment-links)

[Checkout](/payments/checkout)

[Stripe Elements](/payments/elements)

Test how your integration handles declines with test cards that simulate successful and declined payments.

[test cards that simulate successful and declined payments](/radar/testing)

Stripe::CardError

[documentation on error codes](/error-codes)

## Invalid request errors

Stripe::InvalidRequestError

- Consult the error code documentation for details on the problem.

[error code documentation](/error-codes)

- For convenience, you can follow the link at  for documentation about the error code.

- If the error involves a specific parameter, use  to determine which one.

## Connection errors

Stripe::APIConnectionError

Solutions

Treat the result of the API call as indeterminate. That is, don’t assume that it succeeded or that if failed.

To find out if it succeeded, you can:

- Retrieve the relevant object from Stripe and check its status.

- Listen for webhook notification that the operation succeeded or failed.

To make it easier to recover from connection errors, you can:

- When creating or updating an object, use an idempotency key. Then, if a connection error occurs, you can safely repeat the request without risk of creating a second object or performing the update twice. Repeat the request with the same idempotency key until you receive a clear success or failure. For advanced advice on this strategy, see Low-level error handling.

[idempotency key](/api/idempotent_requests)

[Low-level error handling](/error-low-level#idempotency)

- Turn on automatic retries. Then, Stripe generates idempotency keys for you, and repeats requests for you when it is safe to do so.

[automatic retries.](#automatic-retries)

This error can mask others. It’s possible that when the connection error resolves, some other error becomes apparent. Check for errors in all of these solutions just as you would in the original request.

## API errors

Stripe::APIError

Solutions

Treat the result of the API call as indeterminate. That is, don’t assume that it succeeded or that it failed.

Rely on webhooks for information about the outcome. Whenever possible, Stripe fires webhooks for any new objects we create as we solve a problem.

[webhooks](/webhooks)

To set your integration up for maximum robustness in unusual situations, see this advanced discussion of server errors.

[this advanced discussion of server errors.](/error-low-level#server-errors)

## Authentication errors

Stripe::AuthenticationError

- Use the correct API key.

[API key](/keys)

- Make sure you aren’t using a key that you “rolled” or revoked.

[“rolled” or revoked](/keys#rolling-keys)

## Idempotency errors

Stripe::IdempotencyError

[idempotency key](/api/idempotent_requests)

- After you use an idempotency key, only reuse it for identical API calls.

- Use idempotency keys under the limit of 255 characters.

## Permission errors

Stripe::PermissionError

- Are you using a restricted API key for a service it doesn’t have access to?

[restricted API key](/keys#limit-access)

- Are you performing an action in the Dashboard while logged in as a user role that lacks permission?

[user role](/get-started/account/teams/roles)

## Rate limit errors

Stripe::RateLimitError

- If a single API call triggers this error, wait and try it again.

- To handle rate-limiting automatically, retry the API call after a delay, and increase the delay exponentially if the error continues. See the documentation on rate limits for further advice.

[rate limits](/rate-limits)

- If you anticipate a large increase in traffic and want to request an increased rate limit, contact support in advance.

[contact support](https://support.stripe.com/)

## Signature verification errors

Stripe::SignatureVerificationError

[webhook](/webhooks)

[signature verification](/webhooks#verify-events)

Solutions

This error can occur when your integration is working correctly. If you use webhook signature verification and a third party attempts to send you a fake or malicious webhook, then verification fails and this error is the result. Catch it and respond with a 400 Bad Request status code.

If you receive this error when you shouldn’t—for instance, with webhooks that you know originate with Stripe—then see the documentation on checking webhook signatures for further advice. In particular, make sure you’re using the correct endpoint secret. This is different from your API key.

[checking webhook signatures](/webhooks#verify-events)
