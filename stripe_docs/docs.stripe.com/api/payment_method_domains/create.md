- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Create a payment method domain

[Create a payment method domain](/api/payment_method_domains/create)

Creates a payment method domain.

- domain_namestringRequiredThe domain name that this payment method domain object represents.

The domain name that this payment method domain object represents.

- enabledbooleanWhether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements.

Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements.

Returns a payment method domain object.

# Update a payment method domain

[Update a payment method domain](/api/payment_method_domains/update)

Updates an existing payment method domain.

- enabledbooleanWhether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements.

Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements.

Returns the updated payment method domain object.

# Retrieve a payment method domain

[Retrieve a payment method domain](/api/payment_method_domains/retrieve)

Retrieves the details of an existing payment method domain.

No parameters.

Returns a payment method domain object.

# List payment method domains

[List payment method domains](/api/payment_method_domains/list)

Lists the details of existing payment method domains.

- domain_namestringThe domain name that this payment method domain object represents.

The domain name that this payment method domain object represents.

- enabledbooleanWhether this payment method domain is enabled. If the domain is not enabled, payment methods will not appear in Elements

Whether this payment method domain is enabled. If the domain is not enabled, payment methods will not appear in Elements

- ending_beforestring

- limitinteger

- starting_afterstring

Returns a list of payment method domain objects.

# Validate an existing payment method domain

[Validate an existing payment method domain](/api/payment_method_domains/validate)

Some payment methods such as Apple Pay require additional steps to verify a domain. If the requirements weren’t satisfied when the domain was created, the payment method will be inactive on the domain. The payment method doesn’t appear in Elements for this domain until it is active.

To activate a payment method on an existing payment method domain, complete the required validation steps specific to the payment method, and then validate the payment method domain with this endpoint.

Related guides: Payment method domains.

[Payment method domains](/payments/payment-methods/pmd-registration)

No parameters.

Returns the updated payment method domain object.
