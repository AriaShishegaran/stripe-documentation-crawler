htmlIdentity | Stripe Documentation[Skip to content](#main-content)Overview[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fidentity)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fidentity)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)[Verify identities](#)
NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Get started](/docs/get-started)# Identity

Learn how to verify identities using Stripe Identity.Available for users in:Use Stripe Identity to confirm the identity of global users to prevent fraud, streamline risk operations, and increase trust and safety. Stripe Identity allows you to:

- Verify the authenticity of ID documents from more than 120 countries
- Capture IDs with a conversion-optimized verification flow
- Match photo IDs with selfies, and validate Social Security numbers (SSNs)
- Access collected images, and extracted data from ID documents

## Get started

[Sign upActivate Identity in the Dashboard.](https://dashboard.stripe.com/identity/application)[Verify your users’ identity documentsBegin by creating sessions and collecting identity documents.](/identity/verify-identity-documents)[Handle verification outcomesListen for verification outcomes so your integration can automatically trigger reactions.](/identity/handle-verification-outcomes)## More verification checks

[Verification checksLearn about all the different verification checks supported by Stripe Identity.](/identity/verification-checks)[Adding selfie checksAdd face similarity checks to prevent fraudsters from using stolen documents.](/identity/selfie)[Additional verifications for ConnectCollect additional identity verification as part of your Connect onboarding experience.](/connect/additional-verifications)## Clone a sample project

[Try out the demoPreview a demo of Stripe Identity](https://identity.stripedemos.com/)[Verify identity documentsWeb · Mobile Web](/samples/identity/modal)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`