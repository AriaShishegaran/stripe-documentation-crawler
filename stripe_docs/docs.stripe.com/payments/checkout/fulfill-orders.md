# Fulfill orders with Checkout

After you integrate Stripe Checkout or create a Stripe Payment Link to take your customers to a payment form, you need notification that you can fulfill their order after they pay.

[Stripe Checkout](https://stripe.com/payments/checkout)

[Stripe Payment Link](https://stripe.com/payments/payment-links)

In this guide, you’ll learn how to:

- Receive an event notification when a customer pays you.

- Handle the event.

- Use Stripe CLI to quickly test your new event handler.

[Stripe CLI](/stripe-cli)

- Optionally, handle additional payment methods.

- Turn on your event handler in production.

[Install Stripe CLI](#install-stripe-cli)

## Install Stripe CLI

The quickest way to develop and test webhooks locally is with the Stripe CLI.

[webhooks](/webhooks)

[Stripe CLI](/stripe-cli)

As a first step, follow the install guide for Stripe CLI.

[install guide](/stripe-cli#install)

Once you have the Stripe CLI installed and have completed the login process, you’re ready to move on to the next step.

[Create your event handlerServer-side](#create-event-handler)

## Create your event handlerServer-side

In this section, you’ll create a small event handler so Stripe can send you a checkout.session.completed event when a customer completes checkout.

First, create a new route for your event handler. Start by printing out the event you receive. You’ll verify that delivery is working in the next step:

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

Run your server (for example, on localhost:4242). Next, set up Stripe CLI to forward events to your local server, so you can test your event handler locally:

Next, go through Checkout as a customer:

- Click your checkout button (you probably set this up in the Accept a payment guide)

[Accept a payment guide](/payments/accept-a-payment?integration=checkout)

- Fill out your payment form with test dataEnter 4242 4242 4242 4242 as the card numberEnter any future date for card expiryEnter any 3-digit number for CVVEnter any billing postal code (90210)

- Enter 4242 4242 4242 4242 as the card number

- Enter any future date for card expiry

- Enter any 3-digit number for CVV

- Enter any billing postal code (90210)

- Click the Pay button

You should see:

- A checkout.session.completed in the stripe listen output

- A print statement from your server’s event logs with the checkout.session.completed event

Now that you’ve verified event delivery, you can add a bit of security to make sure that events are only coming from Stripe.

Anyone can POST data to your event handler. Before processing an event, always verify that it came from Stripe before trusting it. The official Stripe library has built-in support for verifying webhook events, which you’ll update your event handler with:

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

[https://stripe.com/docs/webhooks#verify-events](https://stripe.com/docs/webhooks#verify-events)

Go through the testing flow from the previous step. You should still see the checkout.session.completed event being printed out successfully.

Next, try hitting the endpoint with an unsigned request:

You should get a 400 Bad Request error, because you tried to send an unsigned request to your endpoint.

Now that the basics of the event handler are set up, you can move on to fulfilling the order.

[Fulfill the orderServer-side](#fulfill)

## Fulfill the orderServer-side

To fulfill the order, you’ll need to handle the checkout.session.completed event. Depending on which payment methods you accept (for example, cards, mobile wallets), you’ll also optionally handle a few extra events after this basic step.

Now that you have the basic structure and security in place to make sure any event you process came from Stripe, you can handle the checkout.session.completed event. This event includes the Checkout Session object, which contains details about your customer and their payment.

[Checkout Session](/api/checkout/sessions)

[customer](/api/checkout/sessions/object#checkout_session_object-customer)

[payment](/api/checkout/sessions/object#checkout_session_object-customer)

When handling this event, you might also consider:

- Saving a copy of the order in your own database.

- Sending the customer a receipt email.

- Reconciling the line items and quantity purchased by the customer if using line_item.adjustable_quantity. If the Checkout Session has many line items you can paginate through them with the line_items.

[line_items](/api/checkout/sessions/line_items)

Add code to your event handler to fulfill the order:

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

[https://stripe.com/docs/webhooks#verify-events](https://stripe.com/docs/webhooks#verify-events)

You can configure Checkout to redirect your customers after receiving webhook events. Checkout handles these webhook-triggered redirects slightly differently depending on whether you use the embedded form or a Stripe-hosted page.

[acknowledge that you received the event](/webhooks#acknowledge-events-immediately)

Ensure that stripe listen is still running. Go through Checkout as a test user, just like in the prior steps. Your event handler should receive a checkout.session.completed event, and you should have successfully handled it.

[Handle delayed notification payment methodsServer-side](#delayed-notification)

## Handle delayed notification payment methodsServer-side

This step is only required if you plan to use any of the following payment methods: Bacs Direct Debit, Bank transfers, Boleto, Canadian pre-authorized debits, Konbini, OXXO, SEPA Direct Debit, SOFORT, or ACH Direct Debit.

[Bacs Direct Debit](/payments/bacs-debit/accept-a-payment)

[Bank transfers](/payments/bank-transfers/accept-a-payment)

[Boleto](/payments/boleto/accept-a-payment)

[Canadian pre-authorized debits](/payments/acss-debit/accept-a-payment)

[Konbini](/payments/konbini/accept-a-payment)

[OXXO](/payments/oxxo/accept-a-payment)

[SEPA Direct Debit](/payments/sepa-debit/accept-a-payment)

[SOFORT](/payments/sofort/accept-a-payment)

[ACH Direct Debit](/payments/ach-debit/accept-a-payment)

When receiving payments with a delayed notification payment method, funds aren’t immediately available. It can take multiple days for funds to process so you should delay order fulfillment until the funds are available in your account. After the payment succeeds, the underlying PaymentIntent status changes from processing to succeeded.

[PaymentIntent](/payments/payment-intents)

You’ll need to handle the following Checkout events:

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

[checkout.session.async_payment_succeeded](/api/events/types#event_types-checkout.session.async_payment_succeeded)

[checkout.session.async_payment_failed](/api/events/types#event_types-checkout.session.async_payment_failed)

These events all include the Checkout Session object.

[Checkout Session](/api/checkout/sessions)

Update your event handler to fulfill the order:

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

[https://stripe.com/docs/webhooks#verify-events](https://stripe.com/docs/webhooks#verify-events)

Ensure that stripe listen is still running. Go through Checkout as a test user, like you did in the prior steps. Your event handler should receive a checkout.session.completed event, and you should have successfully handled it.

Now that you’ve completed these steps, you’re ready to go live in production whenever you decide to do so.

[Go live in production](#go-live)

## Go live in production

After you’ve deployed your event handler endpoint to production, you need to register your live URL with Stripe. Follow the guide to register a webhook.

[register a webhook](/webhooks#register-webhook)
