# Moving money out of Treasury financial accounts

You can use a number of methods to move funds from a Treasury financial account to another account (either an external account or another Treasury financial account):

- Originate an OutboundPayment to move money to a third party’s external account or financial account through ACH, wire transfer, or the Stripe network.

- Originate an OutboundTransfer to move money to an external account belonging to the same user through ACH or wire transfer.

- Initiate a card transaction through Stripe Issuing to send money using card networks.

- Receive a ReceivedDebit (initiated by the owner of an external account) to pull money from the financial account through ACH.

Within Stripe, you can save payment method information using a PaymentMethod object. You might use PaymentMethods to save your vendors’ account data so you don’t have to re-enter and collect their information for every payment you make to them.

[PaymentMethod](/api/payment_methods)

You can attach PaymentMethods containing bank account information to a customer (for sending money to a third party) or to a Stripe account (for sending money to a company’s own external bank account). In both cases, you create the PaymentMethod using SetupIntent endpoints.

[SetupIntent](/payments/setup-intents)

The type of Treasury requests you make with a PaymentMethod depends on how they’re attached:

- For customer-attached, use PaymentIntent and OutboundPayment requests.

- For account-attached, use InboundTransfer and OutboundTransfer requests.

See Working with SetupIntents, PaymentMethods, and BankAccounts for more information.

[Working with SetupIntents, PaymentMethods, and BankAccounts](/treasury/moving-money/working-with-bankaccount-objects)

## Handling returned funds

The destination for OutboundTransfers and OutboundPayments can reject the relative flow. For example, the destination address might not exist and the OutboundTransfer or OutboundPayment fails. This can occur over the ach and us_domestic_wire networks. CreditReversals can also return OutboundPayments over the stripe network. In the case of returned funds, the OutboundTransfer or OutboundPayment transitions to the returned status and Stripe creates a transaction to return the funds to the source financial account. Stripe also triggers a treasury.outbound_transfer.returned or treasury.outbound_payment.returned webhook.

## See also

- Moving money with Treasury using OutboundPayment objects

[Moving money with Treasury using OutboundPayment objects](/treasury/moving-money/financial-accounts/out-of/outbound-payments)

- Moving money with Treasury using OutboundTransfer objects

[Moving money with Treasury using OutboundTransfer objects](/treasury/moving-money/financial-accounts/out-of/outbound-transfers)

- Moving money with Treasury using ReceivedDebit objects

[Moving money with Treasury using ReceivedDebit objects](/treasury/moving-money/financial-accounts/out-of/received-debits)

- Moving money with Treasury using DebitReversal objects

[Moving money with Treasury using DebitReversal objects](/treasury/moving-money/financial-accounts/out-of/debit-reversals)

- Working with Stripe Issuing cards

[Working with Stripe Issuing cards](/treasury/account-management/issuing-cards)
