- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Promotion Code

[Promotion Code](/api/promotion_codes)

A Promotion Code represents a customer-redeemable code for a coupon. It can be used to create multiple codes for a single coupon.

[coupon](#coupons)

[POST/v1/promotion_codes](/api/promotion_codes/create)

[POST/v1/promotion_codes/:id](/api/promotion_codes/update)

[GET/v1/promotion_codes/:id](/api/promotion_codes/retrieve)

[GET/v1/promotion_codes](/api/promotion_codes/list)

# The Promotion Code object

[The Promotion Code object](/api/promotion_codes/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- codestringThe customer-facing code. Regardless of case, this code must be unique across all active promotion codes for each customer.

The customer-facing code. Regardless of case, this code must be unique across all active promotion codes for each customer.

- couponobjectHash describing the coupon for this promotion code.Show child attributes

Hash describing the coupon for this promotion code.

- metadatanullable objectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- objectstring

- activeboolean

- createdtimestamp

- customernullable stringExpandable

- expires_atnullable timestamp

- livemodeboolean

- max_redemptionsnullable integer

- restrictionsobject

- times_redeemedinteger

# Create a promotion code

[Create a promotion code](/api/promotion_codes/create)

A promotion code points to a coupon. You can optionally restrict the code to a specific customer, redemption limit, and expiration date.

- couponstringRequiredThe coupon for this promotion code.

The coupon for this promotion code.

- codestringThe customer-facing code. Regardless of case, this code must be unique across all active promotion codes for a specific customer. If left blank, we will generate one automatically.

The customer-facing code. Regardless of case, this code must be unique across all active promotion codes for a specific customer. If left blank, we will generate one automatically.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- activeboolean

- customerstring

- expires_attimestamp

- max_redemptionsinteger

- restrictionsobject

Returns the promotion code object.

# Update a promotion code

[Update a promotion code](/api/promotion_codes/update)

Updates the specified promotion code by setting the values of the parameters passed. Most fields are, by design, not editable.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- activeboolean

- restrictionsobject

The updated promotion code object is returned upon success. Otherwise, this call raises an error.

[an error](#errors)

# Retrieve a promotion code

[Retrieve a promotion code](/api/promotion_codes/retrieve)

Retrieves the promotion code with the given ID. In order to retrieve a promotion code by the customer-facing code use list with the desired code.

[list](/api/promotion_codes/list)

No parameters.

Returns a promotion code if a valid promotion code ID was provided. Raises an error otherwise.

[an error](#errors)
