# Adding selfie checks

While document checks provide a defense against the use of fraudulent identity documents, it’s possible for fraudsters to get access to legitimate stolen documents. To prevent this, Stripe Identity can perform selfie checks on your users.

[document checks](/identity/verification-checks?type=document)

Selfie checks look for distinguishing biological traits, such as face geometry, from a photo ID and a picture of your user’s face. Stripe then uses advanced machine learning algorithms to ensure the face pictures belong to the same person.

To add selfie checks to your application, first follow the guide to collect and verify identity documents.

[collect and verify identity documents](/identity/verify-identity-documents)

## Adding selfie checks to VerificationSessions

When creating a VerificationSession, use the options.document.require_matching_selfie parameter to enable selfie checks.

[creating a VerificationSession](/api/identity/verification_sessions/create)

[options.document.require_matching_selfie](/api/identity/verification_sessions/create#create_identity_verification_session-options-document-require_matching_selfie)

This configures the verification flow to require a photo ID and a face picture from your user.

## Accessing selfie check results

After it’s submitted and processed, the VerificationSession status changes depending on the result of the checks:

[status](/identity/how-sessions-work)

- verified — Both the document and selfie checks were successful. The session verified_outputs contains extracted information from the document.

[verified_outputs](/api/identity/verification_sessions/object#identity_verification_session_object-verified_outputs)

- requires_input — At least one of the document or the selfie checks failed.

To access the captured selfie and document images, you’ll need to retrieve the associated VerificationReport, you can do this by expanding the last_verification_report field in the session:

[VerificationReport](/api/identity/verification_reports)

[expanding](/api/expanding_objects)

[last_verification_report](/api/identity/verification_sessions/object#identity_verification_session_object-last_verification_report)

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

The VerificationReport has document and selfie fields holding the results of the document and selfie checks. Here’s an example VerificationReport with successful document and selfie checks:

[document](/api/identity/verification_reports/object#identity_verification_report_object-document)

[selfie](/api/identity/verification_reports/object#identity_verification_report_object-selfie)

To access the collected document and face images, see Accessing verification results.

[Accessing verification results](/identity/access-verification-results)

## Understanding selfie check failures

The document and selfie VerificationReport fields contain the collected data as well as a status and error fields to help you understand whether the check is successful or not.

[document](/api/identity/verification_reports/object#identity_verification_report_object-document)

[selfie](/api/identity/verification_reports/object#identity_verification_report_object-selfie)

The status field tells you whether each check is successful or not. The possible values are:

- verified - The verification check is successful and the collected data is verified.

- unverified - The verification check failed. You can check the error hash for more information.

When the verification check fails, the error field contains code and reason values to explain the verification failure. The error.code field can be used to programmatically handle verification failures. The reason field contains a descriptive message explaining the failure reason and can be shown to your user.

Failure details are available in the report document.error field.

[document.error](/api/identity/verification_reports/object#identity_verification_report_object-document-error)

[See list of supported document types](/identity/verification-checks?type=document)

[allowed document types](/api/identity/verification_sessions/create#create_identity_verification_session-options-document-allow_document_types)

Failure details are available in the report selfie.error field.

[selfie.error](/api/identity/verification_reports/object#identity_verification_report_object-selfie-error)

## See also

- Verify your users’ identity documents

[Verify your users’ identity documents](/identity/verify-identity-documents)

- The Verification Sessions API

[The Verification Sessions API](/identity/verification-sessions#create)
