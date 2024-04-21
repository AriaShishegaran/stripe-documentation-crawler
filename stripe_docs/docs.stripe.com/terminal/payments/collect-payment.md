# Collect payments

New to the Payment Intents API? Here are some helpful resources:

- The Payment Intents API

[The Payment Intents API](/payments/payment-intents)

- The PaymentIntent object

[The PaymentIntent object](/api/payment_intents)

- More payment scenarios

[More payment scenarios](/payments/more-payment-scenarios)

For BBPOS WisePOS E and Stripe Reader S700, we recommend this integration, which uses the Stripe API instead of a Terminal SDK to collect payments.

Collecting payments with Stripe Terminal requires writing a payment flow in your application. Use the Stripe Terminal SDK to create and update a PaymentIntent, an object representing a single payment session.

[PaymentIntent](/api#payment_intents)

While the core concepts are similar to SDK-based integrations, you follow slightly different steps with the server-driven integration:

- Create a PaymentIntent

[Create a PaymentIntent](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#create-payment)

- Process the payment

[Process the payment](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#process-payment)

- (Optional) Capture the PaymentIntent

[Capture the PaymentIntent](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#capture-payment)

In Step 1, you can define whether to automatically or manually capture your payments. Authorization on the customer’s card takes place in Step 2, when the reader processes the payment.

[Step 1](#create-payment)

[automatically](/api/payment_intents/create#create_payment_intent-capture_method)

[manually](/payments/place-a-hold-on-a-payment-method)

[Step 2](#process-payment)

[Create a PaymentIntent](#create-payment)

## Create a PaymentIntent

- Create a PaymentIntent

[Create a PaymentIntent](/api/payment_intents/create)

The first step in collecting payments is to start the payment flow. When a customer begins checking out, your backend must create a PaymentIntent object that represents a new payment session on Stripe. With the server-driven integration, you create the PaymentIntent server-side.

[PaymentIntent](/api/payment_intents)

In test mode, you can use test amounts to simulate different error scenarios. In live mode, the amount of the PaymentIntent displays on the reader for payment.

[test amounts](/terminal/references/testing#standard-test-cards)

For Terminal payments, the payment_method_types parameter must include card_present.

To accept Interac payments in Canada, you must also include interac_present in payment_method_types.  For more details, visit our Canada documentation.

[Canada documentation](/terminal/payments/regional?integration-country=CA#create-a-paymentintent)

You can control the payment flow as follows:

- To fully control the payment flow for card_present payments, set the capture_method to manual. This allows you to add a reconciliation step before finalizing the payment.

- To authorize and capture payments in one step, set the capture_method to automatic.

[Process the payment](#process-payment)

## Process the payment

If you’re using a simulated reader, use the present_payment_method endpoint to simulate a cardholder tapping or inserting their card on the reader. Use test cards to simulate different success or failure scenarios.

[present_payment_method](/terminal/references/testing#simulated-card-presentment)

[test cards](/terminal/references/testing#standard-test-cards)

You can process a payment immediately with the card presented by a customer, or instead inspect card details before proceeding to process the payment. For most use cases, we recommend processing immediately.

- Process a PaymentIntent

[Process a PaymentIntent](/api/terminal/readers/process_payment_intent)

After you create a PaymentIntent, the next step is to process the payment. The reader prompts the customer to insert or tap their card and then authorizes the payment.

To collect payment, make a request to Stripe with the ID of the PaymentIntent you created and the reader you want to use for the transaction.

Processing the payment happens asynchronously. A cardholder might take a few seconds to get their card from their wallet or pose a question to the operator during payment. When you process a payment, Stripe immediately responds to the request with an HTTP 200 and returns a reader with an action status of in_progress.

[reader](/api/terminal/readers)

Simultaneously, the reader screen switches to a UI that prompts the customer to insert their card. To verify the reader state, listen to the terminal.reader.action_succeeded webhook or poll the Reader and/or PaymentIntent status to get the status of the payment.

[verify the reader state](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#verify-reader)

[Capture the payment](#capture-payment)

## Capture the payment

If you defined capture_method as manual during PaymentIntent creation in Step 1, the SDK returns an authorized but not captured PaymentIntent to your application. Learn more about the difference between authorization and capture. When your application receives a confirmed PaymentIntent, make sure it notifies your backend to capture the PaymentIntent. To do so, create an endpoint on your backend that accepts a PaymentIntent ID and sends a request to the Stripe API to capture it.

[Step 1](#create-payment)

[authorization and capture](/payments/place-a-hold-on-a-payment-method)

A successful capture call results in a PaymentIntent with a status of succeeded.

[Verify the reader state](#verify-reader)

## Verify the reader state

To make sure the reader completed an action, your application must verify the reader state before initiating a new reader action or continuing to capture the payment. In most cases, this verification allows you to confirm a successful (approved) payment and show any relevant UX to your operator for them to complete the transaction. In other cases, you might need to handle errors, including declined payments.

[handle errors](/terminal/payments/collect-payment?terminal-sdk-platform=api#handle-errors)

Use one of the following to check the reader status:

- Listen to webhooks

[Listen to webhooks](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#webhooks)

- Poll the Stripe API

[Poll the Stripe API](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#stripe-api)

- Use the PaymentIntent

[Use the PaymentIntent](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#payment-intent)

- Use the reader object

[Use the reader object](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#reader-object)

For maximum resiliency, we recommend your application listens to webhooks from Stripe to receive real-time notifications of the reader status. Stripe sends three webhooks to notify your application of a reader’s action status:

[webhooks](/webhooks)

- terminal.reader.action_succeeded – Sent when a payment succeeds.

- terminal.reader.action_failed – Sent when a payment fails.

- terminal.reader.action_updated – Sent when a payment updates with the payment method.

To listen for these webhooks, create a webhook endpoint. We recommend having a dedicated webhook endpoint for only these events because they’re high priority and in the critical payment path.

[webhook](/webhooks)

In order to properly retrieve terminal.reader.action_updated events, webhook endpoints must have the terminal_collect_confirm_beta beta header set. Create webhooks to have the same API version and beta header as your collect_payment_method and confirm_payment_intent calls.

[https://example.com/my/webhook/endpoint](https://example.com/my/webhook/endpoint)

In case of webhook delivery issues, you can poll the Stripe API by adding a check status button to your point of sale interface that the operator can invoke, if needed.

You can retrieve the PaymentIntent that you passed to the reader for processing. When you create a PaymentIntent it has an initial status of requires_payment_method. After you successfully collect the payment method, the status updates to requires_confirmation. After the payment processes successfully, the status updates to requires_capture.

You can use the Reader object, which contains an action attribute that shows the latest action received by the reader and its status. Your application can retrieve a Reader to check if the status of the reader action has changed.

[Reader](/api/terminal/readers/object)

[action](/api/terminal/readers/object#terminal_reader_object-action)

[retrieve a Reader](/api/terminal/readers/retrieve)

[status](/api/terminal/readers/object#terminal_reader_object-action-status)

The Reader object is also returned as the response to the process payment step. The action type when processing a payment is process_payment_intent.

The action.status updates to succeeded for a successful payment. This means you can proceed with completing the transaction. Other values for action.status include failed or in_progress.

[Handle errors](#handle-errors)

## Handle errors

The following errors are the most common types your application needs to handle:

- Avoiding double charges

[Avoiding double charges](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#avoiding-double-charges)

- Payment failures

[Payment failures](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#payment-failures)

- Payment timeout

[Payment timeout](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#payment-timeout)

- Payment cancellation

[Payment cancellation](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#payment-cancellation)

- Reader busy

[Reader busy](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#reader-busy)

- Reader timeout

[Reader timeout](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#reader-timeout)

- Reader offline

[Reader offline](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#reader-offline)

- Missing webhooks

[Missing webhooks](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#missing-webhooks)

- Delayed webhooks

[Delayed webhooks](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#delayed-webhooks)

The PaymentIntent object enables money movement at Stripe—use a single PaymentIntent to represent a transaction.

Re-use the same PaymentIntent after a card is declined (for example, if it has insufficient funds), so your customer can try again with a different card.

If you edit the PaymentIntent, you must call process_payment_intent to update the payment information on the reader.

[process_payment_intent](/api/terminal/readers/process_payment_intent)

A PaymentIntent must be in the requires_payment_method state before Stripe can process it. An authorized, captured, or canceled PaymentIntent can’t be processed by a reader and results in an intent_invalid_state error:

[https://stripe.com/docs/error-codes/intent-invalid-state](https://stripe.com/docs/error-codes/intent-invalid-state)

The most common payment failure is a failed payment authorization (for example, a payment that’s declined by the customer’s bank due to insufficient funds).

When a payment authorization fails, Stripe sends the terminal.reader.action_failed webhook. Check the action.failure_code and action.failure_message attributes to know why a payment is declined:

[action.failure_code](/api/terminal/readers/object#terminal_reader_object-action-failure_code)

[action.failure_message](/api/terminal/readers/object#terminal_reader_object-action-failure_message)

In the case of a declined card, prompt the customer for an alternative form of payment. Use the same PaymentIntent in another request to the process_payment_intent endpoint. If you create a new PaymentIntent, you must cancel the failed PaymentIntent to prevent double charges.

[process_payment_intent](/api/terminal/readers/object#terminal_reader_object-action-process_payment_intent)

[cancel](/api/payment_intents/cancel)

For card read errors (for example, an error reading the chip), the reader automatically prompts the customer to retry without any notification to your application. If multiple retries fail, you can prompt for another payment method by making another process_payment_intent request.

[process_payment_intent](/api/terminal/readers/object#terminal_reader_object-action-process_payment_intent)

A reader with unreliable internet connectivity can fail to process a payment because of a networking request timeout when authorizing the card. The reader shows a processing screen for several seconds, followed by a failure screen, and you receive a terminal.reader.action_failed webhook with a failure_code of connection_error:

The payment confirmation request might have been processed by Stripe’s backend systems, but the reader might have disconnected before receiving the response from Stripe. When receiving a webhook with this failure code, fetch the PaymentIntent status to verify if the payment is successfully authorized.

You might need to cancel an in-flight payment. For example, if a customer adds items to their purchase after your integration has already initiated payment collection on the reader. Use the cancel_action endpoint to reset the reader:

[cancel_action](/api/terminal/readers/object#terminal_reader_object-action-cancel_action)

You can’t cancel a reader action in the middle of a payment authorization. If a customer has already presented their card to pay on the reader, you must wait for processing to complete. An authorization normally takes a few seconds to complete. Calling cancel_action during an authorization results in a terminal_reader_busy error.

[cancel_action](/api/terminal/readers/object#terminal_reader_object-action-cancel_action)

Users can set the value of enable_customer_cancellation on these endpoints:

- process_payment_intent

[process_payment_intent](/api/terminal/readers/process_payment_intent)

- process_setup_intent

[process_setup_intent](/api/terminal/readers/process_setup_intent)

- collect_payment_method

[collect_payment_method](/api/terminal/readers/collect_payment_method)

- refund_payment

[refund_payment](/api/terminal/readers/refund_payment)

When set to true, smart reader users see a cancel button.

Payment collection with cancellation enabled

Tapping the cancel button cancels the active transaction. Stripe sends a terminal.reader.action_failed webhook with a failure_code of customer_canceled.

A reader can only process one request at a time. If you make two API requests to the same reader in parallel, one of them fails with a terminal_reader_busy error:

[https://stripe.com/docs/error-codes/terminal-reader-timeout](https://stripe.com/docs/error-codes/terminal-reader-timeout)

[https://stripe.com/docs/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#handle-errors](https://stripe.com/docs/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#handle-errors)

A reader also rejects an API request if it’s busy performing updates or changing settings.

On rare occasions, a reader might fail to respond to an API request on time because of temporary networking issues. If this happens, you receive a terminal_reader_timeout error code:

[https://stripe.com/docs/error-codes/terminal-reader-timeout](https://stripe.com/docs/error-codes/terminal-reader-timeout)

[https://stripe.com/docs/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#handle-errors](https://stripe.com/docs/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#handle-errors)

In this case, we recommend you retry the API request.

On rare occasions, a terminal_reader_timeout error code is a false negative. In this scenario, you receive a terminal_reader_timeout error from the API as described above, but the reader has actually received the command successfully. False negatives happen when Stripe sends a message to the reader, but doesn’t receive an acknowledgement back from the reader due to temporary networking failures.

A location losing its internet connection might result in interrupted communication between the reader and Stripe. In this case, a reader is unresponsive to events initiated from your point of sale application and backend infrastructure.

A reader that consistently fails to respond to API requests is most likely powered off (for example, the power cord is disconnected or it’s out of battery) or not correctly connected to the internet.

A reader is considered offline if Stripe hasn’t received any signal from that reader in the past 2 minutes. Attempting to call API methods on a reader that’s offline results in a terminal_reader_offline error code:

[https://stripe.com/docs/error-codes/terminal-reader-offline](https://stripe.com/docs/error-codes/terminal-reader-offline)

[https://stripe.com/docs/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#handle-errors](https://stripe.com/docs/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#handle-errors)

Follow the guide to debug connectivity issues to make sure a reader is correctly connected to the internet.

[debug connectivity issues](/terminal/readers/bbpos-wisepos-e#troubleshooting)

When a reader disconnects in the middle of a payment, it can’t update its action status in the API. In this scenario, the reader shows an error screen after a card is presented. However, the Reader object in the API doesn’t update to reflect the failure on the device, and you also don’t get reader action webhooks. A reader might be left with an action status of in_progress when this happens, and a cashier has to intervene by calling the cancel_action endpoint to reset the reader state.

[cancel_action](/api/terminal/readers/object#terminal_reader_object-action-cancel_action)

On rare occasions, if Stripe is having an outage, reader action webhooks might be late. You can query the status of the Reader or the PaymentIntent objects to know what their latest state is.

[Webhook events](#webhook-events)

## Webhook events

[handle these errors](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#handle-errors)
