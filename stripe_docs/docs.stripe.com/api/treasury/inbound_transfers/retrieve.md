- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# Test mode: Return an InboundTransferTest helper

[Test mode: Return an InboundTransfer](/api/treasury/inbound_transfers/test_mode_return)

Marks the test mode InboundTransfer object as returned and links the InboundTransfer to a ReceivedDebit. The InboundTransfer must already be in the succeeded state.

No parameters.

Returns the InboundTransfer object with returned set to true. Returns an error if the InboundTransfer has already been returned or cannot be returned.
