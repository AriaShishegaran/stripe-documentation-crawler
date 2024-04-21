# Identify forms with missing information

Stripe automatically identifies forms that are above the IRS or state filing thresholds. In addition to the totals, a 1099 form also needs to have the name, address, and TIN of the connected account on the form to be ready for filing.

If a form is above the threshold (has a filing obligation) and has the name, address, and TIN on the form, Stripe labels the form Ready:

If you need to file a form but the form is missing this key information, Stripe labels the form Needs attention:

Refer to the Get started with tax reporting guide to learn more about tax form statuses.

[Get started with tax reporting](/connect/get-started-tax-reporting#understand-tax-form-status)

The following information describes how to track what forms have Needs attention status, why they have that status, and what to do to get their status to Ready.

## Identity forms in Needs attention state

The Needs attention tab lists all forms with a Needs attention status.

Some forms that appear to be below the federal filing threshold can also appear as Ready or Needs attention due to Grouped TINs or state filing thresholds. Learn more

[Learn more](/connect/file-tax-forms#below-threshold-forms)

The Payee details section lists the missing data that causes the form to have a Needs attention status:

Refer to the Required verification information for taxes guide for information on what information is needed for each form.

[Required verification information for taxes](/connect/required-verification-information-taxes)

The reasons a form might have a Needs attention status include:

- Missing address: The line1, city, state, or postal code is missing.

- Missing TIN: The TIN is missing.

- Mismatched TIN: The name and TIN are present on the form, but failed Stripe’s TIN verification with the IRS as they didn’t match IRS records. Learn more about Tax form TIN status.

[Learn more about Tax form TIN status](/connect/get-started-tax-reporting#understand-tax-form-tin-status)

- Missing name: The name is missing from the account. This reason is rare.

Use the filter to retrieve forms based on the reason for the Needs attention status:

## Remediation options

There are several ways to fix forms that need attention.

[Scenario A: You're able to retrieve the data](#scenario-a)

## Scenario A: You're able to retrieve the data

These are your options if you already have this data or able to retrieve it outside of Stripe.

- Option 1 Recommended:  If you already have this data in your internal systems, or have a way to reach out to your connected account owners to collect this information directly, use the Accounts API to send that data to Stripe. Make sure these required fields are present on the Accounts API. After you send the data to Stripe, it appears in the tax form within 24-36 hours, and the form automatically transitions from Needs attention to Ready.

[Accounts API](/api/accounts/update)

[fields](/connect/required-verification-information-taxes)

- Option 2: Use CSV imports to get this data into the current year’s tax forms. If the CSV process imports all of the required information, the tax form automatically transitions from Needs attention to Ready. Importing these details using CSV only updates this information on the tax form, and doesn’t update the source of truth within Stripe. As a result, the connected account details view doesn’t show these updates.

[CSV imports](/connect/modify-tax-forms?method=csv)

- Option 3: If you need to update only a few forms, you can choose to directly modify the forms in the Dashboard using the Tax Form Editor.

[Tax Form Editor](/connect/modify-tax-forms?method=dashboard)

[Scenario B: You want Stripe to help get the data](#scenario-b)

## Scenario B: You want Stripe to help get the data

These are your options if you don’t have the required information and you want Stripe to help you obtain this data. Stripe recommends using both options to for the best chance of collecting all the information for filing.

- Option 1: If you enable e-delivery through Stripe Express, connected account owners eligible for IRS filing receive emails from Stripe requesting confirmation of their tax information and to update their delivery preferences through Stripe Express. Connected account owners have an opportunity to view and edit their personal details (name, address, TIN).

Option 1: If you enable e-delivery through Stripe Express, connected account owners eligible for IRS filing receive emails from Stripe requesting confirmation of their tax information and to update their delivery preferences through Stripe Express. Connected account owners have an opportunity to view and edit their personal details (name, address, TIN).

[view and edit their personal details](/connect/platform-express-dashboard-taxes-walkthrough)

- Option 2: Use Stripe Onboarding to collect missing detailsAdd the 1099 capability on your accounts programmatically or one-by-one using the Connect Dashboard. By adding the 1099 capability, you make name, address, and TIN a requirement on all your connected accounts. If your connected accounts have more than 600 USD in lifetime volume and don’t have name, address, and verified TIN on file, payouts are paused until Stripe has that information.There’s another feature in private beta called Additional Verifications that allows platforms to add TIN and address requirements on their connected accounts, along with flexibility on when to disable payouts. Reach out to your account manager if you’d like to learn more.Create account links and route your users to Stripe onboarding for Custom accounts. For Express accounts, Stripe automatically detects when there are currently_due requirements (such as address or TIN) on the account and sends the connected account owner an email.

Option 2: Use Stripe Onboarding to collect missing details

- Add the 1099 capability on your accounts programmatically or one-by-one using the Connect Dashboard. By adding the 1099 capability, you make name, address, and TIN a requirement on all your connected accounts. If your connected accounts have more than 600 USD in lifetime volume and don’t have name, address, and verified TIN on file, payouts are paused until Stripe has that information.There’s another feature in private beta called Additional Verifications that allows platforms to add TIN and address requirements on their connected accounts, along with flexibility on when to disable payouts. Reach out to your account manager if you’d like to learn more.

[programmatically](/connect/account-capabilities#tax-reporting)

[one-by-one](/connect/dashboard/managing-individual-accounts#updating-capabilities)

- There’s another feature in private beta called Additional Verifications that allows platforms to add TIN and address requirements on their connected accounts, along with flexibility on when to disable payouts. Reach out to your account manager if you’d like to learn more.

- Create account links and route your users to Stripe onboarding for Custom accounts. For Express accounts, Stripe automatically detects when there are currently_due requirements (such as address or TIN) on the account and sends the connected account owner an email.

[account links](/api/account_links/create)
