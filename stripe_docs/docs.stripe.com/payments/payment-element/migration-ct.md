# Migrate to Confirmation Tokens

Use this guide to learn how to finalize payments on the server by using a ConfirmationToken instead of a PaymentMethod to send data collected from your client to your server.

[ConfirmationToken](/api/confirmation_tokens/object)

[PaymentMethod](/api/payment_methods)

A ConfirmationToken holds a superset of the data found on a PaymentMethod, such as shipping information, and enables new features as we build them.

[Create the Confirmation Tokenclient-side](#client-side)

## Create the Confirmation Tokenclient-side

Instead of calling stripe.createPaymentMethod, call stripe.createConfirmationToken to create a ConfirmationToken object. Pass this ConfirmationToken to the server to confirm the PaymentIntent.

[stripe.createPaymentMethod](/js/payment_methods/create_payment_method_elements)

[stripe.createConfirmationToken](/js/confirmation_tokens/create_confirmation_token)

The stripe.createConfirmationToken method accepts the same parameters as stripe.createPaymentMethod (through params.payment_method_data), plus additional shipping and return_url parameters.

[params.payment_method_data](/js/confirmation_tokens/create_confirmation_token#create_confirmation_token-options-params-payment_method_data)

[shipping](/js/confirmation_tokens/create_confirmation_token#create_confirmation_token-options-params-shipping)

[return_url](/js/confirmation_tokens/create_confirmation_token#create_confirmation_token-options-params-return_url)

[https://example.com/order/123/complete](https://example.com/order/123/complete)

[Create and submit the payment to Stripeserver-side](#server-side)

## Create and submit the payment to Stripeserver-side

You pass the ConfirmationToken to the server to confirm the PaymentIntent, rather than passing a PaymentMethod as you did before. The properties stored on the ConfirmationToken are applied to the Intent when its ID is provided to the confirmation_token parameter at confirmation time.

[PaymentIntent](/api/payment_intents)

[PaymentMethod](/api/payment_methods)

[confirmation_token](/api/payment_intents/create#create_payment_intent-confirmation_token)

If you already provide shipping and return_url on the ConfirmationToken, you don’t need to provide those fields again when confirming the PaymentIntent.

[shipping](/js/confirmation_tokens/create_confirmation_token#create_confirmation_token-options-params-shipping)

[return_url](/js/confirmation_tokens/create_confirmation_token#create_confirmation_token-options-params-return_url)

[https://example.com/order/123/complete](https://example.com/order/123/complete)

Any parameters provided directly to the PaymentIntent or SetupIntent at confirmation time, such as shipping override corresponding properties on the ConfirmationToken.

[OptionalSetting conditional parameters setup_future_usage or capture_method based on payment method](#conditional-options)

## OptionalSetting conditional parameters setup_future_usage or capture_method based on payment method
