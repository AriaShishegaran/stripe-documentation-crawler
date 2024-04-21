htmlAdd authorization flows | Stripe Documentation[Skip to content](#main-content)Authorization flows[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fpkce-oauth-flow)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fpkce-oauth-flow)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)# Add authorization flows

Implement PKCE OAuth workflows in your Stripe app in the Stripe Dashboard.You can implement OAuth with your UI extension in the Dashboard to retrieve access tokens from an OAuth provider instead of building an OAuth backend. If the user gives your Stripe App access to an OAuth provider, they can interact with the services of the OAuth provider directly from your Stripe App in the Dashboard.

![A Stripe App's OAuth flow](https://b.stripecdn.com/docs-statics-srv/assets/oauth_pkce_flow_diagram_v2.491ae76870978963e8b69e82e2b1a1a1.png)

OAuth flow with a Stripe App

## Before you begin

- Ensure that your OAuth provider supports the[Proof Key for Code Exchange (PKCE)](https://auth0.com/docs/get-started/authentication-and-authorization-flow/authorization-code-flow-with-proof-key-for-code-exchange-pkce)flow.
- If you haven’t already, create an app with your OAuth provider to connect and use with your Stripe App.
- [Create a Stripe app](/stripe-apps/create-app)and[build a UI](/stripe-apps/build-ui). The UI extension retrieves the access token from the OAuth provider with the PKCE flow.

[Create an authorization link](#create-authorization-link)End users click on an authorization link from your app to start the OAuth flow and give your app access to the service of the OAuth provider.

1. Create the test mode and live mode OAuth redirect URLs. The redirect URL is unique to your app and includes your app id in the path. For example, if the id field in your app manifest is "id": "com.example.oauth-example":

  - The test mode URL is:

`https://dashboard.stripe.com/test/apps-oauth/com.example.oauth-example`  - The live mode URL is:

`https://dashboard.stripe.com/apps-oauth/com.example.oauth-example`
2. Register the test and live OAuth redirect URLs with your OAuth provider.


3. From your app’s UI extension, create a pathway that routes users from your Stripe app to authorize the OAuth provider by passing the following parameters in the OAuth redirect URLs:

ParameterValue`reponse_type`This is always`code`. The PKCE flow uses`code`as the value to request an authorization code from the OAuth provider.`client_id`The ID of your OAuth app assigned from your OAuth provider.`redirect_uri`The Stripe app’s OAuth redirect URL. This is the URL the OAuth provider uses to redirect a user to your app.`state`The`state`return value from the[createOAuthState](/stripe-apps/reference/extensions-sdk-api#createOAuthState)function.`code_challenge`The`challenge`return value from the[createOAuthState](/stripe-apps/reference/extensions-sdk-api#createOAuthState)function.`code_challenge_method`This is always`S256`.

You can use the following code example to route users from your Stripe App to authorize a third-party app using the OAuth redirect URLs and the Button UI component:

`import {
  ContextView,
  Button,
} from '@stripe/ui-extension-sdk/ui';
import * as React from 'react';
import {createOAuthState} from '@stripe/ui-extension-sdk/oauth';
import type {ExtensionContextValue} from '@stripe/ui-extension-sdk/context';

const {useState, useEffect} = React;

const clientID = 'your_client_id';
const getRedirectURL = (mode: 'live' | 'test') => `https://dashboard.stripe.com/${
  mode === 'test' ? 'test/' : ''
}apps-oauth/com.example.oauth-example`;
const getAuthURL = (state: string, challenge: string, mode: 'live' | 'test') =>
  `https://www.example.com/oauth2/authorize?response_type=code&client_id=${clientID}&redirect_uri=${getRedirectURL(mode)}&state=${state}&code_challenge=${challenge}&code_challenge_method=S256`;

const ExampleApp = ({environment}: ExtensionContextValue) => {
  const {mode} = environment;
  const [authURL, setAuthURL] = useState('');
  useEffect(() => {
    createOAuthState().then(({state, challenge}) => {
      setAuthURL(getAuthURL(state, challenge, mode));
    });
  }, [mode]);

  return (
    <ContextView title="Example">
      <Button type="primary" href={authURL} target="_blank">Authorize ExampleApp</Button>
    </ContextView>
  );
};
export default ExampleApp;`[Retrieve an access token from the OAuth provider](#retrieve-an-access-token)Your app can only make requests on behalf of the current user. After the user authorizes your app, the Dashboard passes their OAuth data to your app through the code and verifier values of the oauthContext context prop.

Only valid authorization attempts allow your app to read the code, verifier, and if applicable, custom state values.  An authorization attempt is valid if the OAuth provider redirects to the redirect_uri and includes the state value in the matching query string parameter of the authorization link. The state value must be identical to the state value returned by createOAuthState function (when you created the authorization link).

From your app’s UI extension, retrieve the access token from the OAuth provider with the following parameters:

ParameterValue`code`The value of the`oauthContext.code`[React prop](/stripe-apps/reference/extensions-sdk-api#props).`grant_type`This is always`authorization_code`.`code_verifier`The value of the`oauthContext.verifier`[React prop](/stripe-apps/reference/extensions-sdk-api#props).`client_id`Your client ID from the OAuth provider.`redirect_uri`The Stripe app’s OAuth redirect URL.You can use the following code example to retrieve an access token from an OAuth provider:

`import {ContextView} from '@stripe/ui-extension-sdk/ui';
import * as React from 'react';
import type {ExtensionContextValue} from '@stripe/ui-extension-sdk/context';

const {useState, useEffect} = React;

// Store the authorization token data.
interface TokenData {
  account_id: string;
  access_token: string;
  expires_in: number;
}

const clientID = 'your_client_id';
const getRedirectURL = (mode: 'live' | 'test') => `https://dashboard.stripe.com/${
  mode === 'test' ? 'test/' : ''
}apps-oauth/com.example.oauth-example`;

// Fetch the authorization token from an example authorization server.
const getTokenFromAuthServer = async ({code, verifier, mode}: {code: string, verifier: string, mode: 'live' | 'test'}): Promise<null | TokenData> => {
  try {
    const response = await fetch(`https://api.example.com/oauth2/token?code=${code}&grant_type=authorization_code&code_verifier=${verifier}&client_id=${clientID}&redirect_uri=${getRedirectURL(mode)}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    });
    if (response.ok) {
      return await response.json();
    }
    throw new Error(await response.text());
  } catch (e) {
    console.error('Unable to retrieve token from authorization server:', (e as Error).message);
    return null;
  }
};

const ExampleApp = ({environment, oauthContext}: ExtensionContextValue) => {
  const [tokenData, setTokenData] = useState<TokenData | null>(null);
  const code = oauthContext?.code || '';
  const verifier = oauthContext?.verifier || '';
  const {mode} = environment;

  useEffect(() => {
    if (code && verifier && !tokenData) {
      getTokenFromAuthServer({code, verifier, mode}).then(setTokenData);
    }
  }, [code, verifier, mode, tokenData]);

  return (
    <ContextView title="Example" />
  )
};
export default ExampleApp;`[Set and find an access token](#set-and-find-access-token)Set and find the access token in the Secret Store API to enable your app to store and use it in later sessions:

1. Add the secret_write permission to your app:

Command Line`stripe apps grant permission "secret_write" "Allows storing secrets between page reloads"`
2. From your app’s UI extension, set the access token in the Secret Store API:

`import {ContextView} from '@stripe/ui-extension-sdk/ui';
import * as React from 'react';
import Stripe from 'stripe';
import {createHttpClient, STRIPE_API_KEY} from '@stripe/ui-extension-sdk/http_client';
import type {ExtensionContextValue} from '@stripe/ui-extension-sdk/context';

const {useState, useEffect} = React;

interface TokenData {
  account_id: string;
  access_token: string;
  expires_in: number;
}

const clientID = 'your_client_id';
const getRedirectURL = (mode: 'live' | 'test') => `https://dashboard.stripe.com/${
  mode === 'test' ? 'test/' : ''
}apps-oauth/com.example.oauth-example`;

// Fetch the authorization token from an example authorization server.
const getTokenFromAuthServer = async ({code, verifier, mode}: {code: string, verifier: string, mode: 'live' | 'test'}): Promise<null | TokenData> => {
  try {
    const response = await fetch(`https://api.example.com/oauth2/token?code=${code}&grant_type=authorization_code&code_verifier=${verifier}&client_id=${clientID}&redirect_uri=${getRedirectURL(mode)}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    });
    if (response.ok) {
      return await response.json();
    }
    throw new Error(await response.text());
  } catch (e) {
    console.error('Unable to retrieve token from authorization server:', (e as Error).message);
    return null;
  }
};

const stripe = new Stripe(STRIPE_API_KEY, {
  httpClient: createHttpClient(),
  apiVersion: '2024-04-10',
});

// Save the token to Secret Store API
const saveTokenData = async ({userID, tokenData}: {userID: string, tokenData: TokenData}) => {
  try {
    await stripe.apps.secrets.create({
      scope: { type: 'user', user: userID },
      name: 'oauth_token',
      payload: JSON.stringify(tokenData),
    });
  } catch (e) {
    console.error('Unable to save token to Secret Store API:', (e as Error).message);
  }
}

const ExampleApp = ({userContext, environment, oauthContext}: ExtensionContextValue) => {
  const [tokenData, setTokenData] = useState<TokenData | null>(null);
  const code = oauthContext?.code || '';
  const verifier = oauthContext?.verifier || '';
  const {mode} = environment;
  const {id: userID} = userContext;

  useEffect(() => {
    if (code && verifier && !tokenData) {
      getTokenFromAuthServer({code, verifier, mode}).then(tokenData => {
        if (tokenData) {
          setTokenData(tokenData);
          saveTokenData({userID, tokenData});
        }
      });
    }
  }, [code, verifier, mode, userID, tokenData]);

  return (
    <ContextView title="Example" />
  )
};

export default ExampleApp;`For more information, see Set a secret.


3. From your app’s UI extension, find the access token in the Secret Store API:

`import {ContextView} from '@stripe/ui-extension-sdk/ui';
import * as React from 'react';
import Stripe from 'stripe';
import {createHttpClient, STRIPE_API_KEY} from '@stripe/ui-extension-sdk/http_client';
import type {ExtensionContextValue} from '@stripe/ui-extension-sdk/context';

const {useState, useEffect} = React;

interface TokenData {
  account_id: string;
  access_token: string;
  expires_in: number;
}

const stripe = new Stripe(STRIPE_API_KEY, {
  httpClient: createHttpClient(),
  apiVersion: '2024-04-10',
});

// Read the token from Secret Store API
const getTokenFromSecretStore = async (userID: string): Promise<TokenData | null> => {
  try {
    const response = await stripe.apps.secrets.find({
      scope: { type: 'user', user: userID },
      name: 'oauth_token',
      expand: ['payload'],
    });
    const secretValue: string = response.payload!;
    return JSON.parse(secretValue) as TokenData;
  } catch (e) {
    console.error('Unable to retrieve token from Secret Store API:', (e as Error).message);
    return null;
  }
};

const ExampleApp = ({userContext}: ExtensionContextValue) => {
  const [tokenData, setTokenData] = useState<TokenData | null>(null);
  const {id: userID} = userContext;

  useEffect(() => {
    if (!tokenData) {
      getTokenFromSecretStore(userID).then(setTokenData);
    }
  }, [userID, tokenData]);

  return (
    <ContextView title="Example" />
  )
};

export default ExampleApp;`For more information, see Find a secret.



## See also

- [Store secrets](/stripe-apps/store-secrets)
- [Server-side logic](/stripe-apps/build-backend)
- [Upload your app](/stripe-apps/upload-install-app)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Create an authorization link](#create-authorization-link)[Retrieve an access token from the OAuth provider](#retrieve-an-access-token)[Set and find an access token](#set-and-find-access-token)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`