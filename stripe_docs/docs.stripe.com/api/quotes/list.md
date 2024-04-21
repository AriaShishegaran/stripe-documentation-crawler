- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# Download quote PDF

[Download quote PDF](/api/quotes/pdf)

Download the PDF for a finalized quote. Explanation for special handling can be found here

[here](https://docs.corp.stripe.com/quotes/overview#quote_pdf)

No parameters.

The PDF file for the quote.

# Finalize a quote

[Finalize a quote](/api/quotes/finalize)

Finalizes the quote.

No parameters.

- expires_attimestamp

Returns an open quote. Raises an error otherwise.

[an error](#errors)
