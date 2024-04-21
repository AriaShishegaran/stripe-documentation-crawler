# Extended authorizations

Extended authorizations allow you to capture a confirmed PaymentIntent up to 31 days later, depending on the card brand and whether your business is in an eligible category. This is helpful if you need more than 48 hours between authorization and payment capture. For example, a hotel authorizes a payment in full when a guest checks in, but captures the payment when the guest checks out.

[confirmed](/api/payment_intents/confirm)

[PaymentIntent](/api/payment_intents/object)

## Availability

Extended authorization is available on Visa, Mastercard, American Express and Discover. Extended authorizations are not supported on single-message payment methods like Interac and eftpos.

[Interac](/terminal/payments/regional?integration-country=CA#interac-payments)

[eftpos](/terminal/payments/regional?integration-country=AU#eftpos-payments)

You can contact support if you’re unsure about the eligibility of your merchant business category. If you’re a Connect user, set the merchant category code for your connected accounts to match their businesses.

[support](https://support.stripe.com/contact)

[Connect](/connect)

[set the merchant category code](/connect/setting-mcc)

## Request extended authorization support

When you create a PaymentIntent, you can request to extend the capture window of the payment. Set the request_extended_authorization field to true and the capture_method to manual.

[request_extended_authorization](/api/payment_intents/create#create_payment_intent-payment_method_options-card_present-request_extended_authorization)

[capture_method](/api/payment_intents/create#create_payment_intent-capture_method)

In the response, the capture_before field indicates the time when the authorization expires. Failure to capture the payment by this time cancels the authorization and releases the funds. When this happens, the PaymentIntent status transitions to canceled.

[capture_before](/api/charges/object#charge_object-payment_method_details-card_present-capture_before)

[PaymentIntent status](/payments/paymentintents/lifecycle)

## Authorization validity

Every card network and card brand has a different rule for how long an authorization is valid. With Terminal, an authorization for in-person payments is valid for at least two days. Because authorization rules can change without prior notice, use the capture_before field to determine the validity window for an authorization.

[capture_before](/api/charges/object#charge_object-payment_method_details-card_present-capture_before)

The capture_before field is located on the Charge, so it is only present after the PaymentIntent is confirmed.

[Charge](/api/charges/object)

* The specific extended authorization window for Visa is 29 days and 18 hours to allow time for clearing processes.** While your validity window is extended to 30 days, you must capture the authorized funds no later than the end of the duration of your customer’s stay or rental.
