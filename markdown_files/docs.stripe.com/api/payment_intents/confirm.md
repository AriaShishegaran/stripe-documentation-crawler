htmlConfirm a PaymentIntent | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Confirm a PaymentIntent

Confirm that your customer intends to pay with current or provided payment method. Upon confirmation, the PaymentIntent will attempt to initiate a payment. If the selected payment method requires additional authentication steps, the PaymentIntent will transition to the requires_action status and suggest additional actions via next_action. If payment fails, the PaymentIntent transitions to the requires_payment_method status or the canceled status if the confirmation limit is reached.  If payment succeeds, the PaymentIntent will transition to the succeeded status (or requires_capture, if capture_method is set to manual). If the confirmation_method is automatic, payment may be attempted using our client SDKs and the PaymentIntent’s client_secret. After next_actions are handled by the client, no additional confirmation is required to complete the payment. If the confirmation_method is manual, all payment attempts must be initiated using a secret key. If any actions are required for the payment, the PaymentIntent will return to the requires_confirmation state after those actions are completed. Your server needs to then explicitly re-confirm the PaymentIntent to initiate the next payment attempt.

### Parameters

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

### More parametersExpand all

- capture_methodenumsecret key only
- confirmation_tokenstring
- error_on_requires_actionboolean
- mandatestringsecret key only
- mandate_dataobject
- off_sessionboolean | stringsecret key only
- payment_method_dataobject
- payment_method_optionsobjectsecret key only
- payment_method_typesarray of stringssecret key only
- radar_optionsobjectsecret key only
- return_urlstring
- use_stripe_sdkboolean

### Returns

Returns the resulting PaymentIntent after all possible transitions are applied.

POST/v1/payment_intents/:id/confirmServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_intents/pi_3MtweELkdIwHu7ix0Dt0gF2H/confirm \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d payment_method=pm_card_visa \  --data-urlencode return_url="https://www.example.com"`Response`{  "id": "pi_3MtweELkdIwHu7ix0Dt0gF2H",  "object": "payment_intent",  "amount": 2000,  "amount_capturable": 0,  "amount_details": {    "tip": {}  },  "amount_received": 2000,  "application": null,  "application_fee_amount": null,  "automatic_payment_methods": {    "enabled": true  },  "canceled_at": null,  "cancellation_reason": null,  "capture_method": "automatic",  "client_secret": "pi_3MtweELkdIwHu7ix0Dt0gF2H_secret_ALlpPMIZse0ac8YzPxkMkFgGC",  "confirmation_method": "automatic",  "created": 1680802258,  "currency": "usd",  "customer": null,  "description": null,  "invoice": null,  "last_payment_error": null,  "latest_charge": "ch_3MtweELkdIwHu7ix05lnLAFd",  "livemode": false,  "metadata": {},  "next_action": null,  "on_behalf_of": null,  "payment_method": "pm_1MtweELkdIwHu7ixxrsejPtG",  "payment_method_options": {    "card": {      "installments": null,      "mandate_options": null,      "network": null,      "request_three_d_secure": "automatic"    },    "link": {      "persistent_token": null    }  },  "payment_method_types": [    "card",    "link"  ],  "processing": null,  "receipt_email": null,  "review": null,  "setup_future_usage": null,  "shipping": null,  "source": null,  "statement_descriptor": null,  "statement_descriptor_suffix": null,  "status": "succeeded",  "transfer_data": null,  "transfer_group": null}`# Increment an authorization

Perform an incremental authorization on an eligible PaymentIntent. To be eligible, the PaymentIntent’s status must be requires_capture and incremental_authorization_supported must be true.

Incremental authorizations attempt to increase the authorized amount on your customer’s card to the new, higher amount provided. Similar to the initial authorization, incremental authorizations can be declined. A single PaymentIntent can call this endpoint multiple times to further increase the authorized amount.

If the incremental authorization succeeds, the PaymentIntent object returns with the updated amount. If the incremental authorization fails, a card_declined error returns, and no other fields on the PaymentIntent or Charge update. The PaymentIntent object remains capturable for the previously authorized amount.

Each PaymentIntent can have a maximum of 10 incremental authorization attempts, including declines. After it’s captured, a PaymentIntent can no longer be incremented.

Learn more about incremental authorizations.

### Parameters

- amountintegerRequiredThe updated total amount that you intend to collect from the cardholder. This amount must be greater than the currently authorized amount.


- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- statement_descriptorstringFor card charges, use statement_descriptor_suffix. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. It must contain at least one letter and be 1–22 characters long.



### More parametersExpand all

- application_fee_amountintegerConnect only
- transfer_dataobjectConnect only

### Returns

Returns a PaymentIntent object with the updated amount if the incremental authorization succeeds. Returns an error if the incremental authorization failed or the PaymentIntent isn’t eligible for incremental authorizations.

POST/v1/payment_intents/:id/increment_authorizationServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_intents/pi_1DtBRR2eZvKYlo2CmCVxxvd7/increment_authorization \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d amount=2099`Response`{  "id": "pi_1DtBRR2eZvKYlo2CmCVxxvd7",  "object": "payment_intent",  "amount": 2099,  "amount_capturable": 2099,  "amount_details": {    "tip": {}  },  "amount_received": 0,  "application": null,  "application_fee_amount": null,  "automatic_payment_methods": null,  "canceled_at": null,  "cancellation_reason": null,  "capture_method": "manual",  "client_secret": "pi_1DtBRR2eZvKYlo2CmCVxxvd7_secret_cWsUkvyTOjhLKh5Wxu61nYc0i",  "confirmation_method": "automatic",  "created": 1680196960,  "currency": "usd",  "customer": null,  "description": null,  "invoice": null,  "last_payment_error": null,  "latest_charge": "ch_3MrPBM2eZvKYlo2C1CEBUD4A",  "livemode": false,  "metadata": {},  "next_action": null,  "on_behalf_of": null,  "payment_method": "pm_1MrPBL2eZvKYlo2CaNa8L11Z",  "payment_method_options": {    "card": {      "installments": null,      "mandate_options": null,      "network": null,      "request_three_d_secure": "automatic"    }  },  "payment_method_types": [    "card"  ],  "processing": null,  "receipt_email": null,  "redaction": null,  "review": null,  "setup_future_usage": null,  "shipping": null,  "statement_descriptor": null,  "statement_descriptor_suffix": null,  "status": "requires_capture",  "transfer_data": null,  "transfer_group": null}`# Reconcile a customer_balance PaymentIntent

Manually reconcile the remaining amount for a customer_balance PaymentIntent.

### Parameters

- amountintegerAmount that you intend to apply to this PaymentIntent from the customer’s cash balance.

A positive integer representing how much to charge in the smallest currency unit (for example, 100 cents to charge 1 USD or 100 to charge 100 JPY, a zero-decimal currency).

The maximum amount is the amount of the PaymentIntent.

When you omit the amount, it defaults to the remaining amount requested on the PaymentIntent.


- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.



### Returns

Returns a PaymentIntent object.

POST/v1/payment_intents/:id/apply_customer_balanceServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/payment_intents/pi_1GszwY2eZvKYlo2CohCEmT6b/apply_customer_balance \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "pi_1GszwY2eZvKYlo2CohCEmT6b",  "object": "payment_intent",  "amount": 1000,  "amount_capturable": 0,  "amount_details": {    "tip": {}  },  "amount_received": 0,  "application": null,  "application_fee_amount": null,  "automatic_payment_methods": null,  "canceled_at": null,  "cancellation_reason": null,  "capture_method": "automatic",  "client_secret": "pi_1GszwY2eZvKYlo2CohCEmT6b_secret_1jQJzqkrQvx4BpwI5hn6WSEO5",  "confirmation_method": "automatic",  "created": 1591918582,  "currency": "usd",  "customer": null,  "description": "Created by stripe.com/docs demo",  "invoice": null,  "last_payment_error": null,  "latest_charge": null,  "livemode": false,  "metadata": {},  "next_action": null,  "on_behalf_of": null,  "payment_method": null,  "payment_method_options": {    "card": {      "installments": null,      "mandate_options": null,      "network": null,      "request_three_d_secure": "automatic"    }  },  "payment_method_types": [    "card"  ],  "processing": null,  "receipt_email": null,  "redaction": null,  "review": null,  "setup_future_usage": null,  "shipping": null,  "statement_descriptor": null,  "statement_descriptor_suffix": null,  "status": "requires_payment_method",  "transfer_data": null,  "transfer_group": null}`# Search PaymentIntents

Search for PaymentIntents you’ve previously created using Stripe’s Search Query Language. Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up to an hour behind during outages. Search functionality is not available to merchants in India.

### Parameters

- querystringRequiredThe search query string. See search query language and the list of supported query fields for payment intents.


- limitintegerA limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.


- pagestringA cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.



### Returns

A dictionary with a data property that contains an array of up to limit PaymentIntents. If no objects match the query, the resulting array will be empty. See the related guide on expanding properties in lists.

GET/v1/payment_intents/searchServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/payment_intents/search \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d query="amount>1000"`Response`{  "object": "search_result",  "url": "/v1/payment_intents/search",  "has_more": false,  "data": [    {      "id": "pi_3MtwBwLkdIwHu7ix28a3tqPa",      "object": "payment_intent",      "amount": 2000,      "amount_capturable": 0,      "amount_details": {        "tip": {}      },      "amount_received": 0,      "application": null,      "application_fee_amount": null,      "automatic_payment_methods": {        "enabled": true      },      "canceled_at": null,      "cancellation_reason": null,      "capture_method": "automatic",      "client_secret": "pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH",      "confirmation_method": "automatic",      "created": 1680800504,      "currency": "usd",      "customer": null,      "description": null,      "invoice": null,      "last_payment_error": null,      "latest_charge": null,      "livemode": false,      "metadata": {},      "next_action": null,      "on_behalf_of": null,      "payment_method": null,      "payment_method_options": {        "card": {          "installments": null,          "mandate_options": null,          "network": null,          "request_three_d_secure": "automatic"        },        "link": {          "persistent_token": null        }      },      "payment_method_types": [        "card",        "link"      ],      "processing": null,      "receipt_email": null,      "review": null,      "setup_future_usage": null,      "shipping": null,      "source": null,      "statement_descriptor": null,      "statement_descriptor_suffix": null,      "status": "requires_payment_method",      "transfer_data": null,      "transfer_group": null    }    {...}    {...}  ],}`# Verify microdeposits on a PaymentIntent

Verifies microdeposits on a PaymentIntent object.

### Parameters

- amountsarray of integersTwo positive integers, in cents, equal to the values of the microdeposits sent to the bank account.


- descriptor_codestringA six-character code starting with SM present in the microdeposit sent to the bank account.



### Returns

Returns a PaymentIntent object.

POST/v1/payment_intents/:id/verify_microdepositsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_intents/pi_1DtBRR2eZvKYlo2CmCVxxvd7/verify_microdeposits \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "amounts[]"=32 \  -d "amounts[]"=45`Response`{  "id": "pi_1DtBRR2eZvKYlo2CmCVxxvd7",  "object": "payment_intent",  "amount": 1099,  "amount_capturable": 0,  "amount_details": {    "tip": {}  },  "amount_received": 0,  "application": null,  "application_fee_amount": null,  "automatic_payment_methods": null,  "canceled_at": null,  "cancellation_reason": null,  "capture_method": "automatic",  "client_secret": "pi_1DtBRR2eZvKYlo2CmCVxxvd7_secret_l80vlOGz9kZQwnzocExJQUsJx",  "confirmation_method": "automatic",  "created": 1680800210,  "currency": "usd",  "customer": null,  "description": null,  "invoice": null,  "last_payment_error": null,  "latest_charge": null,  "livemode": false,  "metadata": {},  "next_action": null,  "on_behalf_of": null,  "payment_method": "pm_1Mtw7C2eZvKYlo2CPsW0F8g0",  "payment_method_options": {    "acss_debit": {      "mandate_options": {        "interval_description": "First day of every month",        "payment_schedule": "interval",        "transaction_type": "personal"      },      "verification_method": "automatic"    }  },  "payment_method_types": [    "acss_debit"  ],  "processing": null,  "receipt_email": null,  "redaction": null,  "review": null,  "setup_future_usage": null,  "shipping": null,  "statement_descriptor": null,  "statement_descriptor_suffix": null,  "status": "succeeded",  "transfer_data": null,  "transfer_group": null}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`