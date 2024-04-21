- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# Cancel a payout

[Cancel a payout](/api/payouts/cancel)

You can cancel a previously created payout if its status is pending. Stripe refunds the funds to your available balance. You can’t cancel automatic Stripe payouts.

No parameters.

Returns the payout object if the cancellation succeeds. Returns an error if the payout is already canceled or can’t be canceled.

# Reverse a payout

[Reverse a payout](/api/payouts/reverse)

Reverses a payout by debiting the destination bank account. At this time, you can only reverse payouts for connected accounts to US bank accounts. If the payout is manual and in the pending status, use /v1/payouts/:id/cancel instead.

By requesting a reversal through /v1/payouts/:id/reverse, you confirm that the authorized signatory of the selected bank account authorizes the debit on the bank account and that no other authorization is required.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns the reversing payout object if the reversal is successful. Returns an error if the payout is already reversed or can’t be reversed.
