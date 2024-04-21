htmlThe Webhook Endpoint object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The Webhook Endpoint object

### Attributes

- idstringUnique identifier for the object.


- api_versionnullablestringThe API version events are rendered as for this webhook endpoint.


- descriptionnullablestringAn optional description of what the webhook is used for.


- enabled_eventsarray of stringsThe list of events to enable for this endpoint. ['*'] indicates that all events are enabled, except those that require explicit selection.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- secretstringThe endpoint’s secret, used to generate webhook signatures. Only returned at creation.


- statusstringThe status of the webhook. It can be enabled or disabled.


- urlstringThe URL of the webhook endpoint.



### More attributesExpand all

- objectstring
- applicationnullablestring
- createdtimestamp
- livemodeboolean

The Webhook Endpoint object`{  "id": "we_1Mr5jULkdIwHu7ix1ibLTM0x",  "object": "webhook_endpoint",  "api_version": null,  "application": null,  "created": 1680122196,  "description": null,  "enabled_events": [    "charge.succeeded",    "charge.failed"  ],  "livemode": false,  "metadata": {},  "secret": "whsec_wRNftLajMZNeslQOP6vEPm4iVx5NlZ6z",  "status": "enabled",  "url": "https://example.com/my/webhook/endpoint"}`# Create a webhook endpoint

A webhook endpoint must have a url and a list of enabled_events. You may optionally specify the Boolean connect parameter. If set to true, then a Connect webhook endpoint that notifies the specified url about events from all connected accounts is created; otherwise an account webhook endpoint that notifies the specified url only about events from your account is created. You can also create webhook endpoints in the webhooks settings section of the Dashboard.

### Parameters

- enabled_eventsarray of enumsRequiredThe list of events to enable for this endpoint. You may specify ['*'] to enable all events, except those that require explicit selection.

Possible enum values`account.application.authorized`Occurs whenever a user authorizes an application. Sent to the related application only.

`account.application.deauthorized`Occurs whenever a user deauthorizes an application. Sent to the related application only.

`account.external_account.created`Occurs whenever an external account is created.

`account.external_account.deleted`Occurs whenever an external account is deleted.

`account.external_account.updated`Occurs whenever an external account is updated.

`account.updated`Occurs whenever an account status or property has changed.

`application_fee.created`Occurs whenever an application fee is created on a charge.

`application_fee.refund.updated`Occurs whenever an application fee refund is updated.

`application_fee.refunded`Occurs whenever an application fee is refunded, whether from refunding a charge or from refunding the application fee directly. This includes partial refunds.

`balance.available`Occurs whenever your Stripe balance has been updated (e.g., when a charge is available to be paid out). By default, Stripe automatically transfers funds in your balance to your bank account on a daily basis. This event is not fired for negative transactions.

[Show 339 more](#)
- urlstringRequiredThe URL of the webhook endpoint.


- api_versionstringEvents sent to this endpoint will be generated with this Stripe Version instead of your account’s default Stripe Version.


- descriptionstringAn optional description of what the webhook is used for.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- connectboolean

### Returns

Returns the webhook endpoint object with the secret field populated.

POST/v1/webhook_endpointsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/webhook_endpoints \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "enabled_events[]"="charge.succeeded" \  -d "enabled_events[]"="charge.failed" \  --data-urlencode url="https://example.com/my/webhook/endpoint"`Response`{  "id": "we_1Mr5jULkdIwHu7ix1ibLTM0x",  "object": "webhook_endpoint",  "api_version": null,  "application": null,  "created": 1680122196,  "description": null,  "enabled_events": [    "charge.succeeded",    "charge.failed"  ],  "livemode": false,  "metadata": {},  "secret": "whsec_wRNftLajMZNeslQOP6vEPm4iVx5NlZ6z",  "status": "enabled",  "url": "https://example.com/my/webhook/endpoint"}`# Update a webhook endpoint

Updates the webhook endpoint. You may edit the url, the list of enabled_events, and the status of your endpoint.

### Parameters

- descriptionstringAn optional description of what the webhook is used for.


- enabled_eventsarray of enumsThe list of events to enable for this endpoint. You may specify ['*'] to enable all events, except those that require explicit selection.

Possible enum values`account.application.authorized`Occurs whenever a user authorizes an application. Sent to the related application only.

`account.application.deauthorized`Occurs whenever a user deauthorizes an application. Sent to the related application only.

`account.external_account.created`Occurs whenever an external account is created.

`account.external_account.deleted`Occurs whenever an external account is deleted.

`account.external_account.updated`Occurs whenever an external account is updated.

`account.updated`Occurs whenever an account status or property has changed.

`application_fee.created`Occurs whenever an application fee is created on a charge.

`application_fee.refund.updated`Occurs whenever an application fee refund is updated.

`application_fee.refunded`Occurs whenever an application fee is refunded, whether from refunding a charge or from refunding the application fee directly. This includes partial refunds.

`balance.available`Occurs whenever your Stripe balance has been updated (e.g., when a charge is available to be paid out). By default, Stripe automatically transfers funds in your balance to your bank account on a daily basis. This event is not fired for negative transactions.

[Show 339 more](#)
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- urlstringThe URL of the webhook endpoint.



### More parametersExpand all

- disabledboolean

### Returns

The updated webhook endpoint object if successful. Otherwise, this call raises an error.

POST/v1/webhook_endpoints/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/webhook_endpoints/we_1Mr5jULkdIwHu7ix1ibLTM0x \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "enabled_events[]"="charge.succeeded" \  -d "enabled_events[]"="charge.failed" \  --data-urlencode url="https://example.com/new_endpoint"`Response`{  "id": "we_1Mr5jULkdIwHu7ix1ibLTM0x",  "object": "webhook_endpoint",  "api_version": null,  "application": null,  "created": 1680122196,  "description": null,  "enabled_events": [    "charge.succeeded",    "charge.failed"  ],  "livemode": false,  "metadata": {},  "status": "disabled",  "url": "https://example.com/new_endpoint"}`# Retrieve a webhook endpoint

Retrieves the webhook endpoint with the given ID.

### Parameters

No parameters.

### Returns

Returns a webhook endpoint if a valid webhook endpoint ID was provided. Raises an error otherwise.

GET/v1/webhook_endpoints/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/webhook_endpoints/we_1Mr5jULkdIwHu7ix1ibLTM0x \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "we_1Mr5jULkdIwHu7ix1ibLTM0x",  "object": "webhook_endpoint",  "api_version": null,  "application": null,  "created": 1680122196,  "description": null,  "enabled_events": [    "charge.succeeded",    "charge.failed"  ],  "livemode": false,  "metadata": {},  "status": "enabled",  "url": "https://example.com/my/webhook/endpoint"}`# List all webhook endpoints

Returns a list of your webhook endpoints.

### Parameters

No parameters.

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit webhook endpoints, starting after webhook endpoint starting_after. Each entry in the array is a separate webhook endpoint object. If no more webhook endpoints are available, the resulting array will be empty. This request should never raise an error.

GET/v1/webhook_endpointsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/webhook_endpoints \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/webhook_endpoints",  "has_more": false,  "data": [    {      "id": "we_1Mr5jULkdIwHu7ix1ibLTM0x",      "object": "webhook_endpoint",      "api_version": null,      "application": null,      "created": 1680122196,      "description": null,      "enabled_events": [        "charge.succeeded",        "charge.failed"      ],      "livemode": false,      "metadata": {},      "status": "enabled",      "url": "https://example.com/my/webhook/endpoint"    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`