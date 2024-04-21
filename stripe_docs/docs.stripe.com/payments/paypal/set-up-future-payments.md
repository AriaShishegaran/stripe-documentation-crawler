# Set up future PayPal payments

## Enable recurring payments support from the Stripe Dashboard

You can request access to the recurring payments directly from the Stripe Dashboard. To do that, go to the Payment Methods Settings page, find PayPal and click Enable next to the Recurring Payments section. You’ll see the pending status. It usually takes up to 5 business days to get access to the recurring payments for PayPal. When access is granted, you’ll see recurring payments on your PayPal settings page.

[Payment Methods Settings](https://dashboard.stripe.com/settings/payment_methods)

[PayPal settings](https://dashboard.stripe.com/settings/payment_methods)

Use Stripe Checkout to collect PayPal payment details in advance, with the final amount or payment date determined later. This is useful for:

[Stripe Checkout](/payments/checkout)

- Saving payment methods to a wallet to streamline future purchases.

- Collecting surcharges after fulfilling a service.

- Starting a free trial for a subscription.

[Starting a free trial for a subscription](/billing/subscriptions/trials)

[Set up StripeServer-side](#set-up-stripe)

## Set up StripeServer-side

First, you need a Stripe account. Register now.

[Register now](https://dashboard.stripe.com/register)

Use our official libraries for access to the Stripe API from your application:

[Create or retrieve a Customer before setupServer-side](#create-customer)

## Create or retrieve a Customer before setupServer-side

To reuse a PayPal payment method for future payments, it must be attached to a Customer.

[Customer](/api/customers)

You should create a Customer object when your customer creates an account on your business. Associating the ID of the Customer object with your own internal representation of a customer will enable you to retrieve and use the stored payment method details later. If your customer hasn’t created an account, you can still create a Customer object now and associate it with your internal representation of the customer’s account later.

[Create a Checkout SessionClient-sideServer-side](#create-checkout-session)

## Create a Checkout SessionClient-sideServer-side

Before you can accept PayPal payments, your customer must authorize you to use their PayPal account for future payments through Stripe Checkout.

Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

[Checkout Session](/api/checkout/sessions)

Create a Checkout Session in setup mode to collect the required information. After creating the Checkout Session, redirect your customer to the URL returned in the response.

[URL](/api/checkout/sessions/object#checkout_session_object-url)

[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})

[https://example.com/cancel](https://example.com/cancel)

When your customer provides their payment method details, they’re redirected to the success_url, a page on your website that informs them that their payment method was saved successfully. Make the Session ID available on your success page by including the {CHECKOUT_SESSION_ID} template variable in the success_url as in the above example.

When your customer clicks on your logo in a Checkout Session without providing their payment method details, Checkout redirects them back to your website by navigating to the cancel_url. This is usually the page on your website that the customer viewed prior to redirecting to Stripe Checkout.

Don’t rely on the redirect to the success_url alone for detecting payment initiation, as:

- Malicious users could directly access the success_url without paying and gain access to your goods or services.

- Customers may not always reach the success_url after a successful payment—they might close their browser tab before the redirect occurs.

[Retrieve the payment methodServer-side](#retrieve-payment-method)

## Retrieve the payment methodServer-side

After a customer submits their payment details, retrieve the PaymentMethod object. A PaymentMethod stores the customer’s PayPal account information for future payments. You can retrieve the PaymentMethod synchronously using the success_url or asynchronously using webhooks.

[PaymentMethod](/payments/payment-methods)

[PaymentMethod](/api/payment_methods)

[webhooks](/webhooks)

The decision to retrieve the PaymentMethod synchronously or asynchronously depends on your tolerance for dropoff, as customers might not always reach the success_url after a successful payment (for example, it’s possible for them to close their browser tab before the redirect occurs). Using webhooks prevents your integration from experiencing this form of dropoff.

Handle checkout.session.completed webhooks, which contain a Session object. To learn more, see setting up webhooks. The following example is a checkout.session.completed response.

[setting up webhooks](/webhooks)

[https://example.com/cancel](https://example.com/cancel)

[https://example.com/success](https://example.com/success)

Note the value of the setup_intent key, which is the ID for the SetupIntent created with the Checkout Session. A SetupIntent is an object used to set up the customer’s PayPal account information for future payments. Retrieve the SetupIntent object with the ID.

[SetupIntent](/payments/setup-intents)

[Retrieve](/api/setup_intents/retrieve)

[Handle post-setup eventsServer-side](#handle-post-setup-events)

## Handle post-setup eventsServer-side

Use a method such as webhooks to confirm the billing agreement was authorized successfully by your customer, instead of relying on your customer to return to the payment status page. When a customer successfully authorizes the billing agreement, the SetupIntent emits the setup_intent.succeeded webhook event. If a customer doesn’t successfully authorize the billing agreement, the SetupIntent will emit the setup_intent.setup_failed webhook event and returns to a status of requires_payment_method. When a customer revokes the billing agreement from their PayPal account, the mandate.updated is emitted.

[webhooks](/payments/payment-intents/verifying-status#webhooks)

[setup_intent.succeeded](/api/events/types#event_types-setup_intent.succeeded)

[webhook](/webhooks)

[setup_intent.setup_failed](/api/events/types#event_types-setup_intent.setup_failed)

[mandate.updated](/api/events/types#event_types-mandate.updated)

[Test the integration](#testing)

## Test the integration

Test your PayPal integration with your test API keys by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent will transition from requires_action to succeeded.

[test API keys](/keys#test-live-modes)

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click Fail test payment. The PaymentIntent will transition from requires_action to requires_payment_method.

[Use the payment method for future paymentsServer-side](#charge-later)

## Use the payment method for future paymentsServer-side

When you’re ready to charge your customer off-session, use the Customer and PaymentMethod IDs to create a PaymentIntent.

[Customer](/api/customers)

[PaymentMethod](/api/payment_methods)

[PaymentIntent](/api/payment_intents)

To find a paypal instrument to charge, list the PaymentMethods associated with your Customer.

[list](/api/payment_methods/list)

When you have the Customer and PaymentMethod IDs, create a PaymentIntent with the amount and currency of the payment. Set a few other parameters to make the off-session payment:

- Set off_session to true to indicate that the customer is not in your checkout flow during this payment attempt. This causes the PaymentIntent to throw an error if authentication is required.

[off_session](/api/payment_intents/confirm#confirm_payment_intent-off_session)

- Set the value of the PaymentIntent’s confirm property to true, which causes confirmation to occur immediately when the PaymentIntent is created.

[confirm](/api/payment_intents/create#create_payment_intent-confirm)

- Set payment_method to the ID of the PaymentMethod and customer to the ID of the Customer.

[payment_method](/api#create_payment_intent-payment_method)

[customer](/api#create_payment_intent-customer)

[User-initiated payment method cancellationServer-side](#web-user-initiated-payment-method-cancellation)

## User-initiated payment method cancellationServer-side

A customer can cancel the subscription (Billing Agreement) through their PayPal account. When they do so, Stripe emits a mandate.updated webhook. All subsequent Payment Intents using the saved Payment Method will fail until you change to a Payment Method with active mandates. When payments fail for Subscriptions, the status changes to the Subscription status configured in your automatic collection settings. Notify the customer of failure and charge them with a different payment method.

[mandate.updated](/api/events/types#event_types-mandate.updated)

[automatic collection settings](/invoicing/automatic-collection)

[charge them with a different payment method](/billing/subscriptions/overview#requires-payment-method)

[OptionalRemove a saved PayPal accountServer-side](#payment-method-detatch)

## OptionalRemove a saved PayPal accountServer-side
