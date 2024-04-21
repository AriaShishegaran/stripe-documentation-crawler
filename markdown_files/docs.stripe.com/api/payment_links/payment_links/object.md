htmlThe Payment Link object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The Payment Link object

### Attributes

- idstringUnique identifier for the object.


- activebooleanWhether the payment link’s url is active. If false, customers visiting the URL will be shown a page saying that the link has been deactivated.


- line_itemsobjectExpandableThe line items representing what is being sold.

Show child attributes
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- urlstringThe public URL that can be shared with customers.



### More attributesExpand all

- objectstring
- after_completionobject
- allow_promotion_codesboolean
- applicationnullablestringExpandableConnect only
- application_fee_amountnullableintegerConnect only
- application_fee_percentnullablefloatConnect only
- automatic_taxobject
- billing_address_collectionenum
- consent_collectionnullableobject
- currencyenum
- custom_fieldsarray of objects
- custom_textobject
- customer_creationenum
- inactive_messagenullablestring
- invoice_creationnullableobject
- livemodeboolean
- on_behalf_ofnullablestringExpandableConnect only
- payment_intent_datanullableobject
- payment_method_collectionenum
- payment_method_typesnullablearray of enums
- phone_number_collectionobject
- restrictionsnullableobject
- shipping_address_collectionnullableobject
- shipping_optionsarray of objects
- submit_typeenum
- subscription_datanullableobject
- tax_id_collectionobject
- transfer_datanullableobjectConnect only

The Payment Link object`{  "id": "plink_1MoC3ULkdIwHu7ixZjtGpVl2",  "object": "payment_link",  "active": true,  "after_completion": {    "hosted_confirmation": {      "custom_message": null    },    "type": "hosted_confirmation"  },  "allow_promotion_codes": false,  "application_fee_amount": null,  "application_fee_percent": null,  "automatic_tax": {    "enabled": false,    "liability": null  },  "billing_address_collection": "auto",  "consent_collection": null,  "currency": "usd",  "custom_fields": [],  "custom_text": {    "shipping_address": null,    "submit": null  },  "customer_creation": "if_required",  "invoice_creation": {    "enabled": false,    "invoice_data": {      "account_tax_ids": null,      "custom_fields": null,      "description": null,      "footer": null,      "issuer": null,      "metadata": {},      "rendering_options": null    }  },  "livemode": false,  "metadata": {},  "on_behalf_of": null,  "payment_intent_data": null,  "payment_method_collection": "always",  "payment_method_types": null,  "phone_number_collection": {    "enabled": false  },  "shipping_address_collection": null,  "shipping_options": [],  "submit_type": "auto",  "subscription_data": {    "description": null,    "invoice_settings": {      "issuer": {        "type": "self"      }    },    "trial_period_days": null  },  "tax_id_collection": {    "enabled": false  },  "transfer_data": null,  "url": "https://buy.stripe.com/test_cN25nr0iZ7bUa7meUY"}`# Create a payment link

Creates a payment link.

### Parameters

- line_itemsarray of objectsRequiredThe line items representing what is being sold. Each line item represents an item being sold. Up to 20 line items are supported.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata. Metadata associated with this Payment Link will automatically be copied to checkout sessions created by this payment link.



### More parametersExpand all

- after_completionobject
- allow_promotion_codesboolean
- application_fee_amountintegerConnect only
- application_fee_percentfloatConnect only
- automatic_taxobject
- billing_address_collectionenum
- consent_collectionobject
- currencyenum
- custom_fieldsarray of objects
- custom_textobject
- customer_creationenum
- inactive_messagestring
- invoice_creationobject
- on_behalf_ofstringConnect only
- payment_intent_dataobject
- payment_method_collectionenum
- payment_method_typesarray of enums
- phone_number_collectionobject
- restrictionsobject
- shipping_address_collectionobject
- shipping_optionsarray of objects
- submit_typeenum
- subscription_dataobject
- tax_id_collectionobject
- transfer_dataobjectConnect only

### Returns

Returns the payment link.

POST/v1/payment_linksServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_links \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "line_items[0][price]"=price_1MoC3TLkdIwHu7ixcIbKelAC \  -d "line_items[0][quantity]"=1`Response`{  "id": "plink_1MoC3ULkdIwHu7ixZjtGpVl2",  "object": "payment_link",  "active": true,  "after_completion": {    "hosted_confirmation": {      "custom_message": null    },    "type": "hosted_confirmation"  },  "allow_promotion_codes": false,  "application_fee_amount": null,  "application_fee_percent": null,  "automatic_tax": {    "enabled": false,    "liability": null  },  "billing_address_collection": "auto",  "consent_collection": null,  "currency": "usd",  "custom_fields": [],  "custom_text": {    "shipping_address": null,    "submit": null  },  "customer_creation": "if_required",  "invoice_creation": {    "enabled": false,    "invoice_data": {      "account_tax_ids": null,      "custom_fields": null,      "description": null,      "footer": null,      "issuer": null,      "metadata": {},      "rendering_options": null    }  },  "livemode": false,  "metadata": {},  "on_behalf_of": null,  "payment_intent_data": null,  "payment_method_collection": "always",  "payment_method_types": null,  "phone_number_collection": {    "enabled": false  },  "shipping_address_collection": null,  "shipping_options": [],  "submit_type": "auto",  "subscription_data": {    "description": null,    "invoice_settings": {      "issuer": {        "type": "self"      }    },    "trial_period_days": null  },  "tax_id_collection": {    "enabled": false  },  "transfer_data": null,  "url": "https://buy.stripe.com/test_cN25nr0iZ7bUa7meUY"}`# Update a payment link

Updates a payment link.

### Parameters

- activebooleanWhether the payment link’s url is active. If false, customers visiting the URL will be shown a page saying that the link has been deactivated.


- line_itemsarray of objectsThe line items representing what is being sold. Each line item represents an item being sold. Up to 20 line items are supported.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata. Metadata associated with this Payment Link will automatically be copied to checkout sessions created by this payment link.



### More parametersExpand all

- after_completionobject
- allow_promotion_codesboolean
- automatic_taxobject
- billing_address_collectionenum
- custom_fieldsarray of objects
- custom_textobject
- customer_creationenum
- inactive_messagestring
- invoice_creationobject
- payment_intent_dataobject
- payment_method_collectionenum
- payment_method_typesarray of enums
- restrictionsobject
- shipping_address_collectionobject
- subscription_dataobject

### Returns

Updated payment link.

POST/v1/payment_links/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_links/plink_1MoC3ULkdIwHu7ixZjtGpVl2 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "plink_1MoC3ULkdIwHu7ixZjtGpVl2",  "object": "payment_link",  "active": true,  "after_completion": {    "hosted_confirmation": {      "custom_message": null    },    "type": "hosted_confirmation"  },  "allow_promotion_codes": false,  "application_fee_amount": null,  "application_fee_percent": null,  "automatic_tax": {    "enabled": false,    "liability": null  },  "billing_address_collection": "auto",  "consent_collection": null,  "currency": "usd",  "custom_fields": [],  "custom_text": {    "shipping_address": null,    "submit": null  },  "customer_creation": "if_required",  "invoice_creation": {    "enabled": false,    "invoice_data": {      "account_tax_ids": null,      "custom_fields": null,      "description": null,      "footer": null,      "issuer": null,      "metadata": {},      "rendering_options": null    }  },  "livemode": false,  "metadata": {    "order_id": "6735"  },  "on_behalf_of": null,  "payment_intent_data": null,  "payment_method_collection": "always",  "payment_method_types": null,  "phone_number_collection": {    "enabled": false  },  "shipping_address_collection": null,  "shipping_options": [],  "submit_type": "auto",  "subscription_data": {    "description": null,    "invoice_settings": {      "issuer": {        "type": "self"      }    },    "trial_period_days": null  },  "tax_id_collection": {    "enabled": false  },  "transfer_data": null,  "url": "https://buy.stripe.com/test_cN25nr0iZ7bUa7meUY"}`# Retrieve a payment link's line items

When retrieving a payment link, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

### Parameters

No parameters.

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit payment link line items, starting after Line Item starting_after. Each entry in the array is a separate Line Item object. If no more line items are available, the resulting array will be empty.

GET/v1/payment_links/:id/line_itemsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_links/plink_1N4CWjLkdIwHu7ix2Y2F1kqb/line_items \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "object": "list",  "data": [    {      "id": "li_NpsHNiHSaDeU0X",      "object": "item",      "amount_discount": 0,      "amount_subtotal": 1099,      "amount_tax": 0,      "amount_total": 1099,      "currency": "usd",      "description": "T-shirt",      "price": {        "id": "price_1N4AEsLkdIwHu7ix7Ssho8Cl",        "object": "price",        "active": true,        "billing_scheme": "per_unit",        "created": 1683237782,        "currency": "usd",        "custom_unit_amount": null,        "livemode": false,        "lookup_key": null,        "metadata": {},        "nickname": null,        "product": "prod_NppuJWzzNnD5Ut",        "recurring": null,        "tax_behavior": "unspecified",        "tiers_mode": null,        "transform_quantity": null,        "type": "one_time",        "unit_amount": 1099,        "unit_amount_decimal": "1099"      },      "quantity": 1    }  ],  "has_more": false,  "url": "/v1/payment_links/plink_1N4CWjLkdIwHu7ix2Y2F1kqb/line_items"}`# Retrieve payment link

Retrieve a payment link.

### Parameters

No parameters.

### Returns

Returns the payment link.

GET/v1/payment_links/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_links/plink_1MoC3ULkdIwHu7ixZjtGpVl2 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "plink_1MoC3ULkdIwHu7ixZjtGpVl2",  "object": "payment_link",  "active": true,  "after_completion": {    "hosted_confirmation": {      "custom_message": null    },    "type": "hosted_confirmation"  },  "allow_promotion_codes": false,  "application_fee_amount": null,  "application_fee_percent": null,  "automatic_tax": {    "enabled": false,    "liability": null  },  "billing_address_collection": "auto",  "consent_collection": null,  "currency": "usd",  "custom_fields": [],  "custom_text": {    "shipping_address": null,    "submit": null  },  "customer_creation": "if_required",  "invoice_creation": {    "enabled": false,    "invoice_data": {      "account_tax_ids": null,      "custom_fields": null,      "description": null,      "footer": null,      "issuer": null,      "metadata": {},      "rendering_options": null    }  },  "livemode": false,  "metadata": {},  "on_behalf_of": null,  "payment_intent_data": null,  "payment_method_collection": "always",  "payment_method_types": null,  "phone_number_collection": {    "enabled": false  },  "shipping_address_collection": null,  "shipping_options": [],  "submit_type": "auto",  "subscription_data": {    "description": null,    "invoice_settings": {      "issuer": {        "type": "self"      }    },    "trial_period_days": null  },  "tax_id_collection": {    "enabled": false  },  "transfer_data": null,  "url": "https://buy.stripe.com/test_cN25nr0iZ7bUa7meUY"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`