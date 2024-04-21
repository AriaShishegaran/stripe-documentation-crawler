# Add server-side logic

With Stripe Apps, you can add server-side logic with a self-hosted backend. With a self-hosted backend service, you can:

- Integrate securely with third-party systems that require a server-side integration.

- Subscribe to webhook events from Stripe and synchronize Stripe with other systems.

[webhook](/webhooks)

- Use long-lived app logic that executes when the user closes the browser.

- Build apps that provide cron-job-like functionality to schedule specific actions.

How the self-hosted backend relates to the app

[Authenticate users from your UI to your app's backend](#authenticate-ui-to-backend)

## Authenticate users from your UI to your app's backend

To authenticate a user from the Dashboard, the backend needs a signature with the shared secret and the account and user ID of the current, signed-in Dashboard user. If your user doesn’t have permission to call the API, Stripe returns a Permission error.

[Permission error](/error-handling?lang=node#permission-errors)

## Before you begin

- Make sure your backend service can send and receive HTTP requests. If you haven’t built an API server before, consider trying the interactive webhook endpoint builder.

Make sure your backend service can send and receive HTTP requests. If you haven’t built an API server before, consider trying the interactive webhook endpoint builder.

[interactive webhook endpoint builder](/webhooks/quickstart)

- Create your shared secret by uploading your app:Command Linestripe apps uploadDon’t worry if you haven’t finished developing the current version of your app, uploading won’t update your app in live mode.

Create your shared secret by uploading your app:

[uploading your app](/stripe-apps/upload-install-app)

Don’t worry if you haven’t finished developing the current version of your app, uploading won’t update your app in live mode.

- Get your app’s secret to verify the signature in your backend:a. Go to your Stripe app details page by selecting your app from Apps.b. Under the application ID, click the overflow menu (), then click Signing secret to open the signing secret dialog.c. Click the clipboard  to copy your app’s secret from the signing secret dialog.

Get your app’s secret to verify the signature in your backend:

a. Go to your Stripe app details page by selecting your app from Apps.

[Apps](https://dashboard.stripe.com/apps)

b. Under the application ID, click the overflow menu (), then click Signing secret to open the signing secret dialog.

c. Click the clipboard  to copy your app’s secret from the signing secret dialog.

To send a signed request to the app’s backend:

- Get the current signature using the fetchStripeSignature asynchronous function.

[fetchStripeSignature](/stripe-apps/reference/extensions-sdk-api#fetchStripeSignature)

- Add the signature to the Stripe-Signature header.

- Include the user_id and account_id objects in the request.

- On the app’s backend, verify that the request includes the signature, app secret, user_id, and account_id.

See an example of sending a signed request with additional data.

[example of sending a signed request with additional data](/stripe-apps/build-backend#send-a-signed-request-with-additional-data)

An example request from a Stripe app with the Stripe-Signature header:

[https://example.com/${endpoint}/`,](https://example.com/${endpoint}/`,)

Sample backend verifying the request:

Please be aware that the order and naming of the payload fields matters when performing signature verification. The user_id precedes the account_id and the resulting object is as follows: { user_id, account_id }

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

You can authenticate a user by sending a signed request with a payload (additional data). When you call the fetchStripeSignature function with an additional payload request, you create a signature with user_id, account_id and the additional payload you passed into the function. By default, Stripe apps use user_id and account_id to generate the signature string.

An example of generating a secret with additional payload:

[https://example.com/do_more_secret_stuff/`,](https://example.com/do_more_secret_stuff/`,)

Sample backend verifying the signature generated with additional payload:

You can verify the user roles assigned to a given user_id by including the stripe_roles key in the payload. Provide this with userContext?.roles, which returns a list of RoleDefinitions. If any role in the payload isn’t assigned to the user_id provided, fetchStripeSignature returns an invalid request error (400).

[RoleDefinitions](/stripe-apps/reference/extensions-sdk-api#roledefinition)

[https://example.com/do_more_secret_stuff/`,](https://example.com/do_more_secret_stuff/`,)

If your secret is compromised, you can expire your current app’s secret immediately for up to 24 hours to update the app’s secret on your backend. During this time, two secrets are active for the endpoint, the compromised secret and the newly generated secret. Stripe generates one signature per secret until expiration.

To expire and create an app secret:

- Go to your Stripe app details page by selecting your app from Apps.

[Apps](https://dashboard.stripe.com/apps)

- On the page header, click the overflow menu (), then click Signing secret to open the Signing secret dialog.

- Click Expire secret from the signing secret dialog to open the Expire secret dialog.

- Select an expiration duration for your current’s app secret.

- Click Expire secret.

Cross-Origin Resource Sharing (CORS) is an important part of helping keep apps secure from cross-site scripting attacks (XSS). Because Stripe App UI extensions are, by necessity, cross-origin and sandboxed, you must employ a specific approach to handling cross-origin request headers.

[Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

[cross-site scripting attacks (XSS)](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting)

For your UI extension to retrieve data from your backend service, you must configure your backend service to do the following:

- Allow requests using the Options method.

[Options method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/OPTIONS)

- To allow requests from null origins, set the Access-Control-Allow-Origin to *.

UI extensions have a null origin because they run in a sandbox for security purposes.

Many backend frameworks have libraries and guidance to help you handle CORS. Check the documentation for your framework for more specific guidance.

To authenticate that a request came from Stripe on behalf of a particular user or account, see Authenticate users from your UI to your backend.

[Authenticate users from your UI to your backend](/stripe-apps/build-backend#authenticate-ui-to-backend)

Only configure authenticated endpoints and any endpoints the UI extension communicates with to use Access-Control-Allow-Origin: *. Unauthenticated endpoints are vulnerable to CSRF attacks if no other measures are in place.

[CSRF](https://developer.mozilla.org/en-US/docs/Glossary/CSRF)

[Use Stripe APIs](#using-stripe-apis)

## Use Stripe APIs

To interact with Stripe, you can use and authenticate your requests to the Stripe API.

To authenticate your requests, use your existing merchant account API key to interact with Stripe and specify the user’s stripeAccountId.

For server-side API calls, you can make requests as connected accounts using the special header Stripe-Account with the Stripe account identifier (it starts with the prefix acct_) of your platform user. Here’s an example that shows how to Create a PaymentIntent with your platform’s API secret key and your user’s Account identifier.

[Create a PaymentIntent](/api/payment_intents/create)

[API secret key](/keys)

[Account](/api/accounts)

The Stripe-Account header approach is implied in any API request that includes the Stripe account ID in the URL. Here’s an example that shows how to Retrieve an account with your user’s Account identifier in the URL.

[Retrieve an account](/api/accounts/retrieve)

[Account](/api/accounts)

In addition, all of Stripe’s server-side libraries support this approach on a per-request basis, as shown in the following example:

When you make requests from your UI extension to your backend, send a signature with your request to validate the legitimacy of the requests. From the UI extension, pass the stripeAccountId for the current user so that you can make backend requests on behalf of that user.

[send a signature with your request](/stripe-apps/build-backend#authenticate-ui-to-backend)

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

[Call other APIs](#call-other-apis)

## Call other APIs

From your self-hosted backend, you can call any API—your own API or one built by another developer or company.

For more information, learn how to store secret credentials and tokens in your app.

[store secret credentials and tokens in your app](/stripe-apps/store-secrets)

If you need to pass user information from Stripe to another service, use the stripeAccountId passed from your UI extension.

[http://worldclockapi.com/api/json/est/now](http://worldclockapi.com/api/json/est/now)

You can also call a third-party API from your UI extension.

[call a third-party API from your UI extension](/stripe-apps/build-ui#use-third-party-apis)

[Receive event notifications about your app](#receiving-events-webhooks)

## Receive event notifications about your app

Listen for events (such as user installs or uninstalls) on your Stripe app using incoming webhooks so your integration can automatically trigger reactions in your backend such as:

[webhooks](/webhooks)

- Creating user accounts

- Updating permissions

- Disabling a user’s account and removing data

You can receive events from Stripe for an app that’s private to your account only or an app that’s listed on the App Marketplace:

To receive events for an app that’s private to users on your account only:

- Handle webhook events in your app’s backend.

[webhook events](/webhooks#webhook-endpoint-def)

- Register a webhook endpoint in the Stripe Dashboard.

[Register a webhook endpoint](/webhooks#webhooks-summary)

When a merchant triggers an event, Stripe provides the following Event object. This event includes the account property specifying the account ID of the merchant who triggers the event:

[Event](/api/events/object)

Using the account attribute, you can do the following:

- Monitor how many merchants install and uninstall your app.

- Make API calls on behalf of users with Stripe Connect.

[Make API calls on behalf of users with Stripe Connect](/connect/authentication)

In addition to the types of events Stripe supports, Stripe Apps also supports the following events:

[types of events Stripe supports](/api/events/types)

[account.application.authorized](/api/events/types#event_types-account.application.authorized)

[account.application.deauthorized](/api/events/types#event_types-account.application.deauthorized)

You can test webhooks locally for:

- An app that’s only available to all users on your account and listens to events on your own account

- An app that’s available on the Stripe App Marketplace and listens to events on accounts that have installed your app

To test webhooks locally:

- Install the Stripe CLI.

Install the Stripe CLI.

[Install the Stripe CLI](/stripe-cli)

- Authenticate your account:Command Linestripe login

Authenticate your account:

- Open two terminal windows:In one terminal window, Set up event forwarding:Private to your account onlyPublic listing on App MarketplaceCommand Linestripe listen --forward-to localhost:{{PORT}}/webhookIn the other terminal window, Trigger events to test your webhooks integration:Private to your account onlyPublic listing on App MarketplaceCommand Linestripe trigger {{EVENT_NAME}}

Open two terminal windows:

- In one terminal window, Set up event forwarding:Private to your account onlyPublic listing on App MarketplaceCommand Linestripe listen --forward-to localhost:{{PORT}}/webhook

In one terminal window, Set up event forwarding:

[Set up event forwarding](/webhooks#local-listener)

- In the other terminal window, Trigger events to test your webhooks integration:Private to your account onlyPublic listing on App MarketplaceCommand Linestripe trigger {{EVENT_NAME}}

In the other terminal window, Trigger events to test your webhooks integration:

[Trigger events to test your webhooks integration](/webhooks#trigger-test-events)

For more information, see our docs on testing a webhook endpoint.

[testing a webhook endpoint](/webhooks#local-listener)

## See also

- Build a UI

[Build a UI](/stripe-apps/build-ui)

- Upload and install your app

[Upload and install your app](/stripe-apps/upload-install-app)

- Publish your app

[Publish your app](/stripe-apps/publish-app)
