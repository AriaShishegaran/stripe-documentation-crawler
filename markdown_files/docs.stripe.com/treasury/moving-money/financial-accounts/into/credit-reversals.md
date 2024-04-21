htmlMoving money with Treasury using CreditReversal objects | Stripe Documentation[Skip to content](#main-content)Moving money with Treasury using CreditReversal objects[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoving-money%2Ffinancial-accounts%2Finto%2Fcredit-reversals)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoving-money%2Ffinancial-accounts%2Finto%2Fcredit-reversals)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)[Treasury](#)
[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Treasury](/treasury)·[Home](/docs)[Banking as a service](/docs/financial-services)[Treasury](/docs/treasury)[Moving money into financial accounts](/docs/treasury/moving-money/moving-money-into-financial-accounts)# Moving money with Treasury using CreditReversal objects

Learn how you can return funds from received credits that add money to your Treasury financial account.Reversing a ReceivedCredit creates a CreditReversal. You can reverse ReceivedCredits only in some scenarios (detailed in the following table). Whether you can reverse a ReceivedCredit depends on the network and source flow.

The reversal_details sub-hash on the ReceivedCredit object can have the following combination of values, which determines if you can reverse the ReceivedCredit.

RESTRICTED REASONDEADLINE (EPOCH TIMESTAMP)EXAMPLE SCENARIO`source_flow_restricted``null`A Stripe network`ReceivedCredit`that’s the result of a flow other than an`OutboundPayment`. Stripe restricts users from reversing such`ReceivedCredits`.`network_restricted``null`Network constraints prevent Stripe from allowing reversal on some`ReceivedCredits`, such as a`ReceivedCredit`from a wire transfer.`null``{{TIMESTAMP}}`A`ReceivedCredit`, which is reversible, but only until the timestamp in`deadline`. ACH`ReceivedCredits`have a deadline that determines how long you have to reverse them.`deadline_passed``{{TIMESTAMP}}`A`ReceivedCredit`that’s reversible before the timestamp in`deadline`, but is no longer reversible because the`deadline`has passed. ACH`ReceivedCredits`have a limited time of when they’re reversible after they’re created.`already_reversed``null`A`ReceivedCredit`that’s already reversed has this`restricted_reason`. It might have a non-null`deadline`value.`null``null`You can reverse`ReceivedCredits`anytime if they have`null`for both`restricted_reason`and`deadline`.[Creating a CreditReversal](#createrc)Use POST /v1/treasury/credit_reversals to create a CreditReversal. Set the received_credit parameter in the body of the request to the value of the ReceivedCredit ID to reverse.

NoteYou can’t update CreditReversals, so you must set any optional metadata on creation.

The following request creates a CreditReversal based on the ReceivedCredit ID value on the required received_credit parameter. The request also sets an optional metadata value.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/credit_reversals \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d received_credit={{RECEIVED_CREDIT_ID}} \
  -d "metadata[reason]"=Because`If successful, the response returns the new CreditReversal object.

`{
    "id": "{{CREDIT_REVERSAL_ID}}",
    "object": "credit_reversal",
    "amount": 1000,
    "currency": "usd",
    "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
    "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/{{URL_ID}}",
    "livemode": false,
    "metadata": {
        "csr_id": "CSR-12"`See all 19 lines[Retrieve a CreditReversal](#retrievecr)Use GET /v1/treasury/credit_reversals/{{CREDIT_REVERSAL_ID}} to retrieve the CreditReversal with the associated ID.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/credit_reversals/{{CREDIT_REVERSAL_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"`The response returns the specific CreditReversal object.

[JSON (commented)](#)`{
  "id": "{{CREDIT_REVERSAL_ID}}",
  "object": "credit_reversal",
  "livemode": "{{Boolean}}",
  "created": "{{Timestamp}}",
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
  "amount": 1000,
  "currency": "usd",
  // The ReceivedCredit that was reversed
  "received_credit": "{{RECEIVED_CREDIT_ID}}",
  // The rails used to reversed. Always the same as that of the ReceivedCredit
  "network": "ach" | "stripe",
  "status": "processing" | "posted",
  "status_transitions": {
    "posted_at": null | "{{Timestamp}}",
  },
  // Transaction representing balance impact of the CreditReversal
  "transaction": "{{TRANSACTION_ID}}",
  // A unique, Stripe-hosted direct link to the regulatory receipt for the CreditReversal
  "hosted_regulatory_receipt_url": "{{Url}}",
  // A map of String-String intended for users to use custom data
  "metadata": {},
}`[List CreditReversals](#listcr)Use GET /v1/treasury/credit_reversals to retrieve a list of CreditReversals for the financial account with the ID provided in the required financial_account parameter. You can filter the list by standard list parameters, status, or by ReceivedCredit ID using the received_credit parameter.

`{
  // Standard list parameters
  "limit", "starting_after", "ending_before",
  // Filter by status
  "status": "processing" | "posted",
  // Filter by FinancialAccount (Required)
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
  // Filter by ReceivedCredit
  "received_credit": "{{RECEIVED_CREDIT_ID}}"
}`The following request returns the three most recent credit reversals with a status of posted for the specified financial account.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/treasury/credit_reversals \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d limit=3 \
  -d status=posted \
  -d financial_account={{FINANCIAL_ACCOUNT_ID}}`If successful, the response returns the relevant list of CreditReversal objects.

[Testing CreditReversals](#testcr)To test CreditReversals, you must first create test mode ReceivedCredits. Then use POST /v1/treasury/credit_reversals and specify the test mode ReceivedCredit ID in the received_credit parameter to create a test mode CreditReversal.

[CreditReversal Webhooks](#webhookcr)Stripe emits the following CreditReversal events to your webhook endpoint:

- `treasury.credit_reversal.created`on`CreditReversal`creation.
- `treasury.credit_reversal.posted`when the`CreditReversal`posts.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Creating a CreditReversal](#createrc)[Retrieve a CreditReversal](#retrievecr)[List CreditReversals](#listcr)[Testing CreditReversals](#testcr)[CreditReversal Webhooks](#webhookcr)Products Used[Treasury](/treasury)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`