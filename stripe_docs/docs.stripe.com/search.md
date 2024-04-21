# Search

Some top level API resources support retrieval with search API methods. You can use the search APIs to retrieve your Stripe objects in a flexible manner. Using search is a faster alternative to paginating through all resources. To create a search query, review the Search query language and reference the query fields of the resource:

[paginating](/api/pagination)

[Search query language](/search#search-query-language)

- Query fields for charges

[Query fields for charges](/search#query-fields-for-charges)

- Query fields for customers

[Query fields for customers](/search#query-fields-for-customers)

- Query fields for invoices

[Query fields for invoices](/search#query-fields-for-invoices)

- Query fields for PaymentIntents

[Query fields for PaymentIntents](/search#query-fields-for-payment-intents)

- Query fields for prices

[Query fields for prices](/search#query-fields-for-prices)

- Query fields for products

[Query fields for products](/search#query-fields-for-products)

- Query fields for subscriptions

[Query fields for subscriptions](/search#query-fields-for-subscriptions)

## Examples

Here are some examples of what you can do with the Search charges API and Search PaymentIntents API:

[Search charges API](/api/charges/search)

[Search PaymentIntents API](/api/payment_intents/search)

Look up charges matching a custom metadata value.

Look up charges matching the last 4 digits of the card used for the payment.

Look up customers matching an email.

Look up PaymentIntents not in the USD currency.

Filter invoice objects with a total greater than 1000.

Look up charges matching a combination of metadata and currency.

## Search query language

A query clause consists of a field followed by an operator followed by a value:

You can combine multiple query clauses in a search by either separating them with a space, or using the AND or OR keywords (case insensitive). By default, the API combines clauses with AND logic. AND and OR operators are mutually exclusive.

The example query email:"amy@rocketrides.io" metadata["key"]:"value" matches records where both the email address is amy@rocketrides.io, and the metadata in the record includes key with a value of value.

You can negate query clauses using a - character. For example, the following search returns records that don’t match the email amy@rocketrides.io.

-email:"amy@rocketrides.io"

Every search field supports exact matching with a :. Certain fields such as email and name support substring matching. Certain other fields such as amount support numeric comparators like > and <.

Each field includes a type that defines the operations you can use in the field. For a full list of available fields, see supported query fields for each resource.

[supported query fields for each resource](/search#supported-query-fields-for-each-resource)

Using an unsupported operator, such as specifying greater than (>) on a string, returns an error.

string

exact match, substring (case insensitive)

An exact match on a string type returns any record where that record contains all of the words from the query in the same order. For example the query name:"one two three" would match both a result with the name “one two three” and a result with the name “one two three four”.

You must use quotation marks around string values. Quotation marks are optional for numeric values. For example:

- currency:"usd" means quotes are required.

- payment_method_details.card.last4:1234 means quotes are optional.

You can escape quotes inside of quotes with a backslash (\).

description:"the story called \"The Sky and the Sea.\""

You can perform searches on metadata that you’ve added to objects that support it.

[metadata](/api/metadata)

Use the following format to construct a clause for a metadata search: metadata["<field>"]:"<value>".

The following clause demonstrates how to create a clause that queries for records with a donation ID of “asdf-jkl”: metadata["donation-id"]:"asdf-jkl".

You can query for the presence of a metadata key on an object. The following clause would match all records where donation-id is a metadata key. -metadata["donation-id"]:null

The following table lists the syntax that you can use to construct a query.

- field<value

- field>value

- field>=value

- field<=value

## Supported query fields for each resource

For SOURCE, use card, card_present, or interac_present. Use card for online charges, interac_present for Terminal card present charges for the Interac network, and card_present for other Terminal card present charges.

The disputed field accepts only the tokens “true” and “false”, indicating the presence of disputes.

refunded:"true" filters for fully-refunded charges, refunded:"false" filters for partially-refunded charges, and refunded:null filters for non-refunded charges.

## Limitations

The minimum supported API Version to use search is 2020-08-27. Read our API upgrades guide to learn more about upgrades. To use search without upgrading your account API version, you can override the API version on a single request by setting the Stripe-Version request header:

[API upgrades guide](/upgrades)

Read our server-side libraries guide on how to override an API version when using a library.

[server-side libraries](/libraries#versioning)

Don’t use search for read-after-write flows (for example, searching immediately after a charge is made) because the data won’t be immediately available to search. Under normal operating conditions, data is searchable in under 1 minute. Propagation of new or updated data could be delayed during an outage.

We apply a rate limit of up to 20 read operations per second which applies for all search endpoints in both live mode and test mode. Live mode and test mode limits are separate. Keeping the rate limit in mind, for workloads where you need to run analytics on one or more API resource(s), Sigma is much more efficient. For workloads where you need to export a large portion of your API resource, our Data Pipeline product is more efficient.

[rate limit](/rate-limits)

[Sigma](/stripe-data/access-data-in-dashboard)

[Data Pipeline](/stripe-data/access-data-in-warehouse)

Search isn’t available to merchants in India.
