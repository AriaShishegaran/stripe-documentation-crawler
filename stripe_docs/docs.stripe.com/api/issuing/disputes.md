- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Disputes

[Disputes](/api/issuing/disputes)

As a card issuer, you can dispute transactions that the cardholder does not recognize, suspects to be fraudulent, or has other issues with.

[card issuer](/issuing)

Related guide: Issuing disputes

[Issuing disputes](/issuing/purchases/disputes)

[POST/v1/issuing/disputes](/api/issuing/disputes/create)

[POST/v1/issuing/disputes/:id](/api/issuing/disputes/update)

[GET/v1/issuing/disputes/:id](/api/issuing/disputes/retrieve)

[GET/v1/issuing/disputes](/api/issuing/disputes/list)

[POST/v1/issuing/disputes/:id/submit](/api/issuing/dispute/submit)

# The Dispute object

[The Dispute object](/api/issuing/disputes/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- amountintegerDisputed amount in the card’s currency and in the smallest currency unit. Usually the amount of the transaction, but can differ (usually because of currency fluctuation).

Disputed amount in the card’s currency and in the smallest currency unit. Usually the amount of the transaction, but can differ (usually because of currency fluctuation).

[smallest currency unit](/currencies#zero-decimal)

- balance_transactionsnullable array of objectsExpandableList of balance transactions associated with the dispute.Show child attributes

List of balance transactions associated with the dispute.

- currencyenumThe currency the transaction was made in.

The currency the transaction was made in.

- evidenceobjectEvidence for the dispute. Evidence contains exactly two non-null fields: the reason for the dispute and the associated evidence field for the selected reason.Show child attributes

Evidence for the dispute. Evidence contains exactly two non-null fields: the reason for the dispute and the associated evidence field for the selected reason.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- statusenumCurrent status of the dispute.Possible enum valuesexpiredThe dispute has expired.lostThe dispute is lost.submittedThe dispute has been submitted to Stripe.unsubmittedThe dispute is pending submission to Stripe.wonThe dispute is won.

Current status of the dispute.

The dispute has expired.

The dispute is lost.

The dispute has been submitted to Stripe.

The dispute is pending submission to Stripe.

The dispute is won.

- transactionstringExpandableThe transaction being disputed.

The transaction being disputed.

- objectstring

- createdtimestamp

- livemodeboolean

# Create a dispute

[Create a dispute](/api/issuing/disputes/create)

Creates an Issuing Dispute object. Individual pieces of evidence within the evidence object are optional at this point. Stripe only validates that required evidence is present during submission. Refer to Dispute reasons and evidence for more details about evidence requirements.

[Dispute reasons and evidence](/issuing/purchases/disputes#dispute-reasons-and-evidence)

- evidenceobjectEvidence provided for the dispute.Show child parameters

Evidence provided for the dispute.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- transactionstringThe ID of the issuing transaction to create a dispute for. For transaction on Treasury FinancialAccounts, use treasury.received_debit.

The ID of the issuing transaction to create a dispute for. For transaction on Treasury FinancialAccounts, use treasury.received_debit.

- amountinteger

Returns an Issuing Dispute object in unsubmitted status if creation succeeds.

# Update a dispute

[Update a dispute](/api/issuing/disputes/update)

Updates the specified Issuing Dispute object by setting the values of the parameters passed. Any parameters not provided will be left unchanged. Properties on the evidence object can be unset by passing in an empty string.

- evidenceobjectEvidence provided for the dispute.Show child parameters

Evidence provided for the dispute.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- amountinteger

Returns an updated Issuing Dispute object if a valid identifier was provided.

# Retrieve a dispute

[Retrieve a dispute](/api/issuing/disputes/retrieve)

Retrieves an Issuing Dispute object.

No parameters.

Returns an Issuing Dispute object if a valid identifier was provided.
