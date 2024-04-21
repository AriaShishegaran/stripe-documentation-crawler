# Set up future Amazon Pay paymentsBeta

[privacy policy](https://stripe.com/privacy)

This guide describes how to save Amazon Pay payment details using Checkout, our fully hosted checkout page.

[Checkout](/payments/checkout)

Learn how to set up a subscription with Amazon Pay to create recurring payments after saving a payment method in Checkout.

[set up a subscription with Amazon Pay](/billing/subscriptions/amazon-pay)

[Set up StripeServer-side](#web-set-up-stripe)

## Set up StripeServer-side

First, you need a Stripe account. Register now.

[Register now](https://dashboard.stripe.com/register)

Use our official libraries for access to the Stripe API from your application:

[Getting permission to save a payment methodServer-side](#web-permissions)

## Getting permission to save a payment methodServer-side

If you save your customer’s payment method for future use, you need permission. Creating an agreement (sometimes called a mandate) up front allows you to save your customer’s payment details and charge them when they’re not actively using your website or app.

Add terms to your website or app that state how you plan to save your customer’s payment method details, and let them opt in. If you plan to charge your customer when they’re offline, make sure that your terms also include the following:

- The customer’s permission for you to initiate a payment or a series of payments on their behalf for specified transactions

- The anticipated frequency (that is, one-time or recurring) and timing of payments

- How you determine the payment amount

- Your cancellation policy, if you’re setting up the payment method for a subscription service

Make sure that you keep a record of your customer’s written agreement to these terms.

[Create or retrieve a CustomerServer-side](#web-create-customer)

## Create or retrieve a CustomerServer-side

To reuse an Amazon Pay payment method for future payments, attach it to a Customer.

[Customer](/api/customers)

Create a Customer object when your customer creates an account with your business, and associate the ID of the Customer object with your own internal representation of that customer. Alternatively, you can create a new Customer before saving a payment method for future payments.

[Customer object](/api/customers)

Create a new Customer or retrieve an existing Customer to associate with this payment. Include the following code on your server to create a new Customer:

[Create a Checkout SessionServer-side](#web-create-checkout-session)

## Create a Checkout SessionServer-side

Your customer must authorize you to use their Amazon account for future payments through Stripe Checkout. This allows you to accept Amazon payments. Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

[Checkout Session](/api/checkout/sessions)

Create a Checkout Session in setup mode to collect the required information. After creating the Checkout Session, redirect your customer to the URL that the response returns.

[URL](/api/checkout/sessions/object#checkout_session_object-url)

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

[Test your integration](#web-test-integration)

## Test your integration

Select Amazon Pay as the payment method, then click Continue to Amazon Pay. You can test the successful setup case by authenticating the SetupIntent on the redirect page. The SetupIntent transitions from requires_action to succeeded.
