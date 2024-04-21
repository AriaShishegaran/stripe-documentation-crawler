# Save SEPA Direct Debit details for future payments

You can use Checkout in setup mode to collect SEPA Direct Debit payment details in advance, with the final amount or payment date determined later. This is useful for:

[Checkout in setup mode](/payments/save-and-reuse?platform=checkout)

- Saving payment methods to a wallet to streamline future purchases

- Collecting surcharges after fulfilling a service

- Starting a free trial for a subscription

[Starting a free trial for a subscription](/billing/subscriptions/trials)

SEPA Direct Debit is a delayed notification payment method, which means that funds are not immediately available after payment. A payment typically takes 5 business days to arrive in your account.

[Create or retrieve a CustomerServer-side](#create-retrieve-customer)

## Create or retrieve a CustomerServer-side

To reuse a SEPA Direct Debit payment method for future payments, it must be attached to a Customer.

[Customer](/api/customers)

Create a Customer object when your customer creates an account with your business. Associating the ID of the Customer object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later.

Create a new customer or retrieve an existing customer to associate with this payment. Include the following code on your server to create a new customer.

[Set up future payments](#setup-a-payment)

## Set up future payments

This guide builds on the foundational set up future payments Checkout integration.

[set up future payments](/payments/save-and-reuse?platform=checkout)

Use this guide to learn how to enable SEPA Direct Debit—it shows the differences between setting up future payments for cards and using SEPA Direct Debit.

When creating a new Checkout Session, you need to add sepa_debit to the list of payment_method_types.

[Checkout Session](/api/checkout/sessions)

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

[Test your integration](#testing)

## Test your integration

You can test your integration using the IBANs below. The payment method details are successfully collected for each IBAN but exhibit different behavior when charged.

## See also

- Manually configure SEPA Direct Debit as a payment

[Manually configure SEPA Direct Debit as a payment](/payments/sepa-debit/accept-a-payment)

- Connect platforms using the Payment Methods API

[Connect platforms using the Payment Methods API](/payments/payment-methods/connect)
