- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Bank Account object

[The Bank Account object](/api/customer_bank_accounts/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- account_holder_namenullable stringThe name of the person or business that owns the bank account.

The name of the person or business that owns the bank account.

- account_holder_typenullable stringThe type of entity that holds the account. This can be either individual or company.

The type of entity that holds the account. This can be either individual or company.

- bank_namenullable stringName of the bank associated with the routing number (e.g., WELLS FARGO).

Name of the bank associated with the routing number (e.g., WELLS FARGO).

- countrystringTwo-letter ISO code representing the country the bank account is located in.

Two-letter ISO code representing the country the bank account is located in.

- currencyenumThree-letter ISO code for the currency paid out to the bank account.

Three-letter ISO code for the currency paid out to the bank account.

[ISO code for the currency](https://stripe.com/docs/payouts)

- customernullable stringExpandableThe ID of the customer that the bank account is associated with.

The ID of the customer that the bank account is associated with.

- fingerprintnullable stringUniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.

- last4stringThe last four digits of the bank account number.

The last four digits of the bank account number.

- metadatanullable objectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- routing_numbernullable stringThe routing transit number for the bank account.

The routing transit number for the bank account.

- objectstring

- accountnullable stringExpandable

- account_typenullable string

- available_payout_methodsnullable array of enums

- statusstring

# Create a bank account

[Create a bank account](/api/customer_bank_accounts/create)

When you create a new bank account, you must specify a Customer object on which to create it.

- sourceobject | stringRequiredEither a token, like the ones returned by Stripe.js, or a dictionary containing a user’s bank account details (with the options shown below).Show child parameters

Either a token, like the ones returned by Stripe.js, or a dictionary containing a user’s bank account details (with the options shown below).

[Stripe.js](/js)

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns the bank account object.

# Update a bank account

[Update a bank account](/api/customer_bank_accounts/update)

Updates the account_holder_name, account_holder_type, and metadata of a bank account belonging to a customer. Other bank account details are not editable, by design.

- account_holder_namestringThe name of the person or business that owns the bank account.

The name of the person or business that owns the bank account.

- account_holder_typestringThe type of entity that holds the account. This can be either individual or company.

The type of entity that holds the account. This can be either individual or company.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns the bank account object.

# Retrieve a bank account

[Retrieve a bank account](/api/customer_bank_accounts/retrieve)

By default, you can see the 10 most recent sources stored on a Customer directly on the object, but you can also retrieve details about a specific bank account stored on the Stripe account.

No parameters.

Returns the bank account object.

# List all bank accounts

[List all bank accounts](/api/customer_bank_accounts/list)

You can see a list of the bank accounts belonging to a Customer. Note that the 10 most recent sources are always available by default on the Customer. If you need more than those 10, you can use this API method and the limit and starting_after parameters to page through additional bank accounts.

No parameters.

- ending_beforestring

- limitinteger

- starting_afterstring

Returns a list of the bank accounts stored on the customer.
