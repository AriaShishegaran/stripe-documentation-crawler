htmlThe PaymentMethod object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The PaymentMethod object

### Attributes

- idstringUnique identifier for the object.


- billing_detailsobjectBilling information associated with the PaymentMethod that may be used or required by particular types of payment methods.

Show child attributes
- customernullablestringExpandableThe ID of the Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer.


- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- typeenumThe type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.

Possible enum values`acss_debit`Pre-authorized debit payments are used to debit Canadian bank accounts through the Automated Clearing Settlement System (ACSS).

`affirm`Affirm is a buy now, pay later payment method in the US.

`afterpay_clearpay`Afterpay / Clearpay is a buy now, pay later payment method used in Australia, Canada, France, New Zealand, Spain, the UK, and the US.

`alipay`Alipay is a digital wallet payment method used in China.

`amazon_pay`Amazon Pay is a Wallet payment method that lets hundreds of millions of Amazon customers pay their way, every day.

`au_becs_debit`BECS Direct Debit is used to debit Australian bank accounts through the Bulk Electronic Clearing System (BECS).

`bacs_debit`Bacs Direct Debit is used to debit UK bank accounts.

`bancontact`Bancontact is a bank redirect payment method used in Belgium.

`blik`BLIK is a single-use payment method common in Poland.

`boleto`Boleto is a voucher-based payment method used in Brazil.

[Show 56 more](#)

### More attributesExpand all

- objectstring
- acss_debitnullableobject
- affirmnullableobject
- afterpay_clearpaynullableobject
- alipaynullableobject
- allow_redisplaynullableenumPreview feature
- amazon_paynullableobject
- au_becs_debitnullableobject
- bacs_debitnullableobject
- bancontactnullableobject
- bliknullableobject
- boletonullableobject
- cardnullableobject
- card_presentnullableobject
- cashappnullableobject
- createdtimestamp
- customer_balancenullableobject
- epsnullableobject
- fpxnullableobject
- giropaynullableobject
- grabpaynullableobject
- idealnullableobject
- interac_presentnullableobjectPreview feature
- klarnanullableobject
- konbininullableobject
- linknullableobject
- livemodeboolean
- mobilepaynullableobjectPreview feature
- oxxonullableobject
- p24nullableobject
- paynownullableobject
- paypalnullableobject
- pixnullableobject
- promptpaynullableobject
- radar_optionsnullableobject
- revolut_paynullableobject
- sepa_debitnullableobject
- sofortnullableobject
- swishnullableobject
- us_bank_accountnullableobject
- wechat_paynullableobject
- zipnullableobject

The PaymentMethod object`{  "id": "pm_1MqLiJLkdIwHu7ixUEgbFdYF",  "object": "payment_method",  "billing_details": {    "address": {      "city": null,      "country": null,      "line1": null,      "line2": null,      "postal_code": null,      "state": null    },    "email": null,    "name": null,    "phone": null  },  "card": {    "brand": "visa",    "checks": {      "address_line1_check": null,      "address_postal_code_check": null,      "cvc_check": "unchecked"    },    "country": "US",    "exp_month": 8,    "exp_year": 2026,    "fingerprint": "mToisGZ01V71BCos",    "funding": "credit",    "generated_from": null,    "last4": "4242",    "networks": {      "available": [        "visa"      ],      "preferred": null    },    "three_d_secure_usage": {      "supported": true    },    "wallet": null  },  "created": 1679945299,  "customer": null,  "livemode": false,  "metadata": {},  "type": "card"}`# Create a PaymentMethod

Creates a PaymentMethod object. Read the Stripe.js reference to learn how to create PaymentMethods via Stripe.js.

Instead of creating a PaymentMethod directly, we recommend using the PaymentIntents API to accept a payment immediately or the SetupIntent API to collect payment method details ahead of a future payment.

### Parameters

- typeenumRequiredThe type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.

Possible enum values`acss_debit`Pre-authorized debit payments are used to debit Canadian bank accounts through the Automated Clearing Settlement System (ACSS).

`affirm`Affirm is a buy now, pay later payment method in the US.

`afterpay_clearpay`Afterpay / Clearpay is a buy now, pay later payment method used in Australia, Canada, France, New Zealand, Spain, the UK, and the US.

`alipay`Alipay is a digital wallet payment method used in China.

`amazon_pay`Amazon Pay is a Wallet payment method that lets hundreds of millions of Amazon customers pay their way, every day.

`au_becs_debit`BECS Direct Debit is used to debit Australian bank accounts through the Bulk Electronic Clearing System (BECS).

`bacs_debit`Bacs Direct Debit is used to debit UK bank accounts.

`bancontact`Bancontact is a bank redirect payment method used in Belgium.

`blik`BLIK is a single-use payment method common in Poland.

`boleto`Boleto is a voucher-based payment method used in Brazil.

[Show 55 more](#)
- billing_detailsobjectBilling information associated with the PaymentMethod that may be used or required by particular types of payment methods.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- acss_debitobject
- affirmobject
- afterpay_clearpayobject
- alipayobject
- allow_redisplayenum
- amazon_payobject
- au_becs_debitobject
- bacs_debitobject
- bancontactobject
- blikobject
- boletoobject
- cardobject
- cashappobject
- customer_balanceobject
- epsobject
- fpxobject
- giropayobject
- grabpayobject
- idealobject
- interac_presentobjectPreview feature
- klarnaobject
- konbiniobject
- linkobject
- mobilepayobjectPreview feature
- oxxoobject
- p24object
- paynowobject
- paypalobject
- pixobject
- promptpayobject
- radar_optionsobject
- revolut_payobject
- sepa_debitobject
- sofortobject
- swishobject
- us_bank_accountobject
- wechat_payobject
- zipobject

### Returns

Returns a PaymentMethod object.

POST/v1/payment_methodsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_methods \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d type=card \  -d "card[number]"=4242424242424242 \  -d "card[exp_month]"=8 \  -d "card[exp_year]"=2026 \  -d "card[cvc]"=314`Response`{  "id": "pm_1MqLiJLkdIwHu7ixUEgbFdYF",  "object": "payment_method",  "billing_details": {    "address": {      "city": null,      "country": null,      "line1": null,      "line2": null,      "postal_code": null,      "state": null    },    "email": null,    "name": null,    "phone": null  },  "card": {    "brand": "visa",    "checks": {      "address_line1_check": null,      "address_postal_code_check": null,      "cvc_check": "unchecked"    },    "country": "US",    "exp_month": 8,    "exp_year": 2026,    "fingerprint": "mToisGZ01V71BCos",    "funding": "credit",    "generated_from": null,    "last4": "4242",    "networks": {      "available": [        "visa"      ],      "preferred": null    },    "three_d_secure_usage": {      "supported": true    },    "wallet": null  },  "created": 1679945299,  "customer": null,  "livemode": false,  "metadata": {},  "type": "card"}`# Update a PaymentMethod

Updates a PaymentMethod object. A PaymentMethod must be attached a customer to be updated.

### Parameters

- billing_detailsobjectBilling information associated with the PaymentMethod that may be used or required by particular types of payment methods.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- allow_redisplayenum
- cardobject
- linkobject
- us_bank_accountobject

### Returns

Returns a PaymentMethod object.

POST/v1/payment_methods/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_methods/pm_1MqLiJLkdIwHu7ixUEgbFdYF \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "pm_1MqLiJLkdIwHu7ixUEgbFdYF",  "object": "payment_method",  "billing_details": {    "address": {      "city": null,      "country": null,      "line1": null,      "line2": null,      "postal_code": null,      "state": null    },    "email": null,    "name": null,    "phone": null  },  "card": {    "brand": "visa",    "checks": {      "address_line1_check": null,      "address_postal_code_check": null,      "cvc_check": "unchecked"    },    "country": "US",    "exp_month": 8,    "exp_year": 2026,    "fingerprint": "mToisGZ01V71BCos",    "funding": "credit",    "generated_from": null,    "last4": "4242",    "networks": {      "available": [        "visa"      ],      "preferred": null    },    "three_d_secure_usage": {      "supported": true    },    "wallet": null  },  "created": 1679945299,  "customer": null,  "livemode": false,  "metadata": {    "order_id": "6735"  },  "type": "card"}`# Retrieve a Customer's PaymentMethod

Retrieves a PaymentMethod object for a given Customer.

### Parameters

No parameters.

### Returns

Returns a PaymentMethod object.

GET/v1/customers/:id/payment_methods/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/payment_methods/pm_1NVChw2eZvKYlo2CHxiM5E2E \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "pm_1NVChw2eZvKYlo2CHxiM5E2E",  "object": "payment_method",  "billing_details": {    "address": {      "city": null,      "country": null,      "line1": null,      "line2": null,      "postal_code": null,      "state": null    },    "email": null,    "name": null,    "phone": null  },  "card": {    "brand": "visa",    "checks": {      "address_line1_check": null,      "address_postal_code_check": null,      "cvc_check": "pass"    },    "country": "US",    "exp_month": 12,    "exp_year": 2034,    "fingerprint": "Xt5EWLLDS7FJjR1c",    "funding": "credit",    "generated_from": null,    "last4": "4242",    "networks": {      "available": [        "visa"      ],      "preferred": null    },    "three_d_secure_usage": {      "supported": true    },    "wallet": null  },  "created": 1689682128,  "customer": "cus_9s6XKzkNRiz8i3",  "livemode": false,  "metadata": {},  "redaction": null,  "type": "card"}`# Retrieve a PaymentMethod

Retrieves a PaymentMethod object attached to the StripeAccount. To retrieve a payment method attached to a Customer, you should use Retrieve a Customer’s PaymentMethods

### Parameters

No parameters.

### Returns

Returns a PaymentMethod object.

GET/v1/payment_methods/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_methods/pm_1MqLiJLkdIwHu7ixUEgbFdYF \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "pm_1MqLiJLkdIwHu7ixUEgbFdYF",  "object": "payment_method",  "billing_details": {    "address": {      "city": null,      "country": null,      "line1": null,      "line2": null,      "postal_code": null,      "state": null    },    "email": null,    "name": null,    "phone": null  },  "card": {    "brand": "visa",    "checks": {      "address_line1_check": null,      "address_postal_code_check": null,      "cvc_check": "unchecked"    },    "country": "US",    "exp_month": 8,    "exp_year": 2026,    "fingerprint": "mToisGZ01V71BCos",    "funding": "credit",    "generated_from": null,    "last4": "4242",    "networks": {      "available": [        "visa"      ],      "preferred": null    },    "three_d_secure_usage": {      "supported": true    },    "wallet": null  },  "created": 1679945299,  "customer": null,  "livemode": false,  "metadata": {},  "type": "card"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`