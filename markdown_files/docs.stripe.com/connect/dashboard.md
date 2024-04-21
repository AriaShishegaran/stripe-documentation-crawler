htmlManage connected accounts with the Dashboard | Stripe Documentation[Skip to content](#main-content)Dashboard account management[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fdashboard)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fdashboard)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Manage connected accounts with the Dashboard

Learn about using the Stripe Dashboard to find and manage connected accounts.You can use the Dashboard to inspect, support, and better understand your platform’s connected accounts. Some common tasks supported by the Dashboard include:

- [Understand and manage your Connect payments business](/connect/dashboard/understand-your-connect-business)
- [View all accounts](/connect/dashboard/viewing-all-accounts)
- [Review actionable accounts](/connect/dashboard/review-actionable-accounts)
- [Create accounts](/connect/dashboard/managing-individual-accounts#creating-accounts)
- [Find individual accounts](/connect/dashboard/managing-individual-accounts#finding-accounts)
- [Update account information](/connect/dashboard/managing-individual-accounts#updating-accounts)
- [Send funds to accounts](/connect/dashboard/managing-individual-accounts#sending-funds)

Viewing all accounts provides a high-level view of your connected accounts. By default, all accounts are displayed on the accounts overview page, but you can filter by account status, balance, and other attributes. Filtering accounts is useful because it allows you to:

- View accounts that are restricted or have other issues that you can help resolve.
- View your largest accounts.
- View accounts based on their status.

The other workflows, like inspecting accounts and sending funds, are actions you can take on individual accounts. These actions are generally made after you know which accounts need to be inspected or modified.

Before viewing and making changes to accounts, learn more about the status badges displayed in the Dashboard.

## Status badges

Status badges provide a quick way to understand the status of an account. You can hover over the badges to view contextual information, and you can click the status tabs to view accounts grouped by that status. Status badges include:

StatusBadge[Restricted](#restricted)Restricted[Restricted soon](#restricted-soon)Restricted soon[Pending](#pending)(enabled or disabled)PendingorPending[Enabled](#enabled)Enabled[Complete](#complete)Complete[Rejected](#rejected)Rejected### Restricted

Restricted means the account has payouts or payments disabled. Additional information usually needs to be collected to enable these accounts. Hovering over the status badge displays:

- Which capability is disabled (payouts or payments).

To find what information is required to enable the account, navigate to the Actions required tab on the connected account details page.

### Restricted soon

Restricted soon means the account has a due date for providing additional information.

To find what information is required to enable the account, navigate to the Actions required tab on the connected account details page.

### Pending

Pending means the account is being reviewed or verified by Stripe. This occurs when:

- Stripe is verifying the information that was provided, such as an ID document upload.
- Stripe is performing a watchlist check against a list of prohibited individuals and businesses.
- Stripe is reviewing the account for suspected fraudulent activity.

Payouts can be enabled or disabled for accounts with a pending status and requires no action on your part. Stripe automatically updates the account’s status when the review finishes.

### Enabled

Enabled means the account is in good standing, though additional information might be required if another payment volume threshold is reached. Hovering over the status badge displays:

- What information Stripe might request in the future.

In the account’s requirements hash, the array eventually_due contains at least one requirement, but payments and payouts are enabled and current_deadline is empty.

### Complete

Complete means the account provided all the required information and is in good standing.

In the account’s requirements hash, the array eventually_due is empty.

### Rejected

Rejected means you (the platform) or Stripe rejected the connected account. Hovering over the status badge displays:

- Whether the account was rejected by you (the platform), or by Stripe.

You can navigate to the Actions required tab on the connected account details page to see the reason the account was rejected. In general, accounts are rejected by Stripe if they’re suspected of fraudulent activity.

## Use Platform Branding for Connected Accounts

This setting only applies to new accounts created by your platform. Existing accounts aren’t affected.

As the platform, you can initialize newly created connected accounts with your platform branding settings. To do so, navigate to Connect Settings > Branding and enable Copy Platform Branding. After you enable it, all new accounts onboarding to your platform receive the same branding settings as your platform.

Use Account Update to update the account’s branding after creation.

## See also

- [Viewing all accounts](/connect/dashboard/viewing-all-accounts)
- [Managing individual accounts](/connect/dashboard/managing-individual-accounts)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Status badges](#status-badges)[Use Platform Branding for Connected Accounts](#use-platform-branding-for-connected-accounts)[See also](#see-also)Products Used[Connect](/connect)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`