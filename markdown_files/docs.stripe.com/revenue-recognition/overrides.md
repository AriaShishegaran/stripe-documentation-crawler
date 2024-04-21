htmlRevenue Recognition transaction overrides | Stripe Documentation[Skip to content](#main-content)Overrides[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Foverrides)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Foverrides)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)
[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Reporting](/docs/stripe-reports)[Revenue recognition](/docs/revenue-recognition)# Revenue Recognition transaction overrides

Learn how to make manual corrections to your Revenue Recognition reports.WarningStripe will soon deprecate the transaction override feature. Use the data import feature instead.

It’s possible for the information on a transaction to become inaccurate for revenue recognition purposes. This can happen for a number of reasons, such as human error or evolving terms of a sale. The transaction override feature allows you to make corrections, regardless of when you created the transaction.

## Creating a transaction override

You can find the transaction overrides section at the bottom of the Revenue Recognition page.

![Add transaction override modal](https://b.stripecdn.com/docs-statics-srv/assets/transaction-override-add-modal.8d198b30d4dc9c1a53fa374d4d647550.png)

[Enter ID of the transaction model to override](#model)To get started, enter the id of the transaction to override. Stripe supports overrides on the following transaction models:

Transaction modelRestrictions[Invoices](/api/invoices)To override line-item-level details, use the[data import feature](/revenue-recognition/data-import).[Charges](/api/charges)You can’t override charges that are[associated with an invoice](/api/charges/object#charge_object-invoice). Instead, override the invoice itself.You can find the id of a transaction in the Dashboard or using the API. If the transaction occurred in a previous month, you can also find it in the following report downloads when formatted by invoice:

- Invoice Statement
- Debits and credits
- Corrections

[Choose the override type](#override)The following override types are available:

Override TypeDescriptionRecognition period start and end datesThe start date and end dates correspond to when the service started and ended. The revenue of this transaction is recognized within this period. Start and end dates can have the same value, in which case revenue is recognized all at once.Read more about[how transaction overrides work](/revenue-recognition/overrides#how-transaction-overrides-work)below.Transaction exclusionExcluding a transaction removes all records of it from revenue recognition. This only works for invoices that are either[voided](/invoicing/overview#void)or[manually marked as paid](/invoicing/overview#paid), and have no customer balance applied to them.## How transaction overrides work

You can create transaction overrides for transactions that occurred in both past accounting periods and in the current accounting period. If the transaction occurred in a past accounting period, corrections are implemented prospectively at the end of the current accounting period. You can view these corrections in the reports for the current period after it closes.

If the overridden transaction occurred in the current accounting period, it’s not reflected as a correction in the current period. Instead, it’s recognized using the new attributes from the override.

Creating a transaction override doesn’t alter the attributes of the transaction model being overridden.

You can make changes to a transaction override by deleting the override and creating a new one. If you delete an override that impacts transactions in closed accounting periods, the first open accounting period will reflect the effect of the deletion. If the deleted override impacts transactions in open accounting periods, the effect applies directly to those accounting periods.

NoteIf you have any feedback on how we can improve transaction overrides to better suit your accounting needs, visit https://support.stripe.com/.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Creating a transaction override](#creating-a-transaction-override)[Enter ID of the transaction model to override](#model)[Choose the override type](#override)[How transaction overrides work](#how-transaction-overrides-work)Products Used[Revenue Recognition](/billing/revenue-recognition)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`