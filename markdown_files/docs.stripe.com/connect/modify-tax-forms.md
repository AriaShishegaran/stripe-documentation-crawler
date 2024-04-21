htmlUpdate and create 1099 tax forms | Stripe Documentation[Skip to content](#main-content)Update and create tax forms[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fmodify-tax-forms)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fmodify-tax-forms)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Update and create 1099 tax forms

Update and create 1099 tax forms for connected accounts.Getting your 1099 FormsIf you work for a platform that pays you via Stripe and want to learn about your 1099 forms and how to get them, see 1099 tax forms on the Stripe Support site.

Stripe automatically generates tax forms for all connected accounts that have transactions in a given tax year. Tax forms are available on the Tax forms page in the Dashboard. If you need to update or correct a 1099 form, you can do so in one of the following ways:

- Use the Tax form editor-Use the editor in the Dashboard to change the values used in a new 1099 form.
- Export the form as a comma separated value (CSV) file-Export a tax form to a CSV file, modify the values in the CSV file, then import the updated CSV file to generate a new 1099 form with the updated values.

You can also create new tax forms by importing CSV files. If your connected account doesn’t already have a tax form, performing Update or Delta imports automatically creates the form.

Click Create to create a standalone tax form that isn’t associated with a connected account. You must include all columns except for form_id and stripe_account_id. E-delivery isn’t available for standalone forms (only postal mailing is allowed for delivery). If you’re creating a standalone form of a non-default form type, you must include the CSV headers of that form type. If you need assistance getting the correct CSV headers, reach out to support@stripe.com.

Tax form editorCSV filesYou can update the values for payee details and payment amounts in a 1099 tax form using the Tax form editor in the Dashboard. After you update the values, you can generate a new or corrected form with updated values.

## Understanding the tax form editor UI

When you open a record from the Tax forms page, it includes the following sections:

- Payee details-Includes details about the owner of the connected account that you pay out to.
- Totals-Includes the payment detail totals form.
- Forms details-Includes details about delivery and filing status.
- Form timeline-Includes a log of corrections to the tax form. It doesn’t log changes made to the form by exporting the form to a CSV file and then importing an updated CSV file with new values.

You can modify values in the Payee details, Totals, and Forms details sections.

NoteWhen you update the values of a 1099 tax form it updates only the data on the form, not the data in the connected account.

WarningEditing the Payee details or Totals data on a form during the form’s tax year will disable automatic updates to those fields by Stripe. You can always undo your edits to resume automatic updates later.

To update a 1099 tax form before filing

1. On theTax formspage, click the tax form to update.
2. ClickEdit.
3. To update the user details on the 1099 form, such asName,TIN, orAddress, expandPayee detailsand then update the value for each field as appropriate.
4. To update details related to payments and withholdings on the 1099 form, expandTotals, and then update the values as appropriate.
5. ClickSaveto save your changes.

You can then download the updated form as a PDF document.

When you save the form, Stripe validates the format of the values you entered. For example, If you provide a TIN that doesn’t include the correct number of digits, Stripe displays an error message. Stripe doesn’t verify that the TIN is the correct TIN for the connected account, only that it includes the correct number of digits.

## Correcting a tax form after filing

In some cases, you need to correct the values in a 1099 tax form after you file it. If you try to update a tax form that you already filed, you see a Correct button instead of an Edit button in the form.

NoteYou can’t create a corrected 1099 form for a connected account if you already filed it and the status for the filed form is Processing or Rejected. If you need to update a form that is Processing or Rejected, contact Stripe support for assistance.

To correct a 1099 tax form after filing

WarningThe IRS allows you to submit a correction to either the Payee details or Totals data, but not both at the same time. Correct only one set of data for a correction.

1. On theTax formspage, click the tax form to correct.
2. ClickCorrect.
3. To correct the user details on the 1099 form, such asName,TIN, orAddress, expandPayee detailsand then correct the value for each field as appropriate.
4. To correct details related to payments and withholdings on the 1099 form, expandTotalsand then correct the values as appropriate.
5. ClickSaveto save your changes.

You can then file the corrected form and download a PDF copy for your records.

## Quick Correct: Payee Details

When the payee details for a connected account don’t match the values on a tax form for the connected account, a pencil icon appears next to Payee details. Hovering over the pencil shows a tool tip listing the information that doesn’t match. Click the pencil icon, then click Correct to automatically generate a corrected form in which the payee details match those of the connected account.

When you click Correct, Stripe generates a new form with the updated payee information from the connected account Payee details. If there is an existing corrected form that wasn’t yet filed, the corrected form is updated with the information from the connected account. A corrected form includes all payee details that don’t match, such as payee name, address, and TIN. If more than one value is updated, the corrected form updates all mismatched fields.

When you click Correct to update the values in the tax form, it updates all values that are different in the connected account than the tax form. You can’t choose which fields to update values for. You should verify all changes before filing the updated forms. If a connected account user made a typo to their address, the incorrect address is updated in the corrected form. You can choose to change a single value in an updated tax form by using CSV export to export the file to correct. To learn more, see Correct tax forms.

You can use Quick Correct to update details only in tax forms that you have already filed and contain a mismatch between the tax form data and the data in the connected account. When no mismatched data is detected, the pencil icon does not display. If there is a pencil icon displayed to indicate a mismatch in the data because the connected account data is missing, the pencil icon is displayed but the Correct button is deactivated.

In the Quick Correct panel you can view all of the payee details except for the TIN, which is partially redacted.

You can add a Payee details filter with a value of Payee has updated identity info to see only the list of forms with identity values that differ between the connected account and the form, which are the only forms eligible for Quick Correct.

![Payee details filter](https://b.stripecdn.com/docs-statics-srv/assets/payee_details.cf41cd76412580985136ccbf38ba8d25.png)

## Revert: Payee Details & Totals

When the data for Payee details or Totals doesn’t match the values on a tax form for the connected account, an Edited badge appears next to the section. Hovering over the badge shows a tool tip listing the values that don’t match. Click the Undo edits button to automatically revert the tax form to match the data in the connected account.

The difference between Revert and Quick Correct is that you can Revert details on a form when it hasn’t been filed yet, and you can Quick Correct a form after it has been filed. When you click Revert, all mismatched data is updated. You can’t choose which fields to update and exclude others. If there is data missing from the connected account, the Revert button is deactivated.

![Revert details](https://b.stripecdn.com/docs-statics-srv/assets/revert_details.be237e4cac5598ce9708f7260e7988db.png)

## Updating or correcting a 1099 tax form after filing using connected account data

If data for a connected account changes after Stripe generates 1099 forms, you can use the editor in the Dashboard to quickly replace data in the 1099 with data from the connected account. Stripe displays a bell icon in the Payee details section when the data in the form is different from the data in the connected account.

To update or correct a tax form after filing using connected account data

1. On theTax formspage, click the tax form to correct.
2. Click the bell icon to display the data from the connected account.
3. ClickCorrectto update the data in a 1099 form with the data from the connected account.

## User self-serve updates for connected accounts

If you signed up for stripe hosted e-delivery, you can have your users update their tax information themselves before their tax form is filed. If users update their information after filing, the tax form page shows an option to correct the filed 1099 form with the updated information. For more information, see Quick correct: Payee details.

Users can edit their Legal name, Taxpayer Identification Number (TIN), and address. Note that some information can’t be edited after a user’s legal entity is verified, including date of birth, and business type. To edit the information user must contact Stripe Support.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Understanding the tax form editor UI](#understanding-the-tax-form-editor-ui)[Correcting a tax form after filing](#correcting-a-tax-form-after-filing)[Quick Correct: Payee Details](#quick-correct:-payee-details)[Revert: Payee Details & Totals](#revert:-payee-details-&-totals)[Updating or correcting a 1099 tax form after filing using connected account data](#updating-or-correcting-a-1099-tax-form-after-filing-using-connected-account-data)[User self-serve updates for connected accounts](#user-self-serve-updates-for-connected-accounts)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`