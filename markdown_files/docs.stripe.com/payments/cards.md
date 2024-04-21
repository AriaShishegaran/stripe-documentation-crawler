htmlCards | Stripe Documentation[Skip to content](#main-content)Cards[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcards)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcards)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)# Cards

Learn more about accepting card payments with Stripe.Cards are linked to a debit or credit account at a bank. To complete a payment online, customers enter their card information at checkout. Cards are enabled by default and are supported by all Stripe products. You can manage payment methods from the Dashboard. Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow.

## The payment flow

A customer initiates a card payment at checkout by entering their credit card information. Depending on their card network and country location, customers have some card functionalities like additional security verification steps.

![A flowchart showing the three required and one optional step for a customer to pay with card.](https://b.stripecdn.com/docs-statics-srv/assets/pay-with-card.059eb99f8cad148c1aea3bb2a29b8284.svg)

Cards can act as the funding source for other Stripe payment products and methods like Link and wallets. For instance, customers can leverage Link to save their card payment data for fast checkout with any merchant that has Link enabled.

With wallets, customers can store their card details in a digital wallet. From your end, their payment method is managed using a wallet, but for the customer, the transaction shows up in their card history as a charge from their digital wallet provider.

## Supported card brands

Stripe supports several card brands, from large global networks like Visa and Mastercard to local networks like Cartes Bancaires in France or Interac in Canada. When you integrate Stripe, you can begin accepting a diversity of card brands without any additional configurations, including:

- American Express
- China UnionPay (CUP)
- Discover & Diners Club
- eftpos Australia
- Japan Credit Bureau (JCB)
- Mastercard
- Visa

Some card brands require additional configuration, such as Cartes Bancaires and Interac.

### Online card brand capabilities

The following table describes some of the different features and restrictions of each card brand online, including limitations on countries where Stripe users can accept the brand (Stripe Account Country), countries where most cardholders of the brand are located (Customer Country) and support for key features like 3D Secure Authentication, and Wallets (like Apple Pay and Google Pay).

NoteOther payment scenarios like setting up future payments, saving a card or placing a hold are supported across all card brands.

Stripe supports processing payments in 135+ currencies, but some card brand networks have limitations on supported currencies that charges can be made with.

Card BrandStripe Account CountryCustomer Country3D Secure AuthenticationWalletsVisaAll countriesGlobalMastercardAll countriesGlobalAmerican ExpressAll countries except Brazil, Malaysia, Thailand, and the United Arab EmiratesGlobal, except India1Discover & Diners ClubCanada, Japan, United Kingdom, United States, and the following European Economic Area countries: Austria, Belgium, Cyprus, Denmark, Estonia, Finland, France, Germany, Greece, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Slovakia, Slovenia, Spain, Sweden, and SwitzerlandGlobalChina UnionPayAustralia, Canada, Hong Kong, Malaysia, New Zealand, Singapore, United Kingdom, United States, Switzerland, and all countries in the European Economic Area except Croatia, Iceland, and LichtensteinGlobalNot supportedJapan Credit Bureau (JCB)Australia, Canada, Hong Kong, Japan, New Zealand, Singapore, Switzerland, United Kingdom, United States, and all countries in the European Economic Area except IcelandGlobalHong Kong, Japan, Singapore, Switzerland, United Kingdom, and all countries in the European Economic Area except IcelandCartes BancairesAll countries in the[SEPA](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area)regionFranceNot supportedeftposAustraliaAustraliaNot supported, payments will be routed to the co-brand networkNot supported1 For more information, see American Express card support for India-based businesses.

### Exclude card brands

You can disallow the use of specific card brands in the following ways:

- If you use Stripe Radar,[set up a rule](/radar/rules)to reject the desired brands.
- Add custom client-side code that checks the[brand](/api/cards/object#card_object-brand)of a card.
- Use the Payment Element to[filter cards by brand](/payments/customize-payment-methods#filter-card-brands).

## Geographic considerations

Stripe, along with other platforms, offer a solid infrastructure that handles secure payments and complies with specific regulations from different regions. This becomes particularly important with the roll-out of Strong Customer Authentication (SCA) rules in regulated markets like Europe and India, wherein additional verification steps are usually necessary.

It’s essential to ensure your Stripe integration is lined up with SCA rules and 3D Secure (3DS) criteria. Moreover, adjusting your approach to suit regional nuances—like installment payments and card brand preferences—is vital for seamless, compliant, and user-centered transactions.

### SCA and 3D Secure

Some banks, especially in regulated regions like Europe and India, might prompt the customer to authenticate a purchase (for example, by texting the customer a code to enter on the bank’s website). This authentication step is part of Strong Customer Authentication (SCA) Requirements. Making sure that your integration meets SCA requirements for 3DS can sometimes require extra steps.

SCA, a rule in effect as of September 14, 2019, as part of PSD2 regulation in Europe, requires changes to how your European customers authenticate online payments. Card payments require a different user experience, namely 3DS, to meet SCA requirements.

Stripe supports 3DS by default in Stripe Checkout, Payment Links, and a Hosted Invoice Page. You can configure your integration to use 3DS with Subscriptions and Connect with the following:

- [Payment Intents API](/payments/payment-intents)
- [Setup Intents API](/api/setup_intents)
- Elements
- Mobile SDKs

### Installments

Some regions have card brands that support installment payments - which are managed by the card issuer and not by creating Subscriptions or using SetupIntents with Stripe.

If you want to create recurring payments and your region or card network doesn’t support Messes sin interesses or  Installments in Brazil, see how to set up future payments or Subscriptions.

### Card brand choice

The European Union requires businesses to allow their customers the option to pick which card brand processes their transaction because cards in the EU might have both a local network, like Cartes Bancaires, and an affiliated card network, like Visa or Mastercard. You can enable this choice using Elements or Payments APIs so that customers can choose which card brand processes their payment.

### Accept card payments in India

The Reserve Bank of India (RBI) has specific regulations for online transactions that apply to Stripe accounts in India. Stripe Support includes a consolidated list of important resources, for many payment methods in the India FAQs.

## See also

- [Integrate card payment methods](/payments/payment-methods/integration-options)
- [Understand card updates and change default payment methods](/payments/cards/overview#card-updates)
- [Customize the way PaymentElements handle cards](/payments/customize-payment-methods)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[The payment flow](#payment-experience)[Supported card brands](#supported-card-brands)[Geographic considerations](#geographic-considerations)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`