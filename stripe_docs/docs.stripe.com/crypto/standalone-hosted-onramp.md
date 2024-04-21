# Using the standalone hosted onrampBeta

The standalone hosted onramp is a prebuilt frontend integration of the crypto onramp hosted at https://crypto.link.com. Platforms can integrate the crypto onramp by redirecting their users to the standalone hosted onramp, rather than hosting an embedded version of the onramp within their application.

[https://crypto.link.com](https://crypto.link.com)

[using the api](/crypto/using-the-api#how-to-pre-populate-transaction-parameters)

Platforms that want to embed the crypto onramp within their application can integrate the onramp.

[integrate the onramp](/crypto/integrate-the-onramp)

## Generate a redirect URL

Include the following scripts using script tags within the <head> element of your HTML. These scripts must always load directly from Stripe domains, https://js.stripe.com and https://crypto-js.stripe.com, for compatibility and PCI compliance. Don’t include the scripts in a bundle or host a copy yourself. If you do, your integration might break without warning.

[PCI compliance](/security/guide#validating-pci-compliance)

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

[https://crypto-js.stripe.com/crypto-onramp-outer.js](https://crypto-js.stripe.com/crypto-onramp-outer.js)

Generate a redirect URL using the Standalone function, passing in desired parameters:

We allow the following parameters to be pre-populated:

- source_currency: The fiat currency for the transaction (usd only for now).

- amount: The fixed amount of fiat currency or cryptocurrency for this purchase. Specify a fiat amount by passing in source_amount (for example, {source_amount: 42}). Specify a cryptocurrency amount by passing in destination_amount (for example, {destination_amount: 42}). You can only specify one amount.

- destination_currencies: An array of cryptocurrencies you want to restrict to (for example, [eth, usdc]).

- destination_networks: An array of crypto networks you want to restrict to (for example, [ethereum, polygon]).

- destination_network: The default crypto network for this onramp (for example, ethereum).

- destination_currency: The default cryptocurrency for this onramp session (for example, eth).

Redirect your users to the URL for a prebuilt frontend integration of the crypto onramp on the standalone hosted onramp.

## Mint a session with a redirect URL

Similar to other integrations, you need to implement a server endpoint to create a new onramp session for every user visit. The onramp session creation request returns a redirect_url. Redirect your users to the URL for a fully customized and branded crypto onramp on the standalone hosted onramp.

[create a new onramp session](/crypto/using-the-api)

Generate a crypto onramp session with a redirect_url by running the following curl command in your terminal:

[crypto onramp session](/crypto/using-the-api#api-reference)

Sample response:

[https://crypto.link.com?session_hash=CCwaGwoZYWNjdF8yOERUNTg5TzhLQXhDR2JMbXh5WijU7vigBjIGmyBbkqO4Oi10eFHEaFln9gFSsTGQBoQf5qRZK-A0NhiEIeH3QaCMrz-d4oYotirrAd_Bkz4](https://crypto.link.com?session_hash=CCwaGwoZYWNjdF8yOERUNTg5TzhLQXhDR2JMbXh5WijU7vigBjIGmyBbkqO4Oi10eFHEaFln9gFSsTGQBoQf5qRZK-A0NhiEIeH3QaCMrz-d4oYotirrAd_Bkz4)
