htmlTop-ups | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Top-ups

To top up your Stripe balance, you create a top-up object. You can retrieve individual top-ups, as well as list all top-ups. Top-ups are identified by a unique, random ID.

Related guide: Topping up your platform account

Endpoints
# The Top-up object

### Attributes

- idstringUnique identifier for the object.


- amountintegerAmount transferred.


- currencystringThree-letter ISO currency code, in lowercase. Must be a supported currency.


- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- statusenumThe status of the top-up is either canceled, failed, pending, reversed, or succeeded.

Possible enum values`canceled``failed``pending``reversed``succeeded`

### More attributesExpand all

- objectstring
- balance_transactionnullablestringExpandable
- createdtimestamp
- expected_availability_datenullableinteger
- failure_codenullablestring
- failure_messagenullablestring
- livemodeboolean
- sourcenullableobjectDeprecated
- statement_descriptornullablestring
- transfer_groupnullablestring

The Top-up object`{  "id": "tu_1NG6yj2eZvKYlo2C1FOBiHya",  "object": "topup",  "amount": 2000,  "balance_transaction": null,  "created": 123456789,  "currency": "usd",  "description": "Top-up for Jenny Rosen",  "expected_availability_date": 123456789,  "failure_code": null,  "failure_message": null,  "livemode": false,  "source": null,  "statement_descriptor": "Top-up",  "status": "pending",  "transfer_group": null}`# Create a top-up

Top up the balance of an account

### Parameters

- amountintegerRequiredA positive integer representing how much to transfer.


- currencystringRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.


- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- sourcestring
- statement_descriptorstring
- transfer_groupstring

### Returns

Returns the top-up object.

POST/v1/topupsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/topups \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d amount=2000 \  -d currency=usd \  -d description="Top-up for Jenny Rosen" \  -d statement_descriptor=Top-up`Response`{  "id": "tu_1NG6yj2eZvKYlo2C1FOBiHya",  "object": "topup",  "amount": 2000,  "balance_transaction": null,  "created": 123456789,  "currency": "usd",  "description": "Top-up for Jenny Rosen",  "expected_availability_date": 123456789,  "failure_code": null,  "failure_message": null,  "livemode": false,  "source": null,  "statement_descriptor": "Top-up",  "status": "pending",  "transfer_group": null}`# Update a top-up

Updates the metadata of a top-up. Other top-up details are not editable by design.

### Parameters

- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

The newly updated top-up object if the call succeeded. Otherwise, this call raises an error.

POST/v1/topups/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/topups/tu_1NG6yj2eZvKYlo2C1FOBiHya \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "tu_1NG6yj2eZvKYlo2C1FOBiHya",  "object": "topup",  "amount": 2000,  "balance_transaction": null,  "created": 123456789,  "currency": "usd",  "description": "Top-up for Jenny Rosen",  "expected_availability_date": 123456789,  "failure_code": null,  "failure_message": null,  "livemode": false,  "source": null,  "statement_descriptor": "Top-up",  "status": "pending",  "transfer_group": null,  "metadata": {    "order_id": "6735"  }}`# Retrieve a top-up

Retrieves the details of a top-up that has previously been created. Supply the unique top-up ID that was returned from your previous request, and Stripe will return the corresponding top-up information.

### Parameters

No parameters.

### Returns

Returns a top-up if a valid identifier was provided, and raises an error otherwise.

GET/v1/topups/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/topups/tu_1NG6yj2eZvKYlo2C1FOBiHya \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "tu_1NG6yj2eZvKYlo2C1FOBiHya",  "object": "topup",  "amount": 2000,  "balance_transaction": null,  "created": 123456789,  "currency": "usd",  "description": "Top-up for Jenny Rosen",  "expected_availability_date": 123456789,  "failure_code": null,  "failure_message": null,  "livemode": false,  "source": null,  "statement_descriptor": "Top-up",  "status": "pending",  "transfer_group": null}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`