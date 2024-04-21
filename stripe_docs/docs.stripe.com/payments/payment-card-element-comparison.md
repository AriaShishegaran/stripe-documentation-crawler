# Payment Element and Card Element comparison

Previously, each payment method (cards, iDEAL, etc.) required integrating a separate Element. Now, you can use the Payment Element to accept payments from one or multiple payment methods. Since this also includes cards, you have the option to integrate the Card Element or the Payment Element to accept card payments.

For most users, the Payment Element is the best option to process cards. The integration effort is the same as the Card Element and it supports all the common payment flows. It also gives you instant access to additional payment methods, including Google Pay and Apple Pay. Accepting more payment methods can help your business expand its global reach and improve checkout conversion.

[payment methods](/payments/payment-methods/overview)

If you’re already using the Card Element and want to migrate to the Payment Element, follow our migration guide.

[Card Element](/js/element/other_element?type=card)

[Payment Element](/js/element/payment_element)

[migration guide](/payments/payment-element/migration)

You can have a single line Card Element or use split Elements, such as Card Number, Expiry, and CVC. When referring to the Card Element, the information below applies to both styles.

[Card Element](/js/element/other_element?type=card)

[Card Number](/js/element/other_element?type=cardNumber)

[Expiry](/js/element/other_element?type=cardExpiry)

[CVC](/js/element/other_element?type=cardCvc)

[Link](/payments/link)

[Stripe supported card brands](/payments/cards#supported-card-brands)

[3D Secure authentication](/payments/3d-secure)

* Using split input fields is more accessible than using a single line input

## Advanced scenarios

[Set up future payments](/payments/save-and-reuse)

[Save payment details during payment](/payments/save-during-payment)

[Place a hold on a payment method](/payments/place-a-hold-on-a-payment-method)

[Credit card installments](/payments/mx-installments)

[application fee amount](/api/payment_intents/object#payment_intent_object-application_fee_amount)

[Brand choice for cobranded cards](/co-badged-cards-compliance)

If you want to use the Card Element, see our guide on accepting a payment.

[accepting a payment](/payments/card-element)
