# ACH Direct Debit

ACH lets you accept payments from customers with a US bank account. ACH Direct Debit is a reusable, delayed notification payment method. It can take up to 4 business days to receive acknowledgement of success or failure. Because ACH Direct Debit isn’t a guaranteed payment method, there’s a risk of failed payments and disputes.

[reusable](/payments/payment-methods#usage)

[delayed notification](/payments/payment-methods#payment-notification)

[up to 4 business days](/payments/ach-debit#timing)

[disputes](/payments/ach-debit#disputed-payments)

For more information about the fees charged for ACH transactions, see pricing details.

[pricing details](https://stripe.com/pricing#pricing-details)

Accepting bank accounts is slightly different from accepting cards:

- Your customer must authorize the payment terms.

[authorize](/payments/ach-debit#mandates)

- Bank accounts must be verified.

[verified](#verification)

- Customer locationsUS

Customer locations

US

- Presentment currencyUSD

Presentment currency

USD

- Payment confirmationBusiness-initiated

Payment confirmation

Business-initiated

- Payment method familyBank debit

Payment method family

Bank debit

- Recurring paymentsYes

Recurring payments

Yes

- Payout timing2-5 days

Payout timing

2-5 days

- Connect supportYes

Connect support

Yes

- Dispute supportYes

Dispute support

Yes

- Refunds / Partial refundsYes / yes

Refunds / Partial refunds

Yes / yes

## Payment flow

At checkout, the customer selects ACH Direct Debit.

The customer signs into their bank account to provide account information.

The merchant presents the mandate. The customer accepts it by completing the purchase.

The customer is notified when payment is complete.

## Get started

If ACH is all you want, learn how to accept a payment with ACH. Below are options to skip writing that code.

[accept a payment](/payments/ach-debit/accept-a-payment)

You don’t actually have to integrate ACH Direct Debit and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

The following Stripe products also support adding ACH Direct Debit from the Dashboard:

- Invoicing

[Invoicing](/invoicing/quickstart-guide)

- Payment Links

[Payment Links](/payment-links)

- Subscriptions

[Subscriptions](/billing/subscriptions/overview)

If you prefer to manually list payment methods or want to save ACH Direct Debit details for future payments, see the following guides:

- Manually configure ACH Direct Debit as a payment

[Manually configure ACH Direct Debit as a payment](/payments/ach-debit/accept-a-payment)

- Save ACH Direct Debit details for future payments

[Save ACH Direct Debit details for future payments](/payments/ach-debit/set-up-payment)

## Timing

With ACH Direct Debit, it can take time for funds to become available in your Stripe balance. The amount of time it takes for funds to become available is referred to as the settlement timing. The following tables describe the settlement timings for ACH Direct Debit payments that Stripe offers.

Initial payments made from select bank accounts that use temporary account numbers with Financial Connections might be subject to settlement delays.

[Payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

[Support](https://support.stripe.com/questions/two-day-settlement-for-ach-direct-debit)

A diagram showing the two settlement timings for ACH Direct Debit: standard (4 days) and faster (2 days).

For information on how to cancel payments, see Refund and cancel payments.

[Refund and cancel payments](/refunds#cancel-payment)

## ACH transaction failures

ACH Direct Debit transactions can fail any time after the payment is initiated through payment confirmation. These failures can occur for a number of reasons, such as:

- Insufficient funds

- An invalid account number

- A customer disabling debits from their bank account

If a payment fails after funds have been made available in your Stripe balance, Stripe immediately removes funds from your Stripe account.

In rare situations, Stripe might receive an ACH failure from the bank after a PaymentIntent has transitioned to succeeded. If this happens, Stripe creates a dispute with a reason of:

- insufficient_funds

- incorrect_account_details

- bank_cannot_process

Stripe charges a failure fee in this situation.

## Verification

Learn about validation and verification requirements.

[validation and verification](https://support.stripe.com/questions/nacha-bank-account-validation-rule)

Stripe lets your customers securely share their financial data by linking their financial accounts to your business. Use Financial Connections to access customer-permissioned financial data such as tokenized account and routing numbers, balance data, ownership details, and transaction data.

[Financial Connections](/financial-connections)

Your customers might enter their bank account manually instead of authenticating with Stripe Financial Connections. In these cases, Stripe provides a fully-hosted flow for collecting bank account details and verifies them with microdeposits.

When you use Stripe.js, our JavaScript library for building payment flows, Stripe provides a fully-hosted collection of bank account details, instant bank verification, and (if needed) delayed verification using microdeposits. This verification process is a requirement for many businesses, and it helps reduce payment failures and fraudulent activities.

[Stripe.js](/payments/elements)

## ACH Mandates

ACH Direct Debit rules require that you first get authorization from a customer to take payments before you can debit their bank account. To obtain authorization, you present a mandate to them. This mandate specifies the terms for one-time or recurring payments. The customer must agree to this mandate before you can collect any payments from their bank account.

When you use Stripe to initiate ACH transactions with your customers, make sure you have all the necessary authorizations and approvals from your customers for Stripe to transmit an ACH debit transaction to the customer’s bank account. The information you provide Stripe about each ACH transaction must be accurate and complete, including the name of your customer that authorized you to initiate the ACH transaction to their bank account.

There are two types of mandates: online and offline.

- Online mandates: Appear as part of the payment flow on a website. Customers accept online mandates through a user interface element, such as clicking an Accept or Pay button, or by checking a box.

Online mandates: Appear as part of the payment flow on a website. Customers accept online mandates through a user interface element, such as clicking an Accept or Pay button, or by checking a box.

- Offline mandates: Require that you present the specific terms of the transaction to your customer in writing or over the phone. The customer accepts those terms when they sign the paper or verbally agree to the terms over the phone. See the details on the offline mandate types Stripe supports.

Offline mandates: Require that you present the specific terms of the transaction to your customer in writing or over the phone. The customer accepts those terms when they sign the paper or verbally agree to the terms over the phone. See the details on the offline mandate types Stripe supports.

[details on the offline mandate types](/payments/ach-debit/sec-codes)

Stripe displays an online mandate on the payment page for you if you use one of the following hosted products:

- Checkout

- Payment Element

- Hosted Invoices Page

For custom payment forms that directly integrate with the Payment Intents API, you must display the mandate terms on your payment page before confirming the PaymentIntent or SetupIntent.

You only need to display a mandate the first time you collect a customer’s bank account.

We recommend that you use the following mandate text for your online custom payment form. This text must include  the customer’s name, bank account information, and the date.

For details on displaying the correct business name for Connect users, see merchant of record and statement descriptors.

[merchant of record and statement descriptors](#connect-merchant-of-record)

If you plan to use the customer’s bank account for future payments with the setup_future_usage parameter or by saving bank details for a future payment, also include:

[setup_future_usage](/api/payment_intents/create#create_payment_intent-setup_future_usage)

[saving bank details](/payments/ach-debit/set-up-payment)

If you originate recurring preauthorized debits, you must disclose to your customers how these amounts are calculated or a range the customer can anticipate. You must also give your customer at least 7 calendar days notice if you change the timing of any recurring preauthorized debits.

By default, if your customer provides a billing email address, Stripe automatically emails your customer the following information:

[billing email address](/api/payment_methods/object#payment_method_object-billing_details-email)

- Confirmation of the mandate, per Nacha requirements.

- Notification if Stripe needs to use microdeposits to verify your customer’s bank account. These notification emails link to a hosted verification page.

You can send custom mandate notifications to customers.

To send custom mandate notifications:

- Turn off Stripe emails in the Stripe Dashboard email settings

[email settings](https://dashboard.stripe.com/settings/emails)

- Send a mandate confirmation email when you receive your customer’s bank account and mandate authorization.

In the email, include the following information:

- Authorization date

- Account holder name

- Financial institution

- Routing number

- Last four digits of the account number

The following is a sample mandate confirmation email that you can send.

If you collected the customer’s bank account for future payments with the setup_future_usage parameter or by saving bank details, also include:

[setup_future_usage](/api/payment_intents/create#create_payment_intent-setup_future_usage)

[saving bank details](/payments/ach-debit/set-up-payment)

If you choose to send custom emails, you also need to send microdeposit reminder emails. For detailed instructions, see Custom microdeposit email and verification page.

[Custom microdeposit email and verification page](/payments/ach-debit/accept-a-payment#web-verify-with-microdeposits)

## ACH disputes

ACH Direct Debit provides a dispute process for bank account holders to dispute payments. Customers can generally dispute a payment through their bank for up to 60 calendar days after a debit on a personal account, or up to 2 business days for a business account. In rare instances, a debit payment can be successfully disputed outside these timelines. This is called a late return. The late return process is primarily managed by and ultimately decided at the discretion of the banks involved in the transaction.

When a dispute is created, Stripe sends both the charge.dispute.created and charge.dispute.closed webhook events and deducts the amount of the dispute and associated dispute fee from your Stripe balance.

[charge.dispute.created](/api/events/types#event_types-charge.dispute.created)

[charge.dispute.closed](/api/events/types#event_types-charge.dispute.closed)

[webhook](/webhooks)

Unlike credit card disputes, all ACH Direct Debit disputes are final and there is no process for appeal. If a customer successfully disputes a payment, you must contact them if you want to resolve the situation.

If you proactively issue your customer a refund while the customer’s bank also initiates the dispute process, your customer might receive two credits for the same transaction. Follow the guidelines in the following section on refunds to avoid this situation.

When a customer disputes an ACH Direct Debit payment, it invalidates the mandate associated with the payment method and you can’t reuse it. To attempt a charge again, you must resolve the dispute with the customer and collect a new mandate authorization.

[collect a new mandate authorization](/payments/ach-debit/accept-a-payment#resolving-disputes)

If they dispute a subsequent payment, Stripe blocks the bank account from further re-use. To learn more about resolution steps, see Blocked bank accounts.

[Blocked bank accounts](/payments/ach-debit/blocked-bank-accounts)

## ACH refunds

You have a maximum of 180 days from the date of the original payment to submit a refund for an ACH Direct Debit payment. Refunds require at least 3 business days to process.

If you accidentally debit your customer, contact them immediately to avoid a payment dispute. Factors such as slightly longer settlement time periods and the way banks process ACH Direct Debit transactions can cause confusion between you, your customer, your customer’s bank, and Stripe. For example, your customer might contact both you and their bank to dispute a payment. If you proactively issue your customer a refund while the customer’s bank also initiates the dispute process, your customer might receive two credits for the same transaction, so it’s important to communicate with your customer about the processing time and the status of their refund.

If you request a refund for a payment that hasn’t completed yet (within a few hours of creating the Payment Intent), Stripe doesn’t submit the charge to the bank, essentially canceling the original payment rather than refunding it.

Stripe doesn’t explicitly label ACH Direct Debit refunds as refunds when we deposit the funds back to a customer’s bank account. Instead, we process refunds as a credit and include a reference to the statement descriptor for the original payment.

## Statement descriptors for ACH

Every ACH Direct Debit payment shows up on customers’ bank statements with the name of the merchant. For payments created with Stripe, the name of the merchant is your Stripe account’s statement descriptor. You can override this default behavior for every transaction independently by using a dynamic statement descriptor. To do so, specify the statement_descriptor parameter when creating the PaymentIntent.

[statement descriptor](/get-started/account/statement-descriptors)

[dynamic statement descriptor](/payments/payment-intents#dynamic-statement-descriptor)

[statement_descriptor](/api/payment_intents/create#create_payment_intent-statement_descriptor)

Your statement descriptor truncates to the first 16 alphanumeric characters on the bank statement. For example, if your statement descriptor is ROCKETRIDESLIMITED, the customer sees ROCKETRIDESLIMIT.

Additionally, statement descriptors cannot use the special characters <, >, ', or ".

The table below illustrates the merchant name behavior you can expect on the customer’s bank statement:

Each bank formats these fields differently. Depending on your customer’s bank, some fields may appear in all lowercase or uppercase.

## Connect and ACH

If you use Connect, you must take the following into consideration before you enable and use ACH Direct Debits.

[Connect](/connect)

Set the us_bank_account_ach_payments capability to active on your platform account, and for any connected accounts you want to enable for ACH debits. You can also request more account capabilities.

[request more account capabilities](/connect/account-capabilities#requesting-unrequesting)

The charge type of Connect payments might change the default statement descriptor and the merchant name that appears on the customer’s bank statement. The charge type can also change:

[charge type](/connect/charges)

- The merchant of record shown on the mandate

- The merchant shown on confirmation emails

- The merchant shown on microdeposit reminder emails

The merchant of record determines the Stripe account authorized to create payments with a particular PaymentMethod. To learn more about sharing this authorization across multiple connected accounts, see PaymentMethod and Mandate cloning.

[PaymentMethod](/api/payment_methods/object)

[PaymentMethod and Mandate cloning](#payment-method-and-mandate-cloning)

You can collect customer bank accounts on the platform account and clone ACH Direct debit payment methods. Cloning these methods allows you to save customer bank accounts for later use on connected accounts. When you clone ACH Direct Debit payment methods, Stripe duplicates the mandate authorization to the connected account, but we don’t send any new mandate confirmation emails.

[clone](/payments/payment-methods/connect#cloning-payment-methods)

You can’t use a mandate authorized for a PaymentIntent or SetupIntent on_behalf_of of a connected account with a different connected account.

[on_behalf_of](/connect/charges#on_behalf_of)

When collecting a bank account that you intend to clone to connected accounts, you must communicate to the customer that their authorization extends to connected accounts on your platform. For example, you can communicate this message to a customer through the mandate terms. Failure to communicate this message to your customers could result in customer confusion and increase the risk of disputed payments.

## Testing ACH

Learn how to test scenarios with instant verifications using Financial Connections.

[Financial Connections](/financial-connections/testing#web-how-to-use-test-accounts)

After you collect the bank account details and accept a mandate, send the mandate confirmation and microdeposit verification emails in test mode. To do this, provide an email in the payment_method_data.billing_details[email] field in the form of {any-prefix}+test_email@{any_domain} when you collect the payment method details.

[payment method details](#web-collect-details)

You need to activate your Stripe account before you can trigger these emails in Test mode.

[activate your Stripe account](/get-started/account/activate)

Stripe provides several test account numbers and corresponding tokens you can use to make sure your integration for manually-entered bank accounts is ready for production.

[PaymentIntent cancellation](/api/payment_intents/cancel)

Before test transactions can complete, you need to verify all test accounts that automatically succeed or fail the payment. To do so, use the test microdeposit amounts or descriptor codes below.

To mimic different scenarios, use these microdeposit amounts or 0.01 descriptor code values.
