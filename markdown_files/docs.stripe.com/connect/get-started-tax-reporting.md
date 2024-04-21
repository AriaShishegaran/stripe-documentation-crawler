htmlGet started with tax reporting | Stripe Documentation[Skip to content](#main-content)Get started with tax reporting[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fget-started-tax-reporting)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fget-started-tax-reporting)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Get started with tax reporting

Use the Stripe 1099 tax reporting product to create, modify, file, and deliver tax forms for your connected accounts.Stripe provides capabilities and a tax reporting dashboard to help platforms meet their tax reporting obligations.

Log in to your Stripe account and use the Tax forms view in the Dashboard to create, modify, file, and deliver 1099 tax forms for your connected accounts. If you use a team, only team members with the Tax Analyst or Administrator user role can access all tax-related features.

## Tax season 2023 checklist

Follow this guide to help you prepare for tax season.

Key dates- November 1st: If you’re using e-delivery, Stripe begins outreach to your connected accounts.
- January 5th:  Last recommended day to enable Stripe[outreach](/connect/platform-express-dashboard-taxes-walkthrough)to your connected accounts to automatically collect paperless delivery consent and tax information.
- January 10th: The first date you can e-file tax forms in your Stripe Dashboard.
- January 18th: Last day that Stripecouldsend pre-filing outreach to your connected accounts
- January 23rd: Latest recommended date to e-file tax forms in your Stripe Dashboard to have forms postmarked by the IRS deadline.
- January 31st: The IRS deadline to postmark 1099 tax forms to your connected accounts.
- February 15th: The last day that identity updates will automatically sync onto 1099 tax form drafts for tax year 2023.

CautionAction forms in the Needs attention state to get missing name, address, and taxpayer ID (SSN or EIN) details from your connected accounts. You need this information for filing.

[Get ready for tax season](#get-ready)- [Configure](/connect/get-started-tax-reporting#set-tax-form-default-settings)your platform’s tax settings for tax year2023. You need to do this even if you previously used the Stripe 1099 tax reporting product.
- Start reviewing[forms in the Needs attention state](/connect/identify-forms-missing-information)with missing tax information.
- Starting inAugust, you can edit tax forms[in your Dashboard](/connect/modify-tax-forms?method=dashboard)or through[CSV](/connect/modify-tax-forms?method=csv).  - Provide any[missing identity information](/connect/identify-forms-missing-information)required for filing.
  - (Optional)[Update form totals](/connect/modify-tax-forms)to reflect payment transactions outside of Stripe.
  - (Optional)[Export transaction logs](/connect/calculation-methods#export-transaction-logs)to check which Stripe transactions have contributed to a 1099 form’s total.


- If you’re planning to use e-delivery, enable both e-delivery and outreach from Stripe as delivery preferences in your[tax form settings](https://dashboard.stripe.com/settings/connect/tax_forms).

[Prepare for Stripe outreach to your connected accountsOctober 30th](#outreach)- Publish a[support article](/connect/platform-express-dashboard-taxes-faqs)explaining the tax timeline and your partnership with Stripe for taxes. View the[example article](/connect/platform-express-dashboard-taxes-faqs).
- Required for e-delivery:  - Use theMissing Email Addressfilter in your 1099 dashboard or[export tax forms](/connect/modify-tax-forms?method=csv)as a CSV to identify missing email addresses, since Column B will be blank if the email is missing.[Update email addresses](/api/accounts/update#update_account-email)with the Accounts API so we can email your connected accounts.
  - Make sure that your[Connect branding settings](https://dashboard.stripe.com/settings/connect)and your[support email address](https://dashboard.stripe.com/settings/public)are up to date.
  - Prepare your support teams for tax season2023. View the[example FAQs](/connect/platform-express-dashboard-taxes-faqs)your support team might receive from your connected accounts.


- Recommended for e-delivery:  - Notify your connected accounts when Stripe outreach occurs. View the[example email copy](/connect/platform-express-dashboard-taxes-communication#email-template:-post-stripe-email).



[Review tax form totals and identity informationDecember 31](#review-totals)- Stripe begins[outreach](/connect/platform-express-dashboard-taxes-walkthrough)to your connected accounts starting the week ofNovember 1stif you have opted into e-delivery / outreach from Stripe. We recommend opting in byJanuary 5thso we can contact all of your accounts for pre-filing confirmation byJanuary 18th, the last possible day for automated outreach from Stripe. Note, we don’t send outreach emails to platforms’ connected accounts until7 daysafter you enable the setting.
- Continue[actioning forms](/connect/identify-forms-missing-information)in`Needs attention`and reach out to accounts with missing information.
- Audit tax calculations on some 1099 tax forms.
- Verify your[tax form settings](https://dashboard.stripe.com/settings/connect/tax_forms)so you’re ready to file 1099 tax forms in January.

[Prepare, file, and deliver 1099 tax formsJanuary 23rd](#file)- Input[State Tax Registration](/connect/tax-forms-state-requirements)or withholding numbers for all states where you plan to file.
- [File tax forms](/connect/file-tax-forms)in your Stripe Dashboard no later thanJanuary 23rd. You can begin filing forms onJanuary 10th.  - When you press ‘File’ Stripe files any forms in a ‘Ready’ or ‘Ready!’ state.    - If you have forms in a ‘Needs Attention’ state and wish to file them, you need to[explicitly update the filing requirement](/connect/modify-tax-forms?method=csv#tax-form-status)for these forms before filing.




- Stripe e-delivers or postmarks tax forms for postal delivery byJanuary 31st.
- After February 15, payee identity updates (name, TIN, address) stop flowing onto the 1099 tax forms that haven’t been filed yet. This doesn’t impact forms that you already filed by February 15.

## Set tax form default settings

To configure the settings for tax forms in your account you must log in as the account owner. If you use a team, any user that has the Administrator user role for your account can configure settings. To get started with generating your tax forms for 2023, open the Tax forms page of the Dashboard, and then click Get started.

![Tax dashboard with the get started button highlighted.](https://b.stripecdn.com/docs-statics-srv/assets/tax-net-new-user-landing-experience.6ed30557253b2ce8785af2deff182a8b.png)

Choose the default tax form to generate for your connected accounts, the calculation method to use for your tax form totals, the type of filer for your business, and the kind of transactions you process. We recommend that you use a tax advisor to determine which options are right for your business. You can change almost all tax form settings at any time for the forms that you haven’t filed.

![Select a form type screen.](https://b.stripecdn.com/docs-statics-srv/assets/tax-form-settings-step.9fdf3acbf457f95499c2bdaa81ce7c2c.png)

Select a form type

![Tax calculation screen.](https://b.stripecdn.com/docs-statics-srv/assets/tax-form-settings-step1.a54d8be2498440b91e4229e8426424a6.png)

Select tax calculation

![Type of filer screen](https://b.stripecdn.com/docs-statics-srv/assets/tax-form-settings-step2.dd51a20dca664351848d6b48572ef368.png)

Select type of filer

![Transaction screen.](https://b.stripecdn.com/docs-statics-srv/assets/tax-form-settings-step3.5c7890ebc89925cd89092b3fc3c0db9c.png)

Select types of transactions processed

Next, confirm the business information that displays as the Payer details on all of your tax forms. Make any necessary changes, then click Continue.

![Business information screen.](https://b.stripecdn.com/docs-statics-srv/assets/tax-business-info-step.56acf3720225276598592dffe50c9f34.png)

Next, add state registration or withholding IDs for the states you plan to file with. You can enter these at any time in the future through tax form settings.

![State filing screen.](https://b.stripecdn.com/docs-statics-srv/assets/tax-state-filing-step.200b96a91d14dd22795110ac6865399e.png)

The next step involves choosing your delivery preferences to meet IRS obligations around delivering 1099 forms to payees. We offer two forms of delivery:

- E-delivery through the Stripe Express Dashboard: Owners of eligible connected accounts receive an electronic copy of the 1099 form through the Stripe Express App. Stripe sends an email invite to the connected account owners to confirm their tax details, collect their consent, and provide access to the electronic copy of the form. Read more about how e-delivery works.


- Paper delivery through postal mail: Stripe delivers the 1099 forms to the owners of eligible connected accounts through postal mail based on the address on the tax form. If e-delivery is enabled, but the connected account hasn’t provided e-delivery consent at the time of filing, we fall back on postal delivery to meet IRS obligations.



![Delivery method selection screen.](https://b.stripecdn.com/docs-statics-srv/assets/tax-delivery-preferences-step.72319e394a4f5216a0e18ad0dfbf076c.png)

As a final step, you can view a summary of your tax form settings to confirm your choices. After you confirm your settings, the tax forms dashboard opens, where you can view all of your tax forms for 2023.

![Summary screen.](https://b.stripecdn.com/docs-statics-srv/assets/tax-summary-step.5bdede405d7cfef3c01442f44794bd0a.png)

## View and filter tax forms

You can view all of the tax forms for your connected account using the Tax forms dashboard. Click the appropriate tab to filter the forms displayed. To display the State filing status, Federal filing status, or Delivery filing status instead of Overall filing status, click the gear icon to the right of the column heading and select the status to display.

![Tax reporting page of the Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/tax_reporting_dashboard_new.c5898c0728da3cc9b274a72c2dd13229.png)

You can apply any of the existing filters to limit the results to only those records that match the filter criteria. For example, to display only records for a specific payee, choose the Payee name filter and then enter all or part of a name to match. The records displayed include only the records for payees with Payee names that match the string you used for the filter.

You can use the following filters to display tax forms:

Filter nameFilter valuesTypeType of tax form: 1099-K, 1099-MISC, or 1099-NECOverall filing statusOverall status of tax form: Will not file, Needs attention, Ready, Filing, Accepted, or RejectedFederal filing statusStatus of the Federal tax form: Will not file, Needs attention, Ready, Filing, Accepted, or RejectedState filing statusStatus of the State tax form: Will not file, Needs attention, Ready, Filing, Accepted, or RejectedDelivery statusDelivery status of the tax form: Will not deliver, Needs attention, Ready, Scheduled, Delivering, Delivered, FailedPostal delivery statusPostal delivery status of the tax form: Will not deliver, Needs attention, Ready, Scheduled, Delivering, Delivered, FailedElectronic delivery statusElectronic delivery status of the tax form: Will not deliver, Needs attention, Ready, Scheduled, Delivering, Delivered, FailedPre-filing confirmation statusStatus of Stripe’s pre-filing outreach: Not eligible, Queued, SentStripe merchant IDTax forms for the specified merchant IDForms grouped withTax forms grouped with the specified tax form IDPayee nameTax forms for the payeePayee stateTax forms for the payee’s stateNeeds attentionNeeds attention status: Any reason, Address, Business name, TIN - Any reason, TIN - Missing, TIN - MismatchYTD volumeTax forms with the specified year-to-date volumeCorrectionCorrection status: Correction, OriginalThresholdState or federal threshold status: Meets federal threshold, Meets state threshold, Meets any threshold, Meets state and federal threshold, Meets neither state nor federal thresholdsEmail addressTax forms with the specified email addressMissing email addressFilter for tax forms that either have or don’t have email addresses: True, FalseDelta valuesFilter for tax forms with delta values: With delta values, Without delta valuesStandalone formsFilter for standalone tax forms: All standalone forms, No standalone formsE-delivery consentStatus of e-delivery consent collection: Provided, Not provided, RevokedGrouped TINTax forms that have grouped TINs: Grouped forms only, No grouped forms## Understand tax form status

Stripe automatically calculates the overall status for each tax form, and allows you to apply filing requirements for each form as appropriate. The filing requirement appears as a visual indicator in the tax form status. You can view the status for both State and Federal tax forms.

StatusDescriptionNext stepsAcceptedThe IRS or state accepted the tax form.No further action required.FilingThe tax form has been queued for transmission to the IRS or state, and will be sent shortly.No further action required.FiledThe tax form was sent to the IRS or state, but hasn’t been accepted yet.No further action required.ExportedThe tax form was included in a state filing export, which you can find on the[bulk jobs listing](https://dashboard.stripe.com/connect/taxes/forms/?showJobs=true).You must download the export and manually submit these to the appropriate state reporting agency.Needs attentionThe tax form is above the IRS or state threshold, but requires additional information before filing.Most tax forms require additional information before filing. You can[update the form](/connect/modify-tax-forms)or update the connected account. If you determine that you shouldn’t file the tax form, or you want to file with incomplete information, you can[update the filing requirement](/connect/modify-tax-forms).ReadyThe tax form is above the IRS or state threshold and ready to file.File most tax forms. If you determine that you shouldn’t file the tax form, you can[update the filing requirement](/connect/modify-tax-forms).RejectedThe IRS or state rejected the tax form.Review the IRS[information return penalties](https://www.irs.gov/government-entities/federal-state-local-governments/increase-in-information-return-penalties), and your connected accounts’ tax forms for incorrect names or tax identification numbers. You have 60 days from the initial submission to file corrected tax forms to the IRS. Learn more about[handling rejections](/connect/correct-tax-forms#correction-reasons).Will not fileThe tax form is below the IRS or state threshold, or was overridden and won’t be filed.Most tax forms don’t require further action. If you determine that you should file the tax form, (for example, if the connected account has withholding data), you can[update the form](/connect/modify-tax-forms).## Understand tax form TIN status

Platforms need valid TINs on the tax forms to ensure that the IRS and/or state accepts the forms, and Stripe displays the status of the TIN in the Tax Form Editor as follows:

StatusDescriptionNext stepsVerifiedName & TIN are verifiedNo further action required.MismatchName + TIN didn’t match the records in IRS and need to be resolved before filingFollow up with the account to get a name + TIN that matches IRS records. If you still want to file the form in this state, change the[Filing requirement](/connect/modify-tax-forms?method=csv#tax-form-status)toRequired even if incomplete.OverwrittenPlatform has overwritten the Name and/or TINVerify the name + TIN directly with the IRS and/or use a third party TIN verification tool. You can still file this form in this status.ProvidedName and TIN were inherited from Connect Settings, but Stripe didn’t verify.Verify the name + TIN directly with the IRS and/or use a third party TIN verification tool. You can still file this form in this status.MissingName or TIN not provided and needs to be resolved before filingFollow up with the account to get a name + TIN that matches IRS records. If you still want to file the form in this state, change the Filing requirement toRequired even if incomplete.## Understand tax form delivery status

Stripe sends your tax forms using the delivery method you set for your account, either mail or e-delivery. The Tax forms page shows the delivery status for your tax forms. The following table describes each possible delivery status.

StatusDescriptionNext stepsDeliveredThe forms were successfully delivered.No further action required.DeliveringThe forms were sent, but haven’t been received.No further action required.FailedThe forms were not successfully delivered.No further action required.Needs attentionThe forms are ready to send, but require additional information.Most tax forms require additional information before delivering. You can update the form or update the user information for the connected account.ReadyThese forms are sent when the forms are filed.No further action required.ScheduledThe forms are scheduled for delivery.No further action required.Will not deliverThe forms won’t be delivered.No further action required.## Updating tax forms

You can Update 1099 tax forms for the current year and choose whether or not to include tax identification numbers (TIN).

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Tax season  checklist](#tax-season-checklist)[Get ready for tax season](#get-ready)[Prepare for Stripe outreach to your connected accounts](#outreach)[Review tax form totals and identity information](#review-totals)[Prepare, file, and deliver 1099 tax forms](#file)[Set tax form default settings](#set-tax-form-default-settings)[View and filter tax forms](#view-and-filter-tax-forms)[Understand tax form status](#understand-tax-form-status)[Understand tax form TIN status](#understand-tax-form-tin-status)[Understand tax form delivery status](#understand-tax-form-delivery-status)[Updating tax forms](#updating-tax-forms)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`