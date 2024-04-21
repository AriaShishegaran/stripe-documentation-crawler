- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Create a coupon

[Create a coupon](/api/coupons/create)

You can create coupons easily via the coupon management page of the Stripe dashboard. Coupon creation is also accessible via the API if you need to create coupons on the fly.

[coupon management](https://dashboard.stripe.com/coupons)

A coupon has either a percent_off or an amount_off and currency. If you set an amount_off, that amount will be subtracted from any invoice’s subtotal. For example, an invoice with a subtotal of 100 EUR will have a final total of 0 EUR if a coupon with an amount_off of 20000 is applied to it and an invoice with a subtotal of 300 EUR will have a final total of 100 EUR if a coupon with an amount_off of 20000 is applied to it.

- amount_offintegerA positive integer representing the amount to subtract from an invoice total (required if percent_off is not passed).

A positive integer representing the amount to subtract from an invoice total (required if percent_off is not passed).

- currencyenumThree-letter ISO code for the currency of the amount_off parameter (required if amount_off is passed).

Three-letter ISO code for the currency of the amount_off parameter (required if amount_off is passed).

[ISO code for the currency](https://stripe.com/docs/currencies)

- durationenumSpecifies how long the discount will be in effect if used on a subscription. Defaults to once.Possible enum valuesforeverApplies to all charges from a subscription with this coupon applied.onceApplies to the first charge from a subscription with this coupon applied.repeatingApplies to charges in the first duration_in_months months from a subscription with this coupon applied.

Specifies how long the discount will be in effect if used on a subscription. Defaults to once.

Applies to all charges from a subscription with this coupon applied.

Applies to the first charge from a subscription with this coupon applied.

Applies to charges in the first duration_in_months months from a subscription with this coupon applied.

- duration_in_monthsintegerRequired only if duration is repeating, in which case it must be a positive integer that specifies the number of months the discount will be in effect.

Required only if duration is repeating, in which case it must be a positive integer that specifies the number of months the discount will be in effect.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- namestringName of the coupon displayed to customers on, for instance invoices, or receipts. By default the id is shown if name is not set.

Name of the coupon displayed to customers on, for instance invoices, or receipts. By default the id is shown if name is not set.

- percent_offfloatA positive float larger than 0, and smaller or equal to 100, that represents the discount the coupon will apply (required if amount_off is not passed).

A positive float larger than 0, and smaller or equal to 100, that represents the discount the coupon will apply (required if amount_off is not passed).

- applies_toobject

- currency_optionsobject

- idstring

- max_redemptionsinteger

- redeem_bytimestamp

Returns the coupon object.

# Update a coupon

[Update a coupon](/api/coupons/update)

Updates the metadata of a coupon. Other coupon details (currency, duration, amount_off) are, by design, not editable.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- namestringName of the coupon displayed to customers on, for instance invoices, or receipts. By default the id is shown if name is not set.

Name of the coupon displayed to customers on, for instance invoices, or receipts. By default the id is shown if name is not set.

- currency_optionsobject

The newly updated coupon object if the call succeeded. Otherwise, this call raises an error, such as if the coupon has been deleted.

[an error](#errors)

# Retrieve a coupon

[Retrieve a coupon](/api/coupons/retrieve)

Retrieves the coupon with the given ID.

No parameters.

Returns a coupon if a valid coupon ID was provided. Raises an error otherwise.

[an error](#errors)

# List all coupons

[List all coupons](/api/coupons/list)

Returns a list of your coupons.

No parameters.

- createdobject

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit coupons, starting after coupon starting_after. Each entry in the array is a separate coupon object. If no more coupons are available, the resulting array will be empty.

# Delete a coupon

[Delete a coupon](/api/coupons/delete)

You can delete coupons via the coupon management page of the Stripe dashboard. However, deleting a coupon does not affect any customers who have already applied the coupon; it means that new customers can’t redeem the coupon. You can also delete coupons via the API.

[coupon management](https://dashboard.stripe.com/coupons)

No parameters.

An object with the deleted coupon’s ID and a deleted flag upon success. Otherwise, this call raises an error, such as if the coupon has already been deleted.

[an error](#errors)
