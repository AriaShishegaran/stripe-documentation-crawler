# Refund and cancel payments

You can cancel a payment before it’s completed at no cost. Or you can refund all or part of a payment after it succeeds, which might incur a fee.

[cancel a payment](#cancel-payment)

[incur a fee](#cost-optimization)

Refunds use your available Stripe balance (not including pending amounts). If your available balance doesn’t cover the amount of the refund, Stripe debits the remaining amount from your bank account or holds the refund as pending until you top up your account balance.

## Refund requests

We submit refund requests to your customer’s bank or card issuer. Successful refunds appear on the bank statement of your customers in real time, depending on the card network and issuing bank. Disputes and chargebacks aren’t possible on credit card charges that are fully refunded.

If all of the following conditions apply, we send an email to your customer notifying them of the refund:

- The original charge was created on a customer in your Stripe account.

- The customer has a stored email address.

- You enabled Email customers for refunds in the Dashboard.

[Dashboard](https://dashboard.stripe.com/account/emails)

You can view your refunded payments in the Dashboard.

[view your refunded payments in the Dashboard](https://dashboard.stripe.com/test/payments?status%5B0%5D=refunded&status%5B1%5D=refund_pending&status%5B2%5D=partially_refunded)

## Issue refunds

You can issue refunds by using the Refunds API or the Dashboard. You can issue more than one refund against a charge, but you can’t refund a total greater than the original charge amount.

[Refunds API](/api/refunds)

[Dashboard](https://dashboard.stripe.com/test/payments)

To refund a payment using the Dashboard:

- Find the payment you want to refund in the Payments page.

[Payments](https://dashboard.stripe.com/payments)

- Click the overflow menu () to the right of the payment, then select Refund payment.

- By default, you’ll issue a full refund. For a partial refund, enter a different refund amount.

- Select a reason for the refund. If you select Other, you must add a note that explains the reason for the refund. Click Refund.

Alternatively, you can click on a specific payment and issue a refund from its details page. You can also send refund receipts automatically or manually send a receipt for each refund.

[refund receipts](/receipts#refund-receipts)

The Dashboard supports the bulk refunding of full payments. Select what payments you want to refund by checking the box to the left of each payment—even over multiple pages of results. Then, click Refund and select a reason. You can only issue full refunds in this way; partial refunds must be issued individually.

## Refund destinations

Refunds can only be sent back to the original payment method used in a charge. You can’t send a refund to a different destination, such as another card or bank account.

Refunds to expired or canceled cards are handled by the customer’s card issuer and, in most cases, credited to the customer’s replacement card. If no replacement exists, the card issuer usually delivers the refund to the customer using an alternate method (for example, check or bank account deposit). In rare cases, a refund back to a card might fail.

[fail](#failed-refunds)

For other payment methods, like ACH and iDEAL, refund handling varies from bank to bank. If a customer has closed their method of payment, the bank might return the refund to us—at which point it’s marked as failed.

[ACH](/payments/ach-debit)

[iDEAL](/payments/ideal)

[failed](#failed-refunds)

## Handle failed refunds

A refund can fail if the customer’s bank or card issuer can’t process it. For example, a closed bank account or a problem with the card can cause a refund to fail. When this happens, the bank returns the refunded amount to us and we add it back to your Stripe account balance. This process can take up to 30 days from the post date.

When using the API, a Refund object’s status transitions to failed and includes these attributes:

[Refund](/api#refund_object)

- failure_balance_transaction: The ID of the balance transaction representing the amount returned to your Stripe balance.

[balance transaction](/api#balance_transaction_object)

- failure_reason: The reason why the refund failed. These reasons include:Failure reasonDescriptioncharge_for_pending_refund_disputedA customer disputed the charge while the refund is pending. In this case, we recommend accepting or challenging the dispute instead of refunding to avoid duplicate reimbursements to the customer.declinedRefund declined by our financial partners.expired_or_canceled_cardPayment method is canceled by a customer or expired by the partner.insufficient_fundsRefund is pending due to insufficient funds and has crossed the pending refund expiry window.lost_or_stolen_cardRefund has failed due to loss or theft of the original card.merchant_requestRefund failed upon the business’s request.unknownRefund has failed due to an unknown reason.

[accepting or challenging](/disputes/responding#decide)

In the rare instance that a refund fails, we notify you using the charge.refund.updated webhook event (see all refund-related events). You’ll then need to arrange an alternative way of providing your customer with a refund.

[webhook](/webhooks)

[all refund-related events](#refund-webhook-events)

## Cancel a refund

Depending on the type of refund, you might be able to cancel a refund before it reaches the customer. Some card refunds support cancellation for a short period of time. The refund must not have been processed as a charge reversal. Only Dashboard cancellations are currently supported for card refunds.

For some payment methods, Stripe reaches out to the customer to collect banking information before processing the refund. You can cancel these refunds while banking information hasn’t been collected. Both the API and Dashboard cancellations are supported for this type of refund.

[payment methods](/payments/bank-transfers#refunds)

Canceled refunds transit to a canceled status. As cancellations are a type of refund failure, the attributes failure_reason and failure_balance_transaction are included on the Refund.

[Refund](/api#refund_object)

To cancel a refund using the Dashboard:

- Find the payment associated with the refund in the Payments page.

[Payments](https://dashboard.stripe.com/payments)

- Click the overflow menu () to the right of the payment, then select Cancel refund.

- If there are multiple partial refunds, select the correct refund in the dropdown.

- Confirm the refund cancellation by selecting Yes, cancel refund.

Alternatively, you can click a specific payment and cancel the refund from its details page.

## Refund and reversal

Some refunds—those issued shortly after the original charge—appear in the form of a reversal instead of a refund. In the case of a reversal, the original charge drops off the customer’s statement, and a separate credit isn’t issued.

IC+ users might see a difference in cost between reversals and refunds because reversals usually incur lower network fees.

[IC+](https://support.stripe.com/questions/understanding-blended-interchange-pricing)

To verify if a refund goes through as a reversal on the Dashboard:

- Open the payment details page of the payment associated with the refund.

- In the Timeline, click View Details on the refund entry.

- If it’s a reversal, a corresponding message displays.

## Trace a refund

After you initiate a refund, Stripe submits refund requests to your customer’s bank or card issuer. Your customer sees the refund as a credit approximately 5-10 business days later, depending upon the bank. A customer might contact you if they don’t see the refund. A refund might not be visible to the customer for several reasons:

- Refunds issued shortly after the original charge appear in the form of a reversal instead of a refund. In the case of a reversal, the original charge drops off the customer’s statement, and a separate credit isn’t issued.

- Refunds can fail if the customer’s bank or card issuer has been unable to process it correctly. The bank returns the refunded amount to us and we add it back to your Stripe account balance. This process can take up to 30 days from requesting the refund.

If a customer is asking about a refund, it can be helpful to give them the primary reference number corresponding to the refund. For card refunds, it can be an Acquirer Reference Number (ARN), System Trace Audit Number (STAN), or Retrieval Reference Number (RRN). An ARN, STAN, or RRN is a reference number assigned to a card transaction as it moves through the payment flow. For local payment method refunds, it can be a reference number generated by Stripe or our financial partners which is propagated to the beneficiary banks or institutions. Your customer can then take this reference to their bank, which can provide more information about when the refund is available. Having a reference number can also increase your customer’s confidence that the refund has been initiated.

Refund references are available under the following conditions:

- They’re supported for some financial partners, and marked as unavailable otherwise.

- It takes up to 7 business days after initiating the refund to receive the ARN from downstream banking partners.

- An ARN isn’t available in the case of a reversal, since the original charge isn’t processed. For card networks that don’t support ARNs, we attempt to provide other references such as System Trace Audit Number (STAN) or Retrieval Reference Number (RRN).

To find the reference of a refund using the Dashboard:

- Open the payment details page of the payment associated with the refund.

- In the Timeline, click View Details on the refund entry.

- Where available, Stripe shows the ARN or STAN on the clipboard.

## Cancel a payment

You can cancel a payment using the Dashboard only when its status is uncaptured. To cancel a payment with other statuses, you must use the API.

To cancel uncaptured payments using the Dashboard:

- Find the payment you want to cancel in the Payments page.

[Payments](https://dashboard.stripe.com/payments)

- Click the overflow menu () to the right of the payment, then select Cancel payment.

- Select a reason for canceling, and click Yes. If you select Other, you must add a note that explains the reason for canceling the payment.

## Refund webhook events

Stripe triggers events every time a refund is created or changed. Some other actions, like reviews closing, also trigger events that are relevant to refunds.

[events](/api/events#events)

Make sure that your integration is set up to handle webhook events. You should also build internal logic for notifying customers or your team about the state of the refund process. At a minimum, Stripe recommends that you listen for the charge.refunded event.

[handle webhook events](/payments/handling-payment-events)

The following table describes the most common events related to refunds.

[partially refunded payments](/disputes/best-practices#partial-refund-bp)

[refunds failing](#failed-refunds)

[ARN as a reference number to trace refunds](#tracing-refunds)

[review](/api/events/types#review_object)

## Cost optimization

Depending on the payment method used, you might incur fees to refund a charge (for example, a full or partial refund of a bank transfer). Check our pricing page for more information. Additionally, Stripe doesn’t return processing fees from the original transaction if it’s refunded.

[pricing page](https://stripe.com/pricing)

If your business processes a large volume of refunds close to the time of transaction, we recommend using manual authorization and capture to optimize your refund costs. Manual authorization and capture lets you better control costs by canceling payments before they are captured, or by reducing your captured amount rather than processing a refund.

[manual authorization and capture](/payments/place-a-hold-on-a-payment-method)

## See also

- Add funds to your Stripe balance

[Add funds to your Stripe balance](/get-started/account/add-funds)

- Add funds to your platform balance

[Add funds to your platform balance](/connect/top-ups)

- Currency conversion

[Currency conversion](/currencies/conversions)
