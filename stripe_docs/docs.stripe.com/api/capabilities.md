- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Capabilities

[Capabilities](/api/capabilities)

This is an object representing a capability for a Stripe account.

Related guide: Account capabilities

[Account capabilities](/connect/account-capabilities)

[POST/v1/accounts/:id/capabilities/:id](/api/capabilities/update)

[GET/v1/accounts/:id/capabilities/:id](/api/capabilities/retrieve)

[GET/v1/accounts/:id/capabilities](/api/capabilities/list)

# The Capability object

[The Capability object](/api/capabilities/object)

- idstringThe identifier for the capability.

The identifier for the capability.

- accountstringExpandableThe account for which the capability enables functionality.

The account for which the capability enables functionality.

- requestedbooleanWhether the capability has been requested.

Whether the capability has been requested.

- requirementsobjectInformation about the requirements for the capability, including what information needs to be collected, and by when.Show child attributes

Information about the requirements for the capability, including what information needs to be collected, and by when.

- statusenumThe status of the capability. Can be active, inactive, pending, or unrequested.Possible enum valuesactivedisabledinactivependingunrequested

The status of the capability. Can be active, inactive, pending, or unrequested.

- objectstring

- future_requirementsobject

- requested_atnullable timestamp

# Update an Account Capability

[Update an Account Capability](/api/capabilities/update)

Updates an existing Account Capability. Request or remove a capability by updating its requested parameter.

- requestedbooleanTo request a new capability for an account, pass true. There can be a delay before the requested capability becomes active. If the capability has any activation requirements, the response includes them in the requirements arrays.If a capability isn’t permanent, you can remove it from the account by passing false. Most capabilities are permanent after they’ve been requested. Attempting to remove a permanent capability returns an error.

To request a new capability for an account, pass true. There can be a delay before the requested capability becomes active. If the capability has any activation requirements, the response includes them in the requirements arrays.

If a capability isn’t permanent, you can remove it from the account by passing false. Most capabilities are permanent after they’ve been requested. Attempting to remove a permanent capability returns an error.

Returns an Account Capability object.

# Retrieve an Account Capability

[Retrieve an Account Capability](/api/capabilities/retrieve)

Retrieves information about the specified Account Capability.

No parameters.

Returns an Account Capability object.

# List all account capabilities

[List all account capabilities](/api/capabilities/list)

Returns a list of capabilities associated with the account. The capabilities are returned sorted by creation date, with the most recent capability appearing first.

No parameters.

A dictionary with a data property that contains an array of the capabilities of this account. Each entry in the array is a separate capability object.
