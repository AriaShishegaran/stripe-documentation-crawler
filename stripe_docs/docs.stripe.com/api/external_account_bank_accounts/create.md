- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Create a bank account

[Create a bank account](/api/external_account_bank_accounts/create)

When you create a new bank account, you must specify a Custom account to create it on.

[Custom account](/connect/managed-accounts)

If the bank account’s owner has no other external account in the bank account’s currency, the new bank account will become the default for that currency. However, if the owner already has a bank account for that currency, the new account will become the default only if the default_for_currency parameter is set to true.

- external_accountobject | stringRequiredEither a token, like the ones returned by Stripe.js, or a dictionary containing a user’s bank account details (with the options shown below).Show child parameters

Either a token, like the ones returned by Stripe.js, or a dictionary containing a user’s bank account details (with the options shown below).

[Stripe.js](/js)

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- default_for_currencyboolean

Returns the bank account object

# Update a bank account

[Update a bank account](/api/external_account_bank_accounts/update)

Updates the metadata, account holder name, account holder type of a bank account belonging to a Custom account, and optionally sets it as the default for its currency. Other bank account details are not editable by design. You can re-enable a disabled bank account by performing an update call without providing any arguments or changes.

[Custom account](/connect/custom-accounts)

- default_for_currencybooleanWhen set to true, this becomes the default external account for its currency.

When set to true, this becomes the default external account for its currency.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- account_holder_namestring

- account_holder_typestring

- account_typestring

- documentsobject

Returns the bank account object.

# Retrieve a bank account

[Retrieve a bank account](/api/external_account_bank_accounts/retrieve)

By default, you can see the 10 most recent external accounts stored on a (connected account)[/docs/connect/accounts] directly on the object. You can also retrieve details about a specific bank account stored on the account.

No parameters.

Returns the bank account object.

# List all bank accounts

[List all bank accounts](/api/external_account_bank_accounts/list)

You can see a list of the bank accounts that belong to a connected account. Note that the 10 most recent external accounts are always available by default on the corresponding Stripe object. If you need more than those 10, you can use this API method and the limit and starting_after parameters to page through additional bank accounts.

[connected account](/connect/accounts)

No parameters.

- ending_beforestring

- limitinteger

- objectstring

- starting_afterstring

Returns a list of the bank accounts stored on the account.

# Delete a bank account

[Delete a bank account](/api/external_account_bank_accounts/delete)

You can delete destination bank accounts from a Custom account.

[Custom account](/connect/custom-accounts)

There are restrictions for deleting a bank account with default_for_currency set to true. You cannot delete a bank account if any of the following apply:

- The bank account’s currency is the same as the connected account’s default_currency.

[default_currency](/api/accounts/object#account_object-default_currency)

- There is another external account (card or bank account) with the same currency as the bank account.

To delete a bank account, you must first replace the default external account by setting default_for_currency with another external account in the same currency.

No parameters.

Returns the deleted bank account object.
