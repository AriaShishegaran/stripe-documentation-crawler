- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Update an authorization

[Update an authorization](/api/issuing/authorizations/update)

Updates the specified Issuing Authorization object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns an updated Issuing Authorization object if a valid identifier was provided.

# Retrieve an authorization

[Retrieve an authorization](/api/issuing/authorizations/retrieve)

Retrieves an Issuing Authorization object.

No parameters.

Returns an Issuing Authorization object if a valid identifier was provided.

# List all authorizations

[List all authorizations](/api/issuing/authorizations/list)

Returns a list of Issuing Authorization objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

- cardstringOnly return authorizations that belong to the given card.

Only return authorizations that belong to the given card.

- cardholderstringOnly return authorizations that belong to the given cardholder.

Only return authorizations that belong to the given cardholder.

- statusenumOnly return authorizations with the given status. One of pending, closed, or reversed.Possible enum valuesclosedpendingreversed

Only return authorizations with the given status. One of pending, closed, or reversed.

- createdobject

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit authorizations, starting after authorization starting_after. Each entry in the array is a separate Issuing Authorization object. If no more authorizations are available, the resulting array will be empty.

# Approve an authorization

[Approve an authorization](/api/issuing/authorizations/approve)

[Deprecated] Approves a pending Issuing Authorization object. This request should be made within the timeout window of the real-time authorization flow. This method is deprecated. Instead, respond directly to the webhook request to approve an authorization.

[real-time authorization](/issuing/controls/real-time-authorizations)

[respond directly to the webhook request to approve an authorization](/issuing/controls/real-time-authorizations#authorization-handling)

- amountintegerIf the authorization’s pending_request.is_amount_controllable property is true, you may provide this value to control how much to hold for the authorization. Must be positive (use decline to decline an authorization request).

If the authorization’s pending_request.is_amount_controllable property is true, you may provide this value to control how much to hold for the authorization. Must be positive (use decline to decline an authorization request).

[decline](/api/issuing/authorizations/decline)

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns an approved Issuing Authorization object.

# Decline an authorization

[Decline an authorization](/api/issuing/authorizations/decline)

[Deprecated] Declines a pending Issuing Authorization object. This request should be made within the timeout window of the real time authorization flow. This method is deprecated. Instead, respond directly to the webhook request to decline an authorization.

[real time authorization](/issuing/controls/real-time-authorizations)

[respond directly to the webhook request to decline an authorization](/issuing/controls/real-time-authorizations#authorization-handling)

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns a declined Issuing Authorization object.
