- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# Cancel an OutboundPayment

[Cancel an OutboundPayment](/api/treasury/outbound_payments/cancel)

Cancel an OutboundPayment.

No parameters.

Returns the OutboundPayment object if the cancellation succeeded. Returns an error if the OutboundPayment has already been canceled or cannot be canceled.

# Test mode: Fail an OutboundPaymentTest helper

[Test mode: Fail an OutboundPayment](/api/treasury/outbound_payments/test_mode_fail)

Transitions a test mode created OutboundPayment to the failed status. The OutboundPayment must already be in the processing state.

No parameters.

Returns the OutboundPayment object in the failed state. Returns an error if the OutboundPayment has already been failed or cannot be failed.

# Test mode: Post an OutboundPaymentTest helper

[Test mode: Post an OutboundPayment](/api/treasury/outbound_payments/test_mode_post)

Transitions a test mode created OutboundPayment to the posted status. The OutboundPayment must already be in the processing state.

No parameters.

Returns the OutboundPayment object in the posted state. Returns an error if the OutboundPayment has already been posted or cannot be posted.

# Test mode: Return an OutboundPaymentTest helper

[Test mode: Return an OutboundPayment](/api/treasury/outbound_payments/test_mode_return)

Transitions a test mode created OutboundPayment to the returned status. The OutboundPayment must already be in the processing state.

- returned_detailsobjectOptional hash to set the the return code.Show child parameters

Optional hash to set the the return code.

Returns the OutboundPayment object in the returned state. Returns an error if the OutboundPayment has already been returned or cannot be returned.
