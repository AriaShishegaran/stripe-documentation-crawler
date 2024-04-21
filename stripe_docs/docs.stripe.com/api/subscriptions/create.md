- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Create a subscription

[Create a subscription](/api/subscriptions/create)

Creates a new subscription on an existing customer. Each customer can have up to 500 active or scheduled subscriptions.

When you create a subscription with collection_method=charge_automatically, the first invoice is finalized as part of the request. The payment_behavior parameter determines the exact behavior of the initial payment.

To start subscriptions where the first invoice always begins in a draft status, use subscription schedules instead. Schedules provide the flexibility to model more complex billing configurations that change over time.

[subscription schedules](/billing/subscriptions/subscription-schedules#managing)

- customerstringRequiredThe identifier of the customer to subscribe.

The identifier of the customer to subscribe.

- cancel_at_period_endbooleanBoolean indicating whether this subscription should cancel at the end of the current period.

Boolean indicating whether this subscription should cancel at the end of the current period.

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- default_payment_methodstringID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over default_source. If neither are set, invoices will use the customer’s invoice_settings.default_payment_method or default_source.

ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over default_source. If neither are set, invoices will use the customer’s invoice_settings.default_payment_method or default_source.

[invoice_settings.default_payment_method](/api/customers/object#customer_object-invoice_settings-default_payment_method)

[default_source](/api/customers/object#customer_object-default_source)

- descriptionstringThe subscription’s description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.

The subscription’s description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.

- itemsarray of objectsRequiredA list of up to 20 subscription items, each with an attached price.Show child parameters

A list of up to 20 subscription items, each with an attached price.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- payment_behaviorenumOnly applies to subscriptions with collection_method=charge_automatically.Use allow_incomplete to create Subscriptions with status=incomplete if the first invoice can’t be paid. Creating Subscriptions with this status allows you to manage scenarios where additional customer actions are needed to pay a subscription’s invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the SCA Migration Guide for Billing to learn more. This is the default behavior.Use default_incomplete to create Subscriptions with status=incomplete when the first invoice requires payment, otherwise start as active. Subscriptions transition to status=active when successfully confirming the PaymentIntent on the first invoice. This allows simpler management of scenarios where additional customer actions are needed to pay a subscription’s invoice, such as failed payments, SCA regulation, or collecting a mandate for a bank debit payment method. If the PaymentIntent is not confirmed within 23 hours Subscriptions transition to status=incomplete_expired, which is a terminal state.Use error_if_incomplete if you want Stripe to return an HTTP 402 status code if a subscription’s first invoice can’t be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further customer action is needed, this parameter doesn’t create a Subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the changelog to learn more.pending_if_incomplete is only used with updates and cannot be passed when creating a Subscription.Subscriptions with collection_method=send_invoice are automatically activated regardless of the first Invoice status.Possible enum valuesallow_incompletedefault_incompleteerror_if_incompletepending_if_incomplete

Only applies to subscriptions with collection_method=charge_automatically.

Use allow_incomplete to create Subscriptions with status=incomplete if the first invoice can’t be paid. Creating Subscriptions with this status allows you to manage scenarios where additional customer actions are needed to pay a subscription’s invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the SCA Migration Guide for Billing to learn more. This is the default behavior.

[SCA Migration Guide](/billing/migration/strong-customer-authentication)

Use default_incomplete to create Subscriptions with status=incomplete when the first invoice requires payment, otherwise start as active. Subscriptions transition to status=active when successfully confirming the PaymentIntent on the first invoice. This allows simpler management of scenarios where additional customer actions are needed to pay a subscription’s invoice, such as failed payments, SCA regulation, or collecting a mandate for a bank debit payment method. If the PaymentIntent is not confirmed within 23 hours Subscriptions transition to status=incomplete_expired, which is a terminal state.

[SCA regulation](/billing/migration/strong-customer-authentication)

Use error_if_incomplete if you want Stripe to return an HTTP 402 status code if a subscription’s first invoice can’t be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further customer action is needed, this parameter doesn’t create a Subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the changelog to learn more.

[changelog](/upgrades#2019-03-14)

pending_if_incomplete is only used with updates and cannot be passed when creating a Subscription.

Subscriptions with collection_method=send_invoice are automatically activated regardless of the first Invoice status.

- add_invoice_itemsarray of objects

- application_fee_percentfloatConnect only

- automatic_taxobject

- backdate_start_datetimestamp

- billing_cycle_anchortimestamp

- billing_cycle_anchor_configobject

- billing_thresholdsobject

- cancel_attimestamp

- collection_methodenum

- couponstringDeprecated

- days_until_dueinteger

- default_sourcestring

- default_tax_ratesarray of strings

- discountsarray of objects

- invoice_settingsobject

- off_sessionboolean

- on_behalf_ofstring

- payment_settingsobject

- pending_invoice_item_intervalobject

- promotion_codestringDeprecated

- proration_behaviorenum

- transfer_dataobjectConnect only

- trial_endstring | timestamp

- trial_from_planboolean

- trial_period_daysinteger

- trial_settingsobject

The newly created Subscription object, if the call succeeded. If the attempted charge fails, the subscription is created in an incomplete status.

# Update a subscription

[Update a subscription](/api/subscriptions/update)

Updates an existing subscription to match the specified parameters. When changing prices or quantities, we optionally prorate the price we charge next month to make up for any price changes. To preview how the proration is calculated, use the upcoming invoice endpoint.

[upcoming invoice](/api/invoices/upcoming)

By default, we prorate subscription changes. For example, if a customer signs up on May 1 for a 100 EUR price, they’ll be billed 100 EUR immediately. If on May 15 they switch to a 200 EUR price, then on June 1 they’ll be billed 250 EUR (200 EUR for a renewal of her subscription, plus a 50 EUR prorating adjustment for half of the previous month’s 100 EUR difference). Similarly, a downgrade generates a credit that is applied to the next invoice. We also prorate when you make quantity changes.

Switching prices does not normally change the billing date or generate an immediate charge unless:

- The billing interval is changed (for example, from monthly to yearly).

- The subscription moves from free to paid, or paid to free.

- A trial starts or ends.

In these cases, we apply a credit for the unused time on the previous price, immediately charge the customer using the new price, and reset the billing date.

If you want to charge for an upgrade immediately, pass proration_behavior as always_invoice to create prorations, automatically invoice the customer for those proration adjustments, and attempt to collect payment. If you pass create_prorations, the prorations are created but not automatically invoiced. If you want to bill the customer for the prorations before the subscription’s renewal date, you need to manually invoice the customer.

[invoice the customer](/api/invoices/create)

If you don’t want to prorate, set the proration_behavior option to none. With this option, the customer is billed 100 EUR on May 1 and 200 EUR on June 1. Similarly, if you set proration_behavior to none when switching between different billing intervals (for example, from monthly to yearly), we don’t generate any credits for the old subscription’s unused time. We still reset the billing date and bill immediately for the new subscription.

Updating the quantity on a subscription many times in an hour may result in rate limiting. If you need to bill for a frequently changing quantity, consider integrating usage-based billing instead.

[rate limiting](/rate-limits)

[usage-based billing](/billing/subscriptions/usage-based)

- cancel_at_period_endbooleanBoolean indicating whether this subscription should cancel at the end of the current period.

Boolean indicating whether this subscription should cancel at the end of the current period.

- default_payment_methodstringID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over default_source. If neither are set, invoices will use the customer’s invoice_settings.default_payment_method or default_source.

ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over default_source. If neither are set, invoices will use the customer’s invoice_settings.default_payment_method or default_source.

[invoice_settings.default_payment_method](/api/customers/object#customer_object-invoice_settings-default_payment_method)

[default_source](/api/customers/object#customer_object-default_source)

- descriptionstringThe subscription’s description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.

The subscription’s description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.

- itemsarray of objectsA list of up to 20 subscription items, each with an attached price.Show child parameters

A list of up to 20 subscription items, each with an attached price.

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

- proration_behaviorenumDetermines how to handle prorations when the billing cycle changes (e.g., when switching plans, resetting billing_cycle_anchor=now, or starting a trial), or if an item’s quantity changes. The default value is create_prorations.Possible enum valuesalways_invoiceAlways invoice immediately for prorations.create_prorationsWill cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under certain conditions.noneDisable creating prorations in this request.

Determines how to handle prorations when the billing cycle changes (e.g., when switching plans, resetting billing_cycle_anchor=now, or starting a trial), or if an item’s quantity changes. The default value is create_prorations.

[prorations](/billing/subscriptions/prorations)

Always invoice immediately for prorations.

Will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under certain conditions.

[certain conditions](/subscriptions/upgrading-downgrading#immediate-payment)

Disable creating prorations in this request.

- add_invoice_itemsarray of objects

- application_fee_percentfloatConnect only

- automatic_taxobject

- billing_cycle_anchorstring

- billing_thresholdsobject

- cancel_attimestamp

- cancellation_detailsobject

- collection_methodenum

- couponstringDeprecated

- days_until_dueinteger

- default_sourcestring

- default_tax_ratesarray of strings

- discountsarray of objects

- invoice_settingsobject

- off_sessionboolean

- on_behalf_ofstring

- pause_collectionobject

- payment_settingsobject

- pending_invoice_item_intervalobject

- promotion_codestring

- proration_datetimestamp

- transfer_dataobjectConnect only

- trial_endstring | timestamp

- trial_from_planboolean

- trial_settingsobject

The newly updated Subscription object, if the call succeeded. If payment_behavior is error_if_incomplete and a charge is required for the update and it fails, this call raises an error, and the subscription update does not go into effect.

[an error](/api/errors)

# Retrieve a subscription

[Retrieve a subscription](/api/subscriptions/retrieve)

Retrieves the subscription with the given ID.

No parameters.

Returns the subscription object.

# List subscriptions

[List subscriptions](/api/subscriptions/list)

By default, returns a list of subscriptions that have not been canceled. In order to list canceled subscriptions, specify status=canceled.

- customerstringThe ID of the customer whose subscriptions will be retrieved.

The ID of the customer whose subscriptions will be retrieved.

- pricestringFilter for subscriptions that contain this recurring price ID.

Filter for subscriptions that contain this recurring price ID.

- statusenumThe status of the subscriptions to retrieve. Passing in a value of canceled will return all canceled subscriptions, including those belonging to deleted customers. Pass ended to find subscriptions that are canceled and subscriptions that are expired due to incomplete payment. Passing in a value of all will return subscriptions of all statuses. If no value is supplied, all subscriptions that have not been canceled are returned.

The status of the subscriptions to retrieve. Passing in a value of canceled will return all canceled subscriptions, including those belonging to deleted customers. Pass ended to find subscriptions that are canceled and subscriptions that are expired due to incomplete payment. Passing in a value of all will return subscriptions of all statuses. If no value is supplied, all subscriptions that have not been canceled are returned.

[incomplete payment](/billing/subscriptions/overview#subscription-statuses)

- automatic_taxobject

- collection_methodenum

- createdobject

- ending_beforestring

- limitinteger

- starting_afterstring

- test_clockstring

Returns a list of subscriptions.

# Cancel a subscription

[Cancel a subscription](/api/subscriptions/cancel)

Cancels a customer’s subscription immediately. The customer will not be charged again for the subscription.

Note, however, that any pending invoice items that you’ve created will still be charged for at the end of the period, unless manually deleted. If you’ve set the subscription to cancel at the end of the period, any pending prorations will also be left in place and collected at the end of the period. But if the subscription is set to cancel immediately, pending prorations will be removed.

[deleted](#delete_invoiceitem)

By default, upon subscription cancellation, Stripe will stop automatic collection of all finalized invoices for the customer. This is intended to prevent unexpected payment attempts after the customer has canceled a subscription. However, you can resume automatic collection of the invoices manually after subscription cancellation to have us proceed. Or, you could check for unpaid invoices before allowing the customer to cancel the subscription at all.

No parameters.

- cancellation_detailsobject

- invoice_nowboolean

- prorateboolean

The canceled Subscription object. Its subscription status will be set to canceled.
