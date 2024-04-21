htmlWorking with Treasury financial accounts | Stripe Documentation[Skip to content](#main-content)Working with financial accounts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Faccount-management%2Ffinancial-accounts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Faccount-management%2Ffinancial-accounts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)[Treasury](#)
[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Treasury](/treasury)·[Home](/docs)[Banking as a service](/docs/financial-services)[Treasury](/docs/treasury)# Working with Treasury financial accounts

Learn how to work with financial accounts in Treasury.When you enable Stripe Treasury on your platform, you can add FinancialAccount objects to your platform architecture to enable the efficient storing, sending, and receiving of funds. After you gain API access to Treasury, Stripe attaches a financial account to your platform account and enables you to provision an individual financial account for each eligible Custom connected account on your platform.

NoteMultiple Financial Accounts beta The Multiple Financial Account beta feature enables you to open multiple financial accounts for a single Custom connected account. Contact treasury-support@stripe.com to access test mode for this feature and join the wait list.

Each financial account has its own distinct balance of funds, separate from the balance of the account it’s linked to. For example, the owner of a Custom connected account on your platform might have a 100 EUR connected account balance and a 200 EUR financial account balance. In this scenario, the connected account owner has a sum of 300 EUR spread between their financial account and connected account balances. These two balances remain separate, but the API provides the ability to move money from the connected account balance to the financial account balance.

In the Stripe API, FinancialAccount objects serve as the source and destination of money movement API requests. You request Features through the API to assign to FinancialAccounts that provide additional functionality for the financial accounts on your platform. For example, to enable payment card features on a specific financial account, you send an API request with the FinancialAccount ID for the card_issuing feature. See Financial account features for more information on Feature objects. See the Available features section within that guide to check required connected account capabilities for each Feature.

Before you create financial accounts in live mode for your Treasury integration, we recommend you first create test financial accounts in test mode. Test mode financial accounts can’t receive or send real money, can’t be used in live mode, and don’t generate a live account with real routing and account information, but are otherwise identical in configuration and functionality.

## Create a FinancialAccount

Use POST /v1/treasury/financial_accounts to create FinancialAccounts. Include the connected account ID as the value of the Stripe-Account header of the call to associate the FinancialAccount with a connected account. Currently, each connected account can only have one FinancialAccount.

NoteMultiple Financial Accounts beta Connected accounts can have multiple financial accounts associated with them through providing the same connected account ID as the value of the Stripe-Account header. By default, you can associate a maximum of 10 financial accounts with a single connected account (closed financial accounts don’t contribute to the limit). If you need a higher account threshold, contact treasury-support@stripe.com.

The following JSON defines the FinancialAccount object structure:

[JSON (commented)](#)`{
  "object": "treasury.financial_account",
  "created": 1612927106,
  "id": "fa_123",
  "country": "US",
  "supported_currencies": ["usd"],
  // Arrays of active, pending and restricted features summarize the status of all requested features
  "active_features": ["financial_addresses.aba", "deposit_insurance"],
  "pending_features": ["inbound_transfers.ach"],
  "restricted_features": ["intra_stripe_flows", "outbound_payments.ach", "outbound_payments.us_domestic_wire"],
  "balance": {
    "cash": {"usd": 9000},
    "inbound_pending": {"usd": 0},
    "outbound_pending": {"usd": 1000}
  },
  // The FinancialAccount gains a FinancialAddress once the `financial_addresses.aba` feature is active. For more information, see "Activating features"
  "financial_addresses": [
    {
      "type": "aba",
      "supported_networks": ["ach", "domestic_wire_us"],
      "aba": {
        "account_number_last4": "7890",
        // Use the expand[] parameter to view the `account_number` field hidden by default
        "account_number": "1234567890",
        "routing_number": "000000001",
        "bank_name": "Goldman Sachs"
      }
    }
  ],
  "livemode": true,
  // Financial accounts begin in the "open" state, but can be closed
  // `status_details.closed` is populated once a financial account is closed
  "status": "open",
  "status_details": {
    "closed": {
      // List of one or more reasons why the FinancialAccount was closed:
      // - account_rejected
      // - closed_by_platform
      // - other
      "reasons": [],
    }
  },
  // User-defined metadata
  "metadata": {},
  // Restrictions that the platform can apply to the FinancialAccount
  "platform_restrictions": {
    "inbound_flows": "unrestricted",
    "outbound_flows": "restricted"
  },
}`Typically, you also request financial account features when you make the API request to create the account. Regardless of the Features you request, the connected account must have the treasury capability enabled. If you’re unsure if the connected account has the capability, use GET /v1/accounts/{{CONNECTED_ACCOUNT_ID}} to check. The account’s capabilities hash must have a treasury value of active.

`…
  "capabilities": {
    "card_issuing": "active",
    "card_payments": "active",
    "transfers": "active",
    "treasury": "active",
    "us_bank_account_ach_payments": "active"
  },
…`If you want to issue cards attached to the financial account balance, your platform’s connected accounts must also have the Issuing (card_issuing) capability enabled. The connected account must have this capability before you can request the card_issuing feature for its financial account. If the connected account doesn’t have the capability, attempting to create a FinancialAccount with a request for the card_issuing feature results in an error.

NoteMultiple Financial Account beta You can set the nickname field of a FinancialAccount object to designate the financial account with a custom name. You can use nicknames to create unique identifiers, which can be useful when working with multiple financial accounts under a single connected account. For nicknames to be valid, they must:

- Be unique for each financial account under a given connected account
- Be a non-blank string
- Contain less than 250 characters

If you don’t provide a nickname upon account creation, the nickname field will be empty and will return null. You can update nicknames after creating a FinancialAccount.

The following request creates a financial account assigned to the connected account with the ID assigned in the Stripe-Account header.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/financial_accounts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "supported_currencies[]"=usd \
  -d "features[card_issuing][requested]"=true \
  -d "features[deposit_insurance][requested]"=true \
  -d "features[financial_addresses][aba][requested]"=true \
  -d "features[inbound_transfers][ach][requested]"=true \
  -d "features[intra_stripe_flows][requested]"=true \
  -d "features[outbound_payments][ach][requested]"=true \
  -d "features[outbound_payments][us_domestic_wire][requested]"=true \
  -d "features[outbound_transfers][ach][requested]"=true \
  -d "features[outbound_transfers][us_domestic_wire][requested]"=true`The response is a FinancialAccount object to confirm financial account creation.

`{
  "object": "treasury.financial_account",
  "created": 1612927106,
  "id": "fa_123",
  "country": "US",
  "supported_currencies": ["usd"],
  "active_features": [
    "card_issuing",
  ],
  // Features that require activation enter a pending state before activating
  "pending_features": [
    "deposit_insurance",
    "financial_addresses.aba",
    "inbound_transfers.ach",
    "intra_stripe_flows",
    "outbound_payments.ach",
    "outbound_payments.us_domestic_wire",
    "outbound_transfers.ach",
    "outbound_transfers.us_domestic_wire"
  ],
  "restricted_features": [],
  // A FinancialAddress is not added until the financial_addresses.aba feature has been activated
  "financial_addresses": [],
  "livemode": true,
  "status": "open",
  ...
}`## Update a FinancialAccount

Use POST /v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}} to update the FinancialAccount with the associated ID. Include the connected account ID as the Stripe-Account header value. The following example updates the metadata of the FinancialAccount.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "metadata[key]"=value`## Retrieve a FinancialAccount and account number

Use GET /v1/treasury/financial_accounts/{{FINANCIALACCOUNT_ID}} to retrieve the FinancialAccount with the associated ID. Include the connected account ID as the Stripe-Account header value.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"`By default, the account number for a financial account isn’t included in the response. To retrieve the account number, include the financial_addresses.aba.account_number field in the expand array.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "expand[]"="financial_addresses.aba.account_number"`If successful, the response returns the FinancialAccount object with or without the account number depending on the inclusion of the expand array.

[Response with account expanded](#)`{
  "id": {{FINANCIAL_ACCOUNT_ID}},
  ...
  "financial_addresses": [
    {
      "aba": {
        "account_holder_name": "jenny",
        "account_number": "4242424242420239",
        "account_number_last4": "0239",
        "bank_name": "Stripe Test Bank",
        "routing_number": "000000001"
      },
      ...
    }
  ],
  ...
}`For more information on the expand parameter, see expanding responses.

### Feature summary

The FinancialAccount object contains a summary of the state of all its Features in three arrays - active_features, pending_features, and restricted_features.

`{
  "object": "treasury.financial_account",
  "id": "fa_987",
  "status": "open",
  ...
  "active_features": ["card_issuing"],
  "pending_features": ["financial_addresses.aba"],
  "restricted_features": ["outbound_transfers.ach"],
}`These arrays provide a convenient way to see:

- Any features that aren’t active (`pending_features`or`restricted_features`are not empty).
- Features that are active (`active_features`contains the specific features).
- Restricted features that require action (`restricted_features`isn’t empty).

See Financial account features for more information.

## Close a FinancialAccount

You can permanently close a financial account if it meets the following conditions:

- Has a zero balance.
- There are no pending inbound transfers.
- All attached Issuing cards are canceled.

WarningYou can’t reopen financial accounts after you’ve closed them.

To close a financial account, contact treasury-support@stripe.com and provide the FinancialAccount ID you want to close and the reason for the closure. You must provide your users with account closure notices, as detailed in the Treasury compliance guidelines.

Closing a financial account has no impact on data retention for associated objects, such as Transactions.

You can’t open a new financial account for a connected account if you previously closed a financial account associated with that same connected account. You must open a new connected account to create a new financial account.

NoteMultiple Financial Account beta The Multiple Financial Account beta feature allows you to close a financial account and open a new one associated with the same connected account without having to open a new connected account.

## FinancialAccount closure via API Beta

After you gain access to the beta program, use POST/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/close to close the financial account with the associated ID. Include the associated connected account ID as a header value.

Command Line`curl https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/close \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -X "POST" \
  -H "Stripe-Account: {{CONNECTED_STRIPE_ACCOUNT_ID}}"`The response is the FinancialAccount object with a status of closed to confirm the action.

`{
  "id": "{{FINANCIAL_ACCOUNT_ID}}",
  "object": "treasury.financial_account",
  "status": "closed",
  "status_details": {
    "closed": {
      "reasons": ["closed_by_platform"]
    }
  },
  "active_features": [],
  "pending_features": [],
  "restricted_features": ["financial_addresses.aba"],
  ...
}`### Handling transactions on closed accounts

In rare circumstances, financial accounts might receive credits or debits on closed accounts that Stripe can’t return automatically. As a platform owner, you’re responsible for negative balances incurred after account closure. Stripe support works with you to return any remaining funds owed to the seller or service provider and to remediate closed accounts with a negative balance.

## Webhooks

You can create financial accounts before fulfilling onboarding requirements. In this case, the financial account opens asynchronously and then triggers a treasury.financial_account.features_status_updated webhook with an updated view on any features still restricted due to outstanding onboarding requirements.

- `account.updated`  - When requesting new Features, the platform might get an`account.updated`webhook prompting that the requirements hash has changed and some new fields are now in`pending_verification`.


- `treasury.financial_account.created`  - Triggered whenever a new FinancialAccount is created.


- `treasury.financial_account.closed`  - Notifies when the status of the top-level FinancialAccount changes to closed.


- `treasury.financial_account.features_status_updated`  - Indicates that one or more Features have changed status. This is reflected in changes to the`active_features, pending_features`or`restricted_features`arrays.



Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a FinancialAccount](#create-a-financialaccount)[Update a FinancialAccount](#update-a-financialaccount)[Retrieve a FinancialAccount and account number](#retrieve-a-financialaccount-and-account-number)[Close a FinancialAccount](#close-a-financialaccount)[FinancialAccount closure via API](#financialaccount-closure-via-api)[Webhooks](#webhooks)Products Used[Treasury](/treasury)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`