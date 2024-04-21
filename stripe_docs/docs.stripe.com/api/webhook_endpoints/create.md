- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Create a webhook endpoint

[Create a webhook endpoint](/api/webhook_endpoints/create)

A webhook endpoint must have a url and a list of enabled_events. You may optionally specify the Boolean connect parameter. If set to true, then a Connect webhook endpoint that notifies the specified url about events from all connected accounts is created; otherwise an account webhook endpoint that notifies the specified url only about events from your account is created. You can also create webhook endpoints in the webhooks settings section of the Dashboard.

[webhooks settings](https://dashboard.stripe.com/account/webhooks)

- enabled_eventsarray of enumsRequiredThe list of events to enable for this endpoint. You may specify ['*'] to enable all events, except those that require explicit selection.Possible enum valuesaccount.application.authorizedOccurs whenever a user authorizes an application. Sent to the related application only.account.application.deauthorizedOccurs whenever a user deauthorizes an application. Sent to the related application only.account.external_account.createdOccurs whenever an external account is created.account.external_account.deletedOccurs whenever an external account is deleted.account.external_account.updatedOccurs whenever an external account is updated.account.updatedOccurs whenever an account status or property has changed.application_fee.createdOccurs whenever an application fee is created on a charge.application_fee.refund.updatedOccurs whenever an application fee refund is updated.application_fee.refundedOccurs whenever an application fee is refunded, whether from refunding a charge or from refunding the application fee directly. This includes partial refunds.balance.availableOccurs whenever your Stripe balance has been updated (e.g., when a charge is available to be paid out). By default, Stripe automatically transfers funds in your balance to your bank account on a daily basis. This event is not fired for negative transactions.Show 339 more

The list of events to enable for this endpoint. You may specify ['*'] to enable all events, except those that require explicit selection.

Occurs whenever a user authorizes an application. Sent to the related application only.

Occurs whenever a user deauthorizes an application. Sent to the related application only.

Occurs whenever an external account is created.

Occurs whenever an external account is deleted.

Occurs whenever an external account is updated.

Occurs whenever an account status or property has changed.

Occurs whenever an application fee is created on a charge.

Occurs whenever an application fee refund is updated.

Occurs whenever an application fee is refunded, whether from refunding a charge or from refunding the application fee directly. This includes partial refunds.

[refunding the application fee directly](#fee_refunds)

Occurs whenever your Stripe balance has been updated (e.g., when a charge is available to be paid out). By default, Stripe automatically transfers funds in your balance to your bank account on a daily basis. This event is not fired for negative transactions.

- urlstringRequiredThe URL of the webhook endpoint.

The URL of the webhook endpoint.

- api_versionstringEvents sent to this endpoint will be generated with this Stripe Version instead of your account’s default Stripe Version.

Events sent to this endpoint will be generated with this Stripe Version instead of your account’s default Stripe Version.

- descriptionstringAn optional description of what the webhook is used for.

An optional description of what the webhook is used for.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- connectboolean

Returns the webhook endpoint object with the secret field populated.

# Update a webhook endpoint

[Update a webhook endpoint](/api/webhook_endpoints/update)

Updates the webhook endpoint. You may edit the url, the list of enabled_events, and the status of your endpoint.

- descriptionstringAn optional description of what the webhook is used for.

An optional description of what the webhook is used for.

- enabled_eventsarray of enumsThe list of events to enable for this endpoint. You may specify ['*'] to enable all events, except those that require explicit selection.Possible enum valuesaccount.application.authorizedOccurs whenever a user authorizes an application. Sent to the related application only.account.application.deauthorizedOccurs whenever a user deauthorizes an application. Sent to the related application only.account.external_account.createdOccurs whenever an external account is created.account.external_account.deletedOccurs whenever an external account is deleted.account.external_account.updatedOccurs whenever an external account is updated.account.updatedOccurs whenever an account status or property has changed.application_fee.createdOccurs whenever an application fee is created on a charge.application_fee.refund.updatedOccurs whenever an application fee refund is updated.application_fee.refundedOccurs whenever an application fee is refunded, whether from refunding a charge or from refunding the application fee directly. This includes partial refunds.balance.availableOccurs whenever your Stripe balance has been updated (e.g., when a charge is available to be paid out). By default, Stripe automatically transfers funds in your balance to your bank account on a daily basis. This event is not fired for negative transactions.Show 339 more

The list of events to enable for this endpoint. You may specify ['*'] to enable all events, except those that require explicit selection.

Occurs whenever a user authorizes an application. Sent to the related application only.

Occurs whenever a user deauthorizes an application. Sent to the related application only.

Occurs whenever an external account is created.

Occurs whenever an external account is deleted.

Occurs whenever an external account is updated.

Occurs whenever an account status or property has changed.

Occurs whenever an application fee is created on a charge.

Occurs whenever an application fee refund is updated.

Occurs whenever an application fee is refunded, whether from refunding a charge or from refunding the application fee directly. This includes partial refunds.

[refunding the application fee directly](#fee_refunds)

Occurs whenever your Stripe balance has been updated (e.g., when a charge is available to be paid out). By default, Stripe automatically transfers funds in your balance to your bank account on a daily basis. This event is not fired for negative transactions.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- urlstringThe URL of the webhook endpoint.

The URL of the webhook endpoint.

- disabledboolean

The updated webhook endpoint object if successful. Otherwise, this call raises an error.

[an error](#errors)

# Retrieve a webhook endpoint

[Retrieve a webhook endpoint](/api/webhook_endpoints/retrieve)

Retrieves the webhook endpoint with the given ID.

No parameters.

Returns a webhook endpoint if a valid webhook endpoint ID was provided. Raises an error otherwise.

[an error](#errors)

# List all webhook endpoints

[List all webhook endpoints](/api/webhook_endpoints/list)

Returns a list of your webhook endpoints.

No parameters.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit webhook endpoints, starting after webhook endpoint starting_after. Each entry in the array is a separate webhook endpoint object. If no more webhook endpoints are available, the resulting array will be empty. This request should never raise an error.

# Delete a webhook endpoint

[Delete a webhook endpoint](/api/webhook_endpoints/delete)

You can also delete webhook endpoints via the webhook endpoint management page of the Stripe dashboard.

[webhook endpoint management](https://dashboard.stripe.com/account/webhooks)

No parameters.

An object with the deleted webhook endpoints’s ID. Otherwise, this call raises an error, such as if the webhook endpoint has already been deleted.

[an error](#errors)
