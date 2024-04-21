- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Person object

[The Person object](/api/persons/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- accountstringThe account the person is associated with.

The account the person is associated with.

- addressnullable objectThe person’s address.Show child attributes

The person’s address.

- dobnullable objectThe person’s date of birth.Show child attributes

The person’s date of birth.

- emailnullable stringThe person’s email address.

The person’s email address.

- first_namenullable stringThe person’s first name.

The person’s first name.

- last_namenullable stringThe person’s last name.

The person’s last name.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- phonenullable stringThe person’s phone number.

The person’s phone number.

- relationshipobjectDescribes the person’s relationship to the account.Show child attributes

Describes the person’s relationship to the account.

- requirementsnullable objectInformation about the requirements for this person, including what information needs to be collected, and by when.Show child attributes

Information about the requirements for this person, including what information needs to be collected, and by when.

- objectstring

- additional_tos_acceptancesobject

- address_kananullable object

- address_kanjinullable object

- createdtimestamp

- first_name_kananullable string

- first_name_kanjinullable string

- full_name_aliasesnullable array of strings

- future_requirementsnullable object

- gendernullable enum

- id_number_providedboolean

- id_number_secondary_providednullable boolean

- last_name_kananullable string

- last_name_kanjinullable string

- maiden_namenullable string

- nationalitynullable string

- political_exposurenullable enum

- registered_addressnullable object

- ssn_last_4_providedboolean

- verificationobject

# Create a person

[Create a person](/api/persons/create)

Creates a new person.

- addressobjectThe person’s address.Show child parameters

The person’s address.

- dobobjectThe person’s date of birth.Show child parameters

The person’s date of birth.

- emailstringThe person’s email address.

The person’s email address.

- first_namestringThe person’s first name.

The person’s first name.

- id_numberstringThe person’s ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a PII token provided by Stripe.js.

The person’s ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a PII token provided by Stripe.js.

[PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii)

- last_namestringThe person’s last name.

The person’s last name.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- phonestringThe person’s phone number.

The person’s phone number.

- relationshipobjectThe relationship that this person has with the account’s legal entity.Show child parameters

The relationship that this person has with the account’s legal entity.

- ssn_last_4stringThe last four digits of the person’s Social Security number (U.S. only).

The last four digits of the person’s Social Security number (U.S. only).

- additional_tos_acceptancesobject

- address_kanaobject

- address_kanjiobject

- documentsobject

- first_name_kanastring

- first_name_kanjistring

- full_name_aliasesarray of strings

- genderenum

- id_number_secondarystring

- last_name_kanastring

- last_name_kanjistring

- maiden_namestring

- nationalitystring

- person_tokenstring

- political_exposurestring

- registered_addressobject

- verificationobject

Returns a person object.

# Update a person

[Update a person](/api/persons/update)

Updates an existing person.

- addressobjectThe person’s address.Show child parameters

The person’s address.

- dobobjectThe person’s date of birth.Show child parameters

The person’s date of birth.

- emailstringThe person’s email address.

The person’s email address.

- first_namestringThe person’s first name.

The person’s first name.

- id_numberstringThe person’s ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a PII token provided by Stripe.js.

The person’s ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a PII token provided by Stripe.js.

[PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii)

- last_namestringThe person’s last name.

The person’s last name.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- phonestringThe person’s phone number.

The person’s phone number.

- relationshipobjectThe relationship that this person has with the account’s legal entity.Show child parameters

The relationship that this person has with the account’s legal entity.

- ssn_last_4stringThe last four digits of the person’s Social Security number (U.S. only).

The last four digits of the person’s Social Security number (U.S. only).

- additional_tos_acceptancesobject

- address_kanaobject

- address_kanjiobject

- documentsobject

- first_name_kanastring

- first_name_kanjistring

- full_name_aliasesarray of strings

- genderenum

- id_number_secondarystring

- last_name_kanastring

- last_name_kanjistring

- maiden_namestring

- nationalitystring

- person_tokenstring

- political_exposurestring

- registered_addressobject

- verificationobject

Returns a person object.

# Retrieve a person

[Retrieve a person](/api/persons/retrieve)

Retrieves an existing person.

No parameters.

Returns a person object.

# List all persons

[List all persons](/api/persons/list)

Returns a list of people associated with the account’s legal entity. The people are returned sorted by creation date, with the most recent people appearing first.

- relationshipobjectFilters on the list of people returned based on the person’s relationship to the account’s company.Show child parameters

Filters on the list of people returned based on the person’s relationship to the account’s company.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit people, starting after person starting_after. Each entry in the array is a separate person object. If no more people are available, the resulting array will be empty.
