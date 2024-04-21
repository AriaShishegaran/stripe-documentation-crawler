htmlOnramp no-code quickstart | Stripe Documentation[Skip to content](#main-content)No-code quickstart[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fcrypto%2Fno-code-quickstart)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fcrypto%2Fno-code-quickstart)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)
[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Crypto](/docs/crypto)[Fiat-to-crypto onramp](/docs/crypto)# Onramp no-code quickstartBeta

Customize and generate a redirect URL to the standalone hosted onramp.Platforms can direct users to purchase crypto with a link to the standalone hosted onramp at https://crypto.link.com. The standalone hosted onramp redirect URL supports parameter customization and lets you prefill fields such as the destination currency and the source amount or destination amount.

Share the link by sending it directly to users or by displaying it with a button, as in the example below.

You can also generate a redirect URL with code using the Standalone function and passing in the desired fields. See the standalone hosted onramp docs to learn about what else you can do with the standalone hosted onramp, or to customize additional parameters.

Source amountDestination amountSource amount (USD)Enter the amount of fiat you want to exchange into crypto$ValueDestination currencySelect a destination currencyBitcoinEthereumSolanaMaticUSDC (Ethereum)USDC (Polygon)USDC (Solana)Send users to this URL directly

`https://crypto.link.com`[Copy to clipboard](#)LivemodeExample button with redirect URL

[Buy Crypto](https://crypto.link.com)Generate a redirect URL with code

`const standaloneOnramp = window.StripeOnramp.Standalone();
const redirectUrl = standaloneOnramp.getUrl();

return (
  <a href={redirectUrl}>
    Buy Crypto
  </a>
);`Want to pre-populate the wallet address or embed the onramp into your application?

Submit an onramp application and try the embeddable version of the onramp.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`