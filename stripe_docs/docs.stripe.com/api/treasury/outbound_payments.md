- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Outbound Payments

[Outbound Payments](/api/treasury/outbound_payments)

Use OutboundPayments to send funds to another party’s external bank account or FinancialAccount. To send money to an account belonging to the same user, use an OutboundTransfer.

[FinancialAccount](#financial_accounts)

[OutboundTransfer](#outbound_transfers)

Simulate OutboundPayment state changes with the /v1/test_helpers/treasury/outbound_payments endpoints. These methods can only be called on test mode objects.

[POST/v1/treasury/outbound_payments](/api/treasury/outbound_payments/create)

[GET/v1/treasury/outbound_payments/:id](/api/treasury/outbound_payments/retrieve)

[GET/v1/treasury/outbound_payments](/api/treasury/outbound_payments/list)

[POST/v1/treasury/outbound_payments/:id/cancel](/api/treasury/outbound_payments/cancel)

[POST/v1/test_helpers/treasury/outbound_payments/:id/fail](/api/treasury/outbound_payments/test_mode_fail)

[POST/v1/test_helpers/treasury/outbound_payments/:id/post](/api/treasury/outbound_payments/test_mode_post)

[POST/v1/test_helpers/treasury/outbound_payments/:id/return](/api/treasury/outbound_payments/test_mode_return)

# The Outbound Payment object

[The Outbound Payment object](/api/treasury/outbound_payments/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- objectstringString representing the object’s type. Objects of the same type share the same value.

String representing the object’s type. Objects of the same type share the same value.

- amountintegerAmount (in cents) transferred.

Amount (in cents) transferred.

- cancelablebooleanReturns true if the object can be canceled, and false otherwise.

Returns true if the object can be canceled, and false otherwise.

- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.

Time at which the object was created. Measured in seconds since the Unix epoch.

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- customernullable stringID of the customer to whom an OutboundPayment is sent.

ID of the customer to whom an OutboundPayment is sent.

[customer](/api/customers)

- descriptionnullable stringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- destination_payment_methodnullable stringThe PaymentMethod via which an OutboundPayment is sent. This field can be empty if the OutboundPayment was created using destination_payment_method_data.

The PaymentMethod via which an OutboundPayment is sent. This field can be empty if the OutboundPayment was created using destination_payment_method_data.

- destination_payment_method_detailsnullable objectDetails about the PaymentMethod for an OutboundPayment.Show child attributes

Details about the PaymentMethod for an OutboundPayment.

- end_user_detailsnullable objectDetails about the end user.Show child attributes

Details about the end user.

- expected_arrival_datetimestampThe date when funds are expected to arrive in the destination account.

The date when funds are expected to arrive in the destination account.

- financial_accountstringThe FinancialAccount that funds were pulled from.

The FinancialAccount that funds were pulled from.

- hosted_regulatory_receipt_urlnullable stringA hosted transaction receipt URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

A hosted transaction receipt URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

[hosted transaction receipt](/treasury/moving-money/regulatory-receipts)

- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.

Has the value true if the object exists in live mode or the value false if the object exists in test mode.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- returned_detailsnullable objectDetails about a returned OutboundPayment. Only set when the status is returned.Show child attributes

Details about a returned OutboundPayment. Only set when the status is returned.

- statement_descriptorstringThe description that appears on the receiving end for an OutboundPayment (for example, bank statement for external bank transfer).

The description that appears on the receiving end for an OutboundPayment (for example, bank statement for external bank transfer).

- statusenumCurrent status of the OutboundPayment: processing, failed, posted, returned, canceled. An OutboundPayment is processing if it has been created and is pending. The status changes to posted once the OutboundPayment has been “confirmed” and funds have left the account, or to failed or canceled. If an OutboundPayment fails to arrive at its destination, its status will change to returned.

Current status of the OutboundPayment: processing, failed, posted, returned, canceled. An OutboundPayment is processing if it has been created and is pending. The status changes to posted once the OutboundPayment has been “confirmed” and funds have left the account, or to failed or canceled. If an OutboundPayment fails to arrive at its destination, its status will change to returned.

- status_transitionsobjectHash containing timestamps of when the object transitioned to a particular status.Show child attributes

Hash containing timestamps of when the object transitioned to a particular status.

- transactionstringExpandableThe Transaction associated with this object.

The Transaction associated with this object.

# Create an OutboundPayment

[Create an OutboundPayment](/api/treasury/outbound_payments/create)

Creates an OutboundPayment.

- amountintegerRequiredAmount (in cents) to be transferred.

Amount (in cents) to be transferred.

- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- financial_accountstringRequiredThe FinancialAccount to pull funds from.

The FinancialAccount to pull funds from.

- customerstringID of the customer to whom the OutboundPayment is sent. Must match the Customer attached to the destination_payment_method passed in.

ID of the customer to whom the OutboundPayment is sent. Must match the Customer attached to the destination_payment_method passed in.

- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- destination_payment_methodstringThe PaymentMethod to use as the payment instrument for the OutboundPayment. Exclusive with destination_payment_method_data.

The PaymentMethod to use as the payment instrument for the OutboundPayment. Exclusive with destination_payment_method_data.

- destination_payment_method_dataobjectHash used to generate the PaymentMethod to be used for this OutboundPayment. Exclusive with destination_payment_method.Show child parameters

Hash used to generate the PaymentMethod to be used for this OutboundPayment. Exclusive with destination_payment_method.

- destination_payment_method_optionsobjectPayment method-specific configuration for this OutboundPayment.Show child parameters

Payment method-specific configuration for this OutboundPayment.

- end_user_detailsobjectEnd user details.Show child parameters

End user details.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- statement_descriptorstringThe description that appears on the receiving end for this OutboundPayment (for example, bank statement for external bank transfer). Maximum 10 characters for ach payments, 140 characters for us_domestic_wire payments, or 500 characters for stripe network transfers. The default value is “payment”.

The description that appears on the receiving end for this OutboundPayment (for example, bank statement for external bank transfer). Maximum 10 characters for ach payments, 140 characters for us_domestic_wire payments, or 500 characters for stripe network transfers. The default value is “payment”.

Returns an OutboundPayment object if there were no issues with OutboundPayment creation.

# Retrieve an OutboundPayment

[Retrieve an OutboundPayment](/api/treasury/outbound_payments/retrieve)

Retrieves the details of an existing OutboundPayment by passing the unique OutboundPayment ID from either the OutboundPayment creation request or OutboundPayment list.

No parameters.

Returns an OutboundPayment object if a valid identifier was provided. Otherwise, returns an error.

# List all OutboundPayments

[List all OutboundPayments](/api/treasury/outbound_payments/list)

Returns a list of OutboundPayments sent from the specified FinancialAccount.

- financial_accountstringRequiredReturns objects associated with this FinancialAccount.

Returns objects associated with this FinancialAccount.

- createdobjectOnly return OutboundPayments that were created during the given date interval.Show child parameters

Only return OutboundPayments that were created during the given date interval.

- customerstringOnly return OutboundPayments sent to this customer.

Only return OutboundPayments sent to this customer.

- statusenumOnly return OutboundPayments that have the given status: processing, failed, posted, returned, or canceled.

Only return OutboundPayments that have the given status: processing, failed, posted, returned, or canceled.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit OutboundPayments, starting after OutboundPayments starting_after. Each entry in the array is a separate OutboundPayments object. If no more OutboundPayments are available, the resulting array is empty.
