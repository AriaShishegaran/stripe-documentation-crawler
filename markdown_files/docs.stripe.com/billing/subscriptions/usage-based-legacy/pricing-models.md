htmlModel usage-based pricing | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fusage-based-legacy%2Fpricing-models)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fusage-based-legacy%2Fpricing-models)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# Model usage-based pricingLegacy

Learn about different pricing models for usage-based billing on Stripe.NoteWe’ve updated the way usage-based billing works. See the updated usage-based billing docs.

Learn how to migrate.

With usage-based pricing models, you charge your customers based on how much of your service they use during the billing cycle, instead of explicitly setting quantities, as in the per-seat and flat rate pricing models. (Another difference is that in the per-seat and flat-rate models, you could optionally collect payment for the billing cycle up front. With metered billing, you have to collect payment in arrears.) You must also record and report usage.

Togethere wants to charge on a per-minute basis for usage of their new conferencing service, where more usage drives the per-minute price lower for the customer.

Here’s what that model looks like on Stripe:

![](https://b.stripecdn.com/docs-statics-srv/assets/pricing_model-metered-usage.43b16d41d299829bc3fd34ddc2d14b15.png)

Usage-based pricing model

### Usage types

For recurring purchases, you define how much to charge customers through usage_types-either licensed or metered.

### Licensed usage

### Metered usage

### Package and standard pricing

In the Dashboard, you can select Standard pricing or Package pricing as pricing models. Both of these models map to the licensed (recurring[usage_type]='licensed') usage type. With both models, you specify the number of units when you create or update a subscription. Here’s how they differ:

- WithStandard pricing, the quantity defaults to 1.
- WithPackage pricing, you set the unit amount to values of 2 or more.

### Model usage-based pricing on Stripe

The following example shows how to create a metered usage pricing model. In this case, Togethere charges .07 USD per minute.

DashboardAPITo create a metered usage pricing model on Stripe through the Dashboard:

First, create the Per-minute pricing product. To learn about all the options for creating a product, see the prices guide.

1. Go to the[Product catalog](https://dashboard.stripe.com/products).
2. Click+ Add product.
3. Enter theNameof the product:`Per-minute pricing`, in this case.
4. (Optional)Add aDescription. The description appears at checkout, on the[customer portal](/customer-management), and in[quotes](/quotes).

Next, create the monthly price for the Per-minute pricing product.

Click Advanced pricing options. Select Usage-based, Per tier, and Graduated for the Pricing model.

Create three graduated pricing tiers:

First unitLast unitPer unitFlat feeFor the first0600.25 USD0.00 USDFor the next611200.20 USD0.00 USDFor the next121∞0.15 USD0.00 USDTo create a subscription using that price:

1. Go to thePayments>Subscriptions[page](https://dashboard.stripe.com/subscriptions).
2. Click+ Create subscription.
3. Find or add a customer.
4. Search for the`Per-minute pricing`product you created and select the price you want to use.
5. (Optional)SelectCollect tax automaticallyto use Stripe Tax.
6. ClickStart subscriptionto start it immmediately orSchedule subscriptionto choose when to start it.

Read the docs to learn all the options for creating a subscription.

The subscription integration guide explains how to fit pricing models into a full integration.

- If you’re using Stripe Checkout, the next step is to[create a Checkout session](/billing/subscriptions/build-subscriptions?ui=stripe-hosted#create-session)for your site. Make sure you set up Stripe.
- If you’re using Stripe Elements, the next step is to[create a Customer](/billing/subscriptions/build-subscriptions?ui=elements#create-customer). Make sure you set up Stripe and the sample application.

For other versions of usage-based pricing, see the advanced models section. Also learn how to set up free trials and other optional features for a usage-based billing integration.

[Advanced pricing models](#advanced)### Flat rate and per-seat

You can subscribe the customer to two separate products to model a pricing structure that includes both a base fee and additional per-seat pricing. One product serves as the flat base price and the other product represents the variable per-seat pricing.

Togethere charges a flat monthly rate for their service plus a tiered price for more than 50 users.

Model flat rate and per-seat on Stripe![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

To model this structure on Stripe, Togethere creates a Product and Price for the base fee:

Command Line[curl](#)`curl https://api.stripe.com/v1/prices \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d nickname="Monthly Base Fee" \
  -d product={{BASE_FEE_PRODUCT_ID}} \
  -d unit_amount=500 \
  -d currency=usd \
  -d "recurring[interval]"=month \
  -d "recurring[usage_type]"=licensed`Then they create a monthly price that charges 15 USD per user:

Command Line[curl](#)`curl https://api.stripe.com/v1/prices \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d nickname="Per-seat price" \
  -d product={{PRODUCT_ID}} \
  -d unit_amount=1500 \
  -d currency=usd \
  -d "recurring[interval]"=month \
  -d "recurring[usage_type]"=licensed`Here’s how they subscribe a customer with three users to the base fee price and the per-user price:

Command Line[curl](#)`curl https://api.stripe.com/v1/subscriptions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d "items[0][price]"={{BASE_FEE_PRICE_ID}} \
  -d "items[0][quantity]"=1 \
  -d "items[1][price]"={{PER_SEAT_PRICE_ID}} \
  -d "items[1][quantity]"=3`This results in a 50 USD charge every month: the 5 USD base monthly rate, plus 15 USD each for 3 users.

### Flat rate with metered usage

You can also combine flat fees with usage-based pricing to charge a flat monthly rate in addition to charging for usage over the billing cycle.

To create a flat rate with a metered usage pricing model on Stripe through the Products and Prices APIs:

1. Create the Flat monthly fee product.

Command Line[curl](#)`curl https://api.stripe.com/v1/products \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d name=Per-seat`
2. Create a price for the Flat monthly fee product.

Command Line[curl](#)`curl https://api.stripe.com/v1/prices \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d product={{PRODUCT_ID}} \
  -d unit_amount=1000 \
  -d currency=usd \
  -d "recurring[interval]"=month`
3. Create the Meeting per minute usage price.

Command Line[curl](#)`curl https://api.stripe.com/v1/prices \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d nickname="Metered Monthly Plan" \
  -d product={{PRODUCT_ID}} \
  -d unit_amount=700 \
  -d currency=usd \
  -d "recurring[interval]"=month \
  -d "recurring[usage_type]"=metered`

When you create subscriptions, specify both price IDs:

Command Line[curl](#)`curl https://api.stripe.com/v1/subscriptions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d "items[0][price]"={{FLAT_MONTHLY_FEE_PRICE_ID}} \
  -d "items[0][quantity]"=1 \
  -d "items[1][price]"={{METERED_USAGE_PRICE_ID}} \
  -d "items[1][quantity]"=1`### Decimal amounts

Decimal pricing is useful if you need to create pricing amounts that aren’t whole numbers. For example, if you’re running a cloud storage SaaS business, you can create a price that charges 0.05 cents for each MB used per month. Based on usage, the quantity of MB is then multiplied by 0.05 cents and rounded to the nearest whole cent.

Creating objects with decimal amounts![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

To create prices with decimal amounts, specify unit_amount_decimal instead of unit_amount. unit_amount_decimal allows you to set the amount in the minor unit of the currency that you charge in. For example, you can set unit_amount_decimal = 105.5 in USD to represent 105.5 cents, or 1.055 USD. unit_amount_decimal accepts decimals up to 12 decimal places.

If you plan to use tiers, you can specify unit_amount_decimal instead of unit_amount. You can also create invoice items with unit_amount_decimal instead of unit_amount.

In API responses, the integer unit_amount field isn’t populated if the object is created with a decimal value. For example, if you create a price with unit_amount_decimal = 0.05, the response contains unit_amount = null and unit_amount_decimal = 0.05. You can still pass integer values into unit_amount_decimal, in which case unit_amount is populated in the response. For instance, if you create a price with unit_amount_decimal = 5, the response contains unit_amount = 5 and unit_amount_decimal = 5.0.

NoteIf your integration has event handling that uses unit_amount values and you begin using decimal amounts, you need to use unit_amount_decimal instead. This is important because unit_amount will be returned as null if the decimal amounts can’t be converted into integers, which could cause errors in your integration.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Related Guides[Usage-based billing overview](/docs/billing/subscriptions/usage-based-legacy)[How to record usage](/docs/billing/subscriptions/usage-based-legacy/recording-usage)Products Used[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`