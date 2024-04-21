# Set up a subscription with SEPA Direct Debit

Check out the sample on GitHub or try the hosted version.

[sample on GitHub](https://github.com/stripe-samples/checkout-single-subscription)

[hosted version](https://checkout.stripe.dev/?mode=subscription)

A Checkout Session represents the details of your customer’s intent to purchase. You create a Session when your customer wants to start a subscription. After redirecting your customer to a Checkout Session, Stripe presents a payment form where your customer can complete their purchase. Once your customer has completed a purchase, they will be redirected back to your site.

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

See Create a Session for a complete list of parameters that can be used.

[Create a Session](/api/checkout/sessions/create)

Create a Session with the ID of an existing Price. Ensure that mode is set to subscription and you pass at least one recurring price. You can add one-time prices in addition to recurring prices. After creating the Checkout Session, redirect your customer to the URL returned in the response.

[Price](/api/prices)

[URL](/api/checkout/sessions/object#checkout_session_object-url)

[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})

[https://example.com/cancel](https://example.com/cancel)

When your customer successfully completes their payment, they are redirected to the success_url, a page on your website that informs the customer that their payment was successful. Make the Session ID available on your success page by including the {CHECKOUT_SESSION_ID} template variable in the success_url as in the above example.

When your customer clicks on your logo in a Checkout Session without completing a payment, Checkout redirects them back to your website by navigating to the cancel_url. Typically, this is the page on your website that the customer viewed prior to redirecting to Checkout.

Checkout Sessions expire 24 hours after creation.

From your Dashboard, enable the payment methods you want to accept from your customers. Checkout supports several payment methods.

[Dashboard](https://dashboard.stripe.com/settings/payment_methods)

[several payment methods](/payments/payment-methods/integration-options#payment-method-product-support)

Don’t rely on the redirect to the success_url alone for detecting payment initiation, as:

- Malicious users could directly access the success_url without paying and gain access to your goods or services.

- Customers may not always reach the success_url after a successful payment—they might close their browser tab before the redirect occurs.

[Confirm the payment is successful](#payment-success)

## Confirm the payment is successful

When your customer completes a payment, Stripe redirects them to the URL that you specified in the success_url parameter. Typically, this is a page on your website that informs your customer that their payment was successful.

However, SEPA Direct Debit is a delayed notification payment method, which means that funds aren’t immediately available. A SEPA Direct Debit payment typically takes three business days to make the funds available. Because of this, you’ll want to delay order fulfillment until the funds are available. After the payment succeeds, the underlying PaymentIntent status changes from processing to succeeded.

[PaymentIntent](/payments/payment-intents)

You can confirm the payment is successful in several ways:

Successful payments appear in the Dashboard’s list of payments. When you click a payment, it takes you to the payment detail page. The Checkout summary section contains billing information and the list of items purchased, which you can use to manually fulfill the order.

[list of payments](https://dashboard.stripe.com/payments)

Stripe can help you keep up with incoming payments by sending you email notifications whenever a customer successfully completes one. Use the Dashboard to configure email notifications.

[configure email notifications](https://dashboard.stripe.com/settings/user)

[Test the integration](#testing)

## Test the integration

You can test your integration using the IBANs below. The payment method details are successfully collected for each IBAN but exhibit different behavior when charged.

[OptionalAdding a one-time setup feeServer-side](#adding-setup-fee)

## OptionalAdding a one-time setup feeServer-side

[OptionalCreate prices and products inlineServer-side](#creating-prices-inline)

## OptionalCreate prices and products inlineServer-side

[OptionalExisting customersServer-side](#handling-existing-customers)

## OptionalExisting customersServer-side

[OptionalPrefill customer dataServer-side](#prefilling-customer-data)

## OptionalPrefill customer dataServer-side

[OptionalHandling trialsServer-side](#handling-checkout-trials)

## OptionalHandling trialsServer-side

[OptionalTax ratesServer-side](#tax-rates)

## OptionalTax ratesServer-side

[OptionalAdding couponsServer-side](#coupons)

## OptionalAdding couponsServer-side

## See also

- Customize your integration

[Customize your integration](/payments/checkout/customization)

- Manage subscriptions with the customer portal

[Manage subscriptions with the customer portal](/billing/subscriptions/build-subscriptions?ui=stripe-hosted)
