# BECS Direct Debit payments in Australia

Stripe users in Australia can accept Bulk Electronic Clearing System (BECS) Direct Debit payments from customers with an Australian bank account.

As part of the payment process, businesses must collect a mandate that includes the customer’s bank account details (account holder’s name, the Bank-State-Branch or BSB number, and the bank account number) and must also accept the mandate Service Agreement. This gives the business an authorization to debit the account. Stripe can generate this mandate for businesses to present to their customers.

BECS Direct Debit is a reusable, delayed notification payment method. This means that it can take up to three business days to receive notification on the success or failure of a payment after you initiate a debit from the customer’s account.

[reusable](/payments/payment-methods#usage)

[delayed notification](/payments/payment-methods#payment-notification)

For new users, BECS Direct Debit transactions have a default limit of 1,500 AUD per transaction and 4,500 AUD per week. If you need higher limits, contact support.

[support](https://support.stripe.com/contact)

- Customer locationsAustralia

Customer locations

Australia

- Presentment currencyAUD

Presentment currency

AUD

- Payment confirmationBusiness-intiated

Payment confirmation

Business-intiated

- Payment method familyBank debits

Payment method family

Bank debits

- Recurring paymentsYes

Recurring payments

Yes

- Payout timingStandard payout timing applies

Payout timing

Standard payout timing applies

- Connect supportYes

Connect support

Yes

- Refunds / Partial refundsYes / yes

Refunds / Partial refunds

Yes / yes

- Dispute supportYes

Dispute support

Yes

## Verification Requirements

Using BECS Direct Debit requires you to complete additional identity verification steps. We prompt you to complete these steps after you request access from the Payment methods settings. If you require further assistance, please contact support.

[identity verification](https://support.stripe.com/questions/common-questions-about-stripe-identity#how-verification-works)

[Payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

[contact support](https://support.stripe.com/contact)

## Payment flow

Customer selects BECS Direct Debit at checkout

Customer completes the Direct Debit Request

Customer gets notification that the payment is complete

Preview the payment flow using the test information below or view the sample code on GitHub.

[sample code](https://github.com/stripe-samples/au-becs-debit-payment)

- Any name

- Any email address

- Test BSB number: 000-000

- Test bank account number: 000123456

Preview BECS payment flow

[Preview BECS payment flow](https://v0n15.sse.codesandbox.io)

## Get started

You don’t actually have to integrate BECS Direct Debit and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

If you prefer to manually list payment methods or want to save BECS Direct Debit details for future payments, see the following guides:

- Manually configure BECS Direct Debit as a payment

[Manually configure BECS Direct Debit as a payment](/payments/au-becs-debit/accept-a-payment)

- Save BECS Direct Debit details for future payments

[Save BECS Direct Debit details for future payments](/payments/au-becs-debit/set-up-payment)

## Debit notification emails

The BECS scheme advises that you notify your customer when a mandate is established and each time you debit their account. By default, Stripe automatically sends emails to the customer.

If you decide to send your customer a custom notification:

- Turn off Stripe emails in the Stripe Dashboard email settings.

Turn off Stripe emails in the Stripe Dashboard email settings.

[Stripe Dashboard email settings](https://dashboard.stripe.com/account/emails)

- Use the payment_intent.processing event to trigger debit initiation emails.

Use the payment_intent.processing event to trigger debit initiation emails.

[payment_intent.processing](/api/events/types#event_types-payment_intent.processing)

- It’s best to share (a link to) the mandate in the mandate notification

It’s best to share (a link to) the mandate in the mandate notification

- The pre-debit notifications ideally include:The last 4 digits of the customer’s bank accountThe amount to be debitedYour contact informationThe day you plan to debit the customer’s bank account

The pre-debit notifications ideally include:

- The last 4 digits of the customer’s bank account

- The amount to be debited

- Your contact information

- The day you plan to debit the customer’s bank account

- The BECS guidelines suggest sending notifications at least 14 calendar days before you create a payment, but this isn’t mandatory. The default Stripe pre-debit email happens the day before the account gets debited. These pre-debit notifications should help you avoid unnecessary debit failures and disputes. For recurring payments of the same amount (for example, a subscription of a fixed amount), you can include multiple upcoming debits with corresponding dates in a single notice.

The BECS guidelines suggest sending notifications at least 14 calendar days before you create a payment, but this isn’t mandatory. The default Stripe pre-debit email happens the day before the account gets debited. These pre-debit notifications should help you avoid unnecessary debit failures and disputes. For recurring payments of the same amount (for example, a subscription of a fixed amount), you can include multiple upcoming debits with corresponding dates in a single notice.

[subscription](/billing/subscriptions/creating)

## Disputed payments

BECS Direct Debit provides a dispute process for bank account holders to dispute payments so you should familiarize yourself with this process if you decide to accept BECS Direct Debit payments.

For up to 7 years, a customer can dispute a debit payment through their bank on a “no questions asked” basis. Their bank honors all disputes within this period. If they dispute a charge and their bank accepts the request to return the funds, Stripe immediately removes the funds from your Stripe account.

If a dispute gets created, Stripe sends both the charge.dispute.created and charge.dispute.closed webhook events, and deducts the amount of the dispute and associated dispute fee from your Stripe balance.

[webhook](/webhooks)

Unlike credit card disputes, all BECS Direct Debit disputes are final and can’t be appealed. If a customer successfully disputes a payment, contact them to resolve the situation. ​​If you can come to an agreement and your customer is willing to return the funds to you, they need to make a new payment.

[credit card disputes](/disputes)

If you proactively issue your customer a refund while the customer’s bank also initiates the dispute process, your customer might receive two credits for the same transaction. You should follow the refund guidelines to avoid this.

[refund guidelines](#refunds)

## Mandates

During the payment process, businesses must collect a mandate that authorizes them to debit the account. In the BECS Direct Debit system, these mandates are called Direct Debit Requests, or DDRs.

Bank account holders can request the cancellation of active mandates at any time. To cancel a mandate, a bank account holder must either contact their bank or the party they established the mandate with. Canceling a mandate invalidates any future debit requests that you issue using it. If you want to accept additional payments from your customer, establish a new mandate with them.

You can see the events in your Dashboard, but you should still set up a webhook endpoint.

[webhook endpoint](/webhooks)

## Refunds

Refunds for payments made with BECS Direct Debit must be issued within 90 days from the date of the original payment. Refunds require additional time to process (typically 3-5 business days). If you accidentally debit your customer, contact them immediately to avoid a payment dispute.

Refunds are processed only after the payment process completes. If you create a full or partial refund on a payment that hasn’t completed yet, the refund process starts when the Charge​ object’s status transitions to succeeded​. If the Charge​ object’s status transitions to failed​, the full or partial refund is marked as canceled because the money was never debited from the customer’s bank account.

BECS doesn’t explicitly label refunds when they’re deposited back into a bank account. Instead, refunds are processed as a credit and include a visible reference to the original payment’s statement descriptor.

Due to longer settlement time periods and how banks process BECS Direct Debit transactions, there is potential for confusion between you, your customer, your customer’s bank, and Stripe. For example, your customer might contact both you and their bank to dispute a payment. If you proactively issue your customer a refund while the customer’s bank also initiates the dispute process, your customer might receive two credits for the same transaction.

When issuing a refund, you should inform your customer immediately that the refund can take up to 5 business days to arrive in their bank account. Stripe won’t automatically send the customer any email to inform them about this.

## Statement descriptors

Every BECS Direct Debit payment shows two fields on the customers’ bank statements: the name of the merchant and the lodgement reference unique to this transaction.

For BECS Direct Debit payments created with Stripe, the name of the merchant is your Stripe account’s statement descriptor. You can override this default behavior for every transaction independently by using a dynamic statement descriptor. To do so, specify the statement_descriptor parameter when creating the PaymentIntent.

[statement descriptor](/get-started/account/statement-descriptors)

[dynamic statement descriptor](/payments/payment-intents#dynamic-statement-descriptor)

Your statement descriptor gets truncated to the first 9 alphanumeric characters in the lodgement reference, followed by a unique ID. For example, if your statement descriptor is ROCKETRIDES, the customer will see ROCKETRID_XXXXXXX.

The table below illustrates the merchant name and lodgement reference behavior you can expect on the customer’s bank statement:

Each bank in Australia formats these fields differently. Depending on your customer’s bank, some fields might appear in all lowercase or all uppercase.

The charge type of Connect payments changes the statement descriptor and the merchant name, which appear on the customer’s bank statement.

You can’t use a mandate collected for a PaymentIntent on_behalf_of a Connected Account with a different Connected Account.
