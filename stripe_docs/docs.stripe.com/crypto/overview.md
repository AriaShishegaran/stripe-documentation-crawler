# OverviewBeta

The Stripe fiat-to-crypto onramp enables individuals to securely purchase cryptocurrencies directly from your platform or Dapp at the time of checkout. The onramp is fully customizable and you can integrate it into your product or service.

Stripe acts as the merchant of record for these onramp transactions and takes full liability for all fraud and disputes. Stripe also handles all regulatory requirements, know your customer  (KYC) verifications, and sanctions screening. Customers have the option of saving payment methods, KYC data, and wallet information with Stripe, which makes the returning onramp experience much faster.

[know your customer](https://en.wikipedia.org/wiki/Know_your_customer)

You must submit an onramp application to access the onramp API. Most applications are reviewed within 48 hours.

- Create or sign in to your Stripe account, and submit the onramp application.

[onramp application](https://dashboard.stripe.com/register?redirect=%2Fcrypto-onramp%2Fapplication)

- Complete your Stripe application.

[Stripe application](https://dashboard.stripe.com/account/onboarding)

- After submitting the application in step 2, you can start development using test mode.

Stripe notifies you when your application is approved or if we require more information. Check the status of your application at any time by visiting the onboarding page.

[onboarding page](https://dashboard.stripe.com/crypto-onramp/onboarding)

Please reach out to support@stripe.com with any questions.

An example of Stripe’s fiat-to-crypto onramp being embedded into a 3rd party application

## Integration Options

Stripe provides multiple ways for your application to integrate with the onramp. Learn more about the features available for each one to find which one is right for your use case.

[No-code redirect URL generation](/crypto/no-code-quickstart)

- No code required

- Some customization, including the suggested source or destination amount, and the destination currency and network

- Send users to Stripe hosted onramp at crypto.link.com

[crypto.link.com](https://crypto.link.com)

- Stripe account optional

[Embeddable onramp](/crypto/integrate-the-onramp)

- Brand customization

- Dark mode supported

- Full parameter customization, including destination wallet address, with the Onramp API

[Onramp API](/crypto/using-the-api#api-reference)

[standalone onramp](/crypto/standalone-hosted-onramp)

- Some customization, including the suggested source or destination amount, and the destination currency and network

- Send users to the Stripe hosted onramp at crypto.link.com

[crypto.link.com](https://crypto.link.com)

- Stripe account optional

[standalone onramp](/crypto/standalone-hosted-onramp)

- Brand customization

- Full parameter customization, including destination wallet address, with the Onramp API

[Onramp API](/crypto/using-the-api#api-reference)

- Send users to the Stripe hosted onramp at crypto.link.com

[crypto.link.com](https://crypto.link.com)

†The standalone hosted onramp provides two different integration options with different levels of customization available. See the standalone hosted onramp docs for more information.

[standalone hosted onramp docs](/crypto/standalone-hosted-onramp)

## Feature Set

- Ability to pre-populate parameters of the transaction (wallet_addresses, source and destination currencies, source and destination amounts, supported networks)

- Free for platforms to integrate—fees are paid by users

- Real-time quotes, automated KYC, and multi-chain support in just a few lines of code

- Implement using an embeddable widget, customizable to the look and feel of your brand

- Every status change within a session generates a webhook

- No fraud liability for platforms—Stripe handles all disputes

- Returning users can use 1-click checkout with Link, Stripe’s consumer account infrastructure

- All eligible for delivery of crypto instantly, post-KYC

- ETH

- SOL*

- MATIC

- BTC

- XLM*

- USDC (Ethereum)

- USDC (Solana)*

- USDC (Polygon)*

- USDC (Stellar)*

*SOL, XLM, USDC (Solana), USDC (Stellar), and USDC (Polygon) aren’t available in New York.
