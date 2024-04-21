htmlUsing the standalone hosted onramp | Stripe Documentation[Skip to content](#main-content)Standalone hosted onramp[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fcrypto%2Fstandalone-hosted-onramp)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fcrypto%2Fstandalone-hosted-onramp)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)
[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Crypto](/docs/crypto)[Fiat-to-crypto onramp](/docs/crypto)# Using the standalone hosted onrampBeta

Learn how to use the standalone hosted onramp.The standalone hosted onramp is a prebuilt frontend integration of the crypto onramp hosted at https://crypto.link.com. Platforms can integrate the crypto onramp by redirecting their users to the standalone hosted onramp, rather than hosting an embedded version of the onramp within their application.

Generate a redirect URLMint a session with a redirect URLOverviewGenerate a redirect URL in the frontend without a Stripe account.Mint a session with a redirect URL in the backend with a Stripe account.CustomizationCustomize the suggested source or destination amount, and the destination currency and network.Allows full customization, including destination wallet address. For a full list of parameters, go to[using the api](/crypto/using-the-api#how-to-pre-populate-transaction-parameters).Best forPlatforms that want only want a lightweight frontend integration with light customization and no branding.Platforms that want a fully customized onramp with branding.Platforms that want to embed the crypto onramp within their application can integrate the onramp.

## Generate a redirect URL

Include the following scripts using script tags within the <head> element of your HTML. These scripts must always load directly from Stripe domains, https://js.stripe.com and https://crypto-js.stripe.com, for compatibility and PCI compliance. Don’t include the scripts in a bundle or host a copy yourself. If you do, your integration might break without warning.

`<head>
  <title>Onramp</title>
  <script src="https://js.stripe.com/v3/"></script>
  <script src="https://crypto-js.stripe.com/crypto-onramp-outer.js"></script>
</head>`Generate a redirect URL using the Standalone function, passing in desired parameters:

`const standaloneOnramp = window.StripeOnramp.Standalone({
  source_currency: 'usd',
  amount: {source_amount: '42'},
  destination_networks: ['ethereum', 'bitcoin'],
  destination_currencies: ['eth', 'btc'],
  destination_currency: 'btc',
  destination_network: 'bitcoin'
});
const redirectUrl = standaloneOnramp.getUrl();`We allow the following parameters to be pre-populated:

- `source_currency`: The fiat currency for the transaction (`usd`only for now).
- `amount`: The fixed amount of fiat currency or cryptocurrency for this purchase. Specify a fiat amount by passing in`source_amount`(for example,`{source_amount: 42}`). Specify a cryptocurrency amount by passing in`destination_amount`(for example,`{destination_amount: 42}`). You can only specify one amount.
- `destination_currencies`: An array of cryptocurrencies you want to restrict to (for example,`[eth, usdc]`).
- `destination_networks`: An array of crypto networks you want to restrict to (for example,`[ethereum, polygon]`).
- `destination_network`: The default crypto network for this onramp (for example,`ethereum`).
- `destination_currency`: The default cryptocurrency for this onramp session (for example,`eth`).

Redirect your users to the URL for a prebuilt frontend integration of the crypto onramp on the standalone hosted onramp.

## Mint a session with a redirect URL

Similar to other integrations, you need to implement a server endpoint to create a new onramp session for every user visit. The onramp session creation request returns a redirect_url. Redirect your users to the URL for a fully customized and branded crypto onramp on the standalone hosted onramp.

Generate a crypto onramp session with a redirect_url by running the following curl command in your terminal:

Command Line`curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:`Sample response:

`{
  "id": "cos_0MpKNb589O8KAxCGjmaOVF8T",
  "object": "crypto.onramp_session",
  "client_secret": "cos_0MpKNb589O8KAxCGjmaOVF8T_secret_fqV1TAdhSCFeO9FW5HnygRXca00AwEHIOu8",
  "created": 1679701843,
  "livemode": false,
  "redirect_url": "https://crypto.link.com?session_hash=CCwaGwoZYWNjdF8yOERUNTg5TzhLQXhDR2JMbXh5WijU7vigBjIGmyBbkqO4Oi10eFHEaFln9gFSsTGQBoQf5qRZK-A0NhiEIeH3QaCMrz-d4oYotirrAd_Bkz4",
  "status": "initialized",
  "transaction_details": {
    "destination_currency": null,
    "destination_amount": null,
    "destination_network": null,
    "fees": null,
    "lock_wallet_address": false,
    "source_currency": null,
    "source_amount": null,
    "destination_currencies": [
      "btc",
      "eth",
      "sol",
      "usdc",
      "xlm"
    ],
    "destination_networks": [
      "bitcoin",
      "ethereum",
      "solana",
      "polygon",
      "stellar"
    ],
    "transaction_id": null,
    "wallet_address": null,
    "wallet_addresses": null
  }
}`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Generate a redirect URL](#generate-a-redirect-url)[Mint a session with a redirect URL](#mint-a-session-with-a-redirect-url)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`