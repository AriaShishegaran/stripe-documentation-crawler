htmlCross-border payouts | Stripe Documentation[Skip to content](#main-content)Cross-border payouts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fcross-border-payouts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fcross-border-payouts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Cross-border payoutsUS only

Transfer and pay out funds around the world.Cross-border payouts enable you to pay sellers, freelancers, content creators, and service providers in their local currencies. You can transfer funds to connected accounts in other countries with your existing platform account and charge configuration.

## Fund flow restrictions

The following fund flows are generally supported in countries for cross-border payouts:

- [Separate charges and transfers](/connect/separate-charges-and-transfers)without the`on_behalf_of`parameter
- [Top-ups and transfers](/connect/top-ups)
- [Destination charges](/connect/destination-charges)

Direct charges and destination charges with the on_behalf_of parameter aren’t supported. However, some countries have additional limitations.

For Brazil, India, and Thailand, only the following fund flows are supported:

- [Separate charges and transfers](/connect/separate-charges-and-transfers)without the`on_behalf_of`parameter
- Top-up and transfers

## Supported countries

Cross-border payouts enable US platforms using separate charges and transfers, destination charges, or top-ups to pay out to connected accounts in the following countries:

AlbaniaAlgeriaPreviewAngolaPreviewAntigua & BarbudaArgentinaArmeniaAustraliaAustriaAzerbaijanPreviewBahamasBahrainBangladeshPreviewBelgiumBeninPreviewBhutanPreviewBoliviaBosnia & HerzegovinaBotswanaBruneiBulgariaCambodiaCanadaChileColombiaCosta RicaCôte d’IvoireCroatia*CyprusCzech Republic*DenmarkDominican RepublicEcuadorEgyptEl SalvadorEstoniaEthiopiaFinlandFranceGabonPreviewGambiaGermanyGhanaGreeceGuatemalaGuyanaHong KongHungaryIceland*IndiaIndonesiaIrelandIsraelItalyJamaicaJapanJordanKazakhstanPreviewKenyaKuwaitLaosPreviewLatviaLiechtenstein*LithuaniaLuxembourgMacao SAR ChinaMadagascarMalaysiaMaltaMauritiusMexicoMoldovaMonacoMongoliaMoroccoMozambiquePreviewNamibiaNetherlandsNew ZealandNigerPausedNigeriaNorth MacedoniaNorwayOmanPakistanPanamaParaguayPeruPhilippinesPolandPortugalQatarRomaniaRwandaSan MarinoPreviewSaudi ArabiaSenegalSerbiaSingaporeSlovakiaSloveniaSouth AfricaSouth KoreaSpainSri LankaSt. LuciaSwedenSwitzerland*TaiwanTanzaniaThailandTrinidad & TobagoTunisiaTurkeyUnited Arab EmiratesUnited KingdomUruguayUzbekistanVietnam* Bank accounts in countries with an asterisk (*) can only receive Euro (EUR) payouts.

NoteStripe might pause payouts to countries in the preview program while any issues are resolved. We don’t provide advance notice to you as the owner of the platform or to the owners of your connected accounts.

Some countries have special requirements for payments received from outside their country’s borders, or limitations on the supported fund flows. Those countries might also have higher minimum payout amounts.

Stripe isn’t responsible for providing direct support for accounts on the recipient service agreement. However, the platform can reach out to Stripe for support for these accounts.

## Restrictions and requirements

- The platform must be in the US.
- Funds must come from separate charges and transfers, destination charges without`on_behalf_of`(OBO), or top-ups.
- The platform must be the business of record. Consequently,[destination charges with on_behalf_of (OBO)](/connect/destination-charges#settlement-merchant)aren’t supported.
- Connected accounts must onboard under the[recipient service agreement](/connect/service-agreement-types#recipient). That means transfers to`recipient`accounts take an extra 24 hours to become available in the connected account’s balance.
- US connected accounts don’t support cross-border payouts; onboard US connected accounts using the full[terms of service](/connect/service-agreement-types).
- You can’t make cross-border[instant payouts](/connect/instant-payouts).

The onboarding specifications for cross-border payouts vary by destination country. To learn more, see:

- [Required verification information](/connect/required-verification-information)
- [Supported settlement currencies](/connect/payouts-connected-accounts#supported-settlement)
- [Bank account formats](/connect/payouts-bank-accounts)

## Get started

Existing Connect platforms - Select the recipient service agreement at account creation.

New Connect platforms - Follow one of the guides below that best fits your use case, and make sure to specify the recipient service agreement in the account creation step.

- [Collect payments and then pay out](/connect/collect-then-transfer-guide)
- [Pay out money](/connect/add-and-pay-out-guide)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Fund flow restrictions](#fund-flow-restrictions)[Supported countries](#supported-countries)[Restrictions and requirements](#restrictions-and-requirements)[See also](#get-started)Products Used[Connect](/connect)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`