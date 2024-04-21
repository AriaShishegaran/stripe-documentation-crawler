htmlMoving money with Treasury using ReceivedDebit objects | Stripe Documentation[Skip to content](#main-content)Moving money with Treasury using ReceivedDebit objects[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoving-money%2Ffinancial-accounts%2Fout-of%2Freceived-debits)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoving-money%2Ffinancial-accounts%2Fout-of%2Freceived-debits)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)[Treasury](#)
[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Treasury](/treasury)·[Home](/docs)[Banking as a service](/docs/financial-services)[Treasury](/docs/treasury)[Moving money out of financial accounts](/docs/treasury/moving-money/moving-money-out-of-financial-accounts)# Moving money with Treasury using ReceivedDebit objects

Learn how external account holders can pull funds from a Treasury financial account.Certain processes initiated outside of Stripe Treasury result in money being pulled out of a Treasury financial account. This includes:

- Spending money on a card through[Stripe Issuing](/issuing/purchases/transactions#using-with-stripe-treasury)
- Pulling money out of a financial account into an external account using ACH debits
- Pulling money out of a platform’s financial account into that platform’s Stripe Payments balance using[top-ups](/treasury/moving-money/payouts#top-ups)

These money movements result in the creation of ReceivedDebit objects. You don’t create ReceivedDebits directly, rather you observe ReceivedDebit object creation with webhooks. If there are insufficient funds in the account, the ReceivedDebit fails in most cases.

[Retrieving a ReceivedDebit](#retrieverecdeb)Use GET /v1/treasury/received_debits/{{RECEIVED_DEBIT_ID}} to retrieve the ReceivedDebit with the associated ID.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/received_debits/{{RECEIVED_DEBIT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"`If successful, the response returns the ReceivedDebit object with the associated ID. Some of the parameters in the response have additional details that are only returned when you add them as values to the expand[] parameter. The fields that you can expand have an “Expandable” comment in the following response example. See Expanding Responses to learn more about expanding object responses.

[JSON (commented)](#)`{
  "id": "{{RECEIVED_DEBIT_ID}}",
  "object": "received_debit",
  "livemode": Boolean,
  "created": Timestamp,
  // The FinancialAccount funds have been pulled from
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}", // Expandable
  "amount": 1000,
  "currency": "usd",
  "description": "Testing",`See all 71 lines[Listing ReceivedDebits](#listrecdeb)Use GET /v1/treasury/received_debits to retrieve all ReceivedDebits for a financial account. You must specify a financial account ID for the financial_account parameter. You can filter the results by the standard list parameters or by status.

`{
  // Standard list parameters
  "limit", "starting_after", "ending_before",
  // Filter by FinancialAccount (Required)
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
  // Filter by status
  "status": "succeeded" | "failed"
}`The following request retrieves the last successful ReceivedDebit object that occurred before the provided ReceivedDebit for the financial account identified.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/treasury/received_debits \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d financial_account={{FINANCIAL_ACCOUNT_ID}} \
  -d limit=1 \
  -d ending_before={{RECEIVED_DEBIT_ID}}`[Testing ReceivedDebits](#test-received-debit)Stripe Treasury provides test endpoints for ReceivedDebit objects. Use POST /v1/test_helpers/treasury/received_debits to simulate ReceivedDebit creation in test mode. You can’t create ReceivedDebit objects in live mode, so using this endpoint enables you to test the flow of funds when a third party initiates creation of a ReceivedDebit. Set financial_account to the ID of the financial account to send money from. Set network to ach and optionally provide the ABA financial address details for the source_details.aba parameter. As in live mode, test mode ReceivedDebits fail if there are insufficient funds available.

[ReceivedDebit webhooks](#webhookrecdeb)Stripe emits the following ReceivedDebit events to your webhook endpoint:

- `treasury.received_debit.created`on`ReceivedDebit`creation.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Retrieving a ReceivedDebit](#retrieverecdeb)[Listing ReceivedDebits](#listrecdeb)[Testing ReceivedDebits](#test-received-debit)[ReceivedDebit webhooks](#webhookrecdeb)Products Used[Treasury](/treasury)[Issuing](/issuing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`