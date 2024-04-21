- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Update a PaymentIntent

[Update a PaymentIntent](/api/payment_intents/update)

Updates properties on a PaymentIntent object without confirming.

Depending on which properties you update, you might need to confirm the PaymentIntent again. For example, updating the payment_method always requires you to confirm the PaymentIntent again. If you prefer to update and confirm at the same time, we recommend updating properties through the confirm API instead.

[confirm API](/api/payment_intents/confirm)

- amountintegerAmount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or equivalent in charge currency. The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

Amount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or equivalent in charge currency. The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

[smallest currency unit](/currencies#zero-decimal)

[equivalent in charge currency](/currencies#minimum-and-maximum-charge-amounts)

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- customerstringID of the Customer this PaymentIntent belongs to, if one exists.Payment methods attached to other Customers cannot be used with this PaymentIntent.If present in combination with setup_future_usage, this PaymentIntent’s payment method will be attached to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete.

ID of the Customer this PaymentIntent belongs to, if one exists.

Payment methods attached to other Customers cannot be used with this PaymentIntent.

If present in combination with setup_future_usage, this PaymentIntent’s payment method will be attached to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete.

[setup_future_usage](#payment_intent_object-setup_future_usage)

- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

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

- statement_descriptorstringFor card charges, use statement_descriptor_suffix. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. It must contain at least one letter and be 1–22 characters long.

For card charges, use statement_descriptor_suffix. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. It must contain at least one letter and be 1–22 characters long.

[statement_descriptor_suffix](https://stripe.com/docs/payments/account/statement-descriptors#dynamic)

- statement_descriptor_suffixstringProvides information about a card payment that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.

Provides information about a card payment that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.

- application_fee_amountintegerConnect only

- capture_methodenumsecret key only

- payment_method_configurationstring

- payment_method_dataobject

- payment_method_optionsobject

- payment_method_typesarray of strings

- transfer_dataobjectConnect only

- transfer_groupstringConnect only

Returns a PaymentIntent object.

# Retrieve a PaymentIntent

[Retrieve a PaymentIntent](/api/payment_intents/retrieve)

Retrieves the details of a PaymentIntent that has previously been created.

You can retrieve a PaymentIntent client-side using a publishable key when the client_secret is in the query string.

If you retrieve a PaymentIntent with a publishable key, it only returns a subset of properties. Refer to the payment intent object reference for more details.

[payment intent](#payment_intent_object)

- client_secretstringRequired if you use a publishable key.The client secret of the PaymentIntent. We require it if you use a publishable key to retrieve the source.

The client secret of the PaymentIntent. We require it if you use a publishable key to retrieve the source.

Returns a PaymentIntent if a valid identifier was provided.

# List all PaymentIntents

[List all PaymentIntents](/api/payment_intents/list)

Returns a list of PaymentIntents.

- customerstringOnly return PaymentIntents for the customer that this customer ID specifies.

Only return PaymentIntents for the customer that this customer ID specifies.

- createdobject

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit PaymentIntents, starting after PaymentIntent starting_after. Each entry in the array is a separate PaymentIntent object. If no other PaymentIntents are available, the resulting array is empty.

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
