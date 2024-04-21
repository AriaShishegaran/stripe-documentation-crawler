# Card payments without bank authentication

This integration supports businesses accepting only US and Canadian cards. It’s simpler up front, but does not scale to support a global customer base.

Growing or global businesses should use Stripe’s global integration to support bank requests for two-factor authentication and allow customers to pay with more payment methods.

[global integration](/payments/accept-a-payment)

[Build a checkout formClient-side](#web-collect-payment-details)

## Build a checkout formClient-side

Elements, part of Stripe.js, provides drop-in UI components for collecting card information from customers. They are hosted by Stripe and placed into your payment form as an iframe so your customer’s card details never touch your code.

[Elements](/payments/elements)

First, include the Stripe.js script in the head of every page on your site.

[Stripe.js](/js)

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

Including the script on every page of your site lets you take advantage of Stripe’s advanced fraud functionality and ability to detect anomalous browsing behavior.

[advanced fraud functionality](/radar)

This script must always load directly from js.stripe.com to remain PCI compliant. You can’t include the script in a bundle or host a copy of it yourself.

[PCI compliant](/security/guide)

When you use Elements, all payment information is submitted over a secure HTTPS connection.

The address of the page that contains Elements must also start with https:// rather than http://. For more information about getting SSL certificates and integrating them with your server to enable a secure HTTPS connection, see the security documentation.

[security](/security)

Next, you need a Stripe account. Register now.

[Register now](https://dashboard.stripe.com/register)

Create empty DOM elements (containers) with unique IDs within your payment form.

Create an instance of the Stripe object, providing your publishable API key as the first parameter. Afterwards, create an instance of the Elements object and use it to mount a Card element in the empty DOM element container on the page.

[Stripe object](/js#stripe-function)

[API key](/keys)

[Elements object](/js#stripe-elements)

[mount](/js#element-mount)

Use stripe.createPaymentMethod on your client to collect the card details and create a PaymentMethod when the customer submits the payment form. Send the ID of the PaymentMethod to your server.

[stripe.createPaymentMethod](/js/payment_methods/create_payment_method)

[PaymentMethod](/api/payment_methods)

[Set up StripeServer-side](#web-setup)

## Set up StripeServer-side

Use an official library to make requests to the Stripe API from your application:

[Make a paymentServer-side](#web-create-payment-intent)

## Make a paymentServer-side

Set up an endpoint on your server to receive the request from the client.

Stripe uses a PaymentIntent object to represent your intent to collect payment from a customer, tracking charge attempts and payment state changes throughout the process.

[PaymentIntent](/api/payment_intents)

Always decide how much to charge on the server, a trusted environment, as opposed to the client. This prevents malicious customers from being able to choose their own prices.

Create an HTTP endpoint to respond to the AJAX request from step 1. In that endpoint, you should decide how much to charge the customer. To create a payment, create a PaymentIntent using the PaymentMethod ID from step 1 with the following code:

[PaymentMethod](/api/payment_methods)

If you set error_on_requires_action to true when confirming a payment, Stripe automatically fails the payment if it requires two-factor authentication from the user.

[error_on_requires_action](/api/payment_intents/create#create_payment_intent-error_on_requires_action)

When you make a payment with the API, the response includes a status of the PaymentIntent. If the payment was successful, it will have a status of succeeded.

If the payment is declined, the response includes the error code and error message. Here’s an example of a payment that failed because two-factor authentication was required for the card.

[https://stripe.com/docs/error-codes/authentication-required](https://stripe.com/docs/error-codes/authentication-required)

[https://stripe.com/docs/payments/payment-intents/upgrade-to-handle-actions.](https://stripe.com/docs/payments/payment-intents/upgrade-to-handle-actions)

[https://stripe.com/docs/error-codes/authentication-required](https://stripe.com/docs/error-codes/authentication-required)

[https://stripe.com/docs/payments/payment-intents/upgrade-to-handle-actions.](https://stripe.com/docs/payments/payment-intents/upgrade-to-handle-actions)

[Test the integration](#web-test)

## Test the integration

There are several test cards you can use in test mode to make sure this integration is ready. Use them with any CVC, postal code, and future expiration date.

See the full list of test cards.

[test cards](/testing)

[Upgrade your integration to handle card authentication](#web-upgrade-to-handle-card-authentication)

## Upgrade your integration to handle card authentication

Congratulations! You completed a payments integration for basic card payments. Note that this integration declines cards that require authentication during payment.

If you start seeing payments in the Dashboard listed as Failed, then it’s time to upgrade your integration. Stripe’s global integration handles these payments instead of automatically declining them.

[upgrade your integration](/payments/payment-intents/upgrade-to-handle-actions)
