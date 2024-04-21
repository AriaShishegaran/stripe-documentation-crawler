- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Verification Session

[Verification Session](/api/identity/verification_sessions)

A VerificationSession guides you through the process of collecting and verifying the identities of your users. It contains details about the type of verification, such as what verification check to perform. Only create one VerificationSession for each verification in your system.

[verification check](/identity/verification-checks)

A VerificationSession transitions through multiple statuses throughout its lifetime as it progresses through the verification flow. The VerificationSession contains the user’s verified data after verification checks are complete.

[multiple statuses](/identity/how-sessions-work)

Related guide: The Verification Sessions API

[The Verification Sessions API](/identity/verification-sessions)

[POST/v1/identity/verification_sessions](/api/identity/verification_sessions/create)

[POST/v1/identity/verification_sessions/:id](/api/identity/verification_sessions/update)

[GET/v1/identity/verification_sessions/:id](/api/identity/verification_sessions/retrieve)

[GET/v1/identity/verification_sessions](/api/identity/verification_sessions/list)

[POST/v1/identity/verification_sessions/:id/cancel](/api/identity/verification_sessions/cancel)

[POST/v1/identity/verification_sessions/:id/redact](/api/identity/verification_sessions/redact)

# The VerificationSession object

[The VerificationSession object](/api/identity/verification_sessions/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- objectstringString representing the object’s type. Objects of the same type share the same value.

String representing the object’s type. Objects of the same type share the same value.

- client_reference_idnullable stringA string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.

A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.

- client_secretnullable stringThe short-lived client secret used by Stripe.js to show a verification modal inside your app. This client secret expires after 24 hours and can only be used once. Don’t store it, log it, embed it in a URL, or expose it to anyone other than the user. Make sure that you have TLS enabled on any page that includes the client secret. Refer to our docs on passing the client secret to the frontend to learn more.

The short-lived client secret used by Stripe.js to show a verification modal inside your app. This client secret expires after 24 hours and can only be used once. Don’t store it, log it, embed it in a URL, or expose it to anyone other than the user. Make sure that you have TLS enabled on any page that includes the client secret. Refer to our docs on passing the client secret to the frontend to learn more.

[show a verification modal](/js/identity/modal)

[passing the client secret to the frontend](/identity/verification-sessions#client-secret)

- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.

Time at which the object was created. Measured in seconds since the Unix epoch.

- last_errornullable objectIf present, this property tells you the last error encountered when processing the verification.Show child attributes

If present, this property tells you the last error encountered when processing the verification.

- last_verification_reportnullable stringExpandableID of the most recent VerificationReport. Learn more about accessing detailed verification results.

ID of the most recent VerificationReport. Learn more about accessing detailed verification results.

[Learn more about accessing detailed verification results.](/identity/verification-sessions#results)

- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.

Has the value true if the object exists in live mode or the value false if the object exists in test mode.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- optionsnullable objectA set of options for the session’s verification checks.Show child attributes

A set of options for the session’s verification checks.

- redactionnullable objectRedaction status of this VerificationSession. If the VerificationSession is not redacted, this field will be null.Show child attributes

Redaction status of this VerificationSession. If the VerificationSession is not redacted, this field will be null.

- statusenumStatus of this VerificationSession. Learn more about the lifecycle of sessions.Possible enum valuescanceledThe VerificationSession has been invalidated for future submission attempts.processingThe session has been submitted and is being processed. Most verification checks are processed in less than 1 minute.requires_inputRequires user input before processing can continue.verifiedProcessing of all the verification checks are complete and successfully verified.

Status of this VerificationSession. Learn more about the lifecycle of sessions.

[Learn more about the lifecycle of sessions](/identity/how-sessions-work)

The VerificationSession has been invalidated for future submission attempts.

The session has been submitted and is being processed. Most verification checks are processed in less than 1 minute.

[verification checks](/identity/verification-checks)

Requires user input before processing can continue.

Processing of all the verification checks are complete and successfully verified.

- typeenumThe type of verification check to be performed.Possible enum valuesdocumentDocument check.id_numberID number check.

The type of verification check to be performed.

[verification check](/identity/verification-checks)

Document check.

[Document check](/identity/verification-checks?type=document)

ID number check.

[ID number check](/identity/verification-checks?type=id-number)

- urlnullable stringThe short-lived URL that you use to redirect a user to Stripe to submit their identity information. This URL expires after 48 hours and can only be used once. Don’t store it, log it, send it in emails or expose it to anyone other than the user. Refer to our docs on verifying identity documents to learn how to redirect users to Stripe.

The short-lived URL that you use to redirect a user to Stripe to submit their identity information. This URL expires after 48 hours and can only be used once. Don’t store it, log it, send it in emails or expose it to anyone other than the user. Refer to our docs on verifying identity documents to learn how to redirect users to Stripe.

[verifying identity documents](/identity/verify-identity-documents?platform=web&type=redirect)

- verified_outputsnullable objectExpandableThe user’s verified data.Show child attributes

The user’s verified data.

# Create a VerificationSession

[Create a VerificationSession](/api/identity/verification_sessions/create)

Creates a VerificationSession object.

After the VerificationSession is created, display a verification modal using the session client_secret or send your users to the session’s url.

If your API key is in test mode, verification checks won’t actually process, though everything else will occur as if in live mode.

Related guide: Verify your users’ identity documents

[Verify your users’ identity documents](/identity/verify-identity-documents)

- client_reference_idstringA string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.

A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- optionsobjectA set of options for the session’s verification checks.Show child parameters

A set of options for the session’s verification checks.

- return_urlstringThe URL that the user will be redirected to upon completing the verification flow.

The URL that the user will be redirected to upon completing the verification flow.

- typeenumThe type of verification check to be performed.Possible enum valuesdocumentDocument check.id_numberID number check.

The type of verification check to be performed.

[verification check](/identity/verification-checks)

Document check.

[Document check](/identity/verification-checks?type=document)

ID number check.

[ID number check](/identity/verification-checks?type=id-number)

Returns the created VerificationSession object

# Update a VerificationSession

[Update a VerificationSession](/api/identity/verification_sessions/update)

Updates a VerificationSession object.

When the session status is requires_input, you can use this method to update the verification check and options.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- optionsobjectA set of options for the session’s verification checks.Show child parameters

A set of options for the session’s verification checks.

- typeenumThe type of verification check to be performed.Possible enum valuesdocumentDocument check.id_numberID number check.

The type of verification check to be performed.

[verification check](/identity/verification-checks)

Document check.

[Document check](/identity/verification-checks?type=document)

ID number check.

[ID number check](/identity/verification-checks?type=id-number)

Returns the updated VerificationSession object

# Retrieve a VerificationSession

[Retrieve a VerificationSession](/api/identity/verification_sessions/retrieve)

Retrieves the details of a VerificationSession that was previously created.

When the session status is requires_input, you can use this method to retrieve a valid client_secret or url to allow re-submission.

No parameters.

Returns a VerificationSession object
