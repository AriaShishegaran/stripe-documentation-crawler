htmlTax ID Additional Verification | Stripe Documentation[Skip to content](#main-content)Tax ID Additional Verification[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fconnect-tax-id-onboarding)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fconnect-tax-id-onboarding)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Identify forms with missing information](/docs/connect/identify-forms-missing-information)# Tax ID Additional Verification

Learn how to use Stripe Tax ID Additional Verification to collect and verify the Tax ID of your users.Connect dynamically requires onboarding information to keep your accounts compliant, but you can influence what information Connect requires in your platform by adding additional verifications (AVs) to accounts. Requesting an additional verification requires your connected accounts to provide certain information, which is then verified.

Platforms might be subject to IRS fines up to 290 USD per submission if they file 1099s with incorrect information (for example, name or tax ID mismatches). The Tax ID AV provides a way for platforms to collect certified tax IDs throughout the year directly from your connected accounts before issuing 1099s, to make sure the appropriate 1099 tax forms use the correct Taxpayer Identification Number (TIN).

The Tax ID Additional Verification performs a name and TIN check either at the personal level or business level based on required verification information for taxes.

## How it works

The Tax ID Additional Verification allows you to enforce the mandatory collection and verification of tax ID requirements for a connected account. Platforms add requirements for Tax ID collection/verification for a connected account using the Accounts API.

For Custom Connect platforms, after you add the requirements on a connected account, your platform can Create an account link to redirect the user from your platform to Connect Onboarding. Alternatively, you can collect the requirements directly from your platform, and then send it to Stripe using Update an account. For Express Connect platforms, Stripe sends the Express connected accounts an email to complete the missing or invalid requirements using the Express Dashboard.

After Stripe receives the user’s TIN, we automatically verify it by comparing it with the IRS database. If the IRS database confirms the TIN is a match, the requirements are considered satisfied. If the IRS database doesn’t return a TIN match with the connected account’s tax details, then enforcement limits are triggered.

Platforms have full customization in setting enforcement limits to determine when Connected Accounts are required to provide a verified TIN. You can set the following enforcement limits to impose disablement of payouts or payouts or payments if a verified TIN isn’t on file:

- Upfront: Block payouts or payments if a verified TIN isn’t on file immediately.
- Volume: Block payouts or payments if a verified TIN isn’t on file after processingxUSD.
- Time: Block payouts or payments if a verified TIN isn’t on file afterxdays.
- Combo: Block payouts or payments if a verified TIN isn’t on file afterxdays or after processingxUSD.

## Get started

Currently, access to Stripe’s Tax ID Additional Verification is limited to US beta users. To request access to the beta, reach out to your account team or contact Stripe for more information.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[How it works](#how-it-works)[Get started](#get-started)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`