- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Disputes

[Disputes](/api/disputes)

A dispute occurs when a customer questions your charge with their card issuer. When this happens, you have the opportunity to respond to the dispute with evidence that shows that the charge is legitimate.

Related guide: Disputes and fraud

[Disputes and fraud](/disputes)

[POST/v1/disputes/:id](/api/disputes/update)

[GET/v1/disputes/:id](/api/disputes/retrieve)

[GET/v1/disputes](/api/disputes/list)

[POST/v1/disputes/:id/close](/api/disputes/close)

# The Dispute object

[The Dispute object](/api/disputes/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- amountintegerDisputed amount. Usually the amount of the charge, but it can differ (usually because of currency fluctuation or because only part of the order is disputed).

Disputed amount. Usually the amount of the charge, but it can differ (usually because of currency fluctuation or because only part of the order is disputed).

- chargestringExpandableID of the charge that’s disputed.

ID of the charge that’s disputed.

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- evidenceobjectEvidence provided to respond to a dispute. Updating any field in the hash submits all fields in the hash for review.Show child attributes

Evidence provided to respond to a dispute. Updating any field in the hash submits all fields in the hash for review.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- payment_intentnullable stringExpandableID of the PaymentIntent that’s disputed.

ID of the PaymentIntent that’s disputed.

- reasonstringReason given by cardholder for dispute. Possible values are bank_cannot_process, check_returned, credit_not_processed, customer_initiated, debit_not_authorized, duplicate, fraudulent, general, incorrect_account_details, insufficient_funds, product_not_received, product_unacceptable, subscription_canceled, or unrecognized. Learn more about dispute reasons.

Reason given by cardholder for dispute. Possible values are bank_cannot_process, check_returned, credit_not_processed, customer_initiated, debit_not_authorized, duplicate, fraudulent, general, incorrect_account_details, insufficient_funds, product_not_received, product_unacceptable, subscription_canceled, or unrecognized. Learn more about dispute reasons.

[dispute reasons](/disputes/categories)

- statusenumCurrent status of dispute. Possible values are warning_needs_response, warning_under_review, warning_closed, needs_response, under_review, won, or lost.Possible enum valueslostneeds_responseunder_reviewwarning_closedwarning_needs_responsewarning_under_reviewwon

Current status of dispute. Possible values are warning_needs_response, warning_under_review, warning_closed, needs_response, under_review, won, or lost.

- objectstring

- balance_transactionsarray of objects

- createdtimestamp

- evidence_detailsobject

- is_charge_refundableboolean

- livemodeboolean

- payment_method_detailsnullable object

# Update a dispute

[Update a dispute](/api/disputes/update)

When you get a dispute, contacting your customer is always the best first step. If that doesn’t work, you can submit evidence to help us resolve the dispute in your favor. You can do this in your dashboard, but if you prefer, you can use the API to submit evidence programmatically.

[dashboard](https://dashboard.stripe.com/disputes)

Depending on your dispute type, different evidence fields will give you a better chance of winning your dispute. To figure out which evidence fields to provide, see our guide to dispute types.

[guide to dispute types](/disputes/categories)

- evidenceobjectEvidence to upload, to respond to a dispute. Updating any field in the hash will submit all fields in the hash for review. The combined character count of all fields is limited to 150,000.Show child parameters

Evidence to upload, to respond to a dispute. Updating any field in the hash will submit all fields in the hash for review. The combined character count of all fields is limited to 150,000.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- submitbooleanWhether to immediately submit evidence to the bank. If false, evidence is staged on the dispute. Staged evidence is visible in the API and Dashboard, and can be submitted to the bank by making another request with this attribute set to true (the default).

Whether to immediately submit evidence to the bank. If false, evidence is staged on the dispute. Staged evidence is visible in the API and Dashboard, and can be submitted to the bank by making another request with this attribute set to true (the default).

Returns the dispute object.

# Retrieve a dispute

[Retrieve a dispute](/api/disputes/retrieve)

Retrieves the dispute with the given ID.

No parameters.

Returns a dispute if a valid dispute ID was provided. Raises an error otherwise.

[an error](#errors)

# List all disputes

[List all disputes](/api/disputes/list)

Returns a list of your disputes.

- chargestringOnly return disputes associated to the charge specified by this charge ID.

Only return disputes associated to the charge specified by this charge ID.

- payment_intentstringOnly return disputes associated to the PaymentIntent specified by this PaymentIntent ID.

Only return disputes associated to the PaymentIntent specified by this PaymentIntent ID.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit disputes, starting after dispute starting_after. Each entry in the array is a separate dispute object. If no more disputes are available, the resulting array will be empty.
