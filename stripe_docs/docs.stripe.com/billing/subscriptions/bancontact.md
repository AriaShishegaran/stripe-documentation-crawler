# Set up a subscription with Bancontact and SEPA Direct Debit

Bancontact is a single use payment method that requires customers to authenticate each payment. After your customer authenticates the payment, Stripe saves your customer’s IBAN in a SEPA Direct Debit payment method. You can then use the SEPA Direct Debit payment method to accept future payments.

[single use](/payments/payment-methods#usage)

[authenticate](/payments/payment-methods#customer-actions)

[IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number)

[SEPA Direct Debit](/payments/sepa-debit)

[accept future payments](/payments/sepa-debit/accept-a-payment)

Check out the sample on GitHub or try the hosted version.

[sample on GitHub](https://github.com/stripe-samples/checkout-single-subscription)

[hosted version](https://checkout.stripe.dev/?mode=subscription)

With this integration, Stripe charges the first Subscription payment through Bancontact to collect your customer’s bank details. If you’re offering a free trial, Stripe charges your customer 0.02 EUR through Bancontact to collect their bank details and immediately refunds it.

A Checkout Session represents the details of your customer’s intent to purchase. You create a Session when your customer wants to start a subscription. After redirecting your customer to a Checkout Session, Stripe presents a payment form where your customer can complete their purchase. After your customer completes a purchase, they’re redirected back to your site.

[Checkout Session](/api/checkout/sessions)

[subscription](/billing/subscriptions/creating)

[Set up StripeServer-side](#web-setup)

## Set up StripeServer-side

Install the Stripe client of your choice:

Install the Stripe CLI (optional). The CLI provides webhook testing, and you can run it to create your products and prices.

[webhook testing](/webhooks#test-webhook)

[https://brew.sh/](https://brew.sh/)

For additional install options, see Get started with the Stripe CLI.

[Get started with the Stripe CLI](/stripe-cli)

[Create the pricing modelDashboardStripe CLI](#create-pricing-model)

## Create the pricing modelDashboardStripe CLI

Create your products and their prices in the Dashboard or with the Stripe CLI.

[products](/api/products)

[prices](/api/prices)

This example uses a fixed-price service with two different service-level options: Basic and Premium. For each service-level option, you need to create a product and a recurring price. (If you want to add a one-time charge for something like a setup fee, create a third product with a one-time price. To keep things simple, this example doesn’t include a one-time charge.)

In this example, each product bills at monthly intervals. The price for the Basic product is 5 EUR. The price for the Premium product is 15 EUR.

Go to the Add a product page and create two products. Add one price for each product, each with a monthly recurring billing period:

[Add a product](https://dashboard.stripe.com/test/products/create)

- Premium product: Premium service with extra featuresPrice: Standard pricing | 15 EUR

Premium product: Premium service with extra features

- Price: Standard pricing | 15 EUR

- Basic product: Basic service with minimum featuresPrice: Standard pricing | 5 EUR

Basic product: Basic service with minimum features

- Price: Standard pricing | 5 EUR

After you create the prices, record the price IDs so you can use them in other  steps. Price IDs look like this: price_G0FvDp6vZvdwRZ.

When you’re ready, use the Copy to live mode button at the top right of the page to clone your product from test mode to live mode.

[test mode to live mode](/keys#test-live-modes)

For other pricing models, see Billing examples.

[Billing examples](/products-prices/pricing-models)

[Create a Checkout SessionClient-sideServer-side](#create-checkout-session)

## Create a Checkout SessionClient-sideServer-side

Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

See Create a Session for a complete list of parameters that you can use.

[Create a Session](/api/checkout/sessions/create)

Create a Session with the ID of an existing Price. Make sure that the mode is set to subscription and that you pass at least one recurring price. You can add one-time prices in addition to recurring prices. After creating the Checkout Session, redirect your customer to the URL returned in the response.

[Price](/api/prices)

[URL](/api/checkout/sessions/object#checkout_session_object-url)

When creating a Session, you can specify payment_method_types or have Stripe automatically pick payment methods based on your Dashboard settings. If you don’t specify payment_method_types, you must turn on Bancontact recurring payments in the Dashboard. This enables SEPA Direct Debit for recurring Bancontact payments only, but doesn’t turn on SEPA Direct Debit payments as a stand alone payment method.

[Dashboard](https://dashboard.stripe.com/settings/payment_methods)

[Dashboard](https://dashboard.stripe.com/settings/payment_methods)

[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})

[https://example.com/cancel](https://example.com/cancel)

When your customer successfully completes their payment, they’re redirected to the success_url, a page on your website that informs the customer that their payment was successful. Make the Session ID available on your success page by including the {CHECKOUT_SESSION_ID} template variable in the success_url as in the above example.

When your customer clicks on your logo in a Checkout Session without completing a payment, Checkout redirects them back to your website by navigating to the cancel_url. Typically, this is the page on your website that the customer viewed prior to redirecting to Checkout.

Checkout Sessions expire 24 hours after creation.

Don’t rely on the redirect to the success_url alone for detecting payment initiation, as:

- Malicious users could directly access the success_url without paying and gain access to your goods or services.

- Customers may not always reach the success_url after a successful payment—they might close their browser tab before the redirect occurs.

[Confirm the payment is successful](#payment-success)

## Confirm the payment is successful

When your customer completes a payment, they’re redirected to the URL that you specified as the success_url. This is typically a page on your website that informs your customer that their payment was successful.

Use the Dashboard, a custom webhook, or a third-party plugin to handle post-payment events like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

[webhook](/webhooks)

Successful payments appear in the Dashboard’s list of payments. When you click a payment, it takes you to the payment detail page. The Checkout summary section contains billing information and the list of items purchased, which you can use to manually fulfill the order.

[list of payments](https://dashboard.stripe.com/payments)

When a customer successfully pays for a recurring service, they’re automatically subscribed. Their subscription is recorded as a new entry in the Dashboard’s list of subscriptions.

[list of subscriptions](https://dashboard.stripe.com/subscriptions)

Stripe can help you keep up with incoming payments by sending you email notifications whenever a customer successfully completes one. Use the Dashboard to configure email notifications.

[configure email notifications](https://dashboard.stripe.com/settings/user)

You can use plugins like Zapier to automate updating your purchase fulfillment systems with information from Stripe payments.

[Zapier](https://stripe.com/works-with/zapier)

Some examples of automation supported by plugins include:

- Updating spreadsheets used for order tracking in response to successful payments

- Updating inventory management systems in response to successful payments

- Triggering notifications to internal customer service teams using email or chat applications

[Test the integration](#testing)

## Test the integration

Using your test API keys, select Bancontact as the payment method and click the Subscribe button. After confirming, you’re redirected to a test page with options to authorize or fail the payment.

[test API keys](/keys#test-live-modes)

- Click Authorize test payment to test the case when the setup is successful.

- Click Fail test payment to test the case when the customer fails to authenticate.

[OptionalCreate a trial for your subscription](#trials)

## OptionalCreate a trial for your subscription

## See also

- Customize your integration

[Customize your integration](/payments/checkout/customization)

- Manage subscriptions with the customer portal

[Manage subscriptions with the customer portal](/billing/subscriptions/build-subscriptions?ui=stripe-hosted)
