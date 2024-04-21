htmlBECS Direct Debit payments in Australia | Stripe Documentation[Skip to content](#main-content)BECS Direct Debit in Australia[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fau-becs-debit)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fau-becs-debit)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank debits](/docs/payments/bank-debits)# BECS Direct Debit payments in Australia

Learn how to accept payments with BECS Direct Debit in Australia.Stripe users in Australia can accept Bulk Electronic Clearing System (BECS) Direct Debit payments from customers with an Australian bank account.

As part of the payment process, businesses must collect a mandate that includes the customer’s bank account details (account holder’s name, the Bank-State-Branch or BSB number, and the bank account number) and must also accept the mandate Service Agreement. This gives the business an authorization to debit the account. Stripe can generate this mandate for businesses to present to their customers.

BECS Direct Debit is a reusable, delayed notification payment method. This means that it can take up to three business days to receive notification on the success or failure of a payment after you initiate a debit from the customer’s account.

For new users, BECS Direct Debit transactions have a default limit of 1,500 AUD per transaction and 4,500 AUD per week. If you need higher limits, contact support.

Payment method propertiesCountry availability- Customer locations

Australia


- Presentment currency

AUD


- Payment confirmation

Business-intiated


- Payment method family

Bank debits


- Recurring payments

Yes


- Payout timing

Standard payout timing applies


- Connect support

Yes


- Refunds / Partial refunds

Yes / yes


- Dispute support

Yes



## Verification Requirements

Using BECS Direct Debit requires you to complete additional identity verification steps. We prompt you to complete these steps after you request access from the Payment methods settings. If you require further assistance, please contact support.

## Payment flow

![](https://b.stripecdn.com/docs-statics-srv/assets/checkout.4af16ecfd4f0a3f4044c56d6100c4a42.svg)

Customer selects BECS Direct Debit at checkout

![](https://b.stripecdn.com/docs-statics-srv/assets/account-info.6df4a503f8d05d1d9ddd20a6f15172df.svg)

Customer completes the Direct Debit Request

![](https://b.stripecdn.com/docs-statics-srv/assets/success.1ee3b6d34d944693e654e84f6d1be9f3.svg)

Customer gets notification that the payment is complete

Preview the payment flow using the test information below or view the sample code on GitHub.

- Any name
- Any email address
- Test BSB number: 000-000
- Test bank account number: 000123456

Preview BECS payment flow

## Get started

You don’t actually have to integrate BECS Direct Debit and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- [Checkout](/checkout/quickstart): Our prebuilt, hosted checkout page.
- [Elements](/payments/quickstart): Our drop-in UI components.

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

If you prefer to manually list payment methods or want to save BECS Direct Debit details for future payments, see the following guides:

- [Manually configure BECS Direct Debit as a payment](/payments/au-becs-debit/accept-a-payment)
- [Save BECS Direct Debit details for future payments](/payments/au-becs-debit/set-up-payment)

## Debit notification emails

The BECS scheme advises that you notify your customer when a mandate is established and each time you debit their account. By default, Stripe automatically sends emails to the customer.

If you decide to send your customer a custom notification:

- Turn off Stripe emails in the Stripe Dashboard email settings.


- Use the payment_intent.processing event to trigger debit initiation emails.


- It’s best to share (a link to) the mandate in the mandate notification


- The pre-debit notifications ideally include:

  - The last 4 digits of the customer’s bank account
  - The amount to be debited
  - Your contact information
  - The day you plan to debit the customer’s bank account


- The BECS guidelines suggest sending notifications at least 14 calendar days before you create a payment, but this isn’t mandatory. The default Stripe pre-debit email happens the day before the account gets debited. These pre-debit notifications should help you avoid unnecessary debit failures and disputes. For recurring payments of the same amount (for example, a subscription of a fixed amount), you can include multiple upcoming debits with corresponding dates in a single notice.



## Disputed payments

BECS Direct Debit provides a dispute process for bank account holders to dispute payments so you should familiarize yourself with this process if you decide to accept BECS Direct Debit payments.

For up to 7 years, a customer can dispute a debit payment through their bank on a “no questions asked” basis. Their bank honors all disputes within this period. If they dispute a charge and their bank accepts the request to return the funds, Stripe immediately removes the funds from your Stripe account.

If a dispute gets created, Stripe sends both the charge.dispute.created and charge.dispute.closed webhook events, and deducts the amount of the dispute and associated dispute fee from your Stripe balance.

Unlike credit card disputes, all BECS Direct Debit disputes are final and can’t be appealed. If a customer successfully disputes a payment, contact them to resolve the situation. ​​If you can come to an agreement and your customer is willing to return the funds to you, they need to make a new payment.

WarningIf you proactively issue your customer a refund while the customer’s bank also initiates the dispute process, your customer might receive two credits for the same transaction. You should follow the refund guidelines to avoid this.

## Mandates

During the payment process, businesses must collect a mandate that authorizes them to debit the account. In the BECS Direct Debit system, these mandates are called Direct Debit Requests, or DDRs.

Bank account holders can request the cancellation of active mandates at any time. To cancel a mandate, a bank account holder must either contact their bank or the party they established the mandate with. Canceling a mandate invalidates any future debit requests that you issue using it. If you want to accept additional payments from your customer, establish a new mandate with them.

### Mandate events

Event nameDescription`mandate.updated`Occurs whenever a mandate is canceled by the customer or due to a permanent debit failure. The`status`property will change to`inactive`.You can see the events in your Dashboard, but you should still set up a webhook endpoint.

## Refunds

Refunds for payments made with BECS Direct Debit must be issued within 90 days from the date of the original payment. Refunds require additional time to process (typically 3-5 business days). If you accidentally debit your customer, contact them immediately to avoid a payment dispute.

Refunds are processed only after the payment process completes. If you create a full or partial refund on a payment that hasn’t completed yet, the refund process starts when the Charge​ object’s status transitions to succeeded​. If the Charge​ object’s status transitions to failed​, the full or partial refund is marked as canceled because the money was never debited from the customer’s bank account.

BECS doesn’t explicitly label refunds when they’re deposited back into a bank account. Instead, refunds are processed as a credit and include a visible reference to the original payment’s statement descriptor.

Due to longer settlement time periods and how banks process BECS Direct Debit transactions, there is potential for confusion between you, your customer, your customer’s bank, and Stripe. For example, your customer might contact both you and their bank to dispute a payment. If you proactively issue your customer a refund while the customer’s bank also initiates the dispute process, your customer might receive two credits for the same transaction.

When issuing a refund, you should inform your customer immediately that the refund can take up to 5 business days to arrive in their bank account. Stripe won’t automatically send the customer any email to inform them about this.

## Statement descriptors

Every BECS Direct Debit payment shows two fields on the customers’ bank statements: the name of the merchant and the lodgement reference unique to this transaction.

For BECS Direct Debit payments created with Stripe, the name of the merchant is your Stripe account’s statement descriptor. You can override this default behavior for every transaction independently by using a dynamic statement descriptor. To do so, specify the statement_descriptor parameter when creating the PaymentIntent.

CautionYour statement descriptor gets truncated to the first 9 alphanumeric characters in the lodgement reference, followed by a unique ID. For example, if your statement descriptor is ROCKETRIDES, the customer will see ROCKETRID_XXXXXXX.

The table below illustrates the merchant name and lodgement reference behavior you can expect on the customer’s bank statement:

Default statement descriptorDynamic statement descriptorMerchant nameLodgement referenceRocket RidesUnspecified`RocketRides``RocketRid_AB1234CD`Rocket Rides`Sunday Ride``RocketRides``SundayRid_AB1234CD`Each bank in Australia formats these fields differently. Depending on your customer’s bank, some fields might appear in all lowercase or all uppercase.

### Statement descriptors and Connect

The charge type of Connect payments changes the statement descriptor and the merchant name, which appear on the customer’s bank statement.

Charge typeDescriptor taken fromDirectConnected AccountDestinationPlatformSeparate charge and transferPlatformDestination (with`on_behalf_of`)Connected AccountSeparate charge and transfer (with`on_behalf_of`)Connected AccountYou can’t use a mandate collected for a PaymentIntent on_behalf_of a Connected Account with a different Connected Account.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Verification Requirements](#verification-requirements)[Payment flow](#payment-flow)[Get started](#get-started)[Debit notification emails](#debit-notification-emails)[Disputed payments](#disputed-payments)[Mandates](#mandates)[Refunds](#refunds)[Statement descriptors](#statement-descriptors)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`