- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The PaymentMethodDomain object

[The PaymentMethodDomain object](/api/payment_method_domains/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- domain_namestringThe domain name that this payment method domain object represents.

The domain name that this payment method domain object represents.

- enabledbooleanWhether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements.

Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements.

- objectstring

- apple_payobject

- createdtimestamp

- google_payobject

- linkobject

- livemodeboolean

- paypalobject

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