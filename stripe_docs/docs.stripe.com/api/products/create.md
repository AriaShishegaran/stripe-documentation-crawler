- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Create a product

[Create a product](/api/products/create)

Creates a new product object.

- namestringRequiredThe product’s name, meant to be displayable to the customer.

The product’s name, meant to be displayable to the customer.

- activebooleanWhether the product is currently available for purchase. Defaults to true.

Whether the product is currently available for purchase. Defaults to true.

- descriptionstringThe product’s description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.

The product’s description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.

- idstringAn identifier will be randomly generated by Stripe. You can optionally override this ID, but the ID must be unique across all products in your Stripe account.

An identifier will be randomly generated by Stripe. You can optionally override this ID, but the ID must be unique across all products in your Stripe account.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- default_price_dataobject

- imagesarray of strings

- marketing_featuresarray of objects

- package_dimensionsobject

- shippableboolean

- statement_descriptorstring

- tax_codestring

- unit_labelstring

- urlstring

Returns a product object if the call succeeded.

# Update a product

[Update a product](/api/products/update)

Updates the specific product by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

- activebooleanWhether the product is available for purchase.

Whether the product is available for purchase.

- default_pricestringThe ID of the Price object that is the default price for this product.

The ID of the Price object that is the default price for this product.

[Price](/api/prices)

- descriptionstringThe product’s description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.

The product’s description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- namestringThe product’s name, meant to be displayable to the customer.

The product’s name, meant to be displayable to the customer.

- imagesarray of strings

- marketing_featuresarray of objects

- package_dimensionsobject

- shippableboolean

- statement_descriptorstring

- tax_codestring

- unit_labelstring

- urlstring

Returns the product object if the update succeeded.

# Retrieve a product

[Retrieve a product](/api/products/retrieve)

Retrieves the details of an existing product. Supply the unique product ID from either a product creation request or the product list, and Stripe will return the corresponding product information.

No parameters.

Returns a product object if a valid identifier was provided.

# List all products

[List all products](/api/products/list)

Returns a list of your products. The products are returned sorted by creation date, with the most recently created products appearing first.

- activebooleanOnly return products that are active or inactive (e.g., pass false to list all inactive products).

Only return products that are active or inactive (e.g., pass false to list all inactive products).

- createdobject

- ending_beforestring

- idsarray of strings

- limitinteger

- shippableboolean

- starting_afterstring

- urlstring

A dictionary with a data property that contains an array of up to limit products, starting after product starting_after. Each entry in the array is a separate product object. If no more products are available, the resulting array will be empty.

# Delete a product

[Delete a product](/api/products/delete)

Delete a product. Deleting a product is only possible if it has no prices associated with it. Additionally, deleting a product with type=good is only possible if it has no SKUs associated with it.

No parameters.

Returns a deleted object on success. Otherwise, this call raises an error.

[an error](#errors)