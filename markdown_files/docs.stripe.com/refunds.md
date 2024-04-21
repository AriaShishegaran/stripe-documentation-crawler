htmlRefund and cancel payments | Stripe Documentation[Skip to content](#main-content)Refund and cancel payments[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frefunds)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frefunds)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)
[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[After the payment](/docs/payments/after-the-payment)# Refund and cancel payments

Learn how to cancel or refund a payment.You can cancel a payment before it’s completed at no cost. Or you can refund all or part of a payment after it succeeds, which might incur a fee.

Refunds use your available Stripe balance (not including pending amounts). If your available balance doesn’t cover the amount of the refund, Stripe debits the remaining amount from your bank account or holds the refund as pending until you top up your account balance.

## Refund requests

We submit refund requests to your customer’s bank or card issuer. Successful refunds appear on the bank statement of your customers in real time, depending on the card network and issuing bank. Disputes and chargebacks aren’t possible on credit card charges that are fully refunded.

If all of the following conditions apply, we send an email to your customer notifying them of the refund:

- The original charge was created on a customer in your Stripe account.
- The customer has a stored email address.
- You enabledEmail customers for refundsin the[Dashboard](https://dashboard.stripe.com/account/emails).

You can view your refunded payments in the Dashboard.

## Issue refunds

You can issue refunds by using the Refunds API or the Dashboard. You can issue more than one refund against a charge, but you can’t refund a total greater than the original charge amount.

DashboardAPITo refund a payment using the Dashboard:

1. Find the payment you want to refund in the[Payments](https://dashboard.stripe.com/payments)page.
2. Click the overflow menu () to the right of the payment, then selectRefund payment.
3. By default, you’ll issue a full refund. For a partial refund, enter a different refund amount.
4. Select a reason for the refund. If you selectOther, you must add a note that explains the reason for the refund. ClickRefund.

Alternatively, you can click on a specific payment and issue a refund from its details page. You can also send refund receipts automatically or manually send a receipt for each refund.

Bulk refundsThe Dashboard supports the bulk refunding of full payments. Select what payments you want to refund by checking the box to the left of each payment—even over multiple pages of results. Then, click Refund and select a reason. You can only issue full refunds in this way; partial refunds must be issued individually.

## Refund destinations

Refunds can only be sent back to the original payment method used in a charge. You can’t send a refund to a different destination, such as another card or bank account.

Refunds to expired or canceled cards are handled by the customer’s card issuer and, in most cases, credited to the customer’s replacement card. If no replacement exists, the card issuer usually delivers the refund to the customer using an alternate method (for example, check or bank account deposit). In rare cases, a refund back to a card might fail.

For other payment methods, like ACH and iDEAL, refund handling varies from bank to bank. If a customer has closed their method of payment, the bank might return the refund to us—at which point it’s marked as failed.

## Handle failed refunds

A refund can fail if the customer’s bank or card issuer can’t process it. For example, a closed bank account or a problem with the card can cause a refund to fail. When this happens, the bank returns the refunded amount to us and we add it back to your Stripe account balance. This process can take up to 30 days from the post date.

When using the API, a Refund object’s status transitions to failed and includes these attributes:

- `failure_balance_transaction`: The ID of the[balance transaction](/api#balance_transaction_object)representing the amount returned to your Stripe balance.
- `failure_reason`: The reason why the refund failed. These reasons include:Failure reasonDescription`charge_for_pending_refund_disputed`A customer disputed the charge while the refund is pending. In this case, we recommend[accepting or challenging](/disputes/responding#decide)the dispute instead of refunding to avoid duplicate reimbursements to the customer.`declined`Refund declined by our financial partners.`expired_or_canceled_card`Payment method is canceled by a customer or expired by the partner.`insufficient_funds`Refund is pending due to insufficient funds and has crossed the pending refund expiry window.`lost_or_stolen_card`Refund has failed due to loss or theft of the original card.`merchant_request`Refund failed upon the business’s request.`unknown`Refund has failed due to an unknown reason.

In the rare instance that a refund fails, we notify you using the charge.refund.updated webhook event (see all refund-related events). You’ll then need to arrange an alternative way of providing your customer with a refund.

## Cancel a refund

Depending on the type of refund, you might be able to cancel a refund before it reaches the customer. Some card refunds support cancellation for a short period of time. The refund must not have been processed as a charge reversal. Only Dashboard cancellations are currently supported for card refunds.

For some payment methods, Stripe reaches out to the customer to collect banking information before processing the refund. You can cancel these refunds while banking information hasn’t been collected. Both the API and Dashboard cancellations are supported for this type of refund.

Canceled refunds transit to a canceled status. As cancellations are a type of refund failure, the attributes failure_reason and failure_balance_transaction are included on the Refund.

DashboardAPITo cancel a refund using the Dashboard:

1. Find the payment associated with the refund in the[Payments](https://dashboard.stripe.com/payments)page.
2. Click the overflow menu () to the right of the payment, then selectCancel refund.
3. If there are multiple partial refunds, select the correct refund in the dropdown.
4. Confirm the refund cancellation by selectingYes, cancel refund.

Alternatively, you can click a specific payment and cancel the refund from its details page.

## Refund and reversal

Some refunds—those issued shortly after the original charge—appear in the form of a reversal instead of a refund. In the case of a reversal, the original charge drops off the customer’s statement, and a separate credit isn’t issued.

IC+ users might see a difference in cost between reversals and refunds because reversals usually incur lower network fees.

DashboardAPITo verify if a refund goes through as a reversal on the Dashboard:

1. Open the payment details page of the payment associated with the refund.
2. In the Timeline, clickView Detailson the refund entry.
3. If it’s a reversal, a corresponding message displays.

## Trace a refund

After you initiate a refund, Stripe submits refund requests to your customer’s bank or card issuer. Your customer sees the refund as a credit approximately 5-10 business days later, depending upon the bank. A customer might contact you if they don’t see the refund. A refund might not be visible to the customer for several reasons:

- Refunds issued shortly after the original charge appear in the form of a reversal instead of a refund. In the case of a reversal, the original charge drops off the customer’s statement, and a separate credit isn’t issued.
- Refunds can fail if the customer’s bank or card issuer has been unable to process it correctly. The bank returns the refunded amount to us and we add it back to your Stripe account balance. This process can take up to 30 days from requesting the refund.

If a customer is asking about a refund, it can be helpful to give them the primary reference number corresponding to the refund. For card refunds, it can be an Acquirer Reference Number (ARN), System Trace Audit Number (STAN), or Retrieval Reference Number (RRN). An ARN, STAN, or RRN is a reference number assigned to a card transaction as it moves through the payment flow. For local payment method refunds, it can be a reference number generated by Stripe or our financial partners which is propagated to the beneficiary banks or institutions. Your customer can then take this reference to their bank, which can provide more information about when the refund is available. Having a reference number can also increase your customer’s confidence that the refund has been initiated.

Refund references are available under the following conditions:

- They’re supported for some financial partners, and marked as unavailable otherwise.
- It takes up to 7 business days after initiating the refund to receive the ARN from downstream banking partners.
- An ARN isn’t available in the case of a reversal, since the original charge isn’t processed. For card networks that don’t support ARNs, we attempt to provide other references such as System Trace Audit Number (STAN) or Retrieval Reference Number (RRN).

DashboardAPITo find the reference of a refund using the Dashboard:

1. Open the payment details page of the payment associated with the refund.
2. In the Timeline, clickView Detailson the refund entry.
3. Where available, Stripe shows the ARN or STAN on the clipboard.

## Cancel a payment

You can cancel a payment using the Dashboard only when its status is uncaptured. To cancel a payment with other statuses, you must use the API.

DashboardAPITo cancel uncaptured payments using the Dashboard:

1. Find the payment you want to cancel in the[Payments](https://dashboard.stripe.com/payments)page.
2. Click the overflow menu () to the right of the payment, then selectCancel payment.
3. Select a reason for canceling, and clickYes. If you selectOther, you must add a note that explains the reason for canceling the payment.

## Refund webhook events

Stripe triggers events every time a refund is created or changed. Some other actions, like reviews closing, also trigger events that are relevant to refunds.

Make sure that your integration is set up to handle webhook events. You should also build internal logic for notifying customers or your team about the state of the refund process. At a minimum, Stripe recommends that you listen for the charge.refunded event.

The following table describes the most common events related to refunds.

EventDescription`charge.dispute.funds_reinstated`Sent when funds are reinstated to your account after a dispute is closed, including[partially refunded payments](/disputes/best-practices#partial-refund-bp).`charge.refund.updated`Sent when the refund is updated. Updates include adding metadata,[refunds failing](#failed-refunds), and providing details like the[ARN as a reference number to trace refunds](#tracing-refunds).`charge.refunded`Sent when a charge is refunded, including partial refunds.`refund.created`Sent when a refund from a customer’s cash balance is created. Stripe only sends this in rare cases. For most use cases, listen for`charge.refunded`to know when a refund is complete.`refund.updated`Sent for refunds without a corresponding charge, like a cash balance refund.`review.closed`Sent when a[review](/api/events/types#review_object)is closed. See the`reason`field to understand why it was closed, one of:`approved`,`disputed`,`refunded`, or`refunded_as_fraud`.`source.refund_attributes_required`DeprecatedSent when the refund attributes are required on a receiver source to process a refund or a mispayment.## Cost optimization

Depending on the payment method used, you might incur fees to refund a charge (for example, a full or partial refund of a bank transfer). Check our pricing page for more information. Additionally, Stripe doesn’t return processing fees from the original transaction if it’s refunded.

If your business processes a large volume of refunds close to the time of transaction, we recommend using manual authorization and capture to optimize your refund costs. Manual authorization and capture lets you better control costs by canceling payments before they are captured, or by reducing your captured amount rather than processing a refund.

## See also

- [Add funds to your Stripe balance](/get-started/account/add-funds)
- [Add funds to your platform balance](/connect/top-ups)
- [Currency conversion](/currencies/conversions)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Refund requests](#refund-requests)[Issue refunds](#issuing)[Refund destinations](#destination)[Handle failed refunds](#failed-refunds)[Cancel a refund](#cancel-refund)[Refund and reversal](#refund-and-reversal)[Trace a refund](#tracing-refunds)[Cancel a payment](#cancel-payment)[Refund webhook events](#refund-webhook-events)[Cost optimization](#cost-optimization)[See also](#see-also)Related Guides[Bank transfer refunds](/docs/payments/bank-transfers#refunds)[Currency conversion of disputes and refunds](/docs/currencies/conversions#conversions-disputes-refunds)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`