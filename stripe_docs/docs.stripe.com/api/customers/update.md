- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Update a customer

[Update a customer](/api/customers/update)

Updates the specified customer by setting the values of the parameters passed. Any parameters not provided will be left unchanged.  For example, if you pass the source parameter, that becomes the customer’s active source (e.g., a card) to be used for all charges in the future. When you update a customer to a new valid card source by passing the source parameter: for each of the customer’s current subscriptions, if the subscription bills automatically and is in the past_due state, then the latest open invoice for the subscription with automatic collection enabled will be retried. This retry will not count as an automatic retry, and will not affect the next regularly scheduled payment for the invoice. Changing the default_source for a customer will not trigger this behavior.

This request accepts mostly the same arguments as the customer creation call.

- addressobjectThe customer’s address.Show child parameters

The customer’s address.

- descriptionstringAn arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard.

An arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard.

- emailstringCustomer’s email address. It’s displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to 512 characters.

Customer’s email address. It’s displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to 512 characters.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- namestringThe customer’s full name or business name.

The customer’s full name or business name.

- phonestringThe customer’s phone number.

The customer’s phone number.

- shippingobjectThe customer’s shipping information. Appears on invoices emailed to this customer.Show child parameters

The customer’s shipping information. Appears on invoices emailed to this customer.

- balanceinteger

- cash_balanceobject

- couponstring

- default_sourcestring

- invoice_prefixstring

- invoice_settingsobject

- next_invoice_sequenceinteger

- preferred_localesarray of strings

- promotion_codestring

- sourcestring

- taxobject

- tax_exemptenum

Returns the customer object if the update succeeded. Raises an error if update parameters are invalid (e.g. specifying an invalid coupon or an invalid source).

[an error](#errors)

# Retrieve a customer

[Retrieve a customer](/api/customers/retrieve)

Retrieves a Customer object.

No parameters.

Returns the Customer object for a valid identifier. If it’s for a deleted Customer, a subset of the customer’s information is returned, including a deleted property that’s set to true.

# List all customers

[List all customers](/api/customers/list)

Returns a list of your customers. The customers are returned sorted by creation date, with the most recent customers appearing first.

- emailstringA case-sensitive filter on the list based on the customer’s email field. The value must be a string.

A case-sensitive filter on the list based on the customer’s email field. The value must be a string.

- createdobject

- ending_beforestring

- limitinteger

- starting_afterstring

- test_clockstring

A dictionary with a data property that contains an array of up to limit customers, starting after customer starting_after. Passing an optional email will result in filtering to customers with only that exact email address. Each entry in the array is a separate customer object. If no more customers are available, the resulting array will be empty.

# Delete a customer

[Delete a customer](/api/customers/delete)

Permanently deletes a customer. It cannot be undone. Also immediately cancels any active subscriptions on the customer.

No parameters.

Returns an object with a deleted parameter on success. If the customer ID does not exist, this call raises an error.

[an error](#errors)

Unlike other objects, deleted customers can still be retrieved through the API in order to be able to track their history. Deleting customers removes all credit card details and prevents any further operations to be performed (such as adding a new subscription).

# Search customers

[Search customers](/api/customers/search)

Search for customers you’ve previously created using Stripe’s Search Query Language. Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up to an hour behind during outages. Search functionality is not available to merchants in India.

[Search Query Language](/search#search-query-language)

- querystringRequiredThe search query string. See search query language and the list of supported query fields for customers.

The search query string. See search query language and the list of supported query fields for customers.

[search query language](/search#search-query-language)

[query fields for customers](/search#query-fields-for-customers)

- limitintegerA limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- pagestringA cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.

A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.

A dictionary with a data property that contains an array of up to limit customers. If no objects match the query, the resulting array will be empty. See the related guide on expanding properties in lists.

[expanding properties in lists](/expand#lists)
