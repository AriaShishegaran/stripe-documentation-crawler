# Building a custom storefront

Adobe Commerce can operate as a headless commerce platform that’s decoupled from its storefront. You can use the REST API or GraphQL API to build custom storefronts, such as progressive web apps (PWA), mobile apps, or frontends based on React, Vue, or other frameworks.

The Stripe module extends the REST API and GraphQL API with the following functionality:

- Setting payment method tokens during order placement

- Performing 3D Secure customer authentication

- Managing customers’ saved payment methods

The Stripe module uses the REST API on the checkout page. You can find examples of how to use the API in the Stripe module directory under the examples/ subdirectory.

The following example uses the GraphQL API to build a custom storefront.

[Tokenize a payment method during the checkout flow](#tokenize-payment-method)

## Tokenize a payment method during the checkout flow

You can use the PaymentElement to collect a payment method from the customer during checkout. After the customer provides their payment method details and clicks Place Order, you can tokenize the payment method and use it to place the order. Calling createPaymentMethod generates a payment method token from the details provided in the PaymentElement.

[PaymentElement](/payments/payment-element)

[generates a payment method token](/payments/finalize-payments-on-the-server-legacy?type=payment#create-pm)

[Pass the tokenized payment method](#pass-tokenized-payment-method)

## Pass the tokenized payment method

After you obtain a payment method token, you must call setPaymentMethodOnCart to set the payment method on the order.

[set the payment method](https://developer.adobe.com/commerce/webapi/graphql/tutorials/checkout/set-payment-method/#set-payment-method-on-cart)

Use the following parameters for setPaymentMethodOnCart:

[Place the order](#place-order)

## Place the order

After you set the payment method token, you can use the Adobe Commerce placeOrder mutation to place an order:

The example above requests a client_secret, which isn’t a default placeOrder mutation parameter. The Stripe module adds this parameter for you to use after the order is placed to finalize details specific to the selected payment method. You can finalize payment with the stripe.handleNextAction(client_secret) method. Options include performing an inline 3D Secure authentication for cards, displaying a printable voucher for certain payment methods, or redirecting the customer externally for authentication.

[Manual authentication](#manual-authentication)

## Manual authentication

Payment methods that require customer authentication go through the following process:

- The order is placed in pending status.

- Control is passed to the frontend to perform the authentication.

- After successful authentication, payment is collected.

- A charge.succeeded webhook event passes to your website.

- The module handles the event, and changes the order status from pending to processing.

Card payments receive synchronous payment confirmation, so you can wait to place an order until after the payment succeeds. To do so, pass the manual_authentication parameter on the setPaymentMethodOnCart mutation: 'manual_authentication': "card"

If customer authentication is required and you pass this parameter, the order won’t be placed and the frontend receives an error with the client_secret. You can then use the client_secret to manually authenticate the payment and call the placeOrder mutation after a successful authentication. The second order placement creates and saves the order in a processing status using the already successful payment.

[Retrieve saved payment methods](#retrieve-payment-methods)

## Retrieve saved payment methods

You can use listStripePaymentMethods to retrieve a list of saved payment methods for a customer in an active checkout session.

[Save a payment method](#save-payment-method)

## Save a payment method

You can use addStripePaymentMethod to save payment methods to a customer’s account. The payment_method parameter is the tokenized payment method ID. The tokenization process is similar to the tokenization process during the checkout flow.

[Delete a saved payment method](#delete-payment-method)

## Delete a saved payment method

You can use deleteStripePaymentMethod to allow customers to delete saved payment methods from their account.

For most use cases, we recommend passing a payment method fingerprint, which deletes all payment methods that match the fingerprint. The listStripePaymentMethods mutation automatically removes duplicates before returning recently added payment methods that match a specific fingerprint. But if you only delete a payment method by ID, the results of listStripePaymentMethods might include an older saved payment method with the same fingerprint.

## See also

- SetupIntents API

[SetupIntents API](/payments/setup-intents)

- Using the Adobe Commerce admin panel

[Using the Adobe Commerce admin panel](/connectors/adobe-commerce/admin)

- Troubleshooting

[Troubleshooting](/connectors/adobe-commerce/troubleshooting)
