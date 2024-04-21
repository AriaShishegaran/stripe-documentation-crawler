htmlGenerate credit notes programmatically | Stripe Documentation[Skip to content](#main-content)Generate credit notes[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fintegration%2Fprogrammatic-credit-notes)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/invoicing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fintegration%2Fprogrammatic-credit-notes)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Invoicing](/docs/invoicing)[Integrate with the API](/docs/invoicing/integration)# Generate credit notes programmatically

Use the Invoicing API to adjust or refund finalized invoices with credit notes.To adjust the balance of an open or paid invoice, generate a credit note.

NoteFor information about working with credit notes using the Dashboard, see Issue credit notes.

When you create a credit note, you can apply credit amounts in three ways:

- Discount a fixed amount from an invoice line item.
- Discount a quantity from an invoice line item. The total discount is the discount quantity times the unit price of that line item.
- Apply a discount to the total invoice amount by adding a custom discount line item with a description, quantity, and unit price. The total discount is the quantity times the unit price.

We recommend discounting invoice line items when possible, since it associates each credit with a line item. Adding a custom discount line item can make reporting and tracking difficult, because the credit isn’t associated with a real invoice line item.

NoteYou can’t combine discount types on an invoice line item. For example, if you discount a line item quantity, then a future credit note can only discount that line item by quantity, not by amount. If you discount a line item amount, then a future credit note can only discount that line item by amount, not by quantity.

## Credit notes for open invoices

When you create a custom line item on a credit note for an open invoice, the amount_due on the invoice decreases based on the custom_line_items in the credit note. This is in addition to any adjustments you make to existing invoice_line_items. For example, if the amount due on an open invoice is 100 USD and you create a custom_line_item with quantity=1 and unit_amount=2000, the new amount due on the invoice is 80 USD.

On an invoice, credit notes appear as items after applying discounts and taxes—so they’re a post-tax adjusted amount.  We calculate the invoice amount due using the following order:

1. Sum of invoice line items
2. Discounts
3. Pre-tax invoice total
4. Taxes
5. Customer credit balance
6. Credit notes applied (to gross amount due)
7. New amount due

If applying a credit note to an invoice changes the amount due to zero, the invoice automatically transitions into the paid state. If you want to change the quantity or amount of an existing line item, pass the invoice ID, the line item ID, and the new quantity or amount. When a line item has a quantity and an amount, you can only update the quantity. Otherwise, you can only change the amount. The example below adjusts the quantity to two:

Command Line[curl](#)`curl https://api.stripe.com/v1/credit_notes \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d invoice={{INVOICE_ID}} \
  -d "lines[0][type]"=invoice_line_item \
  -d "lines[0][invoice_line_item]"={{INVOICE_LINE_ITEM}} \
  -d "lines[0][quantity]"=2`To create a custom line item on the credit note, pass the invoice ID, description, quantity, and unit amount. You can (optionally) set a tax rate as well. This example creates a custom line item on the credit note for 10 USD:

Command Line[curl](#)`curl https://api.stripe.com/v1/credit_notes \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d invoice={{INVOICE_ID}} \
  -d "lines[0][type]"=custom_line_item \
  -d "lines[0][description]"="Courtesy credit" \
  -d "lines[0][quantity]"=1 \
  -d "lines[0][unit_amount]"=1000`## Credit notes for paid invoices

When you create a credit note for a paid invoice, the amount due on the invoice doesn’t change. Instead, the user can choose one or more of the following options:

ActionDescriptionCreate a refundRefund the invoice’s charge back to the customer’s payment method.Link a refundLink an existing refund for the invoice’s charge.Credit the customer credit balanceCredit the customer credit balance, which is automatically applied to their future invoices.Credit outside of StripeCredit the invoice for an amount made in an adjustment outside of Stripe.In the following example, the credit note creates a refund:

Command Line[curl](#)`curl https://api.stripe.com/v1/credit_notes \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d invoice={{INVOICE_ID}} \
  -d "lines[0][type]"=invoice_line_item \
  -d "lines[0][invoice_line_item]"={{INVOICE_LINE_ITEM}} \
  -d "lines[0][quantity]"=2 \
  -d refund_amount=500`Here, the credit note creates a credit to the customer credit balance:

Command Line[curl](#)`curl https://api.stripe.com/v1/credit_notes \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d invoice={{INVOICE_ID}} \
  -d "lines[0][type]"=invoice_line_item \
  -d "lines[0][invoice_line_item]"={{INVOICE_LINE_ITEM}} \
  -d "lines[0][quantity]"=2 \
  -d credit_amount=500`You can also combine multiple parameters. Funds that are left over after subtracting the refund and credit amounts from the invoice amount results in a credit outside of Stripe, usually with cash or a check:

Command Line[curl](#)`curl https://api.stripe.com/v1/credit_notes \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d invoice={{INVOICE_ID}} \
  -d "lines[0][type]"=invoice_line_item \
  -d "lines[0][invoice_line_item]"={{INVOICE_LINE_ITEM}} \
  -d "lines[0][quantity]"=2 \
  -d refund_amount=100 \
  -d credit_amount=200 \
  -d out_of_band_amount=200`## Voiding credit notes

You can void a credit note only if it’s on an open invoice. Voiding a credit note reverses its adjustment, increasing the amount due on the invoice by the amount of the credit note. To void a credit note:

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/credit_notes/{{CREDIT_NOTE_ID}}/void \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`## Crediting negative line items  Beta

You can now credit negative invoice line items. This feature is currently in private beta. If you’d like early access, please request to join our beta here.

Interested in crediting negative line items?Please provide your email address below and our team will be in touch.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.You can credit a negative amount to a negative invoice_line_item using either the amount or quantity parameters.

For example, if you have an open invoice with two line items:

- a positive line item with`quantity=1`and`unit_amount=10000`
- and a negative line item with`quantity=1`and`unit_amount=-5000`.

This example uses the amount parameter to credit the full amount of both line items:

Command Line[curl](#)`curl https://api.stripe.com/v1/credit_notes \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d invoice={{INVOICE_ID}} \
  -d "lines[0][type]"=invoice_line_item \
  -d "lines[0][invoice_line_item]"={{POSITIVE_INVOICE_LINE_ITEM}} \
  -d "lines[0][amount]"=10000 \
  -d "lines[1][type]"=invoice_line_item \
  -d "lines[1][invoice_line_item]"={{NEGATIVE_INVOICE_LINE_ITEM}} \
  -d "lines[1][amount]"=-5000`This example uses the quantity parameter to do the same:

Command Line[curl](#)`curl https://api.stripe.com/v1/credit_notes \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d invoice={{INVOICE_ID}} \
  -d "lines[0][type]"=invoice_line_item \
  -d "lines[0][invoice_line_item]"={{POSITIVE_INVOICE_LINE_ITEM}} \
  -d "lines[0][quantity]"=1 \
  -d "lines[1][type]"=invoice_line_item \
  -d "lines[1][invoice_line_item]"={{NEGATIVE_INVOICE_LINE_ITEM}} \
  -d "lines[1][quantity]"=1`The following restrictions apply:

- The total amount of the credit note must remain positive.
- The total amount credited to a negative line item must be negative.
- The total amount credited to a negative line item can’t be less than the line item amount.

You also can’t credit a negative amount on a custom_line_item. We only support negative amounts on invoice_line_items.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Credit notes for open invoices](#open-invoices)[Credit notes for paid invoices](#paid-invoices)[Voiding credit notes](#voiding)[Crediting negative line items](#negative-line-items)Products Used[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`