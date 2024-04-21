htmlBackend integration recipes | Stripe Documentation[Skip to content](#main-content)Integration recipes[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fcrypto%2Fintegration-recipes)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fcrypto%2Fintegration-recipes)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)
[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Crypto](/docs/crypto)[Fiat-to-crypto onramp](/docs/crypto)# Backend integration recipesBeta

Learn best practices for integrating the onramp for different web3 use cases.To optimize the user experience, frame the onramp as a native component of your application. In addition to frontend design, you often want to pre-populate onramp parameters when creating an onramp session in the backend. The following are some common use cases and suggested implementations.

### Wallet

Wallet users have two main onramp entry points—wallet funding and transaction top up.

1. Wallet funding![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You can proactively prompt users to fund their wallet after they create a new wallet or when their funds are critically low.

In these cases, you might want to specify the following:

- `wallet_addresses`: Use the wallet address already in use.
- `destination_networks`: Set to the default or selected network to reduce user confusion.
- `destination_currencies`: Leaving this blank is acceptable but you can optionally restrict it to the native gas token or any desired cryptocurrencies (for example, if you offer a Defi service in USDC, consider the case where the user likely needs both USDC and the gas token).
- `destination_network`: Leave this blank to inherit first value of supported network.
- `destination_currency`: Leave this blank to inherit first value of supported cryptocurrencies.

Command Line`curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "customer_ip_address"="8.8.8.8" \
  -d "wallet_addresses[ethereum]"="0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2" \
  -d "wallet_addresses[solana]"="bufoH37MTiMTNAfBS4VEZ94dCEwMsmeSijD2vZRShuV" \
  -d "destination_networks[]"="ethereum" \
  -d "destination_networks[]"="solana"`2. Transaction top-up![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

When a Dapp or the user proposes a transaction, you might detect that the transaction fails because of insufficient funds. In this case, you can calculate the delta required for the transaction to complete. However, it’s often difficult to detect the requested amount or cryptocurrency for ERC or SPL tokens.

In these cases, you might want to specify the following:

- `wallet_addresses`: Use the wallet address in use
- `destination_networks`: Set to the selected network
- `destination_currencies`: Restrict to the missing currencies when possible
- `destination_network`: Set to the selected network (a required value if you want to set the amount)
- `destination_currency`: Set to the target currency (a required value if you want to set the amount)
- `destination_amount`: Set to the balance differences and leave enough buffer room for gas when applicable

Command Line`curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "customer_ip_address"="8.8.8.8" \
  -d "wallet_addresses[ethereum]"="0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2" \
  -d "destination_networks[]"="ethereum" \
  -d "destination_currencies[]"="usdc" \
  -d "destination_network"="ethereum" \
  -d "destination_currency"="usdc" \
  -d "destination_amount"="10"`### Dapp or NFT checkout

In some applications, you can use the onramp in checkout when you know what the destination amount is. For example, a Dapp might be used to sell memberships for a fixed price, or when the user is looking to buy a specific NFT from a marketplace.

In these cases, you might want to specify the following:

- `wallet_addresses`—Use the connected wallet address
- `destination_networks`—Use the connected network
- `destination_currencies`—Use the presentment currency (that is, the price in the currency the goods are quoted in)
- `destination_network`—Set to the selected network above (a required value if you want to set the amount)
- `destination_currency`—Set to the target currency above (a required value if you want to set amount)
- `destination_amount`—Set it to either the balance difference or to cover the entire purchase amount. Some users adopt both using on-chain analytics with just about an even split. A user might choose the full amount to simplify their tax cost basis or to not spend accumulated assets. In both cases, you should leave room for gas.

Command Line`curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "customer_ip_address"="8.8.8.8" \
  -d "wallet_addresses[ethereum]"="0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2" \
  -d "destination_networks[]"="ethereum" \
  -d "destination_currencies[]"="eth" \
  -d "destination_network"="ethereum" \
  -d "destination_currency"="eth" \
  -d "destination_amount"="0.2343"`### DEX

A DEX presents a unique opportunity to let users buy any cryptocurrency with fiat. While a DEX can incrementally prompt users to top up crypto when exchanging arbitrary crypto pairs using an existing interface, it’s preferable to have a dedicated user flow that focuses on fiat to crypto only.

As the onramp lets you own your brand and user experience, a DEX can build an onramp widget that takes advantage of Stripe’s ability to process fiat into selective cryptocurrencies, and DEX can complete the final leg exchanging it to arbitrary currencies. A DEX can also build an onramp widget for a specific token. For example, a DAO might endorse a specific liquidity pool and use a DEX to distribute their tokens and onboard new users with fiat.

In these cases, you might want to specify the following

- `wallet_addresses`—Use the wallet address already in use
- `destination_networks`—Set to the selected network
- `destination_currencies`—Restrict to the selected cryptocurrency
- `destination_network`—Set to selected network (a required value if you want to set the amount)
- `destination_currency`—Set to the target currency (a required value if you want to set the amount)
- `destination_amount`—Set only if you can collect the user’s intent ahead of time—leave blank for Stripe to suggest smart default values

Command Line`curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "customer_ip_address"="8.8.8.8" \
  -d "wallet_addresses[ethereum]"="0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2" \
  -d "destination_networks[]"="ethereum" \
  -d "destination_currencies[]"="eth" \
  -d "destination_network"="ethereum" \
  -d "destination_currency"="eth"`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`