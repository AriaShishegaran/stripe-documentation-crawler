# Import Bacs data to Stripe

You can migrate your data from your current payment processor to your Stripe account using the Bacs bulk change process. We work with other payment processors and Bacs sponsor banks throughout the migration to securely migrate your Bacs data. A Bacs migration takes at least 6 weeks to complete.

To export Bacs data from Stripe to another payment processor, see Export Bacs data from Stripe.

[Export Bacs data from Stripe](/payments/bacs-debit/export-data)

[Submit your Bacs import migration request](#submit-bacs-request)

## Submit your Bacs import migration request

Start the migration process by submitting a data migration request.

- Navigate to the Stripe Support form for data migrations. If you’re not signed in, select Sign in and enter the credentials of the account that you want to migrate your data to.

[Stripe Support form for data migrations](https://support.stripe.com/contact/email?topic=migrations)

- Select Import data from a third party into a Stripe account.

- Select Bacs as the data type you want to import.

- Complete the remaining fields and select Send email.

Our Data Migrations team emails you within 3 business days of receiving your request with a questionnaire for you to complete.

You need a Service User Number (SUN) on Stripe to migrate your Bacs data to your Stripe account. You can either use Stripe’s shared SUN or upgrade to Custom Branding and use a custom SUN.

To use Stripe’s shared SUN, state in the questionnaire that you want to use Stripe’s shared SUN.

To request your own custom SUN on Stripe:

- In the Dashboard, navigate to Payment Methods.

[Payment Methods](https://dashboard.stripe.com/test/settings/payment_methods)

- Expand Bacs Direct Debit and click Configure.

- Select the option to upgrade your Bacs Direct Debit plan.

- Specify your Business Display Name.

- Specify your Business Support Email.

- Check the box to confirm that you understand the conditions and select Customise.

[Print, sign, and send your Bulk Change Deed](#sign-bulk-change-deed)

## Print, sign, and send your Bulk Change Deed

To complete the migration, your current Bacs provider needs to sign a bulk change deed. This agreement authorizes the transfer of your mandates from your current payment processor to Stripe.

Sign in to download the Bulk Change Deed.

[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbacs-debit%2Fimport-data)

[Determine your switch date](#determine-switch-date)

## Determine your switch date

After we receive your Bulk Change Deed, Stripe’s Data Migrations team works with you, your current payment processor, and our sponsor bank to agree on a switch date. The actual import into Stripe takes place on your switch date.

[Send communications to your customers](#send-communications)

## Send communications to your customers

The Letter to Payers explains why the migration is needed, how it affects Payers, and the Direct Debit Guarantee.

Download the pre-approved Letter to Payers template and send it to your customers at least 2 days before your switch date. You can’t make any edits outside of the highlighted fields. If you want to make edits to the Letter to Payers, a review is required by Stripe’s sponsor bank.

Sign in to download the Letter to Payers template.

[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbacs-debit%2Fimport-data)

You can decide how to communicate the letter to your customers. For example email, mail, and text message are all valid communication options. Not alerting payers to this change can result in failed payments and disputes.

The payer might see two references to the business in the bank portal for 1-3 business days when Stripe imports the business’s existing mandates. This is because one is the mandate with the former provider, and the other is Stripe’s mandate.

[Wait for your data import](#wait-for-import)

## Wait for your data import

Your current payment processor needs to send on your existing mandates and payers bank account details after we’ve gained authority for them.

Your current payment processor cancels your mandates and our Data Migrations team completes the import of these mandates on the agreed-upon date. Our Data Migrations team sends you a confirmation email when your import is complete. You can’t charge your customers on your current payment processor after they cancel the mandates on the switch date.

This table shows the Bacs timeline in business days from the time (T) that a payment is made to when a new mandate must be collected:

Timelines and document information might differ when exporting data from Stripe to a new payment processor. See Export Bacs data from Stripe for more information.

[Export Bacs data from Stripe](/payments/bacs-debit/export-data)
