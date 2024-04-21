# Export account activity to QuickBooks

You can’t import IIF-formatted into QuickBooks Online. Instead, check out some of the available third-party accounting integrations that support one-click imports of your activity.

[third-party accounting integrations](https://stripe.partners/?f_category=accounting)

In addition to the CSV-formatted reports that are available for export in the Dashboard, information about payments, refunds, fees, and payouts is also available in a QuickBooks Desktop-compatible IIF file. You can download this within the Dashboard’s Legacy exports settings.

[reports](/reports)

[payouts](/payouts)

[QuickBooks Desktop](http://quickbooks.intuit.com/)

[Legacy exports settings](https://dashboard.stripe.com/account/legacy_exports)

## QuickBooks accounts

The exported IIF file creates the following nine accounts in QuickBooks, if they don’t already exist. All of the Stripe-created accounts are prefaced by Stripe to make them easy to locate and identify.

If these accounts already exist but are of a different type than what you see in the exports file, QuickBooks presents an error about being unable to change the account type. If this occurs edit the conflicting accounts to have the same type as the IIF file.

Always back up your QuickBooks data before importing new information.

## Date format and timezones

The IIF file formats the date as MM/DD/YYYY. QuickBooks uses the same date format as your operating system. If this differs from the exported file, you can temporarily change your operating system’s date format:

- Set the date format in your operating system to MM/DD/YYYY.

- Import the QuickBooks IIF file.

- Change your operating system’s date format back to your preferred style.

Your account’s timezone setting is used for the date range of the IIF export.

[timezone setting](https://dashboard.stripe.com/settings/account)

## Merging QuickBooks accounts

You may want to merge one or more of these created accounts with an existing QuickBooks account. In particular, you may want to merge the Stripe Checking Account, which represents the bank where your Stripe payouts are sent, with your actual banking account in QuickBooks:

- Select Lists > Chart of Accounts to view all of your accounts.

- Make sure both accounts being merged are on the same level (that is, both can be sub-accounts or both can be primary level accounts).

- Select the account you are no longer going to use (for example, Stripe Checking Account).

- Click Account > Edit Account at the bottom of the Chart of Accounts window.

- Change the name of this account to exactly match the name of the other account (the one you’ll be keeping).

- Click Save.

You’re then prompted about merging the account with an existing one. Click Yes to proceed with the merge, No to cancel. The records in the renamed account will be merged into the retained account. Accounts need to be re-merged after each new import.

## Considerations for Connect platforms with Custom accounts

Platform owners with Custom accounts can view the Dashboard of connected Stripe accounts. From the connected account’s Dashboard, export an IIF file in the same way as a normal Stripe account.

Connect platforms creating charges on behalf of connected accounts that need to generate 1099s for Custom accounts must declare the correct tax-line mapping of the Stripe Third-Party Account. This expense account is given an initial tax-line mapping of 1099-MISC: Nonemployee compensation.

[Connect](/connect)

For QuickBooks to use Stripe Third-Party Account data for the generation of 1099s, you must first enable this feature within QuickBooks’ preferences.

- Select Preferences > Tax: 1099 > Company Preferences within QuickBooks.

- Click on the link in If you want to map your accounts to boxes on Form 1099-MISC, click here.

- In the resulting QuickBooks 1099 Wizard, select Stripe Third-Party Account under Accounts used for 1099.

- Under Apply payments to this 1099 box for Stripe Third-Party Account, select Box 7: Nonemployee compensation.
