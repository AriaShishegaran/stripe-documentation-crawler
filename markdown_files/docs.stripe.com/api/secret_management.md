htmlSecrets | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Secrets

Secret Store is an API that allows Stripe Apps developers to securely persist secrets for use by UI Extensions and app backends.

The primary resource in Secret Store is a secret. Other apps can’t view secrets created by an app. Additionally, secrets are scoped to provide further permission control.

All Dashboard users and the app backend share account scoped secrets. Use the account scope for secrets that don’t change per-user, like a third-party API key.

A user scoped secret is accessible by the app backend and one specific Dashboard user. Use the user scope for per-user secrets like per-user OAuth tokens, where different users might have different permissions.

Related guide: Store data between page reloads

Endpoints
# The Secret object

### Attributes

- idstringUnique identifier for the object.


- objectstringString representing the object’s type. Objects of the same type share the same value.


- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.


- deletednullablebooleanIf true, indicates that this secret has been deleted


- expires_atnullabletimestampThe Unix timestamp for the expiry time of the secret, after which the secret deletes.


- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.


- namestringA name for the secret that’s unique within the scope.


- payloadnullablestringExpandableThe plaintext secret value to be stored.


- scopeobjectSpecifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.

Show child attributes

The Secret object`{  "id": "appsecret_5110hHS1707T6fjBnah1LkdIwHu7ix",  "object": "apps.secret",  "created": 1680209063,  "expires_at": null,  "livemode": false,  "name": "my-api-key",  "scope": {    "type": "account"  }}`# List secrets

List all secrets stored on the given scope.

### Parameters

- scopeobjectRequiredSpecifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.

Show child parameters

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit Secrets, starting after Secret starting_after. Each entry in the array is a separate Secret object. If no more Secrets are available, the resulting array will be empty.

GET/v1/apps/secretsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/apps/secrets \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "scope[type]"=account`Response`{  "object": "list",  "url": "/v1/apps/secrets",  "has_more": false,  "data": [    {      "id": "appsecret_5110hHS1707T6fjBnah1LkdIwHu7ix",      "object": "apps.secret",      "created": 1680209063,      "expires_at": null,      "livemode": false,      "name": "my-api-key",      "scope": {        "type": "account"      }    }    {...}    {...}  ],}`# Delete a Secret

Deletes a secret from the secret store by name and scope.

### Parameters

- namestringRequiredA name for the secret that’s unique within the scope.


- scopeobjectRequiredSpecifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.

Show child parameters

### Returns

Returns the deleted secret object.

POST/v1/apps/secrets/deleteServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/apps/secrets/delete \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d name=my-api-key \  -d "scope[type]"=account`Response`{  "id": "appsecret_5110hHS1707T6fjBnah1LkdIwHu7ix",  "object": "apps.secret",  "deleted": true}`# Find a Secret

Finds a secret in the secret store by name and scope.

### Parameters

- namestringRequiredA name for the secret that’s unique within the scope.


- scopeobjectRequiredSpecifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.

Show child parameters

### Returns

Returns a secret object.

GET/v1/apps/secrets/findServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/apps/secrets/find \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d name=my-api-key \  -d "scope[type]"=account`Response`{  "id": "appsecret_5110hHS1707T6fjBnah1LkdIwHu7ix",  "object": "apps.secret",  "created": 1680209063,  "expires_at": null,  "livemode": false,  "name": "my-api-key",  "scope": {    "type": "account"  }}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`