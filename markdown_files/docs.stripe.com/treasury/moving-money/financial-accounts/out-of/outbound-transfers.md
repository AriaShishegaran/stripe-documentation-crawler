htmlMoving money with Treasury using OutboundTransfer objects | Stripe Documentation[Skip to content](#main-content)Moving money with Treasury using OutboundTransfer objects[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoving-money%2Ffinancial-accounts%2Fout-of%2Foutbound-transfers)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoving-money%2Ffinancial-accounts%2Fout-of%2Foutbound-transfers)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)[Treasury](#)
[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Treasury](/treasury)·[Home](/docs)[Banking as a service](/docs/financial-services)[Treasury](/docs/treasury)[Moving money out of financial accounts](/docs/treasury/moving-money/moving-money-out-of-financial-accounts)# Moving money with Treasury using OutboundTransfer objects

Learn how to transfer money out of Treasury financial accounts to external accounts.An OutboundTransfer object facilitates money movement out of a financial account. Use OutboundTransfer to send funds over ACH rails or through a domestic wire transfer to an external bank account that a connected account user owns.

Outbound transfers typically arrive at the receiving bank between the same day and 2 business days, depending on whether you use a wire or ACH.

NoteMulti FA beta If enrolled in the Multi FA beta, you can use OutboundTransfer to send funds over stripe network rails to another financial account associated with the same connected account. Funds arrive in the destination financial account within minutes.

Refer to the Money movement timelines guide for more information.

OutboundTransfers support the us_bank_account type of payment method. Alternatively, you can use an existing BankAccount that belongs to the merchant as an ExternalAccount.

[Create an OutboundTransfer](#createobt)Use POST /v1/treasury/outbound_transfers to create an OutboundTransfer for the financial account with the associated ID. Among the request’s possible parameters, four are required:

- `amount`: Amount of transfer in cents.
- `currency`: Three-letter ISO currency code.
- `financial_account`: Source financial account ID to pull funds from.
- `destination_payment_method`: Destination`PaymentMethod`ID or`BankAccount`ID to receive funds.

`{
  // The source financial account to pull funds from.
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
  // The amount to send. 10.00 USD in this case.
  "amount": 1000,
  "currency": "usd",
  // The destination PaymentMethod or BankAccount.
  "destination_payment_method": "{{PAYMENT_METHOD_ID}}"  | "{{BANK_ACCOUNT_ID}}",
  // Optionally, to explicitly specify a network, override the `network` value
  "destination_payment_method_options": {
    "us_bank_account": {
      "network": "ach" | "us_domestic_wire"
    }
  },
  // A description visible on the external bank statement.
  "statement_descriptor": "Bank xfer",
  // An optional internal description to identify this OutboundTransfer
  "description": "Transfer to my external account",
  // Stripe does not support updating originated transfers after creation.
  // You can only set metadata at creation.
  "metadata": nil | Hash,
}`The following request creates an OutboundTransfer on an account-attached PaymentMethod with the source of funds coming from the identified financial account.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/outbound_transfers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d financial_account={{FINANCIAL_ACCOUNT_ID}} \
  -d amount=1000 \
  -d currency=usd \
  -d destination_payment_method={{PAYMENT_METHOD_ID}} \
  -d statement_descriptor="Test xfer" \
  -d "destination_payment_method_options[us_bank_account][network]"=ach`NoteSame Day ACH beta Include the optional destination_payment_method_options[us_bank_account][ach][submission]=same_day parameter to send funds through ACH rails that arrive the same business day if the OutboundTransfer call is successfully completed before the cut-off time. If this parameter isn’t included when creating an OutboundPayment, the transaction uses the default money movement timeline. Include destination_payment_method_options[us_bank_account][network]=ach when using this feature. Reach out to treasury-support@stripe.com to join the Same Day ACH beta waitlist.

If successful, the response returns the newly created OutboundTransfer object.

`{
    "id": "{{OUTBOUND_TRANSFER_ID}}",
    "object": "outbound_transfer",
    "amount": 1000,
    "cancelable": true,
    "created": 1648479987,
    "currency": "usd",
    "description": null,
    "destination_payment_method": "{{PAYMENT_METHOD_ID}}",
    "destination_payment_method_details": {`See all 50 lines### Wire transfer: Routing numbers

Some banks might use a separate wire transfer routing number that differs from ACH. Consequently, you might receive an error during wire creation if the routing number on the payment method doesn’t support wire transfers. If you receive this error, you need to add a new payment method with your bank’s wire routing number.

### Wire transfer: Recipient address

Wire transfers require additional metadata beyond ACH, in particular recipient name and billing address. The address provided should be the address of the accountholder receiving the wire rather than the address of their bank.

When entering the billing_details.address for a payment method, all address fields must be complete. Attempting to send a wire with incomplete fields on the billing_details.address results in an error.

NoteWhen sending a wire using an OutboundTransfer, if you don’t fill out any address fields, Stripe defaults to the legal entity of the primary Stripe account holder.

[Retrieve an OutboundTransfer](#retrieveobt)Use GET /v1/treasury/outbound_transfers/{{OUTBOUND_TRANSFER_ID}} to retrieve details for the OutboundTransfer with the associated ID.

The following request retrieves the OutboundTransfer with the associated ID, expanding the details of the Transaction.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/treasury/outbound_transfers/{{OUTBOUND_TRANSFER_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "expand[]"=transaction`If successful, the response returns the OutboundTransfer object with the associated ID. Some of the parameters in the response have additional details that are only returned when you add them as values to the expand[] parameter. The fields that you can expand have an “Expandable” comment in the following response example. See Expanding Responses to learn more about expanding object responses.

[JSON (commented)](#)`{
  "id": "{{OUTBOUND_TRANSFER_ID}}",
  "object": "outbound_transfer",
  "livemode": Boolean,
  "created": Timestamp,
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}", // Expandable
  "amount": 1000,
  "currency": "usd",
  "destination_payment_method": "{{PAYMENT_METHOD_ID}}",
  "description": "Transfer to my external account",`See all 85 linesTracking Details betaIf you’re enrolled in the Tracking Details beta, the tracking_details field displays the trace ID for ACH transfers or IMAD/OMAD for wire transfers if they’re available. Reach out to treasury-support@stripe.com to join the beta waitlist.

[Cancel an OutboundTransfer](#cancelobt)Use POST /v1/treasury/outbound_transfers/{{OUTBOUND_TRANSFER_ID}}/cancel to cancel the OutboundTransfer with the associated ID. The OutboundTransfer object includes a cancelable parameter with a Boolean value to indicate whether you can cancel the transfer. After an OutboundTransfer submits to the network, the cancelable value becomes false and you receive an error from this endpoint for that transfer.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/treasury/outbound_transfers/{{OUTBOUND_TRANSFER_ID}}/cancel \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"`If successful, the response returns the OutboundTransfer object with a status of canceled.

`{
    "id": "{{OUTBOUND_TRANSFER_ID}} ",
    "object": "outbound_transfer",
    "amount": 1000,
    "cancelable": false,
    "created": 1648487177,
    "currency": "usd",
    ...
    "status": "canceled",
    "status_transitions": {
        "canceled_at": 1648487198,
        "failed_at": null,
        "posted_at": null,
        "returned_at": null
    },
    "transaction": "{{TRANSACTION_ID}}"
}`[List OutboundTransfers](#listobt)Use GET /v1/treasury/outbound_transfers to list the OutboundTransfers sent from the financial account with the ID of the financial_account parameter. You can filter the list with the standard list parameters or by status.

`{
  // Standard list parameters
  "limit", "starting_after", "ending_before",
  // Filter by status
  "status": "processing" | "posted" | "failed" | "returned" | "canceled",
  // Filter by FinancialAccount (Required)
  "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
}`The following request retrieves OutboundTransfers from the financial account identified. The included parameters limit the response to the first three transfers after the OutboundTransfer with the provided ID.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/treasury/outbound_transfers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d financial_account={{FINANCIAL_ACCOUNT_ID}} \
  -d limit=3 \
  -d starting_after={{OUTBOUND_TRANSFER_ID}}`If successful, the response returns a list of OutboundTransfer objects that satisfy any filtering conditions.

[OutboundTransfer states](#statesobt)The following table describes each status for OutboundTransfers and what the possible transition states are.

STATUSDESCRIPTIONTRANSITIONS TO STATE`processing`The`OutboundTransfer`starting state. Funds are allotted to a pending transaction (but are still part of the current balance). The user can cancel the`OutboundTransfer`while the value of the`cancelable`parameter is`true`.`posted`,`canceled`,`failed``canceled`(terminal)A user canceled the`OutboundTransfer`before posting. Stripe voids the pending transaction and returns the funds to the user.N/A`posted`The`OutboundTransfer`has been sent to the network and funds have left the account (with the transaction posting).`returned``returned`(terminal)The`OutboundTransfer`failed to successfully arrive at the destination (for example, due to incorrect account details). Stripe returns the funds to the user with`returned_details[transaction]`.N/A`failed`(terminal)The`OutboundTransfer`failed to be sent to the network. Stripe voids the pending transaction and returns the funds to the user. Stripe might use this state to indicate internal errors.N/A[Testing OutboundTransfers](#testingobt)In test mode, you can specify the destination_payment_method as a test mode payment method. You can create your own test mode PaymentMethods or use our test IDs when testing your integration.

TYPEOUTCOMEPAYMENT METHOD`us_bank_account`Default, transitions to`posted`.`pm_usBankAccount``us_bank_account`Transitions to`posted`, adds one day to the original`expected_arrival_date`.`pm_usBankAccount_expectedArrivalDateUpdated``us_bank_account`Remains in`processing`.`pm_usBankAccount_processing``us_bank_account`Transitions to`canceled`.`pm_usBankAccount_canceledByUser``us_bank_account`Transitions to`failed`.`pm_usBankAccount_internalFailure``us_bank_account`Transitions to`returned`with`returned_details.code="no_account"`.`pm_usBankAccount_noAccount``us_bank_account`Transitions to`returned`with`returned_details.code="account_closed"`.`pm_usBankAccount_accountClosed``us_bank_account`Transitions to`returned`with`returned_details.code="invalid_account_number"`.`pm_usBankAccount_invalidAccountNumber`In all cases, the OutboundTransfer response is in the processing state. Stripe triggers webhooks for the relevant state transitions, and fetching the OutboundTransfer after creation returns the expected state.

### OutboundTransfer test helper endpoints

Stripe provides endpoints to help you test OutboundTransfers in different states. After creating an OutboundTransfer, use these endpoints to move the OutboundTransfer directly to a new state of posted, failed, canceled, or returned.

- Use the test post endpoint to move the identified OutboundTransfer from processing to posted.

POST /v1/test_helpers/treasury/outbound_transfers/{{OUTBOUND_TRANSFER_ID}}/post


- Use the test fail endpoint to move the identified OutboundTransfer from processing to failed.

POST /v1/test_helpers/treasury/outbound_transfers/{{OUTBOUND_TRANSFER_ID}}/fail


- Use the test return endpoint to move the identified OutboundTransfer from posted to returned.

POST /v1/test_helpers/treasury/outbound_transfers/{{OUTBOUND_TRANSFER_ID}}/return



These endpoints are particularly useful when testing error scenarios, such as returns, which would otherwise require outside action.

For the return endpoint, include the optional returned_details.code parameter in the body to indicate why the transfer was returned. If not provided, the transfer defaults to the declined return code.

`{
  "returned_details": {
    "code": "account_closed" |
          "account_frozen" |
          "bank_account_restricted" |
          "bank_ownership_changed" |
          "could_not_process" |
          "invalid_account_number" |
          "incorrect_account_holder_name" |
          "invalid_currency" |
          "no_account" |
          "declined"
  }
}`In all cases, Stripe triggers webhooks for each relevant state transition, and fetching the OutboundTransfer after transition returns the expected state.

[OutboundTransfer webhooks](#obtwebhooks)Stripe emits the following OutboundTransfer events to your webhook endpoint:

- `treasury.outbound_transfer.created`on OutboundTransfer creation.
- `treasury.outbound_transfer.{{new_status}}`when an OutboundTransfer changes status. Available status value options include:  - `treasury.outbound_transfer.posted`
  - `treasury.outbound_transfer.failed`
  - `treasury.outbound_transfer.returned`
  - `treasury.outbound_transfer.canceled`


- `treasury.outbound_transfer.expected_arrival_date_updated`when the`expected_arrival_date`of an OutboundTransfer changes.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create an OutboundTransfer](#createobt)[Retrieve an OutboundTransfer](#retrieveobt)[Cancel an OutboundTransfer](#cancelobt)[List OutboundTransfers](#listobt)[OutboundTransfer states](#statesobt)[Testing OutboundTransfers](#testingobt)[OutboundTransfer webhooks](#obtwebhooks)Products Used[Treasury](/treasury)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`