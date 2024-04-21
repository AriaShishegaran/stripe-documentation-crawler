htmlCorrect tax forms | Stripe Documentation[Skip to content](#main-content)Correct tax forms[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fcorrect-tax-forms)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fcorrect-tax-forms)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Correct tax forms

Learn how to file corrections to tax forms.Getting your 1099 FormsIf you work for a platform that pays you via Stripe and want to learn about your 1099 forms and how to get them, see 1099 tax forms on the Stripe Support site.

In some cases, you need to correct the values in a 1099 tax form after you’ve filed it. If you try to update a tax form that you already filed, you see a Correct button instead of an Edit button in the form.

## Correction Reasons

You might need to issue a correction for several reasons:

- To change the identity data of your connected account. For example, users may request changes to their name, address, or tax identification information


- To change form totals


- To handle forms with Rejected state filing status. If you have forms with federal filing status of Rejected, please reach out to Stripe support.

Here are the most common rejection reasons:

AttributeExample rejection reasonsTINMissing, invalid, mismatched with IRS recordsAddressNon-English characters, malformed zip codes, missing fields (for example, city, empty Line 1 address)NameMissing, non-English or non-alphabetical charactersThe Rejected status implies that the form was either rejected by the IRS or state after submission, or that the state refused to accept the information during submission.

You can file a correction to update information on a form that has been rejected by a state (if federal filing status shows up as “rejected”, please contact Stripe support). Stripe 1099 intelligently files Corrections if the form was initially accepted or Replacements if it was rejected.


- To handle delivery failures

If the delivery status is Failed, that means we couldn’t deliver the tax form to the mailing address on file. There could be two reasons for this:

  - Misconfigured address-  The address is missing or invalid. For example, it includes non-English characters, the zip code doesn’t have the correct number of digits, or the city is missing.
  - Non-deliverable address- The address doesn’t exist and our delivery partners can’t use it to deliver first-class mail.



## Supported corrections

You can correct most boxes on a tax form. Depending on when you submit a correction and what you’re correcting, penalties may apply.

The IRS generally allows you to correct totals or payee information.

- When you correct totals, a single form replaces the original and includes the original payee information, new totals, and a checked Corrected checkbox.


- When you correct payee information, two forms replace the original:

  - The first form includes the original payee information, zeros for all totals, and a checkedCorrectedcheckbox.
  - The second form includes the new payee information, original totals, and an uncheckedCorrectedcheckbox (because this is the first form received by the new payee).



The IRS imposes certain requirements on tax form corrections.

You can’t correct:

- The payee name and form totals in the same form
- The payee tax identification number and form totals in the same form
- Tax forms that the IRS hasn’t accepted
- The form type (for example, 1099-MISC to 1099-NEC)

## Create a correction

You can only correct tax forms that the IRS has accepted.  There are a few ways to start corrections, each of which results in a corrected form that shows up as a Ready Correction.

NoteIf you want to update information for the connected account permanently, make the changes programmatically using the Accounts API or the Connected Accounts details page and you can then use Quick Correct as shown below. Without doing this first, you’ll be updating the information only on the tax form. This doesn’t persist onto the connected account details and you’ll have to re-enter this information next tax season.

- Use the Tax form editor

  1. Select the form on the[Tax forms](https://dashboard.stripe.com/connect/taxes/forms)page.
  2. ClickCorrectto create a correction.
  3. Make the necessary changes.
  4. Save the changes.


- Use a CSV import

  1. Select the form and export it as a CSV.
  2. Open the CSV in a compatible tool to make and save the necessary changes.
  3. Import the updated CSV using the import modeCorrect.

Corrections use the same CSV schema as updates and are filed regardless of filing threshold. This allows you to zero out a tax form that was accidentally filed or to correct a tax form to have a lower volume. The Filing_requirement allows you to specify whether or not to file a correction.


- Use Quick Correct

If the identity (name, address, TIN) of the connected account has been updated in Stripe and now differs from what’s on the filed form, a pencil icon appears next to the “Payee details” for platform admin accounts. Hovering over the pencil and clicking Correct generates a corrected form to match the identity values of the connected account.

When you click Correct to update the values in the tax form, it updates all values that are different in the connected account than the tax form. You can’t choose which fields to update values for. Verify all changes before filing the updated forms. For example, if a connected account user made a typo in their address, the incorrect address is updated in the corrected form.

To list the forms with identity values that differ between the connected account and the tax form in order to find potential corrections, add a Payee details filter with a value of “Payee has updated identity info”.



## View or cancel a correction

Tax form corrections have a Correction badge in the tax forms list and on the detail pane in the Dashboard. You can download previous versions of a tax form from the detail pane. To cancel a correction before filing, click Cancel correction from the menu on the detail pane.

![View or cancel tax form corrections](https://b.stripecdn.com/docs-statics-srv/assets/view-cancel-correction-new.2c0d2cdae64ec49be826b5e641ea5b89.png)

## File a correction

Once you have successfully created a correction via one of the methods above, the corrected form will move to “Ready” column of your Tax Forms page after a page refresh regardless of whether the form is above filing threshold.

If you want to file the correction, select the correction and click the file button. If you want to skip filing one of the corrections, set the filing requirement to NOT_REQUIRED in the Tax Form Editor or import a CSV file.

If you’ve selected to e-deliver your tax forms, your connected account will get an email letting them know that the corrected form is available in Stripe Express.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Correction Reasons](#correction-reasons)[Supported corrections](#supported-corrections)[Create a correction](#create-a-correction)[View or cancel a correction](#view-or-cancel-a-correction)[File a correction](#file-a-correction)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`