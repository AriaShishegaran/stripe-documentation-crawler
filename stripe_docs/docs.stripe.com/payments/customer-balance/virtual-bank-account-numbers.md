# Virtual bank account numbers

Virtual Bank Account Numbers (VBANs) are an important part of the bank transfers payment method. To accept funds from a bank transfer, Stripe issues a VBAN to your customer. When the customer transfers money to that VBAN, Stripe automatically allocates the funds to the customer’s cash balance. After these funds arrive on the customer’s cash balance, Stripe carries out further reconciliation steps to associate the funds with the correct PaymentIntent or Invoice.

After a customer has been allocated a VBAN, it belongs to them forever. Any additional funds that are sent to that VBAN are automatically added to customer’s cash balance. Because VBANs are permanent, it’s important to understand their limits and best practices for using them.

## Allocation

There are several ways to allocate a VBAN to a customer.

- When you create and confirm a PaymentIntent with the customer balance payment method, Stripe looks for an existing VBAN that is assigned to the customer and for the country specified in the request. If the customer does not have an appropriate VBAN, Stripe generates a new VBAN for the customer.

When you create and confirm a PaymentIntent with the customer balance payment method, Stripe looks for an existing VBAN that is assigned to the customer and for the country specified in the request. If the customer does not have an appropriate VBAN, Stripe generates a new VBAN for the customer.

- When you create a new Invoice with the customer balance payment method, Stripe looks for an existing VBAN that matches the country and is assigned to the customer specified in the request. If the customer does not have an appropriate VBAN, Stripe generates a new VBAN for the customer.

When you create a new Invoice with the customer balance payment method, Stripe looks for an existing VBAN that matches the country and is assigned to the customer specified in the request. If the customer does not have an appropriate VBAN, Stripe generates a new VBAN for the customer.

- The Funding Instructions API creates VBANs without requiring an existing PaymentIntent or Invoice. You can use this API when you don’t expect payment from a customer yet but still want to create a new VBAN for them.

The Funding Instructions API creates VBANs without requiring an existing PaymentIntent or Invoice. You can use this API when you don’t expect payment from a customer yet but still want to create a new VBAN for them.

[Funding Instructions API](/payments/customer-balance/funding-instructions)

## Limits and Best Practices

When you integrate with bank transfers, only request a VBAN for a customer if they’re likely to make a payment using a bank transfer. In these cases, you only generate a VBAN when creating a PaymentIntent or a Invoice.

Don’t assign VBANs to inactive customers or make VBAN allocation part of your registration flow.

Due to regional differences in VBAN availability, Stripe enforces different limits per region. If you need more VBANs than the limits allow, please reach out to our support team.

[reach out to our support team](https://support.stripe.com/)

[a fee](https://stripe.com/pricing/local-payment-methods)
