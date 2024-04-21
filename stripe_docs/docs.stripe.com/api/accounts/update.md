- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Update an account

[Update an account](/api/accounts/update)

Updates a connected account by setting the values of the parameters passed. Any parameters not provided are left unchanged.

[connected account](/connect/accounts)

For Custom accounts, you can update any information on the account. For other accounts, you can update all information until that account has started to go through Connect Onboarding. Once you create an Account Link or Account Session, some properties can only be changed or updated for Custom accounts.

[Account Link](/api/account_links)

[Account Session](/api/account_sessions)

To update your own account, use the Dashboard. Refer to our Connect documentation to learn more about updating accounts.

[Dashboard](https://dashboard.stripe.com/settings/account)

[Connect](/connect/updating-accounts)

- business_typeenumThe business type. Once you create an Account Link or Account Session, this property can only be updated for Custom accounts.Possible enum valuescompanygovernment_entityUS onlyindividualnon_profit

The business type. Once you create an Account Link or Account Session, this property can only be updated for Custom accounts.

[Account Link](https://docs.stripe.com/api/account_links)

[Account Session](https://docs.stripe.com/api/account_sessions)

US only

- capabilitiesobjectEach key of the dictionary represents a capability, and each capability maps to its settings (e.g. whether it has been requested or not). Each capability will be inactive until you have provided its specific requirements and Stripe has verified them. An account may have some of its requested capabilities be active and some be inactive.Show child parameters

Each key of the dictionary represents a capability, and each capability maps to its settings (e.g. whether it has been requested or not). Each capability will be inactive until you have provided its specific requirements and Stripe has verified them. An account may have some of its requested capabilities be active and some be inactive.

- companyobjectInformation about the company or business. This field is available for any business_type. Once you create an Account Link or Account Session, this property can only be updated for Custom accounts.Show child parameters

Information about the company or business. This field is available for any business_type. Once you create an Account Link or Account Session, this property can only be updated for Custom accounts.

[Account Link](https://docs.stripe.com/api/account_links)

[Account Session](https://docs.stripe.com/api/account_sessions)

- emailstringThe email address of the account holder. This is only to make the account easier to identify to you. Stripe only emails Custom accounts with your consent.

The email address of the account holder. This is only to make the account easier to identify to you. Stripe only emails Custom accounts with your consent.

- individualobjectInformation about the person represented by the account. This field is null unless business_type is set to individual. Once you create an Account Link or Account Session, this property can only be updated for Custom accounts.Show child parameters

Information about the person represented by the account. This field is null unless business_type is set to individual. Once you create an Account Link or Account Session, this property can only be updated for Custom accounts.

[Account Link](https://docs.stripe.com/api/account_links)

[Account Session](https://docs.stripe.com/api/account_sessions)

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- tos_acceptanceobjectDetails on the account’s acceptance of the Stripe Services Agreement This property can only be updated for Custom accounts.Show child parameters

Details on the account’s acceptance of the Stripe Services Agreement This property can only be updated for Custom accounts.

[Stripe Services Agreement](https://docs.stripe.com/connect/updating-accounts#tos-acceptance)

- account_tokenstring

- business_profileobject

- default_currencyenum

- documentsobject

- external_accountstring

- settingsobject

Returns an Account object if the call succeeds. If the account ID does not exist or another issue occurs, this call raises an error.

[Account](#account_object)

[an error](#errors)

# Retrieve account

[Retrieve account](/api/accounts/retrieve)

Retrieves the details of an account.

No parameters.

Returns an Account object if the call succeeds. If the account ID does not exist, this call raises an error.

[Account](#account_object)

[an error](#errors)

# List all connected accounts

[List all connected accounts](/api/accounts/list)

Returns a list of accounts connected to your platform via Connect. If you’re not a platform, the list is empty.

[Connect](/connect)

No parameters.

- createdobject

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit accounts, starting after account starting_after. Each entry in the array is a separate Account object. If no more accounts are available, the resulting array is empty.

[Account](#account_object)

# Delete an account

[Delete an account](/api/accounts/delete)

With Connect, you can delete accounts you manage.

[Connect](/connect)

Accounts created using test-mode keys can be deleted at any time. Standard accounts created using live-mode keys cannot be deleted. Custom or Express accounts created using live-mode keys can only be deleted once all balances are zero.

If you want to delete your own account, use the account information tab in your account settings instead.

[account information tab in your account settings](https://dashboard.stripe.com/settings/account)

No parameters.

Returns an object with a deleted parameter if the call succeeds. If the account ID does not exist, this call raises an error.

[an error](#errors)

# Reject an account

[Reject an account](/api/account/reject)

With Connect, you may flag accounts as suspicious.

[Connect](/connect)

Test-mode Custom and Express accounts can be rejected at any time. Accounts created using live-mode keys may only be rejected once all balances are zero.

- reasonstringRequiredThe reason for rejecting the account. Can be fraud, terms_of_service, or other.

The reason for rejecting the account. Can be fraud, terms_of_service, or other.

Returns an account with payouts_enabled and charges_enabled set to false on success. If the account ID does not exist, this call raises an error.

[an error](#errors)
