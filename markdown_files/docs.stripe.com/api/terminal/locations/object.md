htmlThe Location object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The Location object

### Attributes

- idstringUnique identifier for the object.


- addressobjectThe full address of the location.

Show child attributes
- display_namestringThe display name of the location.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.



### More attributesExpand all

- objectstring
- configuration_overridesnullablestring
- livemodeboolean

The Location object`{  "id": "tml_FBakXQG8bQk4Mm",  "object": "terminal.location",  "address": {    "city": "San Francisco",    "country": "US",    "line1": "1234 Main Street",    "line2": "",    "postal_code": "94111",    "state": "CA"  },  "display_name": "My First Store",  "livemode": false,  "metadata": {}}`# Create a Location

Creates a new Location object. For further details, including which address fields are required in each country, see the Manage locations guide.

### Parameters

- addressobjectRequiredThe full address of the location.

Show child parameters
- display_namestringRequiredA name for the location.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- configuration_overridesstring

### Returns

Returns a Location object if creation succeeds.

POST/v1/terminal/locationsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/terminal/locations \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d display_name="My First Store" \  -d "address[line1]"="1234 Main Street" \  -d "address[city]"="San Francisco" \  -d "address[postal_code]"=94111 \  -d "address[state]"=CA \  -d "address[country]"=US`Response`{  "id": "tml_FBakXQG8bQk4Mm",  "object": "terminal.location",  "address": {    "city": "San Francisco",    "country": "US",    "line1": "1234 Main Street",    "line2": "",    "postal_code": "94111",    "state": "CA"  },  "display_name": "My First Store",  "livemode": false,  "metadata": {}}`# Update a Location

Updates a Location object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

### Parameters

- addressobjectThe full address of the location.

Show child parameters
- display_namestringA name for the location.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- configuration_overridesstring

### Returns

Returns an updated Location object if a valid identifier was provided.

POST/v1/terminal/locations/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/terminal/locations/tml_FBakXQG8bQk4Mm \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d display_name="Update Store Name"`Response`{  "id": "tml_FBakXQG8bQk4Mm",  "object": "terminal.location",  "address": {    "city": "San Francisco",    "country": "US",    "line1": "1234 Main Street",    "line2": "",    "postal_code": "94111",    "state": "CA"  },  "display_name": "Update Store Name",  "livemode": false,  "metadata": {}}`# Retrieve a Location

Retrieves a Location object.

### Parameters

No parameters.

### Returns

Returns a Location object if a valid identifier was provided.

GET/v1/terminal/locations/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/terminal/locations/tml_FBakXQG8bQk4Mm \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "tml_FBakXQG8bQk4Mm",  "object": "terminal.location",  "address": {    "city": "San Francisco",    "country": "US",    "line1": "1234 Main Street",    "line2": "",    "postal_code": "94111",    "state": "CA"  },  "display_name": "My First Store",  "livemode": false,  "metadata": {}}`# List all Locations

Returns a list of Location objects.

### Parameters

No parameters.

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit locations, starting after location starting_after. Each entry in the array is a separate Terminal location object. If no more locations are available, the resulting array will be empty.

GET/v1/terminal/locationsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/terminal/locations \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/terminal/locations",  "has_more": false,  "data": [    {      "id": "tml_FBakXQG8bQk4Mm",      "object": "terminal.location",      "address": {        "city": "San Francisco",        "country": "US",        "line1": "1234 Main Street",        "line2": "",        "postal_code": "94111",        "state": "CA"      },      "display_name": "My First Store",      "livemode": false,      "metadata": {}    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`