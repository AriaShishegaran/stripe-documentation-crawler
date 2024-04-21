htmlCapabilities | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Capabilities

This is an object representing a capability for a Stripe account.

Related guide: Account capabilities

Endpoints
# The Capability object

### Attributes

- idstringThe identifier for the capability.


- accountstringExpandableThe account for which the capability enables functionality.


- requestedbooleanWhether the capability has been requested.


- requirementsobjectInformation about the requirements for the capability, including what information needs to be collected, and by when.

Show child attributes
- statusenumThe status of the capability. Can be active, inactive, pending, or unrequested.

Possible enum values`active``disabled``inactive``pending``unrequested`

### More attributesExpand all

- objectstring
- future_requirementsobject
- requested_atnullabletimestamp

The Capability object`{  "id": "card_payments",  "object": "capability",  "account": "acct_1032D82eZvKYlo2C",  "future_requirements": {    "alternatives": [],    "current_deadline": null,    "currently_due": [],    "disabled_reason": null,    "errors": [],    "eventually_due": [],    "past_due": [],    "pending_verification": []  },  "requested": true,  "requested_at": 1688491010,  "requirements": {    "alternatives": [],    "current_deadline": null,    "currently_due": [],    "disabled_reason": null,    "errors": [],    "eventually_due": [],    "past_due": [],    "pending_verification": []  },  "status": "inactive"}`# Update an Account Capability

Updates an existing Account Capability. Request or remove a capability by updating its requested parameter.

### Parameters

- requestedbooleanTo request a new capability for an account, pass true. There can be a delay before the requested capability becomes active. If the capability has any activation requirements, the response includes them in the requirements arrays.

If a capability isn’t permanent, you can remove it from the account by passing false. Most capabilities are permanent after they’ve been requested. Attempting to remove a permanent capability returns an error.



### Returns

Returns an Account Capability object.

POST/v1/accounts/:id/capabilities/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/capabilities/card_payments \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d requested=true`Response`{  "id": "card_payments",  "object": "capability",  "account": "acct_1032D82eZvKYlo2C",  "future_requirements": {    "alternatives": [],    "current_deadline": null,    "currently_due": [],    "disabled_reason": null,    "errors": [],    "eventually_due": [],    "past_due": [],    "pending_verification": []  },  "requested": true,  "requested_at": 1688491010,  "requirements": {    "alternatives": [],    "current_deadline": null,    "currently_due": [],    "disabled_reason": null,    "errors": [],    "eventually_due": [],    "past_due": [],    "pending_verification": []  },  "status": "inactive"}`# Retrieve an Account Capability

Retrieves information about the specified Account Capability.

### Parameters

No parameters.

### Returns

Returns an Account Capability object.

GET/v1/accounts/:id/capabilities/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/capabilities/card_payments \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "card_payments",  "object": "capability",  "account": "acct_1032D82eZvKYlo2C",  "future_requirements": {    "alternatives": [],    "current_deadline": null,    "currently_due": [],    "disabled_reason": null,    "errors": [],    "eventually_due": [],    "past_due": [],    "pending_verification": []  },  "requested": true,  "requested_at": 1688491010,  "requirements": {    "alternatives": [],    "current_deadline": null,    "currently_due": [],    "disabled_reason": null,    "errors": [],    "eventually_due": [],    "past_due": [],    "pending_verification": []  },  "status": "inactive"}`# List all account capabilities

Returns a list of capabilities associated with the account. The capabilities are returned sorted by creation date, with the most recent capability appearing first.

### Parameters

No parameters.

### Returns

A dictionary with a data property that contains an array of the capabilities of this account. Each entry in the array is a separate capability object.

GET/v1/accounts/:id/capabilitiesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/capabilities \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "object": "list",  "url": "/v1/accounts/acct_1032D82eZvKYlo2C/capabilities",  "has_more": false,  "data": [    {      "id": "card_payments",      "object": "capability",      "account": "acct_1032D82eZvKYlo2C",      "future_requirements": {        "alternatives": [],        "current_deadline": null,        "currently_due": [],        "disabled_reason": null,        "errors": [],        "eventually_due": [],        "past_due": [],        "pending_verification": []      },      "requested": true,      "requested_at": 1693951912,      "requirements": {        "alternatives": [],        "current_deadline": null,        "currently_due": [],        "disabled_reason": null,        "errors": [],        "eventually_due": [],        "past_due": [],        "pending_verification": []      },      "status": "inactive"    }  ]}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`