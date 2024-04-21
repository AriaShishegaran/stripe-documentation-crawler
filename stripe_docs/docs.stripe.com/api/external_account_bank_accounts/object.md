- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The External Bank Account object

[The External Bank Account object](/api/external_account_bank_accounts/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- accountnullable stringExpandableThe ID of the account that the bank account is associated with.

The ID of the account that the bank account is associated with.

- bank_namenullable stringName of the bank associated with the routing number (e.g., WELLS FARGO).

Name of the bank associated with the routing number (e.g., WELLS FARGO).

- countrystringTwo-letter ISO code representing the country the bank account is located in.

Two-letter ISO code representing the country the bank account is located in.

- currencyenumThree-letter ISO code for the currency paid out to the bank account.

Three-letter ISO code for the currency paid out to the bank account.

[ISO code for the currency](https://stripe.com/docs/payouts)

- default_for_currencynullable booleanWhether this bank account is the default external account for its currency.

Whether this bank account is the default external account for its currency.

- last4stringThe last four digits of the bank account number.

The last four digits of the bank account number.

- metadatanullable objectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- routing_numbernullable stringThe routing transit number for the bank account.

The routing transit number for the bank account.

- statusstringFor bank accounts, possible values are new, validated, verified, verification_failed, or errored. A bank account that hasn’t had any activity or validation performed is new. If Stripe can determine that the bank account exists, its status will be validated. Note that there often isn’t enough information to know (e.g., for smaller credit unions), and the validation is not always run. If customer bank account verification has succeeded, the bank account status will be verified. If the verification failed for any reason, such as microdeposit failure, the status will be verification_failed. If a payout sent to this bank account fails, we’ll set the status to errored and will not continue to send scheduled payouts until the bank details are updated.For external accounts, possible values are new, errored and verification_failed. If a payout fails, the status is set to errored and scheduled payouts are stopped until account details are updated. In the US and India, if we can’t verify the owner of the bank account, we’ll set the status to verification_failed. Other validations aren’t run against external accounts because they’re only used for payouts. This means the other statuses don’t apply.

For bank accounts, possible values are new, validated, verified, verification_failed, or errored. A bank account that hasn’t had any activity or validation performed is new. If Stripe can determine that the bank account exists, its status will be validated. Note that there often isn’t enough information to know (e.g., for smaller credit unions), and the validation is not always run. If customer bank account verification has succeeded, the bank account status will be verified. If the verification failed for any reason, such as microdeposit failure, the status will be verification_failed. If a payout sent to this bank account fails, we’ll set the status to errored and will not continue to send scheduled payouts until the bank details are updated.

[scheduled payouts](https://stripe.com/docs/payouts#payout-schedule)

For external accounts, possible values are new, errored and verification_failed. If a payout fails, the status is set to errored and scheduled payouts are stopped until account details are updated. In the US and India, if we can’t verify the owner of the bank account, we’ll set the status to verification_failed. Other validations aren’t run against external accounts because they’re only used for payouts. This means the other statuses don’t apply.

[verify the owner of the bank account](https://support.stripe.com/questions/bank-account-ownership-verification)

- objectstring

- account_holder_namenullable string

- account_holder_typenullable string

- account_typenullable string

- available_payout_methodsnullable array of enums

- customernullable stringExpandable

- fingerprintnullable string

- future_requirementsnullable object

- requirementsnullable object

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
