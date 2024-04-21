htmlConnect W-8 and W-9 | Stripe Documentation[Skip to content](#main-content)Connect W8 and W9[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fconnect-w8-w9-onboarding)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fconnect-w8-w9-onboarding)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Identify forms with missing information](/docs/connect/identify-forms-missing-information)# Connect W-8 and W-9

Use Stripe's W-8 and W-9 Connect product to collect the necessary tax forms from your users.## What’s the Stripe W-8 and W-9 Connect product?

Stripe’s W-8 and W-9 Connect product provides a seamless way to collect certified tax information from connected accounts through the Express Dashboard or Stripe-hosted onboarding. This includes the name, address, and TIN (Tax ID) of a taxpayer. A W-9 tax form is for US residents or citizens and is used to confirm their TIN (SSN/ITIN/EIN). A W-8 tax form is for non-US tax residents and is used to certify their name, address, and foreign TIN (if applicable), to confirm that they’re not a US taxpayer. A non-US resident can also specify the appropriate treaty and/or withholding rates applicable to their business.

Platforms might be subject to IRS fines up to 290 USD per incorrect submission if they file 1099s with incorrect information. W-8 and W-9s provide a way for Platforms to collect certified tax information throughout the year directly from your Connected Accounts before issuing 1099s to make sure the correct information is used on the appropriate 1099 forms.

With the W-8 and W-9 Connect product, your connected accounts can complete the appropriate W8 or W9 form with a few simple clicks. Any information connected accounts have already provided is pre-populated onto the forms for the ease of your users. They only need to confirm the information is accurate and make updates where needed. No more PDFs, emails, or wet-ink signatures needed.

Platforms will have a fully customizable Dashboard which tracks the status of all W-8 or W-9 requests. You’ll be able to easily see which users have completed the appropriate documentation and which users are still pending, and you can download PDFs of any submitted forms.

Connected Accounts will also have a unified tax experience where they can manage completing their tax forms and storage of their tax documents all within the Tax Center.

![Stripe W-8 and W-9 forms dashboard.](https://b.stripecdn.com/docs-statics-srv/assets/w8-w9-dashboard.fca7e6602823d2420c3c1828b4bad753.svg)

Stripe W-8 and W-9 forms dashboard

## How does it work?

Platforms determine appropriate collection timing for when to request a W-8 or W-9. If choosing to collect at onboarding, all new users are asked to verify and attest to their tax information. If choosing to collect at a later date, Platforms request W-8 or W-9 collection with the Accounts API and then route their user to verify and attest to their tax information. Platforms can also request W-8 or W-9 collection from all accounts—existing accounts will be notified at that time.

![Customize the W-8, W-9 collection configuration.](https://b.stripecdn.com/docs-statics-srv/assets/w8-w9-platform-settings.470e604d117bbd4bac5cd400d59b0eb7.png)

Customize the W-8 and W-9 collection configuration

Platforms have full customization in setting enforcement thresholds to determine when Connected Accounts will be required to submit a W-8/W-9 tax form:

- Volume: Block payouts if a W-8 or W-9 isn’t submitted after processingxUSD.
- Time: Block payouts if a W-8 or W-9 isn’t submitted afterxdays.
- Combo: Block payouts if a W-8 or W-9 isn’t submitted afterxdays or after processingxUSD.

## How do I get started?

Currently, access to Stripe’s W-8/W-9 Connect product is limited to US beta users. To request access to the beta and to learn more about pricing, reach out to your account team or contact Stripe for more information.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[What’s the Stripe W-8 and W-9 Connect product?](#what’s-the-stripe-w-8-and-w-9-connect-product)[How does it work?](#how-does-it-work)[How do I get started?](#how-do-i-get-started)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`