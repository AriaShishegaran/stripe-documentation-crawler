- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# TokensPreview feature

[Tokens](/api/issuing/tokens)

An issuing token object is created when an issued card is added to a digital wallet. As a card issuer, you can view and manage these tokens through Stripe.

[card issuer](/issuing)

[view and manage these tokens](/issuing/controls/token-management)

[POST/v1/issuing/tokens/:id](/api/issuing/tokens/update)

[GET/v1/issuing/tokens/:id](/api/issuing/tokens/retrieve)

[GET/v1/issuing/tokens](/api/issuing/tokens/list)

# The Token objectPreview feature

[The Token object](/api/issuing/tokens/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- objectstringString representing the object’s type. Objects of the same type share the same value.

String representing the object’s type. Objects of the same type share the same value.

- cardstringExpandableCard associated with this token.

Card associated with this token.

- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.

Time at which the object was created. Measured in seconds since the Unix epoch.

- device_fingerprintnullable stringThe hashed ID derived from the device ID from the card network associated with the token.

The hashed ID derived from the device ID from the card network associated with the token.

- last4nullable stringThe last four digits of the token.

The last four digits of the token.

- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.

Has the value true if the object exists in live mode or the value false if the object exists in test mode.

- networkenumThe token service provider / card network associated with the token.Possible enum valuesmastercardMasterCard token service provider.visaVisa token service provider.

The token service provider / card network associated with the token.

MasterCard token service provider.

Visa token service provider.

- network_datanullable objectPreview featureExpandableAdditional details obtained from the network about the token, primarily related to the token creation process. For security reasons, this is only available to view in the first 24 hours after token creation, based on the created value, and will be omitted unless you explicitly request it with the expand parameter. Additionally, it’s only available via the “Retrieve a token” endpoint and “Update a token status” endpoint.Show child attributes

Additional details obtained from the network about the token, primarily related to the token creation process. For security reasons, this is only available to view in the first 24 hours after token creation, based on the created value, and will be omitted unless you explicitly request it with the expand parameter. Additionally, it’s only available via the “Retrieve a token” endpoint and “Update a token status” endpoint.

[the expand parameter](/api/expanding_objects)

[“Retrieve a token” endpoint](/api/issuing/tokens/retrieve)

[“Update a token status” endpoint](/api/issuing/tokens/update)

- network_updated_attimestampTime at which the token was last updated by the card network. Measured in seconds since the Unix epoch.

Time at which the token was last updated by the card network. Measured in seconds since the Unix epoch.

- statusenumThe usage state of the token.Possible enum valuesactiveToken is provisioned and usable for payments.deletedTerminal state. Token can no longer be used.requestedToken has been requested to be provisioned, but has not completed the activation process.suspendedToken temporarily cannot be used for payments.

The usage state of the token.

Token is provisioned and usable for payments.

Terminal state. Token can no longer be used.

Token has been requested to be provisioned, but has not completed the activation process.

Token temporarily cannot be used for payments.

- wallet_providernullable enumThe digital wallet for this token, if one was used.Possible enum valuesapple_payApple Pay.google_payGoogle Pay.samsung_paySamsung Pay.

The digital wallet for this token, if one was used.

Apple Pay.

Google Pay.

Samsung Pay.

# Update a token status

[Update a token status](/api/issuing/tokens/update)

Attempts to update the specified Issuing Token object to the status specified.

- statusenumRequiredSpecifies which status the token should be updated to.Possible enum valuesactiveToken is provisioned and usable for payments.deletedTerminal state. Token can no longer be used.suspendedToken temporarily cannot be used for payments.

Specifies which status the token should be updated to.

Token is provisioned and usable for payments.

Terminal state. Token can no longer be used.

Token temporarily cannot be used for payments.

Returns an updated Issuing Token object if a valid identifier was provided.

# Retrieve an issuing token

[Retrieve an issuing token](/api/issuing/tokens/retrieve)

Retrieves an Issuing Token object.

No parameters.

Returns an Issuing Token object if a valid identifier was provided.

# List all issuing tokens for card

[List all issuing tokens for card](/api/issuing/tokens/list)

Lists all Issuing Token objects for a given card.

- cardstringRequiredThe Issuing card identifier to list tokens for.

The Issuing card identifier to list tokens for.

- createdobjectOnly return Issuing tokens that were created during the given date interval.Show child parameters

Only return Issuing tokens that were created during the given date interval.

- statusenumSelect Issuing tokens with the given status.Possible enum valuesactiveToken is provisioned and usable for payments.deletedTerminal state. Token can no longer be used.requestedToken has been requested to be provisioned, but has not completed the activation process.suspendedToken temporarily cannot be used for payments.

Select Issuing tokens with the given status.

Token is provisioned and usable for payments.

Terminal state. Token can no longer be used.

Token has been requested to be provisioned, but has not completed the activation process.

Token temporarily cannot be used for payments.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit tokens, starting after token starting_after. Each entry in the array is a separate Issuing Token object. If no more tokens are available, the resulting array will be empty.
