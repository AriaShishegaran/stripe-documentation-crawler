- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Charge object

[The Charge object](/api/charges/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- amountintegerAmount intended to be collected by this payment. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or equivalent in charge currency. The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

Amount intended to be collected by this payment. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or equivalent in charge currency. The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).

[smallest currency unit](/currencies#zero-decimal)

[equivalent in charge currency](/currencies#minimum-and-maximum-charge-amounts)

- balance_transactionnullable stringExpandableID of the balance transaction that describes the impact of this charge on your account balance (not including refunds or disputes).

ID of the balance transaction that describes the impact of this charge on your account balance (not including refunds or disputes).

- billing_detailsobjectBilling information associated with the payment method at the time of the transaction.Show child attributes

Billing information associated with the payment method at the time of the transaction.

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- customernullable stringExpandableID of the customer this charge is for if one exists.

ID of the customer this charge is for if one exists.

- descriptionnullable stringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- disputedbooleanWhether the charge has been disputed.

Whether the charge has been disputed.

- invoicenullable stringExpandableID of the invoice this charge is for if one exists.

ID of the invoice this charge is for if one exists.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- payment_intentnullable stringExpandableID of the PaymentIntent associated with this charge, if one exists.

ID of the PaymentIntent associated with this charge, if one exists.

- payment_method_detailsnullable objectDetails about the payment method at the time of the transaction.Show child attributes

Details about the payment method at the time of the transaction.

- receipt_emailnullable stringThis is the email address that the receipt for this charge was sent to.

This is the email address that the receipt for this charge was sent to.

- refundedbooleanWhether the charge has been fully refunded. If the charge is only partially refunded, this attribute will still be false.

Whether the charge has been fully refunded. If the charge is only partially refunded, this attribute will still be false.

- shippingnullable objectShipping information for the charge.Show child attributes

Shipping information for the charge.

- statement_descriptornullable stringFor card charges, use statement_descriptor_suffix instead. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. Must contain at least one letter, maximum 22 characters.

For card charges, use statement_descriptor_suffix instead. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. Must contain at least one letter, maximum 22 characters.

- statement_descriptor_suffixnullable stringProvides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.

Provides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.

- statusenumThe status of the payment is either succeeded, pending, or failed.

The status of the payment is either succeeded, pending, or failed.

- objectstring

- amount_capturedinteger

- amount_refundedinteger

- applicationnullable stringExpandableConnect only

- application_feenullable stringExpandableConnect only

- application_fee_amountnullable integerConnect only

- calculated_statement_descriptornullable string

- capturedboolean

- createdtimestamp

- failure_balance_transactionnullable stringExpandable

- failure_codenullable string

- failure_messagenullable string

- fraud_detailsnullable object

- livemodeboolean

- on_behalf_ofnullable stringExpandableConnect only

- outcomenullable object

- paidboolean

- payment_methodnullable string

- radar_optionsnullable object

- receipt_numbernullable string

- receipt_urlnullable string

- refundsnullable objectExpandable

- reviewnullable stringExpandable

- source_transfernullable stringExpandableConnect only

- transfernullable stringExpandableConnect only

- transfer_datanullable objectConnect only

- transfer_groupnullable stringConnect only

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
