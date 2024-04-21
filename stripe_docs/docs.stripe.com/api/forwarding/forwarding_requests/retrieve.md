- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Retrieve a ForwardingRequest

[Retrieve a ForwardingRequest](/api/forwarding/forwarding_requests/retrieve)

Retrieves a ForwardingRequest object.

No parameters.

Returns a ForwardingRequest object.

# List all ForwardingRequests

[List all ForwardingRequests](/api/forwarding/forwarding_requests/list)

Lists all ForwardingRequest objects.

- createdobjectSimilar to other List endpoints, filters results based on created timestamp. You can pass gt, gte, lt, and lte timestamp values.Show child parameters

Similar to other List endpoints, filters results based on created timestamp. You can pass gt, gte, lt, and lte timestamp values.

- ending_beforestringA pagination cursor to fetch the previous page of the list. The value must be a ForwardingRequest ID.

A pagination cursor to fetch the previous page of the list. The value must be a ForwardingRequest ID.

- limitintegerA limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- starting_afterstringA pagination cursor to fetch the next page of the list. The value must be a ForwardingRequest ID.

A pagination cursor to fetch the next page of the list. The value must be a ForwardingRequest ID.

Returns a list of ForwardingRequest objects.

# Webhook Endpoints

[Webhook Endpoints](/api/webhook_endpoints)

You can configure webhook endpoints via the API to be notified about events that happen in your Stripe account or connected accounts.

[webhook endpoints](/webhooks/)

Most users configure webhooks from the dashboard, which provides a user interface for registering and testing your webhook endpoints.

[the dashboard](https://dashboard.stripe.com/webhooks)

Related guide: Setting up webhooks

[Setting up webhooks](/webhooks/configure)

[POST/v1/webhook_endpoints](/api/webhook_endpoints/create)

[POST/v1/webhook_endpoints/:id](/api/webhook_endpoints/update)

[GET/v1/webhook_endpoints/:id](/api/webhook_endpoints/retrieve)

[GET/v1/webhook_endpoints](/api/webhook_endpoints/list)

[DELETE/v1/webhook_endpoints/:id](/api/webhook_endpoints/delete)

Show
