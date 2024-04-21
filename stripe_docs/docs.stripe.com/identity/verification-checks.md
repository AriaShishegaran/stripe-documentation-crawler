# Verification checks

This page is about Stripe Identity verification checks, to learn more about Connect identity verification, please visit Handling verification with the API. If you’re trying to verify your identity as part of getting started with your Stripe account, please visit this page.

[Stripe Identity](/identity)

[Connect](/connect)

[Handling verification with the API](/connect/handling-api-verification)

[this page](https://support.stripe.com/questions/passport-id-or-drivers-license-upload-requirement)

Stripe Identity currently supports five types of verification checks: document, selfie, ID number, address, and phone.

Each verification check requires different information from your user, has different coverage, and has a different verification flow. After you’ve integrated one check, you can add another with minimal changes to your integration.

Document checks verify the authenticity of government-issued identity documents. Stripe uses a combination of machine learning models, automated heuristic analysis and manual reviewers to verify the authenticity of hundreds of different document types.

Machine learning models are used to capture high-definition pictures of the fronts and backs of documents. The document images are analyzed in real-time to check for legibility and warn the user if the document is expired or unlikely to be verified. Stripe checks the images against a database of fraudulent document templates. This database is updated frequently, so that Stripe can detect new fake document templates and automatically block them.

Wherever available, barcodes and other machine-readable features of the document are decoded and consistency checks are performed to ensure that the text document data matches the machine-readable data.

To prevent “presentation attacks” — fraudster using pictures of stolen documents or someone else’s face, Stripe uses computer vision and machine learning algorithms to ensure the user captured an image of an actual document.

See the Verify your users’ identity documents guide to learn how to integrate document checks into your app.

[Verify your users’ identity documents](/identity/verify-identity-documents)

Additionally, document checks can also be paired with ID number checks. This ensures the authenticity of the document and ensure the information in it can be cross-referenced in third party databases.

[paired with ID number checks](/api/identity/verification_sessions/create#create_identity_verification_session-options-document-require_id_number)

Document checks are available for most government issued documents (national IDs, driver’s licenses and passports) from the following countries:

Acceptable identity documents vary by country, however, passports are widely supported.

Stripe doesn’t support extraction of document fields written in Arabic, Chinese, Cyrillic, Greek, Hebrew, Korean, Tamil, or Thai script.

## See also

- Verify your users’ identity documents

[Verify your users’ identity documents](/identity/verify-identity-documents)

- Adding selfie checks

[Adding selfie checks](/identity/selfie)

- The Verification Sessions API

[The Verification Sessions API](/identity/verification-sessions#create)
