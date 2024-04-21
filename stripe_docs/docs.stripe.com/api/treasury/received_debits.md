- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Received Debits

[Received Debits](/api/treasury/received_debits)

ReceivedDebits represent funds pulled from a FinancialAccount. These are not initiated from the FinancialAccount.

[FinancialAccount](#financial_accounts)

[GET/v1/treasury/received_debits/:id](/api/treasury/received_debits/retrieve)

[GET/v1/treasury/received_debits](/api/treasury/received_debits/list)

[POST/v1/test_helpers/treasury/received_debits](/api/treasury/received_debits/test_mode_create)

# The ReceivedDebit object

[The ReceivedDebit object](/api/treasury/received_debits/object)

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

- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- failure_codenullable enumReason for the failure. A ReceivedDebit might fail because the FinancialAccount doesn’t have sufficient funds, is closed, or is frozen.Possible enum valuesaccount_closedFunds can’t be pulled from a closed FinancialAccount.account_frozenFunds can’t be pulled from a frozen FinancialAccount.insufficient_fundsThe FinancialAccount doesn’t have a sufficient balance.otherFunds can’t be pulled from the FinancialAccount for other reasons.

Reason for the failure. A ReceivedDebit might fail because the FinancialAccount doesn’t have sufficient funds, is closed, or is frozen.

Funds can’t be pulled from a closed FinancialAccount.

Funds can’t be pulled from a frozen FinancialAccount.

The FinancialAccount doesn’t have a sufficient balance.

Funds can’t be pulled from the FinancialAccount for other reasons.

- financial_accountnullable stringThe FinancialAccount that funds were pulled from.

The FinancialAccount that funds were pulled from.

- hosted_regulatory_receipt_urlnullable stringA hosted transaction receipt URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

A hosted transaction receipt URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

[hosted transaction receipt](/treasury/moving-money/regulatory-receipts)

- initiating_payment_method_detailsobjectDetails about how a ReceivedDebit was created.Show child attributes

Details about how a ReceivedDebit was created.

- linked_flowsobjectOther flows linked to a ReceivedDebit.Show child attributes

Other flows linked to a ReceivedDebit.

- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.

Has the value true if the object exists in live mode or the value false if the object exists in test mode.

- networkenumThe network used for the ReceivedDebit.

The network used for the ReceivedDebit.

- reversal_detailsnullable objectDetails describing when a ReceivedDebit might be reversed.Show child attributes

Details describing when a ReceivedDebit might be reversed.

- statusenumStatus of the ReceivedDebit. ReceivedDebits are created with a status of either succeeded (approved) or failed (declined). The failure reason can be found under the failure_code.Possible enum valuesfailedThe ReceivedDebit was declined, and no Transaction was created.succeededThe ReceivedDebit was approved.

Status of the ReceivedDebit. ReceivedDebits are created with a status of either succeeded (approved) or failed (declined). The failure reason can be found under the failure_code.

The ReceivedDebit was declined, and no Transaction was created.

The ReceivedDebit was approved.

- transactionnullable stringExpandableThe Transaction associated with this object.

The Transaction associated with this object.

# Retrieve a ReceivedDebit

[Retrieve a ReceivedDebit](/api/treasury/received_debits/retrieve)

Retrieves the details of an existing ReceivedDebit by passing the unique ReceivedDebit ID from the ReceivedDebit list

No parameters.

Returns a ReceivedDebit object.

# List all ReceivedDebits

[List all ReceivedDebits](/api/treasury/received_debits/list)

Returns a list of ReceivedDebits.

- financial_accountstringRequiredThe FinancialAccount that funds were pulled from.

The FinancialAccount that funds were pulled from.

- statusenumOnly return ReceivedDebits that have the given status: succeeded or failed.Possible enum valuesfailedThe ReceivedDebit was declined, and no Transaction was created.succeededThe ReceivedDebit was approved.

Only return ReceivedDebits that have the given status: succeeded or failed.

The ReceivedDebit was declined, and no Transaction was created.

The ReceivedDebit was approved.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit ReceivedDebits, starting after ReceivedDebit starting_after. Each entry in the array is a separate ReceivedDebit object. If no more ReceivedDebits are available, the resulting array will be empty.

# Test mode: Create a ReceivedDebitTest helper

[Test mode: Create a ReceivedDebit](/api/treasury/received_debits/test_mode_create)

Use this endpoint to simulate a test mode ReceivedDebit initiated by a third party. In live mode, you can’t directly create ReceivedDebits initiated by third parties.

- amountintegerRequiredAmount (in cents) to be transferred.

Amount (in cents) to be transferred.

- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- financial_accountstringRequiredThe FinancialAccount to pull funds from.

The FinancialAccount to pull funds from.

- networkenumRequiredSpecifies the network rails to be used. If not set, will default to the PaymentMethod’s preferred network. See the docs to learn more about money movement timelines for each network type.

Specifies the network rails to be used. If not set, will default to the PaymentMethod’s preferred network. See the docs to learn more about money movement timelines for each network type.

[docs](/treasury/money-movement/timelines)

- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- initiating_payment_method_detailsobjectInitiating payment method details for the object.Show child parameters

Initiating payment method details for the object.

A test mode ReceivedDebit object.
