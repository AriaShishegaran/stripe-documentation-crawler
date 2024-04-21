htmlAutomatic collection | Stripe Documentation[Skip to content](#main-content)Automatic collection[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fautomatic-collection)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/invoicing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fautomatic-collection)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Invoicing](/docs/invoicing)[Automated collections](/docs/invoicing/automated-collections)# Automatic collection

Learn about Stripe's automatic recovery features for Invoicing.Stripe provides a number of automated revenue recovery features for one-off invoices to help collect payments that might have failed otherwise. These include automatically updating your users’ saved cards, sending emails when a failed payment occurs, and retrying cards at strategic times.

## Smart Retries

### Bank debit methods

To avoid bank fees, Stripe ​doesn’t retry invoice payments that customers made with bank debit methods including: BECS direct debit, Bacs direct debit, or SEPA direct debit.

Using machine learning, Smart Retries chooses the best times to retry failed payment attempts to increase the chance of successfully paying an invoice. The machine learning system behind Smart Retries uses time-dependent, dynamic signals, such as:

- The number of different devices that have presented a given payment method in the lastNhours.
- The best time to pay (payments made for debit cards in certain countries might be slightly more successful at 12:01 AM in local time zones).

Based on a combination of these factors, Stripe intelligently assesses when to retry payments. We continuously learn from new purchaser behaviors and transactions, which provide for a more targeted approach over traditional rules-based payment retry logic. Any invoice with the auto_advance attribute set to true goes through the Smart Retries flow (if enabled), regardless of the selected payment method.



Smart Retries reattempts the charge according to your specifications for the number of retries and the maximum duration. You can also use Recovery automations to create different retry policies for different customer segments.

You can override this behavior by disabling Smart Retries and defining your own custom retry rules. When you enable dunning, the next_payment_attempt attribute on the invoice.payment_failed webhook indicates when Stripe attempts the next collection.

## Failed payment notifications

In your Subscriptions and emails settings, go to Manage failed payments for subscriptions. The setting Send emails when card payments fail turns on automatic customer emails for failed payments.

If a payment failure occurs on a one-off invoice and Link to a Stripe-hosted page is selected, Stripe sends a link to the Hosted Invoice Page to the customer.

You can customize the color, icon, and logo of your customer emails and Stripe-hosted page in the Branding settings.

### Customize the email message  Beta

For failed payment emails, you can write your own email message to your customers instead of using the default email message. You’ll also need to use a verified custom domain to send emails from.

1. Click the customize link in the sentence below the Send emails to customers to update failed card payment methods option.


2. Choose the Use your own custom email option.


3. Read the email policy guidelines. By law, you can’t add promotional content without explicit consent from the customer.


4. Fill out the contents of the email. As you enter information, you can see a preview of the email.



Interested in joining the beta for customizing failed payment emails?Use the form below to request early access to customizable failed payment emails.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.## Manage invoices sent to customers

In your Subscriptions and emails settings, go to Manage invoices sent to customers to:

- Email finalized invoices to customers—You can turn this option on to always email your customers a finalized invoice. This setting only affects invoices where the[collection_method](/api/invoices/object#invoice_object-collection_method)is set to`send_invoice`.
- Change a past due invoice’s status—You can mark an invoice as uncollectible if it’s past due by 30, 60, or 90 days. You can also leave the invoice past-due.
- Automatically reconcile partial payments that meet a minimum—You can instruct Stripe to mark an invoice as paid if ​​it’s partially paid within the set amount. For example, if the payment received from your customer is within 20 USD or less of the total (or at whatever amount you configure), then this setting applies a credit to the invoice for the outstanding amount. It then marks the invoice as paid.

### Automatic reminders for one-off invoices

To turn on automatic reminders for unpaid, one-off invoices go to Send reminders under Manage advanced invoicing features. When the feature is on, select  whether you want Stripe to send the reminder before, when, or after the invoice is due.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Smart Retries](#smart-retries)[Failed payment notifications](#failed-payment-notifications)[Manage invoices sent to customers](#manage-invoices-sent-customers)Products Used[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`