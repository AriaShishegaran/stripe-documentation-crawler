htmlSet up usage-based billing | Stripe Documentation[Skip to content](#main-content)Set up usage-based billing[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fusage-based%2Fimplementation-guide)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fusage-based%2Fimplementation-guide)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Usage-based Billing](/docs/billing/subscriptions/usage-based)# Set up usage-based billing

Understand the major pieces of a usage-based billing integration.NoteWe updated our usage-based billing process. For information on our previous guidance, refer to our legacy usage-based billing documentation.

This guide explains the core concepts of a usage-based billing model through the perspective of a fictional Gen AI company called Alpaca AI. Alpaca AI charges their users 0.04 USD per 1,000 tokens of consumption, billing at the end of the month in arrears.

- Meter events: You send customer-specific information, represented by meter events, to Stripe. These events represent the raw action a customer took in your system, forming the basis of their bill. In our example, this refers to the number of tokens a customer used in a query.
- Meter: Meters, as configuration objects for meter events, provide guidelines on how you want the meter events aggregated over the billing period. In this case, this refers to the sum of tokens over a month. Meters attach to prices, mapping the customer usage to customer subscriptions.
- Meter event summary: The event summary for a customer and meter returns aggregated usage for a period (the meter defines the aggregation formula). In our example, the meter event summary returns the sum() of tokens for a specific customer, meter, and time window. Meter events don’t become available on the read path and are asynchronously aggregated into Meter event summary results.
- Prices: Prices define the unit cost, currency, and billing cycle. In our example, you define a package price of 0.04 USD for 1000 tokens, billed at a monthly interval. Learn more about[Prices](/api/prices).
- Subscription: Subscriptions allow you to charge recurring charges by associating a user with a specific price. Learn more about[Subscriptions](/api/subscriptions).

This diagram demonstrates the core concepts:

## What you will build

This guide shows you how to:

- Model your business by building a[Billing Meter](/api/billing/meter)and product catalog
- Add payment collection session to your site
- Monitor subscription events

[Set up Stripe](#install-setup)Install the Stripe client of your choice:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`Next, install the Stripe CLI. The CLI provides webhook testing, which you can run to make API calls to Stripe.  This guide demonstrates how to use the CLI to set up a pricing model in a later section.

Command Line[homebrew](#)`# Install Homebrew to run this command: https://brew.sh/
brew install stripe/stripe-cli/stripe

# Connect the CLI to your dashboard
stripe login`For additional install options, see Get started with the Stripe CLI.

[Create a meter](#create-meter)Create the meter in the Dashboard or with the API. You can create the meter from the products and prices page in the next step.

DashboardAPI1. Navigate to the[Meters tab](https://dashboard.stripe.com/test/meters)in your product catalog.
2. Click+ Create meter.
3. Enter the name of the meter (in this case, “Alpaca AI tokens”) for display and organization purposes.
4. Enter the event name (in this case,`alpaca_ai_tokens`). You use this name in[Meter Events](/api/billing/meter-event)to report usage to Stripe.
5. Selectsumas the aggregation formula.

Learn more about configuring meters.

[OptionalTest sending usage](#test-send-usage)[Create a pricing model](#create-pricing-model)Create your products and their pricing options in the Dashboard or with the Stripe API.

DashboardAPITo create a metered usage pricing model in the Dashboard:

1. Navigate to the[Products tab](https://dashboard.stripe.com/test/products).
2. Click+ Add product.
3. Enter the name of the product (in this case, “Alpaca AI”).
4. (Optional)Add a description. The description appears at checkout in the[customer portal](/customer-management)and in[quotes](/quotes).

Next, add a recurring price to the Alpaca AI product:

1. SelectUsage-basedandPer package pricingfor the pricing model.
2. Set the amount to 0.04 USD per 1000 units, and the billing period to monthly.
3. Add the meter`alpaca_ai_tokens`. Optionally, create the meter if you haven’t already.

Use the id of this price when you create subscriptions.

Learn more about different pricing models.

[Create a customer](#create-a-customer)You must create a customer for each subscription. In your application frontend, collect any necessary information from your users and pass it to the backend.

On the server, create the Stripe customer object.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d name="John Doe"`[Subscribe customer to the usage-based price](#subscribe-customer-to-usage-based-price)On the backend, subscribe the customer to the usage-based price.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscriptions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d "items[0][price]"={{PRICE_ID}} \
  -d "expand[0]"=pending_setup_intent`This returns a subscription object with a SetupIntent you need to collect payment information.

[Collect payment information](#collect-payment-information)See how to collect payment details with the client secret found in the response from creating the subscription.

[Report usage](#report-usage)You can start recording usage against the meter for the customer using Meter Events. Specify the customer reference and the value in the payload. Stripe bills the reported usage to the customer at the end of the billing period.

Command Line[curl](#)`curl https://api.stripe.com/v1/billing/meter_events \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d event_name=alpaca_ai_tokens \
  -d "payload[value]"=25 \
  -d "payload[stripe_customer_id]"={{CUSTOMER_ID}}`Learn more about recording usage.

[OptionalRender an upcoming invoice](#render-upcoming-invoice)[OptionalQuery reported usage](#query-reported-usage)[OptionalListen for webhooks](#listen-for-webhooks)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[What you will build](#what-you-will-build)[Set up Stripe](#install-setup)[Create a meter](#create-meter)[Create a pricing model](#create-pricing-model)[Create a customer](#create-a-customer)[Subscribe customer to the usage-based price](#subscribe-customer-to-usage-based-price)[Collect payment information](#collect-payment-information)[Report usage](#report-usage)Related Guides[Usage-based pricing models](/docs/billing/subscriptions/usage-based/pricing-models)Products Used[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`