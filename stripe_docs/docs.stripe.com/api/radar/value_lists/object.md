- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Value List object

[The Value List object](/api/radar/value_lists/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- aliasstringThe name of the value list for use in rules.

The name of the value list for use in rules.

- item_typeenumThe type of items in the value list. One of card_fingerprint, us_bank_account_fingerprint, sepa_debit_fingerprint, card_bin, email, ip_address, country, string, case_sensitive_string, or customer_id.Possible enum valuescard_bincard_fingerprintcase_sensitive_stringcountrycustomer_idemailip_addresssepa_debit_fingerprintstringus_bank_account_fingerprint

The type of items in the value list. One of card_fingerprint, us_bank_account_fingerprint, sepa_debit_fingerprint, card_bin, email, ip_address, country, string, case_sensitive_string, or customer_id.

- list_itemsobjectList of items contained within this value list.Show child attributes

List of items contained within this value list.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- namestringThe name of the value list.

The name of the value list.

- objectstring

- createdtimestamp

- created_bystring

- livemodeboolean

# Create a value list

[Create a value list](/api/radar/value_lists/create)

Creates a new ValueList object, which can then be referenced in rules.

- aliasstringRequiredThe name of the value list for use in rules.

The name of the value list for use in rules.

- namestringRequiredThe human-readable name of the value list.

The human-readable name of the value list.

- item_typestringType of the items in the value list. One of card_fingerprint, us_bank_account_fingerprint, sepa_debit_fingerprint, card_bin, email, ip_address, country, string, case_sensitive_string, or customer_id. Use string if the item type is unknown or mixed.

Type of the items in the value list. One of card_fingerprint, us_bank_account_fingerprint, sepa_debit_fingerprint, card_bin, email, ip_address, country, string, case_sensitive_string, or customer_id. Use string if the item type is unknown or mixed.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns a ValueList object if creation succeeds.

# Update a value list

[Update a value list](/api/radar/value_lists/update)

Updates a ValueList object by setting the values of the parameters passed. Any parameters not provided will be left unchanged. Note that item_type is immutable.

- aliasstringThe name of the value list for use in rules.

The name of the value list for use in rules.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- namestringThe human-readable name of the value list.

The human-readable name of the value list.

Returns an updated ValueList object if a valid identifier was provided.

# Retrieve a value list

[Retrieve a value list](/api/radar/value_lists/retrieve)

Retrieves a ValueList object.

No parameters.

Returns a ValueList object if a valid identifier was provided.

# List all value lists

[List all value lists](/api/radar/value_lists/list)

Returns a list of ValueList objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

- aliasstringThe alias used to reference the value list when writing rules.

The alias used to reference the value list when writing rules.

- containsstring

- createdobject

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit lists, starting after list starting_after. Each entry in the array is a separate ValueList object. If no more lists are available, the resulting array will be empty.
