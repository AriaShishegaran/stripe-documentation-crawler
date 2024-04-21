htmlThe Coupon object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The Coupon object

### Attributes

- idstringUnique identifier for the object.


- amount_offnullableintegerAmount (in the currency specified) that will be taken off the subtotal of any invoices for this customer.


- currencynullableenumIf amount_off has been set, the three-letter ISO code for the currency of the amount to take off.


- durationenumOne of forever, once, and repeating. Describes how long a customer who applies this coupon will get the discount.

Possible enum values`forever`Applies to all charges from a subscription with this coupon applied.

`once`Applies to the first charge from a subscription with this coupon applied.

`repeating`Applies to charges in the first duration_in_months months from a subscription with this coupon applied.


- duration_in_monthsnullableintegerIf duration is repeating, the number of months the coupon applies. Null if coupon duration is forever or once.


- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- namenullablestringName of the coupon displayed to customers on for instance invoices or receipts.


- percent_offnullablefloatPercent that will be taken off the subtotal of any invoices for this customer for the duration of the coupon. For example, a coupon with percent_off of 50 will make a $100 invoice $50 instead.



### More attributesExpand all

- objectstring
- applies_tonullableobjectExpandable
- createdtimestamp
- currency_optionsnullableobjectExpandable
- livemodeboolean
- max_redemptionsnullableinteger
- redeem_bynullabletimestamp
- times_redeemedinteger
- validboolean

The Coupon object`{  "id": "jMT0WJUD",  "object": "coupon",  "amount_off": null,  "created": 1678037688,  "currency": null,  "duration": "repeating",  "duration_in_months": 3,  "livemode": false,  "max_redemptions": null,  "metadata": {},  "name": null,  "percent_off": 25.5,  "redeem_by": null,  "times_redeemed": 0,  "valid": true}`# Create a coupon

You can create coupons easily via the coupon management page of the Stripe dashboard. Coupon creation is also accessible via the API if you need to create coupons on the fly.

A coupon has either a percent_off or an amount_off and currency. If you set an amount_off, that amount will be subtracted from any invoice’s subtotal. For example, an invoice with a subtotal of 100 EUR will have a final total of 0 EUR if a coupon with an amount_off of 20000 is applied to it and an invoice with a subtotal of 300 EUR will have a final total of 100 EUR if a coupon with an amount_off of 20000 is applied to it.

### Parameters

- amount_offintegerA positive integer representing the amount to subtract from an invoice total (required if percent_off is not passed).


- currencyenumThree-letter ISO code for the currency of the amount_off parameter (required if amount_off is passed).


- durationenumSpecifies how long the discount will be in effect if used on a subscription. Defaults to once.

Possible enum values`forever`Applies to all charges from a subscription with this coupon applied.

`once`Applies to the first charge from a subscription with this coupon applied.

`repeating`Applies to charges in the first duration_in_months months from a subscription with this coupon applied.


- duration_in_monthsintegerRequired only if duration is repeating, in which case it must be a positive integer that specifies the number of months the discount will be in effect.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- namestringName of the coupon displayed to customers on, for instance invoices, or receipts. By default the id is shown if name is not set.


- percent_offfloatA positive float larger than 0, and smaller or equal to 100, that represents the discount the coupon will apply (required if amount_off is not passed).



### More parametersExpand all

- applies_toobject
- currency_optionsobject
- idstring
- max_redemptionsinteger
- redeem_bytimestamp

### Returns

Returns the coupon object.

POST/v1/couponsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/coupons \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d duration=repeating \  -d duration_in_months=3 \  -d percent_off="25.5"`Response`{  "id": "jMT0WJUD",  "object": "coupon",  "amount_off": null,  "created": 1678037688,  "currency": null,  "duration": "repeating",  "duration_in_months": 3,  "livemode": false,  "max_redemptions": null,  "metadata": {},  "name": null,  "percent_off": 25.5,  "redeem_by": null,  "times_redeemed": 0,  "valid": true}`# Update a coupon

Updates the metadata of a coupon. Other coupon details (currency, duration, amount_off) are, by design, not editable.

### Parameters

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- namestringName of the coupon displayed to customers on, for instance invoices, or receipts. By default the id is shown if name is not set.



### More parametersExpand all

- currency_optionsobject

### Returns

The newly updated coupon object if the call succeeded. Otherwise, this call raises an error, such as if the coupon has been deleted.

POST/v1/coupons/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/coupons/jMT0WJUD \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "jMT0WJUD",  "object": "coupon",  "amount_off": null,  "created": 1678037688,  "currency": null,  "duration": "repeating",  "duration_in_months": 3,  "livemode": false,  "max_redemptions": null,  "metadata": {    "order_id": "6735"  },  "name": null,  "percent_off": 25.5,  "redeem_by": null,  "times_redeemed": 0,  "valid": true}`# Retrieve a coupon

Retrieves the coupon with the given ID.

### Parameters

No parameters.

### Returns

Returns a coupon if a valid coupon ID was provided. Raises an error otherwise.

GET/v1/coupons/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/coupons/jMT0WJUD \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "jMT0WJUD",  "object": "coupon",  "amount_off": null,  "created": 1678037688,  "currency": null,  "duration": "repeating",  "duration_in_months": 3,  "livemode": false,  "max_redemptions": null,  "metadata": {},  "name": null,  "percent_off": 25.5,  "redeem_by": null,  "times_redeemed": 0,  "valid": true}`# List all coupons

Returns a list of your coupons.

### Parameters

No parameters.

### More parametersExpand all

- createdobject
- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit coupons, starting after coupon starting_after. Each entry in the array is a separate coupon object. If no more coupons are available, the resulting array will be empty.

GET/v1/couponsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/coupons \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/coupons",  "has_more": false,  "data": [    {      "id": "jMT0WJUD",      "object": "coupon",      "amount_off": null,      "created": 1678037688,      "currency": null,      "duration": "repeating",      "duration_in_months": 3,      "livemode": false,      "max_redemptions": null,      "metadata": {},      "name": null,      "percent_off": 25.5,      "redeem_by": null,      "times_redeemed": 0,      "valid": true    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`