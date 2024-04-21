# Review actionable accounts

The Accounts to review tab in your Connect Dashboard helps you monitor the risk and onboarding status of all of your connected accounts. From there, you can:

[Accounts to review tab](https://dashboard.stripe.com/connect/accounts_to_review)

- Proactively monitor your accounts: Monitor the status of your accounts with any open risk, onboarding, or verification requirements. View any risk or onboarding restrictions that impact your accounts or that will impact them in the future.

- Identify the exact requirements needed: Understand an account status quickly, without needing to look through webhook logs. View clear instructions on how to resolve open requirements and take action.

- Export a list of accounts: Download a CSV list of accounts, including remediation links that your accounts with open requirements can use to submit information and resolve issues.

## View all accounts

The Accounts to review tab in your Connect Dashboard provides a list of all your connected accounts with open risk, verification, and onboarding requirements.

[Accounts to review tab](https://dashboard.stripe.com/connect/accounts_to_review)

To view the accounts in a particular status, select the corresponding tab:

In the Actions required and In review tabs, you can toggle the Restrictions column between restrictions and information needed by clicking the gear  in its heading.

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

You can sort the accounts list by total volume, due date, or information needed. In the Rejected tab, you can also sort by accounts with any ongoing appeals.

The Total volume column displays “Unavailable” for connected accounts with Stripe Dashboard access where you don’t have platform controls enabled. Filtering by volume always excludes them. You can identify these accounts by filtering the list by platform controls.

[platform controls](/connect/platform-controls-for-stripe-dashboard-accounts)

Depending on a connected account’s configuration, you can take action on it in the Action required list or In review list by clicking the account’s overflow menu . You can take the following actions:

- Open the Actions required tab on the account activity page.

- Reject the account.

- Pause or resume payouts for the account.

- Pause or resume payments for the account.

- Generate a remediation link that the account can use to take required actions.

[remediation link](/connect/dashboard/remediation-links)

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

[send remediation links to your connected accounts](/connect/dashboard/remediation-links)

## Use Stripe Sigma to identify accounts with open requirements

If you use Stripe Sigma, it can identify accounts that have open requirements or future_requirements. For information about querying for Connect information with Sigma, see Query Connect data.

[Stripe Sigma](/stripe-data)

[Query Connect data](/stripe-data/query-connect-data)

## Review individual accounts

To investigate the open requirements for an account on the Accounts to review tab, click the account. That opens the Actions required tab on that account’s details page, where you can identify specific requirements and take action.

[Actions required](/connect/dashboard/managing-individual-accounts#actions-required)
