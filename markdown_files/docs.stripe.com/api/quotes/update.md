htmlUpdate a quote | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Update a quote

A quote models prices and services for a customer.

### Parameters

- line_itemsarray of objectsA list of line items the customer is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- application_fee_amountintegerConnect only
- application_fee_percentfloatConnect only
- automatic_taxobject
- collection_methodenum
- customerstring
- default_tax_ratesarray of strings
- descriptionstring
- discountsarray of objects
- expires_attimestamp
- footerstring
- headerstring
- invoice_settingsobject
- on_behalf_ofstringConnect only
- subscription_dataobject
- transfer_dataobjectConnect only

### Returns

Returns the updated quote object.

POST/v1/quotes/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/quotes/qt_1Mr7wVLkdIwHu7ixJYSiPTGq \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "qt_1Mr7wVLkdIwHu7ixJYSiPTGq",  "object": "quote",  "amount_subtotal": 2198,  "amount_total": 2198,  "application": null,  "application_fee_amount": null,  "application_fee_percent": null,  "automatic_tax": {    "enabled": false,    "liability": null,    "status": null  },  "collection_method": "charge_automatically",  "computed": {    "recurring": null,    "upfront": {      "amount_subtotal": 2198,      "amount_total": 2198,      "total_details": {        "amount_discount": 0,        "amount_shipping": 0,        "amount_tax": 0      }    }  },  "created": 1680130691,  "currency": "usd",  "customer": "cus_NcMfB0SSFHINCV",  "default_tax_rates": [],  "description": null,  "discounts": [],  "expires_at": 1682722691,  "footer": null,  "from_quote": null,  "header": null,  "invoice": null,  "invoice_settings": {    "days_until_due": null,    "issuer": {      "type": "self"    }  },  "livemode": false,  "metadata": {    "order_id": "6735"  },  "number": null,  "on_behalf_of": null,  "status": "draft",  "status_transitions": {    "accepted_at": null,    "canceled_at": null,    "finalized_at": null  },  "subscription": null,  "subscription_data": {    "description": null,    "effective_date": null,    "trial_period_days": null  },  "subscription_schedule": null,  "test_clock": null,  "total_details": {    "amount_discount": 0,    "amount_shipping": 0,    "amount_tax": 0  },  "transfer_data": null}`# Retrieve a quote's line items

When retrieving a quote, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

### Parameters

No parameters.

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit quote line items, starting after Line Item starting_after. Each entry in the array is a separate Line Item object. If no more line items are available, the resulting array will be empty.

GET/v1/quotes/:id/line_itemsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/quotes/qt_1Mr7wVLkdIwHu7ixJYSiPTGq/line_items \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "object": "list",  "url": "/v1/quotes/qt_1Mr7wVLkdIwHu7ixJYSiPTGq/line_items",  "has_more": false,  "data": [    {      "id": "li_1Mr7wVLkdIwHu7ixBJJ8ww4j",      "object": "item",      "amount_discount": 0,      "amount_subtotal": 2198,      "amount_tax": 0,      "amount_total": 2198,      "currency": "usd",      "description": "T-shirt",      "price": {        "id": "price_1Mr7wULkdIwHu7ixhPkIEN2w",        "object": "price",        "active": true,        "billing_scheme": "per_unit",        "created": 1680130690,        "currency": "usd",        "custom_unit_amount": null,        "livemode": false,        "lookup_key": null,        "metadata": {},        "nickname": null,        "product": "prod_NcMfZX1FelgpZm",        "recurring": null,        "tax_behavior": "unspecified",        "tiers_mode": null,        "transform_quantity": null,        "type": "one_time",        "unit_amount": 1099,        "unit_amount_decimal": "1099"      },      "quantity": 2    }    {...}    {...}  ],}`# Retrieve a quote's upfront line items

When retrieving a quote, there is an includable computed.upfront.line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of upfront line items.

### Parameters

No parameters.

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit upfront line items, starting after Line Item starting_after. Each entry in the array is a separate Line Item object. If no more upfront line items are available, the resulting array will be empty.

GET/v1/quotes/:id/computed_upfront_line_itemsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/quotes/qt_1Mr7wVLkdIwHu7ixJYSiPTGq/computed_upfront_line_items \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "object": "list",  "data": [    {      "id": "li_1Mr7wVLkdIwHu7ixMMjVsIUH",      "object": "item",      "amount_discount": 0,      "amount_subtotal": 2198,      "amount_tax": 0,      "amount_total": 2198,      "currency": "usd",      "description": "T-shirt",      "price": {        "id": "price_1Mr7wULkdIwHu7ixhPkIEN2w",        "object": "price",        "active": true,        "billing_scheme": "per_unit",        "created": 1680130690,        "currency": "usd",        "custom_unit_amount": null,        "livemode": false,        "lookup_key": null,        "metadata": {},        "nickname": null,        "product": "prod_NcMfZX1FelgpZm",        "recurring": null,        "tax_behavior": "unspecified",        "tiers_mode": null,        "transform_quantity": null,        "type": "one_time",        "unit_amount": 1099,        "unit_amount_decimal": "1099"      },      "quantity": 2    }  ],  "has_more": false,  "url": "/v1/quotes/qt_1Mr7wVLkdIwHu7ixJYSiPTGq/computed_upfront_line_items"}`# Retrieve a quote

Retrieves the quote with the given ID.

### Parameters

No parameters.

### Returns

Returns a quote if a valid quote ID was provided. Raises an error otherwise.

GET/v1/quotes/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/quotes/qt_1Mr7wVLkdIwHu7ixJYSiPTGq \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "qt_1Mr7wVLkdIwHu7ixJYSiPTGq",  "object": "quote",  "amount_subtotal": 2198,  "amount_total": 2198,  "application": null,  "application_fee_amount": null,  "application_fee_percent": null,  "automatic_tax": {    "enabled": false,    "liability": null,    "status": null  },  "collection_method": "charge_automatically",  "computed": {    "recurring": null,    "upfront": {      "amount_subtotal": 2198,      "amount_total": 2198,      "total_details": {        "amount_discount": 0,        "amount_shipping": 0,        "amount_tax": 0      }    }  },  "created": 1680130691,  "currency": "usd",  "customer": "cus_NcMfB0SSFHINCV",  "default_tax_rates": [],  "description": null,  "discounts": [],  "expires_at": 1682722691,  "footer": null,  "from_quote": null,  "header": null,  "invoice": null,  "invoice_settings": {    "days_until_due": null,    "issuer": {      "type": "self"    }  },  "livemode": false,  "metadata": {},  "number": null,  "on_behalf_of": null,  "status": "draft",  "status_transitions": {    "accepted_at": null,    "canceled_at": null,    "finalized_at": null  },  "subscription": null,  "subscription_data": {    "description": null,    "effective_date": null,    "trial_period_days": null  },  "subscription_schedule": null,  "test_clock": null,  "total_details": {    "amount_discount": 0,    "amount_shipping": 0,    "amount_tax": 0  },  "transfer_data": null}`# List all quotes

Returns a list of your quotes.

### Parameters

- customerstringThe ID of the customer whose quotes will be retrieved.


- statusenumThe status of the quote.



### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring
- test_clockstring

### Returns

A dictionary with a data property that contains an array of up to limit quotes, starting after quote starting_after. Each entry in the array is a separate quote object. If no more quotes are available, the resulting array will be empty.

GET/v1/quotesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/quotes \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/quotes",  "has_more": false,  "data": [    {      "id": "qt_1Mr7SqLkdIwHu7ixpI1ClZ6z",      "object": "quote",      "amount_subtotal": 2198,      "amount_total": 2198,      "application": null,      "application_fee_amount": null,      "application_fee_percent": null,      "automatic_tax": {        "enabled": false,        "liability": null,        "status": null      },      "collection_method": "charge_automatically",      "computed": {        "recurring": null,        "upfront": {          "amount_subtotal": 2198,          "amount_total": 2198,          "total_details": {            "amount_discount": 0,            "amount_shipping": 0,            "amount_tax": 0          }        }      },      "created": 1680128852,      "currency": "usd",      "customer": "cus_NcMBZUWCIOEgEW",      "default_tax_rates": [],      "description": null,      "discounts": [],      "expires_at": 1682720852,      "footer": null,      "from_quote": null,      "header": null,      "invoice": null,      "invoice_settings": {        "days_until_due": null,        "issuer": {          "type": "self"        }      },      "livemode": false,      "metadata": {},      "number": "QT-5B9DA057-0001-1",      "on_behalf_of": null,      "status": "open",      "status_transitions": {        "accepted_at": null,        "canceled_at": null,        "finalized_at": 1680128853      },      "subscription": null,      "subscription_data": {        "description": null,        "effective_date": null,        "trial_period_days": null      },      "subscription_schedule": null,      "test_clock": null,      "total_details": {        "amount_discount": 0,        "amount_shipping": 0,        "amount_tax": 0      },      "transfer_data": null    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`