- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Retrieve a subscription

[Retrieve a subscription](/api/subscriptions/retrieve)

Retrieves the subscription with the given ID.

No parameters.

Returns the subscription object.

# List subscriptions

[List subscriptions](/api/subscriptions/list)

By default, returns a list of subscriptions that have not been canceled. In order to list canceled subscriptions, specify status=canceled.

- customerstringThe ID of the customer whose subscriptions will be retrieved.

The ID of the customer whose subscriptions will be retrieved.

- pricestringFilter for subscriptions that contain this recurring price ID.

Filter for subscriptions that contain this recurring price ID.

- statusenumThe status of the subscriptions to retrieve. Passing in a value of canceled will return all canceled subscriptions, including those belonging to deleted customers. Pass ended to find subscriptions that are canceled and subscriptions that are expired due to incomplete payment. Passing in a value of all will return subscriptions of all statuses. If no value is supplied, all subscriptions that have not been canceled are returned.

The status of the subscriptions to retrieve. Passing in a value of canceled will return all canceled subscriptions, including those belonging to deleted customers. Pass ended to find subscriptions that are canceled and subscriptions that are expired due to incomplete payment. Passing in a value of all will return subscriptions of all statuses. If no value is supplied, all subscriptions that have not been canceled are returned.

[incomplete payment](/billing/subscriptions/overview#subscription-statuses)

- automatic_taxobject

- collection_methodenum

- createdobject

- ending_beforestring

- limitinteger

- starting_afterstring

- test_clockstring

Returns a list of subscriptions.

# Cancel a subscription

[Cancel a subscription](/api/subscriptions/cancel)

Cancels a customer’s subscription immediately. The customer will not be charged again for the subscription.

Note, however, that any pending invoice items that you’ve created will still be charged for at the end of the period, unless manually deleted. If you’ve set the subscription to cancel at the end of the period, any pending prorations will also be left in place and collected at the end of the period. But if the subscription is set to cancel immediately, pending prorations will be removed.

[deleted](#delete_invoiceitem)

By default, upon subscription cancellation, Stripe will stop automatic collection of all finalized invoices for the customer. This is intended to prevent unexpected payment attempts after the customer has canceled a subscription. However, you can resume automatic collection of the invoices manually after subscription cancellation to have us proceed. Or, you could check for unpaid invoices before allowing the customer to cancel the subscription at all.

No parameters.

- cancellation_detailsobject

- invoice_nowboolean

- prorateboolean

The canceled Subscription object. Its subscription status will be set to canceled.

# Resume a subscription

[Resume a subscription](/api/subscriptions/resume)

Initiates resumption of a paused subscription, optionally resetting the billing cycle anchor and creating prorations. If a resumption invoice is generated, it must be paid or marked uncollectible before the subscription will be unpaused. If payment succeeds the subscription will become active, and if payment fails the subscription will be past_due. The resumption invoice will void automatically if not paid by the expiration date.

- billing_cycle_anchorstringEither now or unchanged. Setting the value to now resets the subscription’s billing cycle anchor to the current time (in UTC). Setting the value to unchanged advances the subscription’s billing cycle anchor to the period that surrounds the current time. For more information, see the billing cycle documentation.

Either now or unchanged. Setting the value to now resets the subscription’s billing cycle anchor to the current time (in UTC). Setting the value to unchanged advances the subscription’s billing cycle anchor to the period that surrounds the current time. For more information, see the billing cycle documentation.

[documentation](/billing/subscriptions/billing-cycle)

- proration_behaviorenumDetermines how to handle prorations when the billing cycle changes (e.g., when switching plans, resetting billing_cycle_anchor=now, or starting a trial), or if an item’s quantity changes. The default value is create_prorations.Possible enum valuesalways_invoiceAlways invoice immediately for prorations.create_prorationsWill cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under certain conditions.noneDisable creating prorations in this request.

Determines how to handle prorations when the billing cycle changes (e.g., when switching plans, resetting billing_cycle_anchor=now, or starting a trial), or if an item’s quantity changes. The default value is create_prorations.

[prorations](/billing/subscriptions/prorations)

Always invoice immediately for prorations.

Will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under certain conditions.

[certain conditions](/subscriptions/upgrading-downgrading#immediate-payment)

Disable creating prorations in this request.

- proration_datetimestamp

The subscription object.

# Search subscriptions

[Search subscriptions](/api/subscriptions/search)

Search for subscriptions you’ve previously created using Stripe’s Search Query Language. Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up to an hour behind during outages. Search functionality is not available to merchants in India.

[Search Query Language](/search#search-query-language)

- querystringRequiredThe search query string. See search query language and the list of supported query fields for subscriptions.

The search query string. See search query language and the list of supported query fields for subscriptions.

[search query language](/search#search-query-language)

[query fields for subscriptions](/search#query-fields-for-subscriptions)

- limitintegerA limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- pagestringA cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.

A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.

A dictionary with a data property that contains an array of up to limit subscriptions. If no objects match the query, the resulting array will be empty. See the related guide on expanding properties in lists.

[expanding properties in lists](/expand#lists)
