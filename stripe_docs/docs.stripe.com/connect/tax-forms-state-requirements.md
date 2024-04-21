# File tax forms with states

When you file your 1099 forms from the Tax forms view in the Dashboard, Stripe submits your forms to the IRS and all qualifying states. We automatically apply state thresholds when generating 1099 tax forms, so you can easily determine which forms need state filing based on the addresses of your connected accounts.

[file](/connect/file-tax-forms)

[Tax forms](https://dashboard.stripe.com/connect/taxes/forms)

Stripe supports e-filing in all states but won’t transmit forms to states on your behalf that have backup or state withholding amounts. Review 1099 form requirements by state and work with your tax advisor to make sure you understand the tax requirements specific to your business.

[1099 form requirements by state](/connect/tax-forms-state-requirements#check-1099-form-requirements-by-state)

## Prepare to file with the states

Before filing forms in your Dashboard, do the following to make sure forms are filed correctly with both the IRS and states:

[Choose the tax form type in the Dashboard](#choose-form-type)

## Choose the tax form type in the Dashboard

Configure your tax forms settings to choose the tax form type (or types) you’ll file: 1099-K, 1099-NEC, or 1099-MISC. Each state has different requirements for each form type.

[Configure your tax forms settings](/connect/get-started-tax-reporting#set-tax-form-default-settings)

[Determine the states where your connected accounts are based](#determine-location)

## Determine the states where your connected accounts are based

In the Dashboard, you can either export a CSV file with state information (reported in the payee_region column) or filter by Payee state.

[Dashboard](https://dashboard.stripe.com/connect/taxes/forms)

[export](/connect/modify-tax-forms?method=csv)

[Determine which states to file with](#determine-states)

## Determine which states to file with

Some state 1099 filings also require a state tax registration or withholding ID. Refer to the tables in the Check 1099 form requirements by state section to determine where you might need state online accounts and IDs.

[Check 1099 form requirements by state](/connect/tax-forms-state-requirements#check-1099-form-requirements-by-state)

[Add the state tax Registration or withholding ID](#add-state-reg)

## Add the state tax Registration or withholding ID

After you obtain the registration or withholding ID, add the states in which you’ll file and the corresponding IDs on the Tax forms settings page. In the Dashboard, click Settings. On Product settings, under Connect, click Tax form settings.

[Tax forms settings](https://dashboard.stripe.com/settings/connect/tax_forms)

Refer to the tables in the Check 1099 form requirements by state section to determine where you might need state online accounts and IDs. If prompted that some state registration or withholding IDs were missing during filing, you need to go to the Connect Tax forms settings page, add the missing IDs, and then go through the filing flow again.

[Check 1099 form requirements by state](/connect/tax-forms-state-requirements#check-1099-form-requirements-by-state)

[Tax forms settings](https://dashboard.stripe.com/settings/connect/tax_forms)

## State-by-state breakdown

When you’re ready to file forms in your Dashboard, the forms for IRS and state reporting agencies will be filed at the same time. To understand the number of forms being filed in each state, click Show state-by-state breakdown on the File Federal and state tax forms window in the filing flow. This page also indicates whether the state’s registration or withholding ID is missing or has already been provided. A yellow informational banner displays at the top of every page in the filing flow if state IDs are missing from states that are being filed.

[file forms in your Dashboard](/connect/file-tax-forms)

## Withholding

Stripe can’t file tax forms with the state authorities if state withholding is present. If you have forms with state withholding, Stripe won’t file those with the states but will make the files available as an export and file with the IRS. Please check the Exports & Imports section in the Dashboard for the downloaded file. Please consult a tax advisor on how/whether to file these forms with state agencies.

## Check 1099 form requirements by state

Choose the form type to view state filing requirements:

- 1099-K

[1099-K](/connect/1099-K)

- 1099-NEC

[1099-NEC](/connect/1099-NEC)

- 1099-MISC

[1099-MISC](/connect/1099-MISC)

## Correct 1099 reports with the states

When you file a correction with the IRS, the state correction is filed at the same time. To file a correction with a state for a form that was already filed, you must create a correction.

[correction](/connect/correct-tax-forms)

## Frequently asked questions

The following section provides answers to common questions about filing tax forms through Connect.

Stripe does not support this at the moment. Stripe only checks eligibility and files in the state where the connected account’s address is registered.

Stripe files with the IRS and the State right away when you file the submission and you can’t make changes to that. But platforms are always able to make “corrections” and then file them and Stripe takes care of processing those corrections to the IRS and the State.

We’ve introduced a new State filing status. For more information, see Understand tax form status.

[Understand tax form status](/connect/get-started-tax-reporting#understand-tax-form-status)

No. If you override the filing requirements, it applies to both federal and state filing.

When you choose to override the filing status and select File even if incomplete, there are still certain edge cases where your form might still have a state filing status of Needs Attention. This is done to minimize the risk of rejections from the state. Take note of the following state-specific rules:

- Pennsylvania: The form must have a non-zero Taxpayer Identification Number (TIN) and pass a basic address validation check, which requires at least one digit and one number in the address.

- Illinois: The form must have a non-zero TIN and a valid payee name.

- Oregon: The form must have a non-zero TIN.

- District of Columbia: The form cannot have a TIN with all digits being the same number.
