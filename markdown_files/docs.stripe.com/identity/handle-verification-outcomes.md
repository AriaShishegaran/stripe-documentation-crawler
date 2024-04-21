htmlHandle verification outcomes | Stripe Documentation[Skip to content](#main-content)Handle verification outcomes[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fidentity%2Fhandle-verification-outcomes)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fidentity%2Fhandle-verification-outcomes)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)[Verify identities](#)
NetherlandsEnglish (United States)[](#)[](#)[Identity](/identity)·[Home](/docs)[Get started](/docs/get-started)[Verify identities](/docs/identity)# Handle verification outcomes

Listen for verification results so your integration can automatically trigger reactions.You wrote code to display a modal to collect identity documents. Now, when your user submits a document, you can listen to verification results to trigger reactions in your application.

In this guide, you’ll learn how to:

1. Receive an event notification when a verification finishes processing.
2. Handle successful and failed verification checks.
3. Turn your event handler on in production.

Verification checks are asynchronous, which means that verification results aren’t immediately available. When the processing completes, the VerificationSession status updates and the verified information is available. Stripe generates events every time a session changes status. In this guide, we’ll implement webhooks to notify your app when verification results become available.

See How sessions work to learn the status and lifecycle of verification sessions.

[Set up StripeServer-side](#set-up-stripe)Install our official libraries for access to the Stripe API from your application:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`[Create a webhook and handle VerificationSession eventsServer-side](#create-webhook)See the Build a webhook endpoint guide for a step by step explanation on how to create a webhook endpoint.

A webhook is an endpoint on your server that receives requests from Stripe, notifying you about events that happen on your account. In this step, we’ll build an endpoint to receive events on VerificationSession status changes.

Webhook endpoints must be publicly accessible so Stripe can send unauthenticated requests. You’ll need to verify that Stripe sent the event by using the Stripe library and request header:

server.js[Node](#)`// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz');

// You can find your endpoint's secret in your webhook settings
const endpointSecret = 'whsec_...';

// This example uses Express to receive webhooks
const express = require('express');

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require('body-parser');

const app = express();

// Use JSON parser for all non-webhook routes
app.use((req, res, next) => {
  if (req.originalUrl === '/webhook') {
    next();
  } else {
    bodyParser.json()(req, res, next);
  }
});

app.post('/webhook', bodyParser.raw({type: 'application/json'}), (req, res) => {
  let event;

  // Verify the event came from Stripe
  try {
    const sig = req.headers['stripe-signature'];
    event = stripe.webhooks.constructEvent(req.body, sig, endpointSecret);
  } catch (err) {
    // On error, log and return the error message
    console.log(`❌ Error message: ${err.message}`);
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }

  // Successfully constructed event

  res.json({received: true});
});

app.listen(4242, () => {
  console.log('Running on port 4242');
});`Now that you have the basic structure and security in place to listen to notifications from Stripe, update your webhook endpoint to handle verification session events.

All session events include the VerificationSession object, which contains details about the verification checks performed. See Accessing verification results to learn how to retrieve verified information not included in session events.

Stripe sends the following events when the session status changes:

Event nameDescriptionNext steps[identity.verification_session.verified](/api/events/types#event_types-identity.verification_session.verified)Processing of all the[verification checks](/identity/verification-checks)have completed, and they’re all successfully verified.Trigger relevant actions in your application.[identity.verification_session.requires_input](/api/events/types#event_types-identity.verification_session.requires_input)Processing of all the[verification checks](/identity/verification-checks)have completed, and at least one of the checks failed.Trigger relevant actions in your application and potentially allow your user to retry the verification.Your webhook code needs to handle the identity.verification_session.verified and identity.verification_session.requires_input events. You can subscribe to other session events to trigger additional reactions in your app.

### Handle VerificationSession verified status change

The identity.verification_session.verified event is sent when verification checks have completed and are all successfully verified.

Add code to your event handler to handle all verification checks passing:

server.js[Node](#)`// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz');

// You can find your endpoint's secret in your webhook settings
const endpointSecret = 'whsec_...';

// This example uses Express to receive webhooks
const express = require('express');

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require('body-parser');

const app = express();

// Use JSON parser for all non-webhook routes
app.use((req, res, next) => {
  if (req.originalUrl === '/webhook') {
    next();
  } else {
    bodyParser.json()(req, res, next);
  }
});

app.post('/webhook', bodyParser.raw({type: 'application/json'}), (req, res) => {
  let event;

  // Verify the event came from Stripe
  try {
    const sig = req.headers['stripe-signature'];
    event = stripe.webhooks.constructEvent(req.body, sig, endpointSecret);
  } catch (err) {
    // On error, log and return the error message
    console.log(`❌ Error message: ${err.message}`);
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }

  // Successfully constructed event
  switch (event.type) {
    case 'identity.verification_session.verified': {
      // All the verification checks passed
      const verificationSession = event.data.object;
      break;
    }
  }

  res.json({received: true});
});

app.listen(4242, () => {
  console.log('Running on port 4242');
});`When handling this event, you might also consider:

- Saving the verification status in your own database
- Sending an email to your user letting them know they’ve been verified
- [Expanding](/api/expanding_objects)the VerificationSession[verified outputs](/api/identity/verification_sessions/object#identity_verification_session_object-verified_outputs)and comparing them against an expected value.

### Handle VerificationSession requires_input status changes

The identity.verification_session.requires_input event is sent when at least one of the checks failed. You can inspect the last_error hash on the verification session to handle specific failure reasons:

- The[last_error.code](/api/identity/verification_sessions/object#identity_verification_session_object-last_error-code)field can be used to programmatically handle verification failures.
- The[last_error.reason](/api/identity/verification_sessions/object#identity_verification_session_object-last_error-reason)field contains a descriptive message explaining the failure reason and can be shown to your user.

Event error codes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

SessionDocumentSelfieID NumberAddress (Invite only)Error codeDescription`consent_declined`The user declined to be verified by Stripe. Check with your legal counsel to see if you have an obligation to offer an alternative, non-biometric means to verify, such as through a manual review.`under_supported_age`Stripe doesn’t verify users under the age of majority.`country_not_supported`Stripe doesn’t verify users from the provided country.Add code to your event handler to handle verification check failure:

server.js[Node](#)`// Set your secret key. Remember to switch to your live secret key in production.
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = require('stripe')('sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz');

// You can find your endpoint's secret in your webhook settings
const endpointSecret = 'whsec_...';

// This example uses Express to receive webhooks
const express = require('express');

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require('body-parser');

const app = express();

// Use JSON parser for all non-webhook routes
app.use((req, res, next) => {
  if (req.originalUrl === '/webhook') {
    next();
  } else {
    bodyParser.json()(req, res, next);
  }
});

app.post('/webhook', bodyParser.raw({type: 'application/json'}), (req, res) => {
  let event;

  // Verify the event came from Stripe
  try {
    const sig = req.headers['stripe-signature'];
    event = stripe.webhooks.constructEvent(req.body, sig, endpointSecret);
  } catch (err) {
    // On error, log and return the error message
    console.log(`❌ Error message: ${err.message}`);
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }

  // Successfully constructed event
  switch (event.type) {
    case 'identity.verification_session.verified': {
      // All the verification checks passed
      const verificationSession = event.data.object;
      break;
    }
    case 'identity.verification_session.requires_input': {
      // At least one of the verification checks failed
      const verificationSession = event.data.object;

      console.log('Verification check failed: ' + verificationSession.last_error.reason);

      // Handle specific failure reasons
      switch (verificationSession.last_error.code) {
        case 'document_unverified_other': {
          // The document was invalid
          break;
        }
        case 'document_expired': {
          // The document was expired
          break;
        }
        case 'document_type_not_supported': {
          // document type not supported
          break;
        }
        default: {
          // ...
        }
      }
    }
  }

  res.json({received: true});
});

app.listen(4242, () => {
  console.log('Running on port 4242');
});`Depending on your use case, you might want to allow your users to retry the verification if it fails. We recommend that you limit the amount of submission attempts.

When handling this event, you might also consider:

- Manually reviewing the collected information
- Sending an email to your user letting them know that their verification failed
- Providing your user an alternative verification method

[Go live in production](#go-live)After you’ve deployed your event handler endpoint to production, set up the endpoint so Stripe knows where to send live mode events. It’s also helpful to go through the development checklist to ensure a smooth transition when taking your integration live.

Webhook endpoints are configured in the Dashboard or programmatically using the API.

### Add an endpoint in the Dashboard

In the Dashboard’s Webhooks settings page, click Add an endpoint to add a new webhook endpoint. Enter the URL of your webhook endpoint and select which events to listen to. See the full list of Verification Session events.

### Add endpoint with the API

You can also programmatically create webhook endpoints. As with the form in the Dashboard, you can enter any URL as the destination for events and which event types to subscribe to.

Command Line`curl https://api.stripe.com/v1/webhook_endpoints \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "url"="https://{{DOMAIN}}/my/webhook/endpoint" \
  -d "enabled_events[]"="identity.verification_session.verified" \
  -d "enabled_events[]"="identity.verification_session.requires_input"`## See also

- [Test a webhook endpoint](/webhooks#test-webhook)
- [How sessions work](/identity/how-sessions-work)
- [Best practices for using webhooks](/webhooks#best-practices)
- [Webhook development checklist](/get-started/checklist/go-live)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up Stripe](#set-up-stripe)[Create a webhook and handle VerificationSession events](#create-webhook)[Go live in production](#go-live)[See also](#see-also)Products Used[Identity](/identity)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`