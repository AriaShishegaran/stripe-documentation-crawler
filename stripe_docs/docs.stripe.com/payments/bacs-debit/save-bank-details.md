# Save Bacs Direct Debit bank details

Use Stripe Checkout to collect Bacs Direct Debit payment details in advance, with the final amount or payment date determined later. This is useful for:

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

[Create a CustomerServer-side](#create-customer)

## Create a CustomerServer-side

To reuse a Bacs Direct Debit payment method for future payments, you must attach it to a Customer. Create a Customer object when someone creates an account with you and associate the ID of the Customer object with your own internal representation of a customer so you can use the stored payment method details later. If you have an existing Customer object, skip this step.

[Customer](/api/customers)

[Create a Checkout SessionClient-sideServer-side](#create-checkout-session)

## Create a Checkout SessionClient-sideServer-side

Stripe Checkout provides a hosted payment page that is compliant with Bacs Direct Debit rules.

[Stripe Checkout](/payments/checkout)

If you would like to design your own Bacs Direct Debit form, please contact our sales team.

[contact](https://stripe.com/contact/sales)

Before you can accept Direct Debit payments, your customer must provide their bank account information and give permission to debit their account (also known as a mandate) through Stripe Checkout.

[mandate](/payments/payment-methods/bacs-debit#mandates)

Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

Create a Checkout Session in setup mode to collect the required information. After creating the Checkout Session, redirect your customer to the URL returned in the response.

[URL](/api/checkout/sessions/object#checkout_session_object-url)

[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})

[https://example.com/cancel](https://example.com/cancel)

When your customer provides their payment method details, they’re redirected to the success_url, a page on your website that informs them that their payment method was saved successfully. Make the Session ID available on your success page by including the {CHECKOUT_SESSION_ID} template variable in the success_url as in the above example.

When your customer clicks on your logo in a Checkout Session without providing their payment method details, Checkout redirects them back to your website by navigating to the cancel_url. This is usually the page on your website that the customer viewed prior to redirecting to Stripe Checkout.

Don’t rely on the redirect to the success_url alone for detecting payment initiation, as:

- Malicious users could directly access the success_url without paying and gain access to your goods or services.

- Customers may not always reach the success_url after a successful payment—they might close their browser tab before the redirect occurs.

The Bacs Direct Debit rules require that customers are sent an email notification when payment details are collected. By default, these emails are sent automatically by Stripe. You can also opt to send your own Bacs notifications.

[send your own Bacs notifications](/payments/payment-methods/bacs-debit#debit-notifications)

[Retrieve the payment methodServer-side](#retrieve-payment-method)

## Retrieve the payment methodServer-side

After a customer submits their payment details, retrieve the PaymentMethod object. A PaymentMethod stores the customer’s bank account information for future payments. You can retrieve the PaymentMethod synchronously using the success_url or asynchronously using webhooks.

[PaymentMethod](/payments/payment-methods)

[PaymentMethod](/api/payment_methods)

[webhooks](/webhooks)

The decision to retrieve the PaymentMethod synchronously or asynchronously depends on your tolerance for dropoff, as customers might not always reach the success_url after a successful payment (for example, it’s possible for them to close their browser tab before the redirect occurs). Using webhooks prevents your integration from experiencing this form of dropoff.

Handle checkout.session.completed webhooks, which contain a Session object. To learn more, see setting up webhooks. The following example is a checkout.session.completed response.

[setting up webhooks](/webhooks)

[https://example.com/cancel](https://example.com/cancel)

[https://example.com/success](https://example.com/success)

Note the value of the setup_intent key, which is the ID for the SetupIntent created with the Checkout Session. A SetupIntent is an object used to set up the customer’s bank account information for future payments. Retrieve the SetupIntent object with the ID.

[SetupIntent](/payments/setup-intents)

[Retrieve](/api/setup_intents/retrieve)

[Handle post-setup eventsServer-side](#handle-post-setup-events)

## Handle post-setup eventsServer-side

Once the Checkout Session completes, payment details are submitted to the bank as a mandate.

The mandate can change at any time after you’ve collected it. This might be the result of the customer instructing their bank to amend the mandate or because of a change in the bank itself (for example, the customer changes to a different one). Stripe sends the following events when the mandate changes:

[mandate.status](/api/mandates/object#mandate_object-status)

These events are available in the Dashboard, but you can set up a webhook to handle these programatically.

[Dashboard](https://dashboard.stripe.com/events)

[webhook](/webhooks)

[Test the integration](#testing)

## Test the integration

There are several test bank account numbers you can use in test mode to make sure this integration is ready.

[test mode](/keys#test-live-modes)

You can test using any of the account numbers provided above. However, because Bacs Direct Debit payments take several days to process, use the test account numbers that operate on a three-minute delay to better simulate the behavior of live payments.

By default, Stripe automatically sends emails to the customer when payment details are initially collected and each time a debit will be made on their account. These notifications aren’t sent in testmode.

[emails](/payments/payment-methods/bacs-debit#debit-notifications)

[Use the payment method for future paymentsServer-side](#charge-later)

## Use the payment method for future paymentsServer-side

After you set up a PaymentMethod, you can accept future Bacs Direct Debit payments by creating and confirming a PaymentIntent.

[PaymentMethod](/api/payment_methods)

[PaymentIntent](/payments/payment-intents)
