# Save card details after payment

Use Stripe Terminal to save card details for online reuse while processing in-person transactions.

When you successfully confirm a payment, the returned object contains a successful charge ID. This charge contains a generated_card ID, which represents the ID of a card PaymentMethod that’s used to charge the saved card.

[confirm a payment](/terminal/payments/collect-payment#confirm-payment)

[generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)

[PaymentMethod](/api/payment_methods)

[charge the saved card](/terminal/features/saving-cards/overview#charging-saved-card)

The initial, in-person payment benefits from the liability shift (and in certain markets, lower pricing given to standard Terminal payments). But subsequent payments happen online and they’re treated as card-not-present. For example, a gym customer pays for an initial session in person and begins a membership in the same transaction. Or a clothing store collects a customer’s email address and payment method at the checkout counter during purchase, and the customer can log in later and use it again.

[lower pricing](https://stripe.com/terminal#pricing)

[standard Terminal payments](/terminal/payments/collect-payment)

You can automatically attach the generated_card PaymentMethod to a customer object to easily retrieve saved card details in the future. When creating a PaymentIntent, provide a customer ID and set the setup_future_usage parameter to indicate you intend to make future payments with the payment method.

[PaymentIntent](/api/payment_intents/create)

[customer ID](/api/customers)

[setup_future_usage](/api/payment_intents/create#create_payment_intent-setup_future_usage)

Unless your business is a car rental service or hotel, you can’t save mobile wallets (for example, Apple Pay or Google Pay) for later reuse while transacting. We have a limited private beta available for users with a car rental service or hotel. To request access, please contact stripe-terminal-betas@stripe.com.

[mobile wallets](/payments/wallets)

[stripe-terminal-betas@stripe.com](mailto:stripe-terminal-betas@stripe.com)

With the iOS, Android, and React Native SDKs, you can create a PaymentIntent client-side and provide the customer and set setup_future_usage.

Client-side PaymentIntent creation is possible with the iOS or Android SDKs. If you’re using the JavaScript SDK for Stripe Terminal, create a PaymentIntent server-side.

The JavaScript SDK and server-driven integration require you to create the PaymentIntent on your server. For iOS or Android, you can create the PaymentIntent on your server if the information required to start a payment isn’t readily available in your app.

You can retrieve the saved card details by listing the card payment methods associated with that customer.

[listing](/api/payment_methods/list)

You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For example, the European Data Protection Board has issued guidance regarding saving payment details. These requirements generally apply if you want to save your customer’s payment method for future use, such as presenting a customer’s payment method to them in the checkout flow for a future purchase or charging them when they’re not actively using your website or app.

Add terms to your website or app that state how you plan to save payment method details and allow customers to opt in. If you plan to charge the customer while they’re offline, then at a minimum, make sure that your terms also cover the following:

- The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.

- The anticipated timing and frequency of payments (for instance, whether charges are for scheduled installment or subscription payments, or for unscheduled top-ups).

- How the payment amount is determined.

- Your cancellation policy, if you’re setting up the payment method for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

When you save a payment method, it can only be used for the specific usage that you included in your terms. If you want to charge customers when they’re offline and also save the customer’s payment method to present to them as a saved payment method for future purchases, you must explicitly collect consent from the customer. One way to do so is with a “Save my payment method for future use” checkbox.
