- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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
