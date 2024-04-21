- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Plan object

[The Plan object](/api/plans/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- activebooleanWhether the plan can be used for new purchases.

Whether the plan can be used for new purchases.

- amountnullable integerThe unit amount in cents to be charged, represented as a whole integer if possible. Only set if billing_scheme=per_unit.

The unit amount in cents to be charged, represented as a whole integer if possible. Only set if billing_scheme=per_unit.

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- intervalenumThe frequency at which a subscription is billed. One of day, week, month or year.

The frequency at which a subscription is billed. One of day, week, month or year.

- metadatanullable objectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- nicknamenullable stringA brief description of the plan, hidden from customers.

A brief description of the plan, hidden from customers.

- productnullable stringExpandableThe product whose pricing this plan determines.

The product whose pricing this plan determines.

- objectstring

- aggregate_usagenullable enum

- amount_decimalnullable decimal string

- billing_schemeenum

- createdtimestamp

- interval_countinteger

- livemodeboolean

- meternullable stringPreview feature

- tiersnullable array of objectsExpandable

- tiers_modenullable enum

- transform_usagenullable object

- trial_period_daysnullable integer

- usage_typeenum

# Create a plan

[Create a plan](/api/plans/create)

You can now model subscriptions more flexibly using the Prices API. It replaces the Plans API and is backwards compatible to simplify your migration.

[Prices API](#prices)

- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- intervalenumRequiredSpecifies billing frequency. Either day, week, month or year.Possible enum valuesdaymonthweekyear

Specifies billing frequency. Either day, week, month or year.

- productobjectRequiredThe product whose pricing the created plan will represent. This can either be the ID of an existing product, or a dictionary containing fields used to create a service product.Show child parameters

The product whose pricing the created plan will represent. This can either be the ID of an existing product, or a dictionary containing fields used to create a service product.

[service product](/api#product_object-type)

- activebooleanWhether the plan is currently available for new subscriptions. Defaults to true.

Whether the plan is currently available for new subscriptions. Defaults to true.

- amountintegerRequired unless billing_scheme=tieredA positive integer in cents (or 0 for a free plan) representing how much to charge on a recurring basis.

A positive integer in cents (or 0 for a free plan) representing how much to charge on a recurring basis.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- nicknamestringA brief description of the plan, hidden from customers.

A brief description of the plan, hidden from customers.

- aggregate_usageenum

- amount_decimalstring

- billing_schemeenum

- idstring

- interval_countinteger

- meterstringPreview feature

- tiersarray of objectsRequired if billing_scheme=tiered

- tiers_modeenumRequired if billing_scheme=tiered

- transform_usageobject

- trial_period_daysinteger

- usage_typeenum

Returns the plan object.

# Update a plan

[Update a plan](/api/plans/update)

Updates the specified plan by setting the values of the parameters passed. Any parameters not provided are left unchanged. By design, you cannot change a plan’s ID, amount, currency, or billing cycle.

- activebooleanWhether the plan is currently available for new subscriptions.

Whether the plan is currently available for new subscriptions.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- nicknamestringA brief description of the plan, hidden from customers.

A brief description of the plan, hidden from customers.

- productstring

- trial_period_daysinteger

The updated plan object is returned upon success. Otherwise, this call raises an error.

[an error](#errors)

# Retrieve a plan

[Retrieve a plan](/api/plans/retrieve)

Retrieves the plan with the given ID.

No parameters.

Returns a plan if a valid plan ID was provided. Raises an error otherwise.

[an error](#errors)

# List all plans

[List all plans](/api/plans/list)

Returns a list of your plans.

- activebooleanOnly return plans that are active or inactive (e.g., pass false to list all inactive plans).

Only return plans that are active or inactive (e.g., pass false to list all inactive plans).

- productstringOnly return plans for the given product.

Only return plans for the given product.

- createdobject

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit plans, starting after plan starting_after. Each entry in the array is a separate plan object. If no more plans are available, the resulting array will be empty.
