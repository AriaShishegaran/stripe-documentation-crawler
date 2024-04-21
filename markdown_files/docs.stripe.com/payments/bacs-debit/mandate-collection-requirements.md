htmlRequirements for online Bacs Direct Debit mandate collection | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbacs-debit%2Fmandate-collection-requirements)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbacs-debit%2Fmandate-collection-requirements)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# Requirements for online Bacs Direct Debit mandate collection

Host your own Bacs Direct Debit mandate collection form.As a Stripe user you can host your own Bacs Direct Debit mandate collection forms, allowing you to provide a fully customized experience for your customers. There are specific requirements around both what you need to display and what you need to collect from your customers when obtaining a Bacs Direct Debit mandate from them. Use the information in this document to create your own Bacs Direct Debit collection form. Contact us.

## Information to be collected from the payer

Collect the following information from the payer:

- Bank or building society account number
- Sort code
- Account holder name
- Billing address (unless it has already been provided)
- Agreement from the payer that they’re the account holder and only person required to authorize debits from the account, and that they understand the merchant has partnered with Stripe to collect Direct Debit payments. You should collect this with a checkbox next to the following wording:`I understand that [Merchant Name] has partnered with Stripe, who collects Direct Debits on behalf of [Merchant Name] and confirm that I am the account holder and the only person required to authorize debits from this account.`

Use the following example form for a fictional company named ‘Rocket Rides’ as a reference when creating your information collection form:

![Screenshot of a payment form for the fictional company Rocket Rides with contextualized examples of the information you need to collect from the payer.](https://b.stripecdn.com/docs-statics-srv/assets/bacs-mandate-collection-example.c88809add0cd96b47eec366a89c59b35.png)

## Information to be displayed to the payer

Display the following information to the payer:

- Your postal and/or customer support email address
- Your general inquiries or customer service contact number
- Notification of the advance notice period, which is 2 working days
- The company name that will appear against the Direct Debit on the payer’s bank statement
- A hyperlink or unedited copy of[Stripe’s Direct Debit guarantee](https://stripe.com/legal/bacs-direct-debit-guarantee)
- The entered bank details so that that the payer can confirm them
- A final screen explaining that the setup of the Direct Debit Instruction is complete and that an email confirmation will follow within 3 working days

Use the following example confirmation screen for a fictional company named ‘Rocket Rides’ as a reference when creating your own form:

![Screenshot of a payment confirmation form with the payer's direct debit details.](https://b.stripecdn.com/docs-statics-srv/assets/bacs-mandate-collection-confirmation-example.4918520e67e84b054742c93925b7dff5.png)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Information to be collected from the payer](#information-to-be-collected-from-the-payer)[Information to be displayed to the payer](#information-to-be-displayed-to-the-payer)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`