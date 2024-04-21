htmlFile tax forms with states | Stripe Documentation[Skip to content](#main-content)File tax forms with states[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Ftax-forms-state-requirements)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Ftax-forms-state-requirements)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# File tax forms with states

Learn about the state requirements for filing 1099 forms.When you file your 1099 forms from the Tax forms view in the Dashboard, Stripe submits your forms to the IRS and all qualifying states. We automatically apply state thresholds when generating 1099 tax forms, so you can easily determine which forms need state filing based on the addresses of your connected accounts.

NoteStripe supports e-filing in all states but won’t transmit forms to states on your behalf that have backup or state withholding amounts. Review 1099 form requirements by state and work with your tax advisor to make sure you understand the tax requirements specific to your business.

## Prepare to file with the states

Before filing forms in your Dashboard, do the following to make sure forms are filed correctly with both the IRS and states:

[Choose the tax form type in the Dashboard](#choose-form-type)Configure your tax forms settings to choose the tax form type (or types) you’ll file: 1099-K, 1099-NEC, or 1099-MISC. Each state has different requirements for each form type.

[Determine the states where your connected accounts are based](#determine-location)In the Dashboard, you can either export a CSV file with state information (reported in the payee_region column) or filter by Payee state.

![Filter by payee state](https://b.stripecdn.com/docs-statics-srv/assets/payee_state.f077495dfbceb3bba62b27c5aee2bb9f.png)

[Determine which states to file with](#determine-states)Some state 1099 filings also require a state tax registration or withholding ID. Refer to the tables in the Check 1099 form requirements by state section to determine where you might need state online accounts and IDs.

[Add the state tax Registration or withholding ID](#add-state-reg)After you obtain the registration or withholding ID, add the states in which you’ll file and the corresponding IDs on the Tax forms settings page. In the Dashboard, click Settings. On Product settings, under Connect, click Tax form settings.

![Add the state tax registration or withholding ID for each state you'll file](https://b.stripecdn.com/docs-statics-srv/assets/state_tax_registration_id.b61e81338146c94a3e98ee995cd866ce.png)

Refer to the tables in the Check 1099 form requirements by state section to determine where you might need state online accounts and IDs. If prompted that some state registration or withholding IDs were missing during filing, you need to go to the Connect Tax forms settings page, add the missing IDs, and then go through the filing flow again.

## State-by-state breakdown

When you’re ready to file forms in your Dashboard, the forms for IRS and state reporting agencies will be filed at the same time. To understand the number of forms being filed in each state, click Show state-by-state breakdown on the File Federal and state tax forms window in the filing flow. This page also indicates whether the state’s registration or withholding ID is missing or has already been provided. A yellow informational banner displays at the top of every page in the filing flow if state IDs are missing from states that are being filed.

![Review filing details page displaying a banner to indicate a missing Tax ID.](https://b.stripecdn.com/docs-statics-srv/assets/tax-forms-review-filing-missing-ID.40d5902778ca845d5190d1679d9f4ee8.png)

## Withholding

Stripe can’t file tax forms with the state authorities if state withholding is present. If you have forms with state withholding, Stripe won’t file those with the states but will make the files available as an export and file with the IRS. Please check the Exports & Imports section in the Dashboard for the downloaded file. Please consult a tax advisor on how/whether to file these forms with state agencies.

## Check 1099 form requirements by state

Choose the form type to view state filing requirements:

- [1099-K](/connect/1099-K)
- [1099-NEC](/connect/1099-NEC)
- [1099-MISC](/connect/1099-MISC)

## Correct 1099 reports with the states

When you file a correction with the IRS, the state correction is filed at the same time. To file a correction with a state for a form that was already filed, you must create a correction.

## Frequently asked questions

The following section provides answers to common questions about filing tax forms through Connect.

### What happens if a connected account needs their form filed in multiple states?

Stripe does not support this at the moment. Stripe only checks eligibility and files in the state where the connected account’s address is registered.

### When we click “File”, does Stripe file with the IRS and the States at the same time, or do we have the ability to make changes if one has a later deadline?

Stripe files with the IRS and the State right away when you file the submission and you can’t make changes to that. But platforms are always able to make “corrections” and then file them and Stripe takes care of processing those corrections to the IRS and the State.

### How do I know if a particular form will be filed with the state?

We’ve introduced a new State filing status. For more information, see Understand tax form status.

### Can I override the filing requirement for State filing without overriding the filing requirement for Federal filing?

No. If you override the filing requirements, it applies to both federal and state filing.

### Why wasn’t the state filing status overridden when I selected “File even if incomplete”?

When you choose to override the filing status and select File even if incomplete, there are still certain edge cases where your form might still have a state filing status of Needs Attention. This is done to minimize the risk of rejections from the state. Take note of the following state-specific rules:

- Pennsylvania: The form must have a non-zero Taxpayer Identification Number (TIN) and pass a basic address validation check, which requires at least one digit and one number in the address.
- Illinois: The form must have a non-zero TIN and a valid payee name.
- Oregon: The form must have a non-zero TIN.
- District of Columbia: The form cannot have a TIN with all digits being the same number.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Prepare to file with the states](#prepare-to-file-with-the-states)[Choose the tax form type in the Dashboard](#choose-form-type)[Determine the states where your connected accounts are based](#determine-location)[Determine which states to file with](#determine-states)[Add the state tax Registration or withholding ID](#add-state-reg)[State-by-state breakdown](#state-by-state-breakdown)[Withholding](#withholding)[Check 1099 form requirements by state](#check-1099-form-requirements-by-state)[Correct 1099 reports with the states](#correct-1099-reports-with-the-states)[Frequently asked questions](#frequently-asked-questions)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`