htmlThe File Link object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The File Link object

### Attributes

- idstringUnique identifier for the object.


- expires_atnullabletimestampTime that the link expires.


- filestringExpandableThe file object this link points to.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- urlnullablestringThe publicly accessible URL to download the file.



### More attributesExpand all

- objectstring
- createdtimestamp
- expiredboolean
- livemodeboolean

The File Link object`{  "id": "link_1Mr23jLkdIwHu7ix65betcoo",  "object": "file_link",  "created": 1680108075,  "expired": false,  "expires_at": null,  "file": "file_1Mr23iLkdIwHu7ixQkCV3CBR",  "livemode": false,  "metadata": {},  "url": "https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h"}`# Create a file link

Creates a new file link object.

### Parameters

- filestringRequiredThe ID of the file. The file’s purpose must be one of the following: business_icon, business_logo, customer_signature, dispute_evidence, finance_report_run, identity_document_downloadable, pci_document, selfie, sigma_scheduled_query, tax_document_user_upload, or terminal_reader_splashscreen.


- expires_attimestampThe link isn’t usable after this future timestamp.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns the file link object if successful and raises an error otherwise.

POST/v1/file_linksServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/file_links \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d file=file_1Mr23iLkdIwHu7ixQkCV3CBR`Response`{  "id": "link_1Mr23jLkdIwHu7ix65betcoo",  "object": "file_link",  "created": 1680108075,  "expired": false,  "expires_at": null,  "file": "file_1Mr23iLkdIwHu7ixQkCV3CBR",  "livemode": false,  "metadata": {},  "url": "https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h"}`# Update a file link

Updates an existing file link object. Expired links can no longer be updated.

### Parameters

- expires_atstring | timestampA future timestamp after which the link will no longer be usable, or now to expire the link immediately.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns the file link object if successful, and raises an error otherwise.

POST/v1/file_links/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/file_links/link_1Mr23jLkdIwHu7ix65betcoo \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "link_1Mr23jLkdIwHu7ix65betcoo",  "object": "file_link",  "created": 1680108075,  "expired": false,  "expires_at": null,  "file": "file_1Mr23iLkdIwHu7ixQkCV3CBR",  "livemode": false,  "metadata": {    "order_id": "6735"  },  "url": "https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h"}`# Retrieve a file link

Retrieves the file link with the given ID.

### Parameters

No parameters.

### Returns

If the identifier you provide is valid, a file link object returns. If not, Stripe raises an error.

GET/v1/file_links/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/file_links/link_1Mr23jLkdIwHu7ix65betcoo \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "link_1Mr23jLkdIwHu7ix65betcoo",  "object": "file_link",  "created": 1680108075,  "expired": false,  "expires_at": null,  "file": "file_1Mr23iLkdIwHu7ixQkCV3CBR",  "livemode": false,  "metadata": {},  "url": "https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h"}`# List all file links

Returns a list of file links.

### Parameters

No parameters.

### More parametersExpand all

- createdobject
- ending_beforestring
- expiredboolean
- filestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit file links, starting after the starting_after file link. Each entry in the array is a separate file link object. If there aren’t additional available file links, the resulting array is empty.

GET/v1/file_linksServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/file_links \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/file_links",  "has_more": false,  "data": [    {      "id": "link_1Mr23jLkdIwHu7ix65betcoo",      "object": "file_link",      "created": 1680108075,      "expired": false,      "expires_at": null,      "file": "file_1Mr23iLkdIwHu7ixQkCV3CBR",      "livemode": false,      "metadata": {},      "url": "https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h"    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`