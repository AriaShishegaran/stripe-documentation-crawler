htmlOnline payments | Stripe Documentation[Skip to content](#main-content)Online payments[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fonline-payments)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fonline-payments)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)
[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)# Online payments

Learn about Stripe's integration choices for accepting online payments.[Recommended integrations](#recommended-integrations)[No codeStripe Payment Links](/payment-links)Embed or share a link to a Stripe payment page to accept payments without a website.Integration effort:[RecommendedStripe Checkout](/checkout/quickstart)Send your customers to a checkout page to pay. Embed it directly in your site or redirect to a Stripe-hosted payment page.Integration effort:[Stripe Elements](/payments/quickstart)Integrate customizable UI components into your website or mobile app to collect payment information from customers.Integration effort:Optimize your integration![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

To optimize your integration and increase revenue, select the recommended integration that meets your business needs, add payment methods, and add Link.

[Compare features and availability](#compare-features-and-availability)All integrations support one-time and recurring payments, fraud protection, and global payments.

PAYMENT LINKSCHECKOUTRecommendedELEMENTSAPI ONLYDESCRIPTIONShareable linkPrebuilt payment formUI componentsNo Stripe UIINTEGRATION EFFORTNo codingLow codingMore codingMost codingSTRIPE-HOSTED PAGEEMBED ON YOUR SITEUI CUSTOMIZATIONLimited customization1Limited customization1Extensive customization with[Appearance API](/elements/appearance-api)Customize full appearance and accept payments with your own UIMOBILE SUPPORTResponsive webResponsive webResponsive web and mobile nativeResponsive web and mobile native[STRIPE TAX](/tax)SUPPORTBuilt-inBuilt-inRequires integration with[Stripe Tax API](/tax/custom)Requires integration with[Stripe Tax API](/tax/custom)RECURRING PAYMENTSBuilt-inBuilt-inRequires integration with[Subscriptions API](/subscriptions)Requires integration with[Subscriptions API](/subscriptions)[PAYMENT METHODS](/payments/payment-methods/overview)- [Dynamically display](/payments/payment-methods/integration-options#choose-how-to-add-payment-methods)40+ payment methods2
- Manage in the[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)without coding

- [Dynamically display](/payments/payment-methods/integration-options#choose-how-to-add-payment-methods)40+ payment methods2
- Manage in the[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)without coding

- [Dynamically display](/payments/payment-methods/integration-options#choose-how-to-add-payment-methods)40+ payment methods2
- Manage in the[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)without coding
- Access to[external payment methods](/payments/external-payment-methods)

Integrate 50+ payment methods with code[FASTER CHECKOUT WITH LINK](/payments/link)Built-inBuilt-inBuilt-inUnavailable[PCI COMPLIANCE](/security/guide#validating-pci-compliance)VERIFICATIONAnnual SAQ-AAnnual SAQ-AAnnual SAQ-AAnnual SAQ-D1Limited customization provides 20 preset fonts, 3 preset border radiuses, logo and background customization, and custom button color.

2Dynamic payment methods filter for eligibility and display the most relevant payment methods to maximize conversion.

[Explore more no-code integrations](#explore-no-code)[Invoices](/invoicing/dashboard)Ideal for:Sending an invoice to a specific customerHow it works:Stripe emails your customer an invoice for one-time or recurring payments and a link they can use to pay the invoice online.[Create invoice](https://dashboard.stripe.com/invoices/create)[Manual payments](https://support.stripe.com/questions/enter-customer-payment-information-manually-into-stripe-for-mail-or-telephone-orders)Ideal for:Small payment volumeHow it works:Manually enter payment details in the Dashboard to charge a customer for one-time or recurring payments.[Create payment](https://dashboard.stripe.com/payments/new)[Integrate directly with the API or SDKs](#integrate-api-sdk)### API only

You can build a custom integration using our API reference documentation and libraries.

Our collection of server-side and community libraries provides support for most backend development languages.

### Web and mobile SDKs

You can also accept payments in your own UI using the Stripe SDKs:

- [Stripe.js](/js)(also supports[React](/stripe-js/react))
- [iOS](https://stripe.dev/stripe-ios/)
- [Android](https://stripe.dev/stripe-android)
- [React Native](https://stripe.dev/stripe-react-native)

[Integrate with a platform or a plugin](#integrate-platform-plugin)Stripe partners with thousands of popular platforms and supports plugins to bring Stripe payments into your website. See all of our integration solutions in our online directory.

[ShopifySell online, on social media, and in person with a multichannel commerce platform.](https://stripe.com/partners/shopify)[SquarespaceUse Stripe payments on a single platform to sell your products.](https://stripe.com/partners/squarespace)[Adobe CommerceUse the Stripe Connector for Adobe Commerce for accepting payments on Adobe Commerce.](/connectors/adobe-commerce)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`