- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Account object

[The Account object](/api/financial_connections/accounts/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- objectstringString representing the object’s type. Objects of the same type share the same value.

String representing the object’s type. Objects of the same type share the same value.

- account_holdernullable objectThe account holder that this account belongs to.Show child attributes

The account holder that this account belongs to.

- balancenullable objectThe most recent information about the account’s balance.Show child attributes

The most recent information about the account’s balance.

- balance_refreshnullable objectThe state of the most recent attempt to refresh the account balance.Show child attributes

The state of the most recent attempt to refresh the account balance.

- categoryenumThe type of the account. Account category is further divided in subcategory.Possible enum valuescashThe account represents real funds held by the institution (e.g. a checking or savings account).creditThe account represents credit extended by the institution (e.g. a credit card or mortgage).investmentThe account represents investments, or any account where there are funds of unknown liquidity.otherThe account does not fall under the other categories.

The type of the account. Account category is further divided in subcategory.

The account represents real funds held by the institution (e.g. a checking or savings account).

The account represents credit extended by the institution (e.g. a credit card or mortgage).

The account represents investments, or any account where there are funds of unknown liquidity.

The account does not fall under the other categories.

- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.

Time at which the object was created. Measured in seconds since the Unix epoch.

- display_namenullable stringA human-readable name that has been assigned to this account, either by the account holder or by the institution.

A human-readable name that has been assigned to this account, either by the account holder or by the institution.

- institution_namestringThe name of the institution that holds this account.

The name of the institution that holds this account.

- last4nullable stringThe last 4 digits of the account number. If present, this will be 4 numeric characters.

The last 4 digits of the account number. If present, this will be 4 numeric characters.

- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.

Has the value true if the object exists in live mode or the value false if the object exists in test mode.

- ownershipnullable stringExpandableThe most recent information about the account’s owners.

The most recent information about the account’s owners.

- ownership_refreshnullable objectThe state of the most recent attempt to refresh the account owners.Show child attributes

The state of the most recent attempt to refresh the account owners.

- permissionsnullable array of enumsThe list of permissions granted by this account.Possible enum valuesbalancesAllows accessing balance data from the account.ownershipAllows accessing ownership data from the account.payment_methodAllows the creation of a payment method from the account.transactionsAllows accessing transactions data from the account.

The list of permissions granted by this account.

Allows accessing balance data from the account.

Allows accessing ownership data from the account.

Allows the creation of a payment method from the account.

Allows accessing transactions data from the account.

- statusenumThe status of the link to the account.Possible enum valuesactiveStripe is able to retrieve data from the Account without issues.disconnectedAccount connection has been terminated.inactiveStripe cannot retrieve data from the Account.

The status of the link to the account.

Stripe is able to retrieve data from the Account without issues.

Account connection has been terminated.

Stripe cannot retrieve data from the Account.

- subcategoryenumIf category is cash, one of:checkingsavingsotherIf category is credit, one of:mortgageline_of_creditcredit_cardotherIf category is investment or other, this will be other.Possible enum valuescheckingThe account is a checking account.credit_cardThe account represents a credit card.line_of_creditThe account represents a line of credit.mortgageThe account represents a mortgage.otherThe account does not fall under any of the other subcategories.savingsThe account is a savings account.

If category is cash, one of:

- checking

- savings

- other

If category is credit, one of:

- mortgage

- line_of_credit

- credit_card

- other

If category is investment or other, this will be other.

The account is a checking account.

The account represents a credit card.

The account represents a line of credit.

The account represents a mortgage.

The account does not fall under any of the other subcategories.

The account is a savings account.

- subscriptionsnullable array of enumsThe list of data refresh subscriptions requested on this account.Possible enum valuestransactionsSubscribes to periodic transactions data refreshes from the account.

The list of data refresh subscriptions requested on this account.

Subscribes to periodic transactions data refreshes from the account.

- supported_payment_method_typesarray of enumsThe PaymentMethod type(s) that can be created from this account.Possible enum valueslinkA link PaymentMethod can be created.us_bank_accountA us_bank_account PaymentMethod can be created.

The PaymentMethod type(s) that can be created from this account.

[PaymentMethod type](/api/payment_methods/object#payment_method_object-type)

A link PaymentMethod can be created.

A us_bank_account PaymentMethod can be created.

- transaction_refreshnullable objectThe state of the most recent attempt to refresh the account transactions.Show child attributes

The state of the most recent attempt to refresh the account transactions.

# Retrieve an Account

[Retrieve an Account](/api/financial_connections/accounts/retrieve)

Retrieves the details of an Financial Connections Account.

No parameters.

Returns an Account object if a valid identifier was provided, and raises an error otherwise.

[an error](#errors)

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
