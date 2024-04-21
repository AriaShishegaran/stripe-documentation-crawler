htmlBacs Direct Debit payments in the UK | Stripe Documentation[Skip to content](#main-content)Bacs Direct Debit[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-methods%2Fbacs-debit)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-methods%2Fbacs-debit)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank debits](/docs/payments/bank-debits)# Bacs Direct Debit payments in the UK

Learn how to accept payments with Bacs Direct Debit in the UK.Stripe users in the UK can accept Bacs Direct Debit payments from customers with a UK bank account.

To debit an account, businesses must collect a mandate from their customers. The mandate includes the customer’s sort code, account number, name, email, and full address. Stripe can generate this mandate for businesses to present to their customers.

BACS Direct Debit transactions have a limit of 100,000 GBP each. New users have an additional weekly limit of 10,000 GBP, which quickly increases as you process more BACS Direct Debit payments. If you need higher limits, contact support.

Bacs Direct Debit is a reusable, delayed notification payment method. That means it takes 3 business days to confirm the success or failure of a payment when a mandate is already in place, but when you must collect a new mandate, it can take 6 business days.

Payment method propertiesCountry availability- Customer locations

UK


- Presentment currency

GBP


- Payment confirmation

Business-initiated


- Payment method family

Bank debit


- Recurring payments

Yes


- Payout timing

Standard payout timing applies


- Connect support

Yes


- Dispute support

Yes


- Refunds / Partial refunds

Yes / yes



## Verification Requirements

Using Bacs Direct Debit requires you to complete additional identity verification steps. We prompt you to complete these steps after you request access from the Payment methods settings. If you require further assistance, please contact support.

## Get started

You don’t actually have to integrate Bacs Direct Debit and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- [Checkout](/checkout/quickstart): Our prebuilt, hosted checkout page.
- [Elements](/payments/quickstart): Our drop-in UI components.

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

### Other payment products

The following Stripe products also support adding Bacs Direct Debit from the Dashboard:

- [Invoicing](/invoicing/quickstart-guide)
- [Payment Links](/payment-links)
- [Subscriptions](/billing/subscriptions/overview)

If you prefer to manually list payment methods or want to save Bacs Direct Debit details for future payments, see the following guides:

- [Manually configure Bacs Direct Debit as a payment](/payments/bacs-debit/accept-a-payment)
- [Save Bacs Direct Debit details for future payments](/payments/bacs-debit/save-bank-details)

## Debit notifications

Bacs Direct Debit requires that customers are notified of the following:

- When payment details are initially collected and confirmed
- Each time a debit will be made on their account

By default, Stripe automatically sends emails to the customer for the above cases. You can customize the colors and logo for these emails to fit the design and branding of your business.

If you require sending your own customer email notifications, follow these steps to customize your Business Display Name and contact us for approval of your email templates.

## Disputed payments

Bacs Direct Debit provides a dispute process for customers to dispute payments.

CautionCustomers can dispute a payment through their bank for an unlimited period of time.

When a dispute is created, Stripe sends a charge.dispute.created webhook event and deducts the dispute amount from your Stripe balance. Bacs Direct Debit disputes don’t incur a fee.

Unlike credit card disputes, Bacs Direct Debit disputes are final and can’t be appealed. If a customer successfully disputes a payment, you must contact them if you want to resolve the situation. If you’re able to come to an arrangement and your customer is willing to return the funds to you, they must make a new payment.

## Mandates

As part of the payment process, businesses must collect a mandate which gives them authorization to debit an account. For Bacs, this mandate is called a Direct Debit Instruction, or DDI. You can find information on how to collect a mandate with Stripe Checkout on the Accept a payment page.

Customers can request the cancellation of a mandate at any time. To cancel a mandate, a customer must either reach out to the party they established the mandate with, or to their bank. Canceling a mandate invalidates any future debit requests that you issue using this mandate. If you want to accept additional payments from your customer, you need to establish a new mandate with them.

### Mandate events

The mandate can change at any time after you’ve collected it. This might be the result of the customer instructing their bank to amend the mandate or because of a change in the bank itself (for example, the customer changes to a different one). Stripe sends the following events when the mandate changes:

Event nameDescriptionCan accept payments?`mandate.updated`Occurs whenever a mandate is rejected, canceled, or reactivated by the Bacs network. Check[mandate.status](/api/mandates/object#mandate_object-status)to determine if the mandate can continue to be used.Yes, if the new status is`active``payment_method.automatically_updated`Occurs when a customer’s bank account details change.YesThese events are available in the Dashboard, but you can set up a webhook to handle these programatically.

## Refunds

Refunds for payments made with Bacs Direct Debit must be submitted within 180 days from the date of the original payment. Refunds require additional time to process (typically 3-4 business days). If you accidentally debit your customer, please contact them immediately to avoid a payment dispute.

WarningRefunds aren’t part of the Bacs Direct Debit scheme and are provided outside of Bacs Direct Debit by Stripe. Since Bacs Direct Debit has an indefinite indemnity period, if a customer creates a dispute any time after a refund has been issued, you can lose both the disputed amount and the amount you refunded separately.

You can issue full or partial refunds for Direct Debit payments by using the API to create a refund with the PaymentIntent object.

Refunds are processed only after the payment process is complete. If you create a full or partial refund on a payment that hasn’t completed yet, the refund process starts when the Charge object’s status transitions to succeeded. If the Charge object’s status transitions to failed, the full or partial refund is marked as canceled because the money was never debited from the customer’s bank account.

## Timing

It takes 3 business days to confirm the success or failure of a Bacs Direct Debit payment when a mandate is already in place and 6 business days when a new mandate must be collected. Payments made after 20:00 UTC are submitted the following business day.

In some cases, the bank might notify us of a payment failure after the payment has been marked as successful in your Stripe account. In this case the payment failure is identified as a dispute with the appropriate reason code.

This table shows the Bacs timeline in business days from the time (T) that a payment is made when a new mandate must be collected:

T+0Mandate submittedT+3Mandate is active and the payment is submittedT+5Funds leave the customer’s bank accountT+6Funds are available in Stripe## Checkout

Checkout creates a secure, Stripe-hosted payment page that lets you collect payments quickly. You can use Checkout to collect Bacs Direct Debit payments, or collect payment details that you can use to initiate payments at a later date.

### Request the bacs_debit_payments capability

Platforms in the UK don’t need to request the bacs_debit_payments capability for their UK Connect accounts when performing destination charges. Platforms outside the UK might still need to process Bacs Direct Debit payments for their UK Connect accounts, and they must have the bacs_debit_payments capability enabled.

In both scenarios, you must request the bacs_debit_payments capability if you want to use the on_behalf_of parameter.

Requesting the bacs_debit_payments capability with settings.bacs_debit_payments.display_name automatically enables custom branding. This allows you to collect mandates using the connected account’s chosen display name as the statement descriptor.

Each account that uses custom branding incurs a 50 GBP monthly fee.

If you don’t want to use custom branding, you can do either of the following:

- Request the capability without specifying`settings.bacs_debit_payments.display_name`
- Set the default value of`settings.bacs_debit_payments.display_name = Stripe`before requesting the capability

## Custom Branding

Upgrade to Custom Branding if you want to customize your customer’s bank statements, Stripe Checkout, and customer emails for direct debits to show your business name.

You can enable Custom Branding for your account in your Bacs Direct Debit settings.

For your Express or Custom accounts, you can enable Custom Branding by selecting settings.bacs_debit_payments.display_name in the API.

You can do this during account creation or when updating the account after setup.

If you request the bacs_debit_payments capability without specifying settings.bacs_debit_payments.display_name, the account defaults to Stripe branding.

Custom Branding is charged at 50 GBP per active month. Your business name is shown for new mandates created 5 business days after your request. To expedite Custom Branding or apply it to multiple connected accounts for a single fee, contact us.

If you don’t use your custom branding for a long period of time, your account automatically reverts back to the default Stripe branding.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Verification Requirements](#verification-requirements)[Get started](#get-started)[Debit notifications](#debit-notifications)[Disputed payments](#disputed-payments)[Mandates](#mandates)[Refunds](#refunds)[Timing](#timing)[Checkout](#checkout)[Custom Branding](#custom-branding)Products Used[Payments](/payments)[Checkout](/payments/checkout)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`