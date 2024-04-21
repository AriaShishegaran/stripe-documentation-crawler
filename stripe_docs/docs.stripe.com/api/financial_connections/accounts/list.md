- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# List Accounts

[List Accounts](/api/financial_connections/accounts/list)

Returns a list of Financial Connections Account objects.

- account_holderobjectIf present, only return accounts that belong to the specified account holder. account_holder[customer] and account_holder[account] are mutually exclusive.Show child parameters

If present, only return accounts that belong to the specified account holder. account_holder[customer] and account_holder[account] are mutually exclusive.

- sessionstringIf present, only return accounts that were collected as part of the given session.

If present, only return accounts that were collected as part of the given session.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit Account objects, starting after account starting_after. Each entry in the array is a separate Account object. If no more accounts are available, the resulting array will be empty. This request will raise an error if more than one of account_holder[account], account_holder[customer], or session is specified.

# Disconnect an Account

[Disconnect an Account](/api/financial_connections/accounts/disconnect)

Disables your access to a Financial Connections Account. You will no longer be able to access data associated with the account (e.g. balances, transactions).

No parameters.

Returns an Account object if a valid identifier was provided, and raises an error otherwise.

[an error](#errors)

# Refresh Account data

[Refresh Account data](/api/financial_connections/accounts/refresh)

Refreshes the data associated with a Financial Connections Account.

- featuresarray of enumsRequiredThe list of account features that you would like to refresh.Possible enum valuesbalanceBalance data from the accountownershipOwnership data from the accounttransactionsTransactions data from the account

The list of account features that you would like to refresh.

Balance data from the account

Ownership data from the account

Transactions data from the account

Returns an Account object if a valid identifier was provided and if you have sufficient permissions to that account. Raises an error otherwise.

[an error](#errors)

# Subscribe to data refreshes for an Account

[Subscribe to data refreshes for an Account](/api/financial_connections/accounts/subscribe)

Subscribes to periodic refreshes of data associated with a Financial Connections Account.

- featuresarray of enumsRequiredThe list of account features to which you would like to subscribe.Possible enum valuestransactionsTransactions data from the account

The list of account features to which you would like to subscribe.

Transactions data from the account

Returns an Account object if a valid identifier was provided and if you have sufficient permissions to that account. Raises an error otherwise.

[an error](#errors)

# Unsubscribe from data refreshes for an Account

[Unsubscribe from data refreshes for an Account](/api/financial_connections/accounts/unsubscribe)

Unsubscribes from periodic refreshes of data associated with a Financial Connections Account.

- featuresarray of enumsRequiredThe list of account features from which you would like to unsubscribe.Possible enum valuestransactionsTransactions data from the account

The list of account features from which you would like to unsubscribe.

Transactions data from the account

Returns an Account object if a valid identifier was provided and if you have sufficient permissions to that account. Raises an error otherwise.

[an error](#errors)
