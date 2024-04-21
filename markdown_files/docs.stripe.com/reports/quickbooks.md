htmlExport account activity to QuickBooks | Stripe Documentation[Skip to content](#main-content)QuickBooks Desktop[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Freports%2Fquickbooks)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Freports%2Fquickbooks)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)
[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Reporting](/docs/stripe-reports)[Basic financial reports](/docs/reports)[Connect an accounting tool](/docs/accounting-integrations)# Export account activity to QuickBooks

Download an export of your Stripe account data suitable for import into your desktop QuickBooks.### QuickBooks Online users

You can’t import IIF-formatted into QuickBooks Online. Instead, check out some of the available third-party accounting integrations that support one-click imports of your activity.

In addition to the CSV-formatted reports that are available for export in the Dashboard, information about payments, refunds, fees, and payouts is also available in a QuickBooks Desktop-compatible IIF file. You can download this within the Dashboard’s Legacy exports settings.

## QuickBooks accounts

The exported IIF file creates the following nine accounts in QuickBooks, if they don’t already exist. All of the Stripe-created accounts are prefaced by Stripe to make them easy to locate and identify.

NameTypeDescriptionStripe AccountBankAll charges, refunds, and payoutsStripe Checking AccountBankRepresents your actual bank account to which Stripe sends payoutsStripe Payment Processing FeesExpenseProcessing fees for all chargesStripe ReturnsIncomeAll refundsStripe SalesIncomeAll charges minus processing feesStripe Third-Party AccountTax-Related ExpenseEvery transfer to a third-partyStripe Other FeesExpenseAdjustmentsStripe Processing Fees AdjExpenseAdjustmentsStripe Other IncomeIncomeAdjustmentsIf these accounts already exist but are of a different type than what you see in the exports file, QuickBooks presents an error about being unable to change the account type. If this occurs edit the conflicting accounts to have the same type as the IIF file.

NoteAlways back up your QuickBooks data before importing new information.

## Date format and timezones

The IIF file formats the date as MM/DD/YYYY. QuickBooks uses the same date format as your operating system. If this differs from the exported file, you can temporarily change your operating system’s date format:

1. Set the date format in your operating system to MM/DD/YYYY.
2. Import the QuickBooks IIF file.
3. Change your operating system’s date format back to your preferred style.

Your account’s timezone setting is used for the date range of the IIF export.

## Merging QuickBooks accounts

You may want to merge one or more of these created accounts with an existing QuickBooks account. In particular, you may want to merge the Stripe Checking Account, which represents the bank where your Stripe payouts are sent, with your actual banking account in QuickBooks:

1. SelectLists > Chart of Accountsto view all of your accounts.
2. Make sure both accounts being merged are on the same level (that is, both can be sub-accounts or both can be primary level accounts).
3. Select the account you are no longer going to use (for example,Stripe Checking Account).
4. ClickAccount > Edit Accountat the bottom of theChart of Accountswindow.
5. Change the name of this account to exactly match the name of the other account (the one you’ll be keeping).
6. ClickSave.

You’re then prompted about merging the account with an existing one. Click Yes to proceed with the merge, No to cancel. The records in the renamed account will be merged into the retained account. Accounts need to be re-merged after each new import.

## Considerations for Connect platforms with Custom accounts

Platform owners with Custom accounts can view the Dashboard of connected Stripe accounts. From the connected account’s Dashboard, export an IIF file in the same way as a normal Stripe account.

Connect platforms creating charges on behalf of connected accounts that need to generate 1099s for Custom accounts must declare the correct tax-line mapping of the Stripe Third-Party Account. This expense account is given an initial tax-line mapping of 1099-MISC: Nonemployee compensation.

For QuickBooks to use Stripe Third-Party Account data for the generation of 1099s, you must first enable this feature within QuickBooks’ preferences.

1. SelectPreferences > Tax: 1099 > Company Preferenceswithin QuickBooks.
2. Click on the link inIf you want to map your accounts to boxes on Form 1099-MISC, click here.
3. In the resulting QuickBooks 1099 Wizard, selectStripe Third-Party AccountunderAccounts used for 1099.
4. UnderApply payments to this 1099 boxforStripe Third-Party Account, selectBox 7: Nonemployee compensation.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[QuickBooks accounts](#quickbooks-accounts)[Date format and timezones](#date-format)[Merging QuickBooks accounts](#merging-quickbooks-accounts)[Considerations for Connect platforms with Custom accounts](#connect-platforms-with-custom-accounts)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`