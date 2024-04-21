htmlUpdate a charge | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Update a charge

Updates the specified charge by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

### Parameters

- customerstringThe ID of an existing customer that will be associated with this request. This field may only be updated if there is no existing associated customer with this charge.


- descriptionstringAn arbitrary string which you can attach to a charge object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the description of the charge(s) that they are describing.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- receipt_emailstringThis is the email address that the receipt for this charge will be sent to. If this field is updated, then a new email receipt will be sent to the updated address.


- shippingobjectShipping information for the charge. Helps prevent fraud on charges for physical goods.

Show child parameters

### More parametersExpand all

- fraud_detailsobject
- transfer_groupstringConnect only

### Returns

Returns the charge object if the update succeeded. This call will raise an error if update parameters are invalid.

POST/v1/charges/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/charges/ch_3MmlLrLkdIwHu7ix0snN0B15 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[shipping]"=express`Response`{  "id": "ch_3MmlLrLkdIwHu7ix0snN0B15",  "object": "charge",  "amount": 1099,  "amount_captured": 1099,  "amount_refunded": 0,  "application": null,  "application_fee": null,  "application_fee_amount": null,  "balance_transaction": "txn_3MmlLrLkdIwHu7ix0uke3Ezy",  "billing_details": {    "address": {      "city": null,      "country": null,      "line1": null,      "line2": null,      "postal_code": null,      "state": null    },    "email": null,    "name": null,    "phone": null  },  "calculated_statement_descriptor": "Stripe",  "captured": true,  "created": 1679090539,  "currency": "usd",  "customer": null,  "description": null,  "disputed": false,  "failure_balance_transaction": null,  "failure_code": null,  "failure_message": null,  "fraud_details": {},  "invoice": null,  "livemode": false,  "metadata": {    "shipping": "express"  },  "on_behalf_of": null,  "outcome": {    "network_status": "approved_by_network",    "reason": null,    "risk_level": "normal",    "risk_score": 32,    "seller_message": "Payment complete.",    "type": "authorized"  },  "paid": true,  "payment_intent": null,  "payment_method": "card_1MmlLrLkdIwHu7ixIJwEWSNR",  "payment_method_details": {    "card": {      "brand": "visa",      "checks": {        "address_line1_check": null,        "address_postal_code_check": null,        "cvc_check": null      },      "country": "US",      "exp_month": 3,      "exp_year": 2024,      "fingerprint": "mToisGZ01V71BCos",      "funding": "credit",      "installments": null,      "last4": "4242",      "mandate": null,      "network": "visa",      "network_token": {        "used": false      },      "three_d_secure": null,      "wallet": null    },    "type": "card"  },  "receipt_email": null,  "receipt_number": null,  "receipt_url": "https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KPDLl6UGMgawkab5iK86LBYtkq0XrhiQf1RsA2ubesH4GHiixEU8_1-Wp7h4oQEdfSUGiZpJwtQHBErT",  "refunded": false,  "refunds": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/charges/ch_3MmlLrLkdIwHu7ix0snN0B15/refunds"  },  "review": null,  "shipping": null,  "source_transfer": null,  "statement_descriptor": null,  "statement_descriptor_suffix": null,  "status": "succeeded",  "transfer_data": null,  "transfer_group": null}`# Retrieve a charge

Retrieves the details of a charge that has previously been created. Supply the unique charge ID that was returned from your previous request, and Stripe will return the corresponding charge information. The same information is returned when creating or refunding the charge.

### Parameters

No parameters.

### Returns

Returns a charge if a valid identifier was provided, and raises an error otherwise.

GET/v1/charges/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/charges/ch_3MmlLrLkdIwHu7ix0snN0B15 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "ch_3MmlLrLkdIwHu7ix0snN0B15",  "object": "charge",  "amount": 1099,  "amount_captured": 1099,  "amount_refunded": 0,  "application": null,  "application_fee": null,  "application_fee_amount": null,  "balance_transaction": "txn_3MmlLrLkdIwHu7ix0uke3Ezy",  "billing_details": {    "address": {      "city": null,      "country": null,      "line1": null,      "line2": null,      "postal_code": null,      "state": null    },    "email": null,    "name": null,    "phone": null  },  "calculated_statement_descriptor": "Stripe",  "captured": true,  "created": 1679090539,  "currency": "usd",  "customer": null,  "description": null,  "disputed": false,  "failure_balance_transaction": null,  "failure_code": null,  "failure_message": null,  "fraud_details": {},  "invoice": null,  "livemode": false,  "metadata": {},  "on_behalf_of": null,  "outcome": {    "network_status": "approved_by_network",    "reason": null,    "risk_level": "normal",    "risk_score": 32,    "seller_message": "Payment complete.",    "type": "authorized"  },  "paid": true,  "payment_intent": null,  "payment_method": "card_1MmlLrLkdIwHu7ixIJwEWSNR",  "payment_method_details": {    "card": {      "brand": "visa",      "checks": {        "address_line1_check": null,        "address_postal_code_check": null,        "cvc_check": null      },      "country": "US",      "exp_month": 3,      "exp_year": 2024,      "fingerprint": "mToisGZ01V71BCos",      "funding": "credit",      "installments": null,      "last4": "4242",      "mandate": null,      "network": "visa",      "three_d_secure": null,      "wallet": null    },    "type": "card"  },  "receipt_email": null,  "receipt_number": null,  "receipt_url": "https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KOvG06AGMgZfBXyr1aw6LBa9vaaSRWU96d8qBwz9z2J_CObiV_H2-e8RezSK_sw0KISesp4czsOUlVKY",  "refunded": false,  "review": null,  "shipping": null,  "source_transfer": null,  "statement_descriptor": null,  "statement_descriptor_suffix": null,  "status": "succeeded",  "transfer_data": null,  "transfer_group": null}`# List all charges

Returns a list of charges you’ve previously created. The charges are returned in sorted order, with the most recent charges appearing first.

### Parameters

- customerstringOnly return charges for the customer specified by this customer ID.



### More parametersExpand all

- createdobject
- ending_beforestring
- limitinteger
- payment_intentstring
- starting_afterstring
- transfer_groupstringConnect only

### Returns

A dictionary with a data property that contains an array of up to limit charges, starting after charge starting_after. Each entry in the array is a separate charge object. If no more charges are available, the resulting array will be empty. If you provide a non-existent customer ID, this call raises an error.

GET/v1/chargesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/charges \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/charges",  "has_more": false,  "data": [    {      "id": "ch_3MmlLrLkdIwHu7ix0snN0B15",      "object": "charge",      "amount": 1099,      "amount_captured": 1099,      "amount_refunded": 0,      "application": null,      "application_fee": null,      "application_fee_amount": null,      "balance_transaction": "txn_3MmlLrLkdIwHu7ix0uke3Ezy",      "billing_details": {        "address": {          "city": null,          "country": null,          "line1": null,          "line2": null,          "postal_code": null,          "state": null        },        "email": null,        "name": null,        "phone": null      },      "calculated_statement_descriptor": "Stripe",      "captured": true,      "created": 1679090539,      "currency": "usd",      "customer": null,      "description": null,      "disputed": false,      "failure_balance_transaction": null,      "failure_code": null,      "failure_message": null,      "fraud_details": {},      "invoice": null,      "livemode": false,      "metadata": {},      "on_behalf_of": null,      "outcome": {        "network_status": "approved_by_network",        "reason": null,        "risk_level": "normal",        "risk_score": 32,        "seller_message": "Payment complete.",        "type": "authorized"      },      "paid": true,      "payment_intent": null,      "payment_method": "card_1MmlLrLkdIwHu7ixIJwEWSNR",      "payment_method_details": {        "card": {          "brand": "visa",          "checks": {            "address_line1_check": null,            "address_postal_code_check": null,            "cvc_check": null          },          "country": "US",          "exp_month": 3,          "exp_year": 2024,          "fingerprint": "mToisGZ01V71BCos",          "funding": "credit",          "installments": null,          "last4": "4242",          "mandate": null,          "network": "visa",          "three_d_secure": null,          "wallet": null        },        "type": "card"      },      "receipt_email": null,      "receipt_number": null,      "receipt_url": "https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KOvG06AGMgZfBXyr1aw6LBa9vaaSRWU96d8qBwz9z2J_CObiV_H2-e8RezSK_sw0KISesp4czsOUlVKY",      "refunded": false,      "review": null,      "shipping": null,      "source_transfer": null,      "statement_descriptor": null,      "statement_descriptor_suffix": null,      "status": "succeeded",      "transfer_data": null,      "transfer_group": null    }    {...}    {...}  ],}`# Capture a charge

Capture the payment of an existing, uncaptured charge that was created with the capture option set to false.

Uncaptured payments expire a set number of days after they are created (7 by default), after which they are marked as refunded and capture attempts will fail.

Don’t use this method to capture a PaymentIntent-initiated charge. Use Capture a PaymentIntent.

### Parameters

- amountintegerThe amount to capture, which must be less than or equal to the original amount. Any additional amount will be automatically refunded.


- receipt_emailstringThe email address to send this charge’s receipt to. This will override the previously-specified email address for this charge, if one was set. Receipts will not be sent in test mode.


- statement_descriptorstringFor card charges, use statement_descriptor_suffix instead. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. Must contain at least one letter, maximum 22 characters.


- statement_descriptor_suffixstringProvides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.



### More parametersExpand all

- application_fee_amountintegerConnect only
- transfer_dataobjectConnect only
- transfer_groupstringConnect only

### Returns

Returns the charge object, with an updated captured property (set to true). Capturing a charge will always succeed, unless the charge is already refunded, expired, captured, or an invalid capture amount is specified, in which case this method will raise an error.

POST/v1/charges/:id/captureServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/charges/ch_3MrVHGLkdIwHu7ix1mN3zEiP/capture \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "ch_3MrVHGLkdIwHu7ix1mN3zEiP",  "object": "charge",  "amount": 1099,  "amount_captured": 1099,  "amount_refunded": 0,  "application": null,  "application_fee": null,  "application_fee_amount": null,  "balance_transaction": "txn_3MrVHGLkdIwHu7ix1Yb1LdXJ",  "billing_details": {    "address": {      "city": null,      "country": null,      "line1": null,      "line2": null,      "postal_code": null,      "state": null    },    "email": null,    "name": null,    "phone": null  },  "calculated_statement_descriptor": "Stripe",  "captured": true,  "created": 1680220390,  "currency": "usd",  "customer": null,  "description": null,  "destination": null,  "dispute": null,  "disputed": false,  "failure_balance_transaction": null,  "failure_code": null,  "failure_message": null,  "fraud_details": {},  "invoice": null,  "livemode": false,  "metadata": {},  "on_behalf_of": null,  "order": null,  "outcome": {    "network_status": "approved_by_network",    "reason": null,    "risk_level": "normal",    "risk_score": 0,    "seller_message": "Payment complete.",    "type": "authorized"  },  "paid": true,  "payment_intent": null,  "payment_method": "card_1MrVHGLkdIwHu7ix7H1PgERt",  "payment_method_details": {    "card": {      "brand": "visa",      "checks": {        "address_line1_check": null,        "address_postal_code_check": null,        "cvc_check": null      },      "country": "US",      "exp_month": 3,      "exp_year": 2024,      "fingerprint": "mToisGZ01V71BCos",      "funding": "credit",      "installments": null,      "last4": "4242",      "mandate": null,      "network": "visa",      "network_token": {        "used": false      },      "three_d_secure": null,      "wallet": null    },    "type": "card"  },  "receipt_email": null,  "receipt_number": null,  "receipt_url": "https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KOfBmKEGMgarecoy8cU6LBYTBSk6QLeqixDK3Wp7agsQfREj3vSXJTrg8SjoxhuNjSJzxMcN6QHTlEDG",  "refunded": false,  "review": null,  "shipping": null,  "source": {    "id": "card_1MrVHGLkdIwHu7ix7H1PgERt",    "object": "card",    "address_city": null,    "address_country": null,    "address_line1": null,    "address_line1_check": null,    "address_line2": null,    "address_state": null,    "address_zip": null,    "address_zip_check": null,    "brand": "Visa",    "country": "US",    "customer": null,    "cvc_check": null,    "dynamic_last4": null,    "exp_month": 3,    "exp_year": 2024,    "fingerprint": "mToisGZ01V71BCos",    "funding": "credit",    "last4": "4242",    "metadata": {},    "name": null,    "tokenization_method": null  },  "source_transfer": null,  "statement_descriptor": null,  "statement_descriptor_suffix": null,  "status": "succeeded",  "transfer_data": null,  "transfer_group": null}`# Search charges

Search for charges you’ve previously created using Stripe’s Search Query Language. Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up to an hour behind during outages. Search functionality is not available to merchants in India.

### Parameters

- querystringRequiredThe search query string. See search query language and the list of supported query fields for charges.


- limitintegerA limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.


- pagestringA cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.



### Returns

A dictionary with a data property that contains an array of up to limit charges. If no objects match the query, the resulting array will be empty. See the related guide on expanding properties in lists.

GET/v1/charges/searchServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/charges/search \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  --data-urlencode query="amount>999 AND metadata['order_id']:'6735'"`Response`{  "object": "search_result",  "url": "/v1/charges/search",  "has_more": false,  "data": [    {      "id": "ch_3MrVHGLkdIwHu7ix3VP9P8qH",      "object": "charge",      "amount": 1000,      "amount_captured": 1000,      "amount_refunded": 0,      "application": null,      "application_fee": null,      "application_fee_amount": null,      "balance_transaction": "txn_3MrVHGLkdIwHu7ix33fWgyw1",      "billing_details": {        "address": {          "city": null,          "country": null,          "line1": null,          "line2": null,          "postal_code": null,          "state": null        },        "email": null,        "name": null,        "phone": null      },      "calculated_statement_descriptor": "Stripe",      "captured": true,      "created": 1680220390,      "currency": "usd",      "customer": null,      "description": null,      "disputed": false,      "failure_balance_transaction": null,      "failure_code": null,      "failure_message": null,      "fraud_details": {},      "invoice": null,      "livemode": false,      "metadata": {        "order_id": "6735"      },      "on_behalf_of": null,      "outcome": {        "network_status": "approved_by_network",        "reason": null,        "risk_level": "normal",        "risk_score": 28,        "seller_message": "Payment complete.",        "type": "authorized"      },      "paid": true,      "payment_intent": null,      "payment_method": "card_1MrVHGLkdIwHu7ixi93aSYS2",      "payment_method_details": {        "card": {          "brand": "visa",          "checks": {            "address_line1_check": null,            "address_postal_code_check": null,            "cvc_check": null          },          "country": "US",          "exp_month": 3,          "exp_year": 2024,          "fingerprint": "mToisGZ01V71BCos",          "funding": "credit",          "installments": null,          "last4": "4242",          "mandate": null,          "network": "visa",          "network_token": {            "used": false          },          "three_d_secure": null,          "wallet": null        },        "type": "card"      },      "receipt_email": null,      "receipt_number": null,      "receipt_url": "https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KOfBmKEGMgY6smXCZpA6LBZYyAwZTSPplSpB7KwcptJiKqQfv6nQiL75NRCxebjOIiABDK3odR96wc2r",      "refunded": false,      "review": null,      "shipping": null,      "source_transfer": null,      "statement_descriptor": null,      "statement_descriptor_suffix": null,      "status": "succeeded",      "transfer_data": null,      "transfer_group": null    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`