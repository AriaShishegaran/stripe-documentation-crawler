- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Retrieve a quote's upfront line items

[Retrieve a quote's upfront line items](/api/quotes/line_items/upfront/list)

When retrieving a quote, there is an includable computed.upfront.line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of upfront line items.

[computed.upfront.line_items](https://stripe.com/docs/api/quotes/object#quote_object-computed-upfront-line_items)

No parameters.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit upfront line items, starting after Line Item starting_after. Each entry in the array is a separate Line Item object. If no more upfront line items are available, the resulting array will be empty.

# Retrieve a quote

[Retrieve a quote](/api/quotes/retrieve)

Retrieves the quote with the given ID.

No parameters.

Returns a quote if a valid quote ID was provided. Raises an error otherwise.

[an error](#errors)

# List all quotes

[List all quotes](/api/quotes/list)

Returns a list of your quotes.

- customerstringThe ID of the customer whose quotes will be retrieved.

The ID of the customer whose quotes will be retrieved.

- statusenumThe status of the quote.

The status of the quote.

- ending_beforestring

- limitinteger

- starting_afterstring

- test_clockstring

A dictionary with a data property that contains an array of up to limit quotes, starting after quote starting_after. Each entry in the array is a separate quote object. If no more quotes are available, the resulting array will be empty.

# Accept a quote

[Accept a quote](/api/quotes/accept)

Accepts the specified quote.

No parameters.

Returns an accepted quote and creates an invoice, subscription or subscription schedule. Raises an error otherwise.

[an error](#errors)

# Cancel a quote

[Cancel a quote](/api/quotes/cancel)

Cancels the quote.

No parameters.

Returns a canceled quote. Raises an error otherwise.

[an error](#errors)
