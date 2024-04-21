- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Payout object

[The Payout object](/api/payouts/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- amountintegerThe amount (in cents) that transfers to your bank account or debit card.

The amount (in cents) that transfers to your bank account or debit card.

- arrival_datetimestampDate that you can expect the payout to arrive in the bank. This factors in delays to account for weekends or bank holidays.

Date that you can expect the payout to arrive in the bank. This factors in delays to account for weekends or bank holidays.

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- descriptionnullable stringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- metadatanullable objectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- statement_descriptornullable stringExtra information about a payout that displays on the user’s bank statement.

Extra information about a payout that displays on the user’s bank statement.

- statusstringCurrent status of the payout: paid, pending, in_transit, canceled or failed. A payout is pending until it’s submitted to the bank, when it becomes in_transit. The status changes to paid if the transaction succeeds, or to failed or canceled (within 5 business days). Some payouts that fail might initially show as paid, then change to failed.

Current status of the payout: paid, pending, in_transit, canceled or failed. A payout is pending until it’s submitted to the bank, when it becomes in_transit. The status changes to paid if the transaction succeeds, or to failed or canceled (within 5 business days). Some payouts that fail might initially show as paid, then change to failed.

- objectstring

- application_feenullable stringPreview featureExpandableConnect only

- application_fee_amountnullable integerPreview featureConnect only

- automaticboolean

- balance_transactionnullable stringExpandable

- createdtimestamp

- destinationnullable stringExpandable

- failure_balance_transactionnullable stringExpandable

- failure_codenullable enum

- failure_messagenullable string

- livemodeboolean

- methodstring

- original_payoutnullable stringExpandable

- reconciliation_statusenum

- reversed_bynullable stringExpandable

- source_typestring

- typeenum

# Create a payout

[Create a payout](/api/payouts/create)

To send funds to your own bank account, create a new payout object. Your Stripe balance must cover the payout amount. If it doesn’t, you receive an “Insufficient Funds” error.

[Stripe balance](#balance)

If your API key is in test mode, money won’t actually be sent, though every other action occurs as if you’re in live mode.

If you create a manual payout on a Stripe account that uses multiple payment source types, you need to specify the source type balance that the payout draws from. The balance object details available and pending amounts by source type.

[balance object](#balance_object)

- amountintegerRequiredA positive integer in cents representing how much to payout.

A positive integer in cents representing how much to payout.

- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users.

An arbitrary string attached to the object. Often useful for displaying to users.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- statement_descriptorstringA string that displays on the recipient’s bank or card statement (up to 22 characters). A statement_descriptor that’s longer than 22 characters return an error. Most banks truncate this information and display it inconsistently. Some banks might not display it at all.

A string that displays on the recipient’s bank or card statement (up to 22 characters). A statement_descriptor that’s longer than 22 characters return an error. Most banks truncate this information and display it inconsistently. Some banks might not display it at all.

- destinationstring

- methodstring

- source_typestring

Returns a payout object if no initial errors are present during the payout creation (invalid routing number, insufficient funds, and so on). We initially mark the status of the payout object as pending.

# Update a payout

[Update a payout](/api/payouts/update)

Updates the specified payout by setting the values of the parameters you pass. We don’t change parameters that you don’t provide. This request only accepts the metadata as arguments.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns the payout object if the update succeeds. This call raises an error if update parameters are invalid.

[an error](#errors)

# Retrieve a payout

[Retrieve a payout](/api/payouts/retrieve)

Retrieves the details of an existing payout. Supply the unique payout ID from either a payout creation request or the payout list. Stripe returns the corresponding payout information.

No parameters.

Returns a payout object if a you provide a valid identifier. raises An error occurs otherwise.

[An error](#errors)

# List all payouts

[List all payouts](/api/payouts/list)

Returns a list of existing payouts sent to third-party bank accounts or payouts that Stripe sent to you. The payouts return in sorted order, with the most recently created payouts appearing first.

- statusstringOnly return payouts that have the given status: pending, paid, failed, or canceled.

Only return payouts that have the given status: pending, paid, failed, or canceled.

- arrival_dateobject

- createdobject

- destinationstring

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit payouts, starting after payout starting_after. Each entry in the array is a separate payout object. If no other payouts are available, the resulting array is empty.