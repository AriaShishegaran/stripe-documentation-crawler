htmlPlatform controls in the Stripe Dashboard | Stripe Documentation[Skip to content](#main-content)Platform controls for Stripe Dashboard accounts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fplatform-controls-for-stripe-dashboard-accounts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fplatform-controls-for-stripe-dashboard-accounts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Platform controls in the Stripe Dashboard

Manage more features on behalf of your connected accounts that use the Stripe Dashboard with platform controls.### Account types

Connect platforms can work with three different[account types](https://stripe.com/docs/connect/accounts).This content applies only to Standard accounts.Thousands of platforms and marketplaces use Stripe Connect to facilitate payments and pay out recipients. Using the Stripe Dashboard and relying on Stripe to manage onboarding, reporting, and loss liability is already the fastest way to enable your customs to accept payments directly. Now you can manage more features on behalf of your connected accounts with platform controls.

- [Control payout timing](#control-payout-timing)
- [Access consolidated reporting](#access-consolidated-reporting)
- [Co-brand your connected accounts](#co-brand-your-connected-account-experience)

NoteStarting in June 2021, Platforms using OAuth with read_write scope won’t be able to connect to accounts that are controlled by another platform. Learn more about OAuth changes for Standard Platforms.

## Configuring platform controls

Navigate to the third-party extensions page.

Select the options for your connected accounts there. These options apply to all of your new connected accounts moving forward. Visit the connected accounts page to change settings for individual connected accounts.

## Control payout timing

As the platform, you can now update your connected accounts’ payouts programmatically using the Stripe API or in the Stripe Dashboard.

You can also initiate payouts on behalf of your connected accounts programmatically using the Stripe API or via the Dashboard.

Navigate to the payout schedules page to determine whether connected accounts can manage their own payout schedules. Connected accounts can still make manual payouts after you, as the platform, choose to restrict connected accounts from updating their own payout schedule.

NoteIf you need full control over your connected accounts’ payouts and want to restrict your connected accounts from being able to make their own payouts, contact us with a detailed description of your use case.

## Access consolidated reporting

You can access reporting across all connected accounts that you control using the built in-Dashboard reporting as well as within Stripe Sigma, a custom reporting solution that makes all of your data available as an interactive SQL environment in the Dashboard. To learn more:

- [Stripe Financial reports](/reports)
- [Stripe Sigma for Connect platforms](/stripe-data/query-connect-data)

## Co-brand your connected accounts

As the platform, you can manage your brand settings within the Connect Settings > Stripe Dashboard section. All new accounts onboarding to your platform will see your icon and branding color in their dashboard. To understand changes for connected accounts, see this Support article.

NoteThese features apply only to new accounts onboarding to your platform, denoted by true in the is_controller property for the Account object. Existing accounts aren’t eligible for these features.

## Remove accounts

From the connected account details page in your Dashboard, click the overflow menu () and choose Remove account. This action disconnects the account and revokes access in the same way as the OAuth de-authorize endpoint. Removing an account from your platform resets any platform controls (such as payout timing) you’ve configured for the connected account. If the account reconnects later, prior platform controls aren’t reinstated.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Configuring platform controls](#configuring-platform-controls)[Control payout timing](#control-payout-timing)[Access consolidated reporting](#access-consolidated-reporting)[Co-brand your connected accounts](#co-brand-your-connected-accounts)[Remove accounts](#remove-accounts)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`