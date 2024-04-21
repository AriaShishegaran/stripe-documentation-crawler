- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Tax Rate

[Tax Rate](/api/tax_rates)

Tax rates can be applied to invoices, subscriptions and Checkout Sessions to collect tax.

[invoices](/billing/invoices/tax-rates)

[subscriptions](/billing/subscriptions/taxes)

[Checkout Sessions](/payments/checkout/set-up-a-subscription#tax-rates)

Related guide: Tax rates

[Tax rates](/billing/taxes/tax-rates)

[POST/v1/tax_rates](/api/tax_rates/create)

[POST/v1/tax_rates/:id](/api/tax_rates/update)

[GET/v1/tax_rates](/api/tax_rates/list)

[GET/v1/tax_rates/:id](/api/tax_rates/retrieve)

# The Tax Rate object

[The Tax Rate object](/api/tax_rates/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- activebooleanDefaults to true. When set to false, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

Defaults to true. When set to false, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

- countrynullable stringTwo-letter country code (ISO 3166-1 alpha-2).

Two-letter country code (ISO 3166-1 alpha-2).

[ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

- descriptionnullable stringAn arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

- display_namestringThe display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.

- inclusivebooleanThis specifies if the tax rate is inclusive or exclusive.

This specifies if the tax rate is inclusive or exclusive.

- jurisdictionnullable stringThe jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

- metadatanullable objectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- percentagefloatTax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.

- statenullable stringISO 3166-2 subdivision code, without country prefix. For example, “NY” for New York, United States.

ISO 3166-2 subdivision code, without country prefix. For example, “NY” for New York, United States.

[ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2:US)

- objectstring

- createdtimestamp

- effective_percentagenullable float

- jurisdiction_levelnullable enum

- livemodeboolean

- tax_typenullable enum

# Create a tax rate

[Create a tax rate](/api/tax_rates/create)

Creates a new tax rate.

- display_namestringRequiredThe display name of the tax rate, which will be shown to users.

The display name of the tax rate, which will be shown to users.

- inclusivebooleanRequiredThis specifies if the tax rate is inclusive or exclusive.

This specifies if the tax rate is inclusive or exclusive.

- percentagefloatRequiredThis represents the tax rate percent out of 100.

This represents the tax rate percent out of 100.

- activebooleanFlag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

Flag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

- countrystringTwo-letter country code (ISO 3166-1 alpha-2).

Two-letter country code (ISO 3166-1 alpha-2).

[ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

- descriptionstringAn arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

- jurisdictionstringThe jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- statestringISO 3166-2 subdivision code, without country prefix. For example, “NY” for New York, United States.

ISO 3166-2 subdivision code, without country prefix. For example, “NY” for New York, United States.

[ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2:US)

- tax_typeenum

The created tax rate object.

# Update a tax rate

[Update a tax rate](/api/tax_rates/update)

Updates an existing tax rate.

- activebooleanFlag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

Flag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.

- countrystringTwo-letter country code (ISO 3166-1 alpha-2).

Two-letter country code (ISO 3166-1 alpha-2).

[ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

- descriptionstringAn arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.

- display_namestringThe display name of the tax rate, which will be shown to users.

The display name of the tax rate, which will be shown to users.

- jurisdictionstringThe jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- statestringISO 3166-2 subdivision code, without country prefix. For example, “NY” for New York, United States.

ISO 3166-2 subdivision code, without country prefix. For example, “NY” for New York, United States.

[ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2:US)

- tax_typeenum

The updated tax rate.

# List all tax rates

[List all tax rates](/api/tax_rates/list)

Returns a list of your tax rates. Tax rates are returned sorted by creation date, with the most recently created tax rates appearing first.

- activebooleanOptional flag to filter by tax rates that are either active or inactive (archived).

Optional flag to filter by tax rates that are either active or inactive (archived).

- createdobject

- ending_beforestring

- inclusiveboolean

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit tax rates, starting after tax rate starting_after. Each entry in the array is a separate tax rate object. If no more tax rates are available, the resulting array will be empty.
