htmlMerchant risk tooling | Stripe Documentation[Skip to content](#main-content)Risk tooling[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Frisk-management%2Frisk-tooling)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Frisk-management%2Frisk-tooling)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Risk management with Connect](/docs/connect/risk-management)# Merchant risk tooling

Use Stripe tools to prevent and manage merchant risk.If you decide to manage merchant risk yourself, Stripe offers tools to help you:

- Identify a potentially fraudulent connected account using a fraud risk score.
- Investigate a connected account by reviewing risk metrics and fraud indicators.
- Gather additional information about a connected account through document verification and a selfie check.
- Take action against a connected account by pausing payouts, pausing payments, rejecting the account, or blocking its external payout account.

## Identify potentially fraudulent connected accounts

Stripe provides a fraud risk score for each connected account based on the risk-related signals that we collect. In your Dashboard, you can filter the accounts overview based on the fraud risk score. The Home page also alerts you to potentially fraudulent connected accounts.

## Investigate a connected account

In your Dashboard, you can view the following information in the connected account details page:

- The fraud risk score of the connected account
- Potential fraud indicators, which provide you with suggestions for potential areas to investigate further
- Risk-related metrics, such as declines, disputes, and refunds, specific to that connected account

## Gather additional information

To gather more information on the connected account, you can ask to verify a government-issued ID document and, optionally, a selfie. When you do so, you also set an enforcement that automatically occurs if the connected account doesn’t successfully complete the verification. This enforcement can either be to pause payouts only, or to pause both payouts and payments. This enforcement can occur either after a certain period of time or after a certain total lifetime volume.

## Take action

You can pause payments, pause payouts, or reject a connected account using the API or the Dashboard.

## Request early access

Interested in getting early access to merchant risk tooling?Merchant risk tooling is currently in private beta. To learn more or get early access, please enter your email address below.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thanks for signing up. We'll be in touch with next steps.Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Identify potentially fraudulent connected accounts](#identify-potentially-fraudulent-connected-accounts)[Investigate a connected account](#investigate-a-connected-account)[Gather additional information](#gather-additional-information)[Take action](#take-action)[Request early access](#request-early-access)Products Used[Connect](/connect)[Radar](/radar)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`