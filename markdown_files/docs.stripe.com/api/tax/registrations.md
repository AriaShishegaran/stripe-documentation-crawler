htmlTax Registrations | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Tax Registrations

A Tax Registration lets us know that your business is registered to collect tax on payments within a region, enabling you to automatically collect tax.

Stripe doesn’t register on your behalf with the relevant authorities when you create a Tax Registration object. For more information on how to register to collect tax, see our guide.

Related guide: Using the Registrations API

Endpoints
# The Tax Registration object

### Attributes

- idstringUnique identifier for the object.


- objectstringString representing the object’s type. Objects of the same type share the same value.


- active_fromtimestampTime at which the registration becomes active. Measured in seconds since the Unix epoch.


- countrystringTwo-letter country code (ISO 3166-1 alpha-2).


- country_optionsobjectSpecific options for a registration in the specified country.

Show child attributes
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.


- expires_atnullabletimestampIf set, the registration stops being active at this time. If not set, the registration will be active indefinitely. Measured in seconds since the Unix epoch.


- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.


- statusenumThe status of the registration. This field is present for convenience and can be deduced from active_from and expires_at.

Possible enum values`active`The Tax Registration is currently active.

`expired`The Tax Registration is no longer active.

`scheduled`The Tax Registration will become active in the future.



The Tax Registration object`{  "id": "taxreg_NkyGPRPytKq66j",  "object": "tax.registration",  "active_from": 1682036640,  "country": "US",  "country_options": {    "us": {      "state": "CA",      "type": "state_sales_tax"    }  },  "created": 1682006400,  "expires_at": null,  "livemode": false,  "status": "active",  "state": "CA",  "type": "standard"}`# Create a registration

Creates a new Tax Registration object.

### Parameters

- active_fromstring | timestampRequiredTime at which the Tax Registration becomes active. It can be either now to indicate the current time, or a future timestamp measured in seconds since the Unix epoch.


- countrystringRequiredTwo-letter country code (ISO 3166-1 alpha-2).


- country_optionsobjectRequiredSpecific options for a registration in the specified country.

Show child parameters
- expires_attimestampIf set, the Tax Registration stops being active at this time. If not set, the Tax Registration will be active indefinitely. Timestamp measured in seconds since the Unix epoch.



### Returns

A Tax Registration object.

POST/v1/tax/registrationsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tax/registrations \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d country=US \  -d "country_options[us][state]"=CA \  -d "country_options[us][type]"=state_sales_tax \  -d active_from=now`Response`{  "id": "taxreg_NkyGPRPytKq66j",  "object": "tax.registration",  "active_from": 1682036640,  "country": "US",  "country_options": {    "us": {      "state": "CA",      "type": "state_sales_tax"    }  },  "created": 1682006400,  "expires_at": null,  "livemode": false,  "status": "active",  "state": "CA",  "type": "standard"}`# Update a registration

Updates an existing Tax Registration object.

A registration cannot be deleted after it has been created. If you wish to end a registration you may do so by setting expires_at.

### Parameters

- active_fromstring | timestampTime at which the registration becomes active. It can be either now to indicate the current time, or a timestamp measured in seconds since the Unix epoch.


- expires_atstring | timestampIf set, the registration stops being active at this time. If not set, the registration will be active indefinitely. It can be either now to indicate the current time, or a timestamp measured in seconds since the Unix epoch.



### Returns

A Tax Registration object.

POST/v1/tax/registrations/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tax/registrations/taxreg_NkyGPRPytKq66j \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d expires_at=now`Response`{  "id": "taxreg_NkyGPRPytKq66j",  "object": "tax.registration",  "active_from": 1683036640,  "country": "US",  "country_options": {    "us": {      "state": "CA",      "type": "state_sales_tax"    }  },  "created": 1682006400,  "expires_at": 1684072000,  "livemode": false,  "status": "active",  "state": "CA",  "type": "standard"}`# Retrieve a registration

Returns a Tax Registration object.

### Parameters

No parameters.

### Returns

A Tax Registration object.

GET/v1/tax/registrations/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tax/registrations/taxreg_NkyGPRPytKq66j \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "taxreg_NkyGPRPytKq66j",  "object": "tax.registration",  "active_from": 1682036640,  "country": "US",  "country_options": {    "us": {      "state": "CA",      "type": "state_sales_tax"    }  },  "created": 1682006400,  "expires_at": null,  "livemode": false,  "status": "active",  "state": "CA",  "type": "standard"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`