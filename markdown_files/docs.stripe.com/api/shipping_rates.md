htmlShipping Rates | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Shipping Rates

Shipping rates describe the price of shipping presented to your customers and applied to a purchase. For more information, see Charge for shipping.

Endpoints
# The Shipping Rate object

### Attributes

- idstringUnique identifier for the object.


- activebooleanWhether the shipping rate can be used for new purchases. Defaults to true.


- display_namenullablestringThe name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.


- fixed_amountnullableobjectDescribes a fixed amount to charge for shipping. Must be present if type is fixed_amount.

Show child attributes
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- typeenumThe type of calculation to use on the shipping rate. Can only be fixed_amount for now.



### More attributesExpand all

- objectstring
- createdtimestamp
- delivery_estimatenullableobject
- livemodeboolean
- tax_behaviornullableenum
- tax_codenullablestringExpandable

The Shipping Rate object`{  "id": "shr_1MrRx2LkdIwHu7ixikgEA6Wd",  "object": "shipping_rate",  "active": true,  "created": 1680207604,  "delivery_estimate": null,  "display_name": "Ground shipping",  "fixed_amount": {    "amount": 500,    "currency": "usd"  },  "livemode": false,  "metadata": {},  "tax_behavior": "unspecified",  "tax_code": null,  "type": "fixed_amount"}`# Create a shipping rate

Creates a new shipping rate object.

### Parameters

- display_namestringRequiredThe name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.


- fixed_amountobjectDescribes a fixed amount to charge for shipping. Must be present if type is fixed_amount.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- typeenumRequiredThe type of calculation to use on the shipping rate. Can only be fixed_amount for now.



### More parametersExpand all

- delivery_estimateobject
- tax_behaviorenum
- tax_codestring

### Returns

Returns a shipping rate object if the call succeeded.

POST/v1/shipping_ratesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/shipping_rates \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d display_name="Ground shipping" \  -d type=fixed_amount \  -d "fixed_amount[amount]"=500 \  -d "fixed_amount[currency]"=usd`Response`{  "id": "shr_1MrRx2LkdIwHu7ixikgEA6Wd",  "object": "shipping_rate",  "active": true,  "created": 1680207604,  "delivery_estimate": null,  "display_name": "Ground shipping",  "fixed_amount": {    "amount": 500,    "currency": "usd"  },  "livemode": false,  "metadata": {},  "tax_behavior": "unspecified",  "tax_code": null,  "type": "fixed_amount"}`# Update a shipping rate

Updates an existing shipping rate object.

### Parameters

- activebooleanWhether the shipping rate can be used for new purchases. Defaults to true.


- fixed_amountobjectDescribes a fixed amount to charge for shipping. Must be present if type is fixed_amount.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- tax_behaviorenum

### Returns

Returns the modified shipping rate object if the call succeeded.

POST/v1/shipping_rates/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/shipping_rates/shr_1MrRx2LkdIwHu7ixikgEA6Wd \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "shr_1MrRx2LkdIwHu7ixikgEA6Wd",  "object": "shipping_rate",  "active": true,  "created": 1680207604,  "delivery_estimate": null,  "display_name": "Ground shipping",  "fixed_amount": {    "amount": 500,    "currency": "usd"  },  "livemode": false,  "metadata": {    "order_id": "6735"  },  "tax_behavior": "unspecified",  "tax_code": null,  "type": "fixed_amount"}`# Retrieve a shipping rate

Returns the shipping rate object with the given ID.

### Parameters

No parameters.

### Returns

Returns a shipping rate object if a valid identifier was provided.

GET/v1/shipping_rates/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/shipping_rates/shr_1MrRx2LkdIwHu7ixikgEA6Wd \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "shr_1MrRx2LkdIwHu7ixikgEA6Wd",  "object": "shipping_rate",  "active": true,  "created": 1680207604,  "delivery_estimate": null,  "display_name": "Ground shipping",  "fixed_amount": {    "amount": 500,    "currency": "usd"  },  "livemode": false,  "metadata": {},  "tax_behavior": "unspecified",  "tax_code": null,  "type": "fixed_amount"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`