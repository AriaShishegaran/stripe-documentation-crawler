htmlCrypto payouts | Stripe Documentation[Skip to content](#main-content)Crypto payouts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fcrypto-payouts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fcrypto-payouts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Crypto payoutsBeta

Learn how to enable crypto payouts on your platform.BetaAccess to Crypto payouts is currently limited to beta users. If you’re interested in trying it out, fill out the interest form and select Paying out third parties in crypto.

### Account types

Connect platforms can work with three different[account types](https://stripe.com/docs/connect/accounts).This content applies only to Express accounts.Crypto payouts enable your platform to pay out in crypto, starting with USDC. You can use crypto payouts with your existing integration to avoid managing crypto yourself—your platform’s funds can remain in fiat currency, and Stripe handles converting to crypto and then paying it out.

## Supported countries

Crypto payouts enable platforms in the US to pay out to connected accounts in the following countries:

ArmeniaAustriaAzerbaijanBahrainBeninBhutanBosnia & HerzegovinaBruneiBulgariaCanadaCroatiaCyprusCzech RepublicDenmarkDjiboutiDominicaEcuadorEl SalvadorEstoniaFinlandFranceGambiaGermanyGhanaGreeceGrenadaGuatemalaHong KongHungaryIndiaIrelandJamaicaJapanKuwaitLatviaLiechtensteinLithuaniaMaltaMauritiusMoldovaMontenegroNetherlandsNew ZealandNigerNorwayOmanPanamaPhilippinesPolandPortugalRomaniaSamoaSan MarinoSenegalSingaporeSlovakiaSloveniaSouth KoreaSpainSt. LuciaSt. Vincent & GrenadinesSwedenSwitzerlandTunisiaUnited KingdomUnited StatesRegional considerationsUnited StatesCrypto payouts aren’t currently available in New York or Hawaii.

## Before you begin

1. Activated US Platform: Your Platform must be in the US and activated. You can activate it by[registering your platform](https://dashboard.stripe.com/connect/tasklist),[activating your account](https://dashboard.stripe.com/account/onboarding), and[completing the platform profile](https://dashboard.stripe.com/connect/settings/profile).
2. Individual recipients: Recipients paid in crypto must be individuals or sole proprietors. Paying companies and non-profits in crypto isn’t currently supported.
3. Express Dashboard access: To pay an individual in crypto, create a connected account for them with access to the[Express Dashboard](/connect/express-dashboard). They can link a crypto wallet and choose their preferred currency in this Dashboard.
4. Pay with the Transfers API: You must use the[Transfers API](/api/transfers)within your integration to pay in crypto. Transfers to connected accounts with linked crypto wallets are converted from fiat to USDC, enabling you to pay in USDC while your platform balance stays in fiat. If you haven’t built an integration yet, you can pay in crypto using a[no-code](/connect/add-and-pay-out-guide?dashboard-or-api?dashboard-or-api=dashboard)or[programmatic integration](/connect/add-and-pay-out-guide?dashboard-or-api?dashboard-or-api=api).

## Paying out in crypto with Connect

Sellers, freelancers, content creators, and service providers around the world are increasingly looking to be paid directly in crypto. Being paid in crypto helps them access international platforms that otherwise could not support them, or because they regularly use crypto and often convert funds from fiat. With crypto payouts, you can now support these users without writing a single line of code.

### How it works

When you opt in to crypto payouts and provide your users access to the Express Dashboard, your users can link a crypto wallet with their account and set their default currency to USDC. Your users can link a crypto wallet using the Express Dashboard.

When a user links a crypto wallet, they immediately see a new USDC balance on their connected account. The USDC balance works like any other local currency balance. You can Transfer funds into the balance and the funds are paid out to their linked crypto wallet instead of their bank account. When you create Transfers in USD, they automatically convert to the preferred currency of your recipients. This simplifies your integration and enables you to have a unified integration across fiat and crypto payouts.

Connected account users can view account information, such as their crypto account balance and upcoming payouts, using the Express Dashboard. Stripe handles all compliance requirements, and generates tax forms for recipients paid in crypto.

### Getting started

After Stripe approves your use case, your users can link a crypto wallet to their account and set USDC as their preferred currency. For any user with a default currency set to USDC, Stripe automatically converts Transfers to USDC.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Supported countries](#supported-countries)[Before you begin](#before-you-begin)[Paying out in crypto with Connect](#paying-out-in-crypto-with-connect)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`