# Recurring pricing models

Pricing models are patterns that represent your business on Stripe. With Product and Price objects, you can model what you sell and how you charge for it.

[Pricing models](/products-prices/pricing-models)

[Product](/api/products)

[Price](/api/prices)

[Flat rate: Good-better-best](#flat-rate)

## Flat rate: Good-better-best

Many SaaS businesses offer their customers a choice of escalating service options. This flat-rate pricing model is called good-better-best. Customers choose a service tier (good, better, or best) and pay a flat rate for it.

Imagine a business called Togethere that sells a collaboration platform. They offer three different service levels: basic, starter, and enterprise. For each service level, they offer a monthly and yearly price. Togethere operates in several countries, so they have prices in multiple currencies.

In this example, Togethere has three products: Basic, Starter, Enterprise. Each product has several different prices. The basic level has prices for 10 USD per month and 100 USD per year. Both prices are for the same Basic product, so they share the same product description on the customer’s receipt and invoice.

Here’s what that model looks like on Stripe:

Flat rate: Good-better-best pricing model

To create a good-better-best model on Stripe through the Dashboard follow the steps below.

First, create the Basic product. To learn about all the options for creating a product, see the prices guide.

[prices guide](/products-prices/manage-prices#create-product)

- Go to Product catalog.

[Product catalog](https://dashboard.stripe.com/products)

- Click + Add product.

- Enter the Name of your product.

- (Optional) Add a Description. The description appears at checkout, on the customer portal, and in quotes.

[customer portal](/customer-management)

[quotes](/quotes)

Next, create the monthly price for the Basic product:

- Click Advanced pricing options.

- Select Recurring and choose Flat rate for the pricing model.

- Enter the price amount-in this case, 10.00.

- Select Monthly for the Billing period.

- Click Next to save the price.

Then, create the yearly price for the Basic product:

- Click + Add another price.

- Select Recurring and choose Flat rate for the pricing model.

- Enter the price amount-in this case, 100.00.

- Select Yearly for the Billing period.

- Click Add product to save the product and price. You can edit the product and price later.

The subscription integration guide explains how to fit pricing models into a full integration.

- If you’re using Stripe Checkout, the next step is to create a Checkout session for your site. Make sure to set up Stripe.

[create a Checkout session](/billing/subscriptions/build-subscriptions?ui=stripe-hosted#create-session)

- If you’re using Stripe Elements, the next step is to create a Customer. Make sure you set up Stripe and the sample application.

[create a Customer](/billing/subscriptions/build-subscriptions?ui=elements#create-customer)

[Per-seat](#per-seat)

## Per-seat

Togethere, our example collaboration platform company, also wants to offer a per-seat plan. Per-seat pricing is another common offering for SaaS businesses. Togethere’s customers pick how many seats they’ll use, and Togethere charges based on that amount.

To model this scenario, Togethere creates a product and price structure where each unit represents a user. When Togethere creates a subscription for a customer, the customer specifies the number of users for that subscription.

Here’s what that model looks like on Stripe:

Per-seat pricing model

See the advanced pricing model section for examples of other models. Flat rate and per-seat pricing, where you charge a customer a flat monthly fee in addition to a per-seat rate, is another common model for SaaS businesses.

[advanced](/billing/subscriptions/usage-based/pricing-models)

[Flat rate and per-seat](#adding-flat-fees)

To create a per-seat model on Stripe through the Dashboard follow the steps below.

First, create the Per-seat product. To learn about all the options for creating a product, see the prices guide.

[prices guide](/products-prices/manage-prices#create-product)

- Go to Product catalog.

[Product catalog](https://dashboard.stripe.com/products)

- Click +Add product.

- Enter the Name of the product: Per-seat, in this case.

- (Optional) Add a Description. The description appears at checkout, on the customer portal, and in quotes.

[customer portal](/customer-management)

[quotes](/quotes)

Next, create the monthly price for the Per-seat product:

- Select Recurring.

- Enter the price amount-in this case, 80.00.

- Select Monthly for the Billing period.

- Click Add product to save the product and price. You can edit the product and price later.

To create a subscription using that price:

- Go to the Payments > Subscriptions page.

- Click + Create subscription.

- Find or add a customer.

- Search for the Per-seat product you created and select the price you want to use.

- (Optional) Select Collect tax automatically to use Stripe Tax.

- Click Start subscription to start it immmediately or Schedule subscription to start it on another schedule.

Read the docs to learn all the options for creating a subscription.

[creating a subscription](/billing/subscription-resource?dashboard-or-api=dashboard#create-subscriptions)

The subscription integration guide explains how to fit pricing models into a full integration.

- If you’re using Stripe Checkout, the next step is to create a Checkout session for your site. Make sure you set up Stripe.

[create a Checkout session](/billing/subscriptions/build-subscriptions?ui=stripe-hosted#create-session)

- If you’re using Stripe Elements, the next step is to create a Customer. Make sure you set up Stripe and the sample application.

[create a Customer](/billing/subscriptions/build-subscriptions?ui=elements#create-customer)

For other versions of per-seat pricing, see the advanced models section.

[advanced](#advanced)

[Usage-based pricing](#usage-based-pricing)

## Usage-based pricing

Usage-based pricing is a common pricing model for SaaS businesses that enables you to charge based on a customer’s usage of your product or service. As a business, you provide access to your service and bill your customer based on their usage. To see what an end-to-end integration based on the usage-based pricing model looks like, read the usage-based pricing models guide.

[usage-based pricing models](/billing/subscriptions/usage-based/pricing-models)

[Tiered pricing](#tiered-pricing)

## Tiered pricing

Prices can represent tiers, allowing the unit cost to change with quantity or usage. Togethere might, for example, want to offer lower rates for customers who use more projects per month. The following examples show two different ways to adjust pricing as usage increases: volume-based pricing and graduated pricing. To demonstrate these approaches to tiered pricing, we’ll use the following tiers:

Use tiers if you need non-linear pricing when quantity or usage changes. You can also combine tiered pricing with base fees to create more complex pricing models.

[usage](/api/billing/meter-event)

[complex pricing models](/billing/subscriptions/usage-based/pricing-models)

When you create a price with billing_scheme=per_unit, the unit_amount is the same regardless of how many units a customer buys. Stripe multiplies this amount by the quantity to determine the total cost. For example, a unit_amount of 5 USD creates this billing structure:

[create a price](/api#create_price)

When you create a price with billing_scheme=tiered, the unit cost varies depending on how many units your customer buys. Here’s an example tier structure:

Multiplication happens:

- At the start of the billing period if the Price objects have recurring.usage_type = licensed.

- At the end of the billing period if the Price objects have recurring.usage_type = metered.

With tiered billing, you:

- Set the tiers_mode to either volume or graduated.

- Create a tiers array to represent the tiers structure.

See also the volume-based and graduated pricing examples.

[volume-based](/products-prices/pricing-models#volume-based-pricing)

[graduated](/products-prices/pricing-models#graduated-pricing)

With volume-based pricing, the subscription item is billed at the tier corresponding to the amount of usage at the end of the period. To implement volume-based billing tiers, set volume as the value of tiers_mode:

Under volume-based pricing, a customer with 5 projects is charged 35 USD at the end of the period: 7 USD for each of the 5 projects. However, if they accumulate 6 projects the following month, then all projects are billed at the 6-10 rate. That month, they’re charged 39 USD (6.50 × 6).

With tiers_mode=volume, the entire quantity is multiplied by the unit cost of the tier.

Because the tier price applies to the entire quantity or usage, the total can decrease when calculating the final cost.

While similar to volume pricing, graduated pricing charges for the usage in each tier instead of applying a single price to all usage. To use graduated tiers, set the value of tiers_mode to graduated:

With graduated pricing, 5 projects result in the same charge as volume-based pricing—35 USD total at 7 USD per project. This changes as usage breaks out of the first tier. A customer with more than 5 projects is charged 7 USD per project for the first 5 projects, then 6.50 USD for projects 6 through 10, and finally 6 USD per project thereafter. A customer with 6 projects would be charged 41.50 USD, 35 USD for the first 5 projects and 6.50 USD for the 6th project.

With tiers_mode=graduated, the quantity is multiplied by the amount that falls into that tier. Then, the total is summed. For example, the total cost for an amount of 6 is 29 USD: 25 USD for the 5 quantity that falls into the 1–5 tier, plus 4 USD for the single quantity that falls into the 6–10 tier.

You can specify a flat fee (flat_amount) to add to the invoice. This works for both tiers_mode=volume and tiers_mode=graduated. For example, you can have a flat fee that increases when certain usage thresholds are met:

[invoice](/api/invoices)

In this example, if quantity is 12 and tiers_mode=volume, the total amount to be billed is 12 * 3 USD + 30 USD = 66 USD.

If quantity is 12 and tiers_mode=graduated, the total amount is 5 * 5 USD + 10 USD + 5 * 4 USD + 20 USD + 2 * 3 USD + 30 USD = 111 USD. A tier can have either a unit_amount or a flat_amount, or both, but it must have at least one of the two.

If quantity is 0, the total amount is 10 USD regardless of tiers_mode. We always bill the first flat fee tier when quantity=0. To bill 0 when there’s no usage, set up an up_to=1 tier with an unit_amount equal to the flat fee and omit the flat_amount.

[Variable pricing](#variable-pricing)

## Variable pricing

There are two types of variable pricing models:

- Inline pricing: You define the price for your customer when you create a subscription, invoice, or Checkout Session.

- Pay-what-you-want pricing: The customer fills in the price they pay, like with a tip or donation. This type of variable pricing isn’t supported for recurring payments. See Let customers decide what to pay for information about using this type of pricing for single payments.

[Let customers decide what to pay](/payments/checkout/pay-what-you-want)

In some cases, you might want to use a custom price that hasn’t been preconfigured. For example, you might want to use inline prices when you manage your product catalog outside of Stripe.

You can only create inline prices through the API. Inline prices aren’t compatible with Payment Links.

[Payment Links](/payment-links/api)

To create an inline price use case, pass in price_data instead of a price.id when you create a subscription. For example, to subscribe a customer to a monthly subscription with an inline price:

[price_data](/api/subscriptions/create#create_subscription-items-price_data)

[price.id](/api/subscriptions/object#subscription_object-items-data-price-id)

This creates a monthly recurring price of 50 USD for the basic service offering. By default, prices created with price_data are effectively archived (they’re marked as active=false) so that they you can’t reuse them for other customers or subscriptions. You can’t update or reuse inline prices after you create them. You can also use price_data with these APIs:

- Checkout

[Checkout](/api/checkout/sessions)

- Invoice Items

[Invoice Items](/api/invoiceitems)

- Subscription Schedules

[Subscription Schedules](/api/subscription_schedules)

[Multi-currency prices](#multicurrency)

## Multi-currency prices

A single Price can support multiple currencies. This helps you manage localized pricing when selling internationally.

[Price](/api/prices)

You can create multi-currency Prices in the API or the Dashboard.

[API](/api/prices/create)

From the Product details page for a product in your Dashboard, click on + Add another price to create a new price. The first currency on your Price will be the default currency. Make sure all your Prices have the same default currency. After selecting the default currency, click on + Add more currencies to add currency options to your Price.

[Dashboard](https://dashboard.stripe.com/test/products)

You can search and select from supported currencies. Stripe suggests an exchange rate based on currency values at 12:00 PM EST, but you can pick your own. For currencies that are subject to larger fluctuations, we recommend adding more of a buffer.

After you’re done filling in the details, click Add price to save it.

Coupons, Promotion Codes, and Shipping Rates also support multi-currency in a similar way to Prices.

[Coupons](/billing/subscriptions/coupons#coupons)

[Promotion Codes](/billing/subscriptions/coupons#promotion-codes)

[Shipping Rates](/payments/during-payment/charge-shipping)

To show your customer the price in their currency, you can retrieve the multi-currency Price and view its currency_options.<currency>.unit_amount field. The API response won’t include currency_options by default. To include it in the response, expand the currency_options field:

[currency_options.<currency>.unit_amount](/api/prices/object#price_object-currency_options-unit_amount)

[expand](/api/expanding_objects)

To improve latency and avoid problems with rate-limiting, cache the Price instead of re-fetching it every time a customer visits your site.

Each purchase uses one of the multi-currency Price’s supported currencies, depending on how you use the Price in your integration.

Checkout automatically determines the customer’s local currency from their IP address, as long as the Price supports that currency. If the customer’s local currency isn’t supported, Checkout uses the Price’s default currency.

If a Checkout Session uses multiple Prices, Coupons, Promotion Codes, or Shipping Rates, then they must all support the customer’s local currency, or else Checkout uses the default currency. They must all have the same default currency, or else Stripe returns an error when you create the Checkout Session.

Alternatively, you can use the currency parameter to explicitly tell Checkout which currency to use.

[currency](/api/checkout/sessions/create#create_checkout_session-currency)

Learn more about defining multi-currency prices in Checkout.

[multi-currency prices](/payments/checkout/multi-currency-prices)

If you have an existing single-currency Price, you can retroactively add multiple currencies to it in the Dashboard.

Only the Stripe Dashboard can retroactively add multiple currencies to an existing Price. The Stripe API doesn’t support retroactively adding multiple currencies. If you’re using the API, create a new multi-currency Price from scratch.

After you add a new currency to a Price, the only way to change it is to archive the existing Price and create a new one. Learn more about managing existing prices.

[managing existing prices](/products-prices/how-products-and-prices-work#manage-existing-products-and-prices)

If you use Checkout or Payment Links, then multi-currency Prices take effect automatically. If Stripe detects that the customer’s local currency is supported by the Price, then it automatically uses that currency. If you use multiple Prices, Coupons, Promotion Codes, or Shipping Rates in a single purchase, then they must all support the customer’s local currency, and they must all have the same default currency.

If you’re creating Subscriptions directly, the multi-currency Price(s) won’t take effect until you start passing the currency parameter. If you don’t pass the currency parameter, the Subscription always uses the Price(s)’ default currency.

[Multiple prices](#multiple-prices)

## Multiple prices

Products can use multiple prices to define different pricing options. The product description is shared between prices and appears the same on the customer’s receipt and invoice—only the pricing differs.

As Togethere’s product matures, they begin offering the same product at different price points. Specifically, certain customers are willing to pay for discounted up-front quarterly and yearly subscriptions. Togethere creates a quarterly 57 USD option:

And a yearly 220 USD option:

[Display pricing information](#pricing-table)

## Display pricing information

After creating your pricing structures, you can embed a pricing table on your website to display pricing information to your customers. When customers choose a subscription option, they’re taken directly to checkout. Configure, customize, and update directly in the Dashboard without writing any code.

[pricing table](/payments/checkout/pricing-table)

[Dashboard](https://dashboard.stripe.com/test/pricing-tables)
