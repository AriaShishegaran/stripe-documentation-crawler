htmlThe Plan object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The Plan object

### Attributes

- idstringUnique identifier for the object.


- activebooleanWhether the plan can be used for new purchases.


- amountnullableintegerThe unit amount in cents to be charged, represented as a whole integer if possible. Only set if billing_scheme=per_unit.


- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- intervalenumThe frequency at which a subscription is billed. One of day, week, month or year.


- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- nicknamenullablestringA brief description of the plan, hidden from customers.


- productnullablestringExpandableThe product whose pricing this plan determines.



### More attributesExpand all

- objectstring
- aggregate_usagenullableenum
- amount_decimalnullabledecimal string
- billing_schemeenum
- createdtimestamp
- interval_countinteger
- livemodeboolean
- meternullablestringPreview feature
- tiersnullablearray of objectsExpandable
- tiers_modenullableenum
- transform_usagenullableobject
- trial_period_daysnullableinteger
- usage_typeenum

The Plan object`{  "id": "plan_NjpIbv3g3ZibnD",  "object": "plan",  "active": true,  "aggregate_usage": null,  "amount": 1200,  "amount_decimal": "1200",  "billing_scheme": "per_unit",  "created": 1681851647,  "currency": "usd",  "interval": "month",  "interval_count": 1,  "livemode": false,  "metadata": {},  "nickname": null,  "product": "prod_NjpI7DbZx6AlWQ",  "tiers_mode": null,  "transform_usage": null,  "trial_period_days": null,  "usage_type": "licensed"}`# Create a plan

You can now model subscriptions more flexibly using the Prices API. It replaces the Plans API and is backwards compatible to simplify your migration.

### Parameters

- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.


- intervalenumRequiredSpecifies billing frequency. Either day, week, month or year.

Possible enum values`day``month``week``year`
- productobjectRequiredThe product whose pricing the created plan will represent. This can either be the ID of an existing product, or a dictionary containing fields used to create a service product.

Show child parameters
- activebooleanWhether the plan is currently available for new subscriptions. Defaults to true.


- amountintegerRequired unless billing_scheme=tieredA positive integer in cents (or 0 for a free plan) representing how much to charge on a recurring basis.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- nicknamestringA brief description of the plan, hidden from customers.



### More parametersExpand all

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

### Returns

Returns the plan object.

POST/v1/plansServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/plans \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d amount=1200 \  -d currency=usd \  -d interval=month \  -d product=prod_NjpI7DbZx6AlWQ`Response`{  "id": "plan_NjpIbv3g3ZibnD",  "object": "plan",  "active": true,  "aggregate_usage": null,  "amount": 1200,  "amount_decimal": "1200",  "billing_scheme": "per_unit",  "created": 1681851647,  "currency": "usd",  "interval": "month",  "interval_count": 1,  "livemode": false,  "metadata": {},  "nickname": null,  "product": "prod_NjpI7DbZx6AlWQ",  "tiers_mode": null,  "transform_usage": null,  "trial_period_days": null,  "usage_type": "licensed"}`# Update a plan

Updates the specified plan by setting the values of the parameters passed. Any parameters not provided are left unchanged. By design, you cannot change a plan’s ID, amount, currency, or billing cycle.

### Parameters

- activebooleanWhether the plan is currently available for new subscriptions.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- nicknamestringA brief description of the plan, hidden from customers.



### More parametersExpand all

- productstring
- trial_period_daysinteger

### Returns

The updated plan object is returned upon success. Otherwise, this call raises an error.

POST/v1/plans/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/plans/plan_NjpIbv3g3ZibnD \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "plan_NjpIbv3g3ZibnD",  "object": "plan",  "active": true,  "aggregate_usage": null,  "amount": 1200,  "amount_decimal": "1200",  "billing_scheme": "per_unit",  "created": 1681851647,  "currency": "usd",  "interval": "month",  "interval_count": 1,  "livemode": false,  "metadata": {    "order_id": "6735"  },  "nickname": null,  "product": "prod_NjpI7DbZx6AlWQ",  "tiers_mode": null,  "transform_usage": null,  "trial_period_days": null,  "usage_type": "licensed"}`# Retrieve a plan

Retrieves the plan with the given ID.

### Parameters

No parameters.

### Returns

Returns a plan if a valid plan ID was provided. Raises an error otherwise.

GET/v1/plans/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/plans/plan_NjpIbv3g3ZibnD \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "plan_NjpIbv3g3ZibnD",  "object": "plan",  "active": true,  "aggregate_usage": null,  "amount": 1200,  "amount_decimal": "1200",  "billing_scheme": "per_unit",  "created": 1681851647,  "currency": "usd",  "interval": "month",  "interval_count": 1,  "livemode": false,  "metadata": {},  "nickname": null,  "product": "prod_NjpI7DbZx6AlWQ",  "tiers_mode": null,  "transform_usage": null,  "trial_period_days": null,  "usage_type": "licensed"}`# List all plans

Returns a list of your plans.

### Parameters

- activebooleanOnly return plans that are active or inactive (e.g., pass false to list all inactive plans).


- productstringOnly return plans for the given product.



### More parametersExpand all

- createdobject
- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit plans, starting after plan starting_after. Each entry in the array is a separate plan object. If no more plans are available, the resulting array will be empty.

GET/v1/plansServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/plans \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/plans",  "has_more": false,  "data": [    {      "id": "plan_NjpIbv3g3ZibnD",      "object": "plan",      "active": true,      "aggregate_usage": null,      "amount": 1200,      "amount_decimal": "1200",      "billing_scheme": "per_unit",      "created": 1681851647,      "currency": "usd",      "interval": "month",      "interval_count": 1,      "livemode": false,      "metadata": {},      "nickname": null,      "product": "prod_NjpI7DbZx6AlWQ",      "tiers_mode": null,      "transform_usage": null,      "trial_period_days": null,      "usage_type": "licensed"    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`