htmlMoving money with Treasury using InboundTransfer objects | Stripe Documentation[Skip to content](#main-content)Moving money with Treasury using InboundTransfer objects[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoving-money%2Ffinancial-accounts%2Finto%2Finbound-transfers)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoving-money%2Ffinancial-accounts%2Finto%2Finbound-transfers)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)[Treasury](#)
[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Treasury](/treasury)·[Home](/docs)[Banking as a service](/docs/financial-services)[Treasury](/docs/treasury)[Moving money into financial accounts](/docs/treasury/moving-money/moving-money-into-financial-accounts)# Moving money with Treasury using InboundTransfer objects

Learn how to transfer money from another account you own into a Treasury financial account.Inbound transfers move money from an external US bank account into a financial account using the ACH network. These transfers are initiated with InboundTransfer objects.

Inbound transfers take 2-4 business days to complete unless you’re using the Same Day ACH capability. See the Money movement timelines guide for more information.

NoteYou can use inbound transfers to move funds from a financial account owner’s bank account. To accept funds from an external party into a financial account, use an ACH Debit into the Payments balance, followed by a payout to the financial account.

[Create an InboundTransfer](#createibt)Use POST /v1/treasury/inbound_transfers to create an InboundTransfer object, which represents pull-based transfers from an external account that you own into your financial account. In other words, you create an InboundTransfer to move funds into your financial account by debiting your external US bank account. You must include the following parameters with your request:

- `amount`: The amount in cents to be transferred into the financial account.
- `currency`: Three-letter ISO currency code (`usd`is currently the only supported value).
- `financial_account`: The ID of the financial account receiving the transfer.
- `origin_payment_method`: The source of funds for the inbound transfer. You must first set up the account-attached payment method for inbound flows and verify the bank account using a[SetupIntent](/api/setup_intents). Alternatively, you can use an existing[BankAccount](/api/customer_bank_accounts)previously set up as a verified[ExternalAccount](/api/external_accounts). Whether you use a payment method or a bank account, you need the[user’s permission](/treasury/moving-money/working-with-bankaccount-objects)to debit the funds from the account.

The following JSON shows the data you can include in the body of your request.

`{
  // The source PaymentMethod or BankAccount. Funds are pulled from this account.
  "origin_payment_method": "{{PAYMENT_METHOD_ID}}" | "{{BANK_ACCOUNT_ID}}",
  // The destination FinancialAccount. Funds arrive in this account.
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
  // The amount to debit. 10.00 USD in this case.
  "amount": 1000,
  "currency": "usd",
  // An optional, internal description for the InboundTransfer.
  "description": "Funds for vendor payment payment_234281",
  // An optional descriptor for the InboundTransfer to send
  // to the network with the debit request. Max 10 characters
  "statement_descriptor": "payment_1",
  // Stripe does not support updating InboundTransfers after creation.
  // You can only set metadata at creation time.
  "metadata": null | {{Hash}}
}`The following request transfers 200 USD using an account-attached payment method into the financial account with the provided ID. The Stripe-Account header value identifies the Stripe account that owns both the financial account and the payment method.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/inbound_transfers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d origin_payment_method={{PAYMENT_METHOD_ID}} \
  -d financial_account={{FINANCIAL_ACCOUNT_ID}} \
  -d amount=20000 \
  -d currency=usd \
  -d description="Funds for repair" \
  -d statement_descriptor="Invoice 12"`If successful, the response provides the InboundTransfer object. The object includes a hosted_regulatory_receipt_url that provides access to details of the transaction for the account holder on your platform.

`{
    "id": "{{INBOUND_TRANSFER_ID}}",
    "object": "inbound_transfer",
    "amount": 20000,
    "created": 1648071297,
    "currency": "usd",
    "description": "Funds for repair",
    "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
    "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/{{IBT_URL}}",
    "linked_flows": null,
    "livemode": false,
    "metadata": {},
    "origin_payment_method": "{{PAYMENT_METHOD_ID}}",
    ...
    "statement_descriptor": "Invoice 12",
    "status": "processing",
    ...
}`Note Same Day ACH beta The optional origin_payment_method_options[us_bank_account][ach][submission]=same_day parameter enables funds to arrive in the originating financial account within the same business day if the InboundTransfer call successfully completed before the cut off time. If this parameter isn’t included when creating an InboundTransfer, the transaction uses the default money movement timeline. Include destination_payment_method_options[us_bank_account][network]=ach when using this feature. Reach out to treasury-support@stripe.com to join the Same Day ACH beta waitlist.

[Retrieve an InboundTransfer](#getibt)Use GET /v1/treasury/inbound_transfers/{{INBOUND_TRANSFER_ID}} to retrieve the InboundTransfer object with the associated ID.

The following JSON shows the data you can include in the body of your request. Some of the parameters in the response have additional details that are only returned when you add them as values to the expand[] parameter. The fields that you can expand have an “Expandable” comment in the following response example. See Expanding Responses to learn more about expanding object responses.

`{
  "id": "{{INBOUND_TRANSFER_ID}}",
  "object": "inbound_transfer",
  "livemode": false,
  "created": "{{Timestamp}}",
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}", // Expandable
  "amount": 1000,
  "currency": "usd",
  // The only current valid PaymentMethod type for InboundTransfers is us_bank_account
  "origin_payment_method": "{{PAYMENT_METHOD_ID}}",`See all 52 linesThe following request retrieves the InboundTransfer with the id value of {{INBOUND_TRANSFER_ID}}. Including transaction in the expand[] array of the body returns the relevant expanded information.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/treasury/inbound_transfers/{{INBOUND_TRANSFER_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "expand[]"=financial_account`If successful, the response returns the InboundTransfer object with the expanded information.

`{
    "id": "{{INBOUND_TRANSFER_ID}}",
    "object": "inbound_transfer",
    "amount": 20000,
    "created": 1648071297,
    "currency": "usd",
    "description": "Inbound transfer",
    "failure_details": null,
    "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
    "hosted_regulatory_receipt_url": "https://payments.stripe.com/regulatory-receipt/{{INBOUND_TRANSFER_ID}}",`See all 78 lines[List InboundTransfers](#listibt)Use GET /v1/treasury/inbound_transfers to retrieve all the InboundTransfers for the financial account with the associated ID. You can filter the list with the standard list parameters or by status.

`{
  // Standard list parameters
  "limit", "starting_after", "ending_before",
  // Filter by status
  "status": "processing" | "succeeded" | "failed",
  // Filter by FinancialAccount (Required)
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}", // Required
}`The following request retrieves all the inbound transfers with a status of succeeded for the financial account with ID {{FINANCIAL_ACCOUNT_ID}}, which is attached to the connected account with ID {{CONNECTED_ACCOUNT_ID}}.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/treasury/inbound_transfers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d financial_account={{FINANCIAL_ACCOUNT_ID}} \
  -d status=succeeded`[InboundTransfer states](#ibtstates)The following table describes each status and what the possible transition states are.

STATUSDESCRIPTIONTRANSITIONS TO STATE`processing`The`InboundTransfer`creation succeeded. Stripe instructs movement of funds on the network.`failed`,`canceled`,`succeeded``failed`(terminal)The`InboundTransfer`failed to confirm. No transaction was created, and the`payment_method`hasn’t been debited.N/A`canceled`(terminal)The`InboundTransfer`was canceled prior to submission to the network. Stripe voids the transaction and no funds are moved from the external bank account.N/A`succeeded`(terminal)The`InboundTransfer`succeeded and funds have landed in the account. A Transaction has been created. InboundTransfers can be returned after succeeding if the external account pulls back their funds, which is represented by a linked ReceivedDebit.N/A[Testing InboundTransfers](#testingibts)To test your integration end-to-end, use the SetupIntents requests in test mode to create a PaymentMethod, then pass that PaymentMethod into an InboundTransfer creation request. Valid PaymentMethods result in succeeded InboundTransfers, while invalid PaymentMethods (for example, PaymentMethods of unsupported types, PaymentMethods containing an unverified bank account, or PaymentMethods that aren’t setup for inbound flows) throw the same errors as in live mode.

[Testing InboundTransfer states](#testingibtstate)Stripe also provides a set of test PaymentMethod tokens you can use to trigger specific state transitions:

PAYMENT_METHOD VALUERESULT`pm_usBankAccount``InboundTransfer`that transitions from`processing`to`succeeded`.`pm_usBankAccount_processing``InboundTransfer`that remains in the`processing`state.`pm_usBankAccount_internalFailure``InboundTransfer`that transitions from`processing`to`failed`.To test various edge cases more quickly, PaymentMethod tokens simulate specific failure types:

PAYMENT_METHOD VALUERESULT`pm_usBankAccount_noAccount``InboundTransfer`that transitions to failed with`failure_details.code= "no_account"`.`pm_usBankAccount_accountClosed``InboundTransfer`that transitions to`failed`with`failure_details.code= "account_closed"`.`pm_usBankAccount_invalidAccountNumber``InboundTransfer`that transitions to failed with`failure_details.code= "invalid_account_number"`.`pm_usBankAccount_insufficientFunds``InboundTransfer`that transitions to failed with`failure_details.code= "insufficient_funds"`.`pm_usBankAccount_debitNotAuthorized``InboundTransfer`that transitions to failed with`failure_details.code= "debit_not_authorized"`.`pm_usBankAccount_dispute``InboundTransfer`that transitions from`processing`to`succeeded`and is later disputed.`inbound_transfer.returned`becomes`true`, and a linked`ReceivedDebit`is created.In all cases, the InboundTransfer response begins in the processing state. You receive webhooks for each relevant state transition, and fetching the InboundTransfer after creation returns the expected state.

[InboundTransfer test helper endpoints](#ibthelperendpoints)Stripe also provides endpoints that enable you to test InboundTransfers in different states. Create an InboundTransfer, then:

- Use the test succeed endpoint to move the transfer with the associated ID directly into the succeeded state.

POST /v1/test_helpers/treasury/inbound_transfers/{{INBOUND_TRANSFER_ID}}/succeed


- Use the test fail endpoint to move the transfer with the associated ID directly into the failed state.

POST /v1/test_helpers/treasury/inbound_transfers/{{INBOUND_TRANSFER_ID}}/fail



These endpoints are particularly useful when testing error scenarios, such as returns, which would otherwise require action from the external account the InboundTransfer was pulling funds from.

Include the optional failure_details.code parameter in the body to indicate why the transfer failed. If you don’t provide it, the transfer fails with the default could_not_process failure code.

`{
  "failure_details": {
    "code": "account_closed" |
          "account_frozen" |
          "bank_account_restricted" |
          "bank_ownership_changed" |
          "could_not_process" | // Generic fallback code
          "invalid_account_number" |
          "incorrect_account_holder_name" |
          "invalid_currency" |
          "no_account"
  }
}`Treasury also provides a return endpoint to simulate an InboundTransfer that succeeds, but is later returned.

Use the test return endpoint to initiate the simulated return on the InboundTransfer with the associated ID.

POST /v1/test_helpers/treasury/inbound_transfers/{{INBOUND_TRANSFER_ID}}/return

All test endpoints trigger webhooks for each relevant state transition, and fetching the InboundTransfer after transition returns the expected state.

[InboundTransfer webhooks](#ibtwebhooks)Stripe emits the following InboundTransfer events to your webhook endpoint:

- `treasury.inbound_transfer.created`on`InboundTransfer`creation.
- `treasury.inbound_transfer.{{new_status}}`when an`InboundTransfer`changes status. Available status value options include:  - `treasury.inbound_transfer.succeeded`
  - `treasury.inbound_transfer.failed`



Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create an InboundTransfer](#createibt)[Retrieve an InboundTransfer](#getibt)[List InboundTransfers](#listibt)[InboundTransfer states](#ibtstates)[Testing InboundTransfers](#testingibts)[Testing InboundTransfer states](#testingibtstate)[InboundTransfer test helper endpoints](#ibthelperendpoints)[InboundTransfer webhooks](#ibtwebhooks)Products Used[Treasury](/treasury)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`