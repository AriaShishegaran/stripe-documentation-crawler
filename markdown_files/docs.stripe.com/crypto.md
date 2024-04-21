htmlStripe Crypto | Stripe Documentation[Skip to content](#main-content)Fiat-to-crypto onramp[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fcrypto)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fcrypto)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)
[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)# Stripe CryptoBeta

Learn how to integrate the Stripe fiat-to-crypto onramp.You must submit an onramp application to access the onramp API. Most applications are reviewed within 48 hours.

### To submit your application:

1. Create or sign in to your Stripe account, and submit the[onramp application](https://dashboard.stripe.com/register?redirect=%2Fcrypto-onramp%2Fapplication).
2. Complete your[Stripe application](https://dashboard.stripe.com/account/onboarding).
3. After submitting the application in step 2, you can start development using test mode.

Stripe notifies you when your application is approved or if we require more information. Check the status of your application by visiting the onboarding page.

Contact Stripe Support with any questions.

Enable users to purchase crypto directly from your application[Overview](/docs/crypto/overview)![](https://b.stripecdn.com/docs-statics-srv/assets/crypto-onramp-overview-banner.eb44e843dcabbf44808d8a0e7b85ae1f.png)

## Get started

Learn more about which integration option is right for your use case in the onramp overview.

[Sample integrationQuickstartBuild a starter embeddable onramp integration with our code-based tour that includes downloadable files so you can follow along.](/crypto/quickstart)[No-code quickstartQuickstartCustomize and generate a redirect URL to the standalone hosted onramp. Stripe account optional.](/crypto/no-code-quickstart)[Integrate the embeddable onrampUse this guide if you want to fully customize and embed Stripe onramp on your site.](/crypto/integrate-the-onramp)[Integrate the standalone hosted onrampUse this guide if you want to write minimal code and have your customers use the hosted version of Stripe onramp.](/crypto/standalone-hosted-onramp)## Explore the API

[Using the APILearn how to use the onramp API and customize your application.](/crypto/using-the-api)[Quotes APIFetch estimated quotes for onramp conversions.](/crypto/quotes-api)## Additional Resources

[Integration recipesLearn best practices for how to integrate the onramp for different web3 use cases.](/crypto/integration-recipes)[Mobile integrationLearn how to the integrate the onramp for mobile use.](/crypto/mobile-integration)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`