# Charges versus Payment Intents APIs

## Understanding the Stripe payment APIs

There are three ways to accept payments on Stripe today:

- Stripe Checkout

- Charges API

- Payment Intents API

[Payment Intents API](/payments/payment-intents)

Stripe Checkout is a prebuilt payment page that you can redirect your customer to for simple purchases and subscriptions. It provides many features, such as Apple Pay, Google Pay, internationalization, and form validation.

[Stripe Checkout](/payments/checkout)

[subscriptions](/billing/subscriptions/creating)

The Charges and Payment Intents APIs let you build custom payment flows and experiences.

[Charges](/api/charges)

[Payment Intents](/api/payment_intents)

The Payment Intents API is the unifying API for all Stripe products and payment methods. While we are not deprecating Charges, new features are only available with the Payment Intents API.

For a full feature comparison, see the table below:

[Strong Customer Authentication](/strong-customer-authentication)

[Sources API](/sources)

[many other payment methods](/payments/payment-methods/overview)

[Is SCA ready](/strong-customer-authentication)

## Migrating code that reads from charges

If you have an application with multiple payment flows and incrementally migrating each one from the Charges API to the Payment Intents API, you should first update any code that reads from the Charge object. To help with this, the charge object has two additional properties, payment_method_details and billing_details, which provide a consistent interface for reading the details of the payment method used for the charge.

[Payment Intents API](/payments/payment-intents)

[Charge](/api/charges)

[payment_method_details](/api/charges/object#charge_object-payment_method_details)

[billing_details](/api/charges/object#charge_object-billing_details)

These fields are available on all API versions and on charge objects created with both the Charges API and the Payment Intents API.

The following table shows commonly used properties on a charge and how the same information can be accessed using the additional properties:

## See also

- Migrate to Payment Intents

[Migrate to Payment Intents](/payments/payment-intents/migration)
