- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Transactions

[Transactions](/api/issuing/transactions)

Any use of an issued card that results in funds entering or leaving your Stripe account, such as a completed purchase or refund, is represented by an Issuing Transaction object.

[issued card](/issuing)

Related guide: Issued card transactions

[Issued card transactions](/issuing/purchases/transactions)

[POST/v1/issuing/transactions/:id](/api/issuing/transactions/update)

[GET/v1/issuing/transactions/:id](/api/issuing/transactions/retrieve)

[GET/v1/issuing/transactions](/api/issuing/transactions/list)

[POST/v1/test_helpers/issuing/transactions/create_force_capture](/api/issuing/transactions/test_mode_create_force_capture)

[POST/v1/test_helpers/issuing/transactions/create_unlinked_refund](/api/issuing/transactions/test_mode_create_unlinked_refund)

[POST/v1/test_helpers/issuing/transactions/:id/refund](/api/issuing/transactions/test_mode_refund)

# The Transaction object

[The Transaction object](/api/issuing/transactions/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- amountintegerThe transaction amount, which will be reflected in your balance. This amount is in your currency and in the smallest currency unit.

The transaction amount, which will be reflected in your balance. This amount is in your currency and in the smallest currency unit.

[smallest currency unit](/currencies#zero-decimal)

- authorizationnullable stringExpandableThe Authorization object that led to this transaction.

The Authorization object that led to this transaction.

- cardstringExpandableThe card used to make this transaction.

The card used to make this transaction.

- cardholdernullable stringExpandableThe cardholder to whom this transaction belongs.

The cardholder to whom this transaction belongs.

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- typeenumThe nature of the transaction.Possible enum valuescaptureFunds were captured by the acquirer. amount will be negative as funds are moving out of your balance. Not all captures will be linked to an authorization, as acquirers can force capture in some cases.refundAn acquirer initiated a refund. This transaction might not be linked to an original capture, for example credits are original transactions. amount will be positive for refunds and negative for refund reversals (very rare).

The nature of the transaction.

Funds were captured by the acquirer. amount will be negative as funds are moving out of your balance. Not all captures will be linked to an authorization, as acquirers can force capture in some cases.

[can force capture in some cases](https://stripe.com/docs/issuing/purchases/transactions)

An acquirer initiated a refund. This transaction might not be linked to an original capture, for example credits are original transactions. amount will be positive for refunds and negative for refund reversals (very rare).

- objectstring

- amount_detailsnullable object

- balance_transactionnullable stringExpandable

- createdtimestamp

- disputenullable stringExpandable

- livemodeboolean

- merchant_amountinteger

- merchant_currencyenum

- merchant_dataobject

- network_datanullable object

- purchase_detailsnullable objectExpandable

- tokennullable stringPreview featureExpandable

- walletnullable enum

# Update a transaction

[Update a transaction](/api/issuing/transactions/update)

Updates the specified Issuing Transaction object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns an updated Issuing Transaction object if a valid identifier was provided.

# Retrieve a transaction

[Retrieve a transaction](/api/issuing/transactions/retrieve)

Retrieves an Issuing Transaction object.

No parameters.

Returns an Issuing Transaction object if a valid identifier was provided.

# List all transactions

[List all transactions](/api/issuing/transactions/list)

Returns a list of Issuing Transaction objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

- cardstringOnly return transactions that belong to the given card.

Only return transactions that belong to the given card.

- cardholderstringOnly return transactions that belong to the given cardholder.

Only return transactions that belong to the given cardholder.

- createdobject

- ending_beforestring

- limitinteger

- starting_afterstring

- typeenum

A dictionary with a data property that contains an array of up to limit transactions, starting after transaction starting_after. Each entry in the array is a separate Issuing Transaction object. If no more transactions are available, the resulting array will be empty.
