# Migrate your basic card integration

If you followed the Card payments without bank authentication guide, your integration creates payments that decline when a bank asks the customer to authenticate the purchase.

[Card payments without bank authentication](/payments/without-card-authentication)

If you start seeing many failed payments like the one in the Dashboard below or with an error code of requires_action_not_handled in the API, upgrade your basic integration to handle, rather than decline, these payments.

Use this guide to learn how to upgrade the integration you built in the previous guide to add server and client code that prompts the customer to authenticate the payment by displaying a modal.

See a full sample of this integration on GitHub.

[full sample](https://github.com/stripe-samples/accept-a-payment/tree/master/custom-payment-flow)

[Check if the payment requires authenticationServer-side](#update-server)

## Check if the payment requires authenticationServer-side

Make two changes to the endpoint on your server that creates the PaymentIntent:

- Remove the error_on_requires_action parameter to no longer fail payments that require authentication. Instead, the PaymentIntent status changes to requires_action.

[error_on_requires_action](/api/payment_intents/create#create_payment_intent-error_on_requires_action)

- Add the confirmation_method parameter to indicate that you want to explicitly (manually) confirm the payment again on the server after handling authentication requests.

Then update your “generate response” function to handle the requires_action state instead of erroring:

[Ask the customer to authenticateClient-side](#update-client)

## Ask the customer to authenticateClient-side

Next, update your client-side code to tell Stripe to show a modal if the customer needs to authenticate.

Use stripe.handleCardAction when a PaymentIntent has a status of requires_action. If successful, the PaymentIntent will have a status of requires_confirmation and you need to confirm the PaymentIntent again on your server to finish the payment.

[stripe.handleCardAction](/js#stripe-handle-card-action)

[Confirm the PaymentIntent againServer-side](#update-server-second-confirm)

## Confirm the PaymentIntent againServer-side

Using the same endpoint you set up earlier, confirm the PaymentIntent again to finalize the payment and fulfill the order. The payment attempt fails and transitions back to requires_payment_method if it is not confirmed again within one hour.

[Test the integration](#test-manual)

## Test the integration

Use our test cards in test mode to verify that your integration was properly updated. Stripe displays a fake authentication page inside the modal in test mode that lets you simulate a successful or failed authentication attempt. In live mode the bank controls the UI of what is displayed inside the modal.
