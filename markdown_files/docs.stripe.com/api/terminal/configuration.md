htmlConfiguration | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Configuration

A Configurations object represents how features should be configured for terminal readers.

Endpoints
# The Configuration object

### Attributes

- idstringUnique identifier for the object.


- bbpos_wisepos_enullableobjectAn object containing device type specific settings for BBPOS WisePOS E

Show child attributes
- is_account_defaultnullablebooleanWhether this Configuration is the default for your account


- tippingnullableobjectOn-reader tipping settings

Show child attributes
- verifone_p400nullableobjectAn object containing device type specific settings for Verifone P400

Show child attributes

### More attributesExpand all

- objectstring
- livemodeboolean
- namenullablestring
- offlinenullableobject

The Configuration object`{  "id": "tmc_FQqbaQCiy0m1xc",  "object": "terminal.configuration",  "is_account_default": false,  "livemode": false}`# Create a Configuration

Creates a new Configuration object.

### Parameters

- bbpos_wisepos_eobjectAn object containing device type specific settings for BBPOS WisePOS E readers

Show child parameters
- tippingobjectTipping configurations for readers supporting on-reader tips

Show child parameters
- verifone_p400objectAn object containing device type specific settings for Verifone P400 readers

Show child parameters

### More parametersExpand all

- namestring
- offlineobject
- stripe_s700objectPreview feature

### Returns

Returns a Configuration object if creation succeeds.

POST/v1/terminal/configurationsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/terminal/configurations \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "tmc_FQqbaQCiy0m1xc",  "object": "terminal.configuration",  "is_account_default": false,  "livemode": false}`# Update a Configuration

Updates a new Configuration object.

### Parameters

- bbpos_wisepos_eobjectAn object containing device type specific settings for BBPOS WisePOS E readers

Show child parameters
- tippingobjectTipping configurations for readers supporting on-reader tips

Show child parameters
- verifone_p400objectAn object containing device type specific settings for Verifone P400 readers

Show child parameters

### More parametersExpand all

- namestring
- offlineobject
- stripe_s700objectPreview feature

### Returns

Returns a Configuration object if the update succeeds.

POST/v1/terminal/configurations/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/terminal/configurations/tmc_FQqbaQCiy0m1xc \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "bbpos_wisepos_e[splashscreen]"=file_1NtDiHBHO5VeT9SUjuWGkEAN`Response`{  "id": "tmc_FQqbaQCiy0m1xc",  "object": "terminal.configuration",  "bbpos_wisepos_e": {    "splashscreen": "file_1NtDiPBHO5VeT9SUvD7GHCi0"  },  "is_account_default": false,  "livemode": false}`# Retrieve a Configuration

Retrieves a Configuration object.

### Parameters

No parameters.

### Returns

Returns a Configuration object if a valid identifier was provided.

GET/v1/terminal/configurations/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/terminal/configurations/tmc_FQqbaQCiy0m1xc \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "tmc_FQqbaQCiy0m1xc",  "object": "terminal.configuration",  "is_account_default": false,  "livemode": false}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`