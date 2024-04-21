htmlUpdate a VerificationSession | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Update a VerificationSession

Updates a VerificationSession object.

When the session status is requires_input, you can use this method to update the verification check and options.

### Parameters

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- optionsobjectA set of options for the session’s verification checks.

Show child parameters
- typeenumThe type of verification check to be performed.

Possible enum values`document`Document check.

`id_number`ID number check.



### Returns

Returns the updated VerificationSession object

POST/v1/identity/verification_sessions/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/identity/verification_sessions/vs_1NuN9WLkdIwHu7ix597AR9uz \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d type=id_number`Response`{  "id": "vs_1NuN9WLkdIwHu7ix597AR9uz",  "object": "identity.verification_session",  "client_secret": "...",  "created": 1695680478,  "last_error": null,  "last_verification_report": null,  "livemode": false,  "metadata": {},  "options": {},  "redaction": null,  "status": "requires_input",  "type": "id_number",  "url": "..."}`# Retrieve a VerificationSession

Retrieves the details of a VerificationSession that was previously created.

When the session status is requires_input, you can use this method to retrieve a valid client_secret or url to allow re-submission.

### Parameters

No parameters.

### Returns

Returns a VerificationSession object

GET/v1/identity/verification_sessions/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/identity/verification_sessions/vs_1NuNAILkdIwHu7ixh7OtGMLw \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "vs_1NuNAILkdIwHu7ixh7OtGMLw",  "object": "identity.verification_session",  "client_secret": "...",  "created": 1695680526,  "last_error": null,  "last_verification_report": null,  "livemode": false,  "metadata": {},  "options": {    "document": {      "require_matching_selfie": true    }  },  "redaction": null,  "status": "requires_input",  "type": "document",  "url": "..."}`# List VerificationSessions

Returns a list of VerificationSessions

### Parameters

- client_reference_idstringA string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.


- createdobjectOnly return VerificationSessions that were created during the given date interval.

Show child parameters
- statusenumOnly return VerificationSessions with this status. Learn more about the lifecycle of sessions.

Possible enum values`canceled`The VerificationSession has been invalidated for future submission attempts.

`processing`The session has been submitted and is being processed. Most verification checks are processed in less than 1 minute.

`requires_input`Requires user input before processing can continue.

`verified`Processing of all the verification checks are complete and successfully verified.



### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

List of VerificationSession objects that match the provided filter criteria.

GET/v1/identity/verification_sessionsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/identity/verification_sessions \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/identity/verification_sessions",  "has_more": false,  "data": [    {      "id": "vs_1NuNAILkdIwHu7ixh7OtGMLw",      "object": "identity.verification_session",      "client_secret": "...",      "created": 1695680526,      "last_error": null,      "last_verification_report": null,      "livemode": false,      "metadata": {},      "options": {        "document": {          "require_matching_selfie": true        }      },      "redaction": null,      "status": "requires_input",      "type": "document",      "url": "..."    }    {...}    {...}  ],}`# Cancel a VerificationSession

A VerificationSession object can be canceled when it is in requires_input status.

Once canceled, future submission attempts are disabled. This cannot be undone. Learn more.

### Parameters

No parameters.

### Returns

Returns the canceled VerificationSession object

POST/v1/identity/verification_sessions/:id/cancelServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/identity/verification_sessions/vs_1NuN3kLkdIwHu7ixk5OvTq3b/cancel \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "vs_1NuN3kLkdIwHu7ixk5OvTq3b",  "object": "identity.verification_session",  "client_secret": null,  "created": 1695680120,  "last_error": null,  "last_verification_report": null,  "livemode": false,  "metadata": {},  "options": {    "document": {      "require_matching_selfie": true    }  },  "redaction": null,  "status": "canceled",  "type": "document",  "url": null}`# Redact a VerificationSession

Redact a VerificationSession to remove all collected information from Stripe. This will redact the VerificationSession and all objects related to it, including VerificationReports, Events, request logs, etc.

A VerificationSession object can be redacted when it is in requires_input or verified status. Redacting a VerificationSession in requires_action state will automatically cancel it.

The redaction process may take up to four days. When the redaction process is in progress, the VerificationSession’s redaction.status field will be set to processing; when the process is finished, it will change to redacted and an identity.verification_session.redacted event will be emitted.

Redaction is irreversible. Redacted objects are still accessible in the Stripe API, but all the fields that contain personal data will be replaced by the string [redacted] or a similar placeholder. The metadata field will also be erased. Redacted objects cannot be updated or used for any purpose.

Learn more.

### Parameters

No parameters.

### Returns

Returns the redacted VerificationSession object

POST/v1/identity/verification_sessions/:id/redactServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/identity/verification_sessions/vs_1NuN3kLkdIwHu7ixk5OvTq3b/redact \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "vs_1NuN3kLkdIwHu7ixk5OvTq3b",  "object": "identity.verification_session",  "client_secret": null,  "created": 1695680120,  "last_error": null,  "last_verification_report": null,  "livemode": false,  "metadata": {},  "options": {    "document": {      "require_matching_selfie": true    }  },  "redaction": {    "status": "processing"  },  "status": "canceled",  "type": "document",  "url": null}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`