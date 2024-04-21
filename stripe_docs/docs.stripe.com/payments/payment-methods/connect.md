# Connect platforms using the Payment Methods API

Connect platform owners can make use of additional payment methods supported with the Payment Methods API. To learn more about creating payments for connected users, and which approach is best for you, refer to our Connect payments and fees documentation.

[Connect](/connect)

[Payment Methods API](/payments/payment-methods)

[payments and fees documentation](/connect/charges)

You can use the Payment Methods API with Connect in a number of ways if you opt for direct charges.

[direct charges](/connect/direct-charges)

## Using the Payment Method API with direct charges

Direct charges require creating PaymentMethods on connected accounts. With any of these methods, you must first enable the payment method you intend to use on the connected account.

[PaymentMethods](/api/payment_methods)

[enable the payment method](/connect/dynamic-payment-methods)

The recommended way to use the Payment Method API with Connect is to save the payment method details during Payment Intent confirmation. For more information about this process, see Save a card during payment.

[Save a card during payment](/payments/save-during-payment)

With Stripe.js, initialize the Stripe object and set stripeAccount to the connected account’s ID and use the setup_future_usage option when confirming the PaymentIntent. This automatically saves the payment information to the customer for reuse with future charges with that connected account.

See PaymentIntents with Stripe.js for more details about confirming each type of payment method.

[PaymentIntents with Stripe.js](/js/payment_intents)

If you’re confirming PaymentIntents from the server, you can make use of authentication using the Stripe-Account header with any of our supported libraries. See Confirm a PaymentIntent for additional details.

[authentication using the Stripe-Account header](/connect/authentication#stripe-account-header)

[Confirm a PaymentIntent](/api/payment_intents/confirm)

You may also create a PaymentMethod directly on a connected account with createPaymentMethod. With Stripe.js, initialize the Stripe object and set stripeAccount to the connected account’s ID.

If you’re creating PaymentMethods from the server, you can make use of authentication using the Stripe-Account header with any of our supported libraries.

[authentication using the Stripe-Account header](/connect/authentication#stripe-account-header)

You can also create PaymentMethods on your platform and clone them to a connected account to create direct charges. Cloning is currently supported for PaymentMethods which have type set to either card or us_bank_account.

After you create a PaymentMethod and attach it to a Customer, you can clone that PaymentMethod on a connected account using the connected account’s ID as the Stripe-Account header. Read more about the Payment Methods API.

[attach](/api/payment_methods/attach)

[Customer](/api/customers)

[Payment Methods API](/payments/payment-methods)

If you want to reuse PaymentMethods on a connected account, attach them to Customers before using them with PaymentIntents to create charges. You must provide the Customer ID in the request when cloning PaymentMethods that are attached to Customers for security purposes.

It is possible to clone PaymentMethods to connected accounts without previously attaching them to Customers. However, note that the original PaymentMethod will be consumed, since PaymentMethods that aren’t attached to Customers can only be used once.

## See also

- Payment Methods API overview

[Payment Methods API overview](/payments/payment-methods)

- Stripe.js Payment Intents

[Stripe.js Payment Intents](/js/payment_intents)
