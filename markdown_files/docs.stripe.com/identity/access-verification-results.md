htmlAccess verification results | Stripe Documentation[Skip to content](#main-content)Access verification results[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fidentity%2Faccess-verification-results)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fidentity%2Faccess-verification-results)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)[Verify identities](#)
NetherlandsEnglish (United States)[](#)[](#)[Identity](/identity)·[Home](/docs)[Get started](/docs/get-started)[Verify identities](/docs/identity)# Access verification results

Learn how to access sensitive verification results.You wrote code to display a modal to collect identity documents and handle verification outcomes. Now you might need access to the sensitive verification results such as your user’s date of birth or pictures of the collected document.

First, consider using the Identity Dashboard to access sensitive verification results. If needed, give team members controlled access to your Stripe account. This saves you development time and ensures the sensitive verification data is kept securely on Stripe.

You can access most verification details programmatically, such as the result of a verification check or the user’s name and address using your secret key. Access to more sensitive fields require the use of restricted API keys.

Verification resultAvailable in DashboardSecret key accessRestricted API key accessAddressDocument typeFirst and last namesIssuing country of the documentResult of the verification checkIssued date of the documentType of ID numberExpiration date of the documentDate of birthDocument ID numberDocument imagesFace imagesID numberRestricted API keys allow access based on the security measures associated with it:

- Restricted keys— Allow access to sensitive verification results for verifications processed in the last 48 hours.
- IP restricted keys- Allow access to sensitive verification results for all verifications.

In this guide, you’ll learn how to:

1. Consider your sensitive data access requirements carefully.
2. Create restricted API keys.
3. Make API requests to obtain sensitive verification results.
4. Roll your keys if they’re compromised.
5. Communicate your sensitive verification results and security measures to your users.
6. Add IP restrictions to your key for long-term access to sensitive verification results.

1. Consider your sensitive data access requirements carefully.
2. Create restricted API keys.
3. Make API requests to obtain sensitive verification results.
4. Roll your keys if they’re compromised.
5. Communicate your sensitive verification results and security measures to your users.

[Consider your sensitive data access requirements carefully](#decide-access-requirements)To build an integration with Stripe Identity that prioritizes your user’s privacy, you must first decide the minimum amount of PII that you need access to.  If you don’t need access to the most sensitive data (that requires authentication with a restricted API key), then your integration can authenticate using your secret key only.

To access PII resulting from a verification, you can retrieve a VerificationSession and expand either the verified_outputs field or - if you need more granular detail on the verification result - the last_verification_report.  Expanding either of these fields automatically includes all of the PII fields they contain that only require a secret key.

Here is an example of how to expand the verified_outputs field to retrieve a user’s name that was verified by Stripe Identity.

server.js[Node](#)`// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz');

const verificationSession = await stripe.identity.verificationSessions.retrieve(
  '{{SESSION_ID}}',
  {
    expand: [
      'verified_outputs',
    ],
  }
);

const firstName = verificationSession.verified_outputs.first_name;`If you do need to access sensitive PII that requires a restricted key, follow the steps in this guide.

[Create a restricted API keyDashboard](#create-restricted-key)You can use your account’s secret API keys to perform any API request without restriction. Accessing sensitive verification results requires restricted keys, which are more secure.

To create a new restricted key,

1. Go to the[API keys page](https://dashboard.stripe.com/apikeys)in the Dashboard and click[Create restricted key](https://dashboard.stripe.com/apikeys/create).
2. Name your key.
3. Make sure the IdentityVerification Sessions and ReportsandAccess recent sensitive verification resultspermissions are set toRead.
4. (optional) If you need to access collected images, add the FilesWritepermission.
5. ClickCreate key.
6. Store the key securely.[Learn more about keeping your keys safe](/keys#safe-keys).

![](https://b.stripecdn.com/docs-statics-srv/assets/rak_identity_permissions.51347778adedec20ad9aaec2cb5a5bb9.png)

[Make API requests to obtain sensitive verification resultsServer-side](#api-request)VerificationReports contain all the collected data and verification results from a submitted session. VerificationReports are created when all verification checks for a session are processed. They allow you to understand why a verification check failed and what data was successfully verified.

You can expand the last_verification_report session field to retrieve the associated VerificationReport.

By default, VerificationReports don’t include sensitive verification results. To access these, you’ll need to:

1. Authenticate using the restricted API key created in step 1.
2. [Expand](/api/expanding_objects)the fields you want to access.

Here’s an example of accessing the extracted date of birth, ID number, and document number from a document check:

server.js[Node](#)`// Set your restricted key. Remember to switch to a live restricted key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('rk_test_...');

const verificationSession = await stripe.identity.verificationSessions.retrieve(
  '{{SESSION_ID}}',
  {
    expand: [
      'verified_outputs.dob',
      'verified_outputs.id_number',
      'last_verification_report.document.number',
    ],
  }
);

const dateOfBirth = verificationSession.verified_outputs.dob;
const idNumber = verificationSession.verified_outputs.id_number;
const documentNumber = verificationSession.last_verification_report.document.number;`## Accessing collected images

You can retrieve identity document and face images that you collect as part of a session using the File Upload API. The following fields on a VerificationReport can hold a reference to a File resource in the Stripe API:

- [document.files](/api/identity/verification_reports/object#identity_verification_report_object-document-front)- images of the identity document
- [selfie.document](/api/identity/verification_reports/object#identity_verification_report_object-selfie-document)- image of the photo ID front
- [selfie.selfie](/api/identity/verification_reports/object#identity_verification_report_object-selfie-selfie)- image of the user’s face

NoteDocument and face images are very sensitive and some countries, such as Germany, have laws prohibiting ID Document images from being shared or kept longer than necessary. As much as possible, access image content with short-lived FileLinks, don’t make copies of the file contents, and redact sessions and collected images when you’re done using them for the purpose collected.

To access the contents of the file, you need to authenticate using the previously created restricted key and Create a FileLink with a short expiration and send the url to the client:

server.js[Node](#)`// Set your restricted key. Remember to switch to a live restricted key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('rk_test_...');

// Get the VerificationReport
const session = await stripe.identity.verificationSessions.retrieve(
  '{{SESSION_ID}}',
  {
    expand: ['last_verification_report'],
  }
);

// Retrieve the File id
const report = session.last_verification_report;
const documentFrontFile = report.document.files[0];

// Create a short-lived FileLink
const fileLink = await stripe.fileLinks.create({
  file: documentFrontFile,
  expires_at: Math.floor(Date.now() / 1000) + 30,  // link expires in 30 seconds
});

// Access the FileLink URL to download file contents
const fileUrl = fileLink.url;`NoteFileLinks for document and selfie files must expire within 30 seconds. We recommend not downloading the file contents on your server, instead send the FileLink URL to the client to display the image.

If you believe an attacker has accessed sensitive data collected by Identity, please reach out to support.

[Roll your keys if they’re compromisedDashboard](#roll-keys)Using restricted API keys that only have Identity permissions allows you to roll the keys in case of emergency without affecting other Stripe product integrations.

We recommend that you regularly monitor your restricted key usage to ensure that no one has gained access to them. In the Dashboard, you can use the overflow menu (…) to view request logs for a specific API key to view all the requests made from that key.

If an API key is compromised, roll the key in the Dashboard to block it and generate a new one. Make sure to expire it immediately to prevent bad actors from retrieving sensitive information.

WarningRolling blocks the API key and generates a new one. We recommend reviewing your security history for events related to this key. Any webhook endpoints created with this key will stay active, even after the key is rolled.

If you believe an attacker has accessed sensitive data collected by Identity, please reach out to support.

[Communicate your sensitive data use and security measures](#tell-users)Make sure your privacy policy includes information on your use of sensitive verification results. It may also help if you provide information about your security practices.

See also

- [Privacy considerations for handling ID verification data as a business](https://support.stripe.com/questions/privacy-considerations-for-handling-id-verification-data-as-a-business)
- [FAQs to provide to your users](/identity/explaining-identity)

[OptionalAdd IP restrictions for long-term access to resultsDashboard](#ip-allowlist)## See also

- [Expanding responses](/api/expanding_objects)
- [API Keys](/keys)
- [Security at Stripe](/security)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Consider your sensitive data access requirements carefully](#decide-access-requirements)[Create a restricted API key](#create-restricted-key)[Make API requests to obtain sensitive verification results](#api-request)[Accessing collected images](#images)[Roll your keys if they’re compromised](#roll-keys)[Communicate your sensitive data use and security measures](#tell-users)[See also](#see-also)Products Used[Identity](/identity)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`