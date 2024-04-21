- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Debit Reversals

[Debit Reversals](/api/treasury/debit_reversals)

You can reverse some ReceivedDebits depending on their network and source flow. Reversing a ReceivedDebit leads to the creation of a new object known as a DebitReversal.

[ReceivedDebits](#received_debits)

[POST/v1/treasury/debit_reversals](/api/treasury/debit_reversals/create)

[GET/v1/treasury/debit_reversals/:id](/api/treasury/debit_reversals/retrieve)

[GET/v1/treasury/debit_reversals](/api/treasury/debit_reversals/list)

# The DebitReversal object

[The DebitReversal object](/api/treasury/debit_reversals/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- objectstringString representing the object’s type. Objects of the same type share the same value.

String representing the object’s type. Objects of the same type share the same value.

- amountintegerAmount (in cents) transferred.

Amount (in cents) transferred.

- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.

Time at which the object was created. Measured in seconds since the Unix epoch.

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- financial_accountnullable stringThe FinancialAccount to reverse funds from.

The FinancialAccount to reverse funds from.

- hosted_regulatory_receipt_urlnullable stringA hosted transaction receipt URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

A hosted transaction receipt URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

[hosted transaction receipt](/treasury/moving-money/regulatory-receipts)

- linked_flowsnullable objectOther flows linked to a DebitReversal.Show child attributes

Other flows linked to a DebitReversal.

- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.

Has the value true if the object exists in live mode or the value false if the object exists in test mode.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- networkenumThe rails used to reverse the funds.

The rails used to reverse the funds.

- received_debitstringThe ReceivedDebit being reversed.

The ReceivedDebit being reversed.

- statusenumStatus of the DebitReversalPossible enum valuesfailedThe network has resolved the DebitReversal against the user.processingThe DebitReversal starting state.succeededThe network has resolved the DebitReversal in the users favour. A crediting Transaction is created.

Status of the DebitReversal

The network has resolved the DebitReversal against the user.

The DebitReversal starting state.

The network has resolved the DebitReversal in the users favour. A crediting Transaction is created.

- status_transitionsobjectHash containing timestamps of when the object transitioned to a particular status.Show child attributes

Hash containing timestamps of when the object transitioned to a particular status.

- transactionnullable stringExpandableThe Transaction associated with this object.

The Transaction associated with this object.

# Create a DebitReversal

[Create a DebitReversal](/api/treasury/debit_reversals/create)

Reverses a ReceivedDebit and creates a DebitReversal object.

- received_debitstringRequiredThe ReceivedDebit to reverse.

The ReceivedDebit to reverse.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns a DebitReversal object.

# Retrieve a DebitReversal

[Retrieve a DebitReversal](/api/treasury/debit_reversals/retrieve)

Retrieves a DebitReversal object.

No parameters.

Returns a DebitReversal object.

# List all DebitReversals

[List all DebitReversals](/api/treasury/debit_reversals/list)

Returns a list of DebitReversals.

- financial_accountstringRequiredReturns objects associated with this FinancialAccount.

Returns objects associated with this FinancialAccount.

- received_debitstringOnly return DebitReversals for the ReceivedDebit ID.

Only return DebitReversals for the ReceivedDebit ID.

- resolutionenumOnly return DebitReversals for a given resolution.Possible enum valueslostDebitReversal was lost, and no Transactions will be created.wonDebitReversal was won, and a crediting Transaction will be created.

Only return DebitReversals for a given resolution.

DebitReversal was lost, and no Transactions will be created.

DebitReversal was won, and a crediting Transaction will be created.

- statusenumOnly return DebitReversals for a given status.Possible enum valuescanceledThe DebitReversal has been canceled before it has been sent to the network and no funds have been returned to the account. (Currently not supported).completedThe network has provided a resolution for the DebitReversal. If won, a crediting Transaction is created.processingThe DebitReversal starting state.

Only return DebitReversals for a given status.

The DebitReversal has been canceled before it has been sent to the network and no funds have been returned to the account. (Currently not supported).

The network has provided a resolution for the DebitReversal. If won, a crediting Transaction is created.

The DebitReversal starting state.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit DebitReversals, starting after DebitReversal starting_after. Each entry in the array is a separate DebitReversal object. If no more DebitReversals are available, the resulting array will be empty.
