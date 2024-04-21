htmlSupport recommendations and FAQ templates | Stripe Documentation[Skip to content](#main-content)FAQ template for connected accounts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fplatform-express-dashboard-taxes-faqs)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fplatform-express-dashboard-taxes-faqs)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[1099 Tax Support and Communication Guide](/docs/connect/platform-express-dashboard-taxes)# Support recommendations and FAQ templates

Respond to top FAQs from connected accounts during 1099 tax season.Familiarize yourself with the connected account express experience by reviewing our product walkthrough.

We know that supporting your connected accounts during tax season can be tricky. We’ve created this guide that addresses top reasons platforms contact Stripe support for help assisting your connected accounts. We’ve also assembled a set of the questions platforms tell us are most often asked by their connected accounts during 1099 tax season and provided boilerplate responses to those questions for you to incorporate as part of your own tax support strategy.

## Platform support recommendations

The following sections represent the questions platforms often contact Stripe support about during 1099 tax season, along with our recommendations for how you can proactively support your connected accounts.

### A connected account wants to know if they’ve already been sent a pre-filing confirmation email from Stripe

To check whether we sent a pre-filing confirmation email to your connected account:

1. Head to the[1099 tab](https://dashboard.stripe.com/connect/taxes/forms)of the Tax Forms dashboard.
2. Use the filterStripe merchant IDto locate the connected account’s 1099 tax form.
3. Check the[Pre-filing confirmation](/connect/tax/whats-new-2023#tracking-stripe-outreach)email status and share with the payee.

![Tax form with pre-filing confirmation status](https://b.stripecdn.com/docs-statics-srv/assets/tax-forms-pre-filing-confirmation-status.15e4a385e3360ece2cd743f4285e93b3.png)

The Pre-Filing confirmation property has the following statuses:

- Queued: This connected account is in the queue and we’ll send their pre-filing confirmation email soon.
- Sent: We sent this connected account their pre-filing confirmation email.
- Not eligible: This connected account isn’t eligible for inclusion in pre-filing confirmation. Possible reasons for ineligibility include:  - The account is missing an email address.
  - The account is under the 1099 reporting threshold
  - The account’s configuration excludes it from eligibility.See[Edge Cases](/connect/platform-express-dashboard-taxes-faqs#edge-cases-for-1099-tax-reporting)for more information.


- Not Sent: This connected account is eligible but wasn’t sent an invite prior to the cutoff date for pre-filing confirmation. See[Tax season 2023 checklist](/connect/get-started-tax-reporting#tax-season-checklist)for more details.

### A connected account hasn’t received or can’t find their pre-filing confirmation email from Stripe

To assist a connected account with getting their pre-filing confirmation email: Before taking any steps in the 1099 tab of the Tax Forms dashboard, advise your connected account to:

1. Check their inbox and spam folders for email with this subject line,Get your [Platform_Name] 2023 tax forms faster by enabling e-delivery.
2. Use the[self-serve tool](https://support.stripe.com/express/how-do-i-get-a-new-invite-link)to resend an invite email to themselves.

NoteThe email address must match the one associated with their Stripe account.

If those options don’t work, head to the 1099 tab of the Tax Forms dashboard to troubleshoot:

Check if the payee is 1099 eligible:

1. Use the filters in the[1099 tab](https://dashboard.stripe.com/connect/taxes/forms)of the Tax Forms dashboard to locate the connected account’s 1099 tax form.
2. [Review the Pre-filing confirmation status](/connect/tax/whats-new-2023#tracking-stripe-outreach). If the status isNot eligibleuse the information in the tooltip to understand why.

Check if the payee has the correct email address or is missing an email address:

- [Select the Edit option next to the email address field](/connect/tax/whats-new-2023#addressing-missing-emails)and add the correct email address. This updates the email address associated with the connected account itself, to avoid issues in future tax seasons.
- Learn more about other ways to[update emails for your accounts](/connect/express-dashboard-taxes#how-do-i-update-the-email-address).

![Account email address](https://b.stripecdn.com/docs-statics-srv/assets/tax-forms-account-email.d60fd2c08eb5fedad766f98b0e5b9502.png)

![Edit account email address modal](https://b.stripecdn.com/docs-statics-srv/assets/tax-forms-edit-account-email-modal.834f62cb61d6a4f2574e40b0e4146347.png)

Navigate to the overflow menu () and select the option to ‘Request pre-filing confirmation’ to send an invite email to the payee’s email address.

![Request pre-filing confirmation link](https://b.stripecdn.com/docs-statics-srv/assets/tax-forms-request-pre-filing-confirmation-link.fb53ecb1d73b4bbacf9f92b5a7c055b4.png)

![Request pre-filing confirmation modal](https://b.stripecdn.com/docs-statics-srv/assets/tax-forms-request-pre-filing-confirmation-modal.04e45b1768e12dbd2a3db1bdd09bc85c.png)

### A connected account has used up all account claim attempts and is blocked from retrying

To reset the account claim attempts for a connected account:

1. Head to the[1099 tab](https://dashboard.stripe.com/connect/taxes/forms)of the Tax Forms dashboard.
2. Locate the connect account’sAccount claim status.  - If the status isNot claimed, no attempts left, navigate to the overflow menu () and select the option toReset account claim attempts.
  - If the status isNot claimedand the payee is still struggling with access, check that you have the most up to date information on file for the account and if required, send a new pre-filing confirmation invite to the connect account.



Account claim status has the following values:

- Claimed: the connected account has completed account claim and has access to the Stripe Express dashboard.
- Not claimed, no attempts left: the connected account has exhausted their attempts to complete account claim and the platform must reset them.
- Not claimed: the connected account has either not attempted yet or still has account claim attempts remaining.

### A connected account wants to use their business tax details instead of their personal details (or vice versa) on their 1099 tax form

The tax details that appear on the 1099 tax form are determined by a connected account’s business type. The IRS expects to see an SSN provided on 1099 forms for Single Person Entities (SPEs). To change the tax details that appear on the form, you can update the connected account’s business type by:

1. Collect the following details from the connected account:  - Desired legal entity type
  - Desired legal entity name and TIN


2. Locate the connected account, navigate toBusiness details, and selectEdit.
3. SelectChange business typeand choose the desiredType of businessandBusiness structure.
4. Follow the prompts to enter the new legal entity details for the connected account’s business.
5. Return to the[1099 tab](https://dashboard.stripe.com/connect/taxes/forms)of the Tax Forms dashboard and verify that the name and TIN on the 1099 tax form match what was shared with you from the connected account.
6. If necessary, edit the 1099 tax form with the newly supplied information.

NoteOnly certain user roles can update this information in the Dashboard, such as the Connect Onboarding Analyst or an Admin. Tax Analysts can’t edit connected account information. See Team roles documentation for more information. You can also update this information using the accounts_update API.

### A connected account no longer has access to the phone number they used for their Stripe Express account

To help your connected account update their phone number:

1. Direct your connected account to the options at the bottom of the[Stripe Express login page](http://express.stripe.com/).
2. Once there, they should select[I no longer have access to this phone](https://support.stripe.com/express/questions/i-lost-my-phone-or-changed-my-number-how-do-i-login-to-my-account)and follow the prompts to update their phone number.

NoteThe payee must have access to the email address that is listed for the connected account to complete the required verification steps.

### A connected account agreed to paperless delivery but also wants a postal mailed copy sent to them

After setting up their account during pre-filing confirmation, your connected account can change their delivery preferences in the Tax Forms page of Stripe Express. To request a mailed copy of their 1099, they can:

1. Navigate to the Tax Forms page of Stripe Express.
2. Select the overflow menu () next to their most recent 1099 tax form.
3. SelectEdit information.
4. Switch the toggle forPostal mail deliveryfromOfftoOn.

NoteThis is only available if you as the platform have opted into Optional Post Delivery in your Delivery Settings.

### A connect account has requested a transaction log of all the transactions included in their 1099 tax form

See Export transaction logs for instructions on exporting the logs for each 1099 form.

## 1099 Tax Support FAQ template for connected accounts

We recommend creating public-facing support articles about the Stripe Express tax experience for your connected accounts. View a great example from DoorDash.

### What are 1099s?

1099 forms are federal income tax information forms used to report earnings and proceeds other than wages, salaries, and tips (which are reported on the federal W-2 form). The forms are filed with the US Internal Revenue Service (IRS) and, if required, state tax departments. Forms must be delivered to recipients by January 31 and can be postal mailed or sent via paperless delivery.

### What is Stripe Express, and how do I access it?

Stripe Express allows you to update your tax information, manage tax forms, and track your earnings. If you’re working with [Platform_Name] and earned $600 or more (within the calendar year in the US), Stripe will send an email inviting you to create an account and log in to Stripe Express.

### How do I download the app?

If you’d like to download the Stripe Express app, you can do so here from:

- iOS:[https://apps.apple.com/us/app/stripe-express/id1560214813](https://apps.apple.com/us/app/stripe-express/id1560214813)
- Android:Not available

### Do I have to download an app?

You don’t need to download an app. You can use either the web-based portal or the Stripe Express app to access your account and tax information.

### Which email address does Stripe use to send Stripe Express invitations?

Stripe uses the email information associated with your [insert platform name] account to send you an invitation to sign up for Stripe Express.

If you’re unable to find that email, head to this Support site page where you can request a new link to be sent to your email. If you still are not able to locate your invite email, please reach out to [Platform_Name] support for help updating your email address and getting a new invite email.

### I no longer have access to the phone number I signed up with. How do I log in to my Stripe Express account?

If you’ve lost or updated your phone number, you can select the “I no longer have access to this phone number” option during login or account creation to authenticate via email and change your phone number.

### I earned enough to need a 1099 form in 2023. Why haven’t I received an email from Stripe?

If you earned enough to need a 1099 form in 2023, you should have received an email from Stripe by mid-January 2024. Emails for pre-filing confirmation will be sent out starting Nov 1, 2023 - this is separate from the email you’ll receive when your form is filed by the platform in January.

If you can’t find an email from Stripe, it’s possible that:

- The may be in your spam/junk mail folder. Please search your inbox for an email titled: “Get your [Platform_Name] 2023 tax forms faster by enabling e-delivery”.
- [Platform_Name] does not have your most current email address on file. Please check any other email addresses you may have used to sign up for [Platform_Name], or reach out to [Platform_Name] to update your email and have an invite email sent to you.
- The email address associated with your [Platform_Name] account is incorrect, missing, or unable to receive mail.
- [Platform_Name] has chosen to postal deliver forms to you. If you haven’t received an email from Stripe or a 1099 in the mail, please reach out to [Platform_Name] to get a copy of your tax forms.

You may not have received an invitation for other reasons, such as:

- You earned less than the threshold for your form type.
- Your email address on file is incorrect, missing, or unable to receive email.
- Your specific account is unsupported on Stripe Express (in uncommon situations where multiple users are sharing the same account, or the same email address is being used on more than 20 accounts)

### Will I receive a 1099 form?

If you earned less than $600 over the course of the year, you may not receive a 1099 form and one won’t be generated for you unless you meet a threshold in your state. If your state has a filing threshold lower than $600, you might receive a 1099 form.

You can check your state’s requirements here: View 1099 state requirements.

### When will I receive my 1099?

Your 1099 tax form will be sent to you by January 31st, 2024 (note: paper forms delivered by postal delivery might take up to 10 additional business days).

- StartingNovember 1st,2023: Stripe will email you instructions on how to set up e-delivery and create a Stripe Express account. If you haven’t already, you’ll need to complete these steps to access your 1099 tax form electronically.
- Before mid January: Confirm your tax information (e.g., name, address, and SSN or EIN) is correct via Stripe Express.
- ByJanuary 31st,2024:  - Your 1099 tax form will be available to download through Stripe Express.
  - Your 1099 tax form will be mailed to you if you don’t receive an email from Stripe or don’t consent to e-delivery. Please allow up to 10 business days for postal delivery.
  - [Platform_Name] will file your 1099 tax form with the IRS and relevant state tax authorities.


- April 15,2024: IRS deadline to file taxes. You’ll need your 1099 tax form to file your taxes.

In January, we strongly suggest that you make sure all of your tax filing details and delivery preferences are up to date in Stripe Express. Your name, address, and Taxpayer Identification Number (Social Security Number /Employer Identification Number) are of primary importance.

### How do I update my tax information?

Open the email from Stripe and click on the “Get started” button, which will prompt you to create a Stripe Express account. After you create an account, you’ll be able to review your tax information (e.g., name, address, and SSN or EIN) and make any necessary changes via Stripe Express. Please update your information no later than mid January 2024.

Please note: If you don’t agree to paperless delivery by mid January 2024, we’ll automatically mail your 1099 tax form to the address on file, so it’s critical that your information is current, correct, and complete.

You may find that your 1099 tax form reports your SSN and you want to use your EIN (or vice-versa). If that’s the case, you’ll want to reach out to your platform to update your legal entity information.

Please note: If you’re operating as an individual, Sole Proprietorship, or Single Member LLC, the IRS will expect to see the individual owner’s Name and  SSN (as opposed to Business Name and EIN) reported on your 1099 tax form.

### When answering the account claim security questions, it states that my answers are incorrect, what should I do?

Please reach out to [Platform_Name] support to confirm the information that they have on file against the information you are providing.

### Why is Stripe requesting personal information like my Social Security Number?

Your SSN, EIN, or ITIN is required to file your 1099 tax form with the IRS and relevant state tax authorities.

### Is my tax information secure?

Stripe’s security tools and best practices ensure that your sensitive information is safely stored and encrypted. Learn more about the safeguards we’ve put in place to protect your information. Please make sure to keep your login credentials for Stripe Express secure.

### How can I download my 1099 tax form?

If you create a Stripe Express account and agree to paperless delivery, Stripe will email you to let you know when your 1099 tax form is available for download via Stripe Express. If you don’t agree to paperless delivery, Stripe will mail you a paper copy of your 1099 tax form instead.

### My information has changed since I signed up for [Platform_Name]. How can I edit information?

Update your account information in the Account tab:

- UnderStripe Express Account, you can update the email address and phone number used to log in to Stripe Express. Please note that only one contact method can be updated at a time.
- UnderLanguage preference, you can choose your preferred language for Stripe Express.
- UnderPayout and Professional Details, you can update personal and legal entity information and view your bank account or debit card information for payouts. To update your payout details, please reach out to your platform.

### How do I get a corrected 1099 tax form?

If you feel you need corrections made to a 1099 tax form that has already been ‘Filed’, use the edit option in the Tax Forms page of Stripe Express. Information you edit will not appear in the 1099 tax form in the Stripe Express dashboard but it is shared with [Platform_Name]. You should reach out to [Platform_Name] after you’ve made the edits you want and they can assist you with a correction. Once [Platform_Name] ‘files’ your correction, you will be notified via email and you will see a new 1099 tax form appear in the Stripe Express dashboard.

Please note that it can take up to 72 hours after the platform files the correction for you to be notified.

### How do I get in touch with Stripe for more help?

If you have a question that isn’t answered here, we recommend looking through the 1099 tax forms or Stripe Express resource pages. If you still need help, please contact Stripe support.

### How do I get into my account?

You can log in to your account by visiting connect.stripe.com/express_login, where you’ll be prompted for your email address and 6-digit phone verification code to log in. If you don’t remember the email address that you signed up with, check your inbox for past emails that we sent about confirming your tax information for paperless delivery. Otherwise, I’ll need to confirm the email address that is associated with your Stripe account. If you have historically accessed your Stripe Express account via your [insert platform portal name], you can continue to log in this way - however, you will now have to enter a 6-digit verification code that will be sent via SMS to the phone number associated with your account to log in. If you’ve lost or updated your phone number, you can select the “I no longer have access to this phone number” option to authenticate via email and change your phone number.

### How do I update my phone number? My phone number changed and I’m locked out.

If you’ve lost your phone or changed your number, you can update the number used for SMS authentication when you log in to Stripe Express.

- Go to[express.stripe.com](https://express.stripe.com)and enter the email address for your account
- On the next screen where a 6-digit verification code is requested, select the “[I no longer have access to this phone number](https://support.stripe.com/express/questions/i-lost-my-phone-or-changed-my-number-how-do-i-login-to-my-account)” option
- Follow the subsequent steps to authenticate your request and add a new phone number to the account.

### Can you resend the email?

You can use the tool on the Stripe Express support page to request a new invite email. However, before doing so, it’s possible that:

- The email may be in your spam/junk mail folder. Please search your inbox for an email from Stripe.
- Your platform does not have your most current email address on file. Please check any other email addresses you may have used with your platform, or reach out to your platform to update your email.
- The email address associated with your account is incorrect, missing, or unable to receive mail.

### I have multiple accounts with different emails. Do I have to sign up multiple times?

If all your accounts pass the 1099 reporting thresholds and your platform is using Stripe Express for e-delivery you’ll be sent invite emails for each account and you’ll need to create an account for each one. Follow the steps in the invite emails.

### Can I update my custom connect account’s bank account or card through Stripe Express?

Note: only use this if you are a platform that does allow this in Stripe Express. To update these details, click on the avatar icon in the top right corner which will bring you to your Account Page. Under Payout Details, you will see the platforms tied to your account. Once a platform is selected, you can update:

- Where to send your payouts (debit card or bank account)
- Your bank account or card detailsHead to[this help page](https://support.stripe.com/express/questions/update-bank-account-or-debit-card-for-payouts)on the Stripe Express support site for more information on troubleshooting other scenarios related to updating your payout details.

### Why do I need to provide my SSN/EIN?

The IRS requires this information to be reported correctly on your 1099 tax form. The IRS requires your Taxpayer Identification Number (TIN) on your 1099 tax form. If you are an individual, your Social Security Number (SSN) or Individual Taxpayer Identification Number (ITIN) is used as your TIN. If you are a business, your Employer Identification Number (EIN) is used as your TIN. If you have earned enough to qualify for a 1099 tax form, the IRS requires your full details to be reported on your 1099 tax form filings. The tax authorities which receive copies of your 1099 tax form will expect to see the income on your individual or business tax return. The EIN/SSN/ITIN is crucial in connecting this information, which is why the IRS requires it.

### I have claimed my account and I think the information is wrong. How do I change it?

To update your personal information on your web browser, first head to the Accounts tab at the top of the page:

- Under Stripe Express Account, you can update the email address and phone number used to log in to Stripe Express. Please note that only one contact method can be updated at a time.
- Under Language preference, you can choose your preferred language for the dashboard.
- Under Payout details, you will see the platform(s) tied to your account. Once a platform is selected, you can update your bank details associated with that platform. Please note that this is only available for some accounts using Stripe Express.
- Under Platform settings, you will see the platform(s) tied to your account. Once a platform is selected, you can update your Professional and Personal details associated with that platform. You will also be able to invite and remove people to your account.Check the[article linked here](https://support.stripe.com/express/questions/how-can-i-update-my-personal-information)to learn more.

### How do I access tax forms from previous years?

If you were eligible for a 1099 tax form in previous years and your platform used Stripe Express to deliver tax forms in those years, you can use the dropdown menu in Stripe Express to change the year and view prior years’ tax forms.

Note: Prior to 2023, the reporting threshold for 1099-K tax forms was $20,000 and 200 transactions.

## Edge cases for 1099 tax reporting

The Stripe Express Dashboard doesn’t support certain types of accounts, as follows:

- Standalone and Split forms: If a form has been split or is a standalone form (that is, not tied to the active user of a connected account), it’s not eligible for electronic delivery.
- Multi-user and multi-currency express accounts: Express accounts that have multiple users or multiple currencies associated with them can’t view the new Express Dashboard and hence do not receive electronic delivery of forms
- Multiple accounts sharing the same email: When multiple accounts for the same platform have the same email, they receive one email per account for pre-filing confirmation, up to five emails. They receive one email per account for e-delivery.
- Rejected and deleted accounts: Accounts that you’ve rejected or deleted no longer have a Stripe relationship and are ineligible to login to Stripe Express
- Pre-filing confirmation outreach from Stripe: accounts that have missing email addresses or are below the filing threshold will be excluded from Stripe outreach.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Platform support recommendations](#platform-support-recommendations)[1099 Tax Support FAQ template for connected accounts](#1099-tax-support-faq-template-for-connected-accounts)[Edge cases for 1099 tax reporting](#edge-cases-for-1099-tax-reporting)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`