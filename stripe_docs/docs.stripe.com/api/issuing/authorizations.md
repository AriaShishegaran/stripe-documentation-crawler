- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Authorizations

[Authorizations](/api/issuing/authorizations)

When an issued card is used to make a purchase, an Issuing Authorization object is created. Authorizations must be approved for the purchase to be completed successfully.

[issued card](/issuing)

[Authorizations](/issuing/purchases/authorizations)

Related guide: Issued card authorizations

[Issued card authorizations](/issuing/purchases/authorizations)

[POST/v1/issuing/authorizations/:id](/api/issuing/authorizations/update)

[GET/v1/issuing/authorizations/:id](/api/issuing/authorizations/retrieve)

[GET/v1/issuing/authorizations](/api/issuing/authorizations/list)

[POST/v1/issuing/authorizations/:id/approve](/api/issuing/authorizations/approve)

[POST/v1/issuing/authorizations/:id/decline](/api/issuing/authorizations/decline)

[POST/v1/test_helpers/issuing/authorizations](/api/issuing/authorizations/test_mode_create)

[POST/v1/test_helpers/issuing/authorizations/:id/capture](/api/issuing/authorizations/test_mode_capture)

[POST/v1/test_helpers/issuing/authorizations/:id/expire](/api/issuing/authorizations/test_mode_expire)

[POST/v1/test_helpers/issuing/authorizations/:id/increment](/api/issuing/authorizations/test_mode_increment)

[POST/v1/test_helpers/issuing/authorizations/:id/reverse](/api/issuing/authorizations/test_mode_reverse)

# The Authorization object

[The Authorization object](/api/issuing/authorizations/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- amountintegerThe total amount that was authorized or rejected. This amount is in currency and in the smallest currency unit. amount should be the same as merchant_amount, unless currency and merchant_currency are different.

The total amount that was authorized or rejected. This amount is in currency and in the smallest currency unit. amount should be the same as merchant_amount, unless currency and merchant_currency are different.

[smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)

- approvedbooleanWhether the authorization has been approved.

Whether the authorization has been approved.

- cardobjectCard associated with this authorization.Show child attributes

Card associated with this authorization.

- cardholdernullable stringExpandableThe cardholder to whom this authorization belongs.

The cardholder to whom this authorization belongs.

- currencyenumThe currency of the cardholder. This currency can be different from the currency presented at authorization and the merchant_currency field on this authorization. Three-letter ISO currency code, in lowercase. Must be a supported currency.

The currency of the cardholder. This currency can be different from the currency presented at authorization and the merchant_currency field on this authorization. Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- statusenumThe current status of the authorization in its lifecycle.Possible enum valuesclosedThe authorization was declined or captured through one or more transactions.pendingThe authorization was created and is awaiting approval or was approved and is awaiting capture.reversedThe authorization was reversed by the merchant or expired without capture.

The current status of the authorization in its lifecycle.

The authorization was declined or captured through one or more transactions.

[captured](/issuing/purchases/transactions)

[transactions](/api/issuing/authorizations/object#issuing_authorization_object-transactions)

The authorization was created and is awaiting approval or was approved and is awaiting capture.

[capture](/issuing/purchases/transactions)

The authorization was reversed by the merchant or expired without capture.

- objectstring

- amount_detailsnullable object

- authorization_methodenum

- balance_transactionsarray of objects

- createdtimestamp

- livemodeboolean

- merchant_amountinteger

- merchant_currencyenum

- merchant_dataobject

- network_datanullable object

- pending_requestnullable object

- request_historyarray of objects

- tokennullable stringPreview featureExpandable

- transactionsarray of objects

- verification_dataobject

- walletnullable string

# Update an authorization

[Update an authorization](/api/issuing/authorizations/update)

Updates the specified Issuing Authorization object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns an updated Issuing Authorization object if a valid identifier was provided.

# Retrieve an authorization

[Retrieve an authorization](/api/issuing/authorizations/retrieve)

Retrieves an Issuing Authorization object.

No parameters.

Returns an Issuing Authorization object if a valid identifier was provided.

# List all authorizations

[List all authorizations](/api/issuing/authorizations/list)

Returns a list of Issuing Authorization objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

- cardstringOnly return authorizations that belong to the given card.

Only return authorizations that belong to the given card.

- cardholderstringOnly return authorizations that belong to the given cardholder.

Only return authorizations that belong to the given cardholder.

- statusenumOnly return authorizations with the given status. One of pending, closed, or reversed.Possible enum valuesclosedpendingreversed

Only return authorizations with the given status. One of pending, closed, or reversed.

- createdobject

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit authorizations, starting after authorization starting_after. Each entry in the array is a separate Issuing Authorization object. If no more authorizations are available, the resulting array will be empty.
