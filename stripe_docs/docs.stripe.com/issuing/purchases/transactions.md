# Issuing transactions

After an authorization is approved and is captured, the status on the authorization is set to closed and a Transaction object is created. This normally happens within 24 hours; however hotels, airlines, and car rental companies are able to capture up to 31 days after authorization.

[authorization](/issuing/purchases/authorizations)

[Transaction](/api#issuing_transaction_object)

When an authorization is captured, two things happen.

- The status on the authorization is set to closed, releasing the purchase amount held by that authorization. A balance transaction of type issuing_authorization_release is created to represent this.

[balance transaction](/reports/balance-transaction-types)

- A new transaction object of type capture is created. The purchase amount is deducted from the balance you’re using for Issuing.

[balance you’re using for Issuing](/issuing/funding/balance)

Spending controls, real time authorization controls, and card status (whether a card is active or not) don’t apply for capture. They can be used to determine whether authorizations are approved, but captures for approved authorizations always succeed.

[Spending controls](/issuing/controls/spending-controls)

[real time authorization controls](/issuing/controls/real-time-authorizations)

## Handling other transactions

In addition to regular transactions, there are a few other cases that you should be ready to handle.

Refunds are transactions with type of refund.

When we create a transaction representing a refund or credit, we try to link it to the original payment authorization. Refunds aren’t necessarily tied to the original payment transaction or authorization, so linking them is an inexact science. As a result, we might link to an unrelated authorization or be unable to link to an authorization at all (for example, if the card is credited rather than refunded). In these cases, the authorization field of the transaction is set to null, and the transaction won’t be linked to the authorization. We process all refunds and credits the same way, regardless of their linkage to a payment authorization.

To simulate the creation of a refund transaction, you can use the Transaction Refund API in the Issuing test helpers.

[Transaction Refund API](/api/issuing/transactions/test_mode_refund)

To create a refund transaction that doesn’t link to an authorization, use the Create Unlinked Refund API in the Issuing test helpers.

[Create Unlinked Refund API](/api/issuing/transactions/test_mode_create_unlinked_refund)
