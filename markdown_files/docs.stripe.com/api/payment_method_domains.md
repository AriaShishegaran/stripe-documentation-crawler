htmlPayment Method Domains | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Payment Method Domains

A payment method domain represents a web domain that you have registered with Stripe. Stripe Elements use registered payment method domains to control where certain payment methods are shown.

Related guides: Payment method domains.

Endpoints
# The PaymentMethodDomain object

### Attributes

- idstringUnique identifier for the object.


- domain_namestringThe domain name that this payment method domain object represents.


- enabledbooleanWhether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements.



### More attributesExpand all

- objectstring
- apple_payobject
- createdtimestamp
- google_payobject
- linkobject
- livemodeboolean
- paypalobject

The PaymentMethodDomain object`{  "id": "pmd_1Nnrer2eZvKYlo2Cips79tWl",  "object": "payment_method_domain",  "apple_pay": {    "status": "active"  },  "created": 1694129445,  "domain_name": "example.com",  "enabled": true,  "google_pay": {    "status": "active"  },  "link": {    "status": "active"  },  "livemode": false,  "paypal": {    "status": "active"  }}`# Create a payment method domain

Creates a payment method domain.

### Parameters

- domain_namestringRequiredThe domain name that this payment method domain object represents.


- enabledbooleanWhether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements.



### Returns

Returns a payment method domain object.

POST/v1/payment_method_domainsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_method_domains \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d domain_name="example.com"`Response`{  "id": "pmd_1Nnrer2eZvKYlo2Cips79tWl",  "object": "payment_method_domain",  "apple_pay": {    "status": "active"  },  "created": 1694129445,  "domain_name": "example.com",  "enabled": true,  "google_pay": {    "status": "active"  },  "link": {    "status": "active"  },  "livemode": false,  "paypal": {    "status": "active"  }}`# Update a payment method domain

Updates an existing payment method domain.

### Parameters

- enabledbooleanWhether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements.



### Returns

Returns the updated payment method domain object.

POST/v1/payment_method_domains/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_method_domains/pmd_1Nnrer2eZvKYlo2Cips79tWl \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d enabled=false`Response`{  "id": "pmd_1Nnrer2eZvKYlo2Cips79tWl",  "object": "payment_method_domain",  "apple_pay": {    "status": "active"  },  "created": 1694129445,  "domain_name": "example.com",  "enabled": false,  "google_pay": {    "status": "active"  },  "link": {    "status": "active"  },  "livemode": false,  "paypal": {    "status": "active"  }}`# Retrieve a payment method domain

Retrieves the details of an existing payment method domain.

### Parameters

No parameters.

### Returns

Returns a payment method domain object.

GET/v1/payment_method_domains/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_method_domains/pmd_1Nnrer2eZvKYlo2Cips79tWl \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "pmd_1Nnrer2eZvKYlo2Cips79tWl",  "object": "payment_method_domain",  "apple_pay": {    "status": "active"  },  "created": 1694129445,  "domain_name": "example.com",  "enabled": true,  "google_pay": {    "status": "active"  },  "link": {    "status": "active"  },  "livemode": false,  "paypal": {    "status": "active"  }}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`