# Accept card payments without webhooks

Stripe recommends using the newer Payment Element instead of the Card Element. It allows you to accept multiple payment methods with a single Element. Learn more about when to use the Card Element and Payment Element.

[Payment Element](/payments/quickstart)

[when to use the Card Element and Payment Element](/payments/payment-card-element-comparison)

For a wider range of support and future proofing, use the standard integration for asynchronous payments.

[standard integration](/payments/accept-a-payment)

This integration waits for the returned response from the client and finalizes a payment on the server, without using webhooks or processing offline events. While it may seem simpler, this integration is difficult to scale as your business grows and has several limitations:

[webhooks](/webhooks)

If you’re migrating an existing Stripe integration from the Charges API, follow the migration guide.

[migration guide](/payments/payment-intents/migration)

- Only supports cards—You’ll have to write more code to support ACH and popular regional payment methods separately.

- Double-charge risk—By synchronously creating a new PaymentIntent each time your customer attempts to pay, you risk accidentally double-charging your customer. Be sure to follow best practices.

[best practices](/error-low-level#idempotency)

- Extra trip to client—​​Cards with 3D Secure or those that are subject to regulations such as Strong Customer Authentication require extra steps on the client. ​

[Strong Customer Authentication](/strong-customer-authentication)

Keep these limitations in mind if you decide to use this integration. Otherwise, use the standard integration.

[standard integration](/payments/accept-a-payment)

[Set up Stripe](#web-setup)

## Set up Stripe

First, you need a Stripe account. Register now.

[Register now](https://dashboard.stripe.com/register)

Use our official libraries for access to the Stripe API from your application:

[Collect card detailsClient-side](#web-collect-card-details)

## Collect card detailsClient-side

Collect card information on the client with Stripe.js and Stripe Elements. Elements is a set of prebuilt UI components for collecting and validating card number, postal code, and expiration date.

A Stripe Element contains an iframe that securely sends the payment information to Stripe over an HTTPS connection. The checkout page address must also start with https:// rather than http:// for your integration to work.

You can test your integration without using HTTPS. Enable it when you’re ready to accept live payments.

[Enable it](/security/guide#tls)

Include the Stripe.js script in the head of every page on your site. Elements is automatically available as a feature of Stripe.js.

[Stripe.js](/js)

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

Including the script on every page of your site lets you take advantage of Stripe’s advanced fraud functionality and ability to detect anomalous browsing behavior.

[advanced fraud functionality](/radar)

To securely collect card details from your customers, Elements creates UI components for you that are hosted by Stripe. They’re then placed into your payment form as an iframe. To determine where to insert these components, create empty DOM elements (containers) with unique IDs within your payment form.

Next, create an instance of the Stripe object, providing your publishable API key as the first parameter. Afterwards, create an instance of the Elements object and use it to mount a Card element in the relevant placeholder in the page.

[Stripe object](/js#stripe-function)

[API key](/keys)

[Elements object](/js#stripe-elements)

[mount](/js#element-mount)

[View full sample](https://github.com/stripe-samples/accept-a-payment/blob/main/custom-payment-flow/client/html/card.js#L63-L73)

The card Element simplifies the form and minimizes the number of fields required by inserting a single, flexible input field that securely collects all necessary card details.

Otherwise, combine cardNumber, cardExpiry, and cardCvc Elements for a flexible, multi-input card form.

Always collect a postal code to increase card acceptance rates and reduce fraud.

The single line Card Element automatically collects and sends the customer’s postal code to Stripe. If you build your payment form with split Elements (Card Number, Expiry, CVC), add a separate input field for the customer’s postal code.

[single line Card Element](/js/element/other_element?type=card)

[Card Number](/js/element/other_element?type=cardNumber)

[Expiry](/js/element/other_element?type=cardExpiry)

[CVC](/js/element/other_element?type=cardCvc)

Finally, use stripe.createPaymentMethod on your client to collect the card details and create a PaymentMethod when the user clicks the submit button.

[stripe.createPaymentMethod](/js/payment_methods/create_payment_method)

[PaymentMethod](/api/payment_methods)

[Submit the PaymentMethod to your serverClient-side](#web-send-to-server)

## Submit the PaymentMethod to your serverClient-side

If the PaymentMethod was created successfully, send its ID to your server.

[PaymentMethod](/api/payment_methods)

[Confirm the PaymentIntent againServer-side](#confirm-payment)

## Confirm the PaymentIntent againServer-side

This code is only executed when a payment requires additional authentication—just like the handling in the previous step. The code itself isn’t optional because any payment could require this extra step.

Using the same endpoint you set up above, confirm the PaymentIntent again to finalize the payment and fulfill the order. Make sure this confirmation happens within one hour of the payment attempt. Otherwise, the payment fails and transitions back to requires_payment_method.

[above](#create-payment-intent)

[Handle any next actionsClient-side](#web-handle-next-actions)

## Handle any next actionsClient-side

Write code to handle situations that require your customer to intervene. A payment normally succeeds after you confirm it on the server in step 4. However, when the PaymentIntent requires additional action from the customer, such as authenticating with 3D Secure, this code comes into play.

[step 4](#create-payment-intent)

[3D Secure](/payments/3d-secure)

Use stripe.handleCardAction to trigger the UI for handling customer action. If authentication succeeds, the PaymentIntent has a status of requires_confirmation. Confirm the PaymentIntent again on your server to finish the payment.

[stripe.handleCardAction](/js/payment_intents/handle_card_action)

While testing, use a test card number that requires authentication (for example, 4000002760003184) to force this flow. Using a card that doesn’t require authentication (for example, 4242424242424242) skips this part of the flow and completes at step 4.

[test card number](/testing#regulatory-cards)

stripe.handleCardAction may take several seconds to complete. During that time, disable your form from being resubmitted and show a waiting indicator like a spinner. If you receive an error, show it to the customer, re-enable the form, and hide the waiting indicator. If the customer must perform additional steps to complete the payment, such as authentication, Stripe.js walks them through that process.

[Confirm the PaymentIntent againServer-side](#confirm-payment)

## Confirm the PaymentIntent againServer-side

This code is only executed when a payment requires additional authentication—just like the handling in the previous step. The code itself isn’t optional because any payment could require this extra step.

Using the same endpoint you set up above, confirm the PaymentIntent again to finalize the payment and fulfill the order. Make sure this confirmation happens within one hour of the payment attempt. Otherwise, the payment fails and transitions back to requires_payment_method.

[above](#create-payment-intent)

[Test the integration](#web-test-integration)

## Test the integration

​​Several test cards are available for you to use in test mode to make sure this integration is ready. Use them with any CVC and an expiration date in the future.

For the full list of test cards see our guide on testing.

[testing](/testing)

[OptionalRecollect a CVC](#web-recollect-cvc)

## OptionalRecollect a CVC
