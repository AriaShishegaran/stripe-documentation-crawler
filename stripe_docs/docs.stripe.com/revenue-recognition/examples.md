# Revenue Recognition examples

After reading the Revenue Recognition overview and methodology pages, use what you learned to review the examples below. Unless stated otherwise, the examples assume that revenue recognition takes place on a per-day basis. Stripe’s tooling recognizes revenue every millisecond but using a daily increment simplifies the calculations.

[overview](/revenue-recognition)

[methodology](/revenue-recognition/methodology)

## Monthly subscription

This example uses the following assumptions:

- On January 15th, at 00:00:00 UTC, a customer starts a monthly subscription that costs 31 USD.

- The subscription generates an invoice.

[invoice](/api/invoices)

- The invoice finalizes and the customer pays 31 USD.

In this example, the invoice and revenue periods are from January 15, 2019 to February 14, 2019. The 31 USD is recognized across 17 days in January and 14 days in February. If you looked at the summary after January ends, you might see something like:

This means that recognized revenue increased by 17 USD for the days in January, and deferred revenue increased by 14 USD for revenue you expect to recognize in February.

## Annual subscription

This example uses the following assumptions:

- On January 1st, at 00:00:00 UTC, a customer starts an annual subscription that costs 365 USD.

- The subscription generates an invoice.

- The invoice finalizes and the customer pays 365 USD.

In this example, the invoice and revenue periods are from 1/1/2019 to 12/31/2019. The 365 USD is recognized daily throughout the year. If you looked at the summary after March ends, you might see something like:

## Monthly metered subscription

There are four types of aggregate_usage, each of which has a different implication on how revenue is recognized.

[aggregate_usage](/api/prices/create#create_price-recurring-aggregate_usage)

This example uses the following assumptions:

- On January 15, a customer subscribes to a monthly metered subscription at 1 USD per unit, and with aggregate_usage=sum.

[metered](/products-prices/pricing-models#usage-based-pricing)

- On January 25, they use 15 units.

- On February 4, they use another 17 units.

- On February 14, the subscription generates an invoice of 32 USD.

- The invoice finalizes for 32 USD, but isn’t paid yet.

In this example, the invoice and revenue periods are from January 15, 2019 to February 14, 2019. Although the invoice isn’t generated until February 14, the 15 USD from January 25 still has to be recognized when the usage was reported. If you looked at the summary after January ends, you might see something like:

If you looked at the summary after February ends and the invoice is yet to be paid, you might see something like:

This example uses the following assumptions:

- On January 15, a customer subscribes to a monthly metered subscription at 1 USD per unit, and with aggregate_usage=max.

[metered](/products-prices/pricing-models#usage-based-pricing)

- On January 25, they use 17 units.

- On February 4, they use another 15 units.

- On February 14, the subscription generates an invoice of 17 USD.

In this example, the invoice and revenue periods are from January 15, 2019 to February 14, 2019. If you looked at the summary after January ends, you might see something like:

If you looked at the summary after February ends and the invoice is yet to be paid, you might see something like:

It’s important to note that the 15 units recorded on February 4 don’t impact revenue recognition because they’re not the max usage record.

This example uses the following assumptions:

- On January 15, a customer subscribes to a monthly metered subscription at 1 USD per unit, and with aggregate_usage=last_during_period.

[metered](/products-prices/pricing-models#usage-based-pricing)

- On January 25, they use 17 units.

- On January 27, they use 10 units.

- On February 4, they use another 15 units.

- On February 14, the subscription generates an invoice of 15 USD.

In this example, the invoice and revenue periods are from January 15, 2019 to February 14, 2019. If you looked at the summary after January ends, you might see something like:

Please note that the 17 units recorded on January 25 doesn’t have any impact on revenue recognition because it is not the last usage record during the period at the end of Jan.

If you looked at the summary after February ends and the invoice is yet to be paid, you might see something like:

Please note that the 17 units recorded on January 25 and 10 units recorded on January 27 don’t have any impact on revenue recognition because they aren’t the last usage during the period.

This example uses the following assumptions:

- On January 15, a customer subscribes to a monthly metered subscription at 1 USD per unit, and with aggregate_usage=last_ever.

[metered](/products-prices/pricing-models#usage-based-pricing)

- On January 25, they use 17 units.

- On January 27, they use 10 units.

- On February 4, they use another 15 units.

- On February 8, they use another 18 units.

- On February 14, the subscription generates an invoice of 18 USD.

- On March 14, the subscription generates another invoice of 18 USD.

In this example, the invoice and revenue periods are from January 15, 2019 to February 14, 2019. If you looked at the summary after January ends, you might see something like:

Please note that the 10 units recorded on January 25 doesn’t have any impact on revenue recognition because it is not the last usage record at the end of Jan.

If you looked at the summary after February ends, you might see something like:

Now in the period of February 14 to March 14, since there’s no usage record within the period, we recognize 18 USD when the invoice happens. If you looked at the summary after March ends, you might see something like:

## Upgrade

This example uses the following assumptions:

- On April 1st, at 00:00 UTC, a customer starts a monthly subscription that costs 90 USD.

- The subscription generates an invoice.

- The invoice finalizes on April 1st and the customer pays 90 USD.

- On April 21st at 00:00 UTC, they upgrade to a monthly subscription that costs 120 USD.2 unbilled invoice items are created to represent (1) -30 USD for the unused time of the previous plan and (2) 40 USD for the remaining time of the new plan.

- 2 unbilled invoice items are created to represent (1) -30 USD for the unused time of the previous plan and (2) 40 USD for the remaining time of the new plan.

- The next invoice includes the 2 unbilled invoice items and is finalized on May 1st, at 00:00:00 UTC with 3 line items:-30 USD for the unused time of the previous plan with the service period from April 21st at 00:00 UTC to May 1st at 00:00 UTC.40 USD for the remaining time of the new plan with the service period from April 21st at 00:00 UTC to May 1st at 00:00 UTC.120 USD for the service in May with the service period from May 1st at 00:00 UTC to June 1st at 00:00 UTC.

- -30 USD for the unused time of the previous plan with the service period from April 21st at 00:00 UTC to May 1st at 00:00 UTC.

- 40 USD for the remaining time of the new plan with the service period from April 21st at 00:00 UTC to May 1st at 00:00 UTC.

- 120 USD for the service in May with the service period from May 1st at 00:00 UTC to June 1st at 00:00 UTC.

If you looked at the summary after May ends, you might see something like:

## Downgrade

This example uses the following assumptions:

- On April 1st, at 00:00 UTC, a customer starts a monthly subscription that costs 90 USD.

- The subscription generates an invoice.

- The invoice finalizes on April 1st and the customer pays 90 USD.

- On April 21st at 00:00 UTC, they downgrade to a monthly subscription that costs 30 USD.2 unbilled invoice items are created to represent (1) -30 USD for the unused time of the previous plan and (2) 10 USD for the remaining time of the new plan.

- 2 unbilled invoice items are created to represent (1) -30 USD for the unused time of the previous plan and (2) 10 USD for the remaining time of the new plan.

- The next invoice includes the 2 unbilled invoice items and is finalized on May 1st, at 00:00:00 UTC with 3 line items:-30 USD for the unused time of the previous plan with the service period from April 21st at 00:00 UTC to May 1st at 00:00 UTC.10 USD for the remaining time of the new plan with the service period from April 21st at 00:00 UTC to May 1st at 00:00 UTC.30 USD for the service in May with the service period from May 1st at 00:00 UTC to June 1st at 00:00 UTC.

- -30 USD for the unused time of the previous plan with the service period from April 21st at 00:00 UTC to May 1st at 00:00 UTC.

- 10 USD for the remaining time of the new plan with the service period from April 21st at 00:00 UTC to May 1st at 00:00 UTC.

- 30 USD for the service in May with the service period from May 1st at 00:00 UTC to June 1st at 00:00 UTC.

If you looked at the summary after May ends, you might see something like:

## Customer credit balance

This example uses the following assumptions:

- On January 15th, at 00:00:00 UTC, a customer starts a monthly subscription that costs 31 USD.

- The subscription generates an invoice.

- The invoice finalizes on January 15th, at 00:00:00 UTC.

- The customer has -11 USD in its customer credit balance. Stripe automatically applies -11 USD to the invoice and adjusts the customer credit balance to 0 USD.

- The customer pays 20 USD on February 9th.

In this example, the invoice and revenue periods are from 1/15/2019 to 2/14/2019. The 31 USD is recognized across 17 days in January and 14 days in February. If you looked at the summary after January ends, you might see something like:

In this scenario, the customer has an existing customer credit balance that’s used to pay the invoice. It’s also possible for a negative amount on an invoice to credit the customer credit balance, which is then used to pay the invoice. This often happens when a customer downgrades to a cheaper subscription. For example, assume that:

- A -31 USD invoice with one invoice line item finalizes on January 15th, at 00:00:00 UTC.

- The service period for the -31 USD invoice line item is from January 15th 00:00:00 UTC to February 15th 00:00:00 UTC.

- Stripe automatically credits 31 USD to the customer credit balance and closes the invoice.

The -31 USD line item books a journal entry that debits DeferredRevenue and credits AccountsReceivable. When Stripe credits the customer credit balance, it books another journal entry that debits AccountsReceivable and credits CustomerBalance. In the summary at the end of January, you might see something like:

Notice that eventually the net revenue is -31 USD.

## Refund

This example uses the following assumptions:

- On January 1st, at 00:00:00 UTC, a customer starts a three month subscription that costs 90 USD.

- The subscription generates an invoice.

- The invoice finalizes and the customer pays 90 USD.

- On February 1st, they receive a full refund.

When you make a full refund:

- The customer receives cash.

- Recognized revenue is offset by contra revenue in the refunds account.

- Deferred revenue from the subscription that hasn’t been recognized is cleared.

In this example, the customer received one month of service, so they receive a 31 USD refund. The refund also decreases the cash balance in your Stripe account by 90 USD. At the time of the refund, there was 59 USD remaining in deferred revenue, so this is also cleared. If you viewed the summary after March ends, it might look something like this:

## Partial refund

This example uses the following assumptions:

- On January 1st, at 00:00:00 UTC, a customer starts a three month subscription that costs 90 USD.

- The subscription generates an invoice.

- The invoice finalizes and the customer pays 90 USD.

- On February 1st, they receive a partial refund of 9 USD.

When the partial refund is made:

- The customer receives 9 USD.

- Recognized revenue is proportionally offset by contra revenue in the refunds account.

- Deferred revenue from the subscription that hasn’t been recognized is also proportionally reduced.

In this example, the customer received one month of service, so 31 USD has been recognized. There is 59 USD remaining in deferred revenue. The partial refund of 9 USD is 10% of 90 USD. Therefore, the refunds account (part of contra revenue) is increased by 3.10 USD (10% of 31 USD), and deferred revenue is decreased by 5.90 USD (10% of 59 USD). If you viewed the summary after March ends, it might look something like this:

## Void

This example uses the following assumptions:

- On January 1st, at 00:00:00 UTC, a customer starts a three month subscription that costs 90 USD.

- The subscription generates an invoice.

- The invoice finalizes, but the customer hasn’t paid yet.

- On February 1st, you void the invoice.

When you void the invoice:

- The accounts receivable account is cleared because we don’t expect to get paid.

- Recognized revenue is offset by contra revenue in the voids account.

- Deferred revenue from the subscription that hasn’t been recognized is cleared.

In this example, the customer received one month of service, so 31 USD in recognized revenue is voided. At the time of the invoice being voided, there was 59 USD remaining in deferred revenue, so this is also cleared. If you viewed the summary after March ends, it might look something like this:

## Uncollectible

This example uses the following assumptions:

- On January 1st, at 00:00:00 UTC, a customer starts a three month subscription that costs 90 USD.

- The subscription generates an invoice.

- The invoice finalizes, but the customer hasn’t paid yet.

- On February 1st, the invoice is marked as uncollectible.

When the invoice is marked as uncollectible:

- The accounts receivable account is cleared because we don’t expect to get paid.

- Recognized revenue is offset by contra revenue in the bad debt account.

- Deferred revenue from the subscription that hasn’t been recognized is cleared.

In this example, the customer received one month of service, so 31 USD in recognized revenue becomes bad debt. At the time of the invoice being marked as uncollectible, there was 59 USD remaining in deferred revenue, so this is also cleared. If you viewed the summary after March ends, it might look something like this:

An uncollectible invoice might still be paid. When the invoice is paid, the bad debt account is cleared out using a part of the received cash amount. The remaining cash amount goes to the recoverables account. If the invoice is paid in April, the summary might look something like this:

An uncollectible invoice may still be voided. When the invoice is voided, the bad debt account is cleared out and the contents are moved into the void account. If the invoice is voided in April, the summary might look something like this:

## Uncollectible invoice with applied customer credit balance

This example uses the following assumptions:

- On January 15th at 00:00:00 UTC, a customer starts a monthly subscription that costs 31 USD.

- The subscription generates an invoice.

- The invoice finalizes on January 15th at 00:00:00 UTC.

- The customer’s credit balance is -11 USD. Stripe automatically applies -11 USD to the invoice and adjusts the credit balance accordingly.

- On February 15th, the invoice is marked as uncollectible.

In this example, the invoice and revenue periods are from January 15, 2019 to February 14, 2019. Stripe recognizes the 31 USD across 17 days in January and 14 days in February.

Stripe automatically offsets recognized revenue with the bad debt account if an invoice is set as uncollectible. With the customer’s 11 USD credit balance, Stripe considers 6 USD (11 x 17 / 31) as recognized revenue and 5 USD  (11 x 14 / 31) as deferred revenue. The portion of paid deferred revenue is considered as a gain and booked in the recoverables account.

The summary after February end might look something like:

As another example, you can increase the customer’s invoice due amount when there’s an outstanding balance (that is, they owe some amount to you). Consider the following:

- A 31 USD invoice with one invoice line item finalizes on January 15th at 00:00:00 UTC.

- The service period for the 31 USD invoice line item is from January 15th 00:00:00 UTC to February 15th 00:00:00 UTC.

- There is a customer credit balance of 10 USD. Because of this, Stripe adds that amount to the invoice making the outstanding balance be 0 USD.This debits AccountsReceivable and credits CustomerBalance for 10 USD.

- This debits AccountsReceivable and credits CustomerBalance for 10 USD.

- Stripe marks the invoice as uncollectible on February 15th.

For an uncollectible invoice, the portion of due customer credit balance isn’t collected. Because of this, it is considered a negative gain and booked as a negative amount to the recoverables account.

The summary after February end might look something like:

## Uncollectible and disputed or refunded

An uncollectible invoice can be paid, then later disputed or refunded.

This example uses the following assumptions:

- On January 1st, at 00:00:00 UTC, a customer starts a three month subscription that costs 90 USD.

- The subscription generates an invoice.

- The invoice finalizes, but the customer hasn’t paid yet.

- On February 1st, the invoice is marked as uncollectible.

- On April 1st, the invoice is paid.

- On May 1st, the corresponding charge is disputed.

As shown in the Uncollectible example, when the invoice is marked as uncollectible and later paid:

- The bad debt account is cleared out.

- The remainder is booked as recoverables.

In this example, the customer later decides to dispute the charge. When a dispute occurs, the summary might look something like:

An invoice marked as uncollectible, paid, and later refunded works in a similar manner except that it uses the refunds account instead of the disputes account.

## Dispute

In case of a dispute, Revenue Recognition works similarly to how a refund works except that it uses the disputes account instead. This example also shows what happens if you win a dispute. It uses the following assumptions:

- On January 1st, at 00:00:00 UTC, a customer starts a three month subscription that costs 90 USD.

- The subscription generates an invoice.

- The invoice finalizes and the customer pays 90 USD.

- On February 1st, they dispute the payment.

- On April 1st, you win the dispute because the bank rules in your favor.

When the customer makes the dispute:

- Cash is returned to the customer.

- Recognized revenue is offset by contra revenue in the disputes account.

- Deferred revenue from the subscription that hasn’t been recognized is cleared.

When you win the dispute:

- Cash is returned to you.

- Recognized revenue and deferred revenue don’t change.

- Cash is offset by an increase in the recoverables account.

In this example, the customer received one month of service, so 31 USD in recognized revenue is disputed. The dispute also decreases the cash balance in your Stripe account by 90 USD. At the time of the dispute, there was 59 USD remaining in deferred revenue, so this is also cleared. Later in time, in April, the bank rules in your favor, so the cash is returned to you.

If you viewed the summary after April ends, it might look something like this:

## Credit note after a payment

You can use a refund, a customer credit, or an out-of-band credit to issue a credit note to a customer after they’ve made a payment.

For example, say a customer starts a subscription for a 3 month period on January 1 at 00:00:00 UTC that costs 90 USD. The subscription generates an invoice and the customer pays it immediately. On February 1, you issue a credit note of 45 USD where you: refund 15 USD; credit 10 USD to the customer balance; and credit 20 USD to an external customer balance (an out-of-band credit). Your summary for March would like something like this:

## Credit note without line items

This example uses the following assumptions:

- On January 1st at 00:00:00 UTC, a customer starts a 6 month subscription that costs 181 USD.

- The subscription generates an invoice.

- The invoice finalizes, but the customer hasn’t paid yet.

- On February 1st, you issue a credit note of 90.50 USD.

When the credit note is issued:

- The accounts receivable account is reduced according to the credit note’s amount.

- Recognized revenue is offset by contra revenue proportionally in the credit notes account.

- Deferred revenue from the subscription that hasn’t been recognized is reduced proportionally to the credit note’s amount.

If you viewed the summary after March ends, it might look something like this:

When the credit note is voided on May 3rd:

- Reverses the credit notes account.

- Increases accounts receivable back to the original invoice due amount.

- Recognizes the reduced revenue in May instead of February, March, and April.

- Reinstates the reduced deferred revenue in May.

The summary after June end might look something like:

Be aware that a credit note without line items doesn’t match with a specific invoice line item. Rather, the amount of the credit note is divided proportionally among the invoice line items.

## Credit note with line items

A credit note with line items would work in a similar way that a credit note without line items does except that a credit note line item is used for adjusting the revenue and other accounts for a corresponding invoice line item.

## Credit note with negative line items  Beta

Adjustments to accounts for a credit note with negative line items are the reverse of those for a credit note with positive line items.

Learn how to credit negative invoice line items in the Dashboard or programmatically with the API.

[credit negative invoice line items in the Dashboard](/invoicing/dashboard/credit-notes#negative-line-items)

[programmatically with the API](/invoicing/integration/programmatic-credit-notes#negative-line-items)

To credit negative invoice line items, join Invoicing’s private beta:

[privacy policy](https://stripe.com/privacy)

## External asset

When you manually mark invoices as paid outside of Stripe, the external asset account increases. All other accounts operate as if the invoice is paid, but the cash account doesn’t change. You can import third party transaction data and consolidate all your revenue sources into your Stripe reporting by using the Data Import feature.

[Data Import feature](/revenue-recognition/data-import)

Below is an example involving the external asset account with the following assumptions:

- On January 1st, at 00:00:00 UTC, a customer starts a monthly subscription that costs 31 USD.

- The subscription generates an invoice, and the invoice finalizes on the same day.

- The invoice is manually marked as paid outside of Stripe on February 5th.

## Tax exempt

Your customers can have a tax exemption status of either exempt or reverse. No tax is calculated on the invoice in either case.

[customers](/api/customers)

[tax exemption status](/billing/taxes/tax-rates#tax-exempt-and-reverse-charge)

For example, say a customer with a tax exemption status of reverse starts a monthly subscription on January 1 at 00:00:00 UTC. It costs 31 USD per month and has a tax-inclusive rate of 10%. Because the customer is tax exempt, the total amount due is 27.90 USD. The subscription generates an invoice, the invoice finalizes, and the customer pays the invoice on the same day. Your journal entry would look like this:

## Tax-inclusive rate on invoice items

An invoice item can include a tax-inclusive rate. When you add an invoice item to an invoice, it can use the same accounting period or a different accounting period from its creation date.

For example, say a customer starts a service for a period of 1 month on January 1 at 00:00:00 UTC. The total amount due is 34.10 USD and has a tax-inclusive rate of 10%. You add the invoice item to an invoice on January 1, the invoice finalizes, and the customer pays the invoice on the same day. Your journal entry would look like this:

For example, say a customer starts a service for a 3 month period on January 1 at 00:00:00 UTC. The total amount due is 100.00 USD and has a tax-inclusive rate of 10%. You add the invoice item to an invoice on March 1, the invoice finalizes, and the customer pays the invoice on the same day. Your journal entry would look like this:

## Tax liability

Invoices and invoice line items can be assigned tax rates. When tax rates are assigned, the Revenue Recognition reports can compute tax liability.

[assigned tax rates](/invoicing/taxes/tax-rates)

Below is an example using an exclusive tax rate with the following assumptions:

- On January 1st, at 00:00:00 UTC, a customer starts a monthly subscription that costs 31 USD with an exclusive tax rate of 10%. The total due amount is 34.10 USD.

- The subscription generates an invoice.

- The invoice finalizes and is paid on the same day.

Below is an example using an inclusive tax rate with the following assumptions:

- On January 1st, at 00:00:00 UTC, a customer starts a monthly subscription that costs 31 USD with an inclusive tax rate of 10%. The total due amount is 31 USD.

- The subscription generates an invoice.

- The invoice finalizes and is paid on the same day.

## Multi-currency

This example uses the following assumptions:

- On January 1st, at 00:00:00 UTC, an invoice finalizes and the customer immediately pays 30 EUR.

- Your account’s settlement currency is USD.

- The EUR to USD exchange rate is 1.20 at the time of finalization and payment.

In this example, you receive 36 USD. Because the invoice finalizes and is paid immediately, you have no exposure to fluctuating exchange rates and therefore no foreign exchange (FX) gains or losses.

## FX loss

This example uses the following assumptions:

- On January 1st, at 00:00:00 UTC, an invoice finalizes for 30 EUR.

- On February 1st, at 00:00:00 UTC, the customer pays the invoice for 30 EUR.

- Your account’s settlement currency is USD.

- The EUR to USD exchange rate is 1.20 at the time of finalization.

- The EUR to USD exchange rate is 1.10 at the time of payment.

In this example, the exchange rate changed between invoice finalization and payment, so you receive 33 USD instead of 36.

## FX loss from a refund or dispute

This example uses the following assumptions:

- On January 1st, at 00:00:00 UTC, an invoice finalizes for 30 EUR.

- On February 1st, at 00:00:00 UTC, the customer pays the invoice for 30 EUR.

- On March 1st, at 00:00:00 UTC, a refund is issued for 30 EUR.

- Your account’s settlement currency is USD.

- The EUR to USD exchange rate is 1.20 at the time of finalization.

- The EUR to USD exchange rate is 1.20 at the time of payment.

- The EUR to USD exchange rate is 1.30 at the time of refund.

In this example, the exchange rate changed between invoice payment and refund, so you receive 36 USD but you later refund 39 USD. Therefore, you incur 3 USD for FxLoss.

A dispute works in the same way as a refund, except that it books the disputes account instead of the refunds account.

## Multiple settlement currencies

This example uses the following assumptions:

- Your account settles in USD by default but EUR is also a supported settlement currency.

- On January 1st, at 00:00:00 UTC, two invoices finalize for separate customers-one is for 30 EUR, and the other is for 400 NOK.

- The NOK to USD conversion rate is 0.10 at the time of finalization and payment.

- Both invoices are paid immediately.

In this example, you receive 40 USD from the NOK transaction and 30 EUR from the EUR transaction. Because EUR is a supported settlement currency, no exchange rate is applied.

## Fees  Beta

Revenue Recognition Stripe fees support is currently in private beta. If you’re interested in getting early access, please create a ticket on our support page.

[create a ticket](https://support.stripe.com/contact/email?topic=financial_reports)

This example uses the following assumptions:

- On January 1st, at 00:00:00 UTC, a customer starts a three month subscription that costs 90 USD.

- The subscription generates an invoice.

- The invoice finalizes and the customer pays 90 USD.

- This payment has a Stripe processing fee of 0.02 USD.

If you view the summary after March ends, you’ll see something like this:

Notice fees are booked on a cash-basis.

## Exclude transactions

Transactions behave differently when excluded, depending on whether they have been paid or not. If a transaction is paid in cash, we debit the cash account and credit the exclusion account after exclusion. If it’s paid by CustomerBalance, we debit the customer balance account and credit the customer balance adjustments account after exclusion. We don’t generate journal entries for unpaid transactions; they behave as if the transaction never occurred.

If you exclude transactions in a closed accounting period, it incurs corrections for transactions that have already been paid. Learn more about corrections.

[corrections](/revenue-recognition/reports)

This example uses the following assumptions:

- On January 5th, 2022, at 09:00:00 UTC, you create a one-time payment of 10 USD using either the Dashboard, the Charges APIs, or the Payment Intents APIs.

- By default, Revenue Recognition immediately recognizes the revenue from this one-time payment.

- On February 5th 2022, you exclude the payment.

- The accounting periods for January 2022 are either closed or open.

After you exclude the payment:

- The revenue account clears to 0 USD because the payment doesn’t generate revenue.

- The cash account remains at 10 USD, acknowledging the received payment.

- An amount of 10 USD is added to the exclusion account.

At the end of February, your summary might reflect the following:

This example uses the following assumptions:

- On January 1st 2022, at 00:00:00 UTC, a customer initiates a one-month subscription (from January 1 to Jan 31) that costs 31 USD.

- The subscription generates an invoice.

- The invoice finalizes, but the customer doesn’t make a payment.

- On February 1st 2022, you exclude the payment.

- The accounting periods are open for January 2022.

If you exclude a finalized invoice during an open accounting period, it leaves no trace of activity related to the invoice. We remove all of the account activities, excluding the cash and customer balance account that isn’t involved in this case, and don’t generate journal entries from the finalization and exclusion of the invoice.
