# Update payment details

Use the following steps to create a Checkout page that collects your customer’s payment details and returns a Payment Method. Then use the Stripe REST APIs to update the payment method used for future invoices.

[invoices](/api/invoices)

This guide uses Checkout to update subscription payment methods. You can instead implement the Billing customer portal to provide a Stripe-hosted dashboard for your customers to manage their subscriptions and billing details.

[Billing customer portal](/customer-management)

[Set up StripeServer-side](#web-setup)

## Set up StripeServer-side

First, you need a Stripe account. Register now.

[Register now](https://dashboard.stripe.com/register)

Use our official libraries for access to the Stripe API from your application:

[Create a Checkout SessionServer-side](#create-checkout-session)

## Create a Checkout SessionServer-side

To create a setup mode Session, use the mode parameter with a value of setup when creating the Session. See the Checkout Session API reference for a complete list of parameters that you can use for Session creation.

[Checkout Session API reference](/api/checkout/sessions/create)

Append the {CHECKOUT_SESSION_ID} template variable to the success_url to get access to the Session ID after your customer successfully completes a Checkout Session.

Finally, use the setup_intent_data.metadata dictionary to pass your customer’s existing Stripe subscription_id to the Checkout Session. Note that there other ways to pass this data to your server, but we’ll use metadata for this guide.

[setup_intent_data.metadata](/api/checkout/sessions/create#create_checkout_session-setup_intent_data-metadata)

[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})

[https://example.com/cancel](https://example.com/cancel)

[Redirect to CheckoutClient-side](#redirect-checkout)

## Redirect to CheckoutClient-side

Checkout relies on Stripe.js, Stripe’s foundational JavaScript library for building payment flows.

[Stripe.js](/payments/elements)

To get started, include the following script tag on your website—always load it directly from https://js.stripe.com. You can’t include it in a bundle or host it yourself. See Stripe samples for examples.

[Stripe samples](https://github.com/stripe-samples)

Next, create an instance of the Stripe object by providing your publishable API key as the first parameter:

[Stripe object](/js#stripe-function)

[API key](/keys)

To use Checkout on your website, you must add a snippet of code that includes the Session id from the previous step. When your customer is ready to save or update their payment method, call redirectToCheckout and provide the Session id as a parameter.

[previous step](#create-checkout-session)

[redirectToCheckout](/js#stripe-redirect-to-checkout)

This code is typically invoked from an event handler that triggers in response to an action taken by your customer, such as clicking on a payment button.

[Retrieve the Checkout SessionServer-side](#retrieve-checkout-session)

## Retrieve the Checkout SessionServer-side

After a customer successfully completes their Checkout Session, you need to retrieve the Session object. There are two ways to do this:

- Asynchronously: Handle checkout.session.completed webhooks, which contain a Session object. Learn more about setting up webhooks.

[webhooks](/webhooks)

[setting up webhooks](/webhooks)

- Synchronously: Obtain the Session ID from the success_url when a user redirects back to your site. Use the Session ID to retrieve the Session object.

[retrieve](/api/checkout/sessions/retrieve)

The right choice depends on your tolerance for dropoff, as customers may not always reach the success_url after a successful payment. It’s possible for them close their browser tab before the redirect occurs. Handling webhooks prevents your integration from being susceptible to this form of dropoff.

After you have retrieved the Session object, get the value of the setup_intent key, which is the ID for the SetupIntent created during the Checkout Session. A SetupIntent is an object used to set up the customer’s bank account information for future payments.

[SetupIntent](/payments/setup-intents)

Example checkout.session.completed payload:

[https://example.com/cancel](https://example.com/cancel)

[https://example.com/success](https://example.com/success)

Note the setup_intent ID for the next step.

[Retrieve the SetupIntentServer-side](#retrieve-setup-intent)

## Retrieve the SetupIntentServer-side

Using the setup_intent ID, retrieve the SetupIntent object using the /v1/setup_intents/:id endpoint.

[/v1/setup_intents/:id](/api/setup_intents/retrieve)

Example response:

Note the customer ID, subscription_id, and payment_method ID for the next steps.

If you’re requesting this information synchronously from the Stripe API (as opposed to handling webhooks), you can combine the previous step with this step by expanding the SetupIntent object in the request to the /v1/checkout/session endpoint. Doing this prevents you from having to make two network requests to access the newly created PaymentMethod ID.

[expanding](/api/expanding_objects)

[Set a default payment methodServer-side](#set-default-payment-method)

## Set a default payment methodServer-side

There are two ways to ensure that a payment method is used for future invoices:

- Set it as the Customer’s invoice_settings.default_payment_method

- Set it as the Subscription’s default_payment_method

Setting invoice_settings.default_payment_method on the Customer will cause all future invoices for that customer to be paid with the specified payment method.

Setting default_payment_method on the Subscription will cause all future invoices for that subscription to be paid with the specified payment method, overriding any invoice_settings.default_payment_method set on the associated Customer.

Using the customer ID and the PaymentMethod ID you retrieved, set the invoice_settings.default_payment_method for the Customer using the /v1/customers/:id endpoint.

[/v1/customers/:id](/api/customers/update)

All future invoices for this customer will now charge the new PaymentMethod created with the setup mode Checkout Session.

Using the subscription ID and the PaymentMethod ID you retrieved, set the default_payment_method for the subscription using the /v1/subscriptions/:id endpoint.

[/v1/subscriptions/:id](/api/subscriptions/update)

All future invoices for this subscription will now charge the new PaymentMethod created with the setup mode Checkout Session, overriding any invoice_settings.default_payment_method set on the associated Customer.

## See also

Congrats! You can now set a default payment method for future invoices. When testing your integration with your test API key, you can use a test card number to ensure that it works correctly.

[test card number](/testing#cards)

- Test Cards

[Test Cards](/testing#cards)
