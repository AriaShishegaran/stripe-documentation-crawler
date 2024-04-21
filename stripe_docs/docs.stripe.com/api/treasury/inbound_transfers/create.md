- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Create an InboundTransfer

[Create an InboundTransfer](/api/treasury/inbound_transfers/create)

Creates an InboundTransfer.

- amountintegerRequiredAmount (in cents) to be transferred.

Amount (in cents) to be transferred.

- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- financial_accountstringRequiredThe FinancialAccount to send funds to.

The FinancialAccount to send funds to.

- origin_payment_methodstringRequiredThe origin payment method to be debited for the InboundTransfer.

The origin payment method to be debited for the InboundTransfer.

- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- statement_descriptorstringThe complete description that appears on your customers’ statements. Maximum 10 characters.

The complete description that appears on your customers’ statements. Maximum 10 characters.

Returns an InboundTransfer object if there were no issues with InboundTransfer creation. The status of the created InboundTransfer object is initially marked as processing.

# Retrieve an InboundTransfer

[Retrieve an InboundTransfer](/api/treasury/inbound_transfers/retrieve)

Retrieves the details of an existing InboundTransfer.

No parameters.

Returns an InboundTransfer object if a valid identifier was provided. Otherwise, returns an error.

# List all InboundTransfers

[List all InboundTransfers](/api/treasury/inbound_transfers/list)

Returns a list of InboundTransfers sent from the specified FinancialAccount.

- financial_accountstringRequiredReturns objects associated with this FinancialAccount.

Returns objects associated with this FinancialAccount.

- statusenumOnly return InboundTransfers that have the given status: processing, succeeded, failed or canceled.

Only return InboundTransfers that have the given status: processing, succeeded, failed or canceled.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit InboundTransfers, starting after InboundTransfer starting_after. Each entry in the array is a separate InboundTransfer object. If no more InboundTransfers are available, the resulting array is empty.

# Cancel an InboundTransfer

[Cancel an InboundTransfer](/api/treasury/inbound_transfers/cancel)

Cancels an InboundTransfer.

No parameters.

Returns the InboundTransfer object if the cancellation succeeded. Returns an error if the InboundTransfer has already been canceled or cannot be canceled.

# Test mode: Fail an InboundTransferTest helper

[Test mode: Fail an InboundTransfer](/api/treasury/inbound_transfers/test_mode_fail)

Transitions a test mode created InboundTransfer to the failed status. The InboundTransfer must already be in the processing state.

- failure_detailsobjectDetails about a failed InboundTransfer.Show child parameters

Details about a failed InboundTransfer.

Returns the InboundTransfer object in the returned state. Returns an error if the InboundTransfer has already failed or cannot be failed.
