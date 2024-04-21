htmlReview actionable accounts | Stripe Documentation[Skip to content](#main-content)Review actionable accounts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fdashboard%2Freview-actionable-accounts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fdashboard%2Freview-actionable-accounts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Dashboard account management](/docs/connect/dashboard)# Review actionable accounts

View connected accounts with open risk, onboarding, and compliance requirements.The Accounts to review tab in your Connect Dashboard helps you monitor the risk and onboarding status of all of your connected accounts. From there, you can:

- Proactively monitor your accounts: Monitor the status of your accounts with any open risk, onboarding, or verification requirements. View any risk or onboarding restrictions that impact your accounts or that will impact them in the future.
- Identify the exact requirements needed: Understand an account status quickly, without needing to look through webhook logs. View clear instructions on how to resolve open requirements and take action.
- Export a list of accounts: Download a CSV list of accounts, including remediation links that your accounts with open requirements can use to submit information and resolve issues.

## View all accounts

The Accounts to review tab in your Connect Dashboard provides a list of all your connected accounts with open risk, verification, and onboarding requirements.

![The Accounts to review page showing connected accounts that need action.](https://b.stripecdn.com/docs-statics-srv/assets/accounts-to-review-listview.56a3016b917811e060e006ab8216bcfe.png)

To view the accounts in a particular status, select the corresponding tab:

TabDescriptionActions requiredActive accounts with open risk, onboarding, or verification requirements from Stripe or from your platform.In reviewActive accounts that Stripe is reviewing submitted information for or is conducting an account review of, regardless of whether any account capabilities are restricted.RejectedAll accounts that have been rejected by Stripe or by your platform.In the Actions required and In review tabs, you can toggle the Restrictions column between restrictions and information needed by clicking the gear  in its heading.

Within each tab, you can customize the filters to narrow the list of connected accounts that are most relevant to you. You can filter by:

- Payments capability status
- Payouts capability status
- Issuing capability status
- Account status
- Verification requirement
- Volume
- Last payout date
- Information needed

You can see all accounts in the currently selected status by removing the default filters. Changing the filters automatically saves new default values.

![A tooltip showing additional filters on the Accounts to review page, including Payments capability status and Payouts capability status.](https://b.stripecdn.com/docs-statics-srv/assets/filters.2f75daf69b8b149699fcd5737e45c3f8.png)

You can sort the accounts list by total volume, due date, or information needed. In the Rejected tab, you can also sort by accounts with any ongoing appeals.

NoteThe Total volume column displays “Unavailable” for connected accounts with Stripe Dashboard access where you don’t have platform controls enabled. Filtering by volume always excludes them. You can identify these accounts by filtering the list by platform controls.

Depending on a connected account’s configuration, you can take action on it in the Action required list or In review list by clicking the account’s overflow menu . You can take the following actions:

- Open theActions requiredtab on the account activity page.
- Reject the account.
- Pause or resume payouts for the account.
- Pause or resume payments for the account.
- Generate a[remediation link](/connect/dashboard/remediation-links)that the account can use to take required actions.

![A dropdown menu showing the ability to reject the connected account, resume payouts, or resume payments](https://b.stripecdn.com/docs-statics-srv/assets/action-reject-account.27a99b4970cc2de5c2f4d0dcbcd05b71.png)

## Export a list of accounts

You can download a CSV list of all accounts in the current view by clicking Export in the top-right corner of the page. It opens a dialog that lets you select the fields to include:

- Account ID
- Business name
- Representative email
- Account status
- Earliest due date
- Payment status
- Payout status
- Issuing status
- Verification update
- Information needed
- Remediation link
- Total volume (USD) (in minor units)
- Last payout date

You can import the list into another system or use it to send remediation links to your connected accounts. A connected account can use a remediation link to submit information for open requirements.

## Use Stripe Sigma to identify accounts with open requirements

If you use Stripe Sigma, it can identify accounts that have open requirements or future_requirements. For information about querying for Connect information with Sigma, see Query Connect data.

## Review individual accounts

To investigate the open requirements for an account on the Accounts to review tab, click the account. That opens the Actions required tab on that account’s details page, where you can identify specific requirements and take action.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[View all accounts](#view-all-accounts)[Export a list of accounts](#export-a-list-of-accounts)[Use Stripe Sigma to identify accounts with open requirements](#use-stripe-sigma-to-identify-accounts-with-open-requirements)[Review individual accounts](#review-individual-accounts)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`