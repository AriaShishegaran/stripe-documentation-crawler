htmlVerify your users’ identity documents | Stripe Documentation[Skip to content](#main-content)Verify identity documents[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fidentity%2Fverify-identity-documents)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fidentity%2Fverify-identity-documents)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)[Verify identities](#)
NetherlandsEnglish (United States)[](#)[](#)[Identity](/identity)·[Home](/docs)[Get started](/docs/get-started)[Verify identities](/docs/identity)# Verify your users’ identity documents

Create sessions and collect identity documents.This guide explains how to use Stripe Identity to securely collect and verify identity documents.

## Before you begin

1. [Activate your account](https://dashboard.stripe.com/account/onboarding).
2. Fill out your[Stripe Identity application](https://dashboard.stripe.com/identity/application).
3. (Optional) Customize your brand settings on the[branding settings page](https://dashboard.stripe.com/settings/branding).



WebiOSAndroidReact NativeNo codeModalRedirectShow a document upload modal inside your website. Here’s what you’ll do:

1. Add a verification button to your webpage that displays a document upload modal.
2. Display a confirmation page on identity document submission.
3. Handle verification results.

[Set up StripeServer-side](#set-up-stripe)First, register for a Stripe account.

Then install the libraries for access to the Stripe API from your application:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`[Add a button to your websiteClient-side](#add-a-button)Create a button on your website for starting the verification.

HTML + JSReact### Add a button

Start by adding a verify button to your page:

verification.html`<html>
  <head>
    <title>Verify your identity</title>
  </head>
  <body>
    <button id="verify-button">Verify</button>
  </body>
</html>`### Add the Stripe.js library to your page

Add Stripe.js to your page by including a script tag in your HTML document:

verification.html`<html>
  <head>
    <title>Verify your identity</title>
    <script src="https://js.stripe.com/v3/"></script>
  </head>
  <body>
    <button id="verify-button">Verify</button>
  </body>
</html>`NoteAlways load Stripe.js directly from https://js.stripe.com. You can’t include it in a bundle or self-host it.

### Initialize Stripe.js

Initialize Stripe.js with your publishable API key by passing the following JavaScript to your page:

verification.html`<html>
  <head>
    <title>Verify your identity</title>
    <script src="https://js.stripe.com/v3/"></script>
  </head>
  <body>
    <button id="verify-button">Verify</button>
    <script type="text/javascript">
      // Set your publishable key: remember to change this to your live publishable key in production
      // See your keys here: https://dashboard.stripe.com/apikeys
      var stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');
    </script>
  </body>
</html>`[Show the document upload modalClient-sideServer-side](#show-modal)Set up the new button to show a document upload modal. After clicking the button, your user can capture and upload a picture of their passport, driver’s license, or national ID.

The modal reduces development time and maintenance and allows you to collect identity documents as part of your existing flows. It also decreases the amount of private information you handle on your site, allows you to support users in a variety of platforms and languages, and allows you to customize the style to match your branding.

### Create a VerificationSession

A VerificationSession is the programmatic representation of the verification. It contains details about the type of verification, such as what check to perform. You can expand the verified outputs field to see details of the data that was verified.

After successfully creating a VerificationSession, send the client secret to the frontend to show the document upload modal.

![](https://b.stripecdn.com/docs-statics-srv/assets/modal_integration_diagram.4c9ef035ee7fcb8b8f58a99fcad27202.svg)

You need a server-side endpoint to create the VerificationSession. Creating the VerificationSession server-side prevents malicious users from overriding verification options and incurring processing charges on your account. Add authentication to this endpoint by including a user reference in the session metadata or storing the session ID in your database.

server.js[Node](#)`// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz');

// In the route handler for /create-verification-session:
// Authenticate your user.

// Create the session.
const verificationSession = await stripe.identity.verificationSessions.create({
  type: 'document',
  metadata: {
    user_id: '{{USER_ID}}',
  },
});

// Return only the client secret to the frontend.
const clientSecret = verificationSession.client_secret;`CautionThe client secret lets your frontend collect sensitive verification information. It’s single-use and expires after 24 hours. Don’t store it, log it, embed it in a URL, or expose it to anyone other than the user. Make sure that you have TLS enabled on any page that includes the client secret. Send only the client secret to your frontend to avoid exposing verification configuration or results.

Test your endpoint by starting your web server (for example, localhost:4242) and sending a POST request with curl to create a VerificationSession:

Command Line`curl -X POST -is "http://localhost:4242/create-verification-session" -d ""`The response in your terminal looks like this:

Command Line`HTTP/1.1 200 OK
Content-Type: application/json

{ client_secret: "vs_QdfQQ6xfGNJR7ogV6..."  }`### Add an event handler to the verify button

Now that you have a button and an endpoint to create a VerificationSession, modify the button to show the document upload modal when clicked. Add a call to verifyIdentity using the client secret:

HTML + JSReactverification.html`<html>
  <head>
    <title>Verify your identity</title>
    <script src="https://js.stripe.com/v3/"></script>
  </head>
  <body>
    <button id="verify-button">Verify</button>

    <script type="text/javascript">
      // Set your publishable key: remember to change this to your live publishable key in production
      // See your keys here: https://dashboard.stripe.com/apikeys
      var stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');

      var verifyButton = document.getElementById('verify-button');

      verifyButton.addEventListener('click', function() {
        // Get the VerificationSession client secret using the server-side
        // endpoint you created in step 3.
        fetch('/create-verification-session', {
          method: 'POST',
        })
        .then(function(response) {
          return response.json();
        })
        .then(function(session) {
          // Show the verification modal.
          return stripe.verifyIdentity(session.client_secret);
        })
        .then(function(result) {
          // If `verifyIdentity` fails, you should display the localized
          // error message to your user using `error.message`.
          if (result.error) {
            alert(result.error.message);
          }
        })
        .catch(function(error) {
          console.error('Error:', error);
        });
      });
    </script>
  </body>
</html>`### Event error codes

Error codeDescription`consent_declined`The user declined verification by Stripe. Check with your legal counsel to see if you have an obligation to offer an alternative, non-biometric means to verify, such as through a manual review.`device_unsupported`The verification requires a camera and the user is on a device without one.`under_supported_age`Stripe doesn’t verify users under the age of majority.### Test the upload modal

Test that the verify button shows a document upload modal:

- Click the verify button, which opens the Stripe document upload modal.
- Ensure no error messages are shown.

If your integration isn’t working:

1. Open the Network tab in your browser’s developer tools.
2. Click the verify button to see if it makes an XHR request to your server-side endpoint (`POST /create-verification-session`).
3. Verify that the request returns a 200 status.
4. Use`console.log(session)`inside your button click listener to confirm that it returns the correct data.

[Show a confirmation pageClient-side](#show-confirmation-page)To provide a user-friendly experience, show a confirmation page after users successfully submit their identity document. Host the page on your site to let the user know that the verification is processing.

HTML + JSReactCreate a minimal confirmation page:

submitted.html`<html>
  <head><title>Your document was submitted</title></head>
  <body>
    <h1>Thanks for submitting your identity document.</h1>
    <p>
      We are processing your verification.
    </p>
  </body>
</html>`Next, update the button handler to redirect to this page:

verification.html`<html>
  <head>
    <title>Verify your identity</title>
    <script src="https://js.stripe.com/v3/"></script>
  </head>
  <body>
    <button id="verify-button">Verify</button>

    <script type="text/javascript">
      // Set your publishable key: remember to change this to your live publishable key in production
      // See your keys here: https://dashboard.stripe.com/apikeys
      var stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY')

      var verifyButton = document.getElementById('verify-button');

      verifyButton.addEventListener('click', function() {
        // Get the VerificationSession client secret using the server-side
        // endpoint you created in step 3.
        fetch('/create-verification-session', {
          method: 'POST',
        })
        .then(function(response) {
          return response.json();
        })
        .then(function(session) {
          // Show the verification modal.
          return stripe.verifyIdentity(session.client_secret);
        })
        .then(function(result) {
          // If `verifyIdentity` fails, you should display the error message
          // using `error.message`.
          if (result.error) {
            alert(result.error.message);
          } else {
            window.location.href = 'submitted.html';
          }
        })
        .catch(function(error) {
          console.error('Error:', error);
        });
      });
    </script>
  </body>
</html>`### Test the confirmation page

Test that your confirmation page works:

- Click your verify button.
- Submit the session by selecting a predefined test case.
- Confirm that the new confirmation page is shown.
- Test the entire flow for failure cases (such as declining consent or refusing camera permissions) and ensure your app handles them without any issues.

Next, find the verification in the Stripe Dashboard. Verification sessions appear in the Dashboard’s list of VerificationSessions. Click a session to go to the Session Detail page. The summary section contains verification results, which you can use in your app.

[Handle verification events](#handle-verification-events)Document checks are asynchronous, which means that verification results are not immediately available. An identity document check typically takes 1 to 3 minutes to complete. After the processing completes, the VerificationSession status changes from processing to verified.

Stripe sends the following events when the session status changes:

Event nameDescriptionNext steps[identity.verification_session.verified](/api/events/types#event_types-identity.verification_session.verified)Processing of all the[verification checks](/identity/verification-checks)have completed, and they’re all successfully verified.Trigger relevant actions in your application.[identity.verification_session.requires_input](/api/events/types#event_types-identity.verification_session.requires_input)Processing of all the[verification checks](/identity/verification-checks)have completed, and at least one of the checks failed.Trigger relevant actions in your application and potentially allow your user to retry the verification.Use a webhook handler to receive these events and automate actions like sending a confirmation email, updating the verification results in your database, or completing an onboarding step. You can also view verification events in the Dashboard.

## Receive events and run business actions

### With code

Build a webhook handler to listen for events and build custom asynchronous verification flows. Test and debug your webhook integration locally with the Stripe CLI.

Build a custom webhook

### Without code

Use the Dashboard to view all your verifications, inspect collected data, and understand verification failures.

View your test verifications in the Dashboard

## See also

- [Handle verification outcomes](/identity/handle-verification-outcomes)
- [Learn about VerificationSessions](/identity/verification-sessions)
- [Learn about Stripe.js](/payments/elements)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Set up Stripe](#set-up-stripe)[Add a button to your website](#add-a-button)[Show the document upload modal](#show-modal)[Show a confirmation page](#show-confirmation-page)[Handle verification events](#handle-verification-events)[Receive events and run business actions](#receive-events-and-run-business-actions)[See also](#see-also)Products Used[Identity](/identity)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`