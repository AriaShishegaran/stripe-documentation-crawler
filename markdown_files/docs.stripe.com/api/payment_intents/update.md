htmlUpdate a PaymentIntent | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Update a PaymentIntent

Updates properties on a PaymentIntent object without confirming.

Depending on which properties you update, you might need to confirm the PaymentIntent again. For example, updating the payment_method always requires you to confirm the PaymentIntent again. If you prefer to update and confirm at the same time, we recommend updating properties through the confirm API instead.

### Parameters

- amountintegerAmount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or equivalent in charge currency. The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).


- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- customerstringID of the Customer this PaymentIntent belongs to, if one exists.

Payment methods attached to other Customers cannot be used with this PaymentIntent.

If present in combination with setup_future_usage, this PaymentIntent’s payment method will be attached to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete.


- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- payment_methodstringID of the payment method (a PaymentMethod, Card, or compatible Source object) to attach to this PaymentIntent.


- receipt_emailstringEmail address that the receipt for the resulting payment will be sent to. If receipt_email is specified for a payment in live mode, a receipt will be sent regardless of your email settings.


- setup_future_usageenumIndicates that you intend to make future payments with this PaymentIntent’s payment method.

Providing this parameter will attach the payment method to the PaymentIntent’s Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be attached to a Customer after the transaction completes.

When processing card payments, Stripe also uses setup_future_usage to dynamically optimize your payment flow and comply with regional legislation and network rules, such as SCA.

If setup_future_usage is already set and you are performing a request using a publishable key, you may only update the value from on_session to off_session.

Possible enum values`off_session`Use off_session if your customer may or may not be present in your checkout flow.

`on_session`Use on_session if you intend to only reuse the payment method when your customer is present in your checkout flow.


- shippingobjectShipping information for this PaymentIntent.

Show child parameters
- statement_descriptorstringFor card charges, use statement_descriptor_suffix. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. It must contain at least one letter and be 1–22 characters long.


- statement_descriptor_suffixstringProvides information about a card payment that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.



### More parametersExpand all

- application_fee_amountintegerConnect only
- capture_methodenumsecret key only
- payment_method_configurationstring
- payment_method_dataobject
- payment_method_optionsobject
- payment_method_typesarray of strings
- transfer_dataobjectConnect only
- transfer_groupstringConnect only

### Returns

Returns a PaymentIntent object.

POST/v1/payment_intents/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_intents/pi_3MtwBwLkdIwHu7ix28a3tqPa \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "pi_3MtwBwLkdIwHu7ix28a3tqPa",  "object": "payment_intent",  "amount": 2000,  "amount_capturable": 0,  "amount_details": {    "tip": {}  },  "amount_received": 0,  "application": null,  "application_fee_amount": null,  "automatic_payment_methods": {    "enabled": true  },  "canceled_at": null,  "cancellation_reason": null,  "capture_method": "automatic",  "client_secret": "pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH",  "confirmation_method": "automatic",  "created": 1680800504,  "currency": "usd",  "customer": null,  "description": null,  "invoice": null,  "last_payment_error": null,  "latest_charge": null,  "livemode": false,  "metadata": {    "order_id": "6735"  },  "next_action": null,  "on_behalf_of": null,  "payment_method": null,  "payment_method_options": {    "card": {      "installments": null,      "mandate_options": null,      "network": null,      "request_three_d_secure": "automatic"    },    "link": {      "persistent_token": null    }  },  "payment_method_types": [    "card",    "link"  ],  "processing": null,  "receipt_email": null,  "review": null,  "setup_future_usage": null,  "shipping": null,  "source": null,  "statement_descriptor": null,  "statement_descriptor_suffix": null,  "status": "requires_payment_method",  "transfer_data": null,  "transfer_group": null}`# Retrieve a PaymentIntent

Retrieves the details of a PaymentIntent that has previously been created.

You can retrieve a PaymentIntent client-side using a publishable key when the client_secret is in the query string.

If you retrieve a PaymentIntent with a publishable key, it only returns a subset of properties. Refer to the payment intent object reference for more details.

### Parameters

- client_secretstringRequired if you use a publishable key.The client secret of the PaymentIntent. We require it if you use a publishable key to retrieve the source.



### Returns

Returns a PaymentIntent if a valid identifier was provided.

GET/v1/payment_intents/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_intents/pi_3MtwBwLkdIwHu7ix28a3tqPa \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "pi_3MtwBwLkdIwHu7ix28a3tqPa",  "object": "payment_intent",  "amount": 2000,  "amount_capturable": 0,  "amount_details": {    "tip": {}  },  "amount_received": 0,  "application": null,  "application_fee_amount": null,  "automatic_payment_methods": {    "enabled": true  },  "canceled_at": null,  "cancellation_reason": null,  "capture_method": "automatic",  "client_secret": "pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH",  "confirmation_method": "automatic",  "created": 1680800504,  "currency": "usd",  "customer": null,  "description": null,  "invoice": null,  "last_payment_error": null,  "latest_charge": null,  "livemode": false,  "metadata": {},  "next_action": null,  "on_behalf_of": null,  "payment_method": null,  "payment_method_options": {    "card": {      "installments": null,      "mandate_options": null,      "network": null,      "request_three_d_secure": "automatic"    },    "link": {      "persistent_token": null    }  },  "payment_method_types": [    "card",    "link"  ],  "processing": null,  "receipt_email": null,  "review": null,  "setup_future_usage": null,  "shipping": null,  "source": null,  "statement_descriptor": null,  "statement_descriptor_suffix": null,  "status": "requires_payment_method",  "transfer_data": null,  "transfer_group": null}`# List all PaymentIntents

Returns a list of PaymentIntents.

### Parameters

- customerstringOnly return PaymentIntents for the customer that this customer ID specifies.



### More parametersExpand all

- createdobject
- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit PaymentIntents, starting after PaymentIntent starting_after. Each entry in the array is a separate PaymentIntent object. If no other PaymentIntents are available, the resulting array is empty.

GET/v1/payment_intentsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/payment_intents \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/payment_intents",  "has_more": false,  "data": [    {      "id": "pi_3MtwBwLkdIwHu7ix28a3tqPa",      "object": "payment_intent",      "amount": 2000,      "amount_capturable": 0,      "amount_details": {        "tip": {}      },      "amount_received": 0,      "application": null,      "application_fee_amount": null,      "automatic_payment_methods": {        "enabled": true      },      "canceled_at": null,      "cancellation_reason": null,      "capture_method": "automatic",      "client_secret": "pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH",      "confirmation_method": "automatic",      "created": 1680800504,      "currency": "usd",      "customer": null,      "description": null,      "invoice": null,      "last_payment_error": null,      "latest_charge": null,      "livemode": false,      "metadata": {},      "next_action": null,      "on_behalf_of": null,      "payment_method": null,      "payment_method_options": {        "card": {          "installments": null,          "mandate_options": null,          "network": null,          "request_three_d_secure": "automatic"        },        "link": {          "persistent_token": null        }      },      "payment_method_types": [        "card",        "link"      ],      "processing": null,      "receipt_email": null,      "review": null,      "setup_future_usage": null,      "shipping": null,      "source": null,      "statement_descriptor": null,      "statement_descriptor_suffix": null,      "status": "requires_payment_method",      "transfer_data": null,      "transfer_group": null    }    {...}    {...}  ],}`# Cancel a PaymentIntent

You can cancel a PaymentIntent object when it’s in one of these statuses: requires_payment_method, requires_capture, requires_confirmation, requires_action or, in rare cases, processing.

After it’s canceled, no additional charges are made by the PaymentIntent and any operations on the PaymentIntent fail with an error. For PaymentIntents with a status of requires_capture, the remaining amount_capturable is automatically refunded.

You can’t cancel the PaymentIntent for a Checkout Session. Expire the Checkout Session instead.

### Parameters

- cancellation_reasonstringReason for canceling this PaymentIntent. Possible values are: duplicate, fraudulent, requested_by_customer, or abandoned



### Returns

Returns a PaymentIntent object if the cancellation succeeds. Returns an error if the PaymentIntent is already canceled or isn’t in a cancelable state.

POST/v1/payment_intents/:id/cancelServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/payment_intents/pi_3MtwBwLkdIwHu7ix28a3tqPa/cancel \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "pi_3MtwBwLkdIwHu7ix28a3tqPa",  "object": "payment_intent",  "amount": 2000,  "amount_capturable": 0,  "amount_details": {    "tip": {}  },  "amount_received": 0,  "application": null,  "application_fee_amount": null,  "automatic_payment_methods": {    "enabled": true  },  "canceled_at": 1680801569,  "cancellation_reason": null,  "capture_method": "automatic",  "client_secret": "pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH",  "confirmation_method": "automatic",  "created": 1680800504,  "currency": "usd",  "customer": null,  "description": null,  "invoice": null,  "last_payment_error": null,  "latest_charge": null,  "livemode": false,  "metadata": {},  "next_action": null,  "on_behalf_of": null,  "payment_method": null,  "payment_method_options": {    "card": {      "installments": null,      "mandate_options": null,      "network": null,      "request_three_d_secure": "automatic"    },    "link": {      "persistent_token": null    }  },  "payment_method_types": [    "card",    "link"  ],  "processing": null,  "receipt_email": null,  "review": null,  "setup_future_usage": null,  "shipping": null,  "source": null,  "statement_descriptor": null,  "statement_descriptor_suffix": null,  "status": "canceled",  "transfer_data": null,  "transfer_group": null}`# Capture a PaymentIntent

Capture the funds of an existing uncaptured PaymentIntent when its status is requires_capture.

Uncaptured PaymentIntents are cancelled a set number of days (7 by default) after their creation.

Learn more about separate authorization and capture.

### Parameters

- amount_to_captureintegerThe amount to capture from the PaymentIntent, which must be less than or equal to the original amount. Any additional amount is automatically refunded. Defaults to the full amount_capturable if it’s not provided.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- application_fee_amountintegerConnect only
- final_captureboolean
- statement_descriptorstring
- statement_descriptor_suffixstring
- transfer_dataobjectConnect only

### Returns

Returns a PaymentIntent object with status="succeeded" if the PaymentIntent is capturable. Returns an error if the PaymentIntent isn’t capturable or if an invalid amount to capture is provided.

POST/v1/payment_intents/:id/captureServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/payment_intents/pi_3MrPBM2eZvKYlo2C1TEMacFD/capture \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "pi_3MrPBM2eZvKYlo2C1TEMacFD",  "object": "payment_intent",  "amount": 1000,  "amount_capturable": 0,  "amount_details": {    "tip": {}  },  "amount_received": 1000,  "application": null,  "application_fee_amount": null,  "automatic_payment_methods": null,  "canceled_at": null,  "cancellation_reason": null,  "capture_method": "automatic",  "client_secret": "pi_3MrPBM2eZvKYlo2C1TEMacFD_secret_9J35eTzWlxVmfbbQhmkNbewuL",  "confirmation_method": "automatic",  "created": 1524505326,  "currency": "usd",  "customer": null,  "description": "One blue fish",  "invoice": null,  "last_payment_error": null,  "latest_charge": "ch_1EXUPv2eZvKYlo2CStIqOmbY",  "livemode": false,  "metadata": {},  "next_action": null,  "on_behalf_of": null,  "payment_method": "pm_1EXUPv2eZvKYlo2CUkqZASBe",  "payment_method_options": {},  "payment_method_types": [    "card"  ],  "processing": null,  "receipt_email": null,  "redaction": null,  "review": null,  "setup_future_usage": null,  "shipping": null,  "statement_descriptor": null,  "statement_descriptor_suffix": null,  "status": "succeeded",  "transfer_data": null,  "transfer_group": null}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`