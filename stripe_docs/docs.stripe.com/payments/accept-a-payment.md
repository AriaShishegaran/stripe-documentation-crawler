# Accept a payment

Build a payment form or use a prebuilt checkout page to start accepting online payments.

Redirect to a Stripe-hosted payment page using Stripe Checkout. See how this integration compares to Stripe’s other integration types.

[Stripe Checkout](/payments/checkout)

[compares to Stripe’s other integration types](/payments/accept-a-payment/web/compare-integrations)

[](https://checkout.stripe.dev/)

Redirect to Stripe-hosted payment page

Try it out

[Try it out](https://checkout.stripe.dev/)

[Set up StripeServer-side](#set-up-stripe)

## Set up StripeServer-side

First, register for a Stripe account.

[register](https://dashboard.stripe.com/register)

Use our official libraries to access the Stripe API from your application:

[Redirect your customer to Stripe CheckoutClient-sideServer-side](#redirect-customers)

## Redirect your customer to Stripe CheckoutClient-sideServer-side

Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

[Checkout Session](/api/checkout/sessions/create)

A Checkout Session is the programmatic representation of what your customer sees when they’re redirected to the payment form. You can configure it with options such as:

- Line items to charge

[Line items](/api/checkout/sessions/create#create_checkout_session-line_items)

- Currencies to use

You also need to specify success_url, a page on your website that Checkout returns your customer to after they complete the payment. You can optionally provide cancel_url, a page on your website that Checkout returns your customer to if they cancel the payment process.

Checkout Sessions expire 24 hours after creation.

After creating a Checkout Session, redirect your customer to the URL returned in the response.

[URL](/api/checkout/sessions/object#checkout_session_object-url)

[https://youtu.be/8aA9Enb8NVc.](https://youtu.be/8aA9Enb8NVc)

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

By default, Stripe enables cards and other prevalent payment methods that can help you reach more customers, and you can turn on or turn off payment methods right from the Stripe Dashboard. Stripe evaluates the currency, payment method restrictions, and other parameters to determine the list of supported payment methods to show in Checkout.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

Test your endpoint by starting your web server (for example, localhost:4242) and running the following command:

You should see a response in your terminal that looks like this:

[https://checkout.stripe.com/c/pay/cs_test_...](https://checkout.stripe.com/c/pay/cs_test_..)

You should now have a working checkout button that redirects your customer to Stripe Checkout.

- Click the checkout button.

- You’re redirected to the Stripe Checkout payment form.

If your integration isn’t working:

- Open the Network tab in your browser’s developer tools.

- Click the checkout button and confirm it sent an XHR request to your server-side endpoint (POST /create-checkout-session).

- Verify the request is returning a 200 status.

- Use console.log(session) inside your button click listener to confirm the correct data returned.

To see how your payment methods appear to customers, enter a transaction ID or set an order amount and currency in the Dashboard.

[Dashboard](https://dashboard.stripe.com/settings/payment_methods/review)

[Show a success pageClient-sideServer-side](#success-page)

## Show a success pageClient-sideServer-side

It’s important for your customer to see a success page after they successfully submit the payment form. Host this success page on your site.

Create a minimal success page:

Next, update the Checkout Session creation endpoint to use this new page:

[http://localhost:4242/success.html](http://localhost:4242/success.html)

[http://localhost:4242/cancel.html](http://localhost:4242/cancel.html)

If you want to customize your success page, read the custom success page guide.

[custom success page](/payments/checkout/custom-success-page)

- Click your checkout button.

- Fill out the payment details with the test card information:Enter 4242 4242 4242 4242 as the card number.Enter any future date for card expiry.Enter any 3-digit number for CVC.Enter any billing postal code.

- Enter 4242 4242 4242 4242 as the card number.

- Enter any future date for card expiry.

- Enter any 3-digit number for CVC.

- Enter any billing postal code.

- Click Pay.

- You’re redirected to your new success page.

Next, find the new payment in the Stripe Dashboard. Successful payments appear in the Dashboard’s list of payments. When you click a payment, it takes you to the payment details page. The Checkout summary section contains billing information and the list of items purchased, which you can use to manually fulfill the order.

[list of payments](https://dashboard.stripe.com/payments)

[Test your integration](#additional-testing-resources)

## Test your integration

To test your Stripe-hosted payment form integration:

- Create a Checkout Session.

- Fill out the payment details with a method from the following table.Enter any future date for card expiry.Enter any 3-digit number for CVC.Enter any billing postal code.

- Enter any future date for card expiry.

- Enter any 3-digit number for CVC.

- Enter any billing postal code.

- Click Pay. You’re redirected to your success_url.

- Go to the Dashboard and look for the payment on the Payments page. If your payment succeeded, you’ll see it in that list.

[Payments page](https://dashboard.stripe.com/test/payments?status%5B0%5D=successful)

- Click your payment to see more details, like a Checkout summary with billing information and the list of purchased items. You can use this information to fulfill the order.

Learn more about testing your integration.

[testing your integration](/testing)

[authentication](/strong-customer-authentication)

See Testing for additional information to test your integration.

[Testing](/testing)

You can enable Apple Pay and Google Pay in your payment methods settings. Apple Pay is enabled by default.

[payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

Checkout’s Stripe-hosted pages don’t need integration changes to enable Apple Pay or Google Pay. Stripe handles these payments the same way as other card payments.

[OptionalCreate products and prices](#create-product-prices-upfront)

## OptionalCreate products and prices

[OptionalExisting customersServer-side](#handling-existing-customers)

## OptionalExisting customersServer-side

[OptionalPrefill customer dataServer-side](#prefill-customer-data)

## OptionalPrefill customer dataServer-side

[OptionalSave payment method detailsServer-side](#save-payment-method-details)

## OptionalSave payment method detailsServer-side

[OptionalSeparate authorization and captureServer-side](#auth-and-capture)

## OptionalSeparate authorization and captureServer-side

[OptionalCustomer account managementNo code](#customer-portal)

## OptionalCustomer account managementNo code

Now that you have your basic integration working, learn how to programmatically get a notification whenever a customer pays.

[programmatically get a notification](/payments/checkout/fulfill-orders)

## See also

- Add discounts

[Add discounts](/payments/checkout/discounts)

- Collect taxes

[Collect taxes](/payments/checkout/taxes)

- Collect tax IDs

[Collect tax IDs](/tax/checkout/tax-ids)

- Add shipping

[Add shipping](/payments/collect-addresses?payment-ui=checkout)

- Customize your branding

[Customize your branding](/payments/checkout/customization)

- Customize your success page

[Customize your success page](/payments/checkout/custom-success-page)
