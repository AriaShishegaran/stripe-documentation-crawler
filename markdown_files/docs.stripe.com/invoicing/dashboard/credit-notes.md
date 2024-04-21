htmlIssue credit notes | Stripe Documentation[Skip to content](#main-content)Issue credit notes[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fdashboard%2Fcredit-notes)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/invoicing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fdashboard%2Fcredit-notes)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Invoicing](/docs/invoicing)[Use the Dashboard](/docs/invoicing/dashboard)# Issue credit notes

Use the Dashboard to adjust or refund finalized invoices with credit notes.Credit notes are documents that decrease the amount of an open or paid invoice. The difference between issuing a credit note and adjusting the amount of an invoice by revising it is that a credit note doesn’t void and replace the original invoice. Some example scenarios where you might use credit notes include:

- You accidentally overbilled a customer—You accidentally charged your customer 110 USD instead of 100 USD because of a data entry mistake. Use a credit note to give your customer a 10 USD credit for the overcharge.
- You’re short on inventory—You billed your customer for five items, but when it’s time to ship them you realize you only have three items left in stock. Use a credit note to refund your customer for the two items they didn’t receive.
- Discounts—You and your customer negotiate a discount on an invoice. Instead of voiding the invoice and issuing a new one, you can use a credit note to adjust the amount owed on the existing invoice.

A credit note reduces the amount due without recording any payment. However, if a credit note reduces the balance of an open invoice to 0, the invoice status changes to paid. For information on invoice statuses, see the Invoicing overview.

NoteFor information about working with credit notes using the API, see Generate credit notes programmatically.

## Get started

When you issue a credit note for an open invoice, it decreases the amount due on the invoice. When you issue a credit note for a paid invoice, you credit the customer’s account balance or give them a refund outside of Stripe.

The sum of all credit notes issued for an invoice can’t exceed the ​​total amount of the invoice. For a paid invoice, the sum of the refund, credit, and out-of-band payment amounts must equal the credit note total.

When you create a credit note, you can apply credit amounts in three ways:

- Discount a fixed amount from an invoice line item.
- Discount a quantity from an invoice line item. The total discount is the discount quantity times the unit price of that line item.
- Apply a discount to the total invoice amount by adding a custom discount line item with a description, quantity, and unit price. The total discount is the quantity times the unit price.

We recommend discounting invoice line items when possible, since it associates each credit with a line item. Adding a custom discount line item can make reporting and tracking difficult, because the credit isn’t associated with a real invoice line item.

NoteYou can’t combine discount types on an invoice line item. For example, if you discount a line item quantity, then a future credit note can only discount that line item by quantity, not by amount. If you discount a line item amount, then a future credit note can only discount that line item by amount, not by quantity.

## Create a credit note

You can create credit notes for open or paid invoices.

1. Open the Invoices page in the Dashboard.


2. Select the open or paid invoice you want to add a credit note to.


3. Click More and select Issue a credit note.


4. Select a reason for the credit note.


5. (Optional) Perform the following actions:

  - Edit line item credit quantities or amounts.


  - Click Add item to add a custom line item.


  - Click Set item tax to select a tax rate to use for credit purposes.




6. If the invoice is paid, choose whether to refund the customer’s card, credit their balance, or refund the amount outside of Stripe (for example, cash).


7. Click Issue credit note to submit the credit note.



NoteOpen invoices can’t have a credit note with a pending payment_intent.

![](https://b.stripecdn.com/docs-statics-srv/assets/credit-note-dashboard.d9f67171b43e5ad618bc6d153b86286a.png)

Issue a credit note in the Dashboard

## Credit balances and discounts

When you issue a credit note on an invoice with an applied customer credit balance, funds are sometimes credited to the credit balance instead of the initial payment method. For example, if a credit balance of 150 USD is applied to an invoice for 200 USD, then the finalized invoice is for 50 USD. If you issue a credit note for 50 USD or less, the funds are refunded to the customer’s payment method. Anything above 50 USD is added to the customer’s credit balance and is applied to the next invoice.

Discounts apply proportionally to all of the line items on an invoice. For example, applying a 50% discount to an invoice with 10 line items at 10 USD each changes the amount of each line item to 5 USD. If you then apply a credit note for one line item, it reduces the invoice amount by 5 USD.

Fixed-amount discounts work the same way. If you apply a 10 USD discount to an invoice with 10 line items at 10 USD, each line item is 10% of the sum amount and is discounted by 10% * 10 USD = 1 USD. The amount of each line item becomes 9 USD. If you then apply a credit note for one line item, it reduces the invoice amount by 9 USD.

If you want to credit the original line item amount, you can make up the difference by adding a custom discount line item to the credit note. For example, if a discount reduced a line item’s credit amount from 10 USD to 9 USD, you can add a custom discount line item for 1 USD.

## Voiding credit notes

You can void a credit note only if it’s on an open invoice. Voiding a credit note reverses its adjustment, increasing the amount due on the invoice by the amount of the credit note.

To void a credit note in the Dashboard, click the overflow menu () at the top right of the credit note, then select Void credit note.

## Crediting negative line items  Beta

You can now credit negative invoice line items. This feature is currently in private beta. If you’d like early access, please request to join our beta here.

Interested in crediting negative line items?Please provide your email address below and our team will be in touch.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.The following restrictions apply:

- The total amount of the credit note must remain positive.
- The total amount credited to a negative line item must be negative.
- The total amount credited to a negative line item can’t be less than the line item amount.

You also can’t credit a negative amount on a custom credit note line item. We only support negative amounts on credit note line items that are tied to invoice line items.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Get started](#issuing)[Create a credit note](#creating)[Credit balances and discounts](#customer-balances-discounts)[Voiding credit notes](#voiding)[Crediting negative line items](#negative-line-items)Products Used[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`