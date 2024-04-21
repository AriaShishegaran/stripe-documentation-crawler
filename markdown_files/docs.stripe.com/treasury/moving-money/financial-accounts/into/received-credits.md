htmlMoving money with Treasury using ReceivedCredit objects | Stripe Documentation[Skip to content](#main-content)Moving money with Treasury using ReceivedCredit objects[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoving-money%2Ffinancial-accounts%2Finto%2Freceived-credits)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoving-money%2Ffinancial-accounts%2Finto%2Freceived-credits)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)[Treasury](#)
[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Treasury](/treasury)·[Home](/docs)[Banking as a service](/docs/financial-services)[Treasury](/docs/treasury)[Moving money into financial accounts](/docs/treasury/moving-money/moving-money-into-financial-accounts)# Moving money with Treasury using ReceivedCredit objects

Learn how to move money into a Treasury financial account from another Treasury financial account or bank account.When funds move into a financial account, Stripe creates a corresponding ReceivedCredit object on the account. A ReceivedCredit contains information on how the funds were sent and from what account, where possible. You can send funds to a financial account with the account’s routing and account numbers for ach and us_domestic_wire, or the financial account ID for transfers between financial accounts.

When the origin of the funds is another Treasury financial account, the ReceivedCredit contains a linked_flows.source_flow reference to the originating money movement. In this case, the source OutboundPayment has stripe as its network value.

[Retrieve a ReceivedCredit](#retrieverc)Use GET /v1/treasury/received_credits/{{RECEIVED_CREDIT_ID}} to retrieve the ReceivedCredit with the specified ID.

The following request retrieves the ReceivedCredit with the specified ID. The response for this request includes expanded Transaction object details.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/treasury/received_credits/{{RECEIVED_CREDIT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "expand[]"=transaction`If successful, the response provides the requested ReceivedCredit object. Some of the parameters in the response have additional details that are only returned when you add them as values to the expand[] parameter of your request. The fields that you can expand have an Expandable comment in the following response example. See Expanding Responses to learn more about expanding object responses.

[JSON (commented)](#)`{
  "id": "{{RECEIVED_CREDIT_ID}}",
  "object": "received_credit",
  "livemode": true | false,
  "created": "{{Timestamp}}",
  // The FinancialAccount that received the funds
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}", // Expandable
  "amount": 1000,
  "currency": "usd",
  // The description of this movement sent by the originator`See all 79 lines[List ReceivedCredits](#listrc)Use GET /v1/treasury/received_credits to retrieve all of the ReceivedCredits for the financial account with the ID of the required financial_account parameter. You can filter the list with the standard list parameters, by status, or by linked_flows.source_flow_type.

`{
  // Standard list parameters
  "limit", "starting_after", "ending_before",
  // Filter by FinancialAccount (required)
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
  // Filter by status
  "status": "succeeded" | "failed",
  // Filter by `source_flow_type`
  "linked_flows.source_flow_type": nil | "payout" | "outbound_payment"
}`The following request retrieves the ReceivedCredits that have a status of failed for the specified financial account.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/treasury/received_credits \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d financial_account={{FINANCIAL_ACCOUNT_ID}} \
  -d status=failed`If successful, the response includes the ReceivedCredit objects that match the criteria specified in the request.

[Testing ReceivedCredits](#testingrc)Use POST /v1/test_helpers/treasury/received_credits to simulate receiving funds in a financial account. To simulate a bank transfer from an account outside of Stripe to your financial account, set initiating_payment_method_details to the values of the external bank account, and set network to ach or us_domestic_wire.

The following request creates a test mode ReceivedCredit from an external bank account using an OutboundPayment between two financial accounts on the same platform.

Command Line[curl](#)`curl https://api.stripe.com/v1/test_helpers/treasury/received_credits \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d financial_account={{DESTINATION_FINANCIAL_ACCOUNT_ID}} \
  -d network=ach \
  -d amount=1234 \
  -d currency=usd`If successful, the response returns a ReceivedCredit object. The following is an example of a response for a bank transfer.

`{
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
  "network": "ach",
  "amount": "1234",
  "currency": "usd",
  "description": "Test",
  "source_details": {
    "type": "aba",
    "aba": {
      "country": "US",
      "routing_number": "12341234",
      "account_number": "0123456789",
      "account_holder_name": "Jenny Rosen",
    }
  }
}`[ReceivedCredit webhooks](#webhooksrc)Stripe emits the following ReceivedCredit events to your webhook endpoint:

- `treasury.received_credit.created`on`ReceivedCredit`creation.
- `treasury.received_credit.{{new_status}}`when an`ReceivedCredit`changes status. Available status value options include:  - `treasury.received_credit.succeeded`
  - `treasury.received_credit.failed`


- `treasury.received_credit.reversed`on`ReceivedCredit`[reversal](/treasury/moving-money/financial-accounts/into/credit-reversals).

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Retrieve a ReceivedCredit](#retrieverc)[List ReceivedCredits](#listrc)[Testing ReceivedCredits](#testingrc)[ReceivedCredit webhooks](#webhooksrc)Products Used[Treasury](/treasury)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`