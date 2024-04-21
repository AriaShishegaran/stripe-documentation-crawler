# Pause payments and payouts on connected accounts

Platforms can pause payments or payouts on accounts where they’re liable for negative balances, including Express and Custom accounts, through the Connected Account details Dashboard page. Unlike rejecting an account, you can pause payments or payouts regardless of the connected account’s balance. You can unpause payments or payouts at any time through the same page.

[payouts](/payouts)

[Connected Account details](/connect/dashboard/managing-individual-accounts)

[rejecting an account](/api/account/reject)

You can only pause payments in live mode. The Connected Account details page for a test mode account doesn’t include the payments pause function.

After performing an action on a connected account, you can view the change in the account’s status, which is reflected in the Accounts API. In the API response for the connected account, the charges_enabled or payouts_enabled fields return false depending on the action taken, and the requirements hash has a disabled_reason of platform_paused.

By visiting the Connected Account list page, you can filter for the accounts that you have restricted either payments or payouts for.

[Connected Account list](/connect/dashboard/viewing-all-accounts)

Actioned accounts with access to the Express Dashboard see a notice there, explaining that their platform paused payments or payouts on their account, and telling them to direct any questions to their platform.

Actioned accounts without access to a Stripe-hosted Dashboard, including Custom accounts, don’t see any communication from Stripe. You’re responsible for notifying them when you pause their payments or payouts.
