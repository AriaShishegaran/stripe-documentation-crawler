htmlRetrieve an upcoming invoice's line items | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Retrieve an upcoming invoice's line items

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

GET/v1/invoicesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/invoices \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/invoices",  "has_more": false,  "data": [    {      "id": "in_1MtHbELkdIwHu7ixl4OzzPMv",      "object": "invoice",      "account_country": "US",      "account_name": "Stripe Docs",      "account_tax_ids": null,      "amount_due": 0,      "amount_paid": 0,      "amount_remaining": 0,      "amount_shipping": 0,      "application": null,      "application_fee_amount": null,      "attempt_count": 0,      "attempted": false,      "auto_advance": false,      "automatic_tax": {        "enabled": false,        "liability": null,        "status": null      },      "billing_reason": "manual",      "charge": null,      "collection_method": "charge_automatically",      "created": 1680644467,      "currency": "usd",      "custom_fields": null,      "customer": "cus_NeZwdNtLEOXuvB",      "customer_address": null,      "customer_email": "jennyrosen@example.com",      "customer_name": "Jenny Rosen",      "customer_phone": null,      "customer_shipping": null,      "customer_tax_exempt": "none",      "customer_tax_ids": [],      "default_payment_method": null,      "default_source": null,      "default_tax_rates": [],      "description": null,      "discount": null,      "discounts": [],      "due_date": null,      "ending_balance": null,      "footer": null,      "from_invoice": null,      "hosted_invoice_url": null,      "invoice_pdf": null,      "issuer": {        "type": "self"      },      "last_finalization_error": null,      "latest_revision": null,      "lines": {        "object": "list",        "data": [],        "has_more": false,        "total_count": 0,        "url": "/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"      },      "livemode": false,      "metadata": {},      "next_payment_attempt": null,      "number": null,      "on_behalf_of": null,      "paid": false,      "paid_out_of_band": false,      "payment_intent": null,      "payment_settings": {        "default_mandate": null,        "payment_method_options": null,        "payment_method_types": null      },      "period_end": 1680644467,      "period_start": 1680644467,      "post_payment_credit_notes_amount": 0,      "pre_payment_credit_notes_amount": 0,      "quote": null,      "receipt_number": null,      "rendering_options": null,      "shipping_cost": null,      "shipping_details": null,      "starting_balance": 0,      "statement_descriptor": null,      "status": "draft",      "status_transitions": {        "finalized_at": null,        "marked_uncollectible_at": null,        "paid_at": null,        "voided_at": null      },      "subscription": null,      "subtotal": 0,      "subtotal_excluding_tax": 0,      "tax": null,      "test_clock": null,      "total": 0,      "total_discount_amounts": [],      "total_excluding_tax": 0,      "total_tax_amounts": [],      "transfer_data": null,      "webhooks_delivered_at": 1680644467    }    {...}    {...}  ],}`# Delete a draft invoice

Permanently deletes a one-off invoice draft. This cannot be undone. Attempts to delete invoices that are no longer in a draft state will fail; once an invoice has been finalized or if an invoice is for a subscription, it must be voided.

### Parameters

No parameters.

### Returns

A successfully deleted invoice. Otherwise, this call raises an error, such as if the invoice has already been deleted.

DELETE/v1/invoices/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X DELETE https://api.stripe.com/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "in_1MtHbELkdIwHu7ixl4OzzPMv",  "object": "invoice",  "deleted": true}`# Finalize an invoice

Stripe automatically finalizes drafts before sending and attempting payment on invoices. However, if you’d like to finalize a draft invoice manually, you can do so using this method.

### Parameters

- auto_advancebooleanControls whether Stripe performs automatic collection of the invoice. If false, the invoice’s state doesn’t automatically advance without an explicit action.



### Returns

Returns an invoice object with status=open.

POST/v1/invoices/:id/finalizeServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/invoices/in_1MtGmCLkdIwHu7ix6PgS6g8S/finalize \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "in_1MtGmCLkdIwHu7ix6PgS6g8S",  "object": "invoice",  "account_country": "US",  "account_name": "Stripe Docs",  "account_tax_ids": null,  "amount_due": 0,  "amount_paid": 0,  "amount_remaining": 0,  "amount_shipping": 0,  "application": null,  "application_fee_amount": null,  "attempt_count": 0,  "attempted": true,  "auto_advance": false,  "automatic_tax": {    "enabled": false,    "liability": null,    "status": null  },  "billing_reason": "manual",  "charge": null,  "collection_method": "send_invoice",  "created": 1680641304,  "currency": "usd",  "custom_fields": null,  "customer": "cus_NeZw0zvTyquTfF",  "customer_address": null,  "customer_email": "jennyrosen@example.com",  "customer_name": "Jenny Rosen",  "customer_phone": null,  "customer_shipping": null,  "customer_tax_exempt": "none",  "customer_tax_ids": [],  "default_payment_method": null,  "default_source": null,  "default_tax_rates": [],  "description": null,  "discount": null,  "discounts": [],  "due_date": 1681246104,  "ending_balance": 0,  "footer": null,  "from_invoice": null,  "hosted_invoice_url": "https://invoice.stripe.com/i/acct_1M2JTkLkdIwHu7ix/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9OZVp3dVBYNnF0dGlvdXRubGVjSXVOOWhiVWpmUktPLDcxMTgyMTA10200x7P2wMSm?s=ap",  "invoice_pdf": "https://pay.stripe.com/invoice/acct_1M2JTkLkdIwHu7ix/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9OZVp3dVBYNnF0dGlvdXRubGVjSXVOOWhiVWpmUktPLDcxMTgyMTA10200x7P2wMSm/pdf?s=ap",  "issuer": {    "type": "self"  },  "last_finalization_error": null,  "latest_revision": null,  "lines": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/invoices/in_1MtGmCLkdIwHu7ix6PgS6g8S/lines"  },  "livemode": false,  "metadata": {},  "next_payment_attempt": null,  "number": "9545A614-0001",  "on_behalf_of": null,  "paid": true,  "paid_out_of_band": false,  "payment_intent": null,  "payment_settings": {    "default_mandate": null,    "payment_method_options": null,    "payment_method_types": null  },  "period_end": 1680641304,  "period_start": 1680641304,  "post_payment_credit_notes_amount": 0,  "pre_payment_credit_notes_amount": 0,  "quote": null,  "receipt_number": null,  "rendering_options": null,  "shipping_cost": null,  "shipping_details": null,  "starting_balance": 0,  "statement_descriptor": null,  "status": "paid",  "status_transitions": {    "finalized_at": 1680641304,    "marked_uncollectible_at": null,    "paid_at": 1680641304,    "voided_at": null  },  "subscription": null,  "subtotal": 0,  "subtotal_excluding_tax": 0,  "tax": null,  "test_clock": null,  "total": 0,  "total_discount_amounts": [],  "total_excluding_tax": 0,  "total_tax_amounts": [],  "transfer_data": null,  "webhooks_delivered_at": 1680641304}`# Mark an invoice as uncollectible

Marking an invoice as uncollectible is useful for keeping track of bad debts that can be written off for accounting purposes.

### Parameters

No parameters.

### Returns

Returns the invoice object.

POST/v1/invoices/:id/mark_uncollectibleServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/invoices/in_1MtG0nLkdIwHu7ixAaUw3Cb4/mark_uncollectible \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "in_1MtG0nLkdIwHu7ixAaUw3Cb4",  "object": "invoice",  "account_country": "US",  "account_name": "Stripe Docs",  "account_tax_ids": null,  "amount_due": 599,  "amount_paid": 0,  "amount_remaining": 599,  "amount_shipping": 0,  "application": null,  "application_fee_amount": null,  "attempt_count": 0,  "attempted": false,  "auto_advance": false,  "automatic_tax": {    "enabled": false,    "liability": null,    "status": null  },  "billing_reason": "manual",  "charge": null,  "collection_method": "charge_automatically",  "created": 1680638365,  "currency": "usd",  "custom_fields": null,  "customer": "cus_NeZw0zvTyquTfF",  "customer_address": null,  "customer_email": "jennyrosen@example.com",  "customer_name": "Jenny Rosen",  "customer_phone": null,  "customer_shipping": null,  "customer_tax_exempt": "none",  "customer_tax_ids": [    {      "type": "eu_vat",      "value": "DE123456789"    },    {      "type": "eu_vat",      "value": "DE123456781"    }  ],  "default_payment_method": null,  "default_source": null,  "default_tax_rates": [],  "description": null,  "discount": null,  "discounts": [],  "due_date": null,  "ending_balance": null,  "footer": null,  "from_invoice": null,  "hosted_invoice_url": null,  "invoice_pdf": null,  "issuer": {    "type": "self"  },  "last_finalization_error": null,  "latest_revision": null,  "lines": {    "object": "list",    "data": [      {        "id": "il_1MtG0nLkdIwHu7ix3eCoIIw7",        "object": "line_item",        "amount": 1099,        "amount_excluding_tax": 1099,        "currency": "usd",        "description": "My First Invoice Item (created for API docs)",        "discount_amounts": [],        "discountable": true,        "discounts": [],        "invoice_item": "ii_1MtG0nLkdIwHu7ixDqfiUgg8",        "livemode": false,        "metadata": {},        "period": {          "end": 1680638365,          "start": 1680638365        },        "price": {          "id": "price_1Mr89PLkdIwHu7ixf5QhiWm2",          "object": "price",          "active": true,          "billing_scheme": "per_unit",          "created": 1680131491,          "currency": "usd",          "custom_unit_amount": null,          "livemode": false,          "lookup_key": null,          "metadata": {},          "nickname": null,          "product": "prod_NcMtLgctyqlJDC",          "recurring": null,          "tax_behavior": "unspecified",          "tiers_mode": null,          "transform_quantity": null,          "type": "one_time",          "unit_amount": 1099,          "unit_amount_decimal": "1099"        },        "proration": false,        "proration_details": {          "credited_items": null        },        "quantity": 1,        "subscription": null,        "tax_amounts": [],        "tax_rates": [],        "type": "invoiceitem",        "unit_amount_excluding_tax": "1099"      }    ],    "has_more": false,    "url": "/v1/invoices/in_1MtG0nLkdIwHu7ixAaUw3Cb4/lines"  },  "livemode": false,  "metadata": {},  "next_payment_attempt": null,  "number": null,  "on_behalf_of": null,  "paid": false,  "paid_out_of_band": false,  "payment_intent": null,  "payment_settings": {    "default_mandate": null,    "payment_method_options": null,    "payment_method_types": null  },  "period_end": 1680638365,  "period_start": 1680638365,  "post_payment_credit_notes_amount": 0,  "pre_payment_credit_notes_amount": 0,  "quote": null,  "receipt_number": null,  "rendering_options": null,  "shipping_cost": null,  "shipping_details": null,  "starting_balance": -500,  "statement_descriptor": null,  "status": "uncollectible",  "status_transitions": {    "finalized_at": null,    "marked_uncollectible_at": null,    "paid_at": null,    "voided_at": null  },  "subscription": null,  "subtotal": 1099,  "subtotal_excluding_tax": 1099,  "tax": null,  "test_clock": null,  "total": 1099,  "total_discount_amounts": [],  "total_excluding_tax": 1099,  "total_tax_amounts": [],  "transfer_data": null,  "webhooks_delivered_at": null,  "closed": true,  "forgiven": true}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`