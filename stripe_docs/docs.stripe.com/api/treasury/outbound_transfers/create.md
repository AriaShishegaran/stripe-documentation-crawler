- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# Cancel an OutboundTransfer

[Cancel an OutboundTransfer](/api/treasury/outbound_transfers/cancel)

An OutboundTransfer can be canceled if the funds have not yet been paid out.

No parameters.

Returns the OutboundTransfer object if the cancellation succeeded. Returns an error if the object has already been canceled or cannot be canceled.

# Test mode: Fail an OutboundTransferTest helper

[Test mode: Fail an OutboundTransfer](/api/treasury/outbound_transfers/test_mode_fail)

Transitions a test mode created OutboundTransfer to the failed status. The OutboundTransfer must already be in the processing state.

No parameters.

Returns the OutboundTransfer object in the failed state. Returns an error if the OutboundTransfer has already been failed or cannot be failed.
