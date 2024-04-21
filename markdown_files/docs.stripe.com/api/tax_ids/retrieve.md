htmlRetrieve a tax ID | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Retrieve a tax ID

Retrieves an account or customer tax_id object.

### Parameters

No parameters.

### Returns

Returns a tax_id object if a valid identifier was provided.

GET/v1/tax_ids/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tax_ids/txi_1NuMB12eZvKYlo2CMecoWkZd \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "txi_1NuMB12eZvKYlo2CMecoWkZd",  "object": "tax_id",  "country": "DE",  "created": 123456789,  "customer": null,  "livemode": false,  "type": "eu_vat",  "value": "DE123456789",  "verification": null,  "owner": {    "type": "self",    "customer": null  }}`# List all Customer tax IDs

Returns a list of tax IDs for a customer.

### Parameters

No parameters.

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit tax IDs, starting after tax ID starting_after. Each entry in the array is a separate tax_id object. If no more tax IDs are available, the resulting array will be empty. Raises an error if the customer ID is invalid.

GET/v1/customers/:id/tax_idsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/customers/cus_NZKoSNZZ58qtO0/tax_ids \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/customers/cus_NZKoSNZZ58qtO0/tax_ids",  "has_more": false,  "data": [    {      "id": "txi_1MoC8zLkdIwHu7ixEhgWcHzJ",      "object": "tax_id",      "country": "DE",      "created": 1679431857,      "customer": "cus_NZKoSNZZ58qtO0",      "livemode": false,      "type": "eu_vat",      "value": "DE123456789",      "verification": {        "status": "pending",        "verified_address": null,        "verified_name": null      }    }    {...}    {...}  ],}`# List all tax IDs

Returns a list of tax IDs.

### Parameters

- ownerobjectThe account or customer the tax ID belongs to. Defaults to owner[type]=self.

Show child parameters

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit tax IDs, starting after tax ID starting_after. Each entry in the array is a separate tax_id object. If no more tax IDs are available, the resulting array will be empty.

GET/v1/tax_idsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/tax_ids \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/tax_ids",  "has_more": false,  "data": [    {      "id": "txi_1NuMB12eZvKYlo2CMecoWkZd",      "object": "tax_id",      "country": "DE",      "created": 123456789,      "customer": null,      "livemode": false,      "type": "eu_vat",      "value": "DE123456789",      "verification": null,      "owner": {        "type": "self",        "customer": null      }    }    {...}    {...}  ],}`# Delete a Customer tax ID

Deletes an existing tax_id object.

### Parameters

No parameters.

### Returns

Returns an object with a deleted parameter on success. If the tax_id object does not exist, this call raises an error.

DELETE/v1/customers/:id/tax_ids/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X DELETE https://api.stripe.com/v1/customers/cus_NZKoSNZZ58qtO0/tax_ids/txi_1MoC8zLkdIwHu7ixEhgWcHzJ \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "txi_1MoC8zLkdIwHu7ixEhgWcHzJ",  "object": "tax_id",  "deleted": true}`# Delete a tax ID

Deletes an existing account or customer tax_id object.

### Parameters

No parameters.

### Returns

Returns an object with a deleted parameter on success. If the tax_id object does not exist, this call raises an error.

DELETE/v1/tax_ids/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X DELETE https://api.stripe.com/v1/tax_ids/txi_1NuMB12eZvKYlo2CMecoWkZd \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "txi_1NuMB12eZvKYlo2CMecoWkZd",  "object": "tax_id",  "deleted": true}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`