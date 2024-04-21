htmlCheckout prices migration guide | Stripe Documentation[Skip to content](#main-content)Migrate Checkout to use Prices[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fmigrating-prices)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fmigrating-prices)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Checkout](/payments/checkout)·[Home](/docs)[Payments](/docs/payments)[Checkout](/docs/payments/checkout)# Checkout prices migration guide

Learn how to update your integration to use prices with Stripe Checkout.The Prices API adds new features and flexibility to how you charge customers. This new integration offers:

- More unified modeling for Checkout items—instead of plans,[SKUs](/api/skus), and inline line items, every item is now aprice.
- The ability to render product images for recurring items.

For the client and server integration, the Prices API unlocks the ability to:

- Create a reusable product and price catalog instead of one-time line items
- Create inline pricing for[subscriptions](/billing/subscriptions/creating)
- Apply dynamic tax rates to[subscriptions](/billing/taxes/collect-taxes?tax-calculation=tax-rates#adding-tax-rates-to-checkout)and[one-time payments](/payments/checkout/taxes)

Don’t want to migrate? You can continue to use your current integration, but new features are not supported. Any new plans or recurring prices you create can be used in the plan parameter of your existing API calls.

## Products and prices overview

Prices are a new, core entity within Stripe that works with subscriptions, invoices, and Checkout. Each price is tied to a single Product, and each product can have multiple prices. Different physical goods or levels of service should be represented by products. Pricing of that product should be represented by prices.

Prices define the base price, currency, and—for recurring products—the billing cycle. This allows you to change and add prices without needing to change the details of what you offer. For example, you might have a single “gold” product that has prices for 10 USD/month, 100 USD/year, 9 EUR/month, and 90 EUR/year. Or you might have a blue t-shirt with 20 USD and 15 EUR prices.

Plans and SKUs (client-only) may be used with the new integration wherever Prices are accepted. You can either create a product and price through the API or through the Dashboard.

## One-time payments

Client and server integrationClient-only integrationThe client and server integration has the following changes for one-time payments:

- Instead of ad-hoc line items (that is, setting the name, amount, and currency), creating a Checkout Session requires creating a[product](/api/products)and, usually, a[price](/api/prices).
- [mode](/api/checkout/sessions/create#create_checkout_session-mode)is now required.

The client-side code remains the same.

### Mapping table

Instead of defining each field on line_items, Checkout uses the underlying product and price objects to determine name, description, amount, currency, and images. You can create products and prices with the API or Dashboard.

Without pricesWith prices`line_items.name``product.name``line_items.description``product.description``line_items.amount`- `price.unit_amount`
- `price_data.unit_amount`(if defined when the Checkout Session is created)

`line_items.currency`- `price.currency`
- `price_data.currency`(if defined when the Checkout Session is created)

`line_items.images``product.images`(displays the first image supplied)### Server-side code for inline items

Previously, you could only create one-time items inline. With prices, you can continue to configure your items inline, but you can also define your prices dynamically with price_data when you create the Checkout Session.

When you create the Checkout Session with price_data, reference an existing product ID with price_data.product, or define your product details dynamically using price_data.product_data. The following example demonstrates the flow for creating a one-time item.

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "line_items[0][quantity]"=1 \
  -d "line_items[0][amount]"=2000 \
  -d "line_items[0][name]"=T-shirt \
  -d "line_items[0][description]"="Comfortable cotton t-shirt" \
  -d "line_items[0][images][]"="https://example.com/t-shirt.png" \
  -d "line_items[0][currency]"=usd \
  -d "line_items[0][price_data][unit_amount]"=2000 \
  -d "line_items[0][price_data][product_data][name]"=T-shirt \
  -d "line_items[0][price_data][product_data][description]"="Comfortable cotton t-shirt" \
  -d "line_items[0][price_data][product_data][images][]"="https://example.com/t-shirt.png" \
  -d "line_items[0][price_data][currency]"=usd \
  -d mode=payment \
  -d success_url="https://example.com/success" \
  -d cancel_url="https://example.com/cancel"`### Server-side code for one-time prices

With this new integration, you can create a product and price catalog upfront instead of needing to define the amount, currency, and name each time you create a Checkout Session.

You can either create a product and price with the Prices API or through the Dashboard. You will need the price ID to create the Checkout Session. The following example demonstrates how to create a product and price through API:

Command Line[curl](#)`curl https://api.stripe.com/v1/products \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d name=T-shirt \
  -d description="Comfortable cotton t-shirt" \
  -d "images[]"="https://example.com/t-shirt.png"

curl https://api.stripe.com/v1/prices \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d product="{{PRODUCT_ID}}" \
  -d unit_amount=2000 \
  -d currency=usd

curl https://api.stripe.com/v1/checkout/sessions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "line_items[0][quantity]"=1 \
  -d "line_items[0][amount]"=2000 \
  -d "line_items[0][name]"=T-shirt \
  -d "line_items[0][description]"="Comfortable cotton t-shirt" \
  -d "line_items[0][images][]"="https://example.com/t-shirt.png" \
  -d "line_items[0][currency]"=usd \
  -d "line_items[0][price]"="{{PRICE_ID}}" \
  -d mode=payment \
  -d success_url="https://example.com/success" \
  -d cancel_url="https://example.com/cancel"`## Subscriptions

Client and server integrationClient-only integrationThe client and server integration has the following changes for recurring payments:

- All items are passed into a single[line_items](/api/checkout/sessions/create#create_checkout_session-line_items)field, instead of`subscription_data.items`.
- [mode](/api/checkout/sessions/create#create_checkout_session-mode)is now required. Set`mode=subscription`if the session includes any recurring items.

The client-side code remains the same. Existing plans can be used wherever recurring prices are accepted.

### Server-side code with plans

Here is a before and after example of creating a Checkout Session with a trial and using an existing plan, which can be used interchangeably with a price. The plan is now passed into line_items instead of subscription_data.items.

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "subscription_data[items][][plan]"="{{PRICE_OR_PLAN_ID}}" \
  -d "line_items[0][price]"="{{PRICE_OR_PLAN_ID}}" \
  -d "line_items[0][quantity]"=1 \
  -d mode=subscription \
  -d success_url="https://example.com/success" \
  -d cancel_url="https://example.com/cancel"`### Server-side code for recurring price with setup fee

If you have recurring plans with a one-time setup fee, create the product and price representing the one-time fee before creating the Checkout Session. See the mapping table for how the old line_items fields map to the new integration. You can either create a product and price through the Prices API or through the Stripe Dashboard. You can also create the one-time item inline. The following example uses an existing price ID:

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "line_items[0][quantity]"=1 \
  -d "line_items[0][amount]"=2000 \
  -d "line_items[0][name]"=T-shirt \
  -d "line_items[0][description]"="Comfortable cotton t-shirt" \
  -d "line_items[0][images][]"="https://example.com/t-shirt.png" \
  -d "line_items[0][currency]"=usd \
  -d "subscription_data[items][][plan]"="{{PLAN_ID}}" \
  -d "line_items[0][price]"="{{PRICE_OR_PLAN_ID}}" \
  -d "line_items[0][quantity]"=1 \
  -d "line_items[1][price]"="{{ONE_TIME_PRICE_ID}}" \
  -d "line_items[1][quantity]"=1 \
  -d mode=subscription \
  -d success_url="https://example.com/success" \
  -d cancel_url="https://example.com/cancel"`## Response object changes

Instead of listing items with display_items, the Checkout Session object uses line_items. The line_items field does not render by default as display_items did, but you can include it using expand when creating a Checkout Session:

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "payment_method_types[]"="card" \
  -d "mode"="payment" \
  -d "line_items[0][price]"="{{PRICE_ID}}" \
  -d "line_items[0][quantity]"=1 \
  -d "success_url"="https://example.com/success" \
  -d "cancel_url"="https://example.com/cancel" \
  -d "expand[]"="line_items"`## Webhook changes

Since line_items is includable, the checkout.session.completed webhook response no longer list items by default. The smaller response object enables you to receive your Checkout webhooks faster. You can retrieve items with the new line_items endpoint:

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions/{{CHECKOUT_SESSION_ID}}/line_items \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:`For more details, see fulfilling orders with Checkout.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Products and prices overview](#product-price-overview)[One-time payments](#one-time-payments-changes)[Subscriptions](#subscription-changes)[Response object changes](#response-object-changes)[Webhook changes](#webhook-changes)Products Used[Checkout](/payments/checkout)[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`