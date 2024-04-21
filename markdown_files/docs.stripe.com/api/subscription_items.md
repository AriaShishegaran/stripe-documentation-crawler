htmlSubscription Items | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Subscription Items

Subscription items allow you to create customer subscriptions with more than one plan, making it easy to represent complex billing relationships.

Endpoints
# The Subscription Item object

### Attributes

- idstringUnique identifier for the object.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- priceobjectThe price the customer is subscribed to.

Show child attributes
- quantitynullableintegerThe quantity of the plan to which the customer should be subscribed.


- subscriptionstringThe subscription this subscription_item belongs to.



### More attributesExpand all

- objectstring
- billing_thresholdsnullableobject
- createdinteger
- discountsarray of stringsExpandable
- tax_ratesnullablearray of objects

The Subscription Item object`{  "id": "si_NcLYdDxLHxlFo7",  "object": "subscription_item",  "billing_thresholds": null,  "created": 1680126546,  "metadata": {},  "price": {    "id": "price_1Mr6rdLkdIwHu7ixwPmiybbR",    "object": "price",    "active": true,    "billing_scheme": "per_unit",    "created": 1680126545,    "currency": "usd",    "custom_unit_amount": null,    "livemode": false,    "lookup_key": null,    "metadata": {},    "nickname": null,    "product": "prod_NcLYGKH0eY5b8s",    "recurring": {      "aggregate_usage": null,      "interval": "month",      "interval_count": 1,      "trial_period_days": null,      "usage_type": "licensed"    },    "tax_behavior": "unspecified",    "tiers_mode": null,    "transform_quantity": null,    "type": "recurring",    "unit_amount": 1000,    "unit_amount_decimal": "1000"  },  "quantity": 2,  "subscription": "sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd",  "tax_rates": []}`# Create a subscription item

Adds a new item to an existing subscription. No existing items will be changed or replaced.

### Parameters

- subscriptionstringRequiredThe identifier of the subscription to modify.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- payment_behaviorenumUse allow_incomplete to transition the subscription to status=past_due if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription’s invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the SCA Migration Guide for Billing to learn more. This is the default behavior.

Use default_incomplete to transition the subscription to status=past_due when payment is required and await explicit confirmation of the invoice’s payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, SCA regulation, or collecting a mandate for a bank debit payment method.

Use pending_if_incomplete to update the subscription using pending updates. When you use pending_if_incomplete you can only pass the parameters supported by pending updates.

Use error_if_incomplete if you want Stripe to return an HTTP 402 status code if a subscription’s invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the changelog to learn more.

Possible enum values`allow_incomplete``default_incomplete``error_if_incomplete``pending_if_incomplete`
- pricestringThe ID of the price object.


- proration_behaviorenumDetermines how to handle prorations when the billing cycle changes (e.g., when switching plans, resetting billing_cycle_anchor=now, or starting a trial), or if an item’s quantity changes. The default value is create_prorations.

Possible enum values`always_invoice`Always invoice immediately for prorations.

`create_prorations`Will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under certain conditions.

`none`Disable creating prorations in this request.


- quantityintegerThe quantity you’d like to apply to the subscription item you’re creating.



### More parametersExpand all

- billing_thresholdsobject
- discountsarray of objects
- price_dataobject
- proration_datetimestamp
- tax_ratesarray of strings

### Returns

Returns the created Subscription Item object, if successful. Otherwise, this call raises an error.

POST/v1/subscription_itemsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/subscription_items \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d subscription=sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd \  -d price=price_1Mr6rdLkdIwHu7ixwPmiybbR \  -d quantity=2`Response`{  "id": "si_NcLYdDxLHxlFo7",  "object": "subscription_item",  "billing_thresholds": null,  "created": 1680126546,  "metadata": {},  "price": {    "id": "price_1Mr6rdLkdIwHu7ixwPmiybbR",    "object": "price",    "active": true,    "billing_scheme": "per_unit",    "created": 1680126545,    "currency": "usd",    "custom_unit_amount": null,    "livemode": false,    "lookup_key": null,    "metadata": {},    "nickname": null,    "product": "prod_NcLYGKH0eY5b8s",    "recurring": {      "aggregate_usage": null,      "interval": "month",      "interval_count": 1,      "trial_period_days": null,      "usage_type": "licensed"    },    "tax_behavior": "unspecified",    "tiers_mode": null,    "transform_quantity": null,    "type": "recurring",    "unit_amount": 1000,    "unit_amount_decimal": "1000"  },  "quantity": 2,  "subscription": "sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd",  "tax_rates": []}`# Update a subscription item

Updates the plan or quantity of an item on a current subscription.

### Parameters

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- payment_behaviorenumUse allow_incomplete to transition the subscription to status=past_due if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription’s invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the SCA Migration Guide for Billing to learn more. This is the default behavior.

Use default_incomplete to transition the subscription to status=past_due when payment is required and await explicit confirmation of the invoice’s payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, SCA regulation, or collecting a mandate for a bank debit payment method.

Use pending_if_incomplete to update the subscription using pending updates. When you use pending_if_incomplete you can only pass the parameters supported by pending updates.

Use error_if_incomplete if you want Stripe to return an HTTP 402 status code if a subscription’s invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the changelog to learn more.

Possible enum values`allow_incomplete``default_incomplete``error_if_incomplete``pending_if_incomplete`
- pricestringThe ID of the price object. When changing a subscription item’s price, quantity is set to 1 unless a quantity parameter is provided.


- proration_behaviorenumDetermines how to handle prorations when the billing cycle changes (e.g., when switching plans, resetting billing_cycle_anchor=now, or starting a trial), or if an item’s quantity changes. The default value is create_prorations.

Possible enum values`always_invoice`Always invoice immediately for prorations.

`create_prorations`Will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under certain conditions.

`none`Disable creating prorations in this request.


- quantityintegerThe quantity you’d like to apply to the subscription item you’re creating.



### More parametersExpand all

- billing_thresholdsobject
- discountsarray of objects
- off_sessionboolean
- price_dataobject
- proration_datetimestamp
- tax_ratesarray of strings

### Returns

POST/v1/subscription_items/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/subscription_items/si_NcLYdDxLHxlFo7 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "si_NcLYdDxLHxlFo7",  "object": "subscription_item",  "billing_thresholds": null,  "created": 1680126546,  "metadata": {    "order_id": "6735"  },  "price": {    "id": "price_1Mr6rdLkdIwHu7ixwPmiybbR",    "object": "price",    "active": true,    "billing_scheme": "per_unit",    "created": 1680126545,    "currency": "usd",    "custom_unit_amount": null,    "livemode": false,    "lookup_key": null,    "metadata": {},    "nickname": null,    "product": "prod_NcLYGKH0eY5b8s",    "recurring": {      "aggregate_usage": null,      "interval": "month",      "interval_count": 1,      "trial_period_days": null,      "usage_type": "licensed"    },    "tax_behavior": "unspecified",    "tiers_mode": null,    "transform_quantity": null,    "type": "recurring",    "unit_amount": 1000,    "unit_amount_decimal": "1000"  },  "quantity": 2,  "subscription": "sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd",  "tax_rates": []}`# Retrieve a subscription item

Retrieves the subscription item with the given ID.

### Parameters

No parameters.

### Returns

Returns a subscription item if a valid subscription item ID was provided. Raises an error otherwise.

GET/v1/subscription_items/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/subscription_items/si_NcLYdDxLHxlFo7 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "si_NcLYdDxLHxlFo7",  "object": "subscription_item",  "billing_thresholds": null,  "created": 1680126546,  "metadata": {},  "price": {    "id": "price_1Mr6rdLkdIwHu7ixwPmiybbR",    "object": "price",    "active": true,    "billing_scheme": "per_unit",    "created": 1680126545,    "currency": "usd",    "custom_unit_amount": null,    "livemode": false,    "lookup_key": null,    "metadata": {},    "nickname": null,    "product": "prod_NcLYGKH0eY5b8s",    "recurring": {      "aggregate_usage": null,      "interval": "month",      "interval_count": 1,      "trial_period_days": null,      "usage_type": "licensed"    },    "tax_behavior": "unspecified",    "tiers_mode": null,    "transform_quantity": null,    "type": "recurring",    "unit_amount": 1000,    "unit_amount_decimal": "1000"  },  "quantity": 2,  "subscription": "sub_1Mr6rbLkdIwHu7ix4Xm9Ahtd",  "tax_rates": []}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`