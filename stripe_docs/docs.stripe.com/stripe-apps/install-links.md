# Using install linksBeta

Install links allow users to install public apps outside of the Stripe App Marketplace. With one integrated flow, you can pass state from your application, complete the installation of the Stripe App, and redirect to your application or site.

The install link page

## Overview

With the following steps, a user can install an app using an install link:

- On your site, the user clicks a link that redirects them to Stripe, passing along the app_id.

- On Stripe, the user selects the appropriate account and accepts permissions for installing the app.

- After installation, the user redirects to your site, along with the Stripe account for the given user.

[redirects to your site](#redirect)

- Your app can now make authenticated account requests.

[Create an install link](#create-install-link)

## Create an install link

Set your allowed_redirect_uris in your app manifest. These are the URLs that users are redirected to after installing your app. You must specify all redirect URLs in your app settings.

After you’ve set allowed_redirect_uris, upload a new version of your app.

[upload a new version](/stripe-apps/upload-install-app)

[https://example.com/callback/stripe](https://example.com/callback/stripe)

[Test your install link](#test-install-link)

## Test your install link

You can use external testing with the following steps to test the install link before submitting it for review:

[external testing](/stripe-apps/test-app)

- Create an external test for your app using the version with allowed_redirect_uris defined in the app manifest. You can update the testing version to the desired one if a test already exists.

[Create an external test](/stripe-apps/test-app)

- The External test tab shows a test install link and displays the allowed redirects in a table.

- When you’re ready to publish, make sure that you upload a new version with any testing URIs and values replaced with the values you intend to use in production.

[Using an install link](#use-install-link)

## Using an install link

When you’ve finished testing, you can make it available for all users with the following steps:

- Publish a new version of your app that defines allowed_redirect_uris.

[Publish a new version](/stripe-apps/publish-app)

- Click the Settings tab. The install link is shown here, and you can copy it. The link looks like this: https://marketplace.stripe.com/apps/install/link/{id}?redirect_uri=https://example.com.

- Recommended To prevent CSRF attacks, you can add the recommended state parameter and pass along a unique token as the value. We’ll include the state you provided when redirecting users to your site. Your site can confirm that the state parameter hasn’t been modified.

- After a user clicks the install link, Stripe opens the following page where they can select an account, review app details, and proceed with the installation.

Install link account selection

[Redirecting to your site](#redirect)

## Redirecting to your site

After the user installs your app, they’re redirected to the redirect_uri URL parameter that matches a defined redirect in allowed_redirect_uris in your app manifest.

For successful installations, the URL includes:

- The user_id value. The ID of the Stripe user that initiated the install.

- The account_id value. The ID of the Stripe account that installed your app.

- The state value, if provided

- The install_signature value. This a hash of the above values that’s generated using your app’s signing secret.

[signing secret](/stripe-apps/build-backend#expire-and-create-secrets)

- If the app is installed into test mode, a livemode=false value is appended to the redirect URL.

An example of a live mode redirect:

[https://example.com/callback/stripe?user_id={USER_ID}&account_id={CONNECTED_ACCOUNT_ID}&state={STATE}&install_signature={INSTALL_SIGNATURE}](https://example.com/callback/stripe?user_id={USER_ID}&account_id={CONNECTED_ACCOUNT_ID}&state={STATE}&install_signature={INSTALL_SIGNATURE})

An example of a test mode redirect:

[https://example.com/callback/stripe?user_id={USER_ID}&account_id={CONNECTED_ACCOUNT_ID}&state={STATE}&install_signature={INSTALL_SIGNATURE}&livemode=false](https://example.com/callback/stripe?user_id={USER_ID}&account_id={CONNECTED_ACCOUNT_ID}&state={STATE}&install_signature={INSTALL_SIGNATURE}&livemode=false)

If the user cancels the installation, they will still be redirected to your site, but the URL includes an error instead:

[https://example.com/callback/stripe?error=access_denied&error_description=The%20user%20denied%20your%20request](https://example.com/callback/stripe?error=access_denied&error_description=The%20user%20denied%20your%20request)

The user is now connected to your app. Store the stripe_user_id in your database—this is the user’s Stripe account ID. You’ll use this value to authenticate as the connected account by passing it into requests in the Stripe-Account header.

[authenticate as the connected account](/connect/authentication)

It’s important to verify that your app’s user was authorized to install the app for the account provided in the redirect URL. An install_signature is included for this reason. This signature is generated from your app’s signing secret and the user_id and account_id that completed the install. The signature also includes the passed state, if provided. The signature can’t be replicated without access to the signing secret, which is only available internally to Stripe and to your app’s backend. Because of this, bad actors can’t replicate the hash if they were to try and spoof the redirect URL. By verifying the app signature, you can trust that the account is associated with your app user.

[signing secret](/stripe-apps/build-backend#expire-and-create-secrets)

To verify the signature, follow these steps:

- Create your app’s signing secret if you haven’t done so already.

[Create your app’s signing secret](/stripe-apps/build-backend#expire-and-create-secrets)

- Setup an app backend to verify the install_signature.

[Setup an app backend](/stripe-apps/build-backend#send-a-signed-request)

The order and naming of the payload fields matter when performing signature verification. The state precedes the user_id, which precedes the account_id. The resulting object should be { state, user_id, account_id }.

After it’s verified, you can make API calls on behalf of the installed account.

[make API calls](/stripe-apps/build-backend#using-stripe-apis)

[Make authenticated requests](#authenticated-requests)

## Make authenticated requests

For server-side API calls, you can make requests as connected accounts using the special header Stripe-Account with the Stripe account identifier (it starts with the prefix acct_) of your platform user. Here’s an example that shows how to Create a PaymentIntent with your platform’s API secret key and your user’s Account identifier.

[Create a PaymentIntent](/api/payment_intents/create)

[API secret key](/keys)

[Account](/api/accounts)

The Stripe-Account header approach is implied in any API request that includes the Stripe account ID in the URL. Here’s an example that shows how to Retrieve an account with your user’s Account identifier in the URL.

[Retrieve an account](/api/accounts/retrieve)

[Account](/api/accounts)

See more examples of making an authenticated request here.

[authenticated request here](/connect/authentication)

## Customize links with URL parameters

You can change the behavior of the app installation by including additional URL parameters in the install link.

[app manifest](/stripe-apps/reference/app-manifest)

To prevent cross-site request forgery (CSRF) attacks, you can use the state parameter. This parameter accepts any string value and returns it unmodified upon redirecting the installer back to your application or platform. To use this parameter, pass a unique and non-guessable value when you initiate an install using an install link. Save the value to use it for verification later.

After the user installs and is redirected back to your application, verify whether the value of the state parameter provided matches the value present in the initial install link. This verification process provides a high-level of confidence to confirm that the stripe_user_id returned belongs to the user who initiated the install and safeguard against potential forgeries.

## Revoking access

An account.application.deauthorized event occurs when a user disconnects your app from their account. You can perform any necessary cleanup on your servers by watching for this event with webhooks.

[event](/api#list_events)

[webhooks](/connect/webhooks)

## See also

- How Stripe Apps work

[How Stripe Apps work](/stripe-apps/how-stripe-apps-work)

- Full API reference

[Full API reference](/api)
