# Metadata

Metadata is an attribute on certain Stripe objects that lets you store more information, structured as key-value pairs, to these objects for your own use and reference. For example, you can store your user’s full name and corresponding unique identifier from your system on a Stripe Customer object.

[Metadata](/api/metadata)

[Stripe Customer](/api/customers)

## Configuration

You can add 50 total key-value pairs within these data limits:

- key: 40 character limit.

- value: 500 character limit.

If your system requires more space than this, store your data in your external database and use a key-value pair to store the external object’s ID in metadata.

Unless you use metadata with Radar, Stripe doesn’t use metadata—for example, to authorize or decline a charge. Additionally, metadata isn’t visible to your customers unless you choose to show it.

[Radar](/radar)

Never store sensitive information, such as bank account information or credit card details, to metadata.

Some Stripe objects also contain a description attribute, which allows you to annotate a payment with a single string. You can use it present information to customers, such as with a receipt description.

Stripe only returns metadata when you use a secret key in your requests. We redact metadata from objects in response to publishable key requests, such as Stripe.js or Mobile SDKs client-side requests.

[secret key](/keys#obtain-api-keys)

## Add metadata

Use the metadata attribute in an API call to pass and store information in key-value pairs.

## Update metadata

Replace values for existing keys and add new key-value pairs in an API call.

For example, you can update a Customer object with an existing key-value pair of "loyalty_program": "no" to"loyalty_program": "yes". You can also add new metadata, such as the "loyalty_member_id": "12345678" key-value pair in the example below, to the existing metadata.

[Customer](/api/customers)

## Delete metadata

Delete a single key or an entire set of keys using the API.

Pass in the key with an empty string as the value to remove the key from the metadata.

Pass an empty object as the value for the metadata attribute to delete all of the keys at once.

## Copy metadata to another object

An object’s metadata doesn’t automatically copy to related objects. To view an object’s metadata, you must inspect that object. To retrieve metadata from a related object, build custom logic to find and inspect the related object. To explicitly copy metadata from one object to another, you need to build your own flow.

In certain cases, we copy metadata from one object to another for backwards compatibility and other unique scenarios.

[Payment Intent](/api/payment_intents)

[Charge](/api/charges)

[Payment Link](/api/payment_links/payment_links)

[Checkout Session](/api/checkout/sessions)

[Subscription](/api/subscriptions)

[Invoice](/api/invoices)

[subscription_details.metadata](/api/invoices/object#invoice_object-subscription_details-metadata)

[Subscription](/api/subscriptions)

[Invoice Line Item](/api/invoices/line_item)

[type](/api/invoices/line_item#invoice_line_item_object-type)

[Checkout Session](/api/checkout/sessions)

[Payment Intent](/api/payment_intents)

[payment_intent_data.metadata](/api/checkout/sessions/create#create_checkout_session-payment_intent_data-metadata)

[Checkout Session](/api/checkout/sessions)

[Subscription](/api/subscriptions)

[subscription_data.metadata](/api/quotes/create#create_quote-subscription_data-metadata)

[Prices](/api/prices)

[Products](/api/products)

[product_data.metadata](/api/prices/create#create_price-product_data-metadata)

[Subscription Schedule](/api/subscription_schedules)

[Subscription](/api/subscriptions)

[phases.metadata](/api/subscription_schedules/create#create_subscription_schedule-phases-metadata)

[Quote](/api/quotes)

[Subscription](/api/subscriptions)

[subscription_data.metadata](/api/quotes/object#quote_object-subscription_data-metadata)

## Events and webhook endpoints

When Stripe sends an Event to your webhook endpoint, it includes the corresponding object and any metadata the object contains. This allows your webhook handler to receive any metadata that you set on Stripe objects and pass it to downstream processes, such as order fulfillment.

[Event](/api/events)

[webhook endpoint](/webhooks)

For example, to include a cart ID when a customer makes a purchase using a Checkout Session, provide it as metadata when you create the Checkout Session:

[Checkout Session](/api/checkout/sessions)

[https://example.com/success](https://example.com/success)

When the customer completes the checkout process, we send a checkout.session.completed Event containing the Checkout Session object’s metadata to your webhook endpoint. You must configure your webhook to listen for that Event so you can access the metadata and use it when processing data.

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

## Search metadata

You can search for existing metadata on supported objects by using specific formatting. This includes searching for records with a specific value for a metadata field or checking if a metadata key is present on an object. Learn more about searching for metadata.

[searching for metadata](/search#metadata)

## Prevent fraud with metadata and Radar

Use metadata with Radar to create custom rules that help prevent fraud. Learn more about Radar metadata attributes.

[Radar metadata attributes](/radar/rules/reference#metadata-attributes)
