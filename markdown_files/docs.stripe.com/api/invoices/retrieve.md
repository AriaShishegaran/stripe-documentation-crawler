htmlRetrieve an invoice | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Retrieve an invoice

Retrieves the invoice with the given ID.

### Parameters

No parameters.

### Returns

Returns an invoice object if a valid invoice ID was provided. Raises an error otherwise.

The invoice object contains a lines hash that contains information about the subscriptions and invoice items that have been applied to the invoice, as well as any prorations that Stripe has automatically calculated. Each line on the invoice has an amount attribute that represents the amount actually contributed to the invoice’s total. For invoice items and prorations, the amount attribute is the same as for the invoice item or proration respectively. For subscriptions, the amount may be different from the plan’s regular price depending on whether the invoice covers a trial period or the invoice period differs from the plan’s usual interval.

The invoice object has both a subtotal and a total. The subtotal represents the total before any discounts, while the total is the final amount to be charged to the customer after all coupons have been applied.

The invoice also has a next_payment_attempt attribute that tells you the next time (as a Unix timestamp) payment for the invoice will be automatically attempted. For invoices with manual payment collection, that have been closed, or that have reached the maximum number of retries (specified in your subscriptions settings), the next_payment_attempt will be null.

GET/v1/invoices/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "in_1MtHbELkdIwHu7ixl4OzzPMv",  "object": "invoice",  "account_country": "US",  "account_name": "Stripe Docs",  "account_tax_ids": null,  "amount_due": 0,  "amount_paid": 0,  "amount_remaining": 0,  "amount_shipping": 0,  "application": null,  "application_fee_amount": null,  "attempt_count": 0,  "attempted": false,  "auto_advance": false,  "automatic_tax": {    "enabled": false,    "liability": null,    "status": null  },  "billing_reason": "manual",  "charge": null,  "collection_method": "charge_automatically",  "created": 1680644467,  "currency": "usd",  "custom_fields": null,  "customer": "cus_NeZwdNtLEOXuvB",  "customer_address": null,  "customer_email": "jennyrosen@example.com",  "customer_name": "Jenny Rosen",  "customer_phone": null,  "customer_shipping": null,  "customer_tax_exempt": "none",  "customer_tax_ids": [],  "default_payment_method": null,  "default_source": null,  "default_tax_rates": [],  "description": null,  "discount": null,  "discounts": [],  "due_date": null,  "ending_balance": null,  "footer": null,  "from_invoice": null,  "hosted_invoice_url": null,  "invoice_pdf": null,  "issuer": {    "type": "self"  },  "last_finalization_error": null,  "latest_revision": null,  "lines": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"  },  "livemode": false,  "metadata": {},  "next_payment_attempt": null,  "number": null,  "on_behalf_of": null,  "paid": false,  "paid_out_of_band": false,  "payment_intent": null,  "payment_settings": {    "default_mandate": null,    "payment_method_options": null,    "payment_method_types": null  },  "period_end": 1680644467,  "period_start": 1680644467,  "post_payment_credit_notes_amount": 0,  "pre_payment_credit_notes_amount": 0,  "quote": null,  "receipt_number": null,  "rendering_options": null,  "shipping_cost": null,  "shipping_details": null,  "starting_balance": 0,  "statement_descriptor": null,  "status": "draft",  "status_transitions": {    "finalized_at": null,    "marked_uncollectible_at": null,    "paid_at": null,    "voided_at": null  },  "subscription": null,  "subtotal": 0,  "subtotal_excluding_tax": 0,  "tax": null,  "test_clock": null,  "total": 0,  "total_discount_amounts": [],  "total_excluding_tax": 0,  "total_tax_amounts": [],  "transfer_data": null,  "webhooks_delivered_at": 1680644467}`# Retrieve an upcoming invoice

At any time, you can preview the upcoming invoice for a customer. This will show you all the charges that are pending, including subscription renewal charges, invoice item charges, etc. It will also show you any discounts that are applicable to the invoice.

Note that when you are viewing an upcoming invoice, you are simply viewing a preview – the invoice has not yet been created. As such, the upcoming invoice will not show up in invoice listing calls, and you cannot use the API to pay or edit the invoice. If you want to change the amount that your customer will be billed, you can add, remove, or update pending invoice items, or update the customer’s discount.

You can preview the effects of updating a subscription, including a preview of what proration will take place. To ensure that the actual proration is calculated exactly the same as the previewed proration, you should pass the subscription_proration_date parameter when doing the actual subscription update. The recommended way to get only the prorations being previewed is to consider only proration line items where period[start] is equal to the subscription_proration_date value passed in the request.

### Parameters

- customerstringThe identifier of the customer whose upcoming invoice you’d like to retrieve. If automatic_tax is enabled then one of customer, customer_details, subscription, or schedule must be set.


- subscriptionstringThe identifier of the subscription for which you’d like to retrieve the upcoming invoice. If not provided, but a subscription_items is provided, you will preview creating a subscription with those items. If neither subscription nor subscription_items is provided, you will retrieve the next upcoming invoice from among the customer’s subscriptions.



### More parametersExpand all

- automatic_taxobject
- couponstringDeprecated
- currencyenum
- customer_detailsobject
- discountsarray of objects
- invoice_itemsarray of objects
- issuerobjectConnect only
- on_behalf_ofstringConnect only
- schedulestring
- schedule_detailsobject
- subscription_billing_cycle_anchorstring | timestampDeprecated
- subscription_cancel_attimestampDeprecated
- subscription_cancel_at_period_endbooleanDeprecated
- subscription_cancel_nowbooleanDeprecated
- subscription_default_tax_ratesarray of stringsDeprecated
- subscription_detailsobject
- subscription_itemsarray of objectsDeprecated
- subscription_proration_behaviorenumDeprecated
- subscription_proration_datetimestampDeprecated
- subscription_resume_atstringDeprecated
- subscription_start_datetimestampDeprecated
- subscription_trial_endstring | timestampDeprecated

### Returns

Returns an invoice if valid customer information is provided. Raises an error otherwise.

GET/v1/invoices/upcomingServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/invoices/upcoming \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d customer=cus_NeZwdNtLEOXuvB`Response`{  "object": "invoice",  "account_country": "US",  "account_name": "Stripe Docs",  "account_tax_ids": null,  "amount_due": 0,  "amount_paid": 0,  "amount_remaining": 0,  "amount_shipping": 0,  "application": null,  "application_fee_amount": null,  "attempt_count": 0,  "attempted": false,  "auto_advance": false,  "automatic_tax": {    "enabled": false,    "liability": null,    "status": null  },  "billing_reason": "manual",  "charge": null,  "collection_method": "charge_automatically",  "created": 1680644467,  "currency": "usd",  "custom_fields": null,  "customer": "cus_NeZwdNtLEOXuvB",  "customer_address": null,  "customer_email": "jennyrosen@example.com",  "customer_name": "Jenny Rosen",  "customer_phone": null,  "customer_shipping": null,  "customer_tax_exempt": "none",  "customer_tax_ids": [],  "default_payment_method": null,  "default_source": null,  "default_tax_rates": [],  "description": null,  "discount": null,  "discounts": [],  "due_date": null,  "ending_balance": null,  "footer": null,  "from_invoice": null,  "hosted_invoice_url": null,  "invoice_pdf": null,  "issuer": {    "type": "self"  },  "last_finalization_error": null,  "latest_revision": null,  "lines": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"  },  "livemode": false,  "metadata": {},  "next_payment_attempt": null,  "number": null,  "on_behalf_of": null,  "paid": false,  "paid_out_of_band": false,  "payment_intent": null,  "payment_settings": {    "default_mandate": null,    "payment_method_options": null,    "payment_method_types": null  },  "period_end": 1680644467,  "period_start": 1680644467,  "post_payment_credit_notes_amount": 0,  "pre_payment_credit_notes_amount": 0,  "quote": null,  "receipt_number": null,  "rendering_options": null,  "shipping_cost": null,  "shipping_details": null,  "starting_balance": 0,  "statement_descriptor": null,  "status": "draft",  "status_transitions": {    "finalized_at": null,    "marked_uncollectible_at": null,    "paid_at": null,    "voided_at": null  },  "subscription": null,  "subtotal": 0,  "subtotal_excluding_tax": 0,  "tax": null,  "test_clock": null,  "total": 0,  "total_discount_amounts": [],  "total_excluding_tax": 0,  "total_tax_amounts": [],  "transfer_data": null,  "webhooks_delivered_at": 1680644467}`# Retrieve an invoice's line items

When retrieving an invoice, you’ll get a lines property containing the total count of line items and the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

### Parameters

No parameters.

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

Returns a list of line_item objects.

GET/v1/invoices/:id/linesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/invoices/in_1NpHok2eZvKYlo2CyeiBref0/lines \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "object": "list",  "url": "/v1/invoices/in_1NpHiG2eZvKYlo2CZV0ZkEBT/lines",  "has_more": false,  "data": [    {      "id": "il_tmp_1NpHiK2eZvKYlo2C9NdV8VrI",      "object": "line_item",      "amount": 129999,      "amount_excluding_tax": 129999,      "currency": "usd",      "description": "My First Invoice Item (created for API docs)",      "discount_amounts": [],      "discountable": true,      "discounts": [],      "invoice_item": "ii_1NpHiK2eZvKYlo2C9NdV8VrI",      "livemode": false,      "metadata": {},      "period": {        "end": 1694467932,        "start": 1694467932      },      "price": {        "id": "price_1NpEIa2eZvKYlo2CXcy5DRPA",        "object": "price",        "active": true,        "billing_scheme": "per_unit",        "created": 1694454804,        "currency": "usd",        "custom_unit_amount": null,        "livemode": false,        "lookup_key": null,        "metadata": {},        "nickname": null,        "product": "prod_OcTFTbV7qh48bd",        "recurring": null,        "tax_behavior": "unspecified",        "tiers_mode": null,        "transform_quantity": null,        "type": "one_time",        "unit_amount": 129999,        "unit_amount_decimal": "129999"      },      "proration": false,      "proration_details": {        "credited_items": null      },      "quantity": 1,      "subscription": null,      "tax_amounts": [],      "tax_rates": [],      "type": "invoiceitem",      "unit_amount_excluding_tax": "129999"    }  ]}`# Retrieve an upcoming invoice's line items

When retrieving an upcoming invoice, you’ll get a lines property containing the total count of line items and the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

### Parameters

- customerstringThe identifier of the customer whose upcoming invoice you’d like to retrieve. If automatic_tax is enabled then one of customer, customer_details, subscription, or schedule must be set.


- subscriptionstringThe identifier of the subscription for which you’d like to retrieve the upcoming invoice. If not provided, but a subscription_items is provided, you will preview creating a subscription with those items. If neither subscription nor subscription_items is provided, you will retrieve the next upcoming invoice from among the customer’s subscriptions.



### More parametersExpand all

- automatic_taxobject
- couponstringDeprecated
- currencyenum
- customer_detailsobject
- discountsarray of objects
- ending_beforestring
- invoice_itemsarray of objects
- issuerobjectConnect only
- limitinteger
- on_behalf_ofstringConnect only
- schedulestring
- schedule_detailsobject
- starting_afterstring
- subscription_billing_cycle_anchorstring | timestampDeprecated
- subscription_cancel_attimestampDeprecated
- subscription_cancel_at_period_endbooleanDeprecated
- subscription_cancel_nowbooleanDeprecated
- subscription_default_tax_ratesarray of stringsDeprecated
- subscription_detailsobject
- subscription_itemsarray of objectsDeprecated
- subscription_proration_behaviorenumDeprecated
- subscription_proration_datetimestampDeprecated
- subscription_resume_atstringDeprecated
- subscription_start_datetimestampDeprecated
- subscription_trial_endstring | timestampDeprecated

### Returns

Returns a list of line_item objects.

GET/v1/invoices/upcoming/linesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/invoices/upcoming/lines \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d customer=cus_OgeRVYRv3sHroi`Response`{  "object": "list",  "url": "/v1/invoices/upcoming/lines",  "has_more": false,  "data": [    {      "id": "il_tmp_1NtH5qBHO5VeT9SUzhbifVXt",      "object": "line_item",      "amount": 1000,      "amount_excluding_tax": 1000,      "currency": "usd",      "description": "My First Invoice Item (created for API docs)",      "discount_amounts": [],      "discountable": true,      "discounts": [],      "invoice_item": "ii_1NtH5qBHO5VeT9SUzhbifVXt",      "livemode": false,      "metadata": {},      "period": {        "end": 1695418858,        "start": 1695418858      },      "price": {        "id": "price_1NrpbEBHO5VeT9SUHp6xMwKA",        "object": "price",        "active": true,        "billing_scheme": "per_unit",        "created": 1695074844,        "currency": "usd",        "custom_unit_amount": null,        "livemode": false,        "lookup_key": null,        "metadata": {},        "nickname": null,        "product": "prod_Of9vdHHGRaGOio",        "recurring": null,        "tax_behavior": "unspecified",        "tiers_mode": null,        "transform_quantity": null,        "type": "one_time",        "unit_amount": 1000,        "unit_amount_decimal": "1000"      },      "proration": false,      "proration_details": {        "credited_items": null      },      "quantity": 1,      "subscription": null,      "tax_amounts": [],      "tax_rates": [],      "type": "invoiceitem",      "unit_amount_excluding_tax": "1000"    }    {...}    {...}  ],}`# List all invoices

You can list all invoices, or list the invoices for a specific customer. The invoices are returned sorted by creation date, with the most recently created invoices appearing first.

### Parameters

- customerstringOnly return invoices for the customer specified by this customer ID.


- statusenumThe status of the invoice, one of draft, open, paid, uncollectible, or void. Learn more


- subscriptionstringOnly return invoices for the subscription specified by this subscription ID.



### More parametersExpand all

- collection_methodenum
- createdobject
- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array invoice attachments,

GET/v1/invoicesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/invoices \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/invoices",  "has_more": false,  "data": [    {      "id": "in_1MtHbELkdIwHu7ixl4OzzPMv",      "object": "invoice",      "account_country": "US",      "account_name": "Stripe Docs",      "account_tax_ids": null,      "amount_due": 0,      "amount_paid": 0,      "amount_remaining": 0,      "amount_shipping": 0,      "application": null,      "application_fee_amount": null,      "attempt_count": 0,      "attempted": false,      "auto_advance": false,      "automatic_tax": {        "enabled": false,        "liability": null,        "status": null      },      "billing_reason": "manual",      "charge": null,      "collection_method": "charge_automatically",      "created": 1680644467,      "currency": "usd",      "custom_fields": null,      "customer": "cus_NeZwdNtLEOXuvB",      "customer_address": null,      "customer_email": "jennyrosen@example.com",      "customer_name": "Jenny Rosen",      "customer_phone": null,      "customer_shipping": null,      "customer_tax_exempt": "none",      "customer_tax_ids": [],      "default_payment_method": null,      "default_source": null,      "default_tax_rates": [],      "description": null,      "discount": null,      "discounts": [],      "due_date": null,      "ending_balance": null,      "footer": null,      "from_invoice": null,      "hosted_invoice_url": null,      "invoice_pdf": null,      "issuer": {        "type": "self"      },      "last_finalization_error": null,      "latest_revision": null,      "lines": {        "object": "list",        "data": [],        "has_more": false,        "total_count": 0,        "url": "/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"      },      "livemode": false,      "metadata": {},      "next_payment_attempt": null,      "number": null,      "on_behalf_of": null,      "paid": false,      "paid_out_of_band": false,      "payment_intent": null,      "payment_settings": {        "default_mandate": null,        "payment_method_options": null,        "payment_method_types": null      },      "period_end": 1680644467,      "period_start": 1680644467,      "post_payment_credit_notes_amount": 0,      "pre_payment_credit_notes_amount": 0,      "quote": null,      "receipt_number": null,      "rendering_options": null,      "shipping_cost": null,      "shipping_details": null,      "starting_balance": 0,      "statement_descriptor": null,      "status": "draft",      "status_transitions": {        "finalized_at": null,        "marked_uncollectible_at": null,        "paid_at": null,        "voided_at": null      },      "subscription": null,      "subtotal": 0,      "subtotal_excluding_tax": 0,      "tax": null,      "test_clock": null,      "total": 0,      "total_discount_amounts": [],      "total_excluding_tax": 0,      "total_tax_amounts": [],      "transfer_data": null,      "webhooks_delivered_at": 1680644467    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`