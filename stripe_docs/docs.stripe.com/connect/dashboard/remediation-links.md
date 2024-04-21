# Remediation link process walkthrough

Remediation links are a no-code solution for platforms to collect verification information from their connected accounts. Platforms generate account-specific remediation links in the Dashboard, then send them to connected accounts through any communication channels, such as email, chat, in-app notifications, or support interactions. When a connected account clicks a remediation link, it takes them to a Stripe-hosted page where they can provide updated information directly to Stripe.

Remediation links are active for 90 days and an account can access them multiple times. If a link expires, you can generate a new one.

Only the following user roles have permission to generate remediation links:

[user roles](/get-started/account/teams/roles)

- Administrator

- Connect Onboarding Analyst

- Developer

- Data Migration Specialist

- Support Associate

- Support Specialist

You can only generate remediation links in the Dashboard, not using the API. To use the API to direct connected accounts to onboarding, create Account links, which are temporary and can only be used once.

[Account links](/connect/custom/onboarding?verification=hosted#stripe-hosted-onboarding)

The page that a remediation link opens depends on the account’s configuration:

[platform Dashboard](https://dashboard.stripe.com/settings/connect/site-links)

This page walks through the process of generating and sending remediation links and describes the experience of a connected account when they use a link.

## 1. Generate remediation links

You can generate a remediation link for an individual account or export a list of remediation links for multiple accounts.

You can generate a link for an account from the Accounts to review tab of your Connect Dashboard or from that account’s details page.

[Connect Dashboard](https://dashboard.stripe.com/connect/accounts_to_review)

On the Accounts to review tab, find the account in the Action required list or In review list. Hover over the account’s overflow menu , then click the link icon .

Generate a remediation link from Accounts to review list

In the Activity section of the connected account’s details page, select the Actions required tab and click an issue to open its possible remediation paths. Generate the link by clicking Send a remediation link. If the account can’t address the issue through a remediation link, then that path doesn’t appear.

Generate a remediation link from the connected account’s details page

On the Accounts to review tab of your Connect Dashboard, filter the view to include the accounts that you want to generate remediation links for, then click Export. In the export dialog, select Remediation link and any other desired fields, then export the list of accounts.

Export a list of accounts

## 2. Send remediation links to connected accounts

You can send remediation links by any communication channel. Because they direct accounts to a Stripe-hosted page, we recommend that when you send a link, you inform the account that you partner with Stripe for payments. That explains why your link takes them to a Stripe-hosted page.

Here’s an example of an email that a platform might use to send a remediation link:

Remediation link email

## 3. Understand what a connected account sees when they click a remediation link

The following tabs help you and your support team understand remediation links from the perspective of a connected account. The screenshots are examples of what a connected account might see, and don’t necessarily match the actual pages presented to your accounts.

For Custom connected accounts, remediation links take them to Stripe-hosted onboarding. To securely update account information, a custom account owner must create a Stripe user account. If the account owner has already clicked the remediation link and verified their identity in the current browser session, clicking the link again takes them directly to the information collection step.

- The account owner enters their phone number and email address

This information establishes the identity of the person updating verification information for the Custom connected account. We use the phone number for SMS authentication with a one-time-password. The phone number doesn’t have to match any number already associated with the account. We only use the email address as a backup authentication method. We don’t send any other emails to that address.

If the email address is associated with an existing Stripe user account, we prompt them to log in to that account using its existing password.

Enter phone number and email address

- The account owner verifies the phone number

We send a code in an SMS message to the phone number and prompt the account owner to enter it. If they access the link again in another browser session, or access another remediation link, we send a new code for re-authentication.

Verify the phone number

- The account owner verifies their identity

To make sure that only authorized people access account information, we prompt the account owner to verify their identity by requesting details associated with the account and its representative. If they fail to enter the requested details a few times, they see the following error message:

One of the fields didn't match the information we received from [platform_name]. You can try again, or check that your information with [platform_name] is up to date.

If the account owner has already verified their identity, or has onboarded through Stripe Express (such as to access Stripe’s Tax Reporting Dashboard), we skip this step.

Verify identity

- The account owner provides information

After verifying the account owner’s identity, we present forms for entering required information.

Remediation links automatically collect both current and future requirements. To control which requirements are collected, direct your accounts to hosted onboarding using Account Links with the collection_options parameter.

[Account Links with the collection_options parameter](/api/account_links/create#create_account_link-collection_options)

If the account has any outstanding risk reviews, we present them first. The following is an example of a risk review form:

Example risk review form

After the forms for any risk reviews, we prompt the account owner to provide any additional information that requires updating. For example, if the statement descriptor isn’t aligned to the business, we present the screen for collecting public details including the statement descriptor, highlighting any fields with errors.

After collecting all the information, we display a summary screen, highlighting any fields that are still outstanding or pending verification from Stripe. To update a field, they can click Edit in the corresponding section.

If an account owner clicks a remediation link and has no outstanding risk reviews or outstanding information requirements, they see the summary page.

Summary page

An account owner can update information in these forms other than the required fields. If they do so, they can trigger additional reviews or verifications. For example, changing the SSN can require the account owner to re-accept the Stripe terms of service or to upload an identity document. The account owner can use the same remediation link to address any additional requirements.
