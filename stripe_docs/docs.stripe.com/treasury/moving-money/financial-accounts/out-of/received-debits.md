# Moving money with Treasury using ReceivedDebit objects

Certain processes initiated outside of Stripe Treasury result in money being pulled out of a Treasury financial account. This includes:

- Spending money on a card through Stripe Issuing

[Stripe Issuing](/issuing/purchases/transactions#using-with-stripe-treasury)

- Pulling money out of a financial account into an external account using ACH debits

- Pulling money out of a platform’s financial account into that platform’s Stripe Payments balance using top-ups

[top-ups](/treasury/moving-money/payouts#top-ups)

These money movements result in the creation of ReceivedDebit objects. You don’t create ReceivedDebits directly, rather you observe ReceivedDebit object creation with webhooks. If there are insufficient funds in the account, the ReceivedDebit fails in most cases.

[Retrieving a ReceivedDebit](#retrieverecdeb)

## Retrieving a ReceivedDebit

Use GET /v1/treasury/received_debits/{{RECEIVED_DEBIT_ID}} to retrieve the ReceivedDebit with the associated ID.

If successful, the response returns the ReceivedDebit object with the associated ID. Some of the parameters in the response have additional details that are only returned when you add them as values to the expand[] parameter. The fields that you can expand have an “Expandable” comment in the following response example. See Expanding Responses to learn more about expanding object responses.

[Expanding Responses](/api/expanding_objects)

[Listing ReceivedDebits](#listrecdeb)

## Listing ReceivedDebits

Use GET /v1/treasury/received_debits to retrieve all ReceivedDebits for a financial account. You must specify a financial account ID for the financial_account parameter. You can filter the results by the standard list parameters or by status.

The following request retrieves the last successful ReceivedDebit object that occurred before the provided ReceivedDebit for the financial account identified.

[ReceivedDebit object](/api/treasury/received_debits/object)

[Testing ReceivedDebits](#test-received-debit)

## Testing ReceivedDebits

Stripe Treasury provides test endpoints for ReceivedDebit objects. Use POST /v1/test_helpers/treasury/received_debits to simulate ReceivedDebit creation in test mode. You can’t create ReceivedDebit objects in live mode, so using this endpoint enables you to test the flow of funds when a third party initiates creation of a ReceivedDebit. Set financial_account to the ID of the financial account to send money from. Set network to ach and optionally provide the ABA financial address details for the source_details.aba parameter. As in live mode, test mode ReceivedDebits fail if there are insufficient funds available.

[ReceivedDebit webhooks](#webhookrecdeb)

## ReceivedDebit webhooks

Stripe emits the following ReceivedDebit events to your webhook endpoint:

[webhook](/webhooks)

- treasury.received_debit.created on ReceivedDebit creation.
