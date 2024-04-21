# Tax API for Sales Tax, GST, and VAT

You can integrate Stripe Tax with Payment Links, Checkout, Billing and Invoicing with no or low code setups.

[Payment Links](/tax/paymentlinks)

[Checkout](/tax/checkout)

[Billing](/tax/subscriptions)

[Invoicing](/tax/invoicing)

Stripe Tax APIs enable you to calculate tax in custom payment flows. After your customer completes their payment, record the transaction so it appears in Stripe Tax reporting. The examples in this guide use Stripe payments APIs, but you can use the Tax API with any payment processor, or multiple payment processors.

[Add registrations](#add-registrations)

## Add registrations

Stripe Tax only calculates tax in jurisdictions where you’re registered to collect tax and requires you to add your registrations in the Dashboard.

[add your registrations](/tax/registering#add-a-registration)

[OptionalCollect customer addressClient-side](#collect-address)

## OptionalCollect customer addressClient-side

[Calculate taxServer-side](#calculate-tax)

## Calculate taxServer-side

You choose when and how often to calculate tax. For example, you can:

[calculate tax](/api/tax/calculations/create)

- Show a tax estimate based on your customer’s IP address when they enter your checkout flow

[based on your customer’s IP address](#ip-address)

- Recalculate tax as your customer types their billing or shipping address

- Calculate the final tax amount to collect when your customer finishes typing their address

Stripe charges a fee per tax calculation API call. You can throttle tax calculation API calls to manage your costs.

[charges a fee](https://stripe.com/tax#pricing)

The examples below show how to calculate tax in a variety of scenarios. Stripe Tax only calculates tax in jurisdictions where you’re registered to collect tax and requires you to add your registrations in the Dashboard.

[add your registrations](/tax/registering#add-a-registration)

This example calculates tax for a US shipping address. The line item has a price of 10 USD and uses your account’s preset tax code.

[preset tax code](/tax/set-up#preset-tax-code)

The calculation response contains amounts you can display to your customer, and use to take payment:

[calculation response](/api/tax/calculations/object)

[amount_total](/api/tax/calculations/object#tax_calculation_object-amount_total)

[amount](/api/payment_intents/create#create_payment_intent-amount)

[tax_amount_exclusive](/api/tax/calculations/object#tax_calculation_object-tax_amount_exclusive)

[tax_amount_inclusive](/api/tax/calculations/object#tax_calculation_object-tax_amount_inclusive)

[tax_breakdown](/api/tax/calculations/object#tax_calculation_object-tax_breakdown)

The calculation returns the customer_tax_location_invalid error code if your customer’s address is invalid or isn’t precise enough to calculate tax:

[https://stripe.com/docs/error-codes/customer-tax-location-invalid](https://stripe.com/docs/error-codes/customer-tax-location-invalid)

When you receive this error, prompt your customer to check the address they’ve entered and fix any typos.

[Create tax transactionServer-side](#tax-transaction)

## Create tax transactionServer-side

Creating a tax transaction records the tax you’ve collected from your customer, so that later you can download exports and generate reports to help with filing your taxes. You can create a transaction from a calculation until the expires_at timestamp, 48 hours after it’s created. Attempting to use it after this time returns an error.

[download exports and generate reports](/tax/reports)

[create a transaction](/api/tax/transactions/create_from_calculation)

[expires_at](/api/tax/calculations/object#tax_calculation_object-expires_at)

When creating a tax transaction, you must provide a unique reference for the tax transaction and each line item. The references appear in tax exports to help you reconcile the tax you collected with the orders in your system.

For example, a tax transaction with reference pi_123456789, line item references L1 and L2, and a shipping cost, looks like this in the itemized tax exports:

When your customer pays, use the calculation ID to record the tax collected. Two ways to do this are:

- If your server has an endpoint where your customer submits their order, you can create the tax transaction after the order is successfully submitted.

- Listen for the payment_intent.succeeded webhook event. Retrieve the calculation ID from the PaymentIntent metadata.

[payment_intent.succeeded](/api/events/types#event_types-payment_intent.succeeded)

The example below creates a transaction and uses the PaymentIntent ID as the unique reference:

Store the tax transaction ID so that later you can record refunds. You can store the transaction ID in your database or in the PaymentIntent’s metadata:

[tax transaction ID](/api/tax/transactions/object#tax_transaction_object-id)

[Record refundsServer-side](#reversals)

## Record refundsServer-side

After creating a tax transaction to record a sale to your customer, you might need to record refunds. These are also represented as tax transactions, with type=reversal. Reversal transactions offset an earlier transaction by having amounts with opposite signs. For example, a transaction that recorded a sale for 50 USD might later have a full reversal of -50 USD.

When you issue a refund (using Stripe or outside of Stripe) you need to create a reversal tax transaction with a unique reference. Common strategies include:

- Append a suffix to the original reference. For example, if the original transaction has reference pi_123456789, then create the reversal transaction with reference pi_123456789-refund.

- Use the ID of the Stripe refund or a refund ID from your system. For example, re_3MoslRBUZ691iUZ41bsYVkOg or myRefund_456.

[Stripe refund](/api/refunds/object)

Choose the approach that works best for how you reconcile your customer orders with your tax exports.

[tax exports](/tax/reports)

When you fully refund a sale in your system, create a reversal transaction with mode=full.

In the example below, tax_1MEFAAI6rIcR421eB1YOzACZ is the tax transaction recording the sale to your customer:

This returns the full reversal transaction that’s created:

Fully reversing a transaction doesn’t affect previous partial reversals. When you record a full reversal, make sure you fully reverse any previous partial reversals for the same transaction to avoid duplicate refunds.

[fully reverse](#reversals-void-refund)

After issuing a refund to your customer, create a reversal tax transaction with mode=partial. This allows you to record a partial refund by providing the line item amounts refunded. You can create up to 10 partial reversals for each sale. Reversing more than the amount of tax you collected returns an error.

[issuing a refund](/api/refunds/create)

The example below records a refund of only the first line item in the original transaction:

This returns the partial reversal transaction that’s created:

For each line item reversed you need to provide the amount and amount_tax reversed. The amount is tax-inclusive if the original calculation line item was tax-inclusive.

How amount and amount_tax are determined depends on your situation:

- If your transactions always have a single line item, use full reversals instead.

[full reversals](#reversals-full)

- If you always refund entire line items, use the original transaction line item amount and amount_tax, but with negative signs.

- If you refund parts of line items, you need to calculate the amounts refunded. For example, for a sale transaction with amount=5000 and amount_tax=500, after refunding half the line item you’d create a partial reversal with line item amount=-2500 and amount_tax=-250.

Alternatively, you can create a reversal with mode=partial by specifying a flat after-tax amount to refund. The amount distributes across each line item and shipping cost proportionally, depending on the remaining amount left to refund on each.

In the example below, the transaction has two line items: one 10 USD item and one 20 USD item, both taxed at 10%. The total amount of the transaction is 33.00 USD. A refund for a flat 16.50 USD is recorded:

This returns the partial reversal transaction that’s created:

For each line item and shipping cost in the original transaction, the refunded amounts and tax are calculated as follows:

- First, we calculate the total remaining funds in the transaction available to refund. Because this transaction hasn’t had any other reversals recorded, the total amount is 33.00 USD.

- Next, we calculate the total amount to refund for each line item. We base this calculation on the proportion of the item’s total available amount to refund versus the total remaining amount of the transaction. For example, the 10 USD item, which has 11.00 USD total remaining to refund, represents 33.33% of the transaction’s remaining total, so the total amount to refund is -16.50 USD * 33.33% = -5.50 USD.

- Finally, the total amount to refund is divided between amount and amount_tax. We also do this proportionally, depending on how much tax is available to refund in the line item compared to the total funds left to refund. Using the 10 USD item example, tax (1.00 USD) represents 9.09% of the total remaining to refund (11.00 USD), so the amount_tax is -5.50 USD * 9.09% = -0.50 USD.

The flat amount distributes according to what’s left to refund in the transaction, not what was originally recorded. Consider this example: instead of recording a refund for a flat 16.50 USD, you first record a partial reversal for the total amount of the 10 USD item:

After this, you record a 16.50 USD flat amount reversal:

This returns the partial reversal transaction:

Because the total amount remaining in the transaction is now 22.00 USD and the 10 USD item is completely refunded, the 16.50 USD distributes entirely to the 20 USD item. The 16.50 USD then distributes, using the logic from step 3, into amount = -15.00 USD and amount_tax = -1.50 USD. Meanwhile, the 10 USD item in the transaction records a refund of 0 USD.

Tax transactions are immutable but you can cancel out a partial refund by creating a full reversal of it.

[full reversal](/api/tax/transactions/create_reversal#tax_transaction_create_reversal-mode)

You might need to do this when:

- The payment refund fails and you haven’t provided the good or service to your customer

[refund fails](/refunds#failed-refunds)

- The wrong order is refunded or the wrong amounts are refunded

- The original sale is fully refunded and the partial refunds are no longer valid

In the example below, tax_1MEFACI6rIcR421eHrjXCSmD is the transaction representing the partial refund:

This returns the full reversal transaction that’s created:

[Testing](#testing)

## Testing

The response structure in test mode is identical to live mode, so that you can confirm your integration is working correctly before going live.

[test mode](/test-mode)

We don’t guarantee test mode calculations return up-to-date taxation results.

You are limited to 1,000 test mode tax calculations per day. Contact Stripe support if you need a higher limit.

[Stripe support](https://support.stripe.com/contact)

[privacy policy](https://stripe.com/privacy)

[OptionalIntegration examples](#integration-examples)

## OptionalIntegration examples

[OptionalCalculate tax on shipping costsServer-side](#shipping-costs)

## OptionalCalculate tax on shipping costsServer-side

[OptionalEstimate taxes with an IP addressServer-side](#ip-address)

## OptionalEstimate taxes with an IP addressServer-side

[OptionalCollect customer tax IDsServer-side](#tax-ids)

## OptionalCollect customer tax IDsServer-side

[OptionalTax-inclusive pricingServer-side](#inclusive-pricing)

## OptionalTax-inclusive pricingServer-side

[OptionalUse an existing Product objectServer-side](#existing-product)

## OptionalUse an existing Product objectServer-side

[OptionalUse an existing Customer objectServer-side](#existing-customer)

## OptionalUse an existing Customer objectServer-side

[OptionalOverride customer taxabilityServer-side](#taxability-override)

## OptionalOverride customer taxabilityServer-side

[OptionalSpecify a ship-from locationServer-sidebeta](#ship_from)

## OptionalSpecify a ship-from locationServer-sidebeta

[OptionalDetailed line item tax breakdownsServer-side](#tax-breakdowns)

## OptionalDetailed line item tax breakdownsServer-side

## See also

- Use Stripe Tax with Connect

[Use Stripe Tax with Connect](/tax/connect)
