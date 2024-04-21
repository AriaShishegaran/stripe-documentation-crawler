# Moving money with Treasury using ReceivedCredit objects

When funds move into a financial account, Stripe creates a corresponding ReceivedCredit object on the account. A ReceivedCredit contains information on how the funds were sent and from what account, where possible. You can send funds to a financial account with the account’s routing and account numbers for ach and us_domestic_wire, or the financial account ID for transfers between financial accounts.

[ReceivedCredit](/api/treasury/received_credits)

When the origin of the funds is another Treasury financial account, the ReceivedCredit contains a linked_flows.source_flow reference to the originating money movement. In this case, the source OutboundPayment has stripe as its network value.

[Retrieve a ReceivedCredit](#retrieverc)

## Retrieve a ReceivedCredit

Use GET /v1/treasury/received_credits/{{RECEIVED_CREDIT_ID}} to retrieve the ReceivedCredit with the specified ID.

[ReceivedCredit](/api/treasury/received_credits)

The following request retrieves the ReceivedCredit with the specified ID. The response for this request includes expanded Transaction object details.

[Transaction object](/api/treasury/transactions)

If successful, the response provides the requested ReceivedCredit object. Some of the parameters in the response have additional details that are only returned when you add them as values to the expand[] parameter of your request. The fields that you can expand have an Expandable comment in the following response example. See Expanding Responses to learn more about expanding object responses.

[Expanding Responses](/api/expanding_objects)

[List ReceivedCredits](#listrc)

## List ReceivedCredits

Use GET /v1/treasury/received_credits to retrieve all of the ReceivedCredits for the financial account with the ID of the required financial_account parameter. You can filter the list with the standard list parameters, by status, or by linked_flows.source_flow_type.

The following request retrieves the ReceivedCredits that have a status of failed for the specified financial account.

If successful, the response includes the ReceivedCredit objects that match the criteria specified in the request.

[ReceivedCredit](/api/treasury/received_credits)

[Testing ReceivedCredits](#testingrc)

## Testing ReceivedCredits

Use POST /v1/test_helpers/treasury/received_credits to simulate receiving funds in a financial account. To simulate a bank transfer from an account outside of Stripe to your financial account, set initiating_payment_method_details to the values of the external bank account, and set network to ach or us_domestic_wire.

The following request creates a test mode ReceivedCredit from an external bank account using an OutboundPayment between two financial accounts on the same platform.

If successful, the response returns a ReceivedCredit object. The following is an example of a response for a bank transfer.

[ReceivedCredit webhooks](#webhooksrc)

## ReceivedCredit webhooks

Stripe emits the following ReceivedCredit events to your webhook endpoint:

[webhook](/webhooks)

- treasury.received_credit.created on ReceivedCredit creation.

- treasury.received_credit.{{new_status}} when an ReceivedCredit changes status. Available status value options include:treasury.received_credit.succeededtreasury.received_credit.failed

- treasury.received_credit.succeeded

- treasury.received_credit.failed

- treasury.received_credit.reversed on ReceivedCredit reversal.

[reversal](/treasury/moving-money/financial-accounts/into/credit-reversals)
