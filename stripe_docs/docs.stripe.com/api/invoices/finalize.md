- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Finalize an invoice

[Finalize an invoice](/api/invoices/finalize)

Stripe automatically finalizes drafts before sending and attempting payment on invoices. However, if you’d like to finalize a draft invoice manually, you can do so using this method.

- auto_advancebooleanControls whether Stripe performs automatic collection of the invoice. If false, the invoice’s state doesn’t automatically advance without an explicit action.

Controls whether Stripe performs automatic collection of the invoice. If false, the invoice’s state doesn’t automatically advance without an explicit action.

[automatic collection](/invoicing/integration/automatic-advancement-collection)

Returns an invoice object with status=open.

# Mark an invoice as uncollectible

[Mark an invoice as uncollectible](/api/invoices/mark_uncollectible)

Marking an invoice as uncollectible is useful for keeping track of bad debts that can be written off for accounting purposes.

No parameters.

Returns the invoice object.

# Pay an invoice

[Pay an invoice](/api/invoices/pay)

Stripe automatically creates and then attempts to collect payment on invoices for customers on subscriptions according to your subscriptions settings. However, if you’d like to attempt payment on an invoice out of the normal collection schedule or for some other reason, you can do so.

[subscriptions settings](https://dashboard.stripe.com/account/billing/automatic)

No parameters.

- forgiveboolean

- mandatestring

- off_sessionboolean

- paid_out_of_bandboolean

- payment_methodstring

- sourcestring

Returns the invoice object.

# Search invoices

[Search invoices](/api/invoices/search)

Search for invoices you’ve previously created using Stripe’s Search Query Language. Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up to an hour behind during outages. Search functionality is not available to merchants in India.

[Search Query Language](/search#search-query-language)

- querystringRequiredThe search query string. See search query language and the list of supported query fields for invoices.

The search query string. See search query language and the list of supported query fields for invoices.

[search query language](/search#search-query-language)

[query fields for invoices](/search#query-fields-for-invoices)

- limitintegerA limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- pagestringA cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.

A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.

A dictionary with a data property that contains an array of up to limit invoices. If no objects match the query, the resulting array will be empty. See the related guide on expanding properties in lists.

[expanding properties in lists](/expand#lists)

# Send an invoice for manual payment

[Send an invoice for manual payment](/api/invoices/send)

Stripe will automatically send invoices to customers according to your subscriptions settings. However, if you’d like to manually send an invoice to your customer out of the normal schedule, you can do so. When sending invoices that have already been paid, there will be no reference to the payment in the email.

[subscriptions settings](https://dashboard.stripe.com/account/billing/automatic)

Requests made in test-mode result in no emails being sent, despite sending an invoice.sent event.

No parameters.

Returns the invoice object.
