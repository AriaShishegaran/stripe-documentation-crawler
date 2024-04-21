- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# Delete a bank account

[Delete a bank account](/api/customer_bank_accounts/delete)

You can delete bank accounts from a Customer.

No parameters.

# Verify a bank account

[Verify a bank account](/api/customer_bank_accounts/verify)

Verify a specified bank account for a given customer.

- amountsarray of integersTwo positive integers, in cents, equal to the values of the microdeposits sent to the bank account.

Two positive integers, in cents, equal to the values of the microdeposits sent to the bank account.
