# Bacs Direct Debit payments

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

Stripe users in the UK can use Checkout in payment mode to accept Bacs Direct Debit payments.

[Checkout](/payments/checkout)

A Checkout Session represents the details of your customer’s intent to purchase. You create a Session when your customer wants to pay for something. After redirecting your customer to a Checkout Session, Stripe presents a payment form where your customer can complete their purchase. Once your customer has completed a purchase, they are redirected back to your site.

[Checkout Session](/api/checkout/sessions)

[Set up StripeServer-side](#set-up-stripe)

## Set up StripeServer-side

First, you need a Stripe account. Register now.

[Register now](https://dashboard.stripe.com/register)

Use our official libraries for access to the Stripe API from your application:

[Create products and prices](#create-products-and-prices)

## Create products and prices

To use Checkout, you first need to create a Product and a Price. Different physical goods or levels of service should be represented by products. Each product’s pricing is represented by one or more prices.

[Product](/api/products)

[Price](/api/prices)

For example, you can create a T-shirt product that has two prices for different currencies, 20 GBP and 25 EUR. This allows you to change and add prices without needing to change the details of your underlying products. You can either create a product and price through the API or in the Dashboard.

[through the API](/api/prices)

[Dashboard](https://dashboard.stripe.com/products)

If you determine your price at checkout (for example, the customer sets a donation amount) or you prefer not to create prices upfront, you can also create ad-hoc prices at Checkout Session creation using an existing product.

[ad-hoc prices](/payments/accept-a-payment?platform=web#redirect-customers)

If you have an existing Checkout integration that doesn’t use Prices, note that the Checkout API has changed since Prices was introduced. You can use this migration guide to upgrade, or keep your existing integration.

[migration guide](/payments/checkout/migrating-prices)

[keep your existing integration](https://support.stripe.com/questions/prices-api-and-existing-checkout-integrations)

Products created in test mode can be copied to live mode so that you don’t need to re-create them. In the Product detail view in the Dashboard, click Copy to live mode in the upper right corner. You can only do this once for each product created in test mode. Subsequent updates to the test product are not reflected for the live product.

Make sure you are in test mode by toggling the View test data button at the bottom of the Stripe Dashboard. Next, define the items you want to sell. To create a new product and price:

- Navigate to the Products section in the Dashboard

[Products](https://dashboard.stripe.com/test/products)

- Click Add product

- Select One time when setting the price

The product name, description, and image that you supply are displayed to customers in Checkout.

[Create a Checkout SessionClient-sideServer-side](#create-session)

## Create a Checkout SessionClient-sideServer-side

Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

Create a Session with line_items. Line items represent a list of items the customer is purchasing.

[line_items](/api/checkout/sessions/create#create_checkout_session-line_items)

When your customer successfully completes their payment, they are redirected to the success_url, a page on your website that informs the customer that their payment details have been successfully collected and their payment is being processed.

When your customer clicks on your logo in a Checkout Session without completing a payment, Checkout redirects them back to your website by navigating to the cancel_url. Typically, this is the page on your website that the customer viewed prior to redirecting to Checkout.

Checkout can accept a payment and save the payment method for future use. Payment methods saved this way can be used for future payments using a PaymentIntent. After creating the Checkout Session, redirect your customer to the URL returned in the response.

[PaymentIntent](/api/payment_intents/create#create_payment_intent-payment_method)

[URL](/api/checkout/sessions/object#checkout_session_object-url)

[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})

[https://example.com/cancel](https://example.com/cancel)

The Bacs Direct Debit rules require that customers receive debit notification emails when payment details are initially collected and when their account is debitted. Stripe sends these emails for you by default.

[debit notification emails](/payments/payment-methods/bacs-debit#debit-notifications)

Creating a Checkout Session returns a Session ID. Make the Session ID available on your success page by including the {CHECKOUT_SESSION_ID} template variable in the success_url as in the above example.

[Session ID](/api/checkout/sessions/object#checkout_session_object-id)

Don’t rely on the redirect to the success_url alone for detecting payment initiation, as:

- Malicious users could directly access the success_url without paying and gain access to your goods or services.

- Customers may not always reach the success_url after a successful payment—they might close their browser tab before the redirect occurs.

[Handle post-payment eventsServer-side](#async)

## Handle post-payment eventsServer-side

When your customer completes a payment, Stripe redirects them to the URL that you specified in the success_url parameter. Typically, this is a page on your website that informs your customer that their payment was successful.

However, Bacs Direct Debit is a delayed notification payment method, which means that funds are not immediately available. A Bacs Direct Debit payment typically takes 3 business days to make the funds available. Because of this, you’ll want to delay order fulfillment until the funds are available. Once the payment succeeds, the underlying PaymentIntent status changes from processing to succeeded.

[PaymentIntent](/payments/payment-intents)

The following Checkout events are sent when the payment status changes:

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

[checkout.session.async_payment_succeeded](/api/events/types#event_types-checkout.session.async_payment_succeeded)

[checkout.session.async_payment_failed](/api/events/types#event_types-checkout.session.async_payment_failed)

Your webhook code will need to handle all 3 of these Checkout events.

[webhook](/webhooks)

Each Checkout webhook payload includes the Checkout Session object, which contains information about the Customer and PaymentIntent.

[Checkout Session object](/api/checkout/sessions)

[Customer](/api/customers)

[PaymentIntent](/payments/payment-intents)

The checkout.session.completed webhook is sent to your server before your customer is redirected. Your webhook acknowledgement (any 2xx status code) triggers the customer’s redirect to the success_url. If Stripe doesn’t receive successful acknowledgement within 10 seconds of a successful payment, your customer is automatically redirected to the success_url page.

On your success_url page, you’ll want to show a success message to your customer, and let them know that fulfillment of the order will take a few days as the Bacs Direct Debit payment method is not instant.

When accepting instant payments (such as credit cards) in addition to delayed notification payments, you’ll need to update your webhook endpoint to handle both kinds of payments when receiving a checkout.session.completed event.

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

[https://stripe.com/docs/webhooks#verify-events](https://stripe.com/docs/webhooks#verify-events)

You can get information about the customer and payment by retrieving the Customer or PaymentIntent objects referenced by the customer, payment_intent properties in the webhook payload.

To test webhooks locally, you can use Stripe CLI. Once you have it installed, you can forward events to your server:

[Stripe CLI](/stripe-cli)

Learn more about setting up webhooks.

[setting up webhooks](/webhooks)

[Test the integration](#testing)

## Test the integration

By this point you should have a basic Bacs Direct Debit integration that collects bank account details and accepts a payment.

There are several test bank account numbers you can use in test mode to make sure this integration is ready.

[test mode](/keys#test-live-modes)

You can test using any of the account numbers provided above. However, because Bacs Direct Debit payments take several days to process, use the test account numbers that operate on a three-minute delay to better simulate the behavior of live payments.

By default, Stripe automatically sends emails to the customer when payment details are initially collected and each time a debit will be made on their account. These notifications aren’t sent in testmode.

[emails](/payments/payment-methods/bacs-debit#debit-notifications)

## Payment failures

Payments can fail for a variety of reasons. The reason for a failure is available through charge.failure_code. You can only retry payments with certain failure codes. If you can’t retry a payment, we recommend reaching out to the customer and asking them to pay again using a different bank account or a different payment method.

[charge.failure_code](/api/charges/object#charge_object-failure_code)

Below is a list of failure codes we currently send for Bacs Direct Debit. We might add more at any time, so in developing and maintaining your code, don’t assume that only these types exist.

To retry a payment, confirm the PaymentIntent again using the same PaymentMethod.

[confirm the PaymentIntent](/api/payment_intents/confirm)

[PaymentMethod](/api/payment_methods)

To ensure success, we recommend reaching out to the payer before retrying a payment.

## See also

- Payment Intent webhooks

[Payment Intent webhooks](/payments/payment-intents/verifying-status#webhooks)

- Managing Mandates

[Managing Mandates](/payments/payment-methods/bacs-debit#mandates)
