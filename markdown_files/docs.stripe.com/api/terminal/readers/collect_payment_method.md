htmlHand-off a PaymentIntent to a Reader and collect card details | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Hand-off a PaymentIntent to a Reader and collect card detailsPreview feature

Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation.

### Parameters

- payment_intentstringRequiredPaymentIntent ID



### More parametersExpand all

- collect_configobject

### Returns

Returns an updated Reader resource.

POST/v1/terminal/readers/:id/collect_payment_methodcURL[](#)[](#)`curl https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7/collect_payment_method \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d payment_intent=pi_1NrpbFBHO5VeT9SUiCEDMdc8`Response`{  "id": "tmr_FDOt2wlRZEdpd7",  "object": "terminal.reader",  "action": {    "failure_code": null,    "failure_message": null,    "collect_payment_method": {      "payment_intent": "pi_1NrpbFBHO5VeT9SUiCEDMdc8"    },    "status": "in_progress",    "type": "collect_payment_method"  },  "device_sw_version": "",  "device_type": "simulated_wisepos_e",  "ip_address": "0.0.0.0",  "label": "Blue Rabbit",  "last_seen_at": 1681320543815,  "livemode": false,  "location": "tml_FDOtHwxAAdIJOh",  "metadata": {},  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",  "status": "online"}`# Hand-off a PaymentIntent to a Reader

Initiates a payment flow on a Reader.

### Parameters

- payment_intentstringRequiredPaymentIntent ID



### More parametersExpand all

- process_configobject

### Returns

Returns an updated Reader resource.

POST/v1/terminal/readers/:id/process_payment_intentServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7/process_payment_intent \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d payment_intent=pi_3NtEKRLkdIwHu7ix3crEirSx`Response`{  "id": "tmr_FDOt2wlRZEdpd7",  "object": "terminal.reader",  "action": {    "failure_code": null,    "failure_message": null,    "process_payment_intent": {      "payment_intent": "pi_3NtEKRLkdIwHu7ix3crEirSx"    },    "status": "in_progress",    "type": "process_payment_intent"  },  "device_sw_version": "",  "device_type": "simulated_wisepos_e",  "ip_address": "0.0.0.0",  "label": "Blue Rabbit",  "last_seen_at": 1695408232226,  "livemode": false,  "location": "tml_FDOtHwxAAdIJOh",  "metadata": {},  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",  "status": "online"}`# Hand-off a SetupIntent to a Reader

Initiates a setup intent flow on a Reader.

### Parameters

- customer_consent_collectedbooleanRequiredCustomer Consent Collected


- setup_intentstringRequiredSetupIntent ID



### More parametersExpand all

- process_configobject

### Returns

Returns an updated Reader resource.

POST/v1/terminal/readers/:id/process_setup_intentServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7/process_setup_intent \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d customer_consent_collected=true \  -d setup_intent=seti_1NtEXHLkdIwHu7ixcBcUmqfe`Response`{  "id": "tmr_FDOt2wlRZEdpd7",  "object": "terminal.reader",  "action": {    "failure_code": null,    "failure_message": null,    "process_setup_intent": {      "setup_intent": "seti_1NtEXHLkdIwHu7ixcBcUmqfe"    },    "status": "in_progress",    "type": "process_setup_intent"  },  "device_sw_version": "",  "device_type": "simulated_wisepos_e",  "ip_address": "0.0.0.0",  "label": "Blue Rabbit",  "last_seen_at": 1681320543815,  "livemode": false,  "location": "tml_FDOtHwxAAdIJOh",  "metadata": {},  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",  "status": "online"}`# Refund a Charge or a PaymentIntent in-person

Initiates a refund on a Reader

### Parameters

- amountintegerA positive integer in cents representing how much of this charge to refund.


- chargestringID of the Charge to refund.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- payment_intentstringID of the PaymentIntent to refund.


- refund_application_feebooleanConnect onlyBoolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge.


- reverse_transferbooleanConnect onlyBoolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount). A transfer can be reversed only by the application that created the charge.



### More parametersExpand all

- refund_payment_configobject

### Returns

Returns an updated Reader resource

POST/v1/terminal/readers/:id/refund_paymentServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/terminal/readers/tmr_njDFG9Z5k7y7KeQI8RmZYDYT/refund_payment \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d payment_intent=pi_1NrpbFBHO5VeT9SUiCEDMdc8`Response`{  "id": "tmr_njDFG9Z5k7y7KeQI8RmZYDYT",  "object": "terminal.reader",  "action": {    "failure_code": null,    "failure_message": null,    "refund_payment": {      "payment_intent": "pi_1NrpbFBHO5VeT9SUiCEDMdc8",      "amount": 1000    },    "status": "in_progress",    "type": "refund_payment"  },  "device_deploy_group": null,  "device_sw_version": null,  "device_type": "bbpos_wisepos_e",  "ip_address": "192.168.2.2",  "label": "Blue Rabbit",  "livemode": false,  "location": null,  "metadata": {},  "serial_number": "123-456-789",  "software": null,  "status": "online"}`# Set reader display

Sets reader display to show cart details.

### Parameters

- typeenumRequiredType


- cartobjectCart

Show child parameters

### Returns

Returns an updated Reader resource.

POST/v1/terminal/readers/:id/set_reader_displayServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7/set_reader_display \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d type=cart \  -d "cart[currency]"=usd \  -d "cart[line_items][0][amount]"=5100 \  -d "cart[line_items][0][description]"="Red t-shirt" \  -d "cart[line_items][0][quantity]"=1 \  -d "cart[tax]"=100 \  -d "cart[total]"=5200`Response`{  "id": "tmr_FDOt2wlRZEdpd7",  "object": "terminal.reader",  "action": {    "failure_code": null,    "failure_message": null,    "set_reader_display": {      "cart": {        "currency": "usd",        "line_items": [          {            "amount": 5100,            "description": "Red t-shirt",            "quantity": 1          }        ],        "tax": 100,        "total": 5200      },      "type": "cart"    },    "status": "in_progress",    "type": "set_reader_display"  },  "device_sw_version": "",  "device_type": "simulated_wisepos_e",  "ip_address": "0.0.0.0",  "label": "Blue Rabbit",  "last_seen_at": 1695166525506,  "livemode": false,  "location": "tml_FDOtHwxAAdIJOh",  "metadata": {},  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",  "status": "online"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`