htmlThe Source object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The Source objectDeprecated

### Attributes

- idstringUnique identifier for the object.


- amountnullableintegerA positive integer in the smallest currency unit (that is, 100 cents for $1.00, or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for single_use sources.


- currencynullableenumThree-letter ISO code for the currency associated with the source. This is the currency for which the source will be chargeable once ready. Required for single_use sources.


- customernullablestringThe ID of the customer to which this source is attached. This will not be present when the source has not been attached to a customer.


- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- ownernullableobjectInformation about the owner of the payment instrument that may be used or required by particular source types.

Show child attributes
- redirectnullableobjectInformation related to the redirect flow. Present if the source is authenticated by a redirect (flow is redirect).

Show child attributes
- statement_descriptornullablestringExtra information about a source. This will appear on your customer’s statement every time you charge the source.


- statusstringThe status of the source, one of canceled, chargeable, consumed, failed, or pending. Only chargeable sources can be used to create a charge.


- typeenumThe type of the source. The type is a payment method, one of ach_credit_transfer, ach_debit, alipay, bancontact, card, card_present, eps, giropay, ideal, multibanco, klarna, p24, sepa_debit, sofort, three_d_secure, or wechat. An additional hash is included on the source with a name matching this value. It contains additional information specific to the payment method used.

Possible enum values`ach_credit_transfer``ach_debit``alipay``bancontact``card``card_present``eps``giropay``ideal``klarna`[Show 6 more](#)

### More attributesExpand all

- objectstring
- client_secretstring
- code_verificationnullableobject
- createdtimestamp
- flowstring
- livemodeboolean
- receivernullableobject
- source_ordernullableobject
- usagenullablestring

The Source object`{  "id": "src_1N3lxdLkdIwHu7ixPHXy8UcI",  "object": "source",  "ach_credit_transfer": {    "account_number": "test_eb829353ed79",    "bank_name": "TEST BANK",    "fingerprint": "kBQsBk9KtfCgjEYK",    "refund_account_holder_name": null,    "refund_account_holder_type": null,    "refund_routing_number": null,    "routing_number": "110000000",    "swift_code": "TSTEZ122"  },  "amount": null,  "client_secret": "src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr",  "created": 1683144457,  "currency": "usd",  "flow": "receiver",  "livemode": false,  "metadata": {},  "owner": {    "address": null,    "email": "jenny.rosen@example.com",    "name": null,    "phone": null,    "verified_address": null,    "verified_email": null,    "verified_name": null,    "verified_phone": null  },  "receiver": {    "address": "110000000-test_eb829353ed79",    "amount_charged": 0,    "amount_received": 0,    "amount_returned": 0,    "refund_attributes_method": "email",    "refund_attributes_status": "missing"  },  "statement_descriptor": null,  "status": "pending",  "type": "ach_credit_transfer",  "usage": "reusable"}`# Create a source

Creates a new source object.

### Parameters

- typestringRequiredThe type of the source to create. Required unless customer and original_source are specified (see the Cloning card Sources guide)


- amountintegerAmount associated with the source. This is the amount for which the source will be chargeable once ready. Required for single_use sources. Not supported for receiver type sources, where charge amount may not be specified until funds land.


- currencyenumThree-letter ISO code for the currency associated with the source. This is the currency for which the source will be chargeable once ready.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- ownerobjectInformation about the owner of the payment instrument that may be used or required by particular source types.

Show child parameters
- redirectobjectParameters required for the redirect flow. Required if the source is authenticated by a redirect (flow is redirect).

Show child parameters
- statement_descriptorstringAn arbitrary string to be displayed on your customer’s statement. As an example, if your website is RunClub and the item you’re charging for is a race ticket, you may want to specify a statement_descriptor of RunClub 5K race ticket. While many payment types will display this information, some may not display it at all.



### More parametersExpand all

- flowstring
- mandateobject
- receiverobject
- source_orderobject
- tokenstring
- usagestring

### Returns

Returns a newly created source.

POST/v1/sourcesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/sources \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d type=ach_credit_transfer \  -d currency=usd \  --data-urlencode "owner[email]"="jenny.rosen@example.com"`Response`{  "id": "src_1N3lxdLkdIwHu7ixPHXy8UcI",  "object": "source",  "ach_credit_transfer": {    "account_number": "test_eb829353ed79",    "bank_name": "TEST BANK",    "fingerprint": "kBQsBk9KtfCgjEYK",    "refund_account_holder_name": null,    "refund_account_holder_type": null,    "refund_routing_number": null,    "routing_number": "110000000",    "swift_code": "TSTEZ122"  },  "amount": null,  "client_secret": "src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr",  "created": 1683144457,  "currency": "usd",  "flow": "receiver",  "livemode": false,  "metadata": {},  "owner": {    "address": null,    "email": "jenny.rosen@example.com",    "name": null,    "phone": null,    "verified_address": null,    "verified_email": null,    "verified_name": null,    "verified_phone": null  },  "receiver": {    "address": "110000000-test_eb829353ed79",    "amount_charged": 0,    "amount_received": 0,    "amount_returned": 0,    "refund_attributes_method": "email",    "refund_attributes_status": "missing"  },  "statement_descriptor": null,  "status": "pending",  "type": "ach_credit_transfer",  "usage": "reusable"}`# Update a source

Updates the specified source by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

This request accepts the metadata and owner as arguments. It is also possible to update type specific information for selected payment methods. Please refer to our payment method guides for more detail.

### Parameters

- amountintegerAmount associated with the source.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- ownerobjectInformation about the owner of the payment instrument that may be used or required by particular source types.

Show child parameters

### More parametersExpand all

- mandateobject
- source_orderobject

### Returns

Returns the source object if the update succeeded. This call will raise an error if update parameters are invalid.

POST/v1/sources/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/sources/src_1N3lxdLkdIwHu7ixPHXy8UcI \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "src_1N3lxdLkdIwHu7ixPHXy8UcI",  "object": "source",  "ach_credit_transfer": {    "account_number": "test_eb829353ed79",    "bank_name": "TEST BANK",    "fingerprint": "kBQsBk9KtfCgjEYK",    "refund_account_holder_name": null,    "refund_account_holder_type": null,    "refund_routing_number": null,    "routing_number": "110000000",    "swift_code": "TSTEZ122"  },  "amount": null,  "client_secret": "src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr",  "created": 1683144457,  "currency": "usd",  "flow": "receiver",  "livemode": false,  "metadata": {    "order_id": "6735"  },  "owner": {    "address": null,    "email": "jenny.rosen@example.com",    "name": null,    "phone": null,    "verified_address": null,    "verified_email": null,    "verified_name": null,    "verified_phone": null  },  "receiver": {    "address": "110000000-test_eb829353ed79",    "amount_charged": 0,    "amount_received": 0,    "amount_returned": 0,    "refund_attributes_method": "email",    "refund_attributes_status": "missing"  },  "statement_descriptor": null,  "status": "pending",  "type": "ach_credit_transfer",  "usage": "reusable"}`# Retrieve a source

Retrieves an existing source object. Supply the unique source ID from a source creation request and Stripe will return the corresponding up-to-date source object information.

### Parameters

No parameters.

### More parametersExpand all

- client_secretstring

### Returns

Returns a source if a valid identifier was provided.

GET/v1/sources/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/sources/src_1N3lxdLkdIwHu7ixPHXy8UcI \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "src_1N3lxdLkdIwHu7ixPHXy8UcI",  "object": "source",  "ach_credit_transfer": {    "account_number": "test_eb829353ed79",    "bank_name": "TEST BANK",    "fingerprint": "kBQsBk9KtfCgjEYK",    "refund_account_holder_name": null,    "refund_account_holder_type": null,    "refund_routing_number": null,    "routing_number": "110000000",    "swift_code": "TSTEZ122"  },  "amount": null,  "client_secret": "src_client_secret_ZaOIRUD8a9uGmQobLxGvqKSr",  "created": 1683144457,  "currency": "usd",  "flow": "receiver",  "livemode": false,  "metadata": {},  "owner": {    "address": null,    "email": "jenny.rosen@example.com",    "name": null,    "phone": null,    "verified_address": null,    "verified_email": null,    "verified_name": null,    "verified_phone": null  },  "receiver": {    "address": "110000000-test_eb829353ed79",    "amount_charged": 0,    "amount_received": 0,    "amount_returned": 0,    "refund_attributes_method": "email",    "refund_attributes_status": "missing"  },  "statement_descriptor": null,  "status": "pending",  "type": "ach_credit_transfer",  "usage": "reusable"}`# Attach a source

Attaches a Source object to a Customer. The source must be in a chargeable or pending state.

### Parameters

- sourcestringRequiredThe identifier of the source to be attached.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns the attached Source object.

POST/v1/customers/:id/sourcesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/sources \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d source=src_1NfRGv2eZvKYlo2Cv7NAImBL`Response`{  "id": "src_1NfRGv2eZvKYlo2Cv7NAImBL",  "object": "source",  "ach_credit_transfer": {    "account_number": "test_52796e3294dc",    "routing_number": "110000000",    "fingerprint": "ecpwEzmBOSMOqQTL",    "bank_name": "TEST BANK",    "swift_code": "TSTEZ122"  },  "amount": 1000,  "client_secret": "src_client_secret_sBqfX18eq6GPfGxGvVfMByCp",  "created": 1692121393,  "currency": "usd",  "customer": "cus_9s6XKzkNRiz8i3",  "flow": "receiver",  "livemode": false,  "metadata": {},  "owner": {    "address": null,    "email": "jenny.rosen@example.com",    "name": null,    "phone": null,    "verified_address": null,    "verified_email": null,    "verified_name": null,    "verified_phone": null  },  "receiver": {    "address": "121042882-38381234567890123",    "amount_received": 1000,    "amount_charged": 0,    "amount_returned": 0,    "refund_attributes_status": "missing",    "refund_attributes_method": "email"  },  "redaction": null,  "statement_descriptor": null,  "status": "chargeable",  "type": "ach_credit_transfer",  "usage": "reusable"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`