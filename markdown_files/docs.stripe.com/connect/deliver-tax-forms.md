htmlDeliver your 1099 tax forms | Stripe Documentation[Skip to content](#main-content)Deliver tax forms[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fdeliver-tax-forms)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fdeliver-tax-forms)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Deliver your 1099 tax forms

Learn about 1099 form delivery requirements and how to deliver your tax forms, including e-delivery and postal delivery.Getting your 1099 FormsIf you work for a platform that pays you via Stripe and want to learn about your 1099 forms and how to get them, see 1099 tax forms on the Stripe Support site.

Revenue authorities (such as the IRS) typically require that you deliver a copy of the tax form to the payee, in addition to filing the tax form. Per IRS recommendations, the tax form you deliver is a “Copy B” with the payee taxpayer identification number (TIN) redacted to the last four digits.

The IRS requires you to provide tax forms to payees using postal mail unless you’ve obtained consent from the payee to only deliver the forms electronically. If you don’t obtain consent for e-delivery, you can still e-deliver as long as you also mail the copy of the tax form to the payee. For more information, see the IRS Requirements for Furnishing Information Returns Electronically.

You must deliver tax forms by the first business day on or after January 31st. For postal delivery, tax forms must be postmarked by this date.

Tax forms are always delivered to payees the first time they’re filed with a revenue authority. This includes e-filing with the IRS as well as states. If a tax form is both e-filed with the IRS and to a state, it’s only delivered on the first of these events.

## Delivery options

There are three options for delivering tax forms:

- E-delivery with the Stripe Express Dashboard:Use the Stripe Express Dashboard to collect e-delivery consent and deliver tax forms.
- E-delivery with Tax Forms APIBeta: Use the Tax Forms API to directly control and manage the entire e-delivery flow.
- Postal delivery:Use Stripe to send tax forms using postal delivery.

## E-delivery with the Stripe Express Dashboard

Your connected accounts are eligible to access their e-delivered tax forms through the Express Dashboard if your connected accounts already have access to the Express Dashboard or if you own the full onboarding and management experience for your connected accounts. Even if your platform is eligible, some of your connected accounts might not be eligible. Connected accounts that aren’t eligible for hosted e-delivery include:

- Multi-user accounts
- Vendors without a stripe account
- Users who have multiple accounts on your platform with the same email addressTo view a full list of the types of connected accounts that aren’t eligible for e-delivery through the Express Dashboard, see[Which accounts get access to e-delivery](/connect/express-dashboard-taxes#which-accounts-get-access-to-e-delivery).

Connected account users must provide e-delivery consent to view and download their forms online. The e-delivery consent is applicable to all future electronic deliveries. Enable postal delivery to make sure that eligible accounts receive their tax forms. Consult your tax advisors if you want to completely opt out of paper delivery.

### Prerequisites for using tax form e-delivery

Ensure that the email address is available and current for the connected accounts on your platform where you own the user experience. You can confirm that an email address for an account is available. Use the following command to view the email address for a connected account:

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  --data-urlencode email="jennyrosen@gmail.com"`### Turn on the e-delivery experience

To turn on e-delivery for your account, open the Tax forms settings page in the Dashboard, then choose Optimize for e-delivery in the Delivery settings section.

Additionally, you can select the Have Stripe collect tax information automatically option to have Stripe email your connected accounts and ask them to update their tax information and delivery preferences. Learn more about e-delivery for connected accounts.

### File and deliver 1099 forms

The Express Dashboard is where eligible Connect platforms deliver 1099s to their users. Toward the end of January, when you click file and deliver, your finalized tax forms are automatically sent out to your connected accounts. They’ll receive another email letting them know their tax forms are ready and get a link to download the forms directly from the Tax forms tab in the Express App. If a connected account user later consents to e-delivery, it applies only to future years because paper forms were already sent.

![Connect tac forms page showing forms that are ready to download.](https://b.stripecdn.com/docs-statics-srv/assets/connect-tax-form-ready-download.45cd97db253255d3fd8878606e74050c.png)

## E-delivery with Tax Forms API

BetaThe Tax Forms API is available in limited beta. To request access to the beta, reach out to your account team or contact Stripe for more information. Access is not guaranteed. At this time, we are unable to support additional beta requests for tax year 2023.

You can use the Tax Forms API to deliver forms to your users directly. With the API, you build and brand the e-delivery flow in your platform and Stripe doesn’t interact with your users directly. You also need to manage the collection of e-delivery consent, how your users access the e-delivered forms, and any user identity changes or corrections that go through your platform.

We’ll use a fictitious account StripeDelivers, a delivery platform to walk through the API experience.

### Getting started

Stripe recommends disabling e-delivery and outreach from Stripe — otherwise your users will also have their e-delivered forms accessible through the Stripe Express Dashboard.

### Collect paperless delivery consent

Per IRS requirements, a StripeDelivers account holder who wants to receive tax correspondence electronically instead of by mail must opt out of receiving postal mail. When an account holder provides or revokes consent, the app sends a POST request to update the connected account’s tax form settings. If an account holder provides consent, Stripe doesn’t mail a copy of their 1099-K form unless you require postal mailing for all accounts in your delivery settings.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "settings[tax_forms][consented_to_paperless_delivery]"=true`### Retrieving tax forms

StripeDelivers wants to create a view of a connected account’s filed 1099-K tax forms in their platform’s app, to satisfy the platform’s IRS tax reporting requirement and inform the account holder of their taxable income.

The developer needs to upload each 1099-K to the platform’s servers to make them available to the view. The app sends a GET request for a list of tax forms from Stripe’s Tax Forms API on each user request.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/tax/forms \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Version: 2024-04-10; retrieve_tax_forms_beta=v1;" \
  -d type=us_1099_k \
  -d "payee[account]"={{CONNECTED_ACCOUNT_ID}}`When a user requests a PDF version of the form, the app sends a GET request to Stripe’s Files API, caches it, and returns it in the response.

Command Line[curl](#)`curl https://files.stripe.com/v1/tax/forms/taxform_123/pdf \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -H "Stripe-Version: 2022-11-15; retrieve_tax_forms_beta=v1;" \
  -o "/tmp/tmp.pdf"`### Notifications

NoteTo receive tax.form.updated webhooks, you need to create a webhook endpoint with the Tax Forms API beta Stripe-Version header.

StripeDelivers wants to notify an account by email when a form is accepted by the IRS. When StripeDelivers receives a tax.form.updated webhook and determines that the form has moved to accepted, it sends an email to the user with a download link.

## Postal delivery

If you want to mail your tax forms, you must file by January 23rd, 2024 to guarantee the tax forms are postmarked by January 31st, 2024. You must also provide a valid US return address to comply with USPS guidelines.

You can use postal delivery for any deliverable address, including PO boxes. For compliance reasons, Stripe doesn’t allow you to set a PO box as the address for a connected account; however, you can use Tax form editor or CSV import to modify the address on the tax form.

You may have connected accounts that are only eligible for state filing and not with the IRS. When you use Stripe to file your forms with the IRS and states, Forms 1099 for the state are mailed to these connected accounts after you finish filing.

If you use CSV import to override the default delivery method, this also affects the state mailing. For example, if you set postal_delivery to false, Stripe doesn’t mail the 1099 form to the connected account for state reporting.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Delivery options](#delivery-options)[E-delivery with the Stripe Express Dashboard](#e-delivery-with-stripe-express)[E-delivery with Tax Forms API](#edelivery-api)[Postal delivery](#postal-delivery)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`