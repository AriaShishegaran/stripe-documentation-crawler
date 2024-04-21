- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Inbound Transfers

[Inbound Transfers](/api/treasury/inbound_transfers)

Use InboundTransfers to add funds to your FinancialAccount via a PaymentMethod that is owned by you. The funds will be transferred via an ACH debit.

[InboundTransfers](/treasury/moving-money/financial-accounts/into/inbound-transfers)

[FinancialAccount](#financial_accounts)

[POST/v1/treasury/inbound_transfers](/api/treasury/inbound_transfers/create)

[GET/v1/treasury/inbound_transfers/:id](/api/treasury/inbound_transfers/retrieve)

[GET/v1/treasury/inbound_transfers](/api/treasury/inbound_transfers/list)

[POST/v1/treasury/inbound_transfers/:id/cancel](/api/treasury/inbound_transfers/cancel)

[POST/v1/test_helpers/treasury/inbound_transfers/:id/fail](/api/treasury/inbound_transfers/test_mode_fail)

[POST/v1/test_helpers/treasury/inbound_transfers/:id/return](/api/treasury/inbound_transfers/test_mode_return)

[POST/v1/test_helpers/treasury/inbound_transfers/:id/succeed](/api/treasury/inbound_transfers/test_mode_succeed)

# The InboundTransfer object

[The InboundTransfer object](/api/treasury/inbound_transfers/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- objectstringString representing the object’s type. Objects of the same type share the same value.

String representing the object’s type. Objects of the same type share the same value.

- amountintegerAmount (in cents) transferred.

Amount (in cents) transferred.

- cancelablebooleanReturns true if the InboundTransfer is able to be canceled.

Returns true if the InboundTransfer is able to be canceled.

- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.

Time at which the object was created. Measured in seconds since the Unix epoch.

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- descriptionnullable stringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- failure_detailsnullable objectDetails about this InboundTransfer’s failure. Only set when status is failed.Show child attributes

Details about this InboundTransfer’s failure. Only set when status is failed.

- financial_accountstringThe FinancialAccount that received the funds.

The FinancialAccount that received the funds.

- hosted_regulatory_receipt_urlnullable stringA hosted transaction receipt URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

A hosted transaction receipt URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

[hosted transaction receipt](/treasury/moving-money/regulatory-receipts)

- linked_flowsobjectOther flows linked to a InboundTransfer.Show child attributes

Other flows linked to a InboundTransfer.

- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.

Has the value true if the object exists in live mode or the value false if the object exists in test mode.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- origin_payment_methodstringThe origin payment method to be debited for an InboundTransfer.

The origin payment method to be debited for an InboundTransfer.

- origin_payment_method_detailsnullable objectDetails about the PaymentMethod for an InboundTransfer.Show child attributes

Details about the PaymentMethod for an InboundTransfer.

- returnednullable booleanReturns true if the funds for an InboundTransfer were returned after the InboundTransfer went to the succeeded state.

Returns true if the funds for an InboundTransfer were returned after the InboundTransfer went to the succeeded state.

- statement_descriptorstringStatement descriptor shown when funds are debited from the source. Not all payment networks support statement_descriptor.

Statement descriptor shown when funds are debited from the source. Not all payment networks support statement_descriptor.

- statusenumStatus of the InboundTransfer: processing, succeeded, failed, and canceled. An InboundTransfer is processing if it is created and pending. The status changes to succeeded once the funds have been “confirmed” and a transaction is created and posted. The status changes to failed if the transfer fails.

Status of the InboundTransfer: processing, succeeded, failed, and canceled. An InboundTransfer is processing if it is created and pending. The status changes to succeeded once the funds have been “confirmed” and a transaction is created and posted. The status changes to failed if the transfer fails.

- status_transitionsobjectHash containing timestamps of when the object transitioned to a particular status.Show child attributes

Hash containing timestamps of when the object transitioned to a particular status.

- transactionnullable stringExpandableThe Transaction associated with this object.

The Transaction associated with this object.

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
