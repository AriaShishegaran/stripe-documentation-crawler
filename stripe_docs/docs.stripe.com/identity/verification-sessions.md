# The Verification Sessions API

Use the Verification Session API to securely collect information and perform verification checks. This API tracks a verification, from initial creation through the entire verification process, and shows verification results upon completion.

[Verification Session API](/api/identity/verification_sessions)

[verification checks](/identity/verification-checks)

For a step-by-step guide on using the Verification Session API to verify your users’ identity document, follow the related guide: Verify your users’ identity documents.

[Verify your users’ identity documents](/identity/verify-identity-documents)

## Creating a VerificationSession

When you create the VerificationSession, determine which verification check to perform by specifying the session type:

[create the VerificationSession](/api/identity/verification_sessions/create)

[verification check](/identity/verification-checks)

[type](/api/identity/verification_sessions/create#create_identity_verification_session-type)

- document - Verify the authenticity and ownership of government-issued identity documents. Can also include a selfie check.

[document](/identity/verification-checks?type=document)

[selfie check](/identity/selfie)

- id_number - Verify a user’s name, date of birth and national ID number.

[id_number](/identity/verification-checks?type=id-number)

If the verification process is interrupted and resumes later, attempt to reuse the same VerificationSession instead of creating a new one. Each VerificationSession has a unique ID that you can use to retrieve it. In your application’s data model, you can store the VerificationSession’s ID to facilitate retrieval.

[retrieve](/api/identity/verification_sessions/retrieve)

The benefit of reusing the VerificationSession is that the object helps track any failed verification attempts. If any of the checks fail, the VerificationSession will have a requires_input status.

We recommend that you provide an idempotency key when creating the VerificationSession to avoid erroneously creating duplicate VerificationSessions for the same person. This key is typically based on the ID that you associate with the verification in your application, like a user reference.

[idempotency key](/api/idempotent_requests)

## Passing the client secret to the frontend

The VerificationSession contains a client secret, a key that’s unique to the individual VerificationSession. The front end uses the client secret to complete the verification.

[client secret](/api/identity/verification_sessions/object#identity_verification_session_object-client_secret)

To use the client secret, you must obtain it from the VerificationSession on your server and pass it to the frontend. You can retrieve the client secret from an endpoint on your server using the browser’s fetch function on the client. This approach is generally most suitable when the client is a single-page application, especially one built with a modern frontend framework such as React.

This example shows how to create the server endpoint that serves the client secret:

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

This example demonstrates how to fetch the client secret with JavaScript on the client side:

The client secret is a sensitive token that you can use to complete the verification. Don’t log it, embed it in URLs, or expose it to anyone but the user that you’re verifying. Make sure that you have TLS on any page that includes the client secret.

[TLS](/security/guide#tls)

## Accessing verification results

Submitting and processing a VerificationSession updates the session status and creates a VerificationReport object. This normally happens within a few minutes.

[VerificationReport](/api/identity/verification_reports/object)

Once all of the verification checks have passed, the status changes to verified. You can expand the verified_outputs field to see the verified data.

[expand](/api/expanding_objects)

[verified_outputs](/api/identity/verification_sessions/object#identity_verification_session_object-verified_outputs)

If any of the verification checks fail, the session will have a requires_input status. Verification failure details are available in the session last_error hash. The last_error.code value can be used to programmatically handle common verification failures. The last_error.reason will contain a string that explains the failure reason and can be shown to your user.

[status](/identity/how-sessions-work)

[last_error](/api/identity/verification_sessions/object#identity_verification_session_object-last_error)

[last_error.code](/api/identity/verification_sessions/object#identity_verification_session_object-last_error-code)

[last_error.reason](/api/identity/verification_sessions/object#identity_verification_session_object-last_error-code)

If you want your user to attempt verification again, you’ll need to Retrieve the VerificationSession to get a fresh URL or client secret to pass to your client.

[Retrieve the VerificationSession](/api/identity/verification_sessions/retrieve)

Learn how to access sensitive verification results

[access sensitive verification results](/identity/access-verification-results)

## Cancelling a VerificationSession

You can cancel a VerificationSession at any point before it’s processing or verified. This invalidates the VerificationSession for future submission attempts, and can’t be undone. The session will have a canceled status.

[status](/identity/how-sessions-work)

## Redacting a VerificationSession

One of the reasons that you might want to redact a verification session is if you receive a data deletion request from your user. You can redact a session to ensure collected information is no longer returned by the Stripe API or visible in Dashboard. You can still retrieve redacted sessions with the API but you can’t update them. Sessions can be redacted from the Dashboard or through the API:

[retrieve](/api/identity/verification_sessions/retrieve)

Redacted sessions show placeholder values for all fields that previously contained personally identifiable information (PII). The session includes a redaction.status field indicating the status of the redaction process. An identity.verification_session.redacted webhook will be sent when the session is redacted. Please note redaction can take up to 4 days.

[redaction.status](/api/identity/verification_sessions/object#identity_verification_session_object-redaction-status)

[identity.verification_session.redacted](/api/events/types#event_types-identity.verification_session.redacted)

If a VerificationSession that has been redacted is retrieved with PII fields expanded, then these fields will still appear in the response but their values will not contain any PII. For example, here is a response that has expanded the verified_outputs and verified_outputs.dob fields on a redacted VerificationSession.

Any VerificationReports, Events, and Request Logs associated with the VerificationSession are also redacted and File contents are no longer downloadable.

[VerificationReports](/api/identity/verification_reports)

[Events](/api/events)

[Request Logs](https://dashboard.stripe.com/logs)

[File](/api/files)

If the VerificationSession is in the processing state you must wait until it finishes before redacting it. Redacting a VerificationSession with requires_action status automatically cancels it.

## Storing information in metadata

Stripe supports adding metadata to the VerificationSession object. Metadata isn’t shown to customers or factored into whether a verification check succeeds or fails.

[metadata](/api#metadata)

Through metadata, you can associate other information—meaningful to you—with Stripe activity. Any metadata you include is viewable in the Dashboard (for example, when looking at the page for an individual session), and is also available in common reports. As an example, you can attach your application’s user ID to the VerificationSession used to verify that user. Doing so allows you, or your team to easily reconcile verifications in Stripe to users in your system.

We recommend you don’t store any sensitive information (PII, ID numbers, and so on) in session metadata. Note that metadata is removed when you redact a VerificationSession.

## See also

- How sessions work

[How sessions work](/identity/how-sessions-work)

- Verify your users’ identity documents

[Verify your users’ identity documents](/identity/verify-identity-documents)
