htmlRetrieve a PaymentMethod | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Retrieve a PaymentMethod

Retrieves a PaymentMethod object attached to the StripeAccount. To retrieve a payment method attached to a Customer, you should use Retrieve a Customer’s PaymentMethods

### Parameters

No parameters.

### Returns

Returns a PaymentMethod object.

GET/v1/payment_methods/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_methods/pm_1MqLiJLkdIwHu7ixUEgbFdYF \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "pm_1MqLiJLkdIwHu7ixUEgbFdYF",  "object": "payment_method",  "billing_details": {    "address": {      "city": null,      "country": null,      "line1": null,      "line2": null,      "postal_code": null,      "state": null    },    "email": null,    "name": null,    "phone": null  },  "card": {    "brand": "visa",    "checks": {      "address_line1_check": null,      "address_postal_code_check": null,      "cvc_check": "unchecked"    },    "country": "US",    "exp_month": 8,    "exp_year": 2026,    "fingerprint": "mToisGZ01V71BCos",    "funding": "credit",    "generated_from": null,    "last4": "4242",    "networks": {      "available": [        "visa"      ],      "preferred": null    },    "three_d_secure_usage": {      "supported": true    },    "wallet": null  },  "created": 1679945299,  "customer": null,  "livemode": false,  "metadata": {},  "type": "card"}`# List a Customer's PaymentMethods

Returns a list of PaymentMethods for a given Customer

### Parameters

- typeenumAn optional filter on the list, based on the object type field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request.



### More parametersExpand all

- allow_redisplayenum
- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit PaymentMethods of type type, starting after PaymentMethods starting_after. Each entry in the array is a separate PaymentMethod object. If no more PaymentMethods are available, the resulting array will be empty.

GET/v1/customers/:id/payment_methodsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/payment_methods \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/customers/cus_9s6XKzkNRiz8i3/payment_methods",  "has_more": false,  "data": [    {      "id": "pm_1NVChw2eZvKYlo2CHxiM5E2E",      "object": "payment_method",      "billing_details": {        "address": {          "city": null,          "country": null,          "line1": null,          "line2": null,          "postal_code": null,          "state": null        },        "email": null,        "name": null,        "phone": null      },      "card": {        "brand": "visa",        "checks": {          "address_line1_check": null,          "address_postal_code_check": null,          "cvc_check": "pass"        },        "country": "US",        "exp_month": 12,        "exp_year": 2034,        "fingerprint": "Xt5EWLLDS7FJjR1c",        "funding": "credit",        "generated_from": null,        "last4": "4242",        "networks": {          "available": [            "visa"          ],          "preferred": null        },        "three_d_secure_usage": {          "supported": true        },        "wallet": null      },      "created": 1689682128,      "customer": "cus_9s6XKzkNRiz8i3",      "livemode": false,      "metadata": {},      "redaction": null,      "type": "card"    }    {...}    {...}  ],}`# List PaymentMethods

Returns a list of PaymentMethods for Treasury flows. If you want to list the PaymentMethods attached to a Customer for payments, you should use the List a Customer’s PaymentMethods API instead.

### Parameters

- typeenumAn optional filter on the list, based on the object type field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request.



### More parametersExpand all

- customerstring
- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit PaymentMethods of type type, starting after PaymentMethods starting_after. Each entry in the array is a separate PaymentMethod object. If no more PaymentMethods are available, the resulting array will be empty.

GET/v1/payment_methodsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/payment_methods \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d type=card \  -d limit=3 \  -d customer=cus_9s6XKzkNRiz8i3`Response`{  "object": "list",  "url": "/v1/payment_methods",  "has_more": false,  "data": [    {      "id": "pm_1NO6mA2eZvKYlo2CEydeHsKT",      "object": "payment_method",      "billing_details": {        "address": {          "city": null,          "country": null,          "line1": null,          "line2": null,          "postal_code": null,          "state": null        },        "email": null,        "name": null,        "phone": null      },      "card": {        "brand": "visa",        "checks": {          "address_line1_check": null,          "address_postal_code_check": null,          "cvc_check": "unchecked"        },        "country": "US",        "exp_month": 8,        "exp_year": 2024,        "fingerprint": "Xt5EWLLDS7FJjR1c",        "funding": "credit",        "generated_from": null,        "last4": "4242",        "networks": {          "available": [            "visa"          ],          "preferred": null        },        "three_d_secure_usage": {          "supported": true        },        "wallet": null      },      "created": 1687991030,      "customer": "cus_9s6XKzkNRiz8i3",      "livemode": false,      "metadata": {},      "type": "card"    }    {...}    {...}  ],}`# Attach a PaymentMethod to a Customer

Attaches a PaymentMethod object to a Customer.

To attach a new PaymentMethod to a customer for future payments, we recommend you use a SetupIntent or a PaymentIntent with setup_future_usage. These approaches will perform any necessary steps to set up the PaymentMethod for future payments. Using the /v1/payment_methods/:id/attach endpoint without first using a SetupIntent or PaymentIntent with setup_future_usage does not optimize the PaymentMethod for future use, which makes later declines and payment friction more likely. See Optimizing cards for future payments for more information about setting up future payments.

To use this PaymentMethod as the default for invoice or subscription payments, set invoice_settings.default_payment_method, on the Customer to the PaymentMethod’s ID.

### Parameters

- customerstringRequiredThe ID of the customer to which to attach the PaymentMethod.



### Returns

Returns a PaymentMethod object.

POST/v1/payment_methods/:id/attachServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_methods/pm_1MqM05LkdIwHu7ixlDxxO6Mc/attach \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d customer=cus_NbZ8Ki3f322LNn`Response`{  "id": "pm_1MqM05LkdIwHu7ixlDxxO6Mc",  "object": "payment_method",  "billing_details": {    "address": {      "city": null,      "country": null,      "line1": null,      "line2": null,      "postal_code": null,      "state": null    },    "email": null,    "name": null,    "phone": null  },  "card": {    "brand": "visa",    "checks": {      "address_line1_check": null,      "address_postal_code_check": null,      "cvc_check": "pass"    },    "country": "US",    "exp_month": 8,    "exp_year": 2026,    "fingerprint": "mToisGZ01V71BCos",    "funding": "credit",    "generated_from": null,    "last4": "4242",    "networks": {      "available": [        "visa"      ],      "preferred": null    },    "three_d_secure_usage": {      "supported": true    },    "wallet": null  },  "created": 1679946402,  "customer": "cus_NbZ8Ki3f322LNn",  "livemode": false,  "metadata": {},  "type": "card"}`# Detach a PaymentMethod from a Customer

Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.

### Parameters

No parameters.

### Returns

Returns a PaymentMethod object.

POST/v1/payment_methods/:id/detachServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/payment_methods/pm_1MqLiJLkdIwHu7ixUEgbFdYF/detach \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "pm_1MqLiJLkdIwHu7ixUEgbFdYF",  "object": "payment_method",  "billing_details": {    "address": {      "city": null,      "country": null,      "line1": null,      "line2": null,      "postal_code": null,      "state": null    },    "email": null,    "name": null,    "phone": null  },  "card": {    "brand": "visa",    "checks": {      "address_line1_check": null,      "address_postal_code_check": null,      "cvc_check": "unchecked"    },    "country": "US",    "exp_month": 8,    "exp_year": 2026,    "fingerprint": "mToisGZ01V71BCos",    "funding": "credit",    "generated_from": null,    "last4": "4242",    "networks": {      "available": [        "visa"      ],      "preferred": null    },    "three_d_secure_usage": {      "supported": true    },    "wallet": null  },  "created": 1679945299,  "customer": null,  "livemode": false,  "metadata": {},  "type": "card"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`