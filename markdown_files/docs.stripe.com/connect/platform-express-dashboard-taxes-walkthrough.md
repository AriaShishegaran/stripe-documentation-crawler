html1099 Tax Support product walkthrough | Stripe Documentation[Skip to content](#main-content)Product walkthrough[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fplatform-express-dashboard-taxes-walkthrough)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fplatform-express-dashboard-taxes-walkthrough)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[1099 Tax Support and Communication Guide](/docs/connect/platform-express-dashboard-taxes)# 1099 Tax Support product walkthrough

Learn about how to manage 1099 Tax forms for connected accounts using Express.The images in this section describe an example of the product flow connected accounts could encounter. We provide these images to help give you and your support team an idea of the overall user experience. Feel free to reach out to Stripe support with any questions about this flow.

[The Stripe Express Dashboard](#express-dashboard)Enabling e-delivery for tax year 2023 gives your Custom or Express connected accounts access to Stripe Express Tax Forms page, a prebuilt web and mobile dashboard for managing their tax information and receiving 1099s electronically.

As you configure your tax form settings, you can also choose to have Stripe send pre-filing confirmation emails to collect tax information and paperless delivery consent directly from your connected accounts. We’ll email your eligible connected accounts starting the week of November 1st.

![Stripe Express dashboard for connected account taxes](https://b.stripecdn.com/docs-statics-srv/assets/stripe-express-tax-dashboard-2023.4fc699b9b7f560443aacd25b89d14a59.png)

The Stripe Express Dashboard where payees can grant e-delivery consent, download their 1099 tax forms, and update their tax information.

![Stripe Express dashboard for connected accounts](https://b.stripecdn.com/docs-statics-srv/assets/stripe-express-dashboard.75de9515d0222275afb3c67a4d6117c4.png)

Connected accounts can also use the Express Dashboard to view their available balance, see upcoming payouts, and track their earnings in real time.

NoteIf you don’t want to give your Custom connected accounts access to the Stripe Express Dashboard or if you don’t want Stripe to email your connected accounts, select postal delivery and disable electronic delivery in your tax form settings.

[Your connected account receives an email from Stripe](#receive-email)Your connected account receives an email from Stripe asking them to confirm their tax information and update their delivery preferences. The subject line reads ‘Get your [Platform_Name] 2023 tax forms faster by enabling e-delivery.’ The following image displays the content of the email.

![Stripe Express Tax form email from Stripe.](https://b.stripecdn.com/docs-statics-srv/assets/tax-form-confirm-information-email-2023.8868bb92bbd3f2fd5fa0e2fe319c11ab.png)

Stripe Express Tax form email from Stripe

[Connected Accounts are prompted to claim their account on Stripe Express](#verify-info)Applies to Custom connected accounts only. After your user clicks the Get Started button in Stripe’s email to connected accounts, they are taken to this screen. If they are already logged in to their Stripe Express account, they proceed to the next screen. This step is only needed if they don’t have a Stripe Express account already.

![The Stripe Express page to create an account.](https://b.stripecdn.com/docs-statics-srv/assets/tax-create-stripe-express-account.7bfe7be3830ecb6ca313cadfa256e758.png)

The Stripe Express page to create an account

[Connected account owners with existing accounts are presented with phone number verification](#two-factor)Express and Custom connected accounts who are logged in to their Stripe Express accounts, already have a Stripe Express account, or who have proceeded from the login screen, are asked for a code sent to the phone number they have on file for their account, or the one they just entered.

![Stripe Express account two-factor authentication dialog.](https://b.stripecdn.com/docs-statics-srv/assets/tax-verify-phone.a6b5b1e2455c322950902d1355324d4d.png)

The Stripe Express account phone number verification dialog.

[After passing phone number verification, connected accounts are asked to verify their identity](#verify-identity)Applies to Custom connected accounts only. After phone number verification is complete, Stripe provides the connected account with prompts to verify their identity.  These are details that should be associated with their connected account. This step is only required for Custom accounts that haven’t already onboarded to Stripe Express. If, after a few attempts, a connected account is unable to enter details that match their account, they’re prompted to check with you as the platform to confirm their details. The error message reads ‘One of the fields didn’t match the information we received from [Platform_Name]. You can try again, or check that your information with [Platform_Name] is up to date.’

![Stripe Express account Verify your identity dialog](https://b.stripecdn.com/docs-statics-srv/assets/tax-verify-identity.7f5df7551dfbb1801cdde12ed9c0dd36.png)

The Stripe Express account Verify your identity dialog.

[After verifying their identity, connected accounts are taken to the Tax forms page of Stripe Express](#tax-forms-page)After the connected account’s details are verified, they’re taken to the Tax forms page in Stripe Express where they can confirm their tax information they have on file for their account and agree to paperless delivery of their 1099 tax form.

![The Tax forms page of the Express Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/tax-forms-page.0430a010ebfa14b6c8914a90376e7a49.png)

The Tax forms page of the Express Dashboard.

They’re prompted to confirm tax information but can choose to skip temporarily if they want to leave their information as is. Your accounts could get blocked if you’ve applied 1099 capabilities and the connected account updates their value to a name and TIN combination that doesn’t match against IRS records. If the connected account is verified and then changes their name or TIN, they’re asked to re-sign a new Stripe Terms Of Service Agreement. Similarly, if Stripe is unable to complete KYC requirements on them based on the information they provided, their account payouts are blocked until they log back in to Stripe Express and correct their information.

![The dialog displayed to connected accounts to confirm their information.](https://b.stripecdn.com/docs-statics-srv/assets/tax-confirm-information.1801e85e31759f80b4e3ffd7fe974778.png)

The dialog displayed to users to confirm their information.

[Connected account owners agree to paperless delivery](#for-delivery)After the tax information is confirmed, Stripe prompts the connected account to agree to paperless delivery.

![The dialog to consent to paperless delivery of tax forms](https://b.stripecdn.com/docs-statics-srv/assets/tax-consent-edelivery.603807401bba412dd0c3bc383d5abd52.png)

The dialog to consent to paperless delivery of tax forms.

If you’ve enabled optional postal delivery, after agreeing to paperless delivery consent, your connected accounts can choose to request a paper copy in addition to the e-delivery of the tax form.

![The dialog to optionally request a paper copy of tax forms](https://b.stripecdn.com/docs-statics-srv/assets/stripe-express-tax-postal-delivery-option.9fe97c25a15822fbe4713b2c281ec96a.png)

[Your connected account receives an email from Stripe](#email-from-stripe)After filing 1099 tax forms in your Stripe dashboard, your connected account receives an email from Stripe to view their tax form electronically. The subject line reads ‘Your [Platform_Name] 1099 tax form is ready.’ The following image displays the content of the email.

![The 1099 electronic delivery email to users](https://b.stripecdn.com/docs-statics-srv/assets/tax-form-delivery-stripe-as-sender-2023-updated-threshold.408645c565172d0dc413e8a3cc1a860d.jpeg)

[Connected account owners can download their tax forms](#display-tax-forms-page)After a connected account agrees to the e-delivery terms, they can download their form when your platform makes it available.

![Stripe Express dashboard where payees can download their 1099 tax forms](https://b.stripecdn.com/docs-statics-srv/assets/stripe-express-tax-dashboard.78c8723a939c34a01e17ae807ffa31d2.png)

The dashboard where payees can download their 1099 tax forms.

Most connected account owners are prompted to enter the last four digits of the TIN on their 1099 tax form before being able to download a copy of the form. Downloads aren’t available for 24 hours after an update has been made to any personal identity information including name, address, business type, or TIN.

![The dialog to verify your SSN information to securely access tax forms.](https://b.stripecdn.com/docs-statics-srv/assets/tax-forms-secure-access.5d000d31ccbd402d50cb3a2731dce4f2.png)

CautionConnected accounts that do not agree to paperless delivery are unable to download their 1099 tax forms and resolve the call to action in their dashboard. Turn on paper delivery in your Stripe Tax form settings to make sure that recipients who don’t consent to e-delivery still receive paper forms.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[The Stripe Express Dashboard](#express-dashboard)[Your connected account receives an email from Stripe](#receive-email)[Connected Accounts are prompted to claim their account on Stripe Express](#verify-info)[Connected account owners with existing accounts are presented with phone number verification](#two-factor)[After passing phone number verification, connected accounts are asked to verify their identity](#verify-identity)[After verifying their identity, connected accounts are taken to the Tax forms page of Stripe Express](#tax-forms-page)[Connected account owners agree to paperless delivery](#for-delivery)[Your connected account receives an email from Stripe](#email-from-stripe)[Connected account owners can download their tax forms](#display-tax-forms-page)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`