- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# List orders

[List orders](/api/climate/order/list)

Lists all Climate order objects. The orders are returned sorted by creation date, with the most recently created orders appearing first.

No parameters.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit orders, starting after order starting_after. Each entry in the array is a separate order object. If no more orders are available, the resulting array is empty.

# Cancel an order

[Cancel an order](/api/climate/order/cancel)

Cancels a Climate order. You can cancel an order within 30 days of creation. Stripe refunds the reservation amount_subtotal, but not the amount_fees for user-triggered cancellations. Frontier might cancel reservations if suppliers fail to deliver. If Frontier cancels the reservation, Stripe provides 90 days advance notice and refunds the amount_total.

- orderstringRequiredUnique identifier of the order.

Unique identifier of the order.

The canceled Climate order object.

# Climate Product

[Climate Product](/api/climate/product)

A Climate product represents a type of carbon removal unit available for reservation. You can retrieve it to see the current price and availability.

[GET/v1/climate/products/:id](/api/climate/product/retrieve)

[GET/v1/climate/products](/api/climate/product/list)

Show

# Climate Supplier

[Climate Supplier](/api/climate/supplier)

A supplier of carbon removal.

[GET/v1/climate/suppliers/:id](/api/climate/supplier/retrieve)

[GET/v1/climate/suppliers](/api/climate/supplier/list)

Show

# Forwarding RequestPreview feature

[Forwarding Request](/api/forwarding/request)

Instructs Stripe to make a request on your behalf using the destination URL. The destination URL is activated by Stripe at the time of onboarding. Stripe verifies requests with your credentials provided during onboarding, and injects card details from the payment_method into the request.

Stripe redacts all sensitive fields and headers, including authentication credentials and card numbers, before storing the request and response data in the forwarding Request object, which are subject to a 30-day retention period.

You can provide a Stripe idempotency key to make sure that requests with the same key result in only one outbound request. The Stripe idempotency key provided should be unique and different from any idempotency keys provided on the underlying third-party request.

Forwarding Requests are synchronous requests that return a response or time out according to Stripe’s limits.

Related guide: Forward card details to third-party API endpoints.

[Forward card details to third-party API endpoints](https://docs.stripe.com/payments/forwarding)

[POST/v1/forwarding/requests](/api/forwarding/forwarding_requests/create)

[GET/v1/forwarding/requests/:id](/api/forwarding/forwarding_requests/retrieve)

[GET/v1/forwarding/requests](/api/forwarding/forwarding_requests/list)

Show

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
