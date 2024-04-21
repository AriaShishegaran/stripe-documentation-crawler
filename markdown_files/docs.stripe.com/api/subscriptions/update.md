htmlUpdate a subscription | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Update a subscription

Updates an existing subscription to match the specified parameters. When changing prices or quantities, we optionally prorate the price we charge next month to make up for any price changes. To preview how the proration is calculated, use the upcoming invoice endpoint.

By default, we prorate subscription changes. For example, if a customer signs up on May 1 for a 100 EUR price, they’ll be billed 100 EUR immediately. If on May 15 they switch to a 200 EUR price, then on June 1 they’ll be billed 250 EUR (200 EUR for a renewal of her subscription, plus a 50 EUR prorating adjustment for half of the previous month’s 100 EUR difference). Similarly, a downgrade generates a credit that is applied to the next invoice. We also prorate when you make quantity changes.

Switching prices does not normally change the billing date or generate an immediate charge unless:

- The billing interval is changed (for example, from monthly to yearly).
- The subscription moves from free to paid, or paid to free.
- A trial starts or ends.

In these cases, we apply a credit for the unused time on the previous price, immediately charge the customer using the new price, and reset the billing date.

If you want to charge for an upgrade immediately, pass proration_behavior as always_invoice to create prorations, automatically invoice the customer for those proration adjustments, and attempt to collect payment. If you pass create_prorations, the prorations are created but not automatically invoiced. If you want to bill the customer for the prorations before the subscription’s renewal date, you need to manually invoice the customer.

If you don’t want to prorate, set the proration_behavior option to none. With this option, the customer is billed 100 EUR on May 1 and 200 EUR on June 1. Similarly, if you set proration_behavior to none when switching between different billing intervals (for example, from monthly to yearly), we don’t generate any credits for the old subscription’s unused time. We still reset the billing date and bill immediately for the new subscription.

Updating the quantity on a subscription many times in an hour may result in rate limiting. If you need to bill for a frequently changing quantity, consider integrating usage-based billing instead.

### Parameters

- cancel_at_period_endbooleanBoolean indicating whether this subscription should cancel at the end of the current period.


- default_payment_methodstringID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over default_source. If neither are set, invoices will use the customer’s invoice_settings.default_payment_method or default_source.


- descriptionstringThe subscription’s description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.


- itemsarray of objectsA list of up to 20 subscription items, each with an attached price.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- payment_behaviorenumUse allow_incomplete to transition the subscription to status=past_due if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription’s invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the SCA Migration Guide for Billing to learn more. This is the default behavior.

Use default_incomplete to transition the subscription to status=past_due when payment is required and await explicit confirmation of the invoice’s payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, SCA regulation, or collecting a mandate for a bank debit payment method.

Use pending_if_incomplete to update the subscription using pending updates. When you use pending_if_incomplete you can only pass the parameters supported by pending updates.

Use error_if_incomplete if you want Stripe to return an HTTP 402 status code if a subscription’s invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the changelog to learn more.

Possible enum values`allow_incomplete``default_incomplete``error_if_incomplete``pending_if_incomplete`
- proration_behaviorenumDetermines how to handle prorations when the billing cycle changes (e.g., when switching plans, resetting billing_cycle_anchor=now, or starting a trial), or if an item’s quantity changes. The default value is create_prorations.

Possible enum values`always_invoice`Always invoice immediately for prorations.

`create_prorations`Will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under certain conditions.

`none`Disable creating prorations in this request.



### More parametersExpand all

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

### Returns

The newly updated Subscription object, if the call succeeded. If payment_behavior is error_if_incomplete and a charge is required for the update and it fails, this call raises an error, and the subscription update does not go into effect.

POST/v1/subscriptions/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/subscriptions/sub_1MowQVLkdIwHu7ixeRlqHVzs \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "sub_1MowQVLkdIwHu7ixeRlqHVzs",  "object": "subscription",  "application": null,  "application_fee_percent": null,  "automatic_tax": {    "enabled": false,    "liability": null  },  "billing_cycle_anchor": 1679609767,  "billing_thresholds": null,  "cancel_at": null,  "cancel_at_period_end": false,  "canceled_at": null,  "cancellation_details": {    "comment": null,    "feedback": null,    "reason": null  },  "collection_method": "charge_automatically",  "created": 1679609767,  "currency": "usd",  "current_period_end": 1682288167,  "current_period_start": 1679609767,  "customer": "cus_Na6dX7aXxi11N4",  "days_until_due": null,  "default_payment_method": null,  "default_source": null,  "default_tax_rates": [],  "description": null,  "discount": null,  "ended_at": null,  "invoice_settings": {    "issuer": {      "type": "self"    }  },  "items": {    "object": "list",    "data": [      {        "id": "si_Na6dzxczY5fwHx",        "object": "subscription_item",        "billing_thresholds": null,        "created": 1679609768,        "metadata": {},        "plan": {          "id": "price_1MowQULkdIwHu7ixraBm864M",          "object": "plan",          "active": true,          "aggregate_usage": null,          "amount": 1000,          "amount_decimal": "1000",          "billing_scheme": "per_unit",          "created": 1679609766,          "currency": "usd",          "interval": "month",          "interval_count": 1,          "livemode": false,          "metadata": {},          "nickname": null,          "product": "prod_Na6dGcTsmU0I4R",          "tiers_mode": null,          "transform_usage": null,          "trial_period_days": null,          "usage_type": "licensed"        },        "price": {          "id": "price_1MowQULkdIwHu7ixraBm864M",          "object": "price",          "active": true,          "billing_scheme": "per_unit",          "created": 1679609766,          "currency": "usd",          "custom_unit_amount": null,          "livemode": false,          "lookup_key": null,          "metadata": {},          "nickname": null,          "product": "prod_Na6dGcTsmU0I4R",          "recurring": {            "aggregate_usage": null,            "interval": "month",            "interval_count": 1,            "trial_period_days": null,            "usage_type": "licensed"          },          "tax_behavior": "unspecified",          "tiers_mode": null,          "transform_quantity": null,          "type": "recurring",          "unit_amount": 1000,          "unit_amount_decimal": "1000"        },        "quantity": 1,        "subscription": "sub_1MowQVLkdIwHu7ixeRlqHVzs",        "tax_rates": []      }    ],    "has_more": false,    "total_count": 1,    "url": "/v1/subscription_items?subscription=sub_1MowQVLkdIwHu7ixeRlqHVzs"  },  "latest_invoice": "in_1MowQWLkdIwHu7ixuzkSPfKd",  "livemode": false,  "metadata": {    "order_id": "6735"  },  "next_pending_invoice_item_invoice": null,  "on_behalf_of": null,  "pause_collection": null,  "payment_settings": {    "payment_method_options": null,    "payment_method_types": null,    "save_default_payment_method": "off"  },  "pending_invoice_item_interval": null,  "pending_setup_intent": null,  "pending_update": null,  "schedule": null,  "start_date": 1679609767,  "status": "active",  "test_clock": null,  "transfer_data": null,  "trial_end": null,  "trial_settings": {    "end_behavior": {      "missing_payment_method": "create_invoice"    }  },  "trial_start": null}`# Retrieve a subscription

Retrieves the subscription with the given ID.

### Parameters

No parameters.

### Returns

Returns the subscription object.

GET/v1/subscriptions/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/subscriptions/sub_1MowQVLkdIwHu7ixeRlqHVzs \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "sub_1MowQVLkdIwHu7ixeRlqHVzs",  "object": "subscription",  "application": null,  "application_fee_percent": null,  "automatic_tax": {    "enabled": false,    "liability": null  },  "billing_cycle_anchor": 1679609767,  "billing_thresholds": null,  "cancel_at": null,  "cancel_at_period_end": false,  "canceled_at": null,  "cancellation_details": {    "comment": null,    "feedback": null,    "reason": null  },  "collection_method": "charge_automatically",  "created": 1679609767,  "currency": "usd",  "current_period_end": 1682288167,  "current_period_start": 1679609767,  "customer": "cus_Na6dX7aXxi11N4",  "days_until_due": null,  "default_payment_method": null,  "default_source": null,  "default_tax_rates": [],  "description": null,  "discount": null,  "ended_at": null,  "invoice_settings": {    "issuer": {      "type": "self"    }  },  "items": {    "object": "list",    "data": [      {        "id": "si_Na6dzxczY5fwHx",        "object": "subscription_item",        "billing_thresholds": null,        "created": 1679609768,        "metadata": {},        "plan": {          "id": "price_1MowQULkdIwHu7ixraBm864M",          "object": "plan",          "active": true,          "aggregate_usage": null,          "amount": 1000,          "amount_decimal": "1000",          "billing_scheme": "per_unit",          "created": 1679609766,          "currency": "usd",          "interval": "month",          "interval_count": 1,          "livemode": false,          "metadata": {},          "nickname": null,          "product": "prod_Na6dGcTsmU0I4R",          "tiers_mode": null,          "transform_usage": null,          "trial_period_days": null,          "usage_type": "licensed"        },        "price": {          "id": "price_1MowQULkdIwHu7ixraBm864M",          "object": "price",          "active": true,          "billing_scheme": "per_unit",          "created": 1679609766,          "currency": "usd",          "custom_unit_amount": null,          "livemode": false,          "lookup_key": null,          "metadata": {},          "nickname": null,          "product": "prod_Na6dGcTsmU0I4R",          "recurring": {            "aggregate_usage": null,            "interval": "month",            "interval_count": 1,            "trial_period_days": null,            "usage_type": "licensed"          },          "tax_behavior": "unspecified",          "tiers_mode": null,          "transform_quantity": null,          "type": "recurring",          "unit_amount": 1000,          "unit_amount_decimal": "1000"        },        "quantity": 1,        "subscription": "sub_1MowQVLkdIwHu7ixeRlqHVzs",        "tax_rates": []      }    ],    "has_more": false,    "total_count": 1,    "url": "/v1/subscription_items?subscription=sub_1MowQVLkdIwHu7ixeRlqHVzs"  },  "latest_invoice": "in_1MowQWLkdIwHu7ixuzkSPfKd",  "livemode": false,  "metadata": {},  "next_pending_invoice_item_invoice": null,  "on_behalf_of": null,  "pause_collection": null,  "payment_settings": {    "payment_method_options": null,    "payment_method_types": null,    "save_default_payment_method": "off"  },  "pending_invoice_item_interval": null,  "pending_setup_intent": null,  "pending_update": null,  "schedule": null,  "start_date": 1679609767,  "status": "active",  "test_clock": null,  "transfer_data": null,  "trial_end": null,  "trial_settings": {    "end_behavior": {      "missing_payment_method": "create_invoice"    }  },  "trial_start": null}`# List subscriptions

By default, returns a list of subscriptions that have not been canceled. In order to list canceled subscriptions, specify status=canceled.

### Parameters

- customerstringThe ID of the customer whose subscriptions will be retrieved.


- pricestringFilter for subscriptions that contain this recurring price ID.


- statusenumThe status of the subscriptions to retrieve. Passing in a value of canceled will return all canceled subscriptions, including those belonging to deleted customers. Pass ended to find subscriptions that are canceled and subscriptions that are expired due to incomplete payment. Passing in a value of all will return subscriptions of all statuses. If no value is supplied, all subscriptions that have not been canceled are returned.



### More parametersExpand all

- automatic_taxobject
- collection_methodenum
- createdobject
- ending_beforestring
- limitinteger
- starting_afterstring
- test_clockstring

### Returns

Returns a list of subscriptions.

GET/v1/subscriptionsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/subscriptions \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/subscriptions",  "has_more": false,  "data": [    {      "id": "sub_1MowQVLkdIwHu7ixeRlqHVzs",      "object": "subscription",      "application": null,      "application_fee_percent": null,      "automatic_tax": {        "enabled": false,        "liability": null      },      "billing_cycle_anchor": 1679609767,      "billing_thresholds": null,      "cancel_at": null,      "cancel_at_period_end": false,      "canceled_at": null,      "cancellation_details": {        "comment": null,        "feedback": null,        "reason": null      },      "collection_method": "charge_automatically",      "created": 1679609767,      "currency": "usd",      "current_period_end": 1682288167,      "current_period_start": 1679609767,      "customer": "cus_Na6dX7aXxi11N4",      "days_until_due": null,      "default_payment_method": null,      "default_source": null,      "default_tax_rates": [],      "description": null,      "discount": null,      "ended_at": null,      "invoice_settings": {        "issuer": {          "type": "self"        }      },      "items": {        "object": "list",        "data": [          {            "id": "si_Na6dzxczY5fwHx",            "object": "subscription_item",            "billing_thresholds": null,            "created": 1679609768,            "metadata": {},            "plan": {              "id": "price_1MowQULkdIwHu7ixraBm864M",              "object": "plan",              "active": true,              "aggregate_usage": null,              "amount": 1000,              "amount_decimal": "1000",              "billing_scheme": "per_unit",              "created": 1679609766,              "currency": "usd",              "interval": "month",              "interval_count": 1,              "livemode": false,              "metadata": {},              "nickname": null,              "product": "prod_Na6dGcTsmU0I4R",              "tiers_mode": null,              "transform_usage": null,              "trial_period_days": null,              "usage_type": "licensed"            },            "price": {              "id": "price_1MowQULkdIwHu7ixraBm864M",              "object": "price",              "active": true,              "billing_scheme": "per_unit",              "created": 1679609766,              "currency": "usd",              "custom_unit_amount": null,              "livemode": false,              "lookup_key": null,              "metadata": {},              "nickname": null,              "product": "prod_Na6dGcTsmU0I4R",              "recurring": {                "aggregate_usage": null,                "interval": "month",                "interval_count": 1,                "trial_period_days": null,                "usage_type": "licensed"              },              "tax_behavior": "unspecified",              "tiers_mode": null,              "transform_quantity": null,              "type": "recurring",              "unit_amount": 1000,              "unit_amount_decimal": "1000"            },            "quantity": 1,            "subscription": "sub_1MowQVLkdIwHu7ixeRlqHVzs",            "tax_rates": []          }        ],        "has_more": false,        "total_count": 1,        "url": "/v1/subscription_items?subscription=sub_1MowQVLkdIwHu7ixeRlqHVzs"      },      "latest_invoice": "in_1MowQWLkdIwHu7ixuzkSPfKd",      "livemode": false,      "metadata": {},      "next_pending_invoice_item_invoice": null,      "on_behalf_of": null,      "pause_collection": null,      "payment_settings": {        "payment_method_options": null,        "payment_method_types": null,        "save_default_payment_method": "off"      },      "pending_invoice_item_interval": null,      "pending_setup_intent": null,      "pending_update": null,      "schedule": null,      "start_date": 1679609767,      "status": "active",      "test_clock": null,      "transfer_data": null,      "trial_end": null,      "trial_settings": {        "end_behavior": {          "missing_payment_method": "create_invoice"        }      },      "trial_start": null    }    {...}    {...}  ],}`# Cancel a subscription

Cancels a customer’s subscription immediately. The customer will not be charged again for the subscription.

Note, however, that any pending invoice items that you’ve created will still be charged for at the end of the period, unless manually deleted. If you’ve set the subscription to cancel at the end of the period, any pending prorations will also be left in place and collected at the end of the period. But if the subscription is set to cancel immediately, pending prorations will be removed.

By default, upon subscription cancellation, Stripe will stop automatic collection of all finalized invoices for the customer. This is intended to prevent unexpected payment attempts after the customer has canceled a subscription. However, you can resume automatic collection of the invoices manually after subscription cancellation to have us proceed. Or, you could check for unpaid invoices before allowing the customer to cancel the subscription at all.

### Parameters

No parameters.

### More parametersExpand all

- cancellation_detailsobject
- invoice_nowboolean
- prorateboolean

### Returns

The canceled Subscription object. Its subscription status will be set to canceled.

DELETE/v1/subscriptions/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X DELETE https://api.stripe.com/v1/subscriptions/sub_1MlPf9LkdIwHu7ixB6VIYRyX \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "sub_1MlPf9LkdIwHu7ixB6VIYRyX",  "object": "subscription",  "application": null,  "application_fee_percent": null,  "automatic_tax": {    "enabled": false,    "liability": null  },  "billing_cycle_anchor": 1678768838,  "billing_thresholds": null,  "cancel_at": null,  "cancel_at_period_end": false,  "canceled_at": 1678768842,  "cancellation_details": {    "comment": null,    "feedback": null,    "reason": "cancellation_requested"  },  "collection_method": "charge_automatically",  "created": 1678768838,  "currency": "usd",  "current_period_end": 1681447238,  "current_period_start": 1678768838,  "customer": "cus_NWSaVkvdacCUi4",  "days_until_due": null,  "default_payment_method": null,  "default_source": null,  "default_tax_rates": [],  "description": null,  "discount": null,  "ended_at": 1678768842,  "invoice_settings": {    "issuer": {      "type": "self"    }  },  "items": {    "object": "list",    "data": [      {        "id": "si_NWSaWTp80M123q",        "object": "subscription_item",        "billing_thresholds": null,        "created": 1678768839,        "metadata": {},        "plan": {          "id": "price_1MlPf7LkdIwHu7ixgcbP7cwE",          "object": "plan",          "active": true,          "aggregate_usage": null,          "amount": 1099,          "amount_decimal": "1099",          "billing_scheme": "per_unit",          "created": 1678768837,          "currency": "usd",          "interval": "month",          "interval_count": 1,          "livemode": false,          "metadata": {},          "nickname": null,          "product": "prod_NWSaMgipulx8IQ",          "tiers_mode": null,          "transform_usage": null,          "trial_period_days": null,          "usage_type": "licensed"        },        "price": {          "id": "price_1MlPf7LkdIwHu7ixgcbP7cwE",          "object": "price",          "active": true,          "billing_scheme": "per_unit",          "created": 1678768837,          "currency": "usd",          "custom_unit_amount": null,          "livemode": false,          "lookup_key": null,          "metadata": {},          "nickname": null,          "product": "prod_NWSaMgipulx8IQ",          "recurring": {            "aggregate_usage": null,            "interval": "month",            "interval_count": 1,            "trial_period_days": null,            "usage_type": "licensed"          },          "tax_behavior": "unspecified",          "tiers_mode": null,          "transform_quantity": null,          "type": "recurring",          "unit_amount": 1099,          "unit_amount_decimal": "1099"        },        "quantity": 1,        "subscription": "sub_1MlPf9LkdIwHu7ixB6VIYRyX",        "tax_rates": []      }    ],    "has_more": false,    "total_count": 1,    "url": "/v1/subscription_items?subscription=sub_1MlPf9LkdIwHu7ixB6VIYRyX"  },  "latest_invoice": "in_1MlPf9LkdIwHu7ixEo6hdgCw",  "livemode": false,  "metadata": {},  "next_pending_invoice_item_invoice": null,  "on_behalf_of": null,  "pause_collection": null,  "payment_settings": {    "payment_method_options": null,    "payment_method_types": null,    "save_default_payment_method": "off"  },  "pending_invoice_item_interval": null,  "pending_setup_intent": null,  "pending_update": null,  "plan": {    "id": "price_1MlPf7LkdIwHu7ixgcbP7cwE",    "object": "plan",    "active": true,    "aggregate_usage": null,    "amount": 1099,    "amount_decimal": "1099",    "billing_scheme": "per_unit",    "created": 1678768837,    "currency": "usd",    "interval": "month",    "interval_count": 1,    "livemode": false,    "metadata": {},    "nickname": null,    "product": "prod_NWSaMgipulx8IQ",    "tiers_mode": null,    "transform_usage": null,    "trial_period_days": null,    "usage_type": "licensed"  },  "quantity": 1,  "schedule": null,  "start_date": 1678768838,  "status": "canceled",  "test_clock": null,  "transfer_data": null,  "trial_end": null,  "trial_settings": {    "end_behavior": {      "missing_payment_method": "create_invoice"    }  },  "trial_start": null}`# Resume a subscription

Initiates resumption of a paused subscription, optionally resetting the billing cycle anchor and creating prorations. If a resumption invoice is generated, it must be paid or marked uncollectible before the subscription will be unpaused. If payment succeeds the subscription will become active, and if payment fails the subscription will be past_due. The resumption invoice will void automatically if not paid by the expiration date.

### Parameters

- billing_cycle_anchorstringEither now or unchanged. Setting the value to now resets the subscription’s billing cycle anchor to the current time (in UTC). Setting the value to unchanged advances the subscription’s billing cycle anchor to the period that surrounds the current time. For more information, see the billing cycle documentation.


- proration_behaviorenumDetermines how to handle prorations when the billing cycle changes (e.g., when switching plans, resetting billing_cycle_anchor=now, or starting a trial), or if an item’s quantity changes. The default value is create_prorations.

Possible enum values`always_invoice`Always invoice immediately for prorations.

`create_prorations`Will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under certain conditions.

`none`Disable creating prorations in this request.



### More parametersExpand all

- proration_datetimestamp

### Returns

The subscription object.

POST/v1/subscriptions/:id/resumeServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/subscriptions/sub_1MoGGtLkdIwHu7ixk5CfdiqC/resume \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d billing_cycle_anchor=now`Response`{  "id": "sub_1MoGGtLkdIwHu7ixk5CfdiqC",  "object": "subscription",  "application": null,  "application_fee_percent": null,  "automatic_tax": {    "enabled": false,    "liability": null  },  "billing_cycle_anchor": 1679447726,  "billing_thresholds": null,  "cancel_at": null,  "cancel_at_period_end": false,  "canceled_at": null,  "cancellation_details": {    "comment": null,    "feedback": null,    "reason": null  },  "collection_method": "charge_automatically",  "created": 1679447723,  "currency": "usd",  "current_period_end": 1682126126,  "current_period_start": 1679447726,  "customer": "cus_NZP5i1diUz55jp",  "days_until_due": null,  "default_payment_method": null,  "default_source": null,  "default_tax_rates": [],  "description": null,  "discount": null,  "ended_at": null,  "invoice_settings": {    "issuer": {      "type": "self"    }  },  "items": {    "object": "list",    "data": [      {        "id": "si_NZP5BhUIuWzXDG",        "object": "subscription_item",        "billing_thresholds": null,        "created": 1679447724,        "metadata": {},        "plan": {          "id": "price_1MoGGsLkdIwHu7ixA9yHsq2N",          "object": "plan",          "active": true,          "aggregate_usage": null,          "amount": 1099,          "amount_decimal": "1099",          "billing_scheme": "per_unit",          "created": 1679447722,          "currency": "usd",          "interval": "month",          "interval_count": 1,          "livemode": false,          "metadata": {},          "nickname": null,          "product": "prod_NZP5rEATBlScM9",          "tiers_mode": null,          "transform_usage": null,          "trial_period_days": null,          "usage_type": "licensed"        },        "price": {          "id": "price_1MoGGsLkdIwHu7ixA9yHsq2N",          "object": "price",          "active": true,          "billing_scheme": "per_unit",          "created": 1679447722,          "currency": "usd",          "custom_unit_amount": null,          "livemode": false,          "lookup_key": null,          "metadata": {},          "nickname": null,          "product": "prod_NZP5rEATBlScM9",          "recurring": {            "aggregate_usage": null,            "interval": "month",            "interval_count": 1,            "trial_period_days": null,            "usage_type": "licensed"          },          "tax_behavior": "unspecified",          "tiers_mode": null,          "transform_quantity": null,          "type": "recurring",          "unit_amount": 1099,          "unit_amount_decimal": "1099"        },        "quantity": 1,        "subscription": "sub_1MoGGtLkdIwHu7ixk5CfdiqC",        "tax_rates": []      }    ],    "has_more": false,    "total_count": 1,    "url": "/v1/subscription_items?subscription=sub_1MoGGtLkdIwHu7ixk5CfdiqC"  },  "latest_invoice": "in_1MoGGwLkdIwHu7ixHSrelo8X",  "livemode": false,  "metadata": {},  "next_pending_invoice_item_invoice": null,  "on_behalf_of": null,  "pause_collection": null,  "payment_settings": {    "payment_method_options": null,    "payment_method_types": null,    "save_default_payment_method": "off"  },  "pending_invoice_item_interval": null,  "pending_setup_intent": null,  "pending_update": null,  "plan": {    "id": "price_1MoGGsLkdIwHu7ixA9yHsq2N",    "object": "plan",    "active": true,    "aggregate_usage": null,    "amount": 1099,    "amount_decimal": "1099",    "billing_scheme": "per_unit",    "created": 1679447722,    "currency": "usd",    "interval": "month",    "interval_count": 1,    "livemode": false,    "metadata": {},    "nickname": null,    "product": "prod_NZP5rEATBlScM9",    "tiers_mode": null,    "transform_usage": null,    "trial_period_days": null,    "usage_type": "licensed"  },  "quantity": 1,  "schedule": null,  "start_date": 1679447723,  "status": "active",  "test_clock": null,  "transfer_data": null,  "trial_end": null,  "trial_settings": {    "end_behavior": {      "missing_payment_method": "create_invoice"    }  },  "trial_start": null}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`