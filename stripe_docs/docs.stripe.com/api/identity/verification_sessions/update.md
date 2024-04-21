- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# List VerificationSessions

[List VerificationSessions](/api/identity/verification_sessions/list)

Returns a list of VerificationSessions

- client_reference_idstringA string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.

A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.

- createdobjectOnly return VerificationSessions that were created during the given date interval.Show child parameters

Only return VerificationSessions that were created during the given date interval.

- statusenumOnly return VerificationSessions with this status. Learn more about the lifecycle of sessions.Possible enum valuescanceledThe VerificationSession has been invalidated for future submission attempts.processingThe session has been submitted and is being processed. Most verification checks are processed in less than 1 minute.requires_inputRequires user input before processing can continue.verifiedProcessing of all the verification checks are complete and successfully verified.

Only return VerificationSessions with this status. Learn more about the lifecycle of sessions.

[Learn more about the lifecycle of sessions](/identity/how-sessions-work)

The VerificationSession has been invalidated for future submission attempts.

The session has been submitted and is being processed. Most verification checks are processed in less than 1 minute.

[verification checks](/identity/verification-checks)

Requires user input before processing can continue.

Processing of all the verification checks are complete and successfully verified.

- ending_beforestring

- limitinteger

- starting_afterstring

List of VerificationSession objects that match the provided filter criteria.

# Cancel a VerificationSession

[Cancel a VerificationSession](/api/identity/verification_sessions/cancel)

A VerificationSession object can be canceled when it is in requires_input status.

[status](/identity/how-sessions-work)

Once canceled, future submission attempts are disabled. This cannot be undone. Learn more.

[Learn more](/identity/verification-sessions#cancel)

No parameters.

Returns the canceled VerificationSession object

# Redact a VerificationSession

[Redact a VerificationSession](/api/identity/verification_sessions/redact)

Redact a VerificationSession to remove all collected information from Stripe. This will redact the VerificationSession and all objects related to it, including VerificationReports, Events, request logs, etc.

A VerificationSession object can be redacted when it is in requires_input or verified status. Redacting a VerificationSession in requires_action state will automatically cancel it.

[status](/identity/how-sessions-work)

The redaction process may take up to four days. When the redaction process is in progress, the VerificationSession’s redaction.status field will be set to processing; when the process is finished, it will change to redacted and an identity.verification_session.redacted event will be emitted.

Redaction is irreversible. Redacted objects are still accessible in the Stripe API, but all the fields that contain personal data will be replaced by the string [redacted] or a similar placeholder. The metadata field will also be erased. Redacted objects cannot be updated or used for any purpose.

Learn more.

[Learn more](/identity/verification-sessions#redact)

No parameters.

Returns the redacted VerificationSession object
