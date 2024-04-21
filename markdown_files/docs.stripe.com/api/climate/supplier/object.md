htmlThe Climate supplier object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The Climate supplier object

### Attributes

- idstringUnique identifier for the object.


- objectstringString representing the object’s type. Objects of the same type share the same value.


- info_urlstringLink to a webpage to learn more about the supplier.


- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.


- locationsarray of objectsThe locations in which this supplier operates.

Show child attributes
- namestringName of this carbon removal supplier.


- removal_pathwayenumThe scientific pathway used for carbon removal.

Possible enum values`biomass_carbon_removal_and_storage`Biomass carbon removal and storage

`direct_air_capture`Direct air capture

`enhanced_weathering`Enhanced weathering



The Climate supplier object`{  "id": "climsup_charm_industrial",  "object": "climate.supplier",  "info_url": "https://frontierclimate.com/portfolio/charm-industrial",  "livemode": false,  "locations": [    {      "city": "San Francisco",      "country": "US",      "latitude": 37.7749,      "longitude": -122.4194,      "region": "CA"    }  ],  "name": "Charm Industrial",  "removal_pathway": "biomass_carbon_removal_and_storage"}`# Retrieve a supplier

Retrieves a Climate supplier object.

### Parameters

No parameters.

### Returns

A Climate supplier object.

GET/v1/climate/suppliers/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/climate/suppliers/climsup_charm_industrial \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "climsup_charm_industrial",  "object": "climate.supplier",  "info_url": "https://frontierclimate.com/portfolio/charm-industrial",  "livemode": false,  "locations": [    {      "city": "San Francisco",      "country": "US",      "latitude": 37.7749,      "longitude": -122.4194,      "region": "CA"    }  ],  "name": "Charm Industrial",  "removal_pathway": "biomass_carbon_removal_and_storage"}`# List suppliers

Lists all available Climate supplier objects.

### Parameters

No parameters.

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit suppliers, starting after supplier starting_after. Each entry in the array is a separate supplier object. If no more suppliers are available, the resulting array is empty.

GET/v1/climate/suppliersServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/climate/suppliers \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/climate/suppliers",  "has_more": false,  "data": [    {      "id": "climsup_charm_industrial",      "object": "climate.supplier",      "info_url": "https://frontierclimate.com/portfolio/charm-industrial",      "livemode": false,      "locations": [        {          "city": "San Francisco",          "country": "US",          "latitude": 37.7749,          "longitude": -122.4194,          "region": "CA"        }      ],      "name": "Charm Industrial",      "removal_pathway": "biomass_carbon_removal_and_storage"    }    {...}    {...}  ],}`# Forwarding RequestPreview feature

Instructs Stripe to make a request on your behalf using the destination URL. The destination URL is activated by Stripe at the time of onboarding. Stripe verifies requests with your credentials provided during onboarding, and injects card details from the payment_method into the request.

Stripe redacts all sensitive fields and headers, including authentication credentials and card numbers, before storing the request and response data in the forwarding Request object, which are subject to a 30-day retention period.

You can provide a Stripe idempotency key to make sure that requests with the same key result in only one outbound request. The Stripe idempotency key provided should be unique and different from any idempotency keys provided on the underlying third-party request.

Forwarding Requests are synchronous requests that return a response or time out according to Stripe’s limits.

Related guide: Forward card details to third-party API endpoints.

Endpoints
Show

# Webhook Endpoints

You can configure webhook endpoints via the API to be notified about events that happen in your Stripe account or connected accounts.

Most users configure webhooks from the dashboard, which provides a user interface for registering and testing your webhook endpoints.

Related guide: Setting up webhooks

Endpoints
Show

Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`