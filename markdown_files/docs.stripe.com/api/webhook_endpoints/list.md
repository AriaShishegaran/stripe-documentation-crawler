htmlList all webhook endpoints | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# List all webhook endpoints

Returns a list of your webhook endpoints.

### Parameters

No parameters.

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit webhook endpoints, starting after webhook endpoint starting_after. Each entry in the array is a separate webhook endpoint object. If no more webhook endpoints are available, the resulting array will be empty. This request should never raise an error.

GET/v1/webhook_endpointsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/webhook_endpoints \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/webhook_endpoints",  "has_more": false,  "data": [    {      "id": "we_1Mr5jULkdIwHu7ix1ibLTM0x",      "object": "webhook_endpoint",      "api_version": null,      "application": null,      "created": 1680122196,      "description": null,      "enabled_events": [        "charge.succeeded",        "charge.failed"      ],      "livemode": false,      "metadata": {},      "status": "enabled",      "url": "https://example.com/my/webhook/endpoint"    }    {...}    {...}  ],}`# Delete a webhook endpoint

You can also delete webhook endpoints via the webhook endpoint management page of the Stripe dashboard.

### Parameters

No parameters.

### Returns

An object with the deleted webhook endpoints’s ID. Otherwise, this call raises an error, such as if the webhook endpoint has already been deleted.

DELETE/v1/webhook_endpoints/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X DELETE https://api.stripe.com/v1/webhook_endpoints/we_1Mr5jULkdIwHu7ix1ibLTM0x \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "we_1Mr5jULkdIwHu7ix1ibLTM0x",  "object": "webhook_endpoint",  "deleted": true}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`