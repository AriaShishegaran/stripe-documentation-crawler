# Automatic collection

Stripe provides a number of automated revenue recovery features for one-off invoices to help collect payments that might have failed otherwise. These include automatically updating your users’ saved cards, sending emails when a failed payment occurs, and retrying cards at strategic times.

## Smart Retries

To avoid bank fees, Stripe ​doesn’t retry invoice payments that customers made with bank debit methods including: BECS direct debit, Bacs direct debit, or SEPA direct debit.

[BECS direct debit](/payments/au-becs-debit)

[Bacs direct debit](/payments/payment-methods/bacs-debit)

[SEPA direct debit](/payments/sepa-debit)

Using machine learning, Smart Retries chooses the best times to retry failed payment attempts to increase the chance of successfully paying an invoice. The machine learning system behind Smart Retries uses time-dependent, dynamic signals, such as:

- The number of different devices that have presented a given payment method in the last N hours.

- The best time to pay (payments made for debit cards in certain countries might be slightly more successful at 12:01 AM in local time zones).

Based on a combination of these factors, Stripe intelligently assesses when to retry payments. We continuously learn from new purchaser behaviors and transactions, which provide for a more targeted approach over traditional rules-based payment retry logic. Any invoice with the auto_advance attribute set to true goes through the Smart Retries flow (if enabled), regardless of the selected payment method.

[auto_advance](/api/invoices/create#create_invoice-auto_advance)



Smart Retries reattempts the charge according to your specifications for the number of retries and the maximum duration. You can also use Recovery automations to create different retry policies for different customer segments.

[Recovery automations](/billing/revenue-recovery/automations)

You can override this behavior by disabling Smart Retries and defining your own custom retry rules. When you enable dunning, the next_payment_attempt attribute on the invoice.payment_failed webhook indicates when Stripe attempts the next collection.

[disabling Smart Retries](https://dashboard.stripe.com/revenue_recovery/retries)

[next_payment_attempt](/api/invoices/object#invoice_object-next_payment_attempt)

[webhook](/webhooks)

## Failed payment notifications

In your Subscriptions and emails settings, go to Manage failed payments for subscriptions. The setting Send emails when card payments fail turns on automatic customer emails for failed payments.

[Subscriptions and emails settings](https://dashboard.stripe.com/settings/billing/automatic)

If a payment failure occurs on a one-off invoice and Link to a Stripe-hosted page is selected, Stripe sends a link to the Hosted Invoice Page to the customer.

[Hosted Invoice Page](/invoicing/hosted-invoice-page)

You can customize the color, icon, and logo of your customer emails and Stripe-hosted page in the Branding settings.

[Branding settings](https://dashboard.stripe.com/settings/branding)

For failed payment emails, you can write your own email message to your customers instead of using the default email message. You’ll also need to use a verified custom domain to send emails from.

[custom domain](/get-started/account/email-domain)

- Click the customize link in the sentence below the Send emails to customers to update failed card payment methods option.

Click the customize link in the sentence below the Send emails to customers to update failed card payment methods option.

- Choose the Use your own custom email option.

Choose the Use your own custom email option.

- Read the email policy guidelines. By law, you can’t add promotional content without explicit consent from the customer.

Read the email policy guidelines. By law, you can’t add promotional content without explicit consent from the customer.

- Fill out the contents of the email. As you enter information, you can see a preview of the email.

Fill out the contents of the email. As you enter information, you can see a preview of the email.

[privacy policy](https://stripe.com/privacy)

## Manage invoices sent to customers

In your Subscriptions and emails settings, go to Manage invoices sent to customers to:

- Email finalized invoices to customers—You can turn this option on to always email your customers a finalized invoice. This setting only affects invoices where the collection_method is set to send_invoice.

[collection_method](/api/invoices/object#invoice_object-collection_method)

- Change a past due invoice’s status—You can mark an invoice as uncollectible if it’s past due by 30, 60, or 90 days. You can also leave the invoice past-due.

- Automatically reconcile partial payments that meet a minimum—You can instruct Stripe to mark an invoice as paid if ​​it’s partially paid within the set amount. For example, if the payment received from your customer is within 20 USD or less of the total (or at whatever amount you configure), then this setting applies a credit to the invoice for the outstanding amount. It then marks the invoice as paid.

To turn on automatic reminders for unpaid, one-off invoices go to Send reminders under Manage advanced invoicing features. When the feature is on, select  whether you want Stripe to send the reminder before, when, or after the invoice is due.
