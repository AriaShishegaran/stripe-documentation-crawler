htmlCustomers | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Customers

This object represents a customer of your business. Use it to create recurring charges and track payments that belong to the same customer.

Related guide: Save a card during payment

Endpoints
# The Customer object

### Attributes

- idstringUnique identifier for the object.


- addressnullableobjectThe customer’s address.

Show child attributes
- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users.


- emailnullablestringThe customer’s email address.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- namenullablestringThe customer’s full name or business name.


- phonenullablestringThe customer’s phone number.


- shippingnullableobjectMailing and shipping address for the customer. Appears on invoices emailed to this customer.

Show child attributes

### More attributesExpand all

- objectstring
- balanceinteger
- cash_balancenullableobjectExpandable
- createdtimestamp
- currencynullablestring
- default_sourcenullablestringExpandable
- delinquentnullableboolean
- discountnullableobject
- invoice_credit_balanceobjectExpandable
- invoice_prefixnullablestring
- invoice_settingsobject
- livemodeboolean
- next_invoice_sequencenullableinteger
- preferred_localesnullablearray of strings
- sourcesnullableobjectExpandable
- subscriptionsnullableobjectExpandable
- taxobjectExpandable
- tax_exemptnullableenum
- tax_idsnullableobjectExpandable
- test_clocknullablestringExpandable

The Customer object`{  "id": "cus_NffrFeUfNV2Hib",  "object": "customer",  "address": null,  "balance": 0,  "created": 1680893993,  "currency": null,  "default_source": null,  "delinquent": false,  "description": null,  "discount": null,  "email": "jennyrosen@example.com",  "invoice_prefix": "0759376C",  "invoice_settings": {    "custom_fields": null,    "default_payment_method": null,    "footer": null,    "rendering_options": null  },  "livemode": false,  "metadata": {},  "name": "Jenny Rosen",  "next_invoice_sequence": 1,  "phone": null,  "preferred_locales": [],  "shipping": null,  "tax_exempt": "none",  "test_clock": null}`# Create a customer

### Parameters

- addressobjectThe customer’s address.

Show child parameters
- descriptionstringAn arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard.


- emailstringCustomer’s email address. It’s displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to 512 characters.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- namestringThe customer’s full name or business name.


- payment_methodstringThe ID of the PaymentMethod to attach to the customer.


- phonestringThe customer’s phone number.


- shippingobjectThe customer’s shipping information. Appears on invoices emailed to this customer.

Show child parameters

### More parametersExpand all

- balanceinteger
- cash_balanceobject
- couponstring
- invoice_prefixstring
- invoice_settingsobject
- next_invoice_sequenceinteger
- preferred_localesarray of strings
- promotion_codestring
- sourcestring
- taxobject
- tax_exemptenum
- tax_id_dataarray of objects
- test_clockstring

### Returns

Returns the Customer object after successful customer creation. Raises an error if create parameters are invalid (for example, specifying an invalid coupon or an invalid source).

POST/v1/customersServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/customers \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d name="Jenny Rosen" \  --data-urlencode email="jennyrosen@example.com"`Response`{  "id": "cus_NffrFeUfNV2Hib",  "object": "customer",  "address": null,  "balance": 0,  "created": 1680893993,  "currency": null,  "default_source": null,  "delinquent": false,  "description": null,  "discount": null,  "email": "jennyrosen@example.com",  "invoice_prefix": "0759376C",  "invoice_settings": {    "custom_fields": null,    "default_payment_method": null,    "footer": null,    "rendering_options": null  },  "livemode": false,  "metadata": {},  "name": "Jenny Rosen",  "next_invoice_sequence": 1,  "phone": null,  "preferred_locales": [],  "shipping": null,  "tax_exempt": "none",  "test_clock": null}`# Update a customer

Updates the specified customer by setting the values of the parameters passed. Any parameters not provided will be left unchanged.  For example, if you pass the source parameter, that becomes the customer’s active source (e.g., a card) to be used for all charges in the future. When you update a customer to a new valid card source by passing the source parameter: for each of the customer’s current subscriptions, if the subscription bills automatically and is in the past_due state, then the latest open invoice for the subscription with automatic collection enabled will be retried. This retry will not count as an automatic retry, and will not affect the next regularly scheduled payment for the invoice. Changing the default_source for a customer will not trigger this behavior.

This request accepts mostly the same arguments as the customer creation call.

### Parameters

- addressobjectThe customer’s address.

Show child parameters
- descriptionstringAn arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard.


- emailstringCustomer’s email address. It’s displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to 512 characters.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- namestringThe customer’s full name or business name.


- phonestringThe customer’s phone number.


- shippingobjectThe customer’s shipping information. Appears on invoices emailed to this customer.

Show child parameters

### More parametersExpand all

- balanceinteger
- cash_balanceobject
- couponstring
- default_sourcestring
- invoice_prefixstring
- invoice_settingsobject
- next_invoice_sequenceinteger
- preferred_localesarray of strings
- promotion_codestring
- sourcestring
- taxobject
- tax_exemptenum

### Returns

Returns the customer object if the update succeeded. Raises an error if update parameters are invalid (e.g. specifying an invalid coupon or an invalid source).

POST/v1/customers/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/customers/cus_NffrFeUfNV2Hib \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "cus_NffrFeUfNV2Hib",  "object": "customer",  "address": null,  "balance": 0,  "created": 1680893993,  "currency": null,  "default_source": null,  "delinquent": false,  "description": null,  "discount": null,  "email": "jennyrosen@example.com",  "invoice_prefix": "0759376C",  "invoice_settings": {    "custom_fields": null,    "default_payment_method": null,    "footer": null,    "rendering_options": null  },  "livemode": false,  "metadata": {    "order_id": "6735"  },  "name": "Jenny Rosen",  "next_invoice_sequence": 1,  "phone": null,  "preferred_locales": [],  "shipping": null,  "tax_exempt": "none",  "test_clock": null}`# Retrieve a customer

Retrieves a Customer object.

### Parameters

No parameters.

### Returns

Returns the Customer object for a valid identifier. If it’s for a deleted Customer, a subset of the customer’s information is returned, including a deleted property that’s set to true.

GET/v1/customers/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/customers/cus_NffrFeUfNV2Hib \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "cus_NffrFeUfNV2Hib",  "object": "customer",  "address": null,  "balance": 0,  "created": 1680893993,  "currency": null,  "default_source": null,  "delinquent": false,  "description": null,  "discount": null,  "email": "jennyrosen@example.com",  "invoice_prefix": "0759376C",  "invoice_settings": {    "custom_fields": null,    "default_payment_method": null,    "footer": null,    "rendering_options": null  },  "livemode": false,  "metadata": {},  "name": "Jenny Rosen",  "next_invoice_sequence": 1,  "phone": null,  "preferred_locales": [],  "shipping": null,  "tax_exempt": "none",  "test_clock": null}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`