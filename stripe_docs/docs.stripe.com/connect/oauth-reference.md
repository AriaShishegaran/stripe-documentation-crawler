# Connect OAuth reference

Connect platforms can work with three different account types.

[Connect](/connect)

[account types](/connect/accounts)

The content on this page applies only to Standard accounts.

The OAuth Connect flow allows you to customize the user’s experience by passing additional parameters to Stripe. Some common examples are explained below, and the rest of the reference lists every possible option.

[Connect](/connect)

As a platform, remember that data you create for a Standard account (that is, charges, customers, invoices, and so on) will be visible on their Stripe account. This also means if they connect other platforms, those platforms will have access to that data too.

[invoices](/api/invoices)

Starting in June 2021, Platforms using OAuth with read_write scope won’t be able to connect to accounts that are controlled by another platform.

Extensions won’t experience any changes to how OAuth behaves. Learn more about OAuth changes for Standard Platforms.

[Extensions](/building-extensions)

[OAuth changes for Standard Platforms](/connect/oauth-changes-for-standard-platforms)

## Common examples

Provide the best possible user experience for users who need to create a new Stripe account by prefilling the account form fields with information you already have, like the user’s email and name. Prefilling has no effect if your user already has a Stripe account. You can’t prefill certain fields, including terms of service acceptance and RISA acceptance in Japan.

For security purposes, Stripe redirects a user only to a predefined URI. However, Connect allows you to define more than one redirect URI, which you can use to further customize the user’s experience. For example, you could redirect some of your users back to https://sub1.example.com and others to https://sub2.example.com.

To dynamically set the redirect URI:

- In your platform settings, add each redirect URI.

[platform settings](https://dashboard.stripe.com/account/applications/settings)

- Add a redirect_uri parameter to your authorization request and set the value to one of your redirect URIs.

If no redirect_uri is specified in the URL, then Stripe uses the first URI configured in your platform settings.

## Authorize the account

For Standard accounts: GET https://connect.stripe.com/oauth/authorize

Sends the user to Stripe to connect to your platform.

[application settings](https://dashboard.stripe.com/account/applications/settings)

[response](#get-authorize-response)

[application settings](https://dashboard.stripe.com/account/applications/settings)

The following query string parameters are all optional—we use them to prefill details in the account form for new users. Some prefilled fields (for example, URL or product category) might be automatically hidden. Any parameters with invalid values are silently ignored.

Note that some of these parameters apply only to Standard accounts (indicated).

[ISO code](http://en.wikipedia.org/wiki/ISO_4217)

The user’s browser is redirected back to your configured redirect URI or the value you passed in the redirect_uri parameter. When successful, you receive the following query parameters:

[configured redirect URI](https://dashboard.stripe.com/account/applications/settings)

In case of an error, the user’s browser won’t be redirected except in the case of access_denied. Instead, errors will be returned in a JSON dictionary with the following fields:

[error code](#get-authorize-error-codes)

[application settings](https://dashboard.stripe.com/account/applications/settings)

## Complete the connection and get the account ID

POST https://connect.stripe.com/oauth/token

Used both for turning an authorization_code into an account connection, and for getting a new access token using a refresh_token.

Make this call using your secret API key as a client_secret POST parameter:

When converting an authorization code to an access token, you must use an API key that matches the mode—live or test—of the authorization code (which depends on whether the client_id used was production or development).

When using a refresh token to request an access token, you may use either a test or live API key to obtain a test or live access token respectively. Any existing access token with the same scope and mode—live or test—is revoked.

Per OAuth v2, this endpoint isn’t idempotent. Consuming an authorization code more than once revokes the account connection.

[to authorize the OAuth request](#get-authorize)

[header](/connect/authentication#stripe-account-header)

[header](/connect/authentication#stripe-account-header)

[applicable](/connect/testing#creating-accounts)

[error code](#post-token-error-codes)

- code doesn’t exist, is expired, has been used, or doesn’t belong to you

- refresh_token doesn’t exist or doesn’t belong to you

- API key mode (live or test mode) doesn’t match the code or refresh_token mode

## Revoke the account’s access

POST https://connect.stripe.com/oauth/deauthorize

Used for revoking access to an account.

You can only revoke a Standard account’s access to your platform.

Make this call using your secret API key as an Authorization header.

When revoking access to an account, you must use an API key that matches the mode — live or test — used to connect to the account. Use a live mode API key if a production client_id created the connection, or a test mode API key for a development client_id.

[error code](#post-deauthorize-error-codes)

- client_id doesn’t belong to you

- stripe_user_id doesn’t exist or isn’t connected to your application

- API key mode (live or test mode) doesn’t match the client_id mode

- no_deauth_on_controlled_account the account can’t be disconnected and instead use the rejection API.

[rejection API](/api/account/reject)
