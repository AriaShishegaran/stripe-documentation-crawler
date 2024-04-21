htmlMoving money with Treasury using DebitReversal objects | Stripe Documentation[Skip to content](#main-content)Moving money with Treasury using DebitReversal objects[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoving-money%2Ffinancial-accounts%2Fout-of%2Fdebit-reversals)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoving-money%2Ffinancial-accounts%2Fout-of%2Fdebit-reversals)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)[Treasury](#)
[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Treasury](/treasury)·[Home](/docs)[Banking as a service](/docs/financial-services)[Treasury](/docs/treasury)[Moving money out of financial accounts](/docs/treasury/moving-money/moving-money-out-of-financial-accounts)# Moving money with Treasury using DebitReversal objects

Learn how you can retrieve funds taken out of a Treasury financial account from an external account holder.Returning the funds from a ReceivedDebit creates a DebitReversal. You can get the funds back from a ReceivedDebit in only some scenarios (detailed in the following table). Whether you can return the funds of a ReceivedDebit depends on the network and source flow.

The reversal_details sub-hash on the ReceivedDebit resource can have the following combination of values, which determines whether you can return the ReceivedDebit funds.

RESTRICTED REASONDEADLINE (EPOCH TIMESTAMP)EXAMPLE SCENARIO`null`7940828047A`ReceivedDebit`that you can return funds from, but only until the timestamp in`deadline`. ACH`ReceivedDebits`have a deadline that determines how long you have to return them.`deadline_passed`1629480538A`ReceivedDebit`whose funds were returnable before the timestamp in`deadline`, but is no longer returnable using the API because the`deadline`has passed. ACH`ReceivedDebits`have a limited time of when they’re returnable using the API after they’re created.`already_reversed`nullA`ReceivedDebit`that’s already been returned. It might have a non-null`deadline`value.`source_flow_restricted`nullA`ReceivedDebit`that can’t be returned because its`source_flow`isn’t reversible.### Return deadlines

You have approximately 1 business day to return ACH debits using the API after receipt. After this time, ACH debit funds might still be returnable but funds return isn’t guaranteed. Contact support to request a return of funds if the reversal deadline has passed.

To create returns of ReceivedDebit funds produced by activity on Issuing cards, see the Issuing disputes guide.

[Creating a DebitReversal](#createdebrev)Use POST /v1/treasury/debit_reversals to create a DebitReversal. Specify the ID of the ReceivedDebit to reverse with the received_debit parameter in the body of the request.

NoteYou can’t update DebitReversals, so you must set any optional metadata on creation.

The following request creates a DebitReversal based on the ReceivedDebit ID value on the required received_debit parameter. The request also sets an optional metadata value.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/debit_reversals \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d received_debit={{RECEIVED_DEBIT_ID}} \
  -d "metadata[reason]"=Because`If successful, the response returns the new DebitReversal object.

`{
  "id": "{{DEBIT_REVERSAL_ID}}",
  "object": "debit_reversal",
  "amount": 1000,
  "currency": "usd",
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
  "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/{{URL_ID}}",
  "linked_flows": null,
  "livemode": false,
  "metadata": {},
  "network": "ach",
  "received_debit": "{{RECEIVED_DEBIT_ID}}",
  "resolution": null,
  "status": "processing",
  "status_transitions": {
    "completed_at": null
  },
  "transaction": "{{TRANSACTION_ID}}"
}`[Retrieve a DebitReversal](#retrievedebrev)Use GET /v1/treasury/debit_reversals/{{DEBIT_REVERSAL_ID}} to retrieve the DebitReversal with the associated ID.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/debit_reversals/{{DEBIT_REVERSAL_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"`If successful, the response returns the identified DebitReversal.

[JSON (commented)](#)`{
  "id": "{{DEBIT_REVERSAL_ID}}",
  "object": "debit_reversal",
  "livemode": true | false,
  "created": "{{Timestamp}}",
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
  "amount": 1000,
  "currency": "usd",
  // the ReceivedDebit being returned
  "received_debit": "{{RECEIVED_DEBIT_ID}}",`See all 25 lines[List DebitReversals](#listdebrev)Use GET /v1/treasury/debit_reversals to retrieve a list of DebitReversals for the financial account with the ID provided in the required financial_account parameter. You can filter the list by standard list parameters, status, or by ReceivedDebit ID using the received_debit parameter.

`{
  // Standard list parameters
  "limit", "starting_after", "ending_before",
  // Filter by financial account (Required)
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
  // Filter by `status`
  "status": "processing" | "canceled" | "completed"
  // Filter by ReceivedDebit
  "received_debit": "{{RECEIVED_DEBIT_ID}}",
}`The following request retrieves the last three DebitReversal objects for the identified financial account.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/treasury/debit_reversals \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d financial_account={{FINANCIAL_ACCOUNT_ID}} \
  -d limit=3`[Testing DebitReversals](#testdebrev)To test DebitReversals, you must first create a test mode ReceivedDebit. Afterwards, use POST /v1/treasury/debit_reversals and specify the test mode ReceivedDebit ID in the received_debit parameter to create a test mode DebitReversal.

[DebitReversal webhooks](#webhooksdebrev)Stripe emits the following DebitReversal events to your webhook endpoint:

- `treasury.debit_reversal.created`on`DebitReversal`creation.
- `treasury.debit_reversal.completed`when the`DebitReversal`completes.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Creating a DebitReversal](#createdebrev)[Retrieve a DebitReversal](#retrievedebrev)[List DebitReversals](#listdebrev)[Testing DebitReversals](#testdebrev)[DebitReversal webhooks](#webhooksdebrev)Products Used[Treasury](/treasury)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`