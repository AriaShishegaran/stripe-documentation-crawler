# Moving money with Treasury using CreditReversal objects

Reversing a ReceivedCredit creates a CreditReversal. You can reverse ReceivedCredits only in some scenarios (detailed in the following table). Whether you can reverse a ReceivedCredit depends on the network and source flow.

[ReceivedCredit](/api/treasury/received_credits)

[CreditReversal](/api/treasury/credit_reversals)

The reversal_details sub-hash on the ReceivedCredit object can have the following combination of values, which determines if you can reverse the ReceivedCredit.

[Creating a CreditReversal](#createrc)

## Creating a CreditReversal

Use POST /v1/treasury/credit_reversals to create a CreditReversal. Set the received_credit parameter in the body of the request to the value of the ReceivedCredit ID to reverse.

You can’t update CreditReversals, so you must set any optional metadata on creation.

[metadata](/api/treasury/credit_reversals/create#create_credit_reversal-metadata)

The following request creates a CreditReversal based on the ReceivedCredit ID value on the required received_credit parameter. The request also sets an optional metadata value.

If successful, the response returns the new CreditReversal object.

[Retrieve a CreditReversal](#retrievecr)

## Retrieve a CreditReversal

Use GET /v1/treasury/credit_reversals/{{CREDIT_REVERSAL_ID}} to retrieve the CreditReversal with the associated ID.

The response returns the specific CreditReversal object.

[List CreditReversals](#listcr)

## List CreditReversals

Use GET /v1/treasury/credit_reversals to retrieve a list of CreditReversals for the financial account with the ID provided in the required financial_account parameter. You can filter the list by standard list parameters, status, or by ReceivedCredit ID using the received_credit parameter.

The following request returns the three most recent credit reversals with a status of posted for the specified financial account.

If successful, the response returns the relevant list of CreditReversal objects.

[CreditReversal objects](/api/treasury/credit_reversals)

[Testing CreditReversals](#testcr)

## Testing CreditReversals

To test CreditReversals, you must first create test mode ReceivedCredits. Then use POST /v1/treasury/credit_reversals and specify the test mode ReceivedCredit ID in the received_credit parameter to create a test mode CreditReversal.

[test mode ReceivedCredits](#testingrc)

[CreditReversal Webhooks](#webhookcr)

## CreditReversal Webhooks

Stripe emits the following CreditReversal events to your webhook endpoint:

[webhook](/webhooks)

- treasury.credit_reversal.created on CreditReversal creation.

- treasury.credit_reversal.posted when the CreditReversal posts.
