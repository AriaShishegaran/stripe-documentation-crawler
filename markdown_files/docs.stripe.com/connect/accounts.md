htmlChoose your account type | Stripe Documentation[Skip to content](#main-content)Choose your account type[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Faccounts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Faccounts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Choose your account type

Learn more about the different types of Stripe accounts you can use with Connect.When using Connect, you must create an account (known as a connected account) for each user that receives money on your platform. You create these accounts when a user signs up for your platform. The type of account you choose for your user determines the Stripe integration you need to build (from Stripe-hosted to completely custom) and the operational responsibilities (such as chargebacks, user support, etc). Connect supports the following account types that are each designed for different use cases:

- [Standard](/connect/standard-accounts)
- [Express](/connect/express-accounts)
- [Custom](/connect/custom-accounts)

## Account types

You must consider several factors when choosing an account type. Integration effort and user experience are especially important because they can affect engineering resource expenditure and conversion rates. You can’t change a connected account’s type after creation.

Extensions building on Connect must use OAuth to connect to Standard accounts.

Stripe recommends you use Express or Standard accounts to minimize integration effort. If you want more control over the user experience, Express or Custom accounts might meet your needs better. To know the account type recommended for your business, refer to your platform profile.

There’s an additional cost for using Express or Custom accounts.

StandardExpressCustomIntegration effortLowestLowSignificantly higherIntegration methodAPI or OAuthAPIAPIFraud and dispute liabilityUserPlatformPlatformPlatform can specify payout timing?Yes, with[Platform controls](/connect/platform-controls-for-stripe-dashboard-accounts)YesYesOnboardingStripeStripePlatform or StripeIdentity information gatheringStripeStripePlatform or StripeUser can access the Dashboard?Yes, full DashboardYes, Express DashboardNoUser support provided byPlatform and StripePlatform and StripePlatformAutomatic updates for new compliance requirementsYesYesNoSupport new countries without integration changesYesYesNoIdeal for platformsWith experienced online businesses as usersAny typeWith significant engineering resources to dedicate to a fully white-labeled experienceUser refers to the person with the connected account (that is, the person being paid for providing goods or services through your platform). With Standard accounts, the user is responsible for fraud and disputes when using direct charges, but this may vary operationally for destination charges.

## Express accounts

With Express accounts, Stripe handles the onboarding and identity verification processes. The platform has the ability to specify charge types and set the connected account’s payout settings programmatically. The platform is responsible for handling disputes and refunds, which is similar to a Custom account.

Although your user has interactions with Stripe, they primarily interact with your platform, particularly for the core payment processing functionality. For Express account holders, Stripe provides an Express Dashboard (a lighter version of the Dashboard) that allows them to manage their personal information and see payouts to their bank.

Use Express accounts when you:

- Want to get started quickly (letting Stripe handle account onboarding, management, and identity verification)
- Want to use[destination charges](/connect/destination-charges)or[separate charges and transfers](/connect/separate-charges-and-transfers)
- Want significant control over your user’s experience

Examples of platforms that would use Express accounts include, but are not limited to: a home-rental marketplace like Airbnb, or a ride-hailing service like Lyft.

Global compliance requirements do evolve and change over time. With Express, Stripe proactively collects information when requirements change. For best practices on how to communicate to your users when this happens, visit the guide for Express accounts.

### Express account availability

Select one of the available countries when you create an Express account. You can’t change the country of your Express account after you create the account.

Some countries are available only when using cross-border payouts.

To know when Express accounts are available in your country, contact Stripe.

AlbaniaAntigua & BarbudaArgentinaArmeniaAustraliaAustriaBahamasBahrainBelgiumBoliviaBosnia & HerzegovinaBotswanaBrazilBruneiBulgariaCambodiaCanadaChileColombiaCosta RicaCôte d’IvoireCroatiaCyprusCzech RepublicDenmarkDominican RepublicEcuadorEgyptEl SalvadorEstoniaEthiopiaFinlandFranceGambiaGermanyGhanaGreeceGuatemalaGuyanaHong KongHungaryIcelandIndiaIndonesiaIrelandIsraelItalyJamaicaJapanJordanKenyaKuwaitLatviaLiechtensteinLithuaniaLuxembourgMacao SAR ChinaMadagascarMalaysiaMaltaMauritiusMexicoMoldovaMonacoMongoliaMoroccoNamibiaNetherlandsNew ZealandNigeriaNorth MacedoniaNorwayOmanPakistanPanamaParaguayPeruPhilippinesPolandPortugalQatarRomaniaRwandaSaudi ArabiaSenegalSerbiaSingaporeSlovakiaSloveniaSouth AfricaSouth KoreaSpainSri LankaSt. LuciaSwedenSwitzerlandTaiwanTanzaniaThailandTrinidad & TobagoTunisiaTurkeyUnited Arab EmiratesUnited KingdomUnited StatesUruguayUzbekistanVietnam## Standard accounts

A Standard Stripe account is a conventional Stripe account where the account holder (that is, your platform’s user) has a relationship with Stripe, is able to log in to the Dashboard, and can process charges on their own.

Use Standard accounts when you:

- Want to get started quickly and don’t need a lot of control over your user’s experience
- Want to use[direct charges](/connect/direct-charges)
- Have users that are familiar with running online businesses or might already have a Stripe account
- Prefer that Stripe handles direct communication with the user for account issues (for example, to request more information for identity verification purposes)

Examples of platforms that would use Standard accounts include, but are not limited to: a store builder like Shopify, or a software as a service like Invoice2go.

Global compliance requirements do evolve and change over time. With Standard, Stripe proactively collects information when requirements change. For best practices on how to communicate to your users when this happens, visit the guide for Standard accounts.

Country can't be changedYou can’t change the country of your Standard account after you create the account.

## Custom accounts

A Custom Stripe account is almost completely invisible to the account holder. You—the platform—are responsible for all interactions with your user, including collecting any information Stripe needs. You have the ability to change all of the account’s settings, including the payout bank or debit card account, programmatically.

Custom account holders don’t have access to the Dashboard, and Stripe doesn’t contact them directly.

Use Custom accounts when you:

- Want complete control over your user’s experience
- Can build the significant infrastructure required to collect user information, create a user dashboard, and handle support
- Want to handle all communication with your users, rather than having your users contact Stripe directly

Creating and managing Custom accounts requires a larger integration effort than the other account types. To learn more, see Using Connect with Custom accounts.

Global compliance requirements do evolve and change over time. For best practices on how to communicate to your users when requirements change, see the guide for Custom accounts.

If you decide to use Custom accounts, Stripe recommends you use Connect Onboarding for Custom accounts to collect onboarding and verification information from your users. This would decrease your integration effort and eliminate the need to update your onboarding form when requirements change over time.

### Custom accounts availability

Select one of the available countries when you create an Custom account. You can’t change the country of your Custom account after you create account.

Some countries are available only when using cross-border payouts.

To know when Custom accounts are available in your country, contact Stripe.

AlbaniaAntigua & BarbudaArgentinaArmeniaAustraliaAustriaBahamasBahrainBelgiumBoliviaBosnia & HerzegovinaBotswanaBrazilBruneiBulgariaCambodiaCanadaChileColombiaCosta RicaCôte d’IvoireCroatiaCyprusCzech RepublicDenmarkDominican RepublicEcuadorEgyptEl SalvadorEstoniaEthiopiaFinlandFranceGambiaGermanyGhanaGreeceGuatemalaGuyanaHong KongHungaryIcelandIndiaIndonesiaIrelandIsraelItalyJamaicaJapanJordanKenyaKuwaitLatviaLiechtensteinLithuaniaLuxembourgMacao SAR ChinaMadagascarMalaysiaMaltaMauritiusMexicoMoldovaMonacoMongoliaMoroccoNamibiaNetherlandsNew ZealandNigeriaNorth MacedoniaNorwayOmanPakistanPanamaParaguayPeruPhilippinesPolandPortugalQatarRomaniaRwandaSaudi ArabiaSenegalSerbiaSingaporeSlovakiaSloveniaSouth AfricaSouth KoreaSpainSri LankaSt. LuciaSwedenSwitzerlandTaiwanTanzaniaThailandTrinidad & TobagoTunisiaTurkeyUnited Arab EmiratesUnited KingdomUnited StatesUruguayUzbekistanVietnam## See also

- [Express Accounts](/connect/express-accounts)
- [Standard Accounts](/connect/standard-accounts)
- [Custom Accounts](/connect/custom-accounts)
- [Account capabilities](/connect/account-capabilities)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Account types](#choosing-approach)[Express accounts](#express-accounts)[Standard accounts](#standard-accounts)[Custom accounts](#custom-accounts)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`