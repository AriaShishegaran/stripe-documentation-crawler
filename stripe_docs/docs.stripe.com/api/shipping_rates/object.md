- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Shipping Rate object

[The Shipping Rate object](/api/shipping_rates/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- activebooleanWhether the shipping rate can be used for new purchases. Defaults to true.

Whether the shipping rate can be used for new purchases. Defaults to true.

- display_namenullable stringThe name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.

The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.

- fixed_amountnullable objectDescribes a fixed amount to charge for shipping. Must be present if type is fixed_amount.Show child attributes

Describes a fixed amount to charge for shipping. Must be present if type is fixed_amount.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- typeenumThe type of calculation to use on the shipping rate. Can only be fixed_amount for now.

The type of calculation to use on the shipping rate. Can only be fixed_amount for now.

- objectstring

- createdtimestamp

- delivery_estimatenullable object

- livemodeboolean

- tax_behaviornullable enum

- tax_codenullable stringExpandable

# Create a shipping rate

[Create a shipping rate](/api/shipping_rates/create)

Creates a new shipping rate object.

- display_namestringRequiredThe name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.

The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.

- fixed_amountobjectDescribes a fixed amount to charge for shipping. Must be present if type is fixed_amount.Show child parameters

Describes a fixed amount to charge for shipping. Must be present if type is fixed_amount.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- typeenumRequiredThe type of calculation to use on the shipping rate. Can only be fixed_amount for now.

The type of calculation to use on the shipping rate. Can only be fixed_amount for now.

- delivery_estimateobject

- tax_behaviorenum

- tax_codestring

Returns a shipping rate object if the call succeeded.

# Update a shipping rate

[Update a shipping rate](/api/shipping_rates/update)

Updates an existing shipping rate object.

- activebooleanWhether the shipping rate can be used for new purchases. Defaults to true.

Whether the shipping rate can be used for new purchases. Defaults to true.

- fixed_amountobjectDescribes a fixed amount to charge for shipping. Must be present if type is fixed_amount.Show child parameters

Describes a fixed amount to charge for shipping. Must be present if type is fixed_amount.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- tax_behaviorenum

Returns the modified shipping rate object if the call succeeded.

# Retrieve a shipping rate

[Retrieve a shipping rate](/api/shipping_rates/retrieve)

Returns the shipping rate object with the given ID.

No parameters.

Returns a shipping rate object if a valid identifier was provided.

# List all shipping rates

[List all shipping rates](/api/shipping_rates/list)

Returns a list of your shipping rates.

- activebooleanOnly return shipping rates that are active or inactive.

Only return shipping rates that are active or inactive.

- createdobjectA filter on the list, based on the object created field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.Show child parameters

A filter on the list, based on the object created field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.

- currencyenumOnly return shipping rates for the given currency.

Only return shipping rates for the given currency.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit shipping rates, starting after shipping rate starting_after. Each entry in the array is a separate shipping rate object. If no more shipping rates are available, the resulting array will be empty. This require should never raise an error.
