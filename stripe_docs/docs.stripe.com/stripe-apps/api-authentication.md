# API authentication methods

Your app can use one of three methods to authenticate requests to the Stripe API on behalf of your users.

[Platform key](/stripe-apps/build-backend#using-stripe-apis)

- You want to manage fewer keys per install.

- Beta You want to distribute your app through Connect platforms.

[OAuth 2.0](/stripe-apps/api-authentication/oauth)

- You already use OAuth to interact with other systems.

- Users need to manage the integration from your software.

[Restricted API key](/stripe-apps/api-authentication/rak)

- Your software can’t support platform or OAuth onboarding.

- Your users run your software on-premise.

## Configure

To configure the API authentication method, edit stripe_api_access_type in the app manifest. For setup instructions, refer to the pages linked in the table above.

[app manifest](/stripe-apps/reference/app-manifest)

## See also

- Set up OAuth 2.0

[Set up OAuth 2.0](/stripe-apps/api-authentication/oauth)

- Set up restricted access key authentication

[Set up restricted access key authentication](/stripe-apps/api-authentication/rak)
