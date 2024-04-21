# Set up usage-based billing

We updated our usage-based billing process. For information on our previous guidance, refer to our legacy usage-based billing documentation.

[legacy usage-based billing documentation](/billing/subscriptions/usage-based-legacy)

This guide explains the core concepts of a usage-based billing model through the perspective of a fictional Gen AI company called Alpaca AI. Alpaca AI charges their users 0.04 USD per 1,000 tokens of consumption, billing at the end of the month in arrears.

- Meter events: You send customer-specific information, represented by meter events, to Stripe. These events represent the raw action a customer took in your system, forming the basis of their bill. In our example, this refers to the number of tokens a customer used in a query.

- Meter: Meters, as configuration objects for meter events, provide guidelines on how you want the meter events aggregated over the billing period. In this case, this refers to the sum of tokens over a month. Meters attach to prices, mapping the customer usage to customer subscriptions.

- Meter event summary: The event summary for a customer and meter returns aggregated usage for a period (the meter defines the aggregation formula). In our example, the meter event summary returns the sum() of tokens for a specific customer, meter, and time window. Meter events don’t become available on the read path and are asynchronously aggregated into Meter event summary results.

- Prices: Prices define the unit cost, currency, and billing cycle. In our example, you define a package price of 0.04 USD for 1000 tokens, billed at a monthly interval. Learn more about Prices.

[Prices](/api/prices)

- Subscription: Subscriptions allow you to charge recurring charges by associating a user with a specific price. Learn more about Subscriptions.

[Subscriptions](/api/subscriptions)

This diagram demonstrates the core concepts:

## What you will build

This guide shows you how to:

- Model your business by building a Billing Meter and product catalog

[Billing Meter](/api/billing/meter)

- Add payment collection session to your site

- Monitor subscription events

[Set up Stripe](#install-setup)

## Set up Stripe

Install the Stripe client of your choice:

Next, install the Stripe CLI. The CLI provides webhook testing, which you can run to make API calls to Stripe.  This guide demonstrates how to use the CLI to set up a pricing model in a later section.

[https://brew.sh/](https://brew.sh/)

For additional install options, see Get started with the Stripe CLI.

[Get started with the Stripe CLI](/stripe-cli)

[Create a meter](#create-meter)

## Create a meter

Create the meter in the Dashboard or with the API. You can create the meter from the products and prices page in the next step.

- Navigate to the Meters tab in your product catalog.

[Meters tab](https://dashboard.stripe.com/test/meters)

- Click + Create meter.

- Enter the name of the meter (in this case, “Alpaca AI tokens”) for display and organization purposes.

- Enter the event name (in this case, alpaca_ai_tokens). You use this name in Meter Events to report usage to Stripe.

[Meter Events](/api/billing/meter-event)

- Select sum as the aggregation formula.

Learn more about configuring meters.

[configuring meters](/billing/subscriptions/usage-based/recording-usage#configuring-meter)

[OptionalTest sending usage](#test-send-usage)

## OptionalTest sending usage

[Create a pricing model](#create-pricing-model)

## Create a pricing model

Create your products and their pricing options in the Dashboard or with the Stripe API.

To create a metered usage pricing model in the Dashboard:

- Navigate to the Products tab.

[Products tab](https://dashboard.stripe.com/test/products)

- Click + Add product.

- Enter the name of the product (in this case, “Alpaca AI”).

- (Optional) Add a description. The description appears at checkout in the customer portal and in quotes.

[customer portal](/customer-management)

[quotes](/quotes)

Next, add a recurring price to the Alpaca AI product:

- Select Usage-based and Per package pricing for the pricing model.

- Set the amount to 0.04 USD per 1000 units, and the billing period to monthly.

- Add the meter alpaca_ai_tokens. Optionally, create the meter if you haven’t already.

Use the id of this price when you create subscriptions.

Learn more about different pricing models.

[pricing models](/products-prices/pricing-models)

[Create a customer](#create-a-customer)

## Create a customer

You must create a customer for each subscription. In your application frontend, collect any necessary information from your users and pass it to the backend.

[customer](/api/customers)

On the server, create the Stripe customer object.

[Subscribe customer to the usage-based price](#subscribe-customer-to-usage-based-price)

## Subscribe customer to the usage-based price

On the backend, subscribe the customer to the usage-based price.

This returns a subscription object with a SetupIntent you need to collect payment information.

[SetupIntent](/api/setup_intents)

[Collect payment information](#collect-payment-information)

## Collect payment information

See how to collect payment details with the client secret found in the response from creating the subscription.

[collect payment details](/payments/save-and-reuse?platform=web&ui=elements#collect-payment-details)

[client secret](/api/setup_intents/object#setup_intent_object-client_secret)

[Report usage](#report-usage)

## Report usage

You can start recording usage against the meter for the customer using Meter Events. Specify the customer reference and the value in the payload. Stripe bills the reported usage to the customer at the end of the billing period.

[Meter Events](/api/billing/meter-event)

Learn more about recording usage.

[recording usage](/billing/subscriptions/usage-based/recording-usage#recording-usage)

[OptionalRender an upcoming invoice](#render-upcoming-invoice)

## OptionalRender an upcoming invoice

[OptionalQuery reported usage](#query-reported-usage)

## OptionalQuery reported usage

[OptionalListen for webhooks](#listen-for-webhooks)

## OptionalListen for webhooks
