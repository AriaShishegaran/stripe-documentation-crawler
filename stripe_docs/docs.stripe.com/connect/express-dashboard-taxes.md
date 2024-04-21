# Deliver tax forms with Stripe Express

## How does e-delivery work for connected accounts?

Starting with tax season 2021, Stripe enabled e-delivery of tax forms through the Stripe Express Dashboard. Your connected account owners can use the Tax Center on Stripe Express Dashboard to manage their tax forms, update their tax information, and manage their tax form delivery preferences. Learn more about working with your users to collect verified tax information for the upcoming tax season in the 1099 Tax Support and Communication Guide.

[Stripe Express Dashboard](/connect/express-dashboard)

[1099 Tax Support and Communication Guide](/connect/platform-express-dashboard-taxes)

Review a detailed product walk-through of the Stripe Express dashboard and Stripe outreach to your eligible connected accounts.

[product walk-through](/connect/platform-express-dashboard-taxes-walkthrough)

## Which connected accounts have access to e-delivery through the Stripe Express Dashboard?

E-delivery through the Stripe Express Dashboard is available to connected accounts that already have access to the Express dashboard and accounts where you have built and managed the full experience otherwise.

There are a few notable exceptions that might affect eligibility for e-delivery. For most platforms, these exceptions include less than 2% of connected accounts.

- More than five connected accounts tied to a single email, whether each account has the same TIN or different TINs. Stripe continues to deliver forms through paper mail for these accounts.

- Payees who don’t have an eligible connected account on Stripe. For example, if you pay someone by check, you can’t deliver their tax form through Stripe Express.

- Only current owners receive forms for connected accounts that have been sold or had their businesses transferred prior to receiving their 1099. Previous owners receive paper forms to the address on file if you split the form.

- Accounts that haven’t been activated in Stripe yet.

For the accounts that aren’t eligible for e-delivery, Stripe can support postal deliveries to the address on file.

## When can my connected account owners access the Tax Center on the Stripe Express Dashboard?

Connected account owners that currently do not have access but are eligible for it can view the Stripe Express Dashboard and the tax forms page starting in November 2023 after receiving the email invitation from Stripe. This will be triggered if you choose to turn on e-delivery of your tax forms through the Express Dashboard and enable early collection of tax information and delivery preferences under your 1099 tax settings.

Currently, connected account owners with existing access to the Express Dashboard can edit their tax information. When you opt your platform in to e-delivery, your connected owners see the tax forms page with a row for your platform.

## How do I enable outreach using the Stripe Express Dashboard to collect identity information and e-delivery consent ahead of tax season?

Collection of tax identity information and e-delivery consent early in the tax season is critical for enabling a smooth tax season. If your platform opts for e-delivery through the Express Dashboard and enables collection of tax information in advance using 1099 tax form settings, Stripe emails platforms’ connected accounts starting the week of November 1st, 2023 to confirm their tax information and provide e-delivery consent through the Express Dashboard. Note, we don’t send outreach emails to platforms’ connected accounts until 7 days after you enable the setting.

This outreach from Stripe gives connected account owners an opportunity to review and update their tax information and confirm their delivery preferences before you file with the IRS, which maximizes e-delivery opt-in rates, speeds up tax form delivery, and minimizes errors on finalized 1099 forms.

If you don’t enable collection of tax information in advance and only configure e-delivery, postal delivery initiates at the time you file for any accounts that have not provided e-delivery consent. If accounts provide consent after you file, that consent is applicable only for the next tax year.

## How does a connected account without current access gain access to the Stripe Express Dashboard?

Connected account owners that are eligible for access to the Express Dashboard receive an invite from Stripe to confirm their tax information starting in November 2023. These emails include a link to Stripe Express Dashboard Account claims. For connected account owners who’ve never claimed their account and accessed the Stripe Express Dashboard, we first gather their email and phone number to set up their credentials. After that, we present them with a series of identity verification questions (Name, TIN, and DOB) to validate that they do own the account. If they fail these challenges, we provide follow-up questions such as address, Bank Last 4, and last payout amount from the platform to verify their identity. If they fail these questions after multiple attempts, we kick-off a manual review through Stripe Express support.

## Which email address does Stripe use for e-delivery?

For connected accounts that have access to the Express dashboard from onboarding: Stripe already has emails associated with these users that are collected at onboarding. For these accounts, Stripe emails the primary user associated with the account. Multi-user Express Dashboard accounts aren’t supported.

If an eligible connected account without current access claimed their account on Stripe Express with a valid email address and phone number, the email address they used to sign up is what Stripe uses. Otherwise, Stripe uses the email address on the account.

Stripe can’t deliver forms electronically if there is no email address on the account. Instead, Stripe attempts to deliver paper forms if a valid address is on the tax form and you opted in to paper delivery.

## Why do emails need to be updated for connected accounts?

In order for a connected account owner to onboard, log in to the Stripe Express Dashboard, or access their tax forms, they need to be able to receive the email from Stripe inviting them to create their account. If for some reason the user has updated their email, Stripe is only able to resend these emails to the email address on file so they must contact your platform for assistance updating their email.

You only need to update emails on behalf of the connected account owners before they’ve claimed their accounts. After the owner claims the account, then Stripe is able to assist your users with updating their emails.

## How do I update the email address?

You can update the email addresses on your connected accounts in the following ways:

- Use the Update API.

[Update](/api/accounts/update#update_account-email)

- Use the CSV import functionality on the Emails page in the Dashboard.

[Emails page](https://dashboard.stripe.com/settings/connect/emails)

- Edit the email addresses in the Payee Details section in the 1099 dashboard.

You can’t update email addresses using the email_address field in a CSV import directly into the 1099 product. Changes made using this method don’t carry over each year.

## How do connected accounts edit their information?

As your connected accounts onboard to the Stripe Express Dashboard, account owners can edit their account details within the Tax forms page. They are able to edit their name, their TIN, and their address, but they aren’t able to change their date of birth or their entity type. For date of birth and entity updates, account owners need to contact Stripe Support.

## How are tax forms kept in sync between the platform and the connected account?

The Tax forms view in the Dashboard is still the main place to generate, correct, split, and file 1099s for your connected accounts. Onboarding to the Stripe Express Dashboard integrates the data from the Tax forms view in the Dashboard directly into the Stripe Express Dashboard if it’s accessible to your connected account owners. Edits made by connected account owners (Name, Social Security Number or Employer Identification Number, address) update your connected accounts and thus the forms in the Tax forms view in the Dashboard until they are filed. For any updates made by a connected account after the filing date, you are given the choice to either correct the tax form or leave the tax form as is. Updates might take up to 24 hours to sync due to TIN aggregation done by Stripe.

[Tax forms](https://dashboard.stripe.com/connect/taxes/forms)

Stripe doesn’t share the updated sensitive PII (such as SSN or EIN) from accounts with your platform through the API for security reasons.

## Can I collect consent for e-delivery through the Stripe Express Dashboard?

Yes, the Stripe Express Dashboard can collect e-delivery consent from your connected accounts. Connected accounts can only view their tax forms after providing e-delivery consent. After providing e-delivery consent, connected accounts are provided with the option to request an optional paper copy. You can update the e-delivery consent for an individual form through either the Form Editor UI on the 1099 Dashboard or using a CSV import using the ‘e-delivery consent’ field from Jan 2023.

[CSV import](/connect/modify-tax-forms?method=csv#import-tax-forms)

Connected accounts are directed to your support team if they would like to revoke e-delivery consent.

## How do connected accounts get alerted when their 1099 forms are available?

Stripe sends an email notification to your connected accounts when their 1099 forms are available. This email includes both Stripe’s logo and your platform’s logo. The platform logo is taken from your Connect branding settings, so please make sure this is up to date before the week of November 1st, 2023.

[Connect branding settings](https://dashboard.stripe.com/settings/connect)

For connected accounts where you own the full experience otherwise, make sure that you also update email addresses on the accounts before the week of November 1st, 2023 so Stripe can email them the following week.  You can update this information using the Accounts API. Express connected accounts already have a user associated with them, and Stripe emails tax forms to the primary user associated with the account.

[update email addresses](/api/accounts/update#update_account-email)

## How should I prepare my connected accounts for e-delivery and the upcoming tax season?

Prepare your connected accounts:

Create a support article with information for your connected account owners to let them know that their 1099s will be delivered by Stripe and that they should expect to receive an email from Stripe in January. See an example.

[See an example](https://help.doordash.com/dashers/s/article/Common-Dasher-Tax-Questions?language=en_US)

Communicate with all eligible connected account owners to let them know they should expect to receive an email from Stripe. This helps with maximizing opt-in to e-delivery and minimizing concerns about phishing.

Subject: Our tax partner Stripe will be sending you an important email. Body: “In the next few days, you will receive an email from Stripe with a link to download your 1099 tax form. <Platform_Name> partners with Stripe to facilitate payments and tax reporting, including 1099 forms. We recommend adding express@stripe.com to your address book so the email isn’t marked as spam. When you receive the email, please click into it and follow the instructions to confirm your tax details.”

## How do I navigate to prior years tax forms?

In the Dashboard, choose the year in the dropdown to look for past years’ forms.

Forms for 2019 or earlier aren’t available through your Dashboard. These forms might be filed through a different system called Payable. If you used Stripe during that period of time, please reach out to support to get the tax forms you need.

## Why are my users being asked to enter the last four digits of their TIN to download their forms?

Connected account owners who have consented to e-delivery must pass a TIN validation to download their tax forms as an added layer of security. The key here is that they must enter the last four digits of the TIN exactly as it appears on their 1099 tax form. For Prior Years tax forms, we present a similar TIN challenge to enter the last four digits for the TIN as it appears on that particular form. If your platform didn’t use Stripe in the past to file 1099s, then those forms aren’t available in the Dashboard.

## Why are connected account owners having issues validating their TIN?

Your users might run into issues downloading their 1099 tax forms if they have updated the TIN on their connected account, if your platform has overwritten the TIN on the 1099 tax form, if they’ve simply forgotten the TIN that appears on the tax form, or if they recently received a new TIN from the IRS and it isn’t in their system yet.

In these instances, users reach out to your platform so that you can work with your users to confirm what TIN appears on the 1099 tax form or assist them with getting a corrected version of their 1099 tax form. You can also download the user’s tax form from the Tax forms dashboard and email it to them directly. Only team members with the Tax Analyst role are able to access this information.

## What else can a connected account manage using the Stripe Express Dashboard?

The Stripe Express Dashboard also includes the Earnings page, which displays connected accounts’ upcoming payouts and earnings history through the activity feed. The activity feed shows transactions from your platform that affect connected accounts’ balances, such as payments, refunds, transfers, and payouts.

[upcoming payouts and earnings](/connect/customize-express-dashboard#set-custom-descriptions)

In the Account settings, connected account owners can update account details including legal entity information and personal information such as name, address, and taxpayer identification numbers, and view and update their bank account information for payouts.

## Why are payouts blocked, restricted, or show as restricted soon for my account?

Your connected account might get blocked after they update their information for a few different reasons:

- If you have applied a capability such as a 1099 capability, and they update their name or TIN to a value that doesn’t match against the IRS database then they must update their information in Stripe Express with a valid name and TIN combination.

- If your connected account was verified previously and changes their name and/or TIN, they are prompted to re-sign a Terms of Service agreement. Failure to do so might result in payouts being blocked until your account goes into Stripe Express and re-signs their Terms of Service agreement.

- If your connected account updates their details with values that can’t be verified against standard government databases, they might be asked to upload proof of identity that helps Stripe identify them. Failure to do so results in payouts being blocked. Your accounts can go into Stripe Express and submit proof of identity under the Accounts section.

## Are Taxpayer Identification Numbers (TINs) checked against the IRS database?

TIN is verified against the IRS database if:

- You have applied the 1099-K, 1099-MISC, or any other capabilities that require a verified TIN, and

- The connected account meets the threshold for the applied capability.

[capability](/connect/required-verification-information-taxes#required-information)

Connected accounts that enter an incorrect Name-TIN combination might see their payouts paused until they log back in to Stripe Express to update their Name and TIN with verified information.

[update their Name and TIN](https://support.stripe.com/express/questions/how-do-i-update-my-tax-information)

## I made a correction to a 1099, how long does this take to sync?

You can correct only tax forms that the IRS has accepted. To start a correction, update the data in the tax forms. You can use either the Tax form editor or CSV export to update the tax form. After you update the form, select the updated form on the Tax forms page, then click Correct to create a correction. It can take up to 48 to 72 hours after the platform files the correction for the payee notification.

## Are my connected accounts able to consolidate their view of taxes across platforms?

As they get paid from different platforms, Stripe Express users can add each platform to the same Stripe Express accounts to create a single view of their earnings and their tax forms.

## Is there a Stripe support address we can direct users to in our help center or is this only available in the onboarding flow of the Express App?

Direct users to https://support.stripe.com/express. From here they can contact Stripe which ensures their questions are routed to a specialized support group best able to help them.

[https://support.stripe.com/express](https://support.stripe.com/express)

## How can a connected account get their invitation email sent again?

The connected account owner can request a new invitation link that’s sent to their email. Direct them to this support page to resend their own invitation email. Ineligible users (connected accounts that didn’t meet the 2023 threshold of $600 for NEC/MISC or $20,000 and 200 transactions for K) don’t receive an email from Stripe.

[this support page](https://support.stripe.com/express/how-do-i-get-a-new-invite-link)

## If a connected account owner consents to e-delivery, do they still get a mailed copy?

If the platform has paper delivery enabled, Stripe presents the connected account owner with the option to request this method of delivery. If they select this option, then Stripe mails the paper copy of their tax form to the address the platform has on file.

## Edge cases for 1099 tax reporting

The new Stripe Express dashboard doesn’t support certain types of accounts, as follows:

- Multi-user and multi-currency accounts: Accounts that have multiple users or multiple currencies associated with them aren’t able to view the Express Dashboard and hence don’t receive electronic delivery of forms.

- Five or more connected accounts sharing the same email: When five or more connected accounts for the same platform have the same email, they don’t receive an email from Stripe

- Rejected and deleted accounts: Accounts that you have rejected or deleted no longer have a Stripe relationship and hence are ineligible to login to the Stripe Express Dashboard.

- Split forms: If a form is split (as in not tied to the active user of a connected account), it’s not eligible for electronic delivery.

## What tax details are prompted for during the pre-verification?

For merchants set up as US Companies, Stripe’s 1099 product uses the business tax details except when they’re set up as a single member LLC or sole proprietorship, in which case it uses the owner’s personal tax details because those account types are disregarded entities for income tax purposes according to the IRS. For Individuals, Stripe uses personal tax details. For more information, refer to Updating 1099 tax form details for connected accounts.

[Updating 1099 tax form details for connected accounts](https://support.stripe.com/questions/updating-1099-tax-form-details-for-connected-accounts)

If a connected account requests to use their business tax details on their 1099 tax form, and you want to support that, you can make the changes by collecting the business tax details from the user, and updating the 1099 tax forms using CSV import or the Tax Form Editor once tax form totals are finalized in January.

[updating the 1099 tax forms using CSV import](/connect/modify-tax-forms?method=csv#1099-csv-schema)

[Tax Form Editor](/connect/modify-tax-forms?method=dashboard#understanding-the-tax-form-editor-ui)

## My connected account did not receive a pre-filing confirmation email

To check whether your connected account has received an email invite, go to the 1099 Dashboard page. If the pre-filing confirmation status is Sent, Stripe attempted outreach to your user. If the status is Queued or Not eligible, like the example below, Stripe hasn’t sent an invite yet.

[1099 Dashboard page](https://dashboard.stripe.com/connect/taxes/forms)

To send your user the pre-filling confirmation email, first confirm that their email address in Stripe is correct. Then, follow these steps:

If Stripe hasn’t sent the pre-filing confirmation email, confirm that your user’s email in Stripe matches the email where they expect to receive the tax form.

To update your user’s email address, follow the steps below. Learn more about other ways to update emails for your accounts.

[update emails for your accounts](#how-do-i-update-the-email-address)

## My connected account was locked out of their Stripe Express account for failing the verification process. How can I resolve this issue?

Connected accounts must claim their Stripe accounts in order to view the Tax Center in the Express dashboard. To authorize the claim, Stripe asks the user a series of questions to verify their identity. For security reasons, if the user fails to correctly answer the verification questions too many times, Stripe locks their account. You can see the status in the 1099 dashboard. A status of “Not claimed, no attempts left” means the connected account is locked. A “Claimed” status means the connected account claimed their Stripe account.

You can reset your user’s claim attempts in the 1099 Dashboard. Before removing them from manual review, we recommend reviewing and updating account claim information (such as representative name, address, SSN, EIN, and DOB) with your connected account. Otherwise, the account might continue to fail to claim their Express account.

If there’s a mismatch between the information you have on file and what your user expects, you can update their connected account directly. You can’t make updates in the 1099 Dashboard and you must have the correct user role.

[update](/connect/updating-service-agreements)

[user role](/get-started/account/teams/roles)
