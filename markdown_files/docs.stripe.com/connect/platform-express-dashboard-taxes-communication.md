html1099 Tax Support proposed communication guidelines | Stripe Documentation[Skip to content](#main-content)Communication timeline[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fplatform-express-dashboard-taxes-communication)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fplatform-express-dashboard-taxes-communication)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[1099 Tax Support and Communication Guide](/docs/connect/platform-express-dashboard-taxes)# 1099 Tax Support proposed communication guidelines

Review a proposed communication timeline for communicating with your connected accounts about 1099 Tax forms.## For platforms using e-delivery with Stripe Express to issue tax forms

We recommend sending a reminder (example below) to connected accounts once they’ve received their pre-filing confirmation from Stripe. Preparing your connected accounts for outreach from Stripe helps to make a smoother user experience during tax season. We’ll send you a heads up email once we start sending pre-filing confirmation emails to your connected accounts.

Who sends?Email to connected accountsDateStripeGet your [Platform_Name]2023tax forms faster by enabling e-deliveryStarting the week ofNovember 1st,2023PlatformEmail template: Post-Stripe emailAny time after Stripe has sent the initial pre-filing confirmation email and before filing your 1099s.StripeYour [Platform_Name] 1099 tax form is readyWhen your platform files in the Stripe Dashboard (must be beforeJanuary 23rd,2024)## Stripe email to connected accounts: Get your [Platform_Name] 2023 tax forms faster by enabling e-delivery

Stripe will send a version of these communications starting the week of November 1st, 2023.

![An example Stripe email to review draft 1099 tax form settings](https://b.stripecdn.com/docs-statics-srv/assets/tax-form-confirm-information-email-2023.8868bb92bbd3f2fd5fa0e2fe319c11ab.png)

An example email from Stripe to a connected accounts to review draft 1099 tax forms.

## Email template: Post-Stripe email

We recommend letting your connected accounts know that they should’ve received information about their 1099 tax forms from Stripe. This is a proposed email template you can customize for your platform.

Reply-to: [Platform’s preferred email]

Subject: Confirm your tax information with Stripe

Pre-header: Please verify your tax information is up to date

Email Copy:

[Platform_Name] partners with Stripe to file 1099 tax forms that report your earnings or sales activity. You should have received an email from Stripe (express@stripe.com) with instructions about how to confirm your tax information and delivery preference to ensure your 1099 tax form is sent to the right place.

Please confirm your information using the link provided in the email from Stripe. You’ll need to create a Stripe Express account and confirm your information is up-to-date to receive your 1099 form for the 2023 tax year. You will be asked a series of security questions to verify your identity.

If you have any questions, visit https://support.stripe.com/express.

What is a 1099 form? A 1099-NEC/1099-MISC form summarizes your earnings as an independent contractor or service provider. It’s provided to you and the IRS, as well as some US states, if you earned $600 or more in 2023.

The 1099-K form summarizes the sales activity of your account. It will be provided to you and the IRS, as well as some US states, if you processed more than $20,000 and had more than 200 transactions in 2023.

Why do I need to verify my information? We want to ensure that information like your name, address, and Taxpayer Identification Number are up to date so that your 1099 tax form is accurate and sent to the right place.

I didn’t receive an email from Stripe—what should I do? Please double check your spam or junk mail folder for an email with the subject line “Get your [Platform_Name] 2023 tax forms faster by enabling e-delivery.” If you haven’t received this email from Stripe, please reach out to [Platform email].

When and where can I expect my 1099 tax form? 1099 tax forms are typically finalized in January. If you meet the income thresholds above, Stripe will send you a link to access your 1099 tax form (or mail a paper form if you prefer).

## Stripe email to connected accounts: Your [Platform_Name] 1099 tax form is ready

Stripe sends a version of this email to your connected accounts after you file your tax forms in the Connect Dashboard.

![An example email from Stripe to a Rocket Rides connected account to view 1099 tax form.](https://b.stripecdn.com/docs-statics-srv/assets/tax-form-delivery-stripe-as-sender-2023.8fad13a7b8e7ff7adecd279791fcf47d.png)

An example email from Stripe to a connected account to view their 1099 tax form. The copy changes slightly if the platform issues a 1099-MISC or 1099-NEC.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[For platforms using e-delivery with Stripe Express to issue tax forms](#for-platforms-using-e-delivery-with-stripe-express-to-issue-tax-forms)[Stripe email to connected accounts: Get your [Platform_Name]  tax forms faster by enabling e-delivery](#stripe-email-to-connected-accounts:-get-your-[platform_name]-tax-forms-faster-by-enabling-e-delivery)[Email template: Post-Stripe email](#email-template:-post-stripe-email)[Stripe email to connected accounts: Your [Platform_Name] 1099 tax form is ready](#stripe-email-to-connected-accounts:-your-[platform_name]-1099-tax-form-is-ready)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`