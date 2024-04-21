- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Coupon object

[The Coupon object](/api/coupons/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- amount_offnullable integerAmount (in the currency specified) that will be taken off the subtotal of any invoices for this customer.

Amount (in the currency specified) that will be taken off the subtotal of any invoices for this customer.

- currencynullable enumIf amount_off has been set, the three-letter ISO code for the currency of the amount to take off.

If amount_off has been set, the three-letter ISO code for the currency of the amount to take off.

[ISO code for the currency](https://stripe.com/docs/currencies)

- durationenumOne of forever, once, and repeating. Describes how long a customer who applies this coupon will get the discount.Possible enum valuesforeverApplies to all charges from a subscription with this coupon applied.onceApplies to the first charge from a subscription with this coupon applied.repeatingApplies to charges in the first duration_in_months months from a subscription with this coupon applied.

One of forever, once, and repeating. Describes how long a customer who applies this coupon will get the discount.

Applies to all charges from a subscription with this coupon applied.

Applies to the first charge from a subscription with this coupon applied.

Applies to charges in the first duration_in_months months from a subscription with this coupon applied.

- duration_in_monthsnullable integerIf duration is repeating, the number of months the coupon applies. Null if coupon duration is forever or once.

If duration is repeating, the number of months the coupon applies. Null if coupon duration is forever or once.

- metadatanullable objectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- namenullable stringName of the coupon displayed to customers on for instance invoices or receipts.

Name of the coupon displayed to customers on for instance invoices or receipts.

- percent_offnullable floatPercent that will be taken off the subtotal of any invoices for this customer for the duration of the coupon. For example, a coupon with percent_off of 50 will make a $100 invoice $50 instead.

Percent that will be taken off the subtotal of any invoices for this customer for the duration of the coupon. For example, a coupon with percent_off of 50 will make a $100 invoice $50 instead.

- objectstring

- applies_tonullable objectExpandable

- createdtimestamp

- currency_optionsnullable objectExpandable

- livemodeboolean

- max_redemptionsnullable integer

- redeem_bynullable timestamp

- times_redeemedinteger

- validboolean

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
