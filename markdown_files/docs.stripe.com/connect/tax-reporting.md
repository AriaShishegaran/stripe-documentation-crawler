htmlUS tax reporting for Connect platforms | Stripe Documentation[Skip to content](#main-content)Overview[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Ftax-reporting)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Ftax-reporting)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# US tax reporting for Connect platforms

Learn how to report the annual payments for your US-based connected accounts.Stripe Connect allows platforms to provide a seamless, end-to-end payment service for their connected accounts. This service may come with certain responsibilities, including tax information reporting.

Getting your 1099 FormsIf you work for a platform that pays you via Stripe and want to learn about your 1099 forms and how to get them, see 1099 tax forms on the Stripe Support site.

Stripe issues 1099-K forms for your connected accounts that meet specific criteria. This includes accounts that have transactions where controller.fees.payer = account.

For any other account setups that have transactions, Stripe won’t be issuing a 1099-K. Instead, consider issuing a Form 1099 to report income and payment transactions. There are several types of 1099 forms, and the applicable form depends on the type of payments you make to your connected account.

NoteStripe recommends that you consult a tax advisor to determine your tax filing and reporting requirements.

### 1099-NEC

Use the 1099-NEC form to report non-employee compensation.

The account must meet all of the following criteria in the previous calendar year:

- Based in the US or a US taxpayer
- $600or more in payments

### 1099-MISC

Use the 1099-MISC form to report other forms of payments made in the course of your business.

The account must meet all of the following criteria in the previous calendar year:

- Based in the US or a US taxpayer
- $600or more in payments or$10in royalties

### 1099-K

Use the 1099-K form to report payment transactions.

The account must meet all of the following criteria in the previous calendar year:

- Based in the US or a US taxpayer
- More than$20,000in gross volume
- More than200transactions

## See also

- [Get started with the Stripe 1099 tax reporting product](/connect/get-started-tax-reporting)
- [Configure your tax form settings](/connect/tax-form-settings)

NoteLooking for help calculating sales tax, VAT, or GST? Check out Stripe Tax.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`