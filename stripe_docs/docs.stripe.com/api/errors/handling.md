- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Handling errors

[Handling errors](/api/errors/handling)

Our Client libraries raise exceptions for many reasons, such as a failed charge, invalid parameters, authentication errors, and network unavailability. We recommend writing code that gracefully handles all possible API exceptions.

- Related guide: Error Handling

[Error Handling](/docs/error-handling)

# Expanding Responses

[Expanding Responses](/api/expanding_objects)

Many objects allow you to request additional information as an expanded response by using the expand request parameter. This parameter is available on all API requests, and applies to the response of that request only. You can expand responses in two ways.

In many cases, an object contains the ID of a related object in its response properties. For example, a Charge might have an associated Customer ID. You can expand these objects in line with the expand request parameter. The expandable label in this documentation indicates ID fields that you can expand into objects.

Some available fields aren’t included in the responses by default, such as the number and cvc fields for the Issuing Card object. You can request these fields as an expanded response by using the expand request parameter.

You can expand recursively by specifying nested fields after a dot (.). For example, requesting invoice.subscription on a charge expands the invoice property into a full Invoice object, then expands the subscription property on that invoice into a full Subscription object.

You can use the expand parameter on any endpoint that returns expandable fields, including list, create, and update endpoints.

Expansions on list requests start with the data property. For example, you can expand data.customers on a request to list charges and associated customers. Performing deep expansions on numerous list requests might result in slower processing times.

Expansions have a maximum depth of four levels (for example, the deepest expansion allowed when listing charges is data.invoice.subscription.default_source).

You can expand multiple objects at the same time by identifying multiple items in the expand array.

- Related guide: Expanding responses

[Expanding responses](/docs/expand)

- Related video: Expand

[Expand](https://www.youtube.com/watch?v=m8Vj_CEWyQc)

# Idempotent requests

[Idempotent requests](/api/idempotent_requests)

The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. When creating or updating an object, use an idempotency key. Then, if a connection error occurs, you can safely repeat the request without risk of creating a second object or performing the update twice.

[idempotency](https://en.wikipedia.org/wiki/Idempotence)

To perform an idempotent request, provide an additional IdempotencyKey element to the request options.

Stripe’s idempotency works by saving the resulting status code and body of the first request made for any given idempotency key, regardless of whether it succeedes or fails. Subsequent requests with the same key return the same result, including 500 errors.

A client generates an idempotency key, which is a unique key that the server uses to recognize subsequent retries of the same request. How you create unique keys is up to you, but we suggest using V4 UUIDs, or another random string with enough entropy to avoid collisions. Idempotency keys are up to 255 characters long.

You can remove keys from the system automatically after they’re at least 24 hours old. We generate a new request if a key is reused after the original is pruned. The idempotency layer compares incoming parameters to those of the original request and errors if they’re the same to prevent accidental misuse.

We save results only after the execution of an endpoint begins. If incoming parameters fail validation, or the request conflicts with another request that’s executing concurrently, we don’t save the idempotent result because no API endpoint initiates the execution. You can retry these requests. Learn more about when you can retry idempotent requests.

[retry idempotent requests](/error-low-level#idempotency)

All POST requests accept idempotency keys. Don’t send idempotency keys in GET and DELETE requests because it has no effect. These requests are idempotent by definition.

- Related video: Idempotency and retries

[Idempotency and retries](/docs/videos/developer-foundations?video=idempotency-and-retries)

# Metadata

[Metadata](/api/metadata)

Updateable Stripe objects—including Account, Charge, Customer, PaymentIntent, Refund, Subscription, and Transfer have a metadata parameter. You can use this parameter to attach key-value data to these Stripe objects.

[Account](/api/accounts)

[Charge](/api/charges)

[Customer](/api/customers)

[PaymentIntent](/api/payment_intents)

[Refund](/api/refunds)

[Subscription](/api/subscriptions)

[Transfer](/api/transfers)

You can specify up to 50 keys, with key names up to 40 characters long and values up to 500 characters long.

You can use metadata to store additional, structured information on an object. For example, you could store your user’s full name and corresponding unique identifier from your system on a Stripe Customer object. Stripe doesn’t use metadata—for example, we don’t use it to authorize or decline a charge and it won’t be seen by your users unless you choose to show it to them.

[Customer](/api/customers)

Some of the objects listed above also support a description parameter. You can use the description parameter to annotate a charge-for example, a human-readable description such as 2 shirts for test@example.com. Unlike metadata, description is a single string, which your users might see (for example, in email receipts Stripe sends on your behalf).

Don’t store any sensitive information (bank account numbers, card details, and so on) as metadata or in the description parameter.

- Related video: Metadata

[Metadata](/docs/videos/developer-foundations?video=metadata)

## Sample metadata use cases

- Link IDs: Attach your system’s unique IDs to a Stripe object to simplify lookups. For example, add your order number to a charge, your user ID to a customer or recipient, or a unique receipt number to a transfer.

- Refund papertrails: Store information about the reason for a refund and the individual responsible for its creation.

- Customer details: Annotate a customer by storing an internal ID for your future use.

# Pagination

[Pagination](/api/pagination)

All top-level API resources have support for bulk fetches through “list” API methods. For example, you can list charges, list customers, and list invoices. These list API methods share a common structure and accept, at a minimum, the following three parameters: limit, starting_after, and ending_before.

[list charges](/api/charges/list)

[list customers](/api/customers/list)

[list invoices](/api/invoices/list)

Stripe’s list API methods use cursor-based pagination through the starting_after and ending_before parameters. Both parameters accept an existing object ID value (see below) and return objects in reverse chronological order. The ending_before parameter returns objects listed before the named object. The starting_after parameter returns objects listed after the named object. These parameters are mutually exclusive. You can use either the starting_after or ending_before parameter, but not both simultaneously.

Our client libraries offer auto-pagination helpers to traverse all pages of a list.

- Related video: Pagination and auto-pagination

[Pagination and auto-pagination](/docs/videos/developer-foundations?video=pagination)

- limitoptional, default is 10This specifies a limit on the number of objects to return, ranging between 1 and 100.

This specifies a limit on the number of objects to return, ranging between 1 and 100.

- starting_afteroptional object IDA cursor to use in pagination. starting_after is an object ID that defines your place in the list. For example, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include starting_after=obj_foo to fetch the next page of the list.

A cursor to use in pagination. starting_after is an object ID that defines your place in the list. For example, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include starting_after=obj_foo to fetch the next page of the list.

- ending_beforeoptional object IDA cursor to use in pagination. ending_before is an object ID that defines your place in the list. For example, if you make a list request and receive 100 objects, starting with obj_bar, your subsequent call can include ending_before=obj_bar to fetch the previous page of the list.

A cursor to use in pagination. ending_before is an object ID that defines your place in the list. For example, if you make a list request and receive 100 objects, starting with obj_bar, your subsequent call can include ending_before=obj_bar to fetch the previous page of the list.

- objectstring, value is "list"A string that provides a description of the object type that returns.

A string that provides a description of the object type that returns.

- dataarrayAn array containing the actual response elements, paginated by any request parameters.

An array containing the actual response elements, paginated by any request parameters.

- has_morebooleanWhether or not there are more elements available after this set. If false, this set comprises the end of the list.

Whether or not there are more elements available after this set. If false, this set comprises the end of the list.

- urlurlThe URL for accessing this list.

The URL for accessing this list.
