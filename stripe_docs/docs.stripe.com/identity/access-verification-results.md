# Access verification results

You wrote code to display a modal to collect identity documents and handle verification outcomes. Now you might need access to the sensitive verification results such as your user’s date of birth or pictures of the collected document.

[display a modal to collect identity documents](/identity/verify-identity-documents)

[handle verification outcomes](/identity/handle-verification-outcomes)

First, consider using the Identity Dashboard to access sensitive verification results. If needed, give team members controlled access to your Stripe account. This saves you development time and ensures the sensitive verification data is kept securely on Stripe.

[Identity Dashboard](https://dashboard.stripe.com/identity)

[give team members controlled access](/get-started/account/teams)

[securely](https://support.stripe.com/questions/managing-your-id-verification-information)

You can access most verification details programmatically, such as the result of a verification check or the user’s name and address using your secret key. Access to more sensitive fields require the use of restricted API keys.

[access most verification details programmatically](/identity/verification-sessions#results)

[secret key](/keys)

[restricted API keys](/keys#limit-access)

Restricted API keys allow access based on the security measures associated with it:

- Restricted keys — Allow access to sensitive verification results for verifications processed in the last 48 hours.

- IP restricted keys - Allow access to sensitive verification results for all verifications.

In this guide, you’ll learn how to:

- Consider your sensitive data access requirements carefully.

- Create restricted API keys.

- Make API requests to obtain sensitive verification results.

- Roll your keys if they’re compromised.

- Communicate your sensitive verification results and security measures to your users.

- Add IP restrictions to your key for long-term access to sensitive verification results.

- Consider your sensitive data access requirements carefully.

- Create restricted API keys.

- Make API requests to obtain sensitive verification results.

- Roll your keys if they’re compromised.

- Communicate your sensitive verification results and security measures to your users.

[Consider your sensitive data access requirements carefully](#decide-access-requirements)

## Consider your sensitive data access requirements carefully

To build an integration with Stripe Identity that prioritizes your user’s privacy, you must first decide the minimum amount of PII that you need access to.  If you don’t need access to the most sensitive data (that requires authentication with a restricted API key), then your integration can authenticate using your secret key only.

To access PII resulting from a verification, you can retrieve a VerificationSession and expand either the verified_outputs field or - if you need more granular detail on the verification result - the last_verification_report.  Expanding either of these fields automatically includes all of the PII fields they contain that only require a secret key.

[expand](/api/expanding_objects)

[verified_outputs](/api/identity/verification_sessions/object#identity_verification_session_object-verified_outputs)

[last_verification_report](/api/identity/verification_sessions/object#identity_verification_session_object-last_verification_report)

Here is an example of how to expand the verified_outputs field to retrieve a user’s name that was verified by Stripe Identity.

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

If you do need to access sensitive PII that requires a restricted key, follow the steps in this guide.

[Create a restricted API keyDashboard](#create-restricted-key)

## Create a restricted API keyDashboard

You can use your account’s secret API keys to perform any API request without restriction. Accessing sensitive verification results requires restricted keys, which are more secure.

[restricted keys](/keys#limit-access)

To create a new restricted key,

- Go to the API keys page in the Dashboard and click Create restricted key.

[API keys page](https://dashboard.stripe.com/apikeys)

[Create restricted key](https://dashboard.stripe.com/apikeys/create)

- Name your key.

- Make sure the Identity Verification Sessions and Reports and Access recent sensitive verification results permissions are set to Read.

- (optional) If you need to access collected images, add the Files Write permission.

- Click Create key.

- Store the key securely. Learn more about keeping your keys safe.

[Learn more about keeping your keys safe](/keys#safe-keys)

[Make API requests to obtain sensitive verification resultsServer-side](#api-request)

## Make API requests to obtain sensitive verification resultsServer-side

VerificationReports contain all the collected data and verification results from a submitted session. VerificationReports are created when all verification checks for a session are processed. They allow you to understand why a verification check failed and what data was successfully verified.

[VerificationReports](/api/identity/verification_reports)

You can expand the last_verification_report session field to retrieve the associated VerificationReport.

[expand](/expand)

[last_verification_report](/api/identity/verification_sessions/object#identity_verification_session_object-last_verification_report)

By default, VerificationReports don’t include sensitive verification results. To access these, you’ll need to:

- Authenticate using the restricted API key created in step 1.

- Expand the fields you want to access.

[Expand](/api/expanding_objects)

Here’s an example of accessing the extracted date of birth, ID number, and document number from a document check:

[document check](/identity/verification-checks?type=document)

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

## Accessing collected images

You can retrieve identity document and face images that you collect as part of a session using the File Upload API. The following fields on a VerificationReport can hold a reference to a File resource in the Stripe API:

[File Upload API](/file-upload)

[File](/api/files)

- document.files - images of the identity document

[document.files](/api/identity/verification_reports/object#identity_verification_report_object-document-front)

- selfie.document - image of the photo ID front

[selfie.document](/api/identity/verification_reports/object#identity_verification_report_object-selfie-document)

- selfie.selfie - image of the user’s face

[selfie.selfie](/api/identity/verification_reports/object#identity_verification_report_object-selfie-selfie)

Document and face images are very sensitive and some countries, such as Germany, have laws prohibiting ID Document images from being shared or kept longer than necessary. As much as possible, access image content with short-lived FileLinks, don’t make copies of the file contents, and redact sessions and collected images when you’re done using them for the purpose collected.

[redact sessions](/identity/verification-sessions#redact)

To access the contents of the file, you need to authenticate using the previously created restricted key and Create a FileLink with a short expiration and send the url to the client:

[Create a FileLink](/api/file_links/create)

[url](/api/file_links/object#file_link_object-url)

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

FileLinks for document and selfie files must expire within 30 seconds. We recommend not downloading the file contents on your server, instead send the FileLink URL to the client to display the image.

If you believe an attacker has accessed sensitive data collected by Identity, please reach out to support.

[reach out to support](https://support.stripe.com/contact)

[Roll your keys if they’re compromisedDashboard](#roll-keys)

## Roll your keys if they’re compromisedDashboard

Using restricted API keys that only have Identity permissions allows you to roll the keys in case of emergency without affecting other Stripe product integrations.

We recommend that you regularly monitor your restricted key usage to ensure that no one has gained access to them. In the Dashboard, you can use the overflow menu (…) to view request logs for a specific API key to view all the requests made from that key.

[Dashboard](https://dashboard.stripe.com/apikeys)

If an API key is compromised, roll the key in the Dashboard to block it and generate a new one. Make sure to expire it immediately to prevent bad actors from retrieving sensitive information.

[Dashboard](https://dashboard.stripe.com/apikeys)

Rolling blocks the API key and generates a new one. We recommend reviewing your security history for events related to this key. Any webhook endpoints created with this key will stay active, even after the key is rolled.

[security history](https://dashboard.stripe.com/security_history)

If you believe an attacker has accessed sensitive data collected by Identity, please reach out to support.

[reach out to support](https://support.stripe.com/contact)

[Communicate your sensitive data use and security measures](#tell-users)

## Communicate your sensitive data use and security measures

Make sure your privacy policy includes information on your use of sensitive verification results. It may also help if you provide information about your security practices.

See also

- Privacy considerations for handling ID verification data as a business

[Privacy considerations for handling ID verification data as a business](https://support.stripe.com/questions/privacy-considerations-for-handling-id-verification-data-as-a-business)

- FAQs to provide to your users

[FAQs to provide to your users](/identity/explaining-identity)

[OptionalAdd IP restrictions for long-term access to resultsDashboard](#ip-allowlist)

## OptionalAdd IP restrictions for long-term access to resultsDashboard

## See also

- Expanding responses

[Expanding responses](/api/expanding_objects)

- API Keys

[API Keys](/keys)

- Security at Stripe

[Security at Stripe](/security)
