- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Subscription Schedule object

[The Subscription Schedule object](/api/subscription_schedules/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- current_phasenullable objectObject representing the start and end dates for the current phase of the subscription schedule, if it is active.Show child attributes

Object representing the start and end dates for the current phase of the subscription schedule, if it is active.

- customerstringExpandableID of the customer who owns the subscription schedule.

ID of the customer who owns the subscription schedule.

- metadatanullable objectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- phasesarray of objectsConfiguration for the subscription schedule’s phases.Show child attributes

Configuration for the subscription schedule’s phases.

- statusenumThe present status of the subscription schedule. Possible values are not_started, active, completed, released, and canceled. You can read more about the different states in our behavior guide.Possible enum valuesactivecanceledcompletednot_startedreleased

The present status of the subscription schedule. Possible values are not_started, active, completed, released, and canceled. You can read more about the different states in our behavior guide.

[behavior guide](/billing/subscriptions/subscription-schedules)

- subscriptionnullable stringExpandableID of the subscription managed by the subscription schedule.

ID of the subscription managed by the subscription schedule.

- objectstring

- applicationnullable stringExpandableConnect only

- canceled_atnullable timestamp

- completed_atnullable timestamp

- createdtimestamp

- default_settingsobject

- end_behaviorenum

- livemodeboolean

- released_atnullable timestamp

- released_subscriptionnullable string

- test_clocknullable stringExpandable

# Create a schedule

[Create a schedule](/api/subscription_schedules/create)

Creates a new subscription schedule object. Each customer can have up to 500 active or scheduled subscriptions.

- customerstringThe identifier of the customer to create the subscription schedule for.

The identifier of the customer to create the subscription schedule for.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- phasesarray of objectsList representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, the end_date of one phase will always equal the start_date of the next phase.Show child parameters

List representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, the end_date of one phase will always equal the start_date of the next phase.

- start_datetimestamp | stringWhen the subscription schedule starts. We recommend using now so that it starts the subscription immediately. You can also use a Unix timestamp to backdate the subscription so that it starts on a past date, or set a future date for the subscription to start on.

When the subscription schedule starts. We recommend using now so that it starts the subscription immediately. You can also use a Unix timestamp to backdate the subscription so that it starts on a past date, or set a future date for the subscription to start on.

- default_settingsobject

- end_behaviorenum

- from_subscriptionstring

Returns a subscription schedule object if the call succeeded.

# Update a schedule

[Update a schedule](/api/subscription_schedules/update)

Updates an existing subscription schedule.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- phasesarray of objectsList representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, the end_date of one phase will always equal the start_date of the next phase. Note that past phases can be omitted.Show child parameters

List representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, the end_date of one phase will always equal the start_date of the next phase. Note that past phases can be omitted.

- proration_behaviorenumIf the update changes the current phase, indicates whether the changes should be prorated. The default value is create_prorations.Possible enum valuesalways_invoiceProrate changes, and force an invoice to be immediately created for any prorations.create_prorationsProrate changes, but leave any prorations as pending invoice items to be picked up on the customer’s next invoice.noneDoes not create any prorations.

If the update changes the current phase, indicates whether the changes should be prorated. The default value is create_prorations.

Prorate changes, and force an invoice to be immediately created for any prorations.

Prorate changes, but leave any prorations as pending invoice items to be picked up on the customer’s next invoice.

Does not create any prorations.

- default_settingsobject

- end_behaviorenum

Returns an updated subscription schedule object if the call succeeded.

# Retrieve a schedule

[Retrieve a schedule](/api/subscription_schedules/retrieve)

Retrieves the details of an existing subscription schedule. You only need to supply the unique subscription schedule identifier that was returned upon subscription schedule creation.

No parameters.

Returns a subscription schedule object if a valid identifier was provided.

# List all schedules

[List all schedules](/api/subscription_schedules/list)

Retrieves the list of your subscription schedules.

- customerstringOnly return subscription schedules for the given customer.

Only return subscription schedules for the given customer.

- canceled_atobject

- completed_atobject

- createdobject

- ending_beforestring

- limitinteger

- released_atobject

- scheduledboolean

- starting_afterstring

A dictionary with a data property that contains an array of up to limit subscription schedules, starting after subscription schedule starting_after. Each entry in the array is a separate subscription schedule object. If no more subscription schedules are available, the resulting array will be empty.
