htmlConfigure tax form settings | Stripe Documentation[Skip to content](#main-content)Tax form settings[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Ftax-form-settings)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Ftax-form-settings)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Configure tax form settings

Learn about the settings you can configure for the 1099 forms you send to connected accounts.Getting your 1099 FormsIf you work for a platform that pays you via Stripe and want to learn about your 1099 forms and how to get them, see 1099 tax forms on the Stripe Support site.

Use the Stripe dashboard to configure the settings for the 1099 forms you send to connected accounts. You can change almost all tax settings for forms that you haven’t filed. For example, if you initially set your tax form to report non-employee compensation (using 1099-NEC) and later determine you need to report payment transactions (using 1099-K), you can change the default form type and automatically update all forms.

If a user with the administrator role configured the tax form default settings in the onboarding flow for 1099 tax reporting, you can assign the Tax Analyst role to a team member on your account to allow that person full access to features in the Tax forms view.

## Common settings

These settings apply to all tax forms.

Default form typeSets the default type of 1099 form to use to report compensation or payment transactions. If you need to deliver multiple form types, you can[change the type of 1099 form](/connect/modify-tax-forms?method=csv#change-the-type-of-1099-form)for an account.Payer tax identityUses the platform account’s information (legal business name and tax identification number) by default. You can change your payer tax identity if, for example, you want the legal entity on the 1099 form to differ from the legal entity associated with your Stripe account.Payer addressUses the platform account’s information by default. This address displays on the 1099-NEC or 1099-MISC form as the Payer’s address and on the 1099-K form as the Filer’s address.Payer phone numberUses the platform account’s information by default. This phone number displays on tax forms as the Payer’s or Filer’s phone number.Payer state registrationsAdd corresponding state tax registration or withholding ID when it is required for the states in which you’ll file.## Delivery method settings

Configure settings for how to deliver your 1099 forms to payees. These settings apply to all 1099 form types.

Delivery strategyConfigures the default delivery strategy to use, either smart delivery settings or customize delivery settings.E-deliverySpecifies whether to e-deliver forms using the[Stripe Express Dashboard](/connect/express-dashboard). If enabled, all accounts with a viable email address receive an email when their 1099 form is available, except in[some rare situations](/connect/express-dashboard-taxes#which-accounts-get-access-to-e-delivery). If an account has given e-delivery consent, they can access their form immediately. If not, they still receive a notice email, but must claim their Stripe Express account before they can access their form.Postal deliverySpecifies whether to deliver printed copies of 1099 forms via postal mail using the platform’s US return mailing address.Postal Delivery Options

Disable Postal DeliveryConnected accounts don’t receive tax forms by postal mail.Optional Postal DeliveryStripe sends printed tax forms through postal mail to every connected account that hasn’t consented to e-delivery at the time of filing, or is ineligible to receive e-delivery. If e-delivery with the Stripe Express Dashboard is enabled, connected accounts can also request a paper copy of their tax form through the Stripe Express Dashboard.Postal deliveryAll connected accounts receive tax forms by postal mail.## 1099-K settings

Configure these settings for the 1099-K forms you send to connected accounts.

Default calculation methodConfigures the default[calculation method](/connect/calculation-methods)to use, either payments that include fees or payments that exclude fees.Filer typeSpecifies if the platform account is a payment settlement entity (PSE) or an electronic payment facilitator (EPF).Payment settlement entityAppears if the filer type is EPF. If so, you must specify the name and phone number for the PSE.Transactions reportedConfigures the type of transaction that’s processed.## 1099-MISC settings

Configure these settings for the 1099-MISC forms you send to connected accounts.

Payments boxPayment amounts are reported in the specified box on the 1099-MISC form. For example, choose3 Other incometo display the amount in box number 3. You can use CSV import to override this box for specific tax forms.Default calculation methodConfigures the default[calculation method](/connect/calculation-methods)to use. You can choose between payments that include fees, payments that exclude fees, or payouts only.## 1099-NEC settings

Configure these settings for your 1099-NEC forms.

Default calculation methodConfigures the default[calculation method](/connect/calculation-methods)to use. You can choose between payments that include fees, payments that exclude fees, or payouts only.Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Common settings](#common-settings)[Delivery method settings](#delivery-method-settings)[1099-K settings](#1099-k-settings)[1099-MISC settings](#1099-misc-settings)[1099-NEC settings](#1099-nec-settings)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`