# Use Payment Element across multiple processorsBeta

Use Payment Element to build a custom payment flow that allows you to collect card details, create a PaymentMethod, and forward the payment method to a third-party processor.

[Payment Element](/payments/payment-element)

[PaymentMethod](/api/payment_methods)

[forward](/api/forwarding/request)

To gain access to use Stripe’s forwarding service, contact your Stripe representative or Stripe support.

[Stripe support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520access%2520the%2520Vault%2520and%2520Forward%2520API%3F%26body%3DWhat%2520endpoint%28s%29%2520would%2520you%2520like%2520to%2520forward%2520card%2520details%2520to%3F)

[Create a PaymentMethodClient-side](#create-payment-method)

## Create a PaymentMethodClient-side

Use a Payment Element to collect payment details. If you’re not integrated with the Payment Element, learn how to get started. After the customer submits your payment form, call stripe.createPaymentMethod to create a PaymentMethod. Pass the PaymentMethod ID to the ForwardingRequest endpoint on your server.

[get started](/payments/accept-a-payment)

[stripe.createPaymentMethod](/js/payment_methods/create_payment_method)

[PaymentMethod](/api/payment_methods)

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

[Create a ForwardingRequest](#create-forwarding-request)

## Create a ForwardingRequest

Contact your Stripe representative to configure your destination endpoint and begin forwarding transactions. Send the card details to this test endpoint before you connect your integration with your third-party processor.

[configure](/payments/vault-and-forward#configuring)

[Handle the ResponseClient-side](#handle-response)

## Handle the ResponseClient-side

After you send the request, you must handle the response.
