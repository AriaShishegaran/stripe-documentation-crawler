- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# Search

[Search](/api/pagination/search)

Some top-level API resource have support for retrieval via “search” API methods. For example, you can search charges, search customers, and search subscriptions.

[search charges](/api/charges/search)

[search customers](/api/customers/search)

[search subscriptions](/api/subscriptions/search)

Stripe’s search API methods utilize cursor-based pagination via the page request parameter and next_page response parameter. For example, if you make a search request and receive "next_page": "pagination_key" in the response, your subsequent call can include page=pagination_key to fetch the next page of results.

Our client libraries offer auto-pagination helpers to easily traverse all pages of a search result.

[auto-pagination](/api/pagination/auto)

- queryrequiredThe search query string. See search query language.

The search query string. See search query language.

[search query language](/search#search-query-language)

- limitoptionalA limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- pageoptionalA cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.

A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.

- objectstring, value is "search_result"A string describing the object type returned.

A string describing the object type returned.

- urlstringThe URL for accessing this list.

The URL for accessing this list.

- has_morebooleanWhether or not there are more elements available after this set. If false, this set comprises the end of the list.

Whether or not there are more elements available after this set. If false, this set comprises the end of the list.

- dataarrayAn array containing the actual response elements, paginated by any request parameters.

An array containing the actual response elements, paginated by any request parameters.

- next_pagestringA cursor for use in pagination. If has_more is true, you can pass the value of next_page to a subsequent call to fetch the next page of results.

A cursor for use in pagination. If has_more is true, you can pass the value of next_page to a subsequent call to fetch the next page of results.

- total_countoptional positive integer or zeroThe total number of objects that match the query, only accurate up to 10,000. This field is not included by default. To include it in the response, expand the total_count field.

The total number of objects that match the query, only accurate up to 10,000. This field is not included by default. To include it in the response, expand the total_count field.

[expand](/api/expanding_objects)

# Auto-pagination

[Auto-pagination](/api/pagination/auto)

Our libraries support auto-pagination. This feature allows you to easily iterate through large lists of resources without having to manually perform the requests to fetch subsequent pages.

# Request IDs

[Request IDs](/api/request_ids)

Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard.

[Dashboard](https://dashboard.stripe.com/logs)

To expedite the resolution process, provide the request identifier when you contact us about a specific request.
