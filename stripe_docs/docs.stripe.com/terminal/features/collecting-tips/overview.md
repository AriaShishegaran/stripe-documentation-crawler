# Collect tips

Use Terminal to collect tips from your customer before or after authorizing a payment. You can collect voluntary tips in two ways:

- On-receipt tipping: Tips are collected when the payment is captured. This method is most commonly used when collecting tips on printed paper receipts.

[On-receipt tipping](/terminal/features/collecting-tips/on-receipt)

- On-reader tipping: The card reader suggests tips to customers before collecting payment.

[On-reader tipping](/terminal/features/collecting-tips/on-reader)

For mandatory tips, you must include the tip amount in the original PaymentIntent amount. You can’t use on-receipt or on-reader tipping.

[amount](/api/payment_intents/object#payment_intent_object-amount)

## On-receipt versus on-reader tipping

The table below outlines some differences between on-receipt tipping and on-reader tipping.

Country

BBPOS WisePad 3: Beta

Stripe Reader S700 Beta and BBPOS WisePOS E:

Reader

BBPOS WisePad 3

[BBPOS WisePad 3](/terminal/payments/setup-reader/bbpos-wisepad3)

BBPOS WisePOS E

[BBPOS WisePOS E](/terminal/payments/setup-reader/bbpos-wisepos-e)

Stripe Reader S700

[Stripe Reader S700](/terminal/readers/stripe-reader-s700)

Any

Integrations/SDKs

BBPOS WisePad 3:

- Android SDK

- iOS SDK

- React Native SDK

BBPOS WisePOS E and Stripe Reader S700:

- All SDKs (JS, iOS, Android, React Native), server-driven

All SDKs (JS, iOS, Android, React Native), server-driven

[Maximum charge amount](/currencies#minimum-and-maximum-charge-amounts)

[Maximum charge amount](/currencies#minimum-and-maximum-charge-amounts)

## How tips are displayed on-receipt or on-reader

On-receipt and on-reader tipping use the PaymentIntents API, work with all Terminal SDKs (JavaScript, iOS, Android, React Native) and server-driven integrations, and require manual capture.

[PaymentIntents](/api/payment_intents)

[JavaScript](/terminal/payments/setup-integration?terminal-sdk-platform=js)

[iOS](/terminal/payments/setup-integration?terminal-sdk-platform=ios)

[Android](/terminal/payments/setup-integration?terminal-sdk-platform=android)

[React Native](/terminal/payments/setup-integration?terminal-sdk-platform=react-native)

[server-driven integrations](/terminal/payments/setup-integration?terminal-sdk-platform=server-driven)

[manual capture](/payments/place-a-hold-on-a-payment-method)

Choose only one tipping method per PaymentIntent. If you use on-reader tipping, you can’t use the same PaymentIntent for on-receipt tipping.

The table below summarizes the specific API behavior.

[amount_to_capture](/api/payment_intents/capture#capture_payment_intent-amount_to_capture)

[capturing a PaymentIntent](/api/payment_intents/capture)

[amount_details](/api/payment_intents/object#payment_intent_object-amount_details)

[Charge](/api/charges/object)

Tips in the underlying Charge object

Tips aren’t directly represented in the Charge object.

After capture, the fields below all show the same value inclusive of the tip.

- amount

[amount](/api/payment_intents/create#create_payment_intent-amount)

- amount_authorized

[amount_authorized](/api/charges/object#charge_object-payment_method_details-card_present-amount_authorized)

- amount_captured

[amount_captured](/api/charges/object#charge_object-amount_captured)

Tips can be derived from the Charge object. You can derive the tip by subtracting amount_authorized from amount.

- amount_authorized is the original authorized amount exclusive of the tip.

- amount_captured and amount are the same and both are inclusive of the tip.
