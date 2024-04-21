htmlThe Session object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The Session object

### Attributes

- idstringUnique identifier for the object.


- client_reference_idnullablestringA unique string to reference the Checkout Session. This can be a customer ID, a cart ID, or similar, and can be used to reconcile the Session with your internal systems.


- currencynullableenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- customernullablestringExpandableThe ID of the customer for this Session. For Checkout Sessions in subscription mode or Checkout Sessions with customer_creation set as always in payment mode, Checkout will create a new customer object based on information provided during the payment flow unless an existing customer was provided when the Session was created.


- customer_emailnullablestringIf provided, this value will be used when the Customer object is created. If not provided, customers will be asked to enter their email address. Use this parameter to prefill customer data if you already have an email on file. To access information about the customer once the payment flow is complete, use the customer attribute.


- line_itemsnullableobjectExpandableThe line items purchased by the customer.

Show child attributes
- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- modeenumThe mode of the Checkout Session.

Possible enum values`payment`Accept one-time payments for cards, iDEAL, and more.

`setup`Save payment details to charge your customers later.

`subscription`Use Stripe Billing to set up fixed-price subscriptions.


- payment_intentnullablestringExpandableThe ID of the PaymentIntent for Checkout Sessions in payment mode.


- payment_statusenumThe payment status of the Checkout Session, one of paid, unpaid, or no_payment_required. You can use this value to decide when to fulfill your customer’s order.

Possible enum values`no_payment_required`The payment is delayed to a future date, or the Checkout Session is in setup mode and doesn’t require a payment at this time.

`paid`The payment funds are available in your account.

`unpaid`The payment funds are not yet available in your account.


- return_urlnullablestringApplies to Checkout Sessions with ui_mode: embedded. The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method’s app or site.


- statusnullableenumThe status of the Checkout Session, one of open, complete, or expired.

Possible enum values`complete`The checkout session is complete. Payment processing may still be in progress

`expired`The checkout session has expired. No further processing will occur

`open`The checkout session is still in progress. Payment processing has not started


- success_urlnullablestringThe URL the customer will be directed to after the payment or subscription creation is successful.


- urlnullablestringThe URL to the Checkout Session. Redirect customers to this URL to take them to Checkout. If you’re using Custom Domains, the URL will use your subdomain. Otherwise, it’ll use checkout.stripe.com. This value is only present when the session is active.



### More attributesExpand all

- objectstring
- after_expirationnullableobject
- allow_promotion_codesnullableboolean
- amount_subtotalnullableinteger
- amount_totalnullableinteger
- automatic_taxobject
- billing_address_collectionnullableenum
- cancel_urlnullablestring
- client_secretnullablestring
- consentnullableobject
- consent_collectionnullableobject
- createdtimestamp
- currency_conversionnullableobject
- custom_fieldsarray of objects
- custom_textobject
- customer_creationnullableenum
- customer_detailsnullableobject
- expires_attimestamp
- invoicenullablestringExpandable
- invoice_creationnullableobject
- livemodeboolean
- localenullableenum
- payment_linknullablestringExpandable
- payment_method_collectionnullableenum
- payment_method_configuration_detailsnullableobject
- payment_method_optionsnullableobject
- payment_method_typesarray of strings
- phone_number_collectionnullableobject
- recovered_fromnullablestring
- redirect_on_completionnullableenum
- saved_payment_method_optionsnullableobject
- setup_intentnullablestringExpandable
- shipping_address_collectionnullableobject
- shipping_costnullableobject
- shipping_detailsnullableobject
- shipping_optionsarray of objects
- submit_typenullableenum
- subscriptionnullablestringExpandable
- tax_id_collectionnullableobject
- total_detailsnullableobject
- ui_modenullableenum

The Session object`{  "id": "cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u",  "object": "checkout.session",  "after_expiration": null,  "allow_promotion_codes": null,  "amount_subtotal": 2198,  "amount_total": 2198,  "automatic_tax": {    "enabled": false,    "liability": null,    "status": null  },  "billing_address_collection": null,  "cancel_url": null,  "client_reference_id": null,  "consent": null,  "consent_collection": null,  "created": 1679600215,  "currency": "usd",  "custom_fields": [],  "custom_text": {    "shipping_address": null,    "submit": null  },  "customer": null,  "customer_creation": "if_required",  "customer_details": null,  "customer_email": null,  "expires_at": 1679686615,  "invoice": null,  "invoice_creation": {    "enabled": false,    "invoice_data": {      "account_tax_ids": null,      "custom_fields": null,      "description": null,      "footer": null,      "issuer": null,      "metadata": {},      "rendering_options": null    }  },  "livemode": false,  "locale": null,  "metadata": {},  "mode": "payment",  "payment_intent": null,  "payment_link": null,  "payment_method_collection": "always",  "payment_method_options": {},  "payment_method_types": [    "card"  ],  "payment_status": "unpaid",  "phone_number_collection": {    "enabled": false  },  "recovered_from": null,  "setup_intent": null,  "shipping_address_collection": null,  "shipping_cost": null,  "shipping_details": null,  "shipping_options": [],  "status": "open",  "submit_type": null,  "subscription": null,  "success_url": "https://example.com/success",  "total_details": {    "amount_discount": 0,    "amount_shipping": 0,    "amount_tax": 0  },  "url": "https://checkout.stripe.com/c/pay/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u#fidkdWxOYHwnPyd1blpxYHZxWjA0SDdPUW5JbmFMck1wMmx9N2BLZjFEfGRUNWhqTmJ%2FM2F8bUA2SDRySkFdUV81T1BSV0YxcWJcTUJcYW5rSzN3dzBLPUE0TzRKTTxzNFBjPWZEX1NKSkxpNTVjRjN8VHE0YicpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPyd2bGtiaWBabHFgaCcpJ2BrZGdpYFVpZGZgbWppYWB3dic%2FcXdwYHgl"}`# Create a Session

Creates a Session object.

### Parameters

- client_reference_idstringA unique string to reference the Checkout Session. This can be a customer ID, a cart ID, or similar, and can be used to reconcile the session with your internal systems.


- customerstringID of an existing Customer, if one exists. In payment mode, the customer’s most recently saved card payment method will be used to prefill the email, name, card details, and billing address on the Checkout page. In subscription mode, the customer’s default payment method will be used if it’s a card, otherwise the most recently saved card will be used. A valid billing address, billing name and billing email are required on the payment method for Checkout to prefill the customer’s card details.

If the Customer already has a valid email set, the email will be prefilled and not editable in Checkout. If the Customer does not have a valid email, Checkout will set the email entered during the session on the Customer.

If blank for Checkout Sessions in subscription mode or with customer_creation set as always in payment mode, Checkout will create a new Customer object based on information provided during the payment flow.

You can set payment_intent_data.setup_future_usage to have Checkout automatically attach the payment method to the Customer you pass in for future reuse.


- customer_emailstringIf provided, this value will be used when the Customer object is created. If not provided, customers will be asked to enter their email address. Use this parameter to prefill customer data if you already have an email on file. To access information about the customer once a session is complete, use the customer field.


- line_itemsarray of objectsRequired unless setup modeA list of items the customer is purchasing. Use this parameter to pass one-time or recurring Prices.

For payment mode, there is a maximum of 100 line items, however it is recommended to consolidate line items if there are more than a few dozen.

For subscription mode, there is a maximum of 20 line items with recurring Prices and 20 line items with one-time Prices. Line items with one-time Prices will be on the initial invoice only.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- modeenumRequiredThe mode of the Checkout Session. Pass subscription if the Checkout Session includes at least one recurring item.

Possible enum values`payment`Accept one-time payments for cards, iDEAL, and more.

`setup`Save payment details to charge your customers later.

`subscription`Use Stripe Billing to set up fixed-price subscriptions.


- return_urlstringRequired conditionallyThe URL to redirect your customer back to after they authenticate or cancel their payment on the payment method’s app or site. This parameter is required if ui_mode is embedded and redirect-based payment methods are enabled on the session.


- success_urlstringRequired conditionallyThe URL to which Stripe should send customers when payment or setup is complete. This parameter is not allowed if ui_mode is embedded. If you’d like to use information from the successful Checkout Session on your page, read the guide on customizing your success page.



### More parametersExpand all

- after_expirationobject
- allow_promotion_codesboolean
- automatic_taxobject
- billing_address_collectionenum
- cancel_urlstring
- consent_collectionobject
- currencyenumRequired conditionally
- custom_fieldsarray of objects
- custom_textobject
- customer_creationenum
- customer_updateobject
- discountsarray of objects
- expires_attimestamp
- invoice_creationobject
- localeenum
- payment_intent_dataobject
- payment_method_collectionenum
- payment_method_configurationstring
- payment_method_dataobject
- payment_method_optionsobject
- payment_method_typesarray of enums
- phone_number_collectionobject
- redirect_on_completionenum
- saved_payment_method_optionsobject
- setup_intent_dataobject
- shipping_address_collectionobject
- shipping_optionsarray of objects
- submit_typeenum
- subscription_dataobject
- tax_id_collectionobject
- ui_modeenum

### Returns

Returns a Session object.

POST/v1/checkout/sessionsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/checkout/sessions \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  --data-urlencode success_url="https://example.com/success" \  -d "line_items[0][price]"=price_1MotwRLkdIwHu7ixYcPLm5uZ \  -d "line_items[0][quantity]"=2 \  -d mode=payment`Response`{  "id": "cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u",  "object": "checkout.session",  "after_expiration": null,  "allow_promotion_codes": null,  "amount_subtotal": 2198,  "amount_total": 2198,  "automatic_tax": {    "enabled": false,    "liability": null,    "status": null  },  "billing_address_collection": null,  "cancel_url": null,  "client_reference_id": null,  "consent": null,  "consent_collection": null,  "created": 1679600215,  "currency": "usd",  "custom_fields": [],  "custom_text": {    "shipping_address": null,    "submit": null  },  "customer": null,  "customer_creation": "if_required",  "customer_details": null,  "customer_email": null,  "expires_at": 1679686615,  "invoice": null,  "invoice_creation": {    "enabled": false,    "invoice_data": {      "account_tax_ids": null,      "custom_fields": null,      "description": null,      "footer": null,      "issuer": null,      "metadata": {},      "rendering_options": null    }  },  "livemode": false,  "locale": null,  "metadata": {},  "mode": "payment",  "payment_intent": null,  "payment_link": null,  "payment_method_collection": "always",  "payment_method_options": {},  "payment_method_types": [    "card"  ],  "payment_status": "unpaid",  "phone_number_collection": {    "enabled": false  },  "recovered_from": null,  "setup_intent": null,  "shipping_address_collection": null,  "shipping_cost": null,  "shipping_details": null,  "shipping_options": [],  "status": "open",  "submit_type": null,  "subscription": null,  "success_url": "https://example.com/success",  "total_details": {    "amount_discount": 0,    "amount_shipping": 0,    "amount_tax": 0  },  "url": "https://checkout.stripe.com/c/pay/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u#fidkdWxOYHwnPyd1blpxYHZxWjA0SDdPUW5JbmFMck1wMmx9N2BLZjFEfGRUNWhqTmJ%2FM2F8bUA2SDRySkFdUV81T1BSV0YxcWJcTUJcYW5rSzN3dzBLPUE0TzRKTTxzNFBjPWZEX1NKSkxpNTVjRjN8VHE0YicpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPyd2bGtiaWBabHFgaCcpJ2BrZGdpYFVpZGZgbWppYWB3dic%2FcXdwYHgl"}`# Retrieve a Session

Retrieves a Session object.

### Parameters

No parameters.

### Returns

Returns a Session object.

GET/v1/checkout/sessions/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/checkout/sessions/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u",  "object": "checkout.session",  "after_expiration": null,  "allow_promotion_codes": null,  "amount_subtotal": 2198,  "amount_total": 2198,  "automatic_tax": {    "enabled": false,    "liability": null,    "status": null  },  "billing_address_collection": null,  "cancel_url": null,  "client_reference_id": null,  "consent": null,  "consent_collection": null,  "created": 1679600215,  "currency": "usd",  "custom_fields": [],  "custom_text": {    "shipping_address": null,    "submit": null  },  "customer": null,  "customer_creation": "if_required",  "customer_details": null,  "customer_email": null,  "expires_at": 1679686615,  "invoice": null,  "invoice_creation": {    "enabled": false,    "invoice_data": {      "account_tax_ids": null,      "custom_fields": null,      "description": null,      "footer": null,      "issuer": null,      "metadata": {},      "rendering_options": null    }  },  "livemode": false,  "locale": null,  "metadata": {},  "mode": "payment",  "payment_intent": null,  "payment_link": null,  "payment_method_collection": "always",  "payment_method_options": {},  "payment_method_types": [    "card"  ],  "payment_status": "unpaid",  "phone_number_collection": {    "enabled": false  },  "recovered_from": null,  "setup_intent": null,  "shipping_address_collection": null,  "shipping_cost": null,  "shipping_details": null,  "shipping_options": [],  "status": "open",  "submit_type": null,  "subscription": null,  "success_url": "https://example.com/success",  "total_details": {    "amount_discount": 0,    "amount_shipping": 0,    "amount_tax": 0  },  "url": "https://checkout.stripe.com/c/pay/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u#fidkdWxOYHwnPyd1blpxYHZxWjA0SDdPUW5JbmFMck1wMmx9N2BLZjFEfGRUNWhqTmJ%2FM2F8bUA2SDRySkFdUV81T1BSV0YxcWJcTUJcYW5rSzN3dzBLPUE0TzRKTTxzNFBjPWZEX1NKSkxpNTVjRjN8VHE0YicpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPyd2bGtiaWBabHFgaCcpJ2BrZGdpYFVpZGZgbWppYWB3dic%2FcXdwYHgl"}`# Retrieve a Checkout Session's line items

When retrieving a Checkout Session, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

### Parameters

No parameters.

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit Checkout Session line items, starting after Line Item starting_after. Each entry in the array is a separate Line Item object. If no more line items are available, the resulting array will be empty.

GET/v1/checkout/sessions/:id/line_itemsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/checkout/sessions/cs_test_a1enSAC01IA3Ps2vL32mNoWKMCNmmfUGTeEeHXI5tLCvyFNGsdG2UNA7mr/line_items \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "object": "list",  "data": [    {      "id": "li_1N4BEoLkdIwHu7ixWtXug1yk",      "object": "item",      "amount_discount": 0,      "amount_subtotal": 2198,      "amount_tax": 0,      "amount_total": 2198,      "currency": "usd",      "description": "T-shirt",      "price": {        "id": "price_1N4AEsLkdIwHu7ix7Ssho8Cl",        "object": "price",        "active": true,        "billing_scheme": "per_unit",        "created": 1683237782,        "currency": "usd",        "custom_unit_amount": null,        "livemode": false,        "lookup_key": null,        "metadata": {},        "nickname": null,        "product": "prod_NppuJWzzNnD5Ut",        "recurring": null,        "tax_behavior": "unspecified",        "tiers_mode": null,        "transform_quantity": null,        "type": "one_time",        "unit_amount": 1099,        "unit_amount_decimal": "1099"      },      "quantity": 2    }  ],  "has_more": false,  "url": "/v1/checkout/sessions/cs_test_a1enSAC01IA3Ps2vL32mNoWKMCNmmfUGTeEeHXI5tLCvyFNGsdG2UNA7mr/line_items"}`# List all Checkout Sessions

Returns a list of Checkout Sessions.

### Parameters

- payment_intentstringOnly return the Checkout Session for the PaymentIntent specified.


- subscriptionstringOnly return the Checkout Session for the subscription specified.



### More parametersExpand all

- createdobject
- customerstring
- customer_detailsobject
- ending_beforestring
- limitinteger
- payment_linkstring
- starting_afterstring
- statusenum

### Returns

A dictionary with a data property that contains an array of up to limit Checkout Sessions, starting after Checkout Session starting_after. Each entry in the array is a separate Checkout Session object. If no more Checkout Sessions are available, the resulting array will be empty.

GET/v1/checkout/sessionsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/checkout/sessions \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/checkout/sessions",  "has_more": false,  "data": [    {      "id": "cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u",      "object": "checkout.session",      "after_expiration": null,      "allow_promotion_codes": null,      "amount_subtotal": 2198,      "amount_total": 2198,      "automatic_tax": {        "enabled": false,        "liability": null,        "status": null      },      "billing_address_collection": null,      "cancel_url": null,      "client_reference_id": null,      "consent": null,      "consent_collection": null,      "created": 1679600215,      "currency": "usd",      "custom_fields": [],      "custom_text": {        "shipping_address": null,        "submit": null      },      "customer": null,      "customer_creation": "if_required",      "customer_details": null,      "customer_email": null,      "expires_at": 1679686615,      "invoice": null,      "invoice_creation": {        "enabled": false,        "invoice_data": {          "account_tax_ids": null,          "custom_fields": null,          "description": null,          "footer": null,          "issuer": null,          "metadata": {},          "rendering_options": null        }      },      "livemode": false,      "locale": null,      "metadata": {},      "mode": "payment",      "payment_intent": null,      "payment_link": null,      "payment_method_collection": "always",      "payment_method_options": {},      "payment_method_types": [        "card"      ],      "payment_status": "unpaid",      "phone_number_collection": {        "enabled": false      },      "recovered_from": null,      "setup_intent": null,      "shipping_address_collection": null,      "shipping_cost": null,      "shipping_details": null,      "shipping_options": [],      "status": "open",      "submit_type": null,      "subscription": null,      "success_url": "https://example.com/success",      "total_details": {        "amount_discount": 0,        "amount_shipping": 0,        "amount_tax": 0      },      "url": "https://checkout.stripe.com/c/pay/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u#fidkdWxOYHwnPyd1blpxYHZxWjA0SDdPUW5JbmFMck1wMmx9N2BLZjFEfGRUNWhqTmJ%2FM2F8bUA2SDRySkFdUV81T1BSV0YxcWJcTUJcYW5rSzN3dzBLPUE0TzRKTTxzNFBjPWZEX1NKSkxpNTVjRjN8VHE0YicpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPyd2bGtiaWBabHFgaCcpJ2BrZGdpYFVpZGZgbWppYWB3dic%2FcXdwYHgl"    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`