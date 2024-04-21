# Integrate India e-mandates

For a deeper dive on India recurring payments, see our comprehensive guide.

[comprehensive guide](/india-recurring-payments)

This guide provides an overview of how to generate and use India e-mandates with Stripe Invoicing for one-time payments. Currently, you can only integrate with India e-mandates through the API.

We use the term off-session to describe payments that occur without the customer’s direct involvement. These types of payments use previously collected customer payment information. In contrast, on-session payments occur when a customer is directly involved in making a payment. This can be either through the user-interface or to complete a two-factor authentication flow like 3D Secure (3DS).

[Generate a mandate](#generate-mandate)

## Generate a mandate

To generate a mandate, while your customer is signed in, make a call to create a SetupIntent that includes the payment method ID and mandate details.

[SetupIntent](/api/setup_intents)

When you submit a request to create a SetupIntent, the start date must be a timestamp and within 1 day of today.

After creating the SetupIntent, use the Payment Element to collect the customer’s payment details and set up future payments. Use stripe.confirmSetup to complete the setup using details collected by the Payment Element.

[set up future payments](/payments/save-and-reuse?platform=web&ui=elements#collect-payment-details)

[stripe.confirmSetup](/js/setup_intents/confirm_setup)

[https://example.com](https://example.com)

Confirming the SetupIntent transitions it to requires_action state, along with the next_action property describing what action needs to be taken for completing the payment.

[https://hooks.stripe.com/redirect/authenticate/src_xxxxxxxxxxx](https://hooks.stripe.com/redirect/authenticate/src_xxxxxxxxxxx)

Upon successful completion of AFA (3DS) by the cardholder, the SetupIntent transitions to a succeeded state and Stripe creates a mandate. The mandate is available on the SetupIntent object.

You can pass the payment_method_options[card][mandate_options] parameter for all subscription registrations requests. Stripe ignores these parameters if your customer is using a non-Indian card for their subscription as the regulation doesn’t apply to them.

[Use a mandate to create an invoice](#use-mandate-invoice)

## Use a mandate to create an invoice

When you create an invoice, you can set the default mandate for any of the invoice’s off-session payments. When you use default mandates, we recommend that you set the corresponding payment method and the default_payment_method:

Eventually, this invoice might attempt an off-session charge of the payment method. This is because you’ve either configured the invoice to automatically advance, have manually advanced it using the Invoice Pay endpoint, or confirmed the invoice’s payment intent. If the invoice attempts to charge your customer, the default_mandate and default_payment_method parameters work together to pay the invoice off-session.

[Invoice Pay](/api/invoices/pay)

As long as the mandate remains active—and the charge falls within the mandate’s initial parameters in terms of the amount and frequency—the charge is successfully processed. It’s also possible to set the default_mandate and default_payment_method parameters on the invoice using the Invoice Update endpoint.

[Invoice Update](/api/invoices/update)

[Use a mandate to charge an invoice](#use-mandate-charge)

## Use a mandate to charge an invoice

If you don’t want to set the mandate on the invoice during creation (for example, you haven’t collected the mandate), you can provide it at two later points during the mandate life cycle. The route you take depends on how you set up your existing invoicing integration.

Alternatively, if you’re using the Invoice Pay endpoint, you can provide the mandate as a top-level mandate parameter. As with setting the default mandate, explicitly provide the payment method you want to use with the mandate:

Similarly, you can use the mandate to confirm the payment intent associated with the invoice:

[Notification and waiting period](#customer-notification)

## Notification and waiting period

Before the charge finally goes through, customers receive a notification that informs them of the charge. Customers are also given the chance to modify or cancel the mandate. After 26 hours pass, the amount is charged to the customer’s card and the invoice is moved into a paid state.

## See also

- India recurring payments

[India recurring payments](/india-recurring-payments)

- Invoicing API

[Invoicing API](/api/invoices)

- How Invoicing works

[How Invoicing works](/invoicing/overview)
