htmlAutomatic invoice advancement | Stripe Documentation[Skip to content](#main-content)Automatic invoice advancement[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fintegration%2Fautomatic-advancement-collection)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/invoicing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fintegration%2Fautomatic-advancement-collection)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Invoicing](/docs/invoicing)[Integrate with the API](/docs/invoicing/integration)# Automatic invoice advancement

Learn how Stripe Invoicing handles automatic advancement and collection.Unless you explicitly disable it, invoices you create in the Dashboard ​automatically finalize when they leave the draft state. Invoices you create with the API, however, ​​won’t automatically finalize. You must turn on automatic collection by setting the auto_advance property on the invoice to true. You must also configure a webhook endpoint to receive their associated events. When you turn auto_advance to false, you’re responsible for transitioning the invoice between statuses. To learn more, see Webhooks and finalizing invoices.

NoteWhen you turn on automatic collection, Stripe does everything to drive the invoice towards payment—including automatically finalizing draft invoices after one hour. During this wait period, the invoice shows a Scheduled status.

## Update automatic advancement

You can toggle the auto_advance property on draft and open invoices. Automatic advancement and collection ​​never occur on invoices that are marked uncollectible, void, or paid. For these invoices, auto_advance is always set to false:

Command Line[curl](#)`curl https://api.stripe.com/v1/invoices/id \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d auto_advance=false`## Pause automatic advancement

In some cases, you might want to stop Stripe from automatically advancing your invoices toward collection. For example, if you want to:

- Use your own business logic to manage the lifecycle of an invoice.
- ​Decide if and when to send invoice emails on a per-invoice basis.

​​In both of these cases, use the auto_advance property to disable the automatic advancement and collection behavior.

## Automatic advancement feature comparison

When you set auto_advance to false, Stripe disables most of the automatic features for Invoicing—leaving collection up to you. The following table outlines some key changes in the behavior of automatic collection, depending on whether auto_advance is set to true or false:

FeatureTrueFalseFinalize drafts to open(after[approximately 1-hour](/billing/subscriptions/overview#subscription-lifecycle))Emailing invoicesAttempting paymentsRetries (email and charge)Invoice reminder emails3D Secure reminder emailsEmail receiptsLegend![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- = Can be enabled depending on your settings.
- = Configurable in your settings.
- = Not enabled. The invoice isn’t automatically transitioned.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Update automatic advancement](#update-auto)[Pause automatic advancement](#pausing-auto-collection)[Automatic advancement feature comparison](#toggle-auto-advance)Products Used[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`