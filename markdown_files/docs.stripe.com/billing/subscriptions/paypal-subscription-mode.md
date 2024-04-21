htmlSet up a subscription with PayPal | Stripe Documentation[Skip to content](#main-content)PayPal in Checkout[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fpaypal-subscription-mode)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fpaypal-subscription-mode)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Subscriptions](/docs/subscriptions)[Manage subscription cycles](/docs/billing/subscriptions/change)[Set payment methods for subscriptions](/docs/billing/subscriptions/payment-methods-setting)# Set up a subscription with PayPal

Use Stripe Checkout with Stripe Billing to set up recurring payments.### Stripe sample

Check out the sample on GitHub or try the hosted version.

A Checkout Session represents the details of your customer’s intent to purchase. You create a Session when your customer wants to start a subscription. After redirecting your customer to a Checkout Session, Stripe presents a payment form where your customer can complete their purchase. Once your customer has completed a purchase, they will be redirected back to your site.

CautionTo start accepting PayPal subscriptions on Stripe, you need to enable PayPal recurring payments from the Dashboard.

[Set up StripeServer-side](#web-setup)First, you need a Stripe account. Register now.

Use our official libraries for access to the Stripe API from your application:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`[Create recurring products and prices](#create-products-and-prices)CautionThe Prices API unifies how one-time purchases and subscriptions are modeled on Stripe. Existing integrations that don’t use the Prices API are still supported. However, some Checkout features only support Prices. See the migration guide to upgrade to the Prices API.

To use Checkout, you first need to create a Product and a Price. Different physical goods or levels of service should be represented by products. Each product’s pricing is represented by one or more prices.

For example, you can create a software product that has four prices: 10 USD/month, 100 USD/year, 9 eur/month, and 90 eur/year. This allows you to change and add prices without needing to change the details of your underlying products. You can either create a product and price through the API or through the Stripe Dashboard.

If your price is determined at checkout (for example, the customer sets a donation amount) or you prefer not to create prices upfront, you can create prices inline at Checkout Session creation.

DashboardAPIBefore you start configuring products, make sure you are in test mode by toggling the View test data button at the bottom of the Stripe Dashboard. Next, define the goods and services you plan to sell. To create a new product and price:

- Navigate to the[Products](https://dashboard.stripe.com/products)section in the Dashboard
- ClickAdd product
- Select “Recurring” when setting the price
- Configure the pricing plan

You can define multiple pricing plans with different parameters for each recurring product. Each price has a generated ID that you can use as a reference during the checkout process.

NoteProducts created in test mode can be copied to live mode so that you don’t need to re-create them. In the Product detail view in the Dashboard, click Copy to live mode on the upper right corner. You can only do this once for each product created in test mode. Subsequent updates to the test product are not reflected for the live product.

[Create a Checkout SessionClient-sideServer-side](#create-checkout-session)Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

index.html`<html>
  <head>
    <title>Checkout</title>
  </head>
  <body>
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>`### Session parameters

See Create a Session for a complete list of parameters that can be used.

Create a Session with the ID of an existing Price. Ensure that mode is set to subscription and you pass at least one recurring price. You can add one-time prices in addition to recurring prices. After creating the Checkout Session, redirect your customer to the URL returned in the response.

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "payment_method_types[]"="paypal" \
  -d "line_items[][price]"={{PRICE_ID}} \
  -d "line_items[][quantity]"=1 \
  -d "mode"="subscription" \
  -d "success_url"="https://example.com/success?session_id={CHECKOUT_SESSION_ID}" \
  -d "cancel_url"="https://example.com/cancel" \`When your customer successfully completes their payment, they are redirected to the success_url, a page on your website that informs the customer that their payment was successful. Make the Session ID available on your success page by including the {CHECKOUT_SESSION_ID} template variable in the success_url as in the above example.

When your customer clicks on your logo in a Checkout Session without completing a payment, Checkout redirects them back to your website by navigating to the cancel_url. Typically, this is the page on your website that the customer viewed prior to redirecting to Checkout.

Checkout Sessions expire 24 hours after creation.

CautionDon’t rely on the redirect to the success_url alone for detecting payment initiation, as:

- Malicious users could directly access the`success_url`without paying andgain access to your goods or services.
- Customers may not always reach the`success_url`after a successful payment—they might close their browser tab before the redirect occurs.

[Confirm the payment is successful](#payment-success)NoteWhen a buyer successfully confirms a subscription on Stripe with PayPal, they receive a receipt from Stripe as well as from PayPal.

When your customer completes a payment, they’re redirected to the URL that you specified as the success_url. This is typically a page on your website that informs your customer that their payment was successful.

Use the Dashboard, a custom webhook, or a third-party plugin to handle post-payment events like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

DashboardWebhooksSuccessful payments appear in the Dashboard’s list of payments. When you click a payment, it takes you to the payment detail page. The Checkout summary section contains billing information and the list of items purchased, which you can use to manually fulfill the order.

![Checkout summary](https://b.stripecdn.com/docs-statics-srv/assets/source.16d3029596357c80a8efdbbfe106108a.png)

NoteStripe can help you keep up with incoming payments by sending you email notifications whenever a customer successfully completes one. Use the Dashboard to configure email notifications.

You can use plugins like Zapier to automate updating your purchase fulfillment systems with information from Stripe payments.

Some examples of automation supported by plugins include:

- Updating spreadsheets used for order tracking in response to successful payments
- Updating inventory management systems in response to successful payments
- Triggering notifications to internal customer service teams using email or chat applications

[Test the integration](#testing)Test your PayPal integration with your test API keys by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent will transition from requires_action to succeeded.

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click Fail test payment. The PaymentIntent will transition from requires_action to requires_payment_method.

[OptionalAdding a one-time setup feeServer-side](#adding-setup-fee)[OptionalCreate prices and products inlineServer-side](#creating-prices-inline)[OptionalExisting customersServer-side](#handling-existing-customers)[OptionalPrefill customer dataServer-side](#prefilling-customer-data)[OptionalHandling trialsServer-side](#handling-checkout-trials)[OptionalTax ratesServer-side](#tax-rates)[OptionalAdding couponsServer-side](#coupons)## See also

- [Customize your integration](/payments/checkout/customization)
- [Manage subscriptions with the customer portal](/billing/subscriptions/build-subscriptions?ui=stripe-hosted)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up Stripe](#web-setup)[Create recurring products and prices](#create-products-and-prices)[Create a Checkout Session](#create-checkout-session)[Confirm the payment is successful](#payment-success)[Test the integration](#testing)[See also](#see-also)Products Used[Billing](/billing)[Payments](/payments)[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`