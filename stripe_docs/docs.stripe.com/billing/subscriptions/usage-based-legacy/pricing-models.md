# Model usage-based pricingLegacy

We’ve updated the way usage-based billing works. See the updated usage-based billing docs.

[updated usage-based billing docs](/billing/subscriptions/usage-based)

Learn how to migrate.

[migrate](/billing/subscriptions/usage-based-legacy/migration-guide)

With usage-based pricing models, you charge your customers based on how much of your service they use during the billing cycle, instead of explicitly setting quantities, as in the per-seat and flat rate pricing models. (Another difference is that in the per-seat and flat-rate models, you could optionally collect payment for the billing cycle up front. With metered billing, you have to collect payment in arrears.) You must also record and report usage.

[per-seat](/products-prices/pricing-models#per-seat)

[flat rate](/products-prices/pricing-models#flat-rate)

[record and report usage](/billing/subscriptions/usage-based-legacy/recording-usage)

Togethere wants to charge on a per-minute basis for usage of their new conferencing service, where more usage drives the per-minute price lower for the customer.

Here’s what that model looks like on Stripe:

Usage-based pricing model

For recurring purchases, you define how much to charge customers through usage_types-either licensed or metered.

In the Dashboard, you can select Standard pricing or Package pricing as pricing models. Both of these models map to the licensed (recurring[usage_type]='licensed') usage type. With both models, you specify the number of units when you create or update a subscription. Here’s how they differ:

[licensed](/api/prices/create#create_price-recurring-usage_type)

- With Standard pricing, the quantity defaults to 1.

- With Package pricing, you set the unit amount to values of 2 or more.

The following example shows how to create a metered usage pricing model. In this case, Togethere charges .07 USD per minute.

To create a metered usage pricing model on Stripe through the Dashboard:

First, create the Per-minute pricing product. To learn about all the options for creating a product, see the prices guide.

[prices guide](/products-prices/manage-prices#create-product)

- Go to the Product catalog.

[Product catalog](https://dashboard.stripe.com/products)

- Click + Add product.

- Enter the Name of the product: Per-minute pricing, in this case.

- (Optional) Add a Description. The description appears at checkout, on the customer portal, and in quotes.

[customer portal](/customer-management)

[quotes](/quotes)

Next, create the monthly price for the Per-minute pricing product.

Click Advanced pricing options. Select Usage-based, Per tier, and Graduated for the Pricing model.

Create three graduated pricing tiers:

To create a subscription using that price:

- Go to the Payments > Subscriptions page.

[page](https://dashboard.stripe.com/subscriptions)

- Click + Create subscription.

- Find or add a customer.

- Search for the Per-minute pricing product you created and select the price you want to use.

- (Optional) Select Collect tax automatically to use Stripe Tax.

- Click Start subscription to start it immmediately or Schedule subscription to choose when to start it.

Read the docs to learn all the options for creating a subscription.

[creating a subscription](/billing/subscription-resource?dashboard-or-api=dashboard#create-subscriptions)

The subscription integration guide explains how to fit pricing models into a full integration.

- If you’re using Stripe Checkout, the next step is to create a Checkout session for your site. Make sure you set up Stripe.

[create a Checkout session](/billing/subscriptions/build-subscriptions?ui=stripe-hosted#create-session)

- If you’re using Stripe Elements, the next step is to create a Customer. Make sure you set up Stripe and the sample application.

[create a Customer](/billing/subscriptions/build-subscriptions?ui=elements#create-customer)

For other versions of usage-based pricing, see the advanced models section. Also learn how to set up free trials and other optional features for a usage-based billing integration.

[advanced](#advanced)

[free trials](/billing/subscriptions/usage-based-legacy#trials)

[Advanced pricing models](#advanced)

## Advanced pricing models

You can subscribe the customer to two separate products to model a pricing structure that includes both a base fee and additional per-seat pricing. One product serves as the flat base price and the other product represents the variable per-seat pricing.

Togethere charges a flat monthly rate for their service plus a tiered price for more than 50 users.

To model this structure on Stripe, Togethere creates a Product and Price for the base fee:

Then they create a monthly price that charges 15 USD per user:

Here’s how they subscribe a customer with three users to the base fee price and the per-user price:

This results in a 50 USD charge every month: the 5 USD base monthly rate, plus 15 USD each for 3 users.

You can also combine flat fees with usage-based pricing to charge a flat monthly rate in addition to charging for usage over the billing cycle.

To create a flat rate with a metered usage pricing model on Stripe through the Products and Prices APIs:

[Products](/api/products)

[Prices](/api/prices)

- Create the Flat monthly fee product.Command Linecurlcurl https://api.stripe.com/v1/products \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d name=Per-seat

Create the Flat monthly fee product.

- Create a price for the Flat monthly fee product.Command Linecurlcurl https://api.stripe.com/v1/prices \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d product={{PRODUCT_ID}} \
  -d unit_amount=1000 \
  -d currency=usd \
  -d "recurring[interval]"=month

Create a price for the Flat monthly fee product.

- Create the Meeting per minute usage price.Command Linecurlcurl https://api.stripe.com/v1/prices \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d nickname="Metered Monthly Plan" \
  -d product={{PRODUCT_ID}} \
  -d unit_amount=700 \
  -d currency=usd \
  -d "recurring[interval]"=month \
  -d "recurring[usage_type]"=metered

Create the Meeting per minute usage price.

When you create subscriptions, specify both price IDs:

Decimal pricing is useful if you need to create pricing amounts that aren’t whole numbers. For example, if you’re running a cloud storage SaaS business, you can create a price that charges 0.05 cents for each MB used per month. Based on usage, the quantity of MB is then multiplied by 0.05 cents and rounded to the nearest whole cent.

To create prices with decimal amounts, specify unit_amount_decimal instead of unit_amount. unit_amount_decimal allows you to set the amount in the minor unit of the currency that you charge in. For example, you can set unit_amount_decimal = 105.5 in USD to represent 105.5 cents, or 1.055 USD. unit_amount_decimal accepts decimals up to 12 decimal places.

[create prices](/api#create_price)

If you plan to use tiers, you can specify unit_amount_decimal instead of unit_amount. You can also create invoice items with unit_amount_decimal instead of unit_amount.

[tiers](/products-prices/pricing-models#tiered-pricing)

[create invoice items](/api/invoiceitems/create)

In API responses, the integer unit_amount field isn’t populated if the object is created with a decimal value. For example, if you create a price with unit_amount_decimal = 0.05, the response contains unit_amount = null and unit_amount_decimal = 0.05. You can still pass integer values into unit_amount_decimal, in which case unit_amount is populated in the response. For instance, if you create a price with unit_amount_decimal = 5, the response contains unit_amount = 5 and unit_amount_decimal = 5.0.

If your integration has event handling that uses unit_amount values and you begin using decimal amounts, you need to use unit_amount_decimal instead. This is important because unit_amount will be returned as null if the decimal amounts can’t be converted into integers, which could cause errors in your integration.
