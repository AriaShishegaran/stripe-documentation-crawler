- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Financial Accounts

[Financial Accounts](/api/treasury/financial_accounts)

Stripe Treasury provides users with a container for money called a FinancialAccount that is separate from their Payments balance. FinancialAccounts serve as the source and destination of Treasury’s money movement APIs.

[POST/v1/treasury/financial_accounts](/api/treasury/financial_accounts/create)

[POST/v1/treasury/financial_accounts/:id](/api/treasury/financial_accounts/update)

[GET/v1/treasury/financial_accounts/:id](/api/treasury/financial_accounts/retrieve)

[GET/v1/treasury/financial_accounts](/api/treasury/financial_accounts/list)

# The FinancialAccount object

[The FinancialAccount object](/api/treasury/financial_accounts/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- objectstringString representing the object’s type. Objects of the same type share the same value.

String representing the object’s type. Objects of the same type share the same value.

- active_featuresarray of enumsThe array of paths to active Features in the Features hash.

The array of paths to active Features in the Features hash.

- balanceobjectThe single multi-currency balance of the FinancialAccount. Positive values represent money that belongs to the user while negative values represent funds the user owes. Currently, FinancialAccounts can only carry balances in USD.Show child attributes

The single multi-currency balance of the FinancialAccount. Positive values represent money that belongs to the user while negative values represent funds the user owes. Currently, FinancialAccounts can only carry balances in USD.

- countrystringTwo-letter country code (ISO 3166-1 alpha-2).

Two-letter country code (ISO 3166-1 alpha-2).

[ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.

Time at which the object was created. Measured in seconds since the Unix epoch.

- featuresnullable objectExpandableThe features and their statuses for this FinancialAccount.Show child attributes

The features and their statuses for this FinancialAccount.

- financial_addressesarray of objectsThe set of credentials that resolve to a FinancialAccount.Show child attributes

The set of credentials that resolve to a FinancialAccount.

- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.

Has the value true if the object exists in live mode or the value false if the object exists in test mode.

- metadatanullable objectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- pending_featuresarray of enumsThe array of paths to pending Features in the Features hash.

The array of paths to pending Features in the Features hash.

- platform_restrictionsnullable objectThe set of functionalities that the platform can restrict on the FinancialAccount.Show child attributes

The set of functionalities that the platform can restrict on the FinancialAccount.

- restricted_featuresarray of enumsThe array of paths to restricted Features in the Features hash.

The array of paths to restricted Features in the Features hash.

- statusenumThe enum specifying what state the account is in.

The enum specifying what state the account is in.

- status_detailsobjectDetails related to the status of this FinancialAccount.Show child attributes

Details related to the status of this FinancialAccount.

- supported_currenciesarray of enumsThe currencies the FinancialAccount can hold a balance in. Three-letter ISO currency code, in lowercase.

The currencies the FinancialAccount can hold a balance in. Three-letter ISO currency code, in lowercase.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

# Create a FinancialAccount

[Create a FinancialAccount](/api/treasury/financial_accounts/create)

Creates a new FinancialAccount. For now, each connected account can only have one FinancialAccount.

- supported_currenciesarray of stringsRequiredThe currencies the FinancialAccount can hold a balance in.

The currencies the FinancialAccount can hold a balance in.

- featuresobjectEncodes whether a FinancialAccount has access to a particular feature. Stripe or the platform can control features via the requested field.Show child parameters

Encodes whether a FinancialAccount has access to a particular feature. Stripe or the platform can control features via the requested field.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- platform_restrictionsobjectThe set of functionalities that the platform can restrict on the FinancialAccount.Show child parameters

The set of functionalities that the platform can restrict on the FinancialAccount.

Returns a FinancialAccount object.

# Update a FinancialAccount

[Update a FinancialAccount](/api/treasury/financial_accounts/update)

Updates the details of a FinancialAccount.

- featuresobjectEncodes whether a FinancialAccount has access to a particular feature, with a status enum and associated status_details. Stripe or the platform may control features via the requested field.Show child parameters

Encodes whether a FinancialAccount has access to a particular feature, with a status enum and associated status_details. Stripe or the platform may control features via the requested field.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- platform_restrictionsobjectThe set of functionalities that the platform can restrict on the FinancialAccount.Show child parameters

The set of functionalities that the platform can restrict on the FinancialAccount.

Returns a FinancialAccount object.

# Retrieve a FinancialAccount

[Retrieve a FinancialAccount](/api/treasury/financial_accounts/retrieve)

Retrieves the details of a FinancialAccount.

No parameters.

Return a FinancialAccount object.
