- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Subscription Item object

[The Subscription Item object](/api/subscription_items/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- priceobjectThe price the customer is subscribed to.Show child attributes

The price the customer is subscribed to.

- quantitynullable integerThe quantity of the plan to which the customer should be subscribed.

The quantity of the plan to which the customer should be subscribed.

[quantity](/subscriptions/quantities)

- subscriptionstringThe subscription this subscription_item belongs to.

The subscription this subscription_item belongs to.

- objectstring

- billing_thresholdsnullable object

- createdinteger

- discountsarray of stringsExpandable

- tax_ratesnullable array of objects

# Create a subscription item

[Create a subscription item](/api/subscription_items/create)

Adds a new item to an existing subscription. No existing items will be changed or replaced.

- subscriptionstringRequiredThe identifier of the subscription to modify.

The identifier of the subscription to modify.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- payment_behaviorenumUse allow_incomplete to transition the subscription to status=past_due if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription’s invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the SCA Migration Guide for Billing to learn more. This is the default behavior.Use default_incomplete to transition the subscription to status=past_due when payment is required and await explicit confirmation of the invoice’s payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, SCA regulation, or collecting a mandate for a bank debit payment method.Use pending_if_incomplete to update the subscription using pending updates. When you use pending_if_incomplete you can only pass the parameters supported by pending updates.Use error_if_incomplete if you want Stripe to return an HTTP 402 status code if a subscription’s invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the changelog to learn more.Possible enum valuesallow_incompletedefault_incompleteerror_if_incompletepending_if_incomplete

Use allow_incomplete to transition the subscription to status=past_due if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription’s invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the SCA Migration Guide for Billing to learn more. This is the default behavior.

[SCA Migration Guide](/billing/migration/strong-customer-authentication)

Use default_incomplete to transition the subscription to status=past_due when payment is required and await explicit confirmation of the invoice’s payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, SCA regulation, or collecting a mandate for a bank debit payment method.

[SCA regulation](/billing/migration/strong-customer-authentication)

Use pending_if_incomplete to update the subscription using pending updates. When you use pending_if_incomplete you can only pass the parameters supported by pending updates.

[pending updates](/billing/subscriptions/pending-updates)

[supported by pending updates](/billing/pending-updates-reference#supported-attributes)

Use error_if_incomplete if you want Stripe to return an HTTP 402 status code if a subscription’s invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the changelog to learn more.

[changelog](/upgrades#2019-03-14)

- pricestringThe ID of the price object.

The ID of the price object.

- proration_behaviorenumDetermines how to handle prorations when the billing cycle changes (e.g., when switching plans, resetting billing_cycle_anchor=now, or starting a trial), or if an item’s quantity changes. The default value is create_prorations.Possible enum valuesalways_invoiceAlways invoice immediately for prorations.create_prorationsWill cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under certain conditions.noneDisable creating prorations in this request.

Determines how to handle prorations when the billing cycle changes (e.g., when switching plans, resetting billing_cycle_anchor=now, or starting a trial), or if an item’s quantity changes. The default value is create_prorations.

[prorations](/billing/subscriptions/prorations)

Always invoice immediately for prorations.

Will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under certain conditions.

[certain conditions](/subscriptions/upgrading-downgrading#immediate-payment)

Disable creating prorations in this request.

- quantityintegerThe quantity you’d like to apply to the subscription item you’re creating.

The quantity you’d like to apply to the subscription item you’re creating.

- billing_thresholdsobject

- discountsarray of objects

- price_dataobject

- proration_datetimestamp

- tax_ratesarray of strings

Returns the created Subscription Item object, if successful. Otherwise, this call raises an error.

[an error](#errors)

# Update a subscription item

[Update a subscription item](/api/subscription_items/update)

Updates the plan or quantity of an item on a current subscription.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- payment_behaviorenumUse allow_incomplete to transition the subscription to status=past_due if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription’s invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the SCA Migration Guide for Billing to learn more. This is the default behavior.Use default_incomplete to transition the subscription to status=past_due when payment is required and await explicit confirmation of the invoice’s payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, SCA regulation, or collecting a mandate for a bank debit payment method.Use pending_if_incomplete to update the subscription using pending updates. When you use pending_if_incomplete you can only pass the parameters supported by pending updates.Use error_if_incomplete if you want Stripe to return an HTTP 402 status code if a subscription’s invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the changelog to learn more.Possible enum valuesallow_incompletedefault_incompleteerror_if_incompletepending_if_incomplete

Use allow_incomplete to transition the subscription to status=past_due if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription’s invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the SCA Migration Guide for Billing to learn more. This is the default behavior.

[SCA Migration Guide](/billing/migration/strong-customer-authentication)

Use default_incomplete to transition the subscription to status=past_due when payment is required and await explicit confirmation of the invoice’s payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, SCA regulation, or collecting a mandate for a bank debit payment method.

[SCA regulation](/billing/migration/strong-customer-authentication)

Use pending_if_incomplete to update the subscription using pending updates. When you use pending_if_incomplete you can only pass the parameters supported by pending updates.

[pending updates](/billing/subscriptions/pending-updates)

[supported by pending updates](/billing/pending-updates-reference#supported-attributes)

Use error_if_incomplete if you want Stripe to return an HTTP 402 status code if a subscription’s invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the changelog to learn more.

[changelog](/upgrades#2019-03-14)

- pricestringThe ID of the price object. When changing a subscription item’s price, quantity is set to 1 unless a quantity parameter is provided.

The ID of the price object. When changing a subscription item’s price, quantity is set to 1 unless a quantity parameter is provided.

- proration_behaviorenumDetermines how to handle prorations when the billing cycle changes (e.g., when switching plans, resetting billing_cycle_anchor=now, or starting a trial), or if an item’s quantity changes. The default value is create_prorations.Possible enum valuesalways_invoiceAlways invoice immediately for prorations.create_prorationsWill cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under certain conditions.noneDisable creating prorations in this request.

Determines how to handle prorations when the billing cycle changes (e.g., when switching plans, resetting billing_cycle_anchor=now, or starting a trial), or if an item’s quantity changes. The default value is create_prorations.

[prorations](/billing/subscriptions/prorations)

Always invoice immediately for prorations.

Will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under certain conditions.

[certain conditions](/subscriptions/upgrading-downgrading#immediate-payment)

Disable creating prorations in this request.

- quantityintegerThe quantity you’d like to apply to the subscription item you’re creating.

The quantity you’d like to apply to the subscription item you’re creating.

- billing_thresholdsobject

- discountsarray of objects

- off_sessionboolean

- price_dataobject

- proration_datetimestamp

- tax_ratesarray of strings

# Retrieve a subscription item

[Retrieve a subscription item](/api/subscription_items/retrieve)

Retrieves the subscription item with the given ID.

No parameters.

Returns a subscription item if a valid subscription item ID was provided. Raises an error otherwise.

[an error](#errors)

# List all subscription items

[List all subscription items](/api/subscription_items/list)

Returns a list of your subscription items for a given subscription.

- subscriptionstringRequiredThe ID of the subscription whose items will be retrieved.

The ID of the subscription whose items will be retrieved.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit subscription items, starting after subscription item starting_after. Each entry in the array is a separate subscription item object. If no more subscription items are available, the resulting array will be empty.
