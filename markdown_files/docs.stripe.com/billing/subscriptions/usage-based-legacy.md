htmlUsage-based billing | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fusage-based-legacy)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fusage-based-legacy)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# Usage-based billingLegacy

Charge customers based on how much they use your product or service.NoteWe’ve updated the way usage-based billing works. See the updated usage-based billing docs.

Learn how to migrate.

## Getting started

[Usage-based pricing modelLearn how to model usage-based pricing on Stripe.](/billing/subscriptions/usage-based-legacy/pricing-models)[Record usageRecord the usage of your users and report it to Stripe.](/billing/subscriptions/usage-based-legacy/recording-usage)[Usage-based billing overviewUnderstand the major pieces of a usage-based billing integration.](/billing/subscriptions/usage-based-legacy#sample-integration)## Usage-based billing lifecycle

Here’s what the lifecycle of a usage-based billing looks like.

This diagram illustrates what happens after you’ve implemented a customer experience.

## Sample integration

This example walks through the implementation of a fictional font service called Typographic.

[Create a product and pricing](#create-product)Model your business on stripe with products and prices.

Create your products and their pricing options with the Stripe API or Dashboard. Typographic has three products, each with two tiers:

- Standard  - Tier one: 10 USD per month for 10,000 requests
  - Tier two: An additional $0.10 USD for each request after 10,000


- Growth  - Tier one: 25 USD per month for 10,000 requests
  - Tier two: An additional $0.10 USD for each request after 10,000


- Enterprise  - Tier one: 75 USD per month for 10,000 requests
  - Tier two: An additional $0.0075 USD for each request after 10,000



To achieve this kind of pricing, you charge a flat fee and an additional amount based on how much customers use. With graduated tiers, customers initially pay the flat fee for the first 10,000 requests. If they make more requests than that, they reach tier two and start paying for each additional request. You could also charge solely based on usage without the flat fee.

During each billing period, you create usage records for each customer and then Stripe adds them up to determine how much to bill for. This process is explained in a subsequent step but understanding the default behavior might impact how you create prices.

DashboardAPITo create a metered usage pricing model on Stripe through the Dashboard:

First, create the Standard product. To learn about all the options for creating a product, see the prices guide.

1. Go to theProducts[tab](https://dashboard.stripe.com/products).
2. Click+ Add product.
3. Enter theNameof the product:`Standard`, in this case.
4. (Optional)Add aDescription. The description appears at checkout, on the[customer portal](/customer-management), and in[quotes](/quotes).

Next, create the monthly price for the Standard product. Select Graduated pricing for the Pricing model, then select Recurring.

Create two graduated pricing tiers:

First unitLast unitPer unitFlat feeFor the first010,0000.00 USD10.00 USDFor the next10,001∞0.10 USD0.00 USDThen, select Monthly for the Billing period and check Usage is metered.

Repeat the steps for the Growth and Enterprise products, filling in the appropriate values as necessary.

Read the docs to learn more about different pricing models.

[Sign up customers](#customer-signup)To let your customers sign up for your services, you need to present a payment form on your website. Use Stripe Checkout to embed the form on your site or redirect customers to a Stripe-hosted form. When a customer selects a recurring product and enters their billing information in the Payment Link, Stripe creates two records:

- [Customer](/api/customers/object)
- [Subscription](/api/subscriptions/object)These records are both stored within Stripe.

Stripe offers other options for setting up your payment form:

- [Pricing tables](/payments/checkout/pricing-table): Create a pricing table from the Stripe Dashboard and embed it on your site. When a customer selects a plan, they’re taken to your checkout page. Pricing tables don’t support sub-cent pricing.
- [Web Elements](/payments/elements): Build custom checkout flows to integrate with your site.

[Create a usage record](#report-usage)Throughout each billing period, you need to report usage to Stripe so that customers are billed the correct amounts. You can maintain your own system for recording customer usage and provide usage information for subscriptions to Stripe.

Learn how to record and report usage.

[Test your integration](#test-integration)Test your integration to make sure it behaves as you expect. Learn more about testing subscriptions integrations.

You can use test clocks to test different scenarios, including mock usage records. When you make a usage reporting call, you need to sync the timestamp of the test clock with the usage records. Make a note of the test clock timestamp so that your usage records fall within the same time window. Learn more about test clocks.

[OptionalFree trials](#trials)[OptionalCancellations](#cancellations)[OptionalBilling thresholds](#thresholds)[OptionalAggregate metered usage](#aggregate-metered-usage)[OptionalTransforming quantities](#transforming-quantities)## See also

- [Sample implementation repository](https://github.com/stripe-samples/subscription-use-cases/tree/main/usage-based-subscriptions)
- [Usage-based billing video tutorial](https://www.youtube.com/watch?v=v8cN4pEofy8)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`