htmlSupported currencies | Stripe Documentation[Skip to content](#main-content)Currencies[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fcurrencies)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fcurrencies)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)
[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[About Stripe payments](/docs/payments/online-payments)# Supported currencies

See what currencies you can use for making charges and for paying out to your bank account.### Supported payment methods

In the Netherlands, you can accept these cards: Visa, Mastercard, American Express, JCB, China UnionPay, debit cards.

You can accept a range of other payment methods, depending on the country of your Stripe account (which you set when you activate it).

You can charge customers in one of more than 135 native currencies and receive funds in your currency. Businesses that have a global presence find this helpful because charging in a customer’s native currency can increase sales.

## Currency presentment and settlement

Currency comes into play in three places:

- The customer’s credit card currency
- The currency of the charge, called thepresentmentcurrency
- The currency accepted by your destination bank account or debit card, called thesettlementcurrency

If the charge currency differs from the customer’s credit card currency, the customer may be charged a foreign exchange fee by their credit card company. The customer may also be charged a fee by their credit card company if the credit card and your business are in different countries, regardless of the currency used.

If the charge currency differs from your settlement currency, Stripe converts the charge to your settlement currency. Refer to our payouts documentation to learn about the different bank account currencies that we support. For information on pricing, see the pricing guide.

## Supported presentment currencies

AustraliaAustriaBelgiumBrazilBulgariaCanadaCroatiaCyprusCzech RepublicDenmarkEstoniaFinlandFranceGermanyGibraltarGreeceHong KongHungaryIndiaIrelandItalyJapanLatviaLiechtensteinLithuaniaLuxembourgMalaysiaMaltaMexicoNetherlandsNew ZealandNorwayPolandPortugalRomaniaSingaporeSlovakiaSloveniaSpainSwedenSwitzerlandThailandUnited Arab EmiratesUnited KingdomUnited StatesStripe users can process charges in the following list of currencies with these exceptions:

- Currencies marked with`*`are not supported by American Express
- These currencies apply to card payments: other payment methods are often tied to a specific currency

Currencies presented as links are zero-decimal currencies, explained below.

Also note that the three-letter ISO code is provided for each currency below, but you should provide the ISO code in all lowercase letters when making the charge request.

- USD
- AED
- AFN*
- ALL
- AMD
- ANG
- AOA*
- ARS*
- AUD
- AWG
- AZN
- BAM
- BBD
- BDT
- BGN
- [BIF](#zero-decimal)
- BMD
- BND
- BOB*
- BRL*
- BSD
- BWP
- BYN
- BZD
- CAD
- CDF
- CHF
- [CLP](#zero-decimal)*
- CNY
- COP*
- CRC*
- CVE*
- CZK
- [DJF](#zero-decimal)*
- DKK
- DOP
- DZD
- EGP
- ETB
- EUR
- FJD
- FKP*
- GBP
- GEL
- GIP
- GMD
- [GNF](#zero-decimal)*
- GTQ*
- GYD
- HKD
- HNL*
- HTG
- HUF
- IDR
- ILS
- INR
- ISK
- JMD
- [JPY](#zero-decimal)
- KES
- KGS
- KHR
- [KMF](#zero-decimal)
- [KRW](#zero-decimal)
- KYD
- KZT
- LAK*
- LBP
- LKR
- LRD
- LSL
- MAD
- MDL
- [MGA](#zero-decimal)
- MKD
- MMK
- MNT
- MOP
- MUR*
- MVR
- MWK
- MXN
- MYR
- MZN
- NAD
- NGN
- NIO*
- NOK
- NPR
- NZD
- PAB*
- PEN*
- PGK
- PHP
- PKR
- PLN
- [PYG](#zero-decimal)*
- QAR
- RON
- RSD
- RUB
- [RWF](#zero-decimal)
- SAR
- SBD
- SCR
- SEK
- SGD
- SHP*
- SLE
- SOS
- SRD*
- STD*
- SZL
- THB
- TJS
- TOP
- TRY
- TTD
- TWD
- TZS
- UAH
- [UGX](#zero-decimal)
- UYU*
- UZS
- [VND](#zero-decimal)
- [VUV](#zero-decimal)
- WST
- [XAF](#zero-decimal)
- XCD
- [XOF](#zero-decimal)*
- [XPF](#zero-decimal)*
- YER
- ZAR
- ZMW

## Zero-decimal currencies

All API requests expect amounts to be provided in a currency’s smallest unit. For example, to charge 10 USD, provide an amount value of 1000 (that is, 1000 cents).

For zero-decimal currencies, still provide amounts as an integer but without multiplying by 100. For example, to charge ¥500, provide an amount value of 500.

Zero-decimal currencies:

- BIF
- CLP
- DJF
- GNF
- JPY
- KMF
- KRW
- MGA
- PYG
- RWF
- UGX
- VND
- VUV
- XAF
- XOF
- XPF

## Three-decimal currencies

The API supports three-decimal currencies for the standard payment flows, including Payment Intents, Refunds, and Disputes. However, to ensure compatibility with Stripe’s payments partners, these API calls require the least-significant (last) digit to be 0. Your integration must round amounts to the nearest ten. For example, 5.124 KWD must be rounded to 5120 or 5130.

Three-decimal currencies:

- BHD
- JOD
- KWD
- OMR
- TND

## Special cases

The following currencies have special conditions that you need to consider when creating payouts or charges.

CurrencyDescriptionIcelandic Króna (ISK)Effective 0:00 UTC on 2023-04-14, ISK becomes a zero-decimal currency. To maintain backwards compatibility, you must pass in amounts with two decimals. For example, to charge 5 ISK, provide an`amount`value of`500`. The`amount`value must be evenly divisible by 100:`100`,`200`,`300`, and so on. You can’t charge fractions of ISK.Hungarian Forint (HUF)Stripe treats HUF as a zero-decimal currency for payouts, even though you can charge two-decimal amounts. When you create a manual payout in HUF, only integer amounts that are evenly divisible by 100 are allowed. For example, if you have an available balance of HUF 10.45, you can pay out HUF 10 by submitting`1000`for the`amount`value. You can’t submit a payout for the full balance, HUF 10.45, because the`amount`value of`1045`is not evenly divisible by 100.New Taiwan Dollar (TWD)Stripe treats TWD as a zero-decimal currency for payouts, even though you can charge two-decimal amounts. When you create a manual payout in TWD, only integer amounts that are evenly divisible by 100 are allowed. For example, if you have an available balance of TWD 800.45, you can pay out TWD 800 by submitting`80000`for the`amount`value. You can’t submit a payout for the full balance, TWD 800.45, because the`amount`value of`80045`is not evenly divisible by 100.Ugandan Shilling (UGX)UGX was a decimal-based currency, but is now effectively a zero-decimal currency. To maintain backwards compatibility, you must pass in amounts with two decimals. For example, to charge 5 UGX, provide an`amount`value of`500`. The`amount`value must be evenly divisible by 100:`100`,`200`,`300`, and so on. In other words, you can’t charge fractions of UGX. For invoices where the`amount`is fractional after prorations, coupons, or taxes, Stripe automatically rounds that amount to the nearest number evenly divisible by 100. Any difference from rounding is credited or debited to the customer balance.## Minimum and maximum charge amounts

As Stripe’s processing fee combines a small fixed amount and a percentage, we enforce a minimum amount when creating a charge. This ensures you don’t lose money on a charge. The minimum amount you can charge depends on which bank account settlement currency the payment would be paid out to.

Settlement CurrencyMinimum Charge AmountUSD$0.50AED2.00 د.إAUD$0.50BGNлв1.00BRLR$0.50CAD$0.50CHF0.50 FrCZK15.00KčDKK2.50-kr.EUR€0.50GBP£0.30HKD$4.00HUF175.00 FtINR₹0.50JPY¥50MXN$10MYRRM 2NOK3.00-kr.NZD$0.50PLN2.00 złRONlei2.00SEK3.00-kr.SGD$0.50THB฿10If you only have one bank account in use and you create charges in the same currency as it, the minimum amount is simply what is listed for your currency. Charges that must be converted into your account’s default settlement currency must meet the equivalent minimum of the settlement currency. For example, if you have GBP and USD bank accounts, with GBP set as your default currency, any non-USD charges you create are converted to GBP. These charges must meet the minimum amount required for GBP (£0.30) after conversion.

There are some exceptions to the minimum charge amount limit (amount values as low as 1 is allowed) when you are creating payments with certain payment methods, such as iDEAL.

The only limit to the maximum amount you can charge a customer is a technical one. The amount value supports up to twelve digits for IDR (for example, a value of 999999999999 for a charge of 9,999,999,999.99 IDR), and up to eight digits for all other currencies (for example, a value of 99999999 for a charge of 999,999.99 USD).

Card networks can impose charge amount limits that are more restrictive than twelve digits.

## European credit cards

There are some factors, like pricing, in which credit cards from Europe are treated distinctly from credit cards from other regions. Stripe defines European cards as cards issued in the following countries:

Country CodeCountryADAndorraATAustriaBEBelgiumBGBulgariaHRCroatiaCYCyprusCZCzech RepublicDKDenmarkEEEstoniaFOFaroe IslandsFIFinlandFRFranceDEGermanyGIGibraltarGRGreeceGLGreenlandGGGuernseyVAHoly See (Vatican City State)HUHungaryISIcelandIEIrelandIMIsle of ManILIsraelITItalyJEJerseyLVLatviaLILiechtensteinLTLithuaniaLULuxembourgMTMaltaMCMonacoNLNetherlandsNONorwayPLPolandPTPortugalRORomaniaPMSaint Pierre and MiquelonSMSan MarinoSKSlovakiaSISloveniaESSpainSESwedenTRTürkiyeGBUnited Kingdom## See also

- [Creating Payments](/payments/payment-intents)
- [Getting Paid](/payouts)
- [Currency Conversions](/currencies/conversions)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Currency presentment and settlement](#currency-presentment-and-settlement)[Supported presentment currencies](#presentment-currencies)[Zero-decimal currencies](#zero-decimal)[Three-decimal currencies](#three-decimal)[Special cases](#special-cases)[Minimum and maximum charge amounts](#minimum-and-maximum-charge-amounts)[European credit cards](#european-credit-cards)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`