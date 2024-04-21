htmlThe Price object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The Price object

### Attributes

- idstringUnique identifier for the object.


- activebooleanWhether the price can be used for new purchases.


- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- nicknamenullablestringA brief description of the price, hidden from customers.


- productstringExpandableThe ID of the product this price is associated with.


- recurringnullableobjectThe recurring components of a price such as interval and usage_type.

Show child attributes
- typeenumOne of one_time or recurring depending on whether the price is for a one-time purchase or a recurring (subscription) purchase.

Possible enum values`one_time``recurring`
- unit_amountnullableintegerThe unit amount in cents to be charged, represented as a whole integer if possible. Only set if billing_scheme=per_unit.



### More attributesExpand all

- objectstring
- billing_schemeenum
- createdtimestamp
- currency_optionsnullableobjectExpandable
- custom_unit_amountnullableobject
- livemodeboolean
- lookup_keynullablestring
- tax_behaviornullableenum
- tiersnullablearray of objectsExpandable
- tiers_modenullableenum
- transform_quantitynullableobject
- unit_amount_decimalnullabledecimal string

The Price object`{  "id": "price_1MoBy5LkdIwHu7ixZhnattbh",  "object": "price",  "active": true,  "billing_scheme": "per_unit",  "created": 1679431181,  "currency": "usd",  "custom_unit_amount": null,  "livemode": false,  "lookup_key": null,  "metadata": {},  "nickname": null,  "product": "prod_NZKdYqrwEYx6iK",  "recurring": {    "aggregate_usage": null,    "interval": "month",    "interval_count": 1,    "trial_period_days": null,    "usage_type": "licensed"  },  "tax_behavior": "unspecified",  "tiers_mode": null,  "transform_quantity": null,  "type": "recurring",  "unit_amount": 1000,  "unit_amount_decimal": "1000"}`# Create a price

Creates a new price for an existing product. The price can be recurring or one-time.

### Parameters

- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.


- activebooleanWhether the price can be used for new purchases. Defaults to true.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- nicknamestringA brief description of the price, hidden from customers.


- productstringRequired unless product_data is providedThe ID of the product that this price will belong to.


- recurringobjectThe recurring components of a price such as interval and usage_type.

Show child parameters
- unit_amountintegerRequired conditionallyA positive integer in cents (or 0 for a free price) representing how much to charge. One of unit_amount or custom_unit_amount is required, unless billing_scheme=tiered.



### More parametersExpand all

- billing_schemeenum
- currency_optionsobject
- custom_unit_amountobjectRequired unless unit_amount is provided
- lookup_keystring
- product_dataobjectRequired unless product is provided
- tax_behaviorenum
- tiersarray of objectsRequired if billing_scheme=tiered
- tiers_modeenumRequired if billing_scheme=tiered
- transfer_lookup_keyboolean
- transform_quantityobject
- unit_amount_decimalstring

### Returns

The newly created Price object is returned upon success. Otherwise, this call raises an error.

POST/v1/pricesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/prices \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d currency=usd \  -d unit_amount=1000 \  -d "recurring[interval]"=month \  -d "product_data[name]"="Gold Plan"`Response`{  "id": "price_1MoBy5LkdIwHu7ixZhnattbh",  "object": "price",  "active": true,  "billing_scheme": "per_unit",  "created": 1679431181,  "currency": "usd",  "custom_unit_amount": null,  "livemode": false,  "lookup_key": null,  "metadata": {},  "nickname": null,  "product": "prod_NZKdYqrwEYx6iK",  "recurring": {    "aggregate_usage": null,    "interval": "month",    "interval_count": 1,    "trial_period_days": null,    "usage_type": "licensed"  },  "tax_behavior": "unspecified",  "tiers_mode": null,  "transform_quantity": null,  "type": "recurring",  "unit_amount": 1000,  "unit_amount_decimal": "1000"}`# Update a price

Updates the specified price by setting the values of the parameters passed. Any parameters not provided are left unchanged.

### Parameters

- activebooleanWhether the price can be used for new purchases. Defaults to true.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- nicknamestringA brief description of the price, hidden from customers.



### More parametersExpand all

- currency_optionsobject
- lookup_keystring
- tax_behaviorenum
- transfer_lookup_keyboolean

### Returns

The updated price object is returned upon success. Otherwise, this call raises an error.

POST/v1/prices/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/prices/price_1MoBy5LkdIwHu7ixZhnattbh \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "price_1MoBy5LkdIwHu7ixZhnattbh",  "object": "price",  "active": true,  "billing_scheme": "per_unit",  "created": 1679431181,  "currency": "usd",  "custom_unit_amount": null,  "livemode": false,  "lookup_key": null,  "metadata": {    "order_id": "6735"  },  "nickname": null,  "product": "prod_NZKdYqrwEYx6iK",  "recurring": {    "aggregate_usage": null,    "interval": "month",    "interval_count": 1,    "trial_period_days": null,    "usage_type": "licensed"  },  "tax_behavior": "unspecified",  "tiers_mode": null,  "transform_quantity": null,  "type": "recurring",  "unit_amount": 1000,  "unit_amount_decimal": "1000"}`# Retrieve a price

Retrieves the price with the given ID.

### Parameters

No parameters.

### Returns

Returns a price if a valid price or plan ID was provided. Raises an error otherwise.

GET/v1/prices/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/prices/price_1MoBy5LkdIwHu7ixZhnattbh \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "price_1MoBy5LkdIwHu7ixZhnattbh",  "object": "price",  "active": true,  "billing_scheme": "per_unit",  "created": 1679431181,  "currency": "usd",  "custom_unit_amount": null,  "livemode": false,  "lookup_key": null,  "metadata": {},  "nickname": null,  "product": "prod_NZKdYqrwEYx6iK",  "recurring": {    "aggregate_usage": null,    "interval": "month",    "interval_count": 1,    "trial_period_days": null,    "usage_type": "licensed"  },  "tax_behavior": "unspecified",  "tiers_mode": null,  "transform_quantity": null,  "type": "recurring",  "unit_amount": 1000,  "unit_amount_decimal": "1000"}`# List all prices

Returns a list of your active prices, excluding inline prices. For the list of inactive prices, set active to false.

### Parameters

- activebooleanOnly return prices that are active or inactive (e.g., pass false to list all inactive prices).


- currencyenumOnly return prices for the given currency.


- productstringOnly return prices for the given product.


- typeenumOnly return prices of type recurring or one_time.

Possible enum values`one_time``recurring`

### More parametersExpand all

- createdobject
- ending_beforestring
- limitinteger
- lookup_keysarray of strings
- recurringobject
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit prices, starting after prices starting_after. Each entry in the array is a separate price object. If no more prices are available, the resulting array will be empty.

GET/v1/pricesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/prices \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/prices",  "has_more": false,  "data": [    {      "id": "price_1MoBy5LkdIwHu7ixZhnattbh",      "object": "price",      "active": true,      "billing_scheme": "per_unit",      "created": 1679431181,      "currency": "usd",      "custom_unit_amount": null,      "livemode": false,      "lookup_key": null,      "metadata": {},      "nickname": null,      "product": "prod_NZKdYqrwEYx6iK",      "recurring": {        "aggregate_usage": null,        "interval": "month",        "interval_count": 1,        "trial_period_days": null,        "usage_type": "licensed"      },      "tax_behavior": "unspecified",      "tiers_mode": null,      "transform_quantity": null,      "type": "recurring",      "unit_amount": 1000,      "unit_amount_decimal": "1000"    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`