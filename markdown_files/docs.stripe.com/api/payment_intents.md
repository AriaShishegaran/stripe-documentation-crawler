htmlPayment Intents | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Payment Intents

A PaymentIntent guides you through the process of collecting a payment from your customer. We recommend that you create exactly one PaymentIntent for each order or customer session in your system. You can reference the PaymentIntent later to see the history of payment attempts for a particular session.

A PaymentIntent transitions through multiple statuses throughout its lifetime as it interfaces with Stripe.js to perform authentication flows and ultimately creates at most one successful charge.

Related guide: Payment Intents API

Endpoints
# The PaymentIntent object

### Attributes

- idstringretrievable with publishable keyUnique identifier for the object.


- amountintegerretrievable with publishable keyAmount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or equivalent in charge currency. The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).


- automatic_payment_methodsnullableobjectretrievable with publishable keySettings to configure compatible payment methods from the Stripe Dashboard

Show child attributes
- client_secretnullablestringretrievable with publishable keyThe client secret of this PaymentIntent. Used for client-side retrieval using a publishable key.

The client secret can be used to complete a payment from your frontend. It should not be stored, logged, or exposed to anyone other than the customer. Make sure that you have TLS enabled on any page that includes the client secret.

Refer to our docs to accept a payment and learn about how client_secret should be handled.


- currencyenumretrievable with publishable keyThree-letter ISO currency code, in lowercase. Must be a supported currency.


- customernullablestringExpandableID of the Customer this PaymentIntent belongs to, if one exists.

Payment methods attached to other Customers cannot be used with this PaymentIntent.

If present in combination with setup_future_usage, this PaymentIntent’s payment method will be attached to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete.


- descriptionnullablestringretrievable with publishable keyAn arbitrary string attached to the object. Often useful for displaying to users.


- last_payment_errornullableobjectretrievable with publishable keyThe payment error encountered in the previous PaymentIntent confirmation. It will be cleared if the PaymentIntent is later updated for any reason.

Show child attributes
- latest_chargenullablestringExpandableThe latest charge created by this PaymentIntent.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Learn more about storing information in metadata.


- next_actionnullableobjectretrievable with publishable keyIf present, this property tells you what actions you need to take in order for your customer to fulfill a payment using the provided source.

Show child attributes
- payment_methodnullablestringExpandableretrievable with publishable keyID of the payment method used in this PaymentIntent.


- receipt_emailnullablestringretrievable with publishable keyEmail address that the receipt for the resulting payment will be sent to. If receipt_email is specified for a payment in live mode, a receipt will be sent regardless of your email settings.


- setup_future_usagenullableenumretrievable with publishable keyIndicates that you intend to make future payments with this PaymentIntent’s payment method.

Providing this parameter will attach the payment method to the PaymentIntent’s Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be attached to a Customer after the transaction completes.

When processing card payments, Stripe also uses setup_future_usage to dynamically optimize your payment flow and comply with regional legislation and network rules, such as SCA.

Possible enum values`off_session`Use off_session if your customer may or may not be present in your checkout flow.

`on_session`Use on_session if you intend to only reuse the payment method when your customer is present in your checkout flow.


- shippingnullableobjectretrievable with publishable keyShipping information for this PaymentIntent.

Show child attributes
- statement_descriptornullablestringFor card charges, use statement_descriptor_suffix. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. It must contain at least one letter and be 1–22 characters long.


- statement_descriptor_suffixnullablestringProvides information about a card payment that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.


- statusenumretrievable with publishable keyStatus of this PaymentIntent, one of requires_payment_method, requires_confirmation, requires_action, processing, requires_capture, canceled, or succeeded. Read more about each PaymentIntent status.

Possible enum values`canceled``processing``requires_action``requires_capture``requires_confirmation``requires_payment_method``succeeded`

### More attributesExpand all

- objectstringretrievable with publishable key
- amount_capturableinteger
- amount_detailsnullableobject
- amount_receivedinteger
- applicationnullablestringExpandableConnect only
- application_fee_amountnullableintegerConnect only
- canceled_atnullabletimestampretrievable with publishable key
- cancellation_reasonnullableenumretrievable with publishable key
- capture_methodenumretrievable with publishable key
- confirmation_methodenumretrievable with publishable key
- createdtimestampretrievable with publishable key
- invoicenullablestringExpandable
- livemodebooleanretrievable with publishable key
- on_behalf_ofnullablestringExpandableConnect only
- payment_method_configuration_detailsnullableobject
- payment_method_optionsnullableobject
- payment_method_typesarray of stringsretrievable with publishable key
- processingnullableobjectretrievable with publishable key
- reviewnullablestringExpandable
- transfer_datanullableobjectConnect only
- transfer_groupnullablestringConnect only

The PaymentIntent object`{  "id": "pi_3MtwBwLkdIwHu7ix28a3tqPa",  "object": "payment_intent",  "amount": 2000,  "amount_capturable": 0,  "amount_details": {    "tip": {}  },  "amount_received": 0,  "application": null,  "application_fee_amount": null,  "automatic_payment_methods": {    "enabled": true  },  "canceled_at": null,  "cancellation_reason": null,  "capture_method": "automatic",  "client_secret": "pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH",  "confirmation_method": "automatic",  "created": 1680800504,  "currency": "usd",  "customer": null,  "description": null,  "invoice": null,  "last_payment_error": null,  "latest_charge": null,  "livemode": false,  "metadata": {},  "next_action": null,  "on_behalf_of": null,  "payment_method": null,  "payment_method_options": {    "card": {      "installments": null,      "mandate_options": null,      "network": null,      "request_three_d_secure": "automatic"    },    "link": {      "persistent_token": null    }  },  "payment_method_types": [    "card",    "link"  ],  "processing": null,  "receipt_email": null,  "review": null,  "setup_future_usage": null,  "shipping": null,  "source": null,  "statement_descriptor": null,  "statement_descriptor_suffix": null,  "status": "requires_payment_method",  "transfer_data": null,  "transfer_group": null}`# Create a PaymentIntent

Creates a PaymentIntent object.

After the PaymentIntent is created, attach a payment method and confirm to continue the payment. Learn more about the available payment flows with the Payment Intents API.

When you use confirm=true during creation, it’s equivalent to creating and confirming the PaymentIntent in the same call. You can use any parameters available in the confirm API when you supply confirm=true.

### Parameters

- amountintegerRequiredAmount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or equivalent in charge currency. The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).


- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.


- automatic_payment_methodsobjectWhen you enable this parameter, this PaymentIntent accepts payment methods that you enable in the Dashboard and that are compatible with this PaymentIntent’s other parameters.

Show child parameters
- confirmbooleanSet to true to attempt to confirm this PaymentIntent immediately. This parameter defaults to false. When creating and confirming a PaymentIntent at the same time, you can also provide the parameters available in the Confirm API.


- customerstringID of the Customer this PaymentIntent belongs to, if one exists.

Payment methods attached to other Customers cannot be used with this PaymentIntent.

If present in combination with setup_future_usage, this PaymentIntent’s payment method will be attached to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete.


- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- off_sessionboolean | stringonly when confirm=trueSet to true to indicate that the customer isn’t in your checkout flow during this payment attempt and can’t authenticate. Use this parameter in scenarios where you collect card details and charge them later. This parameter can only be used with confirm=true.


- payment_methodstringID of the payment method (a PaymentMethod, Card, or compatible Source object) to attach to this PaymentIntent.

If you omit this parameter with confirm=true, customer.default_source attaches as this PaymentIntent’s payment instrument to improve migration for users of the Charges API. We recommend that you explicitly provide the payment_method moving forward.


- receipt_emailstringEmail address to send the receipt to. If you specify receipt_email for a payment in live mode, you send a receipt regardless of your email settings.


- setup_future_usageenumIndicates that you intend to make future payments with this PaymentIntent’s payment method.

Providing this parameter will attach the payment method to the PaymentIntent’s Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be attached to a Customer after the transaction completes.

When processing card payments, Stripe also uses setup_future_usage to dynamically optimize your payment flow and comply with regional legislation and network rules, such as SCA.

Possible enum values`off_session`Use off_session if your customer may or may not be present in your checkout flow.

`on_session`Use on_session if you intend to only reuse the payment method when your customer is present in your checkout flow.


- shippingobjectShipping information for this PaymentIntent.

Show child parameters
- statement_descriptorstringFor card charges, use statement_descriptor_suffix. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. It must contain at least one letter and be 1–22 characters long.


- statement_descriptor_suffixstringProvides information about a card payment that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. The concatenated descriptor must contain 1-22 characters.



### More parametersExpand all

- application_fee_amountintegerConnect only
- capture_methodenum
- confirmation_methodenum
- confirmation_tokenstringonly when confirm=true
- error_on_requires_actionbooleanonly when confirm=true
- mandatestringonly when confirm=true
- mandate_dataobjectonly when confirm=true
- on_behalf_ofstringConnect only
- payment_method_configurationstring
- payment_method_dataobject
- payment_method_optionsobject
- payment_method_typesarray of strings
- radar_optionsobject
- return_urlstringonly when confirm=true
- transfer_dataobjectConnect only
- transfer_groupstringConnect only
- use_stripe_sdkboolean

### Returns

Returns a PaymentIntent object.

POST/v1/payment_intentsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_intents \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d amount=2000 \  -d currency=usd \  -d "automatic_payment_methods[enabled]"=true`Response`{  "id": "pi_3MtwBwLkdIwHu7ix28a3tqPa",  "object": "payment_intent",  "amount": 2000,  "amount_capturable": 0,  "amount_details": {    "tip": {}  },  "amount_received": 0,  "application": null,  "application_fee_amount": null,  "automatic_payment_methods": {    "enabled": true  },  "canceled_at": null,  "cancellation_reason": null,  "capture_method": "automatic",  "client_secret": "pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH",  "confirmation_method": "automatic",  "created": 1680800504,  "currency": "usd",  "customer": null,  "description": null,  "invoice": null,  "last_payment_error": null,  "latest_charge": null,  "livemode": false,  "metadata": {},  "next_action": null,  "on_behalf_of": null,  "payment_method": null,  "payment_method_options": {    "card": {      "installments": null,      "mandate_options": null,      "network": null,      "request_three_d_secure": "automatic"    },    "link": {      "persistent_token": null    }  },  "payment_method_types": [    "card",    "link"  ],  "processing": null,  "receipt_email": null,  "review": null,  "setup_future_usage": null,  "shipping": null,  "source": null,  "statement_descriptor": null,  "statement_descriptor_suffix": null,  "status": "requires_payment_method",  "transfer_data": null,  "transfer_group": null}`# Update a PaymentIntent

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

GET/v1/payment_intents/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_intents/pi_3MtwBwLkdIwHu7ix28a3tqPa \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "pi_3MtwBwLkdIwHu7ix28a3tqPa",  "object": "payment_intent",  "amount": 2000,  "amount_capturable": 0,  "amount_details": {    "tip": {}  },  "amount_received": 0,  "application": null,  "application_fee_amount": null,  "automatic_payment_methods": {    "enabled": true  },  "canceled_at": null,  "cancellation_reason": null,  "capture_method": "automatic",  "client_secret": "pi_3MtwBwLkdIwHu7ix28a3tqPa_secret_YrKJUKribcBjcG8HVhfZluoGH",  "confirmation_method": "automatic",  "created": 1680800504,  "currency": "usd",  "customer": null,  "description": null,  "invoice": null,  "last_payment_error": null,  "latest_charge": null,  "livemode": false,  "metadata": {},  "next_action": null,  "on_behalf_of": null,  "payment_method": null,  "payment_method_options": {    "card": {      "installments": null,      "mandate_options": null,      "network": null,      "request_three_d_secure": "automatic"    },    "link": {      "persistent_token": null    }  },  "payment_method_types": [    "card",    "link"  ],  "processing": null,  "receipt_email": null,  "review": null,  "setup_future_usage": null,  "shipping": null,  "source": null,  "statement_descriptor": null,  "statement_descriptor_suffix": null,  "status": "requires_payment_method",  "transfer_data": null,  "transfer_group": null}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`