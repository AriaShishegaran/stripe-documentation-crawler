- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Cancel a PaymentIntent

[Cancel a PaymentIntent](/api/payment_intents/cancel)

You can cancel a PaymentIntent object when it’s in one of these statuses: requires_payment_method, requires_capture, requires_confirmation, requires_action or, in rare cases, processing.

[in rare cases](/payments/intents)

After it’s canceled, no additional charges are made by the PaymentIntent and any operations on the PaymentIntent fail with an error. For PaymentIntents with a status of requires_capture, the remaining amount_capturable is automatically refunded.

You can’t cancel the PaymentIntent for a Checkout Session. Expire the Checkout Session instead.

[Expire the Checkout Session](/api/checkout/sessions/expire)

- cancellation_reasonstringReason for canceling this PaymentIntent. Possible values are: duplicate, fraudulent, requested_by_customer, or abandoned

Reason for canceling this PaymentIntent. Possible values are: duplicate, fraudulent, requested_by_customer, or abandoned

Returns a PaymentIntent object if the cancellation succeeds. Returns an error if the PaymentIntent is already canceled or isn’t in a cancelable state.

# Capture a PaymentIntent

[Capture a PaymentIntent](/api/payment_intents/capture)

Capture the funds of an existing uncaptured PaymentIntent when its status is requires_capture.

Uncaptured PaymentIntents are cancelled a set number of days (7 by default) after their creation.

Learn more about separate authorization and capture.

[separate authorization and capture](/payments/capture-later)

- amount_to_captureintegerThe amount to capture from the PaymentIntent, which must be less than or equal to the original amount. Any additional amount is automatically refunded. Defaults to the full amount_capturable if it’s not provided.

The amount to capture from the PaymentIntent, which must be less than or equal to the original amount. Any additional amount is automatically refunded. Defaults to the full amount_capturable if it’s not provided.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- application_fee_amountintegerConnect only

- final_captureboolean

- statement_descriptorstring

- statement_descriptor_suffixstring

- transfer_dataobjectConnect only

Returns a PaymentIntent object with status="succeeded" if the PaymentIntent is capturable. Returns an error if the PaymentIntent isn’t capturable or if an invalid amount to capture is provided.

# Confirm a PaymentIntent

[Confirm a PaymentIntent](/api/payment_intents/confirm)

Confirm that your customer intends to pay with current or provided payment method. Upon confirmation, the PaymentIntent will attempt to initiate a payment. If the selected payment method requires additional authentication steps, the PaymentIntent will transition to the requires_action status and suggest additional actions via next_action. If payment fails, the PaymentIntent transitions to the requires_payment_method status or the canceled status if the confirmation limit is reached.  If payment succeeds, the PaymentIntent will transition to the succeeded status (or requires_capture, if capture_method is set to manual). If the confirmation_method is automatic, payment may be attempted using our client SDKs and the PaymentIntent’s client_secret. After next_actions are handled by the client, no additional confirmation is required to complete the payment. If the confirmation_method is manual, all payment attempts must be initiated using a secret key. If any actions are required for the payment, the PaymentIntent will return to the requires_confirmation state after those actions are completed. Your server needs to then explicitly re-confirm the PaymentIntent to initiate the next payment attempt.

[client SDKs](/stripe-js/reference#stripe-handle-card-payment)

[client_secret](#payment_intent_object-client_secret)

- payment_methodstringID of the payment method (a PaymentMethod, Card, or compatible Source object) to attach to this PaymentIntent.

ID of the payment method (a PaymentMethod, Card, or compatible Source object) to attach to this PaymentIntent.

[compatible Source](/payments/payment-methods/transitioning#compatibility)

- receipt_emailstringEmail address that the receipt for the resulting payment will be sent to. If receipt_email is specified for a payment in live mode, a receipt will be sent regardless of your email settings.

Email address that the receipt for the resulting payment will be sent to. If receipt_email is specified for a payment in live mode, a receipt will be sent regardless of your email settings.

[email settings](https://dashboard.stripe.com/account/emails)

- setup_future_usageenumIndicates that you intend to make future payments with this PaymentIntent’s payment method.Providing this parameter will attach the payment method to the PaymentIntent’s Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be attached to a Customer after the transaction completes.When processing card payments, Stripe also uses setup_future_usage to dynamically optimize your payment flow and comply with regional legislation and network rules, such as SCA.If setup_future_usage is already set and you are performing a request using a publishable key, you may only update the value from on_session to off_session.Possible enum valuesoff_sessionUse off_session if your customer may or may not be present in your checkout flow.on_sessionUse on_session if you intend to only reuse the payment method when your customer is present in your checkout flow.

Indicates that you intend to make future payments with this PaymentIntent’s payment method.

Providing this parameter will attach the payment method to the PaymentIntent’s Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be attached to a Customer after the transaction completes.

[attach the payment method](/payments/save-during-payment)

[attached](/api/payment_methods/attach)

When processing card payments, Stripe also uses setup_future_usage to dynamically optimize your payment flow and comply with regional legislation and network rules, such as SCA.

[SCA](/strong-customer-authentication)

If setup_future_usage is already set and you are performing a request using a publishable key, you may only update the value from on_session to off_session.

Use off_session if your customer may or may not be present in your checkout flow.

Use on_session if you intend to only reuse the payment method when your customer is present in your checkout flow.

- shippingobjectShipping information for this PaymentIntent.Show child parameters

Shipping information for this PaymentIntent.

- capture_methodenumsecret key only

- confirmation_tokenstring

- error_on_requires_actionboolean

- mandatestringsecret key only

- mandate_dataobject

- off_sessionboolean | stringsecret key only

- payment_method_dataobject

- payment_method_optionsobjectsecret key only

- payment_method_typesarray of stringssecret key only

- radar_optionsobjectsecret key only

- return_urlstring

- use_stripe_sdkboolean

Returns the resulting PaymentIntent after all possible transitions are applied.

# Increment an authorization

[Increment an authorization](/api/payment_intents/increment_authorization)

Perform an incremental authorization on an eligible PaymentIntent. To be eligible, the PaymentIntent’s status must be requires_capture and incremental_authorization_supported must be true.

[PaymentIntent](/api/payment_intents/object)

[incremental_authorization_supported](/api/charges/object#charge_object-payment_method_details-card_present-incremental_authorization_supported)

Incremental authorizations attempt to increase the authorized amount on your customer’s card to the new, higher amount provided. Similar to the initial authorization, incremental authorizations can be declined. A single PaymentIntent can call this endpoint multiple times to further increase the authorized amount.

If the incremental authorization succeeds, the PaymentIntent object returns with the updated amount. If the incremental authorization fails, a card_declined error returns, and no other fields on the PaymentIntent or Charge update. The PaymentIntent object remains capturable for the previously authorized amount.

[amount](/api/payment_intents/object#payment_intent_object-amount)

[card_declined](/error-codes#card-declined)

Each PaymentIntent can have a maximum of 10 incremental authorization attempts, including declines. After it’s captured, a PaymentIntent can no longer be incremented.

Learn more about incremental authorizations.

[incremental authorizations](/terminal/features/incremental-authorizations)

- amountintegerRequiredThe updated total amount that you intend to collect from the cardholder. This amount must be greater than the currently authorized amount.

The updated total amount that you intend to collect from the cardholder. This amount must be greater than the currently authorized amount.

- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- statement_descriptorstringFor card charges, use statement_descriptor_suffix. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. It must contain at least one letter and be 1–22 characters long.

For card charges, use statement_descriptor_suffix. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. It must contain at least one letter and be 1–22 characters long.

[statement_descriptor_suffix](https://stripe.com/docs/payments/account/statement-descriptors#dynamic)

- application_fee_amountintegerConnect only

- transfer_dataobjectConnect only

Returns a PaymentIntent object with the updated amount if the incremental authorization succeeds. Returns an error if the incremental authorization failed or the PaymentIntent isn’t eligible for incremental authorizations.

# Reconcile a customer_balance PaymentIntent

[Reconcile a customer_balance PaymentIntent](/api/payment_intents/apply_customer_balance)

Manually reconcile the remaining amount for a customer_balance PaymentIntent.

- amountintegerAmount that you intend to apply to this PaymentIntent from the customer’s cash balance.A positive integer representing how much to charge in the smallest currency unit (for example, 100 cents to charge 1 USD or 100 to charge 100 JPY, a zero-decimal currency).The maximum amount is the amount of the PaymentIntent.When you omit the amount, it defaults to the remaining amount requested on the PaymentIntent.

Amount that you intend to apply to this PaymentIntent from the customer’s cash balance.

A positive integer representing how much to charge in the smallest currency unit (for example, 100 cents to charge 1 USD or 100 to charge 100 JPY, a zero-decimal currency).

[smallest currency unit](/currencies#zero-decimal)

The maximum amount is the amount of the PaymentIntent.

When you omit the amount, it defaults to the remaining amount requested on the PaymentIntent.

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

Returns a PaymentIntent object.
