htmlRemediation link process walkthrough | Stripe Documentation[Skip to content](#main-content)Remediation links[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fdashboard%2Fremediation-links)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fdashboard%2Fremediation-links)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Remediation link process walkthrough

Learn how to use remediation links to collect verification information from your connected accounts.Remediation links are a no-code solution for platforms to collect verification information from their connected accounts. Platforms generate account-specific remediation links in the Dashboard, then send them to connected accounts through any communication channels, such as email, chat, in-app notifications, or support interactions. When a connected account clicks a remediation link, it takes them to a Stripe-hosted page where they can provide updated information directly to Stripe.

Remediation links are active for 90 days and an account can access them multiple times. If a link expires, you can generate a new one.

Only the following user roles have permission to generate remediation links:

- Administrator
- Connect Onboarding Analyst
- Developer
- Data Migration Specialist
- Support Associate
- Support Specialist

NoteYou can only generate remediation links in the Dashboard, not using the API. To use the API to direct connected accounts to onboarding, create Account links, which are temporary and can only be used once.

The page that a remediation link opens depends on the account’s configuration:

Connected account has access to:Remediation link opens:A Stripe embedded onboarding component and embedded notification bannerA platform website page that contains the notification banner; configured in the[platform Dashboard](https://dashboard.stripe.com/settings/connect/site-links)Stripe Dashboard (Standard accounts)Account Status page in the Stripe DashboardExpress Dashboard (Express accounts)Stripe Express onboarding flowNo Stripe Dashboard (Custom accounts)Stripe-hosted onboarding; account holder must create a Stripe accountThis page walks through the process of generating and sending remediation links and describes the experience of a connected account when they use a link.

## 1. Generate remediation links

You can generate a remediation link for an individual account or export a list of remediation links for multiple accounts.

### Generate a link for an individual account

You can generate a link for an account from the Accounts to review tab of your Connect Dashboard or from that account’s details page.

On the Accounts to review tab, find the account in the Action required list or In review list. Hover over the account’s overflow menu , then click the link icon .

![](https://b.stripecdn.com/docs-statics-srv/assets/remediation-links-listview.086eeab10e2d47ec1286946ba3471942.png)

Generate a remediation link from Accounts to review list

In the Activity section of the connected account’s details page, select the Actions required tab and click an issue to open its possible remediation paths. Generate the link by clicking Send a remediation link. If the account can’t address the issue through a remediation link, then that path doesn’t appear.

![](https://b.stripecdn.com/docs-statics-srv/assets/remediation-links-connected-account-detail.86a05ab693818dc38d2376ad33ebd98d.png)

Generate a remediation link from the connected account’s details page

### Export links for multiple accounts

On the Accounts to review tab of your Connect Dashboard, filter the view to include the accounts that you want to generate remediation links for, then click Export. In the export dialog, select Remediation link and any other desired fields, then export the list of accounts.

![Export a list of accounts](https://b.stripecdn.com/docs-statics-srv/assets/bulk-export-A2R.56ffa4d9f3eb55c08a1eb71ed46f0904.png)

Export a list of accounts

## 2. Send remediation links to connected accounts

You can send remediation links by any communication channel. Because they direct accounts to a Stripe-hosted page, we recommend that when you send a link, you inform the account that you partner with Stripe for payments. That explains why your link takes them to a Stripe-hosted page.

Here’s an example of an email that a platform might use to send a remediation link:

![Example of a remediation link email](https://b.stripecdn.com/docs-statics-srv/assets/email-action-required.15e5878a481c6a8726e15965bdfaffe1.png)

Remediation link email

## 3. Understand what a connected account sees when they click a remediation link

The following tabs help you and your support team understand remediation links from the perspective of a connected account. The screenshots are examples of what a connected account might see, and don’t necessarily match the actual pages presented to your accounts.

Custom accountsExpress accountsStandard accountsFor Custom connected accounts, remediation links take them to Stripe-hosted onboarding. To securely update account information, a custom account owner must create a Stripe user account. If the account owner has already clicked the remediation link and verified their identity in the current browser session, clicking the link again takes them directly to the information collection step.

1. The account owner enters their phone number and email address

This information establishes the identity of the person updating verification information for the Custom connected account. We use the phone number for SMS authentication with a one-time-password. The phone number doesn’t have to match any number already associated with the account. We only use the email address as a backup authentication method. We don’t send any other emails to that address.

If the email address is associated with an existing Stripe user account, we prompt them to log in to that account using its existing password.

![Phone and email form](https://b.stripecdn.com/docs-statics-srv/assets/custom-hosted-form-phone.aba39ace900df058332908895a12e362.png)

Enter phone number and email address

1. The account owner verifies the phone number

We send a code in an SMS message to the phone number and prompt the account owner to enter it. If they access the link again in another browser session, or access another remediation link, we send a new code for re-authentication.

![Phone number verification form](https://b.stripecdn.com/docs-statics-srv/assets/custom-hosted-form-sms.8caf66b1b4b13bebf8a3ffe9dfbaefb0.png)

Verify the phone number

1. The account owner verifies their identity

To make sure that only authorized people access account information, we prompt the account owner to verify their identity by requesting details associated with the account and its representative. If they fail to enter the requested details a few times, they see the following error message:

One of the fields didn't match the information we received from [platform_name]. You can try again, or check that your information with [platform_name] is up to date.

If the account owner has already verified their identity, or has onboarded through Stripe Express (such as to access Stripe’s Tax Reporting Dashboard), we skip this step.

![Identity verification form](https://b.stripecdn.com/docs-statics-srv/assets/custom-hosted-form-identity.bbe88e8a2278a893f3490b6229f11e03.png)

Verify identity

1. The account owner provides information

After verifying the account owner’s identity, we present forms for entering required information.

NoteRemediation links automatically collect both current and future requirements. To control which requirements are collected, direct your accounts to hosted onboarding using Account Links with the collection_options parameter.

If the account has any outstanding risk reviews, we present them first. The following is an example of a risk review form:

![Example of a risk review form](https://b.stripecdn.com/docs-statics-srv/assets/custom-hosted-form-risk.1f54e301a7ad0f5946bfb011dbb44e76.png)

Example risk review form

After the forms for any risk reviews, we prompt the account owner to provide any additional information that requires updating. For example, if the statement descriptor isn’t aligned to the business, we present the screen for collecting public details including the statement descriptor, highlighting any fields with errors.

After collecting all the information, we display a summary screen, highlighting any fields that are still outstanding or pending verification from Stripe. To update a field, they can click Edit in the corresponding section.

If an account owner clicks a remediation link and has no outstanding risk reviews or outstanding information requirements, they see the summary page.

![The summary page](https://b.stripecdn.com/docs-statics-srv/assets/custom-hosted-summary.b6a700157643004b92918a31d3edf3d0.png)

Summary page

NoteAn account owner can update information in these forms other than the required fields. If they do so, they can trigger additional reviews or verifications. For example, changing the SSN can require the account owner to re-accept the Stripe terms of service or to upload an identity document. The account owner can use the same remediation link to address any additional requirements.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[1. Generate remediation links](#1.-generate-remediation-links)[2. Send remediation links to connected accounts](#2.-send-remediation-links-to-connected-accounts)[3. Understand what a connected account sees when they click a remediation link](#3.-understand-what-a-connected-account-sees-when-they-click-a-remediation-link)Products Used[Connect](/connect)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`