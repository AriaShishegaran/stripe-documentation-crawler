htmlVerification Session | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Verification Session

A VerificationSession guides you through the process of collecting and verifying the identities of your users. It contains details about the type of verification, such as what verification check to perform. Only create one VerificationSession for each verification in your system.

A VerificationSession transitions through multiple statuses throughout its lifetime as it progresses through the verification flow. The VerificationSession contains the user’s verified data after verification checks are complete.

Related guide: The Verification Sessions API

Endpoints
# The VerificationSession object

### Attributes

- idstringUnique identifier for the object.


- objectstringString representing the object’s type. Objects of the same type share the same value.


- client_reference_idnullablestringA string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.


- client_secretnullablestringThe short-lived client secret used by Stripe.js to show a verification modal inside your app. This client secret expires after 24 hours and can only be used once. Don’t store it, log it, embed it in a URL, or expose it to anyone other than the user. Make sure that you have TLS enabled on any page that includes the client secret. Refer to our docs on passing the client secret to the frontend to learn more.


- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.


- last_errornullableobjectIf present, this property tells you the last error encountered when processing the verification.

Show child attributes
- last_verification_reportnullablestringExpandableID of the most recent VerificationReport. Learn more about accessing detailed verification results.


- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- optionsnullableobjectA set of options for the session’s verification checks.

Show child attributes
- redactionnullableobjectRedaction status of this VerificationSession. If the VerificationSession is not redacted, this field will be null.

Show child attributes
- statusenumStatus of this VerificationSession. Learn more about the lifecycle of sessions.

Possible enum values`canceled`The VerificationSession has been invalidated for future submission attempts.

`processing`The session has been submitted and is being processed. Most verification checks are processed in less than 1 minute.

`requires_input`Requires user input before processing can continue.

`verified`Processing of all the verification checks are complete and successfully verified.


- typeenumThe type of verification check to be performed.

Possible enum values`document`Document check.

`id_number`ID number check.


- urlnullablestringThe short-lived URL that you use to redirect a user to Stripe to submit their identity information. This URL expires after 48 hours and can only be used once. Don’t store it, log it, send it in emails or expose it to anyone other than the user. Refer to our docs on verifying identity documents to learn how to redirect users to Stripe.


- verified_outputsnullableobjectExpandableThe user’s verified data.

Show child attributes

The VerificationSession object`{  "id": "vs_1NuNAILkdIwHu7ixh7OtGMLw",  "object": "identity.verification_session",  "client_secret": "...",  "created": 1695680526,  "last_error": null,  "last_verification_report": null,  "livemode": false,  "metadata": {},  "options": {    "document": {      "require_matching_selfie": true    }  },  "redaction": null,  "status": "requires_input",  "type": "document",  "url": "..."}`# Create a VerificationSession

Creates a VerificationSession object.

After the VerificationSession is created, display a verification modal using the session client_secret or send your users to the session’s url.

If your API key is in test mode, verification checks won’t actually process, though everything else will occur as if in live mode.

Related guide: Verify your users’ identity documents

### Parameters

- client_reference_idstringA string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- optionsobjectA set of options for the session’s verification checks.

Show child parameters
- return_urlstringThe URL that the user will be redirected to upon completing the verification flow.


- typeenumThe type of verification check to be performed.

Possible enum values`document`Document check.

`id_number`ID number check.



### Returns

Returns the created VerificationSession object

POST/v1/identity/verification_sessionsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/identity/verification_sessions \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d type=document`Response`{  "id": "vs_1NuN4zLkdIwHu7ixleE6HvkI",  "object": "identity.verification_session",  "client_secret": "...",  "created": 1695680197,  "last_error": null,  "last_verification_report": null,  "livemode": false,  "metadata": {},  "options": {},  "redaction": null,  "status": "requires_input",  "type": "document",  "url": "..."}`# Update a VerificationSession

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

GET/v1/identity/verification_sessions/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/identity/verification_sessions/vs_1NuNAILkdIwHu7ixh7OtGMLw \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "vs_1NuNAILkdIwHu7ixh7OtGMLw",  "object": "identity.verification_session",  "client_secret": "...",  "created": 1695680526,  "last_error": null,  "last_verification_report": null,  "livemode": false,  "metadata": {},  "options": {    "document": {      "require_matching_selfie": true    }  },  "redaction": null,  "status": "requires_input",  "type": "document",  "url": "..."}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`