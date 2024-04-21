htmlAdditional verifications | Stripe Documentation[Skip to content](#main-content)Additional Verifications[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fadditional-verifications)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fadditional-verifications)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Additional verifications

Add identity verification checks to your platform’s connected accounts.Collect additional identity verification from connected accounts to help reduce fraud losses, streamline risk operations, and meet additional compliance requirements. Automatically collect required information with Connect Onboarding or embed Stripe Identity as part of your custom onboarding experience. Restrict your flow of funds based on verification status and volume thresholds.

By adding a few lines of code to your Connect integration, you can:

- Request an ID document check during initial onboarding
- Match the ID photo with selfies of the document holder
- Disable[payouts](/payouts)or payments based on verification status or volume thresholds
- Access captured images and data extracted from ID documents
- Receive detailed status updates and error messages

Common use cases for additional verifications

- Reduce fraud losses—For example, platforms can streamline risk processes by inserting an ID verification before enabling the first payout.
- Increase trust & safety—For example, marketplaces facilitating in-person services can insert ID verification before allowing connected accounts to collect payments or interact with other users and can display a “verified” badge on their profile.
- Meet additional compliance requirements—For example, fintech platforms can conduct ID verification to confirm user identity as part of meeting their own KYC requirements.

## Get started  Invite only

Access to additional verifications is currently by invitation only. If you’re interested in this functionality, reach out to sales for an invitation.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`