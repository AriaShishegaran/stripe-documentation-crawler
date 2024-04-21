- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Cardholders

[Cardholders](/api/issuing/cardholders)

An Issuing Cardholder object represents an individual or business entity who is issued cards.

[issued](/issuing)

Related guide: How to create a cardholder

[How to create a cardholder](/issuing/cards#create-cardholder)

[POST/v1/issuing/cardholders](/api/issuing/cardholders/create)

[POST/v1/issuing/cardholders/:id](/api/issuing/cardholders/update)

[GET/v1/issuing/cardholders/:id](/api/issuing/cardholders/retrieve)

[GET/v1/issuing/cardholders](/api/issuing/cardholders/list)

# The Cardholder object

[The Cardholder object](/api/issuing/cardholders/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- billingobjectThe cardholder’s billing information.Show child attributes

The cardholder’s billing information.

- emailnullable stringThe cardholder’s email address.

The cardholder’s email address.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- namestringThe cardholder’s name. This will be printed on cards issued to them.

The cardholder’s name. This will be printed on cards issued to them.

- phone_numbernullable stringThe cardholder’s phone number. This is required for all cardholders who will be creating EU cards. See the 3D Secure documentation for more details.

The cardholder’s phone number. This is required for all cardholders who will be creating EU cards. See the 3D Secure documentation for more details.

[3D Secure documentation](/issuing/3d-secure#when-is-3d-secure-applied)

- objectstring

- companynullable object

- createdtimestamp

- individualnullable object

- livemodeboolean

- preferred_localesnullable array of enums

- requirementsobject

- spending_controlsnullable object

- statusenum

- typeenum

# Create a cardholder

[Create a cardholder](/api/issuing/cardholders/create)

Creates a new Issuing Cardholder object that can be issued cards.

- billingobjectRequiredThe cardholder’s billing address.Show child parameters

The cardholder’s billing address.

- namestringRequiredThe cardholder’s name. This will be printed on cards issued to them. The maximum length of this field is 24 characters. This field cannot contain any special characters or numbers.

The cardholder’s name. This will be printed on cards issued to them. The maximum length of this field is 24 characters. This field cannot contain any special characters or numbers.

- emailstringThe cardholder’s email address.

The cardholder’s email address.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- phone_numberstringThe cardholder’s phone number. This will be transformed to E.164 if it is not provided in that format already. This is required for all cardholders who will be creating EU cards. See the 3D Secure documentation for more details.

The cardholder’s phone number. This will be transformed to E.164 if it is not provided in that format already. This is required for all cardholders who will be creating EU cards. See the 3D Secure documentation for more details.

[E.164](https://en.wikipedia.org/wiki/E.164)

[3D Secure documentation](/issuing/3d-secure#when-is-3d-secure-applied)

- companyobject

- individualobject

- preferred_localesarray of enums

- spending_controlsobject

- statusenum

- typeenum

Returns an Issuing Cardholder object if creation succeeds.

# Update a cardholder

[Update a cardholder](/api/issuing/cardholders/update)

Updates the specified Issuing Cardholder object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

- billingobjectThe cardholder’s billing address.Show child parameters

The cardholder’s billing address.

- emailstringThe cardholder’s email address.

The cardholder’s email address.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- phone_numberstringThe cardholder’s phone number. This is required for all cardholders who will be creating EU cards. See the 3D Secure documentation for more details.

The cardholder’s phone number. This is required for all cardholders who will be creating EU cards. See the 3D Secure documentation for more details.

[3D Secure documentation](/issuing/3d-secure)

- companyobject

- individualobject

- preferred_localesarray of enums

- spending_controlsobject

- statusenum

Returns an updated Issuing Cardholder object if a valid identifier was provided.

# Retrieve a cardholder

[Retrieve a cardholder](/api/issuing/cardholders/retrieve)

Retrieves an Issuing Cardholder object.

No parameters.

Returns an Issuing Cardholder object if a valid identifier was provided.
