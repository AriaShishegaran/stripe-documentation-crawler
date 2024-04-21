# Build a checkout pageBeta

This custom checkout integration is in private beta. To request access, click here.

[click here.](#)

You can build a custom checkout experience on your website by using Stripe Elements and Custom Checkout, a front-end SDK that manages tax, discounts, shipping rates, and so on.

[Stripe Elements](/payments/elements)

[Set up the serverServer-side](#set-up-server)

## Set up the serverServer-side

Before you begin, you need to register for a Stripe account.

[register](https://dashboard.stripe.com/register)

Use the official Stripe libraries to access the API from your application.

Set the SDK to use the custom_checkout_beta=v1 beta version header.

[Initialize a Checkout SessionServer-side](#initialize-a-checkoutsession)

## Initialize a Checkout SessionServer-side

Add an endpoint on your server that creates a Checkout Session object and returns its client secret to your front end.

[client secret](/api/checkout/sessions/object#checkout_session_object-client_secret)

A Checkout Session represents your customer’s session as they pay for one-time purchases or subscriptions. We recommend creating a new session for each payment attempt. Checkout Sessions expire 24 hours after creation.

For more details about creation parameters, see how to create a Checkout Session.

[create a Checkout Session](/api/checkout/sessions/create)

[Set up the front endClient-side](#set-up-frontend)

## Set up the front endClient-side

Custom Checkout and Elements are automatically available as features of Stripe.js. Include the Stripe.js script on your checkout page by adding it to the head of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

Stripe provides an npm package that you can use to load Stripe.js as a module. See the project on GitHub. Version 3.0.7 or later is required to use Custom Checkout.

[project on GitHub](https://github.com/stripe/stripe-js)

[3.0.7](https://www.npmjs.com/package/%40stripe/stripe-js/v/3.0.7)

Initialize stripe.js with the custom_checkout_beta_2 beta header.

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

Retrieve the client secret from your server and pass it into initCustomCheckout. initCustomCheckout returns a promise resolving to a checkout instance that you can use to read and manipulate the Checkout Session.

[initCustomCheckout](/js/custom_checkout/init)

[checkout](/js/custom_checkout/checkout_object)

[Build your checkout pageClient-side](#build-your-checkout-page)

## Build your checkout pageClient-side

Use the Payment Element to collect payment details. First, create a container DOM element to mount the Payment Element. Then create an instance of the Payment Element using checkout.createElement and mount it by calling element.mount, providing either a CSS selector or the container DOM element.

[checkout.createElement](/js/custom_checkout/create_element?type=payment)

[element.mount](/js/element/mount)

Use the Express Checkout Element to accept payments through one-click buttons, including including Apple Pay, Google Pay, or Link.

[Apple Pay](/apple-pay)

[Google Pay](/google-pay)

[Link](/payments/link)

Create an instance of the Element, passing in a handler function for onConfirm. This function will be called when the customer attempts to complete payment. Call the event.confirm() function within the event payload to finalize payment.

Call checkout.confirm when the customer is ready to complete checkout, such as in response to clicking a pay button.

[checkout.confirm](/js/custom_checkout/confirm)

Before calling confirm, make sure that all required data is present by reading checkout.session.canConfirm. If you’re missing data, you can check for what’s missing by reading checkout.session.confirmationRequirements.

[checkout.session.canConfirm](/js/custom_checkout/session_object#custom_checkout_session_object-canConfirm)

[checkout.session.confirmationRequirements](/js/custom_checkout/session_object#custom_checkout_session_object-confirmationRequirements)

[Handle post-payment eventsServer-side](#handle-post-payment-events)

## Handle post-payment eventsServer-side

Stripe sends a checkout.session.completed event when the payment completes. Use a webhook to receive these events and run actions, such as sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

[webhook](/webhooks/quickstart)

Listen for these events rather than waiting on a callback from the client. On the client, the customer might close the browser window or quit the app before the callback executes. Some payment methods might also take up to 14 days for payment confirmation. Setting up your integration to listen for asynchronous events enables you to accept multiple payment methods with a single integration.

[payment methods](https://stripe.com/payments/payment-methods-guide)

In addition to handling the checkout.session.completed event, we recommend handling other events when collecting payments with Checkout:

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

[checkout.session.async_payment_succeeded](/api/events/types#event_types-checkout.session.async_payment_succeeded)

[checkout.session.async_payment_failed](/api/events/types#event_types-checkout.session.async_payment_failed)

These events all include the Checkout Session object. After the payment succeeds, the underlying PaymentIntent status changes from processing to succeeded.

[Checkout Session](/api/checkout/sessions)

[PaymentIntent](/payments/payment-intents)

[OptionalUpdate line items](#update-line-items)

## OptionalUpdate line items

[OptionalCollect taxes using Stripe Tax](#collect-taxes)

## OptionalCollect taxes using Stripe Tax

[OptionalAdd discounts and promotion codes](#promotion-codes)

## OptionalAdd discounts and promotion codes

[OptionalCollect shipping or billing information](#collect-shipping-or-billing-information)

## OptionalCollect shipping or billing information
