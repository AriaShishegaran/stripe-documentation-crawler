# Verify your users’ identity documents

This guide explains how to use Stripe Identity to securely collect and verify identity documents.

## Before you begin

- Activate your account.

[Activate your account](https://dashboard.stripe.com/account/onboarding)

- Fill out your Stripe Identity application.

[Stripe Identity application](https://dashboard.stripe.com/identity/application)

- (Optional) Customize your brand settings on the branding settings page.

[branding settings page](https://dashboard.stripe.com/settings/branding)



Show a document upload modal inside your website. Here’s what you’ll do:

- Add a verification button to your webpage that displays a document upload modal.

- Display a confirmation page on identity document submission.

- Handle verification results.

[Set up StripeServer-side](#set-up-stripe)

## Set up StripeServer-side

First, register for a Stripe account.

[register](https://dashboard.stripe.com/register)

Then install the libraries for access to the Stripe API from your application:

[Add a button to your websiteClient-side](#add-a-button)

## Add a button to your websiteClient-side

Create a button on your website for starting the verification.

Start by adding a verify button to your page:

Add Stripe.js to your page by including a script tag in your HTML document:

[Stripe.js](/payments/elements)

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

Always load Stripe.js directly from https://js.stripe.com. You can’t include it in a bundle or self-host it.

Initialize Stripe.js with your publishable API key by passing the following JavaScript to your page:

[API key](/keys)

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

[Show the document upload modalClient-sideServer-side](#show-modal)

## Show the document upload modalClient-sideServer-side

Set up the new button to show a document upload modal. After clicking the button, your user can capture and upload a picture of their passport, driver’s license, or national ID.

The modal reduces development time and maintenance and allows you to collect identity documents as part of your existing flows. It also decreases the amount of private information you handle on your site, allows you to support users in a variety of platforms and languages, and allows you to customize the style to match your branding.

A VerificationSession is the programmatic representation of the verification. It contains details about the type of verification, such as what check to perform. You can expand the verified outputs field to see details of the data that was verified.

[VerificationSession](/api/identity/verification_sessions)

[check](/identity/verification-checks)

[expand](/api/expanding_objects)

[verified outputs](/api/identity/verification_sessions/object#identity_verification_session_object-verified_outputs)

After successfully creating a VerificationSession, send the client secret to the frontend to show the document upload modal.

[client secret](/api/identity/verification_sessions/object#identity_verification_session_object-client_secret)

You need a server-side endpoint to create the VerificationSession. Creating the VerificationSession server-side prevents malicious users from overriding verification options and incurring processing charges on your account. Add authentication to this endpoint by including a user reference in the session metadata or storing the session ID in your database.

[create the VerificationSession](/api/identity/verification_sessions/create)

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

The client secret lets your frontend collect sensitive verification information. It’s single-use and expires after 24 hours. Don’t store it, log it, embed it in a URL, or expose it to anyone other than the user. Make sure that you have TLS enabled on any page that includes the client secret. Send only the client secret to your frontend to avoid exposing verification configuration or results.

Test your endpoint by starting your web server (for example, localhost:4242) and sending a POST request with curl to create a VerificationSession:

The response in your terminal looks like this:

Now that you have a button and an endpoint to create a VerificationSession, modify the button to show the document upload modal when clicked. Add a call to verifyIdentity using the client secret:

[verifyIdentity](/js/identity/modal)

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

Test that the verify button shows a document upload modal:

- Click the verify button, which opens the Stripe document upload modal.

- Ensure no error messages are shown.

If your integration isn’t working:

- Open the Network tab in your browser’s developer tools.

- Click the verify button to see if it makes an XHR request to your server-side endpoint (POST /create-verification-session).

- Verify that the request returns a 200 status.

- Use console.log(session) inside your button click listener to confirm that it returns the correct data.

[Show a confirmation pageClient-side](#show-confirmation-page)

## Show a confirmation pageClient-side

To provide a user-friendly experience, show a confirmation page after users successfully submit their identity document. Host the page on your site to let the user know that the verification is processing.

Create a minimal confirmation page:

Next, update the button handler to redirect to this page:

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

Test that your confirmation page works:

- Click your verify button.

- Submit the session by selecting a predefined test case.

- Confirm that the new confirmation page is shown.

- Test the entire flow for failure cases (such as declining consent or refusing camera permissions) and ensure your app handles them without any issues.

Next, find the verification in the Stripe Dashboard. Verification sessions appear in the Dashboard’s list of VerificationSessions. Click a session to go to the Session Detail page. The summary section contains verification results, which you can use in your app.

[list of VerificationSessions](https://dashboard.stripe.com/identity)

[Handle verification events](#handle-verification-events)

## Handle verification events

Document checks are asynchronous, which means that verification results are not immediately available. An identity document check typically takes 1 to 3 minutes to complete. After the processing completes, the VerificationSession status changes from processing to verified.

[Document checks](/identity/verification-checks#document-availability)

[status changes](/identity/how-sessions-work)

Stripe sends the following events when the session status changes:

[identity.verification_session.verified](/api/events/types#event_types-identity.verification_session.verified)

[verification checks](/identity/verification-checks)

[identity.verification_session.requires_input](/api/events/types#event_types-identity.verification_session.requires_input)

[verification checks](/identity/verification-checks)

Use a webhook handler to receive these events and automate actions like sending a confirmation email, updating the verification results in your database, or completing an onboarding step. You can also view verification events in the Dashboard.

[webhook handler](/identity/handle-verification-outcomes)

[verification events in the Dashboard](https://dashboard.stripe.com/events?type=identity.%2A)

## Receive events and run business actions

Build a webhook handler to listen for events and build custom asynchronous verification flows. Test and debug your webhook integration locally with the Stripe CLI.

Build a custom webhook

[Build a custom webhook](/identity/handle-verification-outcomes)

Use the Dashboard to view all your verifications, inspect collected data, and understand verification failures.

View your test verifications in the Dashboard

[View your test verifications in the Dashboard](https://dashboard.stripe.com/test/identity/verification-sessions)

## See also

- Handle verification outcomes

[Handle verification outcomes](/identity/handle-verification-outcomes)

- Learn about VerificationSessions

[Learn about VerificationSessions](/identity/verification-sessions)

- Learn about Stripe.js

[Learn about Stripe.js](/payments/elements)
