htmlAutomate customer emails | Stripe Documentation[Skip to content](#main-content)Automate customer emails[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Frevenue-recovery%2Fcustomer-emails)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Frevenue-recovery%2Fcustomer-emails)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Revenue recovery](/docs/billing/revenue-recovery)# Automate customer emails

Learn how you can use customer emails to recover revenue.Customer emails help prevent involuntary churn by notifying customers and giving them a chance to intervene when churn is likely, like when a payment fails.

Enable email notifications for all the use cases that make sense for your business. We recommend you minimally provide a way for customers to:

- [Confirm payments](#payment-confirmation-notifications)
- [Correct failed payments](#failed-payment-notifications)

## Configure emails

You can turn on customer emails in your subscriptions and emails settings Dashboard without writing any code. All of these emails and hosted pages use your branding settings.

Emails for the following notification types include a link to a page where the customer can update their payment method.

- Payment confirmation notifications
- Failed payment notifications
- Trial ending reminders
- Renewal reminders
- Expiring card notifications

You can set the link destination to your own custom link or a Stripe-hosted page. If you Use your own custom link and don’t provide a URL, we use your business website.

## Failed payment notifications

Notify your customers about failed payments for subscriptions to encourage them to resolve the reason for failure, such as an expired card. Enable Send emails when card payments fail in the revenue recovery settings page.

When you enable this setting, Stripe automatically sends an email to your customer after each failed payment. The email lets your customer know that their recent subscription payment failed and gives them the opportunity to update their payment method so it can be retried successfully.

### Customize the email message  Beta

For failed payment emails, you can write your own email message to your customers instead of using the default email message. You’ll also need to use a verified custom domain to send emails from.

1. Click the customize link in the sentence below the Send emails to customers to update failed card payment methods option.


2. Choose the Use your own custom email option.


3. Read the email policy guidelines. By law, you can’t add promotional content without explicit consent from the customer.


4. Fill out the contents of the email. As you enter information, you can see a preview of the email.



Interested in joining the beta for customizing failed payment emails?Use the form below to request early access to customizable failed payment emails.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.## Unpaid recurring invoice reminders

To send reminder emails about unpaid invoices, enable Send reminders if a recurring invoice hasn’t been paid in the billing settings page, in the Manage invoices sent to customers section.

This sends payment reminders for recurring invoices with a collection method of send_invoice on the configured schedule.

## Trial ending reminders

Under Manage free trial messaging, turn on Send a reminder email 7 days before a free trial ends to send a trial ending reminder.

When the trial ends without a payment method and the subscription is paused, customers can activate the subscription on the hosted page. They can add a payment method to activate the subscription and pay the first invoice.

## Renewal reminders

Under Prevent failed payments, turn on Send emails about upcoming renewals.

Stripe sends this email before the current renewal period ends based on the days configured in the Upcoming renewal events section.

The renewal date in the email uses the customer’s timezone. If the customer’s timezone isn’t defined, it uses the timezone set in your account settings. Otherwise, it defaults to UTC.

## Payment confirmation notifications

Some payments might require manual customer intervention, like those that use 3D Secure or the Boleto payment method. You can manage payments that require confirmation in the Dashboard.

1. To automatically send an email to your customer when their payment requires confirmation, enableSend a Stripe-hosted link for customers to confirm their payments when required. The email includes a link to a Stripe-hosted page where your customer can confirm the payment.
2. To continue sending emails until your customer confirms the payment or it expires, enableSend reminders if payment confirmation isn’t completed.  You can customize the intervals at which Stripe sends these reminders. Each reminder includes a link similar to the original email where the customer can confirm the payment.

## Expiring card notifications

Under Prevent failed payments, turn on Send emails about expiring cards.

This automatically sends an email 1 month before your customer’s card on file expires.

## Link to a Stripe-hosted page

With the Link to a Stripe-hosted page option, Stripe provides a secure, private URL to a Stripe-hosted page in the email. Stripe doesn’t include a link to the Stripe-hosted page if the subscription is set to manually send an invoice.

On that page, your customer can update their payment method for the relevant subscription and pay any outstanding invoices if applicable.

How a customer updates their payment method on the Stripe-hosted page.

Any of the following conditions invalidate the link to the hosted payment page:

- It’s been 30 days since we sent the trial ending email.
- The[subscription status](/billing/subscriptions/overview#subscription-statuses)changes to`cancelled`,`incomplete_expired`, or`unpaid`.
- The trial ended and the customer already provided a payment method for the subscription.
- The subscription’s current renewal period expired.

## Test your configuration

In test mode, Stripe doesn’t automatically send customer emails. To test your customer email settings, use email addresses that belong to your verified email domain or an active team member. If a test mode customer’s email matches either of those conditions, Stripe sends failed payment notifications, upcoming invoice reminders, trial ending reminders, and card expiring reminders in test mode.

## Email logs

You can find logs for emails sent within the last 30 days on the customer page. The logs are updated daily, so they don’t include emails from the current date.

We log the following types of email notifications:

- Failed payment attempts.
- Finalized invoices.
- Receipts for paid invoices.
- Payments requiring 3D Secure.
- Expiring cards on file.
- Unpaid one-off invoices.Invoicing Plus
- Created credit notes.
- Issued refunds.
- Ending subscription trials.
- Canceled subscriptions.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Configure emails](#configure-emails)[Failed payment notifications](#failed-payment-notifications)[Unpaid recurring invoice reminders](#unpaid-recurring-invoice-reminders)[Trial ending reminders](#trial-ending-reminders)[Renewal reminders](#renewal-reminders)[Payment confirmation notifications](#payment-confirmation-notifications)[Expiring card notifications](#expiring-card-notifications)[Link to a Stripe-hosted page](#link-to-a-stripe-hosted-page)[Test your configuration](#test-your-configuration)[Email logs](#email-logs)Products Used[Billing](/billing)[Revenue Recognition](/billing/revenue-recognition)[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`