# Usage-based billingLegacy

We’ve updated the way usage-based billing works. See the updated usage-based billing docs.

[updated usage-based billing docs](/billing/subscriptions/usage-based)

Learn how to migrate.

[migrate](/billing/subscriptions/usage-based-legacy/migration-guide)

## Getting started

[Usage-based pricing modelLearn how to model usage-based pricing on Stripe.](/billing/subscriptions/usage-based-legacy/pricing-models)

Learn how to model usage-based pricing on Stripe.

[Record usageRecord the usage of your users and report it to Stripe.](/billing/subscriptions/usage-based-legacy/recording-usage)

Record the usage of your users and report it to Stripe.

[Usage-based billing overviewUnderstand the major pieces of a usage-based billing integration.](/billing/subscriptions/usage-based-legacy#sample-integration)

Understand the major pieces of a usage-based billing integration.

## Usage-based billing lifecycle

Here’s what the lifecycle of a usage-based billing looks like.

This diagram illustrates what happens after you’ve implemented a customer experience.

## Sample integration

This example walks through the implementation of a fictional font service called Typographic.

[Create a product and pricing](#create-product)

## Create a product and pricing

Model your business on stripe with products and prices.

Create your products and their pricing options with the Stripe API or Dashboard. Typographic has three products, each with two tiers:

[products](/api/products)

- StandardTier one: 10 USD per month for 10,000 requestsTier two: An additional $0.10 USD for each request after 10,000

- Tier one: 10 USD per month for 10,000 requests

- Tier two: An additional $0.10 USD for each request after 10,000

- GrowthTier one: 25 USD per month for 10,000 requestsTier two: An additional $0.10 USD for each request after 10,000

- Tier one: 25 USD per month for 10,000 requests

- Tier two: An additional $0.10 USD for each request after 10,000

- EnterpriseTier one: 75 USD per month for 10,000 requestsTier two: An additional $0.0075 USD for each request after 10,000

- Tier one: 75 USD per month for 10,000 requests

- Tier two: An additional $0.0075 USD for each request after 10,000

To achieve this kind of pricing, you charge a flat fee and an additional amount based on how much customers use. With graduated tiers, customers initially pay the flat fee for the first 10,000 requests. If they make more requests than that, they reach tier two and start paying for each additional request. You could also charge solely based on usage without the flat fee.

[graduated tiers](/products-prices/pricing-models#graduated-pricing)

During each billing period, you create usage records for each customer and then Stripe adds them up to determine how much to bill for. This process is explained in a subsequent step but understanding the default behavior might impact how you create prices.

[usage records](/billing/subscriptions/usage-based-legacy/recording-usage)

To create a metered usage pricing model on Stripe through the Dashboard:

First, create the Standard product. To learn about all the options for creating a product, see the prices guide.

[prices guide](/products-prices/manage-prices#create-product)

- Go to the Products tab.

[tab](https://dashboard.stripe.com/products)

- Click + Add product.

- Enter the Name of the product: Standard, in this case.

- (Optional) Add a Description. The description appears at checkout, on the customer portal, and in quotes.

[customer portal](/customer-management)

[quotes](/quotes)

Next, create the monthly price for the Standard product. Select Graduated pricing for the Pricing model, then select Recurring.

Create two graduated pricing tiers:

Then, select Monthly for the Billing period and check Usage is metered.

Repeat the steps for the Growth and Enterprise products, filling in the appropriate values as necessary.

Read the docs to learn more about different pricing models.

[pricing models](/products-prices/pricing-models)

[Sign up customers](#customer-signup)

## Sign up customers

To let your customers sign up for your services, you need to present a payment form on your website. Use Stripe Checkout to embed the form on your site or redirect customers to a Stripe-hosted form. When a customer selects a recurring product and enters their billing information in the Payment Link, Stripe creates two records:

[Stripe Checkout](/checkout/quickstart)

- Customer

[Customer](/api/customers/object)

- Subscription These records are both stored within Stripe.

[Subscription](/api/subscriptions/object)

Stripe offers other options for setting up your payment form:

- Pricing tables: Create a pricing table from the Stripe Dashboard and embed it on your site. When a customer selects a plan, they’re taken to your checkout page. Pricing tables don’t support sub-cent pricing.

[Pricing tables](/payments/checkout/pricing-table)

- Web Elements: Build custom checkout flows to integrate with your site.

[Web Elements](/payments/elements)

[Create a usage record](#report-usage)

## Create a usage record

Throughout each billing period, you need to report usage to Stripe so that customers are billed the correct amounts. You can maintain your own system for recording customer usage and provide usage information for subscriptions to Stripe.

Learn how to record and report usage.

[record and report usage](/billing/subscriptions/usage-based-legacy/recording-usage)

[Test your integration](#test-integration)

## Test your integration

Test your integration to make sure it behaves as you expect. Learn more about testing subscriptions integrations.

[testing subscriptions integrations](/billing/testing)

You can use test clocks to test different scenarios, including mock usage records. When you make a usage reporting call, you need to sync the timestamp of the test clock with the usage records. Make a note of the test clock timestamp so that your usage records fall within the same time window. Learn more about test clocks.

[test clocks](/billing/testing/test-clocks)

[OptionalFree trials](#trials)

## OptionalFree trials

[OptionalCancellations](#cancellations)

## OptionalCancellations

[OptionalBilling thresholds](#thresholds)

## OptionalBilling thresholds

[OptionalAggregate metered usage](#aggregate-metered-usage)

## OptionalAggregate metered usage

[OptionalTransforming quantities](#transforming-quantities)

## OptionalTransforming quantities

## See also

- Sample implementation repository

[Sample implementation repository](https://github.com/stripe-samples/subscription-use-cases/tree/main/usage-based-subscriptions)

- Usage-based billing video tutorial

[Usage-based billing video tutorial](https://www.youtube.com/watch?v=v8cN4pEofy8)
