htmlSubscription Schedule | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Subscription Schedule

A subscription schedule allows you to create and manage the lifecycle of a subscription by predefining expected changes.

Related guide: Subscription schedules

Endpoints
# The Subscription Schedule object

### Attributes

- idstringUnique identifier for the object.


- current_phasenullableobjectObject representing the start and end dates for the current phase of the subscription schedule, if it is active.

Show child attributes
- customerstringExpandableID of the customer who owns the subscription schedule.


- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- phasesarray of objectsConfiguration for the subscription schedule’s phases.

Show child attributes
- statusenumThe present status of the subscription schedule. Possible values are not_started, active, completed, released, and canceled. You can read more about the different states in our behavior guide.

Possible enum values`active``canceled``completed``not_started``released`
- subscriptionnullablestringExpandableID of the subscription managed by the subscription schedule.



### More attributesExpand all

- objectstring
- applicationnullablestringExpandableConnect only
- canceled_atnullabletimestamp
- completed_atnullabletimestamp
- createdtimestamp
- default_settingsobject
- end_behaviorenum
- livemodeboolean
- released_atnullabletimestamp
- released_subscriptionnullablestring
- test_clocknullablestringExpandable

# Create a schedule

Creates a new subscription schedule object. Each customer can have up to 500 active or scheduled subscriptions.

### Parameters

- customerstringThe identifier of the customer to create the subscription schedule for.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- phasesarray of objectsList representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, the end_date of one phase will always equal the start_date of the next phase.

Show child parameters
- start_datetimestamp | stringWhen the subscription schedule starts. We recommend using now so that it starts the subscription immediately. You can also use a Unix timestamp to backdate the subscription so that it starts on a past date, or set a future date for the subscription to start on.



### More parametersExpand all

- default_settingsobject
- end_behaviorenum
- from_subscriptionstring

### Returns

Returns a subscription schedule object if the call succeeded.

POST/v1/subscription_schedulesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/subscription_schedules \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d customer=cus_NcI8FsMbh0OeFs \  -d start_date=1680716828 \  -d end_behavior=release \  -d "phases[0][items][0][price]"=price_1Mr3YcLkdIwHu7ixYCFhXHNb \  -d "phases[0][items][0][quantity]"=1 \  -d "phases[0][iterations]"=12`Response`{  "id": "sub_sched_1Mr3YdLkdIwHu7ixjop3qtff",  "object": "subscription_schedule",  "application": null,  "canceled_at": null,  "completed_at": null,  "created": 1680113835,  "current_phase": null,  "customer": "cus_NcI8FsMbh0OeFs",  "default_settings": {    "application_fee_percent": null,    "automatic_tax": {      "enabled": false,      "liability": null    },    "billing_cycle_anchor": "automatic",    "billing_thresholds": null,    "collection_method": "charge_automatically",    "default_payment_method": null,    "default_source": null,    "description": null,    "invoice_settings": {      "issuer": {        "type": "self"      }    },    "on_behalf_of": null,    "transfer_data": null  },  "end_behavior": "release",  "livemode": false,  "metadata": {},  "phases": [    {      "add_invoice_items": [],      "application_fee_percent": null,      "billing_cycle_anchor": null,      "billing_thresholds": null,      "collection_method": null,      "coupon": null,      "currency": "usd",      "default_payment_method": null,      "default_tax_rates": [],      "description": null,      "end_date": 1712339228,      "invoice_settings": null,      "items": [        {          "billing_thresholds": null,          "metadata": {},          "plan": "price_1Mr3YcLkdIwHu7ixYCFhXHNb",          "price": "price_1Mr3YcLkdIwHu7ixYCFhXHNb",          "quantity": 1,          "tax_rates": []        }      ],      "metadata": {},      "on_behalf_of": null,      "proration_behavior": "create_prorations",      "start_date": 1680716828,      "transfer_data": null,      "trial_end": null    }  ],  "released_at": null,  "released_subscription": null,  "renewal_interval": null,  "status": "not_started",  "subscription": null,  "test_clock": null}`# Update a schedule

Updates an existing subscription schedule.

### Parameters

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- phasesarray of objectsList representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, the end_date of one phase will always equal the start_date of the next phase. Note that past phases can be omitted.

Show child parameters
- proration_behaviorenumIf the update changes the current phase, indicates whether the changes should be prorated. The default value is create_prorations.

Possible enum values`always_invoice`Prorate changes, and force an invoice to be immediately created for any prorations.

`create_prorations`Prorate changes, but leave any prorations as pending invoice items to be picked up on the customer’s next invoice.

`none`Does not create any prorations.



### More parametersExpand all

- default_settingsobject
- end_behaviorenum

### Returns

Returns an updated subscription schedule object if the call succeeded.

POST/v1/subscription_schedules/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/subscription_schedules/sub_sched_1Mr3YdLkdIwHu7ixjop3qtff \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d end_behavior=release`Response`{  "id": "sub_sched_1Mr3YdLkdIwHu7ixjop3qtff",  "object": "subscription_schedule",  "application": null,  "canceled_at": null,  "completed_at": null,  "created": 1680113835,  "current_phase": null,  "customer": "cus_NcI8FsMbh0OeFs",  "default_settings": {    "application_fee_percent": null,    "automatic_tax": {      "enabled": false,      "liability": null    },    "billing_cycle_anchor": "automatic",    "billing_thresholds": null,    "collection_method": "charge_automatically",    "default_payment_method": null,    "default_source": null,    "description": null,    "invoice_settings": {      "issuer": {        "type": "self"      }    },    "on_behalf_of": null,    "transfer_data": null  },  "end_behavior": "release",  "livemode": false,  "metadata": {},  "phases": [    {      "add_invoice_items": [],      "application_fee_percent": null,      "billing_cycle_anchor": null,      "billing_thresholds": null,      "collection_method": null,      "coupon": null,      "currency": "usd",      "default_payment_method": null,      "default_tax_rates": [],      "description": null,      "end_date": 1712339228,      "invoice_settings": null,      "items": [        {          "billing_thresholds": null,          "metadata": {},          "plan": "price_1Mr3YcLkdIwHu7ixYCFhXHNb",          "price": "price_1Mr3YcLkdIwHu7ixYCFhXHNb",          "quantity": 1,          "tax_rates": []        }      ],      "metadata": {},      "on_behalf_of": null,      "proration_behavior": "create_prorations",      "start_date": 1680716828,      "transfer_data": null,      "trial_end": null    }  ],  "released_at": null,  "released_subscription": null,  "renewal_interval": null,  "status": "not_started",  "subscription": null,  "test_clock": null}`# Retrieve a schedule

Retrieves the details of an existing subscription schedule. You only need to supply the unique subscription schedule identifier that was returned upon subscription schedule creation.

### Parameters

No parameters.

### Returns

Returns a subscription schedule object if a valid identifier was provided.

GET/v1/subscription_schedules/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/subscription_schedules/sub_sched_1Mr3YdLkdIwHu7ixjop3qtff \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "sub_sched_1Mr3YdLkdIwHu7ixjop3qtff",  "object": "subscription_schedule",  "application": null,  "canceled_at": null,  "completed_at": null,  "created": 1680113835,  "current_phase": null,  "customer": "cus_NcI8FsMbh0OeFs",  "default_settings": {    "application_fee_percent": null,    "automatic_tax": {      "enabled": false,      "liability": null    },    "billing_cycle_anchor": "automatic",    "billing_thresholds": null,    "collection_method": "charge_automatically",    "default_payment_method": null,    "default_source": null,    "description": null,    "invoice_settings": {      "issuer": {        "type": "self"      }    },    "on_behalf_of": null,    "transfer_data": null  },  "end_behavior": "release",  "livemode": false,  "metadata": {},  "phases": [    {      "add_invoice_items": [],      "application_fee_percent": null,      "billing_cycle_anchor": null,      "billing_thresholds": null,      "collection_method": null,      "coupon": null,      "currency": "usd",      "default_payment_method": null,      "default_tax_rates": [],      "description": null,      "end_date": 1712339228,      "invoice_settings": null,      "items": [        {          "billing_thresholds": null,          "metadata": {},          "plan": "price_1Mr3YcLkdIwHu7ixYCFhXHNb",          "price": "price_1Mr3YcLkdIwHu7ixYCFhXHNb",          "quantity": 1,          "tax_rates": []        }      ],      "metadata": {},      "on_behalf_of": null,      "proration_behavior": "create_prorations",      "start_date": 1680716828,      "transfer_data": null,      "trial_end": null    }  ],  "released_at": null,  "released_subscription": null,  "renewal_interval": null,  "status": "not_started",  "subscription": null,  "test_clock": null}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`