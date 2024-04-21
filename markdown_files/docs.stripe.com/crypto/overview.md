htmlOverview | Stripe Documentation[Skip to content](#main-content)Overview[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fcrypto%2Foverview)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fcrypto%2Foverview)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)
[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Crypto](/docs/crypto)[Fiat-to-crypto onramp](/docs/crypto)# OverviewBeta

Learn about the Stripe fiat-to-crypto onramp.The Stripe fiat-to-crypto onramp enables individuals to securely purchase cryptocurrencies directly from your platform or Dapp at the time of checkout. The onramp is fully customizable and you can integrate it into your product or service.

Stripe acts as the merchant of record for these onramp transactions and takes full liability for all fraud and disputes. Stripe also handles all regulatory requirements, know your customer  (KYC) verifications, and sanctions screening. Customers have the option of saving payment methods, KYC data, and wallet information with Stripe, which makes the returning onramp experience much faster.

You must submit an onramp application to access the onramp API. Most applications are reviewed within 48 hours.

### To submit your application:

1. Create or sign in to your Stripe account, and submit the[onramp application](https://dashboard.stripe.com/register?redirect=%2Fcrypto-onramp%2Fapplication).
2. Complete your[Stripe application](https://dashboard.stripe.com/account/onboarding).
3. After submitting the application in step 2, you can start development using test mode.

Stripe notifies you when your application is approved or if we require more information. Check the status of your application at any time by visiting the onboarding page.

Please reach out to support@stripe.com with any questions.

![An example of Stripe's fiat-to-crypto onramp being embedded into a 3rd party application](https://b.stripecdn.com/docs-statics-srv/assets/crypto-onramp-overview.c9ec889d4c12403f4b2dbc17600dc640.png)

An example of Stripe’s fiat-to-crypto onramp being embedded into a 3rd party application

## Integration Options

Stripe provides multiple ways for your application to integrate with the onramp. Learn more about the features available for each one to find which one is right for your use case.

OptionOverviewBest for[No-code redirect URL generation](/crypto/no-code-quickstart)- No code required
- Some customization, including the suggested source or destination amount, and the destination currency and network
- Send users to Stripe hosted onramp at[crypto.link.com](https://crypto.link.com)
- Stripe account optional

Users who don’t want to write any code and have static parameter values[Embeddable onramp](/crypto/integrate-the-onramp)Recommended- Brand customization
- Dark mode supported
- Full parameter customization, including destination wallet address, with the[Onramp API](/crypto/using-the-api#api-reference)

Users who want full customization and to embed the onramp widget directly into their applicationRedirect URL to[standalone onramp](/crypto/standalone-hosted-onramp)†- Some customization, including the suggested source or destination amount, and the destination currency and network
- Send users to the Stripe hosted onramp at[crypto.link.com](https://crypto.link.com)
- Stripe account optional

Users who want light customization and a lightweight frontend integrationMinted session with redirect URL to[standalone onramp](/crypto/standalone-hosted-onramp)†- Brand customization
- Full parameter customization, including destination wallet address, with the[Onramp API](/crypto/using-the-api#api-reference)
- Send users to the Stripe hosted onramp at[crypto.link.com](https://crypto.link.com)

Users who want full customization but don’t want to host the onramp themselves†The standalone hosted onramp provides two different integration options with different levels of customization available. See the standalone hosted onramp docs for more information.

## Feature Set

Customizability- Ability to pre-populate parameters of the transaction (wallet_addresses, source and destination currencies, source and destination amounts, supported networks)
- Free for platforms to integrate—fees are paid by users
- Real-time quotes, automated KYC, and multi-chain support in just a few lines of code
- Implement using an embeddable widget, customizable to the look and feel of your brand
- Every status change within a session generates a webhook
- No fraud liability for platforms—Stripe handles all disputes
- Returning users can use 1-click checkout with Link, Stripe’s consumer account infrastructure

Payment MethodsCredit, Debit, ACH, Google Pay- All eligible for delivery of cryptoinstantly, post-KYC

Currencies- ETH
- SOL*
- MATIC
- BTC
- XLM*
- USDC (Ethereum)
- USDC (Solana)*
- USDC (Polygon)*
- USDC (Stellar)*

Country AvailabilityUS (excl. Hawaii)*SOL, XLM, USDC (Solana), USDC (Stellar), and USDC (Polygon) aren’t available in New York.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`