# Manage connected accounts with the Dashboard

You can use the Dashboard to inspect, support, and better understand your platform’s connected accounts. Some common tasks supported by the Dashboard include:

- Understand and manage your Connect payments business

[Understand and manage your Connect payments business](/connect/dashboard/understand-your-connect-business)

- View all accounts

[View all accounts](/connect/dashboard/viewing-all-accounts)

- Review actionable accounts

[Review actionable accounts](/connect/dashboard/review-actionable-accounts)

- Create accounts

[Create accounts](/connect/dashboard/managing-individual-accounts#creating-accounts)

- Find individual accounts

[Find individual accounts](/connect/dashboard/managing-individual-accounts#finding-accounts)

- Update account information

[Update account information](/connect/dashboard/managing-individual-accounts#updating-accounts)

- Send funds to accounts

[Send funds to accounts](/connect/dashboard/managing-individual-accounts#sending-funds)

Viewing all accounts provides a high-level view of your connected accounts. By default, all accounts are displayed on the accounts overview page, but you can filter by account status, balance, and other attributes. Filtering accounts is useful because it allows you to:

[Viewing all accounts](/connect/dashboard/viewing-all-accounts)

[accounts overview](https://dashboard.stripe.com/connect/accounts/overview)

- View accounts that are restricted or have other issues that you can help resolve.

- View your largest accounts.

- View accounts based on their status.

The other workflows, like inspecting accounts and sending funds, are actions you can take on individual accounts. These actions are generally made after you know which accounts need to be inspected or modified.

[individual accounts](/connect/dashboard/managing-individual-accounts)

Before viewing and making changes to accounts, learn more about the status badges displayed in the Dashboard.

[status badges](#status-badges)

## Status badges

Status badges provide a quick way to understand the status of an account. You can hover over the badges to view contextual information, and you can click the status tabs to view accounts grouped by that status. Status badges include:

[status tabs](/connect/dashboard/viewing-all-accounts#tabs-workflows)

[Restricted](#restricted)

[Restricted soon](#restricted-soon)

[Pending](#pending)

[Enabled](#enabled)

[Complete](#complete)

[Rejected](#rejected)

Restricted means the account has payouts or payments disabled. Additional information usually needs to be collected to enable these accounts. Hovering over the status badge displays:

[payouts](/payouts)

- Which capability is disabled (payouts or payments).

To find what information is required to enable the account, navigate to the Actions required tab on the connected account details page.

Restricted soon means the account has a due date for providing additional information.

To find what information is required to enable the account, navigate to the Actions required tab on the connected account details page.

Pending means the account is being reviewed or verified by Stripe. This occurs when:

- Stripe is verifying the information that was provided, such as an ID document upload.

- Stripe is performing a watchlist check against a list of prohibited individuals and businesses.

- Stripe is reviewing the account for suspected fraudulent activity.

Payouts can be enabled or disabled for accounts with a pending status and requires no action on your part. Stripe automatically updates the account’s status when the review finishes.

Enabled means the account is in good standing, though additional information might be required if another payment volume threshold is reached. Hovering over the status badge displays:

[threshold](/connect/identity-verification#verification-requirements)

- What information Stripe might request in the future.

In the account’s requirements hash, the array eventually_due contains at least one requirement, but payments and payouts are enabled and current_deadline is empty.

[requirements](/api/accounts/object#account_object-requirements)

Complete means the account provided all the required information and is in good standing.

In the account’s requirements hash, the array eventually_due is empty.

[requirements](/api/accounts/object#account_object-requirements)

Rejected means you (the platform) or Stripe rejected the connected account. Hovering over the status badge displays:

- Whether the account was rejected by you (the platform), or by Stripe.

You can navigate to the Actions required tab on the connected account details page to see the reason the account was rejected. In general, accounts are rejected by Stripe if they’re suspected of fraudulent activity.

## Use Platform Branding for Connected Accounts

This setting only applies to new accounts created by your platform. Existing accounts aren’t affected.

As the platform, you can initialize newly created connected accounts with your platform branding settings. To do so, navigate to Connect Settings > Branding and enable Copy Platform Branding. After you enable it, all new accounts onboarding to your platform receive the same branding settings as your platform.

Use Account Update to update the account’s branding after creation.

[Account Update](/api/accounts/update)

## See also

- Viewing all accounts

[Viewing all accounts](/connect/dashboard/viewing-all-accounts)

- Managing individual accounts

[Managing individual accounts](/connect/dashboard/managing-individual-accounts)
