- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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
