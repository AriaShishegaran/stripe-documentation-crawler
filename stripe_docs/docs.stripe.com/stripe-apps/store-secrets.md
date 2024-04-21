# Store secret credentials and tokens in your app

The Secret Store API is a way to securely set, find, list, and delete persistent secrets used in Stripe Apps. These credentials, also known as secrets, are only accessible to your app and the users who own them.

[Secret Store API](/api/secret_management)

## Overview

The Secret Store API enables your app to:

- Securely store and retrieve authentication credentials

- Keep users authenticated with third-party services, even if they sign out of stripe.com and sign in again

- Securely pass secrets between your UI extension and backend

Stripe does not permit you to store sensitive personal data, personal account numbers such as credit card numbers, and other data within PCI Compliance using the Secret Store API.

[PCI Compliance](/security/guide#validating-pci-compliance)

The secrets of an uploaded app are only accessible by other apps that you’ve uploaded. You can only publish one app on an account, so published apps can never share secrets. Requests made by third-party apps can’t ever access your app’s secrets.

Use scopes to further specify the accessibility of a given secret. A scope is a collection of secrets identified by its accessibility.

The Secret Store API supports the following scope types:

[account scope](/api/apps/secret_store/secret_resource#secret_object-scope)

[Secrets](/api/apps/secret_store/secret_resource)

[user scope](/api/apps/secret_store/secret_resource#secret_object-scope)

[Secrets](/api/apps/secret_store/secret_resource)

The diagram below shows the secret scoping between the following:

- The Stripe account: “The Cactus Practice Stripe account”

- Two users sharing the same Stripe account: “User 1”, “User 2”

- Two different apps installed by the Stripe account: “Installed App A”, “Installed App B”

- account scoped secrets: “Foo API key” secret for App A, “Bar API key” for App B

- user scoped secrets: “OAuth access token”, “OAuth refresh token”

The scoped secrets of two different apps installed by the Cactus Practice Stripe account.

If a secret becomes invalid at some point in the future, you can specify an expiration time by setting the optional expires_at parameter when you set a secret. This parameter takes in a Unix timestamp (the number of seconds elapsed since the Unix epoch).

[expires_at](/api/apps/secret_store/secret_resource#secret_object-expires_at)

[set a secret](/stripe-apps/store-secrets#set-a-secret)

After the expires_at date has passed, the secret is automatically deleted from the Secret Store API.

Expiration times can’t be in the past and can’t be more than 100 years in the future.

[Set a secret](#set-a-secret)

## Set a secret

- Add the secret_write permission to your app:Command Linestripe apps grant permission "secret_write" "Allows storing secrets between page reloads"

Add the secret_write permission to your app:

- Set a secret by name and scope in the Secret Store API. You can use the following example code in your app’s UI extension or backend:App.tsxUI extensionimport { createHttpClient, STRIPE_API_KEY } from '@stripe/ui-extension-sdk/http_client';
import Stripe from 'stripe';
import type { ExtensionContextValue } from '@stripe/ui-extension-sdk/context';
import { useEffect } from 'react';

// Create an instance of a Stripe object to access customer information.
// You don't need an API Key here, because the app uses the
// dashboard credentials to make requests.
const stripe: Stripe = new Stripe(STRIPE_API_KEY, {
  httpClient: createHttpClient() as Stripe.HttpClient,
  apiVersion: '2024-04-10',
});

const App = ({userContext}: ExtensionContextValue) => {
  useEffect(() => {
    stripe.apps.secrets.create({
      scope: { type: 'user', user: userContext.id },
      name: 'secret_name',
      payload: 'secret value',
      expires_at: 1956528000  // optional
    }).then(resp => console.log(resp));
  }, []);

  return null;
};

export default App;For more information, see the API reference documentation on setting a secret.

Set a secret by name and scope in the Secret Store API. You can use the following example code in your app’s UI extension or backend:

For more information, see the API reference documentation on setting a secret.

[setting a secret](/api/apps/secret_store/set)

[Find a secret](#find-a-secret)

## Find a secret

You can find a secret by name and scope in the Secret Store API. For example, use the following example code in your app’s UI extension or backend:

For more information, see Find a secret.

[Find a secret](/api/apps/secret_store/find)

[Delete a secret](#delete-a-secret)

## Delete a secret

To delete a secret by name and scope in the Secret Store API, you can use the following example code in your app’s UI extension or backend:

For more information, see Delete a secret.

[Delete a secret](/api/apps/secret_store/delete)

[List secrets](#list-secrets)

## List secrets

If you stored the maximum amount of secrets in an account or user scope and want to add another secret, you must delete at least 1 of the 10 secrets. To determine which secrets to delete, you can list all the secrets for a given scope.

To list the secrets of an account or user scope, you can use the following example code in your app’s UI extension or backend:

For more information, see List secrets.

[List secrets](/api/apps/secret_store/list)

## Example apps

The following example apps demonstrate how to use the Secret Store API:

- Simple demo app

[Simple demo app](https://github.com/stripe/stripe-apps/tree/master/examples/secret-store)

- Dropbox OAuth with PKCE app

[Dropbox OAuth with PKCE app](https://github.com/stripe/stripe-apps/tree/master/examples/dropbox-oauth-pkce)

## See also

- Authorization flows

[Authorization flows](/stripe-apps/pkce-oauth-flow)

- Server-side logic

[Server-side logic](/stripe-apps/build-backend)

- Build a UI

[Build a UI](/stripe-apps/build-ui)
