- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Received Credits

[Received Credits](/api/treasury/received_credits)

ReceivedCredits represent funds sent to a FinancialAccount (for example, via ACH or wire). These money movements are not initiated from the FinancialAccount.

[FinancialAccount](#financial_accounts)

[GET/v1/treasury/received_credits/:id](/api/treasury/received_credits/retrieve)

[GET/v1/treasury/received_credits](/api/treasury/received_credits/list)

[POST/v1/test_helpers/treasury/received_credits](/api/treasury/received_credits/test_mode_create)

# The ReceivedCredit object

[The ReceivedCredit object](/api/treasury/received_credits/object)

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

- failure_codenullable enumReason for the failure. A ReceivedCredit might fail because the receiving FinancialAccount is closed or frozen.Possible enum valuesaccount_closedFunds can’t be sent to a closed FinancialAccount.account_frozenFunds can’t be sent to a frozen FinancialAccount.otherFunds can’t be sent to FinancialAccount for other reasons.

Reason for the failure. A ReceivedCredit might fail because the receiving FinancialAccount is closed or frozen.

Funds can’t be sent to a closed FinancialAccount.

Funds can’t be sent to a frozen FinancialAccount.

Funds can’t be sent to FinancialAccount for other reasons.

- financial_accountnullable stringThe FinancialAccount that received the funds.

The FinancialAccount that received the funds.

- hosted_regulatory_receipt_urlnullable stringA hosted transaction receipt URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

A hosted transaction receipt URL that is provided when money movement is considered regulated under Stripe’s money transmission licenses.

[hosted transaction receipt](/treasury/moving-money/regulatory-receipts)

- initiating_payment_method_detailsobjectDetails about the PaymentMethod used to send a ReceivedCredit.Show child attributes

Details about the PaymentMethod used to send a ReceivedCredit.

- linked_flowsobjectOther flows linked to a ReceivedCredit.Show child attributes

Other flows linked to a ReceivedCredit.

- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.

Has the value true if the object exists in live mode or the value false if the object exists in test mode.

- networkenumThe rails used to send the funds.Possible enum valuesachcardstripeus_domestic_wire

The rails used to send the funds.

- reversal_detailsnullable objectDetails describing when a ReceivedCredit may be reversed.Show child attributes

Details describing when a ReceivedCredit may be reversed.

- statusenumStatus of the ReceivedCredit. ReceivedCredits are created either succeeded (approved) or failed (declined). If a ReceivedCredit is declined, the failure reason can be found in the failure_code field.Possible enum valuesfailedThe ReceivedCredit was declined, and no Transaction was created.succeededThe ReceivedCredit was approved.

Status of the ReceivedCredit. ReceivedCredits are created either succeeded (approved) or failed (declined). If a ReceivedCredit is declined, the failure reason can be found in the failure_code field.

The ReceivedCredit was declined, and no Transaction was created.

The ReceivedCredit was approved.

- transactionnullable stringExpandableThe Transaction associated with this object.

The Transaction associated with this object.

# Retrieve a ReceivedCredit

[Retrieve a ReceivedCredit](/api/treasury/received_credits/retrieve)

Retrieves the details of an existing ReceivedCredit by passing the unique ReceivedCredit ID from the ReceivedCredit list.

No parameters.

Returns a ReceivedCredit object.

# List all ReceivedCredits

[List all ReceivedCredits](/api/treasury/received_credits/list)

Returns a list of ReceivedCredits.

- financial_accountstringRequiredThe FinancialAccount that received the funds.

The FinancialAccount that received the funds.

- linked_flowsobjectOnly return ReceivedCredits described by the flow.Show child parameters

Only return ReceivedCredits described by the flow.

- statusenumOnly return ReceivedCredits that have the given status: succeeded or failed.Possible enum valuesfailedThe ReceivedCredit was declined, and no Transaction was created.succeededThe ReceivedCredit was approved.

Only return ReceivedCredits that have the given status: succeeded or failed.

The ReceivedCredit was declined, and no Transaction was created.

The ReceivedCredit was approved.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit ReceivedCredits, starting after ReceivedCredit starting_after. Each entry in the array is a separate ReceivedCredit object. If no more ReceivedCredits are available, the resulting array will be empty.

# Test mode: Create a ReceivedCreditTest helper

[Test mode: Create a ReceivedCredit](/api/treasury/received_credits/test_mode_create)

Use this endpoint to simulate a test mode ReceivedCredit initiated by a third party. In live mode, you can’t directly create ReceivedCredits initiated by third parties.

- amountintegerRequiredAmount (in cents) to be transferred.

Amount (in cents) to be transferred.

- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- financial_accountstringRequiredThe FinancialAccount to send funds to.

The FinancialAccount to send funds to.

- networkenumRequiredSpecifies the network rails to be used. If not set, will default to the PaymentMethod’s preferred network. See the docs to learn more about money movement timelines for each network type.

Specifies the network rails to be used. If not set, will default to the PaymentMethod’s preferred network. See the docs to learn more about money movement timelines for each network type.

[docs](/treasury/money-movement/timelines)

- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- initiating_payment_method_detailsobjectInitiating payment method details for the object.Show child parameters

Initiating payment method details for the object.

A test mode ReceivedCredit object.
