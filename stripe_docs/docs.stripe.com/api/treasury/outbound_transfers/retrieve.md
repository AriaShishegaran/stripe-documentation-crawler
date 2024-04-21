- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# Test mode: Post an OutboundTransferTest helper

[Test mode: Post an OutboundTransfer](/api/treasury/outbound_transfers/test_mode_post)

Transitions a test mode created OutboundTransfer to the posted status. The OutboundTransfer must already be in the processing state.

No parameters.

Returns the OutboundTransfer object in the posted state. Returns an error if the OutboundTransfer has already been posted or cannot be posted.
