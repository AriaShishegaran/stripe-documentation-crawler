- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# Search prices

[Search prices](/api/prices/search)

Search for prices you’ve previously created using Stripe’s Search Query Language. Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up to an hour behind during outages. Search functionality is not available to merchants in India.

[Search Query Language](/search#search-query-language)

- querystringRequiredThe search query string. See search query language and the list of supported query fields for prices.

The search query string. See search query language and the list of supported query fields for prices.

[search query language](/search#search-query-language)

[query fields for prices](/search#query-fields-for-prices)

- limitintegerA limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- pagestringA cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.

A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.

A dictionary with a data property that contains an array of up to limit prices. If no objects match the query, the resulting array will be empty. See the related guide on expanding properties in lists.

[expanding properties in lists](/expand#lists)
