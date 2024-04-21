htmlUpdate a schedule | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Update a schedule

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

GET/v1/subscription_schedules/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/subscription_schedules/sub_sched_1Mr3YdLkdIwHu7ixjop3qtff \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "sub_sched_1Mr3YdLkdIwHu7ixjop3qtff",  "object": "subscription_schedule",  "application": null,  "canceled_at": null,  "completed_at": null,  "created": 1680113835,  "current_phase": null,  "customer": "cus_NcI8FsMbh0OeFs",  "default_settings": {    "application_fee_percent": null,    "automatic_tax": {      "enabled": false,      "liability": null    },    "billing_cycle_anchor": "automatic",    "billing_thresholds": null,    "collection_method": "charge_automatically",    "default_payment_method": null,    "default_source": null,    "description": null,    "invoice_settings": {      "issuer": {        "type": "self"      }    },    "on_behalf_of": null,    "transfer_data": null  },  "end_behavior": "release",  "livemode": false,  "metadata": {},  "phases": [    {      "add_invoice_items": [],      "application_fee_percent": null,      "billing_cycle_anchor": null,      "billing_thresholds": null,      "collection_method": null,      "coupon": null,      "currency": "usd",      "default_payment_method": null,      "default_tax_rates": [],      "description": null,      "end_date": 1712339228,      "invoice_settings": null,      "items": [        {          "billing_thresholds": null,          "metadata": {},          "plan": "price_1Mr3YcLkdIwHu7ixYCFhXHNb",          "price": "price_1Mr3YcLkdIwHu7ixYCFhXHNb",          "quantity": 1,          "tax_rates": []        }      ],      "metadata": {},      "on_behalf_of": null,      "proration_behavior": "create_prorations",      "start_date": 1680716828,      "transfer_data": null,      "trial_end": null    }  ],  "released_at": null,  "released_subscription": null,  "renewal_interval": null,  "status": "not_started",  "subscription": null,  "test_clock": null}`# List all schedules

Retrieves the list of your subscription schedules.

### Parameters

- customerstringOnly return subscription schedules for the given customer.



### More parametersExpand all

- canceled_atobject
- completed_atobject
- createdobject
- ending_beforestring
- limitinteger
- released_atobject
- scheduledboolean
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit subscription schedules, starting after subscription schedule starting_after. Each entry in the array is a separate subscription schedule object. If no more subscription schedules are available, the resulting array will be empty.

GET/v1/subscription_schedulesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/subscription_schedules \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/subscription_schedules",  "has_more": false,  "data": [    {      "id": "sub_sched_1Mr3YdLkdIwHu7ixjop3qtff",      "object": "subscription_schedule",      "application": null,      "canceled_at": null,      "completed_at": null,      "created": 1680113835,      "current_phase": null,      "customer": "cus_NcI8FsMbh0OeFs",      "default_settings": {        "application_fee_percent": null,        "automatic_tax": {          "enabled": false,          "liability": null        },        "billing_cycle_anchor": "automatic",        "billing_thresholds": null,        "collection_method": "charge_automatically",        "default_payment_method": null,        "default_source": null,        "description": null,        "invoice_settings": {          "issuer": {            "type": "self"          }        },        "on_behalf_of": null,        "transfer_data": null      },      "end_behavior": "release",      "livemode": false,      "metadata": {},      "phases": [        {          "add_invoice_items": [],          "application_fee_percent": null,          "billing_cycle_anchor": null,          "billing_thresholds": null,          "collection_method": null,          "coupon": null,          "currency": "usd",          "default_payment_method": null,          "default_tax_rates": [],          "description": null,          "end_date": 1712339228,          "invoice_settings": null,          "items": [            {              "billing_thresholds": null,              "metadata": {},              "plan": "price_1Mr3YcLkdIwHu7ixYCFhXHNb",              "price": "price_1Mr3YcLkdIwHu7ixYCFhXHNb",              "quantity": 1,              "tax_rates": []            }          ],          "metadata": {},          "on_behalf_of": null,          "proration_behavior": "create_prorations",          "start_date": 1680716828,          "transfer_data": null,          "trial_end": null        }      ],      "released_at": null,      "released_subscription": null,      "renewal_interval": null,      "status": "not_started",      "subscription": null,      "test_clock": null    }    {...}    {...}  ],}`# Cancel a schedule

Cancels a subscription schedule and its associated subscription immediately (if the subscription schedule has an active subscription). A subscription schedule can only be canceled if its status is not_started or active.

### Parameters

- invoice_nowbooleanIf the subscription schedule is active, indicates if a final invoice will be generated that contains any un-invoiced metered usage and new/pending proration invoice items. Defaults to true.



### More parametersExpand all

- prorateboolean

### Returns

The canceled subscription_schedule object. Its status will be canceled and canceled_at will be the current time.

POST/v1/subscription_schedules/:id/cancelServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/subscription_schedules/sub_sched_1Mr3owLkdIwHu7ix38CXMudt/cancel \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "sub_sched_1Mr3owLkdIwHu7ix38CXMudt",  "object": "subscription_schedule",  "application": null,  "canceled_at": 1680114847,  "completed_at": null,  "created": 1680114846,  "current_phase": null,  "customer": "cus_NcIPFRC981NmaY",  "default_settings": {    "application_fee_percent": null,    "automatic_tax": {      "enabled": false,      "liability": null    },    "billing_cycle_anchor": "automatic",    "billing_thresholds": null,    "collection_method": "charge_automatically",    "default_payment_method": null,    "default_source": null,    "description": null,    "invoice_settings": {      "issuer": {        "type": "self"      }    },    "on_behalf_of": null,    "transfer_data": null  },  "end_behavior": "release",  "livemode": false,  "metadata": {},  "phases": [    {      "add_invoice_items": [],      "application_fee_percent": null,      "billing_cycle_anchor": null,      "billing_thresholds": null,      "collection_method": null,      "coupon": null,      "currency": "usd",      "default_payment_method": null,      "default_tax_rates": [],      "description": null,      "end_date": 1712339228,      "invoice_settings": null,      "items": [        {          "billing_thresholds": null,          "metadata": {},          "plan": "price_1Mr3owLkdIwHu7ix0RyYpQzk",          "price": "price_1Mr3owLkdIwHu7ix0RyYpQzk",          "quantity": 1,          "tax_rates": []        }      ],      "metadata": {},      "on_behalf_of": null,      "proration_behavior": "create_prorations",      "start_date": 1680716828,      "transfer_data": null,      "trial_end": null    }  ],  "released_at": null,  "released_subscription": null,  "renewal_interval": null,  "status": "canceled",  "subscription": null,  "test_clock": null}`# Release a schedule

Releases the subscription schedule immediately, which will stop scheduling of its phases, but leave any existing subscription in place. A schedule can only be released if its status is not_started or active. If the subscription schedule is currently associated with a subscription, releasing it will remove its subscription property and set the subscription’s ID to the released_subscription property.

### Parameters

No parameters.

### More parametersExpand all

- preserve_cancel_dateboolean

### Returns

The released subscription_schedule object. Its status will be released, released_at will be the current time, and released_subscription will be the ID of the subscription the subscription schedule managed prior to being released.

POST/v1/subscription_schedules/:id/releaseServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/subscription_schedules/sub_sched_1Mr3hWLkdIwHu7ixA5zxZvNI/release \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "sub_sched_1Mr3hWLkdIwHu7ixA5zxZvNI",  "object": "subscription_schedule",  "application": null,  "canceled_at": null,  "completed_at": null,  "created": 1680114386,  "current_phase": null,  "customer": "cus_NcII9GZkTPAnor",  "default_settings": {    "application_fee_percent": null,    "automatic_tax": {      "enabled": false,      "liability": null    },    "billing_cycle_anchor": "automatic",    "billing_thresholds": null,    "collection_method": "charge_automatically",    "default_payment_method": null,    "default_source": null,    "description": null,    "invoice_settings": {      "issuer": {        "type": "self"      }    },    "on_behalf_of": null,    "transfer_data": null  },  "end_behavior": "release",  "livemode": false,  "metadata": {},  "phases": [    {      "add_invoice_items": [],      "application_fee_percent": null,      "billing_cycle_anchor": null,      "billing_thresholds": null,      "collection_method": null,      "coupon": null,      "currency": "usd",      "default_payment_method": null,      "default_tax_rates": [],      "description": null,      "end_date": 1712339228,      "invoice_settings": null,      "items": [        {          "billing_thresholds": null,          "metadata": {},          "plan": "price_1Mr3hVLkdIwHu7ixWuJp9ew0",          "price": "price_1Mr3hVLkdIwHu7ixWuJp9ew0",          "quantity": 1,          "tax_rates": []        }      ],      "metadata": {},      "on_behalf_of": null,      "proration_behavior": "create_prorations",      "start_date": 1680716828,      "transfer_data": null,      "trial_end": null    }  ],  "released_at": 1680114386,  "released_subscription": null,  "renewal_interval": null,  "status": "released",  "subscription": null,  "test_clock": null}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`