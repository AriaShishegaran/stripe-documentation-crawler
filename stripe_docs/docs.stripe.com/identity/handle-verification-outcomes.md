# Handle verification outcomes

You wrote code to display a modal to collect identity documents. Now, when your user submits a document, you can listen to verification results to trigger reactions in your application.

[display a modal to collect identity documents](/identity/verify-identity-documents)

In this guide, you’ll learn how to:

- Receive an event notification when a verification finishes processing.

- Handle successful and failed verification checks.

- Turn your event handler on in production.

Verification checks are asynchronous, which means that verification results aren’t immediately available. When the processing completes, the VerificationSession status updates and the verified information is available. Stripe generates events every time a session changes status. In this guide, we’ll implement webhooks to notify your app when verification results become available.

[Verification checks](/identity/verification-checks)

[events](/api/events)

[webhooks](/webhooks)

See How sessions work to learn the status and lifecycle of verification sessions.

[How sessions work](/identity/how-sessions-work)

[Set up StripeServer-side](#set-up-stripe)

## Set up StripeServer-side

Install our official libraries for access to the Stripe API from your application:

[Create a webhook and handle VerificationSession eventsServer-side](#create-webhook)

## Create a webhook and handle VerificationSession eventsServer-side

See the Build a webhook endpoint guide for a step by step explanation on how to create a webhook endpoint.

[Build a webhook endpoint](/webhooks/quickstart)

A webhook is an endpoint on your server that receives requests from Stripe, notifying you about events that happen on your account. In this step, we’ll build an endpoint to receive events on VerificationSession status changes.

[webhook](/webhooks#webhooks-def)

[status changes](/identity/how-sessions-work)

Webhook endpoints must be publicly accessible so Stripe can send unauthenticated requests. You’ll need to verify that Stripe sent the event by using the Stripe library and request header:

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

Now that you have the basic structure and security in place to listen to notifications from Stripe, update your webhook endpoint to handle verification session events.

All session events include the VerificationSession object, which contains details about the verification checks performed. See Accessing verification results to learn how to retrieve verified information not included in session events.

[session events](/identity/how-sessions-work#events)

[VerificationSession](/api/identity/verification_sessions)

[Accessing verification results](/identity/access-verification-results)

Stripe sends the following events when the session status changes:

[identity.verification_session.verified](/api/events/types#event_types-identity.verification_session.verified)

[verification checks](/identity/verification-checks)

[identity.verification_session.requires_input](/api/events/types#event_types-identity.verification_session.requires_input)

[verification checks](/identity/verification-checks)

Your webhook code needs to handle the identity.verification_session.verified and identity.verification_session.requires_input events. You can subscribe to other session events to trigger additional reactions in your app.

[session events](/identity/how-sessions-work#events)

The identity.verification_session.verified event is sent when verification checks have completed and are all successfully verified.

Add code to your event handler to handle all verification checks passing:

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

When handling this event, you might also consider:

- Saving the verification status in your own database

- Sending an email to your user letting them know they’ve been verified

- Expanding the VerificationSession verified outputs and comparing them against an expected value.

[Expanding](/api/expanding_objects)

[verified outputs](/api/identity/verification_sessions/object#identity_verification_session_object-verified_outputs)

The identity.verification_session.requires_input event is sent when at least one of the checks failed. You can inspect the last_error hash on the verification session to handle specific failure reasons:

[last_error](/api/identity/verification_sessions/object#identity_verification_session_object-last_error)

- The last_error.code field can be used to programmatically handle verification failures.

[last_error.code](/api/identity/verification_sessions/object#identity_verification_session_object-last_error-code)

- The last_error.reason field contains a descriptive message explaining the failure reason and can be shown to your user.

[last_error.reason](/api/identity/verification_sessions/object#identity_verification_session_object-last_error-reason)

Add code to your event handler to handle verification check failure:

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

Depending on your use case, you might want to allow your users to retry the verification if it fails. We recommend that you limit the amount of submission attempts.

When handling this event, you might also consider:

- Manually reviewing the collected information

- Sending an email to your user letting them know that their verification failed

- Providing your user an alternative verification method

[Go live in production](#go-live)

## Go live in production

After you’ve deployed your event handler endpoint to production, set up the endpoint so Stripe knows where to send live mode events. It’s also helpful to go through the development checklist to ensure a smooth transition when taking your integration live.

[development checklist](/get-started/checklist/go-live)

Webhook endpoints are configured in the Dashboard or programmatically using the API.

In the Dashboard’s Webhooks settings page, click Add an endpoint to add a new webhook endpoint. Enter the URL of your webhook endpoint and select which events to listen to. See the full list of Verification Session events.

[Webhooks settings](https://dashboard.stripe.com/webhooks)

[Verification Session events](/identity/how-sessions-work#events)

You can also programmatically create webhook endpoints. As with the form in the Dashboard, you can enter any URL as the destination for events and which event types to subscribe to.

[create webhook endpoints](/api/webhook_endpoints/create)

## See also

- Test a webhook endpoint

[Test a webhook endpoint](/webhooks#test-webhook)

- How sessions work

[How sessions work](/identity/how-sessions-work)

- Best practices for using webhooks

[Best practices for using webhooks](/webhooks#best-practices)

- Webhook development checklist

[Webhook development checklist](/get-started/checklist/go-live)
