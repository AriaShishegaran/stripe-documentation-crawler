- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Outbound Transfers

[Outbound Transfers](/api/treasury/outbound_transfers)

Use OutboundTransfers to transfer funds from a FinancialAccount to a PaymentMethod belonging to the same entity. To send funds to a different party, use OutboundPayments instead. You can send funds over ACH rails or through a domestic wire transfer to a user’s own external bank account.

[FinancialAccount](#financial_accounts)

[OutboundPayments](#outbound_payments)

Simulate OutboundTransfer state changes with the /v1/test_helpers/treasury/outbound_transfers endpoints. These methods can only be called on test mode objects.

[POST/v1/treasury/outbound_transfers](/api/treasury/outbound_transfers/create)

[GET/v1/treasury/outbound_transfers/:id](/api/treasury/outbound_transfers/retrieve)

[GET/v1/treasury/outbound_transfers](/api/treasury/outbound_transfers/list)

[POST/v1/treasury/outbound_transfers/:id/cancel](/api/treasury/outbound_transfers/cancel)

[POST/v1/test_helpers/treasury/outbound_transfers/:id/fail](/api/treasury/outbound_transfers/test_mode_fail)

[POST/v1/test_helpers/treasury/outbound_transfers/:id/post](/api/treasury/outbound_transfers/test_mode_post)

[POST/v1/test_helpers/treasury/outbound_transfers/:id/return](/api/treasury/outbound_transfers/test_mode_return)

# The OutboundTransfer object

[The OutboundTransfer object](/api/treasury/outbound_transfers/object)

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

- descriptionnullable stringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- destination_payment_methodnullable stringThe PaymentMethod used as the payment instrument for an OutboundTransfer.

The PaymentMethod used as the payment instrument for an OutboundTransfer.

- destination_payment_method_detailsobjectDetails about the PaymentMethod for an OutboundTransferShow child attributes

Details about the PaymentMethod for an OutboundTransfer

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

- returned_detailsnullable objectDetails about a returned OutboundTransfer. Only set when the status is returned.Show child attributes

Details about a returned OutboundTransfer. Only set when the status is returned.

- statement_descriptorstringInformation about the OutboundTransfer to be sent to the recipient account.

Information about the OutboundTransfer to be sent to the recipient account.

- statusenumCurrent status of the OutboundTransfer: processing, failed, canceled, posted, returned. An OutboundTransfer is processing if it has been created and is pending. The status changes to posted once the OutboundTransfer has been “confirmed” and funds have left the account, or to failed or canceled. If an OutboundTransfer fails to arrive at its destination, its status will change to returned.

Current status of the OutboundTransfer: processing, failed, canceled, posted, returned. An OutboundTransfer is processing if it has been created and is pending. The status changes to posted once the OutboundTransfer has been “confirmed” and funds have left the account, or to failed or canceled. If an OutboundTransfer fails to arrive at its destination, its status will change to returned.

- status_transitionsobjectHash containing timestamps of when the object transitioned to a particular status.Show child attributes

Hash containing timestamps of when the object transitioned to a particular status.

- transactionstringExpandableThe Transaction associated with this object.

The Transaction associated with this object.

# Create an OutboundTransfer

[Create an OutboundTransfer](/api/treasury/outbound_transfers/create)

Creates an OutboundTransfer.

- amountintegerRequiredAmount (in cents) to be transferred.

Amount (in cents) to be transferred.

- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- financial_accountstringRequiredThe FinancialAccount to pull funds from.

The FinancialAccount to pull funds from.

- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- destination_payment_methodstringThe PaymentMethod to use as the payment instrument for the OutboundTransfer.

The PaymentMethod to use as the payment instrument for the OutboundTransfer.

- destination_payment_method_optionsobjectHash describing payment method configuration details.Show child parameters

Hash describing payment method configuration details.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- statement_descriptorstringStatement descriptor to be shown on the receiving end of an OutboundTransfer. Maximum 10 characters for ach transfers or 140 characters for us_domestic_wire transfers. The default value is “transfer”.

Statement descriptor to be shown on the receiving end of an OutboundTransfer. Maximum 10 characters for ach transfers or 140 characters for us_domestic_wire transfers. The default value is “transfer”.

Returns an OutboundTransfer object if there were no issues with OutboundTransfer creation. The status of the created OutboundTransfer object is initially marked as processing.

# Retrieve an OutboundTransfer

[Retrieve an OutboundTransfer](/api/treasury/outbound_transfers/retrieve)

Retrieves the details of an existing OutboundTransfer by passing the unique OutboundTransfer ID from either the OutboundTransfer creation request or OutboundTransfer list.

No parameters.

Returns an OutboundTransfer object if a valid identifier was provided. Otherwise, returns an error.

# List all OutboundTransfers

[List all OutboundTransfers](/api/treasury/outbound_transfers/list)

Returns a list of OutboundTransfers sent from the specified FinancialAccount.

- financial_accountstringRequiredReturns objects associated with this FinancialAccount.

Returns objects associated with this FinancialAccount.

- statusenumOnly return OutboundTransfers that have the given status: processing, canceled, failed, posted, or returned.

Only return OutboundTransfers that have the given status: processing, canceled, failed, posted, or returned.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit OutboundTransfers, starting after OutboundTransfer starting_after. Each entry in the array is a separate OutboundTransfer object. If no more OutboundTransfers are available, the resulting array is empty.
