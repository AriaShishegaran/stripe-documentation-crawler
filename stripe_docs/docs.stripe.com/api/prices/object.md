- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Price object

[The Price object](/api/prices/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- activebooleanWhether the price can be used for new purchases.

Whether the price can be used for new purchases.

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- nicknamenullable stringA brief description of the price, hidden from customers.

A brief description of the price, hidden from customers.

- productstringExpandableThe ID of the product this price is associated with.

The ID of the product this price is associated with.

- recurringnullable objectThe recurring components of a price such as interval and usage_type.Show child attributes

The recurring components of a price such as interval and usage_type.

- typeenumOne of one_time or recurring depending on whether the price is for a one-time purchase or a recurring (subscription) purchase.Possible enum valuesone_timerecurring

One of one_time or recurring depending on whether the price is for a one-time purchase or a recurring (subscription) purchase.

- unit_amountnullable integerThe unit amount in cents to be charged, represented as a whole integer if possible. Only set if billing_scheme=per_unit.

The unit amount in cents to be charged, represented as a whole integer if possible. Only set if billing_scheme=per_unit.

- objectstring

- billing_schemeenum

- createdtimestamp

- currency_optionsnullable objectExpandable

- custom_unit_amountnullable object

- livemodeboolean

- lookup_keynullable string

- tax_behaviornullable enum

- tiersnullable array of objectsExpandable

- tiers_modenullable enum

- transform_quantitynullable object

- unit_amount_decimalnullable decimal string

# Create a price

[Create a price](/api/prices/create)

Creates a new price for an existing product. The price can be recurring or one-time.

- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- activebooleanWhether the price can be used for new purchases. Defaults to true.

Whether the price can be used for new purchases. Defaults to true.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- nicknamestringA brief description of the price, hidden from customers.

A brief description of the price, hidden from customers.

- productstringRequired unless product_data is providedThe ID of the product that this price will belong to.

The ID of the product that this price will belong to.

- recurringobjectThe recurring components of a price such as interval and usage_type.Show child parameters

The recurring components of a price such as interval and usage_type.

- unit_amountintegerRequired conditionallyA positive integer in cents (or 0 for a free price) representing how much to charge. One of unit_amount or custom_unit_amount is required, unless billing_scheme=tiered.

A positive integer in cents (or 0 for a free price) representing how much to charge. One of unit_amount or custom_unit_amount is required, unless billing_scheme=tiered.

- billing_schemeenum

- currency_optionsobject

- custom_unit_amountobjectRequired unless unit_amount is provided

- lookup_keystring

- product_dataobjectRequired unless product is provided

- tax_behaviorenum

- tiersarray of objectsRequired if billing_scheme=tiered

- tiers_modeenumRequired if billing_scheme=tiered

- transfer_lookup_keyboolean

- transform_quantityobject

- unit_amount_decimalstring

The newly created Price object is returned upon success. Otherwise, this call raises an error.

[an error](#errors)

# Update a price

[Update a price](/api/prices/update)

Updates the specified price by setting the values of the parameters passed. Any parameters not provided are left unchanged.

- activebooleanWhether the price can be used for new purchases. Defaults to true.

Whether the price can be used for new purchases. Defaults to true.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- nicknamestringA brief description of the price, hidden from customers.

A brief description of the price, hidden from customers.

- currency_optionsobject

- lookup_keystring

- tax_behaviorenum

- transfer_lookup_keyboolean

The updated price object is returned upon success. Otherwise, this call raises an error.

[an error](#errors)

# Retrieve a price

[Retrieve a price](/api/prices/retrieve)

Retrieves the price with the given ID.

No parameters.

Returns a price if a valid price or plan ID was provided. Raises an error otherwise.

[an error](#errors)

# List all prices

[List all prices](/api/prices/list)

Returns a list of your active prices, excluding inline prices. For the list of inactive prices, set active to false.

[inline prices](/products-prices/pricing-models#inline-pricing)

- activebooleanOnly return prices that are active or inactive (e.g., pass false to list all inactive prices).

Only return prices that are active or inactive (e.g., pass false to list all inactive prices).

- currencyenumOnly return prices for the given currency.

Only return prices for the given currency.

- productstringOnly return prices for the given product.

Only return prices for the given product.

- typeenumOnly return prices of type recurring or one_time.Possible enum valuesone_timerecurring

Only return prices of type recurring or one_time.

- createdobject

- ending_beforestring

- limitinteger

- lookup_keysarray of strings

- recurringobject

- starting_afterstring

A dictionary with a data property that contains an array of up to limit prices, starting after prices starting_after. Each entry in the array is a separate price object. If no more prices are available, the resulting array will be empty.
