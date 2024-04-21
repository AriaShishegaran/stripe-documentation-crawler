- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Create a chargeDeprecated

[Create a charge](/api/charges/create)

This method is no longer recommended—use the Payment Intents API to initiate a new payment instead. Confirmation of the PaymentIntent creates the Charge object used to request payment.

[Payment Intents API](/api/payment_intents)

- amountintegerRequiredAmount intended to be collected by this payment. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or equivalent in charge currency. The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

Amount intended to be collected by this payment. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or equivalent in charge currency. The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

[smallest currency unit](/currencies#zero-decimal)

[equivalent in charge currency](/currencies#minimum-and-maximum-charge-amounts)

- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- customerstringThe ID of an existing customer that will be charged in this request.

The ID of an existing customer that will be charged in this request.

- descriptionstringAn arbitrary string which you can attach to a Charge object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the description of the charge(s) that they are describing.

An arbitrary string which you can attach to a Charge object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the description of the charge(s) that they are describing.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- receipt_emailstringThe email address to which this charge’s receipt will be sent. The receipt will not be sent until the charge is paid, and no receipts will be sent for test mode charges. If this charge is for a Customer, the email address specified here will override the customer’s email address. If receipt_email is specified for a charge in live mode, a receipt will be sent regardless of your email settings.

The email address to which this charge’s receipt will be sent. The receipt will not be sent until the charge is paid, and no receipts will be sent for test mode charges. If this charge is for a Customer, the email address specified here will override the customer’s email address. If receipt_email is specified for a charge in live mode, a receipt will be sent regardless of your email settings.

[receipt](/dashboard/receipts)

[Customer](/api/customers/object)

[email settings](https://dashboard.stripe.com/account/emails)

- shippingobjectShipping information for the charge. Helps prevent fraud on charges for physical goods.Show child parameters

Shipping information for the charge. Helps prevent fraud on charges for physical goods.

- sourcestringA payment source to be charged. This can be the ID of a card (i.e., credit or debit card), a bank account, a source, a token, or a connected account. For certain sources—namely, cards, bank accounts, and attached sources—you must also pass the ID of the associated customer.

A payment source to be charged. This can be the ID of a card (i.e., credit or debit card), a bank account, a source, a token, or a connected account. For certain sources—namely, cards, bank accounts, and attached sources—you must also pass the ID of the associated customer.

[card](/api#cards)

[bank account](/api#bank_accounts)

[source](/api#sources)

[token](/api#tokens)

[connected account](/connect/account-debits#charging-a-connected-account)

[cards](/api#cards)

[bank accounts](/api#bank_accounts)

[sources](/api#sources)

- statement_descriptorstringFor card charges, use statement_descriptor_suffix instead. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. Must contain at least one letter, maximum 22 characters.

For card charges, use statement_descriptor_suffix instead. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. Must contain at least one letter, maximum 22 characters.

- statement_descriptor_suffixstringProvides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.

Provides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.

- application_fee_amountintegerConnect only

- captureboolean

- on_behalf_ofstringConnect only

- radar_optionsobject

- transfer_dataobjectConnect only

- transfer_groupstringConnect only

Returns the charge object if the charge succeeded. This call raises an error if something goes wrong. A common source of error is an invalid or expired card, or a valid card with insufficient available balance.

[an error](#errors)

# Update a charge

[Update a charge](/api/charges/update)

Updates the specified charge by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

- customerstringThe ID of an existing customer that will be associated with this request. This field may only be updated if there is no existing associated customer with this charge.

The ID of an existing customer that will be associated with this request. This field may only be updated if there is no existing associated customer with this charge.

- descriptionstringAn arbitrary string which you can attach to a charge object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the description of the charge(s) that they are describing.

An arbitrary string which you can attach to a charge object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the description of the charge(s) that they are describing.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- receipt_emailstringThis is the email address that the receipt for this charge will be sent to. If this field is updated, then a new email receipt will be sent to the updated address.

This is the email address that the receipt for this charge will be sent to. If this field is updated, then a new email receipt will be sent to the updated address.

- shippingobjectShipping information for the charge. Helps prevent fraud on charges for physical goods.Show child parameters

Shipping information for the charge. Helps prevent fraud on charges for physical goods.

- fraud_detailsobject

- transfer_groupstringConnect only

Returns the charge object if the update succeeded. This call will raise an error if update parameters are invalid.

[an error](#errors)

# Retrieve a charge

[Retrieve a charge](/api/charges/retrieve)

Retrieves the details of a charge that has previously been created. Supply the unique charge ID that was returned from your previous request, and Stripe will return the corresponding charge information. The same information is returned when creating or refunding the charge.

No parameters.

Returns a charge if a valid identifier was provided, and raises an error otherwise.

[an error](#errors)

# List all charges

[List all charges](/api/charges/list)

Returns a list of charges you’ve previously created. The charges are returned in sorted order, with the most recent charges appearing first.

- customerstringOnly return charges for the customer specified by this customer ID.

Only return charges for the customer specified by this customer ID.

- createdobject

- ending_beforestring

- limitinteger

- payment_intentstring

- starting_afterstring

- transfer_groupstringConnect only

A dictionary with a data property that contains an array of up to limit charges, starting after charge starting_after. Each entry in the array is a separate charge object. If no more charges are available, the resulting array will be empty. If you provide a non-existent customer ID, this call raises an error.

[an error](#errors)

# Capture a charge

[Capture a charge](/api/charges/capture)

Capture the payment of an existing, uncaptured charge that was created with the capture option set to false.

Uncaptured payments expire a set number of days after they are created (7 by default), after which they are marked as refunded and capture attempts will fail.

[7 by default](/charges/placing-a-hold)

Don’t use this method to capture a PaymentIntent-initiated charge. Use Capture a PaymentIntent.

[Capture a PaymentIntent](/api/payment_intents/capture)

- amountintegerThe amount to capture, which must be less than or equal to the original amount. Any additional amount will be automatically refunded.

The amount to capture, which must be less than or equal to the original amount. Any additional amount will be automatically refunded.

- receipt_emailstringThe email address to send this charge’s receipt to. This will override the previously-specified email address for this charge, if one was set. Receipts will not be sent in test mode.

The email address to send this charge’s receipt to. This will override the previously-specified email address for this charge, if one was set. Receipts will not be sent in test mode.

- statement_descriptorstringFor card charges, use statement_descriptor_suffix instead. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. Must contain at least one letter, maximum 22 characters.

For card charges, use statement_descriptor_suffix instead. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. Must contain at least one letter, maximum 22 characters.

- statement_descriptor_suffixstringProvides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.

Provides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.

- application_fee_amountintegerConnect only

- transfer_dataobjectConnect only

- transfer_groupstringConnect only

Returns the charge object, with an updated captured property (set to true). Capturing a charge will always succeed, unless the charge is already refunded, expired, captured, or an invalid capture amount is specified, in which case this method will raise an error.

[an error](#errors)
