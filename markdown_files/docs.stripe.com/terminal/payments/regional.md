htmlRegional considerations | Stripe Documentation[Skip to content](#main-content)Regional considerations[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fpayments%2Fregional)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fpayments%2Fregional)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)# Regional considerations

Learn about regional considerations for integrating Terminal in different countries.​​For the most part, you’ll be able to use a single Terminal integration in all supported countries. However, due to local payment methods or regulations there are some country-specific requirements. After going through the sample integration, use this guide to learn about country-specific requirements for Terminal.

NoteIn order to process Terminal payments, both the Stripe account receiving the funds and the location associated with the reader must be in the same country, accepting local currency only.

CountryChoose a country…## Availability

Refer to the following table to understand which readers and SDK platforms you can use in each country.

CountriesAndroid**iOS**JavaScriptServer-DrivenUnited States![](https://b.stripecdn.com/docs-statics-srv/assets/84052c4398178d23ae59cfdfd4c1a4e3.png)

Stripe Reader M2Bluetooth or USB![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/cbf74926d4a083809dadd9b11bd16740.png)

Tap to PayEmbedded![](https://b.stripecdn.com/docs-statics-srv/assets/84052c4398178d23ae59cfdfd4c1a4e3.png)

Stripe Reader M2Bluetooth![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/cbf74926d4a083809dadd9b11bd16740.png)

Tap to PayEmbedded![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmartAustria+BelgiumCanadaCzech Republic+DenmarkFinland+GermanyIrelandItalyLuxembourg+Malaysia+Norway+Portugal+SpainSwedenSwitzerland+![](https://b.stripecdn.com/docs-statics-srv/assets/ba9684bdc9a5096c66da38a228968305.png)

WisePad 3Bluetooth or USB![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/cbf74926d4a083809dadd9b11bd16740.png)

Tap to Pay*Embedded![](https://b.stripecdn.com/docs-statics-srv/assets/ba9684bdc9a5096c66da38a228968305.png)

WisePad 3Bluetooth![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700*Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmartUnited Kingdom![](https://b.stripecdn.com/docs-statics-srv/assets/ba9684bdc9a5096c66da38a228968305.png)

WisePad 3Bluetooth or USB![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/cbf74926d4a083809dadd9b11bd16740.png)

Tap to PayEmbedded![](https://b.stripecdn.com/docs-statics-srv/assets/ba9684bdc9a5096c66da38a228968305.png)

WisePad 3Bluetooth![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/cbf74926d4a083809dadd9b11bd16740.png)

Tap to PayEmbedded![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700*Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmartNew Zealand+Singapore![](https://b.stripecdn.com/docs-statics-srv/assets/ba9684bdc9a5096c66da38a228968305.png)

WisePad 3Bluetooth or USB![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/cbf74926d4a083809dadd9b11bd16740.png)

Tap to PayEmbedded![](https://b.stripecdn.com/docs-statics-srv/assets/ba9684bdc9a5096c66da38a228968305.png)

WisePad 3Bluetooth![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700*Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmartAustralia![](https://b.stripecdn.com/docs-statics-srv/assets/ba9684bdc9a5096c66da38a228968305.png)

WisePad 3Bluetooth or USB![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/cbf74926d4a083809dadd9b11bd16740.png)

Tap to Pay*Embedded![](https://b.stripecdn.com/docs-statics-srv/assets/ba9684bdc9a5096c66da38a228968305.png)

WisePad 3Bluetooth![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/cbf74926d4a083809dadd9b11bd16740.png)

Tap to PayEmbedded![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700*Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmartFranceNetherlands![](https://b.stripecdn.com/docs-statics-srv/assets/ba9684bdc9a5096c66da38a228968305.png)

WisePad 3Bluetooth or USB![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/cbf74926d4a083809dadd9b11bd16740.png)

Tap to Pay*Embedded![](https://b.stripecdn.com/docs-statics-srv/assets/ba9684bdc9a5096c66da38a228968305.png)

WisePad 3Bluetooth![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/cbf74926d4a083809dadd9b11bd16740.png)

Tap to Pay*Embedded![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart![](https://b.stripecdn.com/docs-statics-srv/assets/42b650b92fa5647632d194573102d0e3.png)

Stripe Reader S700*Smart![](https://b.stripecdn.com/docs-statics-srv/assets/82164fdc231fdbe1b4e24dfc17c9ac63.png)

WisePOS ESmart+Terminal is currently in beta in this country.*This Terminal integration shape is currently in beta.**Compatibility for this mobile SDK also applies when used with React Native.## Integrate Terminal in the United States

Stripe supports Visa, Mastercard, American Express,  and Discover payments in the United States. All transactions must be made in US dollars (USD). To accept Terminal charges in the United States, either your platform account or connected account must be in the United States.

### Use locations

Create Locations for your business with addresses in the United States and associate your readers to them. This will ensure that they automatically download the configuration needed to properly process charges in the United States.

A valid address for a Location in the United States must contain the line1, city, state, postal_code, and country properties.

Command Line[curl](#)`curl https://api.stripe.com/v1/terminal/locations \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "display_name"="HQ" \
  -d "address[line1]"="1272 Valencia Street" \
  -d "address[city]"="San Francisco" \
  -d "address[state]"="CA" \
  -d "address[country]"="US" \
  -d "address[postal_code]"="94110" \`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`