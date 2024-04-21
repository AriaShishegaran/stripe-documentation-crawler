htmlBank transfer | Stripe Documentation[Skip to content](#main-content)Bank transfer[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fbank-transfer)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/invoicing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Fbank-transfer)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Invoicing](/docs/invoicing)[Payment methods for invoices](/docs/invoicing/payment-methods)# Bank transfer

Allow customers to pay invoices by transferring funds to a bank account.Bank transfer payments are often used for large enterprise deals or new business relationships. They can come with a lot of manual work for your team. Stripe can accept bank transfers from your customers using Stripe-provided, customer-specific bank account details.

The advantages of this approach are:

- You keep your bank account details confidential from your customers.
- You can automatically reconcile payments with open[invoices](/api/invoices).

## Overview

The first time you accept a bank transfer payment from a customer, Stripe generates a virtual bank account for them, which you can then share with them directly. All future bank transfer payments from this customer get sent to this bank account. In some countries, Stripe also provides you with a unique transfer reference number that your customer should include with each transfer to make it easier to match the transfer against outstanding payments. Some countries have limits on the number of virtual bank account numbers that you can create for free.

You can find an overview of the common steps when accepting a bank transfer payment in the following sequence diagram:

## Handling under- and over-payments

With bank transfer payments, it’s possible that the customer sends you more or less than the expected payment amount. If the customer sends too little, Stripe partially funds an open payment intent. Invoices won’t be partially funded and remain open until incoming funds cover the full invoice amount.

If the customer sends more than the expected amount, Stripe attempts to reconcile the incoming funds against an open payment and keep the remaining excess amount in the customer cash balance. You can find more details on how Stripe handles reconciliation in the reconciliation section of our documentation.

When a customer underpays:

When a customer overpays:

## Receive bank transfers

### API

You can make an API call to create an invoice with bank transfers as a payment method.

EUUKJPMXUSFirst, you create an invoice.

Command Line[curl](#)`curl https://api.stripe.com/v1/invoices \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d "payment_settings[payment_method_types][]"=customer_balance \
  -d "payment_settings[payment_method_options][customer_balance][funding_type]"=bank_transfer \
  -d "payment_settings[payment_method_options][customer_balance][bank_transfer][type]"=eu_bank_transfer \
  -d "payment_settings[payment_method_options][customer_balance][bank_transfer][eu_bank_transfer][country]"=NL \
  -d collection_method=send_invoice \
  -d days_until_due=30`Then you can add one or more invoice items to the invoice.

Command Line[curl](#)`curl https://api.stripe.com/v1/invoiceitems \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1234 \
  -d currency=eur \
  -d customer={{CUSTOMER_ID}} \
  -d description="Professional services" \
  -d invoice={{INVOICE_ID}}`Then you can finalize the invoice.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/invoices/{{INVOICE_ID}}/finalize \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`After the invoice is finalized, your customer can view their payment instructions on the hosted invoice page. The URL for the hosted invoice page is included in the API response as hosted_invoice_url.

### Dashboard

For USD invoices, you can enable Bank transfer by default in the Invoice settings.

For all other currencies, you can’t enable Bank transfer by default, but you can still add it to individual invoices. To create an invoice that supports a bank transfer payment, add customer_balance to an invoice over the API or configure payment methods on invoices in the Dashboard.

## Payment instructions

For each customer, Stripe generates a unique, virtual bank account number that can accept transfers in the currency of the invoice. The transfer instructions for this virtual bank account are visible to your customer on invoices.

The payment details Stripe creates are:

- Unique—No two customers have the same account number.
- Consistent—A single customer consistently receives the same funding instructions across multiple invoices.
- Currency-appropriate—In countries where bank transfers are supported, Stripe generates local bank account information (for example, a UK account for customers in the UK).
- Customer-localized—Payment instructions shown on invoices respect[Customer preferred languages](/invoicing/customize#customer-language), so you can localize instructions for each customer.

​​After a virtual bank account in Stripe receives a transfer, Stripe automatically reconciles the funds to open invoices and creates a charge to pay the invoice.

## Automatic transfer reconciliation

Upon receiving an inbound transfer, Stripe uses the transfer’s reference code, amount, and date when determining the invoices for reconciliation.

### Reference codes

​​Transfers commonly include a memo such as:

- INVOICE-0011
- Payment for INVOICE-0001
- This is for 001. I’ll send the check for 002 next week.

If the memo contains an invoice number, Stripe first attempts to reconcile the transfer to the referenced invoice. Reference code reconciliation requires that:

- the invoice number refers to an`open`or`past due`invoice.
- if the invoice is`past due`, it has become past due within the past thirty days.
- the amount transferred is enough to pay the invoice.

### Exact amount

After considering reference codes, Stripe looks for the oldest open invoice where the amount precisely matches the amount transferred. If we find one, we reconcile the transfer to the invoice.

### Multiple invoices

If any balance remains, it’s possible that your customer tried to pay multiple invoices with one transfer. Stripe looks for a group of invoices (five or fewer) where the payment received matches the total expected. In the case where there are multiple possible combinations, Stripe picks the smallest combination. If there are multiple options for the smallest combination, Stripe selects the combination that contains the oldest invoice.

### Oldest payable invoice

If more balance remains, it’s possible that your customer tried to pay multiple invoices with one transfer, or transferred extra funds. Stripe progressively pays open invoices by date (finalized until the balance runs out) or until no invoices remain to pay.

### Reconciliation failures

When funds transferred into Stripe aren’t reconciled to any open PaymentIntents or invoices, the funds are placed in the customer balance and the cash_balance.funds_available webhook is sent.

## Manual reconciliation

In certain circumstances, you might want to override Stripe’s automatic reconciliation behavior on a per-customer basis.

In manual reconciliation mode, Stripe doesn’t attempt to automatically reconcile any funds received, so all payments must be reconciled manually.

## Underpayments

Occasionally, customers might make a payment below the amount you requested. In these cases, you can treat the underpaid amount as an expense, and consider the invoice as fully paid.

To allow automatic reconciliation of partial payments, you can configure a minimum payment amount and Stripe credits the difference to the customer. Navigate to the Dashboard’s Automatic collection settings section to specify rules for underpayment.

## Refunding transfers

You can refund completed payments through a refund or credit note back to the customer balance. ​​If any PaymentIntents or invoices are awaiting payment, the funds added to the customer balance are reconciled against them.

## Testing

To test an inbound transfer of funds in the Dashboard or with the Stripe CLI, see Test your integration.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Overview](#overview)[Handling under- and over-payments](#handling-under--and-over-payments)[Receive bank transfers](#bank-transfers)[Payment instructions](#payment-instructions)[Automatic transfer reconciliation](#automatic-transfer-reconciliation)[Manual reconciliation](#manual-reconciliation)[Underpayments](#underpayments)[Refunding transfers](#refund-transfers)[Testing](#testing)Products Used[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`