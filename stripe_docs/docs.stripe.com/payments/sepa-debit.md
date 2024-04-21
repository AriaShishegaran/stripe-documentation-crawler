# SEPA Direct Debit payments

The Single Euro Payments Area (SEPA) is an initiative of the European Union to simplify payments within and across member countries. They established and enforced banking standards to allow for the direct debiting of every EUR-denominated bank account within the SEPA region.

[Single Euro Payments Area (SEPA)](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area)

In order to debit an account, businesses must collect their customer’s name and bank account number in IBAN format. During the payment flow, customers must accept a mandate that gives the business an authorization to debit the account. Stripe is able to generate this mandate for businesses to present to their customers. Locate the ID of the mandate used for this payment on the Charge under the payment_method_details.sepa_debit.mandate property. Then, use the mandate ID to retrieve the Mandate.

[payment_method_details.sepa_debit.mandate](/api/charges/object#charge_object-payment_method_details-sepa_debit-mandate)

[retrieve the Mandate](/api/mandates/retrieve)

SEPA Direct Debit is a reusable, delayed notification payment method. This means that it can take up to 14 business days to receive notification on the success or failure of a payment after you initiate a debit from the customer’s account, though the average is five business days.

[reusable](/payments/payment-methods#usage)

[delayed notification](/payments/payment-methods#payment-notification)

SEPA Direct Debit transactions have a limit of 10,000 EUR each. For new users, there’s an additional weekly limit of 10,000 EUR, which quickly increases as you process more SEPA direct debit payments. If you need higher limits, contact support.

[contact support.](https://support.stripe.com/contact)

- Customer locationsEurope

Customer locations

Europe

- Payment method familyBank debit

Payment method family

Bank debit

- Connect supportYes

Connect support

Yes

- Presentment currencyEUR

Presentment currency

EUR

- Recurring PaymentsYes

Recurring Payments

Yes

- Dispute supportYes

Dispute support

Yes

- Payment confirmationBusiness-initiated

Payment confirmation

Business-initiated

- Payout timing3-6 days

Payout timing

3-6 days

- Refunds/ Partial refundsYes/yes

Refunds/ Partial refunds

Yes/yes

## Verification Requirements

Using SEPA Direct Debit requires you to complete additional identity verification steps. We prompt you to complete these steps after you request access from the Payment methods settings. If you require further assistance, please contact support.

[identity verification](https://support.stripe.com/questions/common-questions-about-stripe-identity#how-verification-works)

[Payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

[contact support](https://support.stripe.com/contact)

## Payment flow

Customer selects SEPA Direct Debit at checkout

[Customer](/api/customers)

Customer provides full name, IBAN, and authorizes mandate

Customer gets notification that the payment is complete

## Get started

You don’t actually have to integrate SEPA Direct Debit and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

The following Stripe products also support adding SEPA Direct Debit from the Dashboard:

- Invoicing

[Invoicing](/invoicing/quickstart-guide)

- Payment Links

[Payment Links](/payment-links)

- Subscriptions

[Subscriptions](/billing/subscriptions/overview)

If you prefer to manually list payment methods or want to save SEPA Direct Debit details for future payments, see the following guides:

- Manually configure SEPA Direct Debit as a payment

[Manually configure SEPA Direct Debit as a payment](/payments/sepa-debit/accept-a-payment)

- Save SEPA Direct Debit details for future payments

[Save SEPA Direct Debit details for future payments](/payments/sepa-debit/set-up-payment)

## Debit notification emails

The SEPA Direct Debit rulebook requires that you notify your customer each time you debit their account. For this case, by default, Stripe automatically sends the customer an email.

[SEPA Direct Debit rulebook](http://www.europeanpaymentscouncil.eu/index.cfm/sepa-direct-debit/sepa-direct-debit-core-scheme-sdd-core)

When processing SEPA Direct Debit payments using the Stripe Creditor ID, debit notification emails are always sent automatically by Stripe.

[Creditor ID](/payments/sepa-debit#creditor-identifiers-(creditor-id))

If you decide to send your customer a custom notification:

- Turn off Stripe emails in the Stripe Dashboard email settings. However, if you use the Sources API, you can only control emails using mandate.notification_method (for more information, see notifying customers of recurring payments).

[Stripe Dashboard email settings](https://dashboard.stripe.com/account/emails)

[mandate.notification_method](/api/sources/update#update_source-mandate-notification_method)

[notifying customers of recurring payments](/sources/sepa-debit#notifying-customers-of-recurring-payments)

- Use the payment_intent.processing event to trigger debit initiation emails.

[payment_intent.processing](/api/events/types#event_types-payment_intent.processing)

- The email must include:The last 4 digits of the debtor’s bank accountThe mandate reference (sepa_debit[reference] on the Mandate)The amount to be debitedYour SEPA creditor identifierYour contact information

- The last 4 digits of the debtor’s bank account

- The mandate reference (sepa_debit[reference] on the Mandate)

- The amount to be debited

- Your SEPA creditor identifier

- Your contact information

- It’s standard to send notifications at least 14 calendar days before you create a payment. However, SEPA rules let you send notifications closer to the payment date—just make sure your mandate clearly states when customers can expect to receive a notification. The mandate provided by Stripe specifies this can happen up to two calendar days in advance of future payments, allowing you to send notifications at payment creation. For recurring payments of the same amount (for example, a subscription of a fixed amount), you may indicate multiple upcoming debits with corresponding dates in a single notice.

[subscription](/billing/subscriptions/creating)

## Creditor Identifiers (Creditor ID)

A SEPA Creditor Identifier (Creditor ID) is an ID associated with each SEPA Direct Debit payment that identifies the company requesting the payment. While companies may have multiple creditor identifiers, each creditor identifier is unique and allows your customers to easily identify the debits on their account.

By default your Stripe account is configured to use a Stripe Creditor ID when collecting SEPA Direct Debit Payments. Stripe Payments will appear on bank statements alongside your configurable Stripe statement descriptor. We recommend configuring a recognizable statement descriptor to ensure customers recognize payments and to reduce the risk of disputes. If you’re using the Stripe Creditor ID, we also recommend you use Stripe Checkout to collect mandates from your customers for SEPA Direct Debits.

[Stripe statement descriptor](/get-started/account/statement-descriptors)

If you’re based in the EU, Stripe recommends that you use your own Creditor ID to both reduce dispute rates and improve your customer experience. You can configure your own Creditor ID on the Payment Method Settings page. When using your own Creditor ID your name will appear on statements instead of Stripe’s and you can use the Stripe statement descriptor for per-payment customization.

[Payment Method Settings](https://dashboard.stripe.com/settings/payment_methods)

[Stripe statement descriptor](/get-started/account/statement-descriptors)

After you’ve collected live SEPA Direct Debit payments on your account, you can’t change your Creditor ID in the dashboard. If you need help with this issue, contact Stripe support for information about migrating to a new Creditor ID.

[Stripe support](https://support.stripe.com/contact)

## Failed payments

SEPA Debit payment failures can occur for a number of reasons, such as a customer’s account being frozen or having insufficient funds.

When a payment fails, Stripe provides a failure reason in the failure_code field on the Charge. Stripe also provides an extended description in the failure_message field on the Charge.

The following table lists the possible SEPA Debit payment failure codes with recommended next steps.

[https://stripe.com/support](https://stripe.com/support)

## Disputed payments

SEPA Direct Debit provides a dispute process for customers to dispute payments.

Customers can dispute a payment through their bank on a “no questions asked” basis up to eight weeks after their account is debited. Any disputes within this period are automatically honored.

After eight weeks and up to 13 months, a customer can only dispute a payment with their bank if the debit is considered unauthorized. If this occurs, we automatically provide the bank with the mandate that the customer approved. This does not guarantee cancellation of the dispute; the bank can still decide that the debit was unauthorized and the customer is entitled to a refund.

A dispute can also occur if the bank is unable to debit the customer’s account because of an issue (for example, the account is frozen or has insufficient funds), but has already provided the funds to make the charge successful. If this occurs, the bank reclaims the funds in the form of a dispute.

When a dispute is created, a charge.dispute.created webhook event is sent and Stripe deducts the dispute amount and dispute fee from your Stripe balance. The dispute fee varies based on your account’s default settlement currency:

[webhook](/webhooks)

Unlike credit card disputes, SEPA Direct Debit disputes are final and there is no process for appeal. If a customer successfully disputes a payment, you must contact them if you want to resolve the situation. If you’re able to come to an arrangement and your customer is willing to return the funds to you, they must make a new payment.

[credit card disputes](/disputes)

In general, each dispute includes the reason for its creation, but this varies from country to country. For example, disputed payments in Germany do not provide additional information for privacy reasons.

If a payment is disputed, and that payment is associated with a multi-use mandate, that mandate could be deactivated. Make sure to check the status of such mandates after a dispute. You have to recollect mandate acceptance from your customers if their previous mandate is deactivated.

## Payouts

SEPA Direct Debit payments are subject to a 5 business day payout timing if your current payout timing is less than 5 business days or 7 calendar days. When you reach 35,000 USD of SEPA Direct Debit processing volume, payout timing for SEPA Direct Debit payments returns to normal.

[payout timing](/payouts#standard-payout-timing)

## Refunds

Customers can dispute a payment with their bank even after it has been refunded, resulting in two credits for the same payment. To prevent fraud, refunds may be disabled upon first refund attempt until your account has been reviewed. The review can take up to 2 business days. If you need assistance processing a refund please contact us via support.stripe.com/contact for further information.

[support.stripe.com/contact](https://support.stripe.com/contact/)

For accounts with refunds enabled, Stripe recommends issuing refunds on SEPA Direct Debit payments only when:

- It is a trusted and verified customer

- You have confirmed with the customer that you’re refunding the payment

- 7 business days have passed since you initiated the payment

Refunds for payments made with SEPA Direct Debit must be submitted within 180 days from the date of the original payment. Refunds require additional time to process (typically three to four business days). If you accidentally debit your customer, please contact them immediately to avoid a payment dispute.

SEPA does not explicitly label refunds when the funds are deposited back to a customer’s bank account. Instead, refunds are processed as a credit and include a visible reference to the original payment’s statement descriptor.

When issuing a refund, you should inform your customer immediately that the refund can take up to five business days to arrive in their bank account.
