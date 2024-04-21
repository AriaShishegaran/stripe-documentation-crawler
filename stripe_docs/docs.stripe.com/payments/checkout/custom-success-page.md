# Customize redirect behavior with a Stripe-hosted page

After payment succeeds, Stripe redirects your customer to a success page that you create and host on your site.

If you’ve integrated with an embedded payment form, you can’t use the success_url parameter. You must use return_url. Learn more about customizing redirect behavior for integrations with the embedded form.

[customizing redirect behavior](/payments/checkout/custom-redirect-behavior)

## Redirect customers to a success page

You can use the details from a Checkout Session to display an order confirmation page for your customer (for example, their name or payment amount) after the payment. To use the details from a Checkout Session:

[Checkout Session](/api/checkout/sessions)

- Modify the success_url parameter to pass the Checkout Session ID to the client side.

[parameter](/api/checkout/sessions/create#create_checkout_session-success_url)

- Look up the Checkout Session using the ID on your success page.

- Use the Checkout Session to customize what’s displayed on your success page.

## Modify the success URL Server-side

Add the {CHECKOUT_SESSION_ID} template variable to the success_url when you create the Checkout Session. Note that this is a literal string and must be added exactly as you see it here. Do not substitute it with a Checkout Session ID—this happens automatically after your customer pays and is redirected to the success page.

[http://yoursite.com/order/success](http://yoursite.com/order/success)

[http://yoursite.com/order/success?session_id={CHECKOUT_SESSION_ID}](http://yoursite.com/order/success?session_id={CHECKOUT_SESSION_ID})

## Create the success page Server-side

Look up the Checkout Session using the ID and create a success page to display the order information. This example prints out the customer’s name:

[https://youtu.be/8aA9Enb8NVc.](https://youtu.be/8aA9Enb8NVc)

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

## Test the integration

To confirm that your redirect is working as expected:

- Click the checkout button.

- Fill in the customer name and other payment details.

- Click Pay.

If it works, you’re redirected to the success page with your custom message. For example, if you used the message in the code samples, the success page displays this message: Thanks for your order, Jenny Rosen!
