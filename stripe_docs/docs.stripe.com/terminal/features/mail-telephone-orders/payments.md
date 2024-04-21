# Process MOTO paymentsBeta

As when collecting payments with the server-driven integration, the first step is to create a PaymentIntent.

[collecting payments](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven&reader=wpe)

- Create a PaymentIntent

[Create a PaymentIntent](#create-payment-intent)

- Process the payment

[Process the payment](#process-payment)

- Verify the reader state

[Verify the reader state](#verify-reader-state)

- Capture the payment

[Capture the payment](#capture-payment)

If you’re displaying cart details using the setReaderDisplay method, you must reset the reader’s display from a line item interface to the splash screen before collecting a MOTO payment.

[setReaderDisplay](/terminal/features/display)

MOTO payment collection flow

[Create a PaymentIntent](#create-payment-intent)

## Create a PaymentIntent

To begin collecting a MOTO payment, you must create a PaymentIntent with payment_method_types that includes card.

[PaymentIntent](/payments/payment-intents)

[payment_method_types](/api/payment_intents/create#create_payment_intent-payment_method_types)

[Process the payment](#process-payment)

## Process the payment

After you create a PaymentIntent, use process_payment_intent to process the payment, setting process_config[moto] to true.

[process_payment_intent](/api/terminal/readers/process_payment_intent)

[process_config[moto]](/api/terminal/readers/process_payment_intent#process_payment_intent-process_config)

The process_payment_intent request is asynchronous. After the request, the reader prompts you to enter the cardholder’s card number, CVC, expiration date, and postal code. You can then confirm the cardholder’s details to submit the payment for authorization.

[process_payment_intent](/api/terminal/readers/process_payment_intent)

[Verify the reader state](#verify-reader-state)

## Verify the reader state

Your application must follow the instructions for verifying the reader state to confirm a successful (approved) payment.

[verifying the reader state](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven&reader=wpe#verify-reader)

[Capture the Payment](#capture-payment)

## Capture the Payment

You must call capture to complete the payment if the PaymentIntent has a status of requires_capture.

[capture](/terminal/payments/collect-payment?terminal-sdk-platform=server-driven#capture-payment)
