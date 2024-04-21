# Working with Treasury financial accounts

When you enable Stripe Treasury on your platform, you can add FinancialAccount objects to your platform architecture to enable the efficient storing, sending, and receiving of funds. After you gain API access to Treasury, Stripe attaches a financial account to your platform account and enables you to provision an individual financial account for each eligible Custom connected account on your platform.

[platform architecture](/treasury/account-management/treasury-accounts-structure)

[gain API access to Treasury](/treasury/access)

Multiple Financial Accounts beta The Multiple Financial Account beta feature enables you to open multiple financial accounts for a single Custom connected account. Contact treasury-support@stripe.com to access test mode for this feature and join the wait list.

[treasury-support@stripe.com](mailto:treasury-support@stripe.com)

Each financial account has its own distinct balance of funds, separate from the balance of the account it’s linked to. For example, the owner of a Custom connected account on your platform might have a 100 EUR connected account balance and a 200 EUR financial account balance. In this scenario, the connected account owner has a sum of 300 EUR spread between their financial account and connected account balances. These two balances remain separate, but the API provides the ability to move money from the connected account balance to the financial account balance.

[balance of funds](/treasury/account-management/working-with-balances-and-transactions)

In the Stripe API, FinancialAccount objects serve as the source and destination of money movement API requests. You request Features through the API to assign to FinancialAccounts that provide additional functionality for the financial accounts on your platform. For example, to enable payment card features on a specific financial account, you send an API request with the FinancialAccount ID for the card_issuing feature. See Financial account features for more information on Feature objects. See the Available features section within that guide to check required connected account capabilities for each Feature.

[Financial account features](/treasury/account-management/financial-account-features)

[Available features](/treasury/account-management/financial-account-features#available-features)

Before you create financial accounts in live mode for your Treasury integration, we recommend you first create test financial accounts in test mode. Test mode financial accounts can’t receive or send real money, can’t be used in live mode, and don’t generate a live account with real routing and account information, but are otherwise identical in configuration and functionality.

[test mode](/test-mode)

## Create a FinancialAccount

Use POST /v1/treasury/financial_accounts to create FinancialAccounts. Include the connected account ID as the value of the Stripe-Account header of the call to associate the FinancialAccount with a connected account. Currently, each connected account can only have one FinancialAccount.

Multiple Financial Accounts beta Connected accounts can have multiple financial accounts associated with them through providing the same connected account ID as the value of the Stripe-Account header. By default, you can associate a maximum of 10 financial accounts with a single connected account (closed financial accounts don’t contribute to the limit). If you need a higher account threshold, contact treasury-support@stripe.com.

[treasury-support@stripe.com](mailto:treasury-support@stripe.com)

The following JSON defines the FinancialAccount object structure:

Typically, you also request financial account features when you make the API request to create the account. Regardless of the Features you request, the connected account must have the treasury capability enabled. If you’re unsure if the connected account has the capability, use GET /v1/accounts/{{CONNECTED_ACCOUNT_ID}} to check. The account’s capabilities hash must have a treasury value of active.

[financial account features](/treasury/account-management/financial-account-features)

If you want to issue cards attached to the financial account balance, your platform’s connected accounts must also have the Issuing (card_issuing) capability enabled. The connected account must have this capability before you can request the card_issuing feature for its financial account. If the connected account doesn’t have the capability, attempting to create a FinancialAccount with a request for the card_issuing feature results in an error.

Multiple Financial Account beta You can set the nickname field of a FinancialAccount object to designate the financial account with a custom name. You can use nicknames to create unique identifiers, which can be useful when working with multiple financial accounts under a single connected account. For nicknames to be valid, they must:

- Be unique for each financial account under a given connected account

- Be a non-blank string

- Contain less than 250 characters

If you don’t provide a nickname upon account creation, the nickname field will be empty and will return null. You can update nicknames after creating a FinancialAccount.

[update](/treasury/account-management/financial-accounts#update-a-financialaccount)

The following request creates a financial account assigned to the connected account with the ID assigned in the Stripe-Account header.

The response is a FinancialAccount object to confirm financial account creation.

## Update a FinancialAccount

Use POST /v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}} to update the FinancialAccount with the associated ID. Include the connected account ID as the Stripe-Account header value. The following example updates the metadata of the FinancialAccount.

[metadata](/api/metadata)

## Retrieve a FinancialAccount and account number

Use GET /v1/treasury/financial_accounts/{{FINANCIALACCOUNT_ID}} to retrieve the FinancialAccount with the associated ID. Include the connected account ID as the Stripe-Account header value.

By default, the account number for a financial account isn’t included in the response. To retrieve the account number, include the financial_addresses.aba.account_number field in the expand array.

If successful, the response returns the FinancialAccount object with or without the account number depending on the inclusion of the expand array.

For more information on the expand parameter, see expanding responses.

[expanding responses](/expand)

The FinancialAccount object contains a summary of the state of all its Features in three arrays - active_features, pending_features, and restricted_features.

These arrays provide a convenient way to see:

- Any features that aren’t active (pending_features or restricted_features are not empty).

- Features that are active (active_features contains the specific features).

- Restricted features that require action (restricted_features isn’t empty).

See Financial account features for more information.

[Financial account features](/treasury/account-management/financial-account-features)

## Close a FinancialAccount

You can permanently close a financial account if it meets the following conditions:

- Has a zero balance.

- There are no pending inbound transfers.

- All attached Issuing cards are canceled.

You can’t reopen financial accounts after you’ve closed them.

To close a financial account, contact treasury-support@stripe.com and provide the FinancialAccount ID you want to close and the reason for the closure. You must provide your users with account closure notices, as detailed in the Treasury compliance guidelines.

[treasury-support@stripe.com](mailto:treasury-support@stripe.com)

Closing a financial account has no impact on data retention for associated objects, such as Transactions.

You can’t open a new financial account for a connected account if you previously closed a financial account associated with that same connected account. You must open a new connected account to create a new financial account.

Multiple Financial Account beta The Multiple Financial Account beta feature allows you to close a financial account and open a new one associated with the same connected account without having to open a new connected account.

## FinancialAccount closure via API Beta

After you gain access to the beta program, use POST/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/close to close the financial account with the associated ID. Include the associated connected account ID as a header value.

The response is the FinancialAccount object with a status of closed to confirm the action.

In rare circumstances, financial accounts might receive credits or debits on closed accounts that Stripe can’t return automatically. As a platform owner, you’re responsible for negative balances incurred after account closure. Stripe support works with you to return any remaining funds owed to the seller or service provider and to remediate closed accounts with a negative balance.

## Webhooks

You can create financial accounts before fulfilling onboarding requirements. In this case, the financial account opens asynchronously and then triggers a treasury.financial_account.features_status_updated webhook with an updated view on any features still restricted due to outstanding onboarding requirements.

[webhook](/webhooks)

- account.updatedWhen requesting new Features, the platform might get an account.updated webhook prompting that the requirements hash has changed and some new fields are now in pending_verification.

- When requesting new Features, the platform might get an account.updated webhook prompting that the requirements hash has changed and some new fields are now in pending_verification.

- treasury.financial_account.createdTriggered whenever a new FinancialAccount is created.

- Triggered whenever a new FinancialAccount is created.

- treasury.financial_account.closedNotifies when the status of the top-level FinancialAccount changes to closed.

- Notifies when the status of the top-level FinancialAccount changes to closed.

- treasury.financial_account.features_status_updatedIndicates that one or more Features have changed status. This is reflected in changes to the active_features, pending_features or restricted_features arrays.

- Indicates that one or more Features have changed status. This is reflected in changes to the active_features, pending_features or restricted_features arrays.
