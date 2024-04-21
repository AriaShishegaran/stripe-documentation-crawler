htmlCreate a Session | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Create a Session

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

GET/v1/checkout/sessionsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/checkout/sessions \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/checkout/sessions",  "has_more": false,  "data": [    {      "id": "cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u",      "object": "checkout.session",      "after_expiration": null,      "allow_promotion_codes": null,      "amount_subtotal": 2198,      "amount_total": 2198,      "automatic_tax": {        "enabled": false,        "liability": null,        "status": null      },      "billing_address_collection": null,      "cancel_url": null,      "client_reference_id": null,      "consent": null,      "consent_collection": null,      "created": 1679600215,      "currency": "usd",      "custom_fields": [],      "custom_text": {        "shipping_address": null,        "submit": null      },      "customer": null,      "customer_creation": "if_required",      "customer_details": null,      "customer_email": null,      "expires_at": 1679686615,      "invoice": null,      "invoice_creation": {        "enabled": false,        "invoice_data": {          "account_tax_ids": null,          "custom_fields": null,          "description": null,          "footer": null,          "issuer": null,          "metadata": {},          "rendering_options": null        }      },      "livemode": false,      "locale": null,      "metadata": {},      "mode": "payment",      "payment_intent": null,      "payment_link": null,      "payment_method_collection": "always",      "payment_method_options": {},      "payment_method_types": [        "card"      ],      "payment_status": "unpaid",      "phone_number_collection": {        "enabled": false      },      "recovered_from": null,      "setup_intent": null,      "shipping_address_collection": null,      "shipping_cost": null,      "shipping_details": null,      "shipping_options": [],      "status": "open",      "submit_type": null,      "subscription": null,      "success_url": "https://example.com/success",      "total_details": {        "amount_discount": 0,        "amount_shipping": 0,        "amount_tax": 0      },      "url": "https://checkout.stripe.com/c/pay/cs_test_a11YYufWQzNY63zpQ6QSNRQhkUpVph4WRmzW0zWJO2znZKdVujZ0N0S22u#fidkdWxOYHwnPyd1blpxYHZxWjA0SDdPUW5JbmFMck1wMmx9N2BLZjFEfGRUNWhqTmJ%2FM2F8bUA2SDRySkFdUV81T1BSV0YxcWJcTUJcYW5rSzN3dzBLPUE0TzRKTTxzNFBjPWZEX1NKSkxpNTVjRjN8VHE0YicpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPyd2bGtiaWBabHFgaCcpJ2BrZGdpYFVpZGZgbWppYWB3dic%2FcXdwYHgl"    }    {...}    {...}  ],}`# Expire a Session

A Session can be expired when it is in one of these statuses: open

After it expires, a customer can’t complete a Session and customers loading the Session see a message saying the Session is expired.

### Parameters

No parameters.

### Returns

Returns a Session object if the expiration succeeded. Returns an error if the Session has already expired or isn’t in an expireable state.

POST/v1/checkout/sessions/:id/expireServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/checkout/sessions/cs_test_a1Ae6ClgOkjygKwrf9B3L6ITtUuZW4Xx9FivL6DZYoYFdfAefQxsYpJJd3/expire \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "cs_test_a1Ae6ClgOkjygKwrf9B3L6ITtUuZW4Xx9FivL6DZYoYFdfAefQxsYpJJd3",  "object": "checkout.session",  "after_expiration": null,  "allow_promotion_codes": null,  "amount_subtotal": 2198,  "amount_total": 2198,  "automatic_tax": {    "enabled": false,    "status": null  },  "billing_address_collection": null,  "cancel_url": null,  "client_reference_id": null,  "consent": null,  "consent_collection": null,  "created": 1679434412,  "currency": "usd",  "custom_fields": [],  "custom_text": {    "shipping_address": null,    "submit": null  },  "customer": null,  "customer_creation": "if_required",  "customer_details": null,  "customer_email": null,  "expires_at": 1679520812,  "invoice": null,  "invoice_creation": {    "enabled": false,    "invoice_data": {      "account_tax_ids": null,      "custom_fields": null,      "description": null,      "footer": null,      "metadata": {},      "rendering_options": null    }  },  "livemode": false,  "locale": null,  "metadata": {},  "mode": "payment",  "payment_intent": null,  "payment_link": null,  "payment_method_collection": "always",  "payment_method_options": {},  "payment_method_types": [    "card"  ],  "payment_status": "unpaid",  "phone_number_collection": {    "enabled": false  },  "recovered_from": null,  "setup_intent": null,  "shipping_address_collection": null,  "shipping_cost": null,  "shipping_details": null,  "shipping_options": [],  "status": "expired",  "submit_type": null,  "subscription": null,  "success_url": "https://example.com/success",  "total_details": {    "amount_discount": 0,    "amount_shipping": 0,    "amount_tax": 0  },  "url": null}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`