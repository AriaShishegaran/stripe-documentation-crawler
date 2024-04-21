htmlPromotion Code | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Promotion Code

A Promotion Code represents a customer-redeemable code for a coupon. It can be used to create multiple codes for a single coupon.

Endpoints
# The Promotion Code object

### Attributes

- idstringUnique identifier for the object.


- codestringThe customer-facing code. Regardless of case, this code must be unique across all active promotion codes for each customer.


- couponobjectHash describing the coupon for this promotion code.

Show child attributes
- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.



### More attributesExpand all

- objectstring
- activeboolean
- createdtimestamp
- customernullablestringExpandable
- expires_atnullabletimestamp
- livemodeboolean
- max_redemptionsnullableinteger
- restrictionsobject
- times_redeemedinteger

The Promotion Code object`{  "id": "promo_1MiM6KLkdIwHu7ixrIaX4wgn",  "object": "promotion_code",  "active": true,  "code": "A1H1Q1MG",  "coupon": {    "id": "nVJYDOag",    "object": "coupon",    "amount_off": null,    "created": 1678040164,    "currency": null,    "duration": "repeating",    "duration_in_months": 3,    "livemode": false,    "max_redemptions": null,    "metadata": {},    "name": null,    "percent_off": 25.5,    "redeem_by": null,    "times_redeemed": 0,    "valid": true  },  "created": 1678040164,  "customer": null,  "expires_at": null,  "livemode": false,  "max_redemptions": null,  "metadata": {},  "restrictions": {    "first_time_transaction": false,    "minimum_amount": null,    "minimum_amount_currency": null  },  "times_redeemed": 0}`# Create a promotion code

A promotion code points to a coupon. You can optionally restrict the code to a specific customer, redemption limit, and expiration date.

### Parameters

- couponstringRequiredThe coupon for this promotion code.


- codestringThe customer-facing code. Regardless of case, this code must be unique across all active promotion codes for a specific customer. If left blank, we will generate one automatically.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- activeboolean
- customerstring
- expires_attimestamp
- max_redemptionsinteger
- restrictionsobject

### Returns

Returns the promotion code object.

POST/v1/promotion_codesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/promotion_codes \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d coupon=nVJYDOag`Response`{  "id": "promo_1MiM6KLkdIwHu7ixrIaX4wgn",  "object": "promotion_code",  "active": true,  "code": "A1H1Q1MG",  "coupon": {    "id": "nVJYDOag",    "object": "coupon",    "amount_off": null,    "created": 1678040164,    "currency": null,    "duration": "repeating",    "duration_in_months": 3,    "livemode": false,    "max_redemptions": null,    "metadata": {},    "name": null,    "percent_off": 25.5,    "redeem_by": null,    "times_redeemed": 0,    "valid": true  },  "created": 1678040164,  "customer": null,  "expires_at": null,  "livemode": false,  "max_redemptions": null,  "metadata": {},  "restrictions": {    "first_time_transaction": false,    "minimum_amount": null,    "minimum_amount_currency": null  },  "times_redeemed": 0}`# Update a promotion code

Updates the specified promotion code by setting the values of the parameters passed. Most fields are, by design, not editable.

### Parameters

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- activeboolean
- restrictionsobject

### Returns

The updated promotion code object is returned upon success. Otherwise, this call raises an error.

POST/v1/promotion_codes/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/promotion_codes/promo_1MiM6KLkdIwHu7ixrIaX4wgn \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "promo_1MiM6KLkdIwHu7ixrIaX4wgn",  "object": "promotion_code",  "active": true,  "code": "A1H1Q1MG",  "coupon": {    "id": "nVJYDOag",    "object": "coupon",    "amount_off": null,    "created": 1678040164,    "currency": null,    "duration": "repeating",    "duration_in_months": 3,    "livemode": false,    "max_redemptions": null,    "metadata": {},    "name": null,    "percent_off": 25.5,    "redeem_by": null,    "times_redeemed": 0,    "valid": true  },  "created": 1678040164,  "customer": null,  "expires_at": null,  "livemode": false,  "max_redemptions": null,  "metadata": {    "order_id": "6735"  },  "restrictions": {    "first_time_transaction": false,    "minimum_amount": null,    "minimum_amount_currency": null  },  "times_redeemed": 0}`# Retrieve a promotion code

Retrieves the promotion code with the given ID. In order to retrieve a promotion code by the customer-facing code use list with the desired code.

### Parameters

No parameters.

### Returns

Returns a promotion code if a valid promotion code ID was provided. Raises an error otherwise.

GET/v1/promotion_codes/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/promotion_codes/promo_1MiM6KLkdIwHu7ixrIaX4wgn \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "promo_1MiM6KLkdIwHu7ixrIaX4wgn",  "object": "promotion_code",  "active": true,  "code": "A1H1Q1MG",  "coupon": {    "id": "nVJYDOag",    "object": "coupon",    "amount_off": null,    "created": 1678040164,    "currency": null,    "duration": "repeating",    "duration_in_months": 3,    "livemode": false,    "max_redemptions": null,    "metadata": {},    "name": null,    "percent_off": 25.5,    "redeem_by": null,    "times_redeemed": 0,    "valid": true  },  "created": 1678040164,  "customer": null,  "expires_at": null,  "livemode": false,  "max_redemptions": null,  "metadata": {},  "restrictions": {    "first_time_transaction": false,    "minimum_amount": null,    "minimum_amount_currency": null  },  "times_redeemed": 0}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`