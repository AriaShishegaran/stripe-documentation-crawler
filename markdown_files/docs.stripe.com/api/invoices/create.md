htmlCreate an invoice | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Create an invoice

This endpoint creates a draft invoice for a given customer. The invoice remains a draft until you finalize the invoice, which allows you to pay or send the invoice to your customers.

### Parameters

- auto_advancebooleanControls whether Stripe performs automatic collection of the invoice. If false, the invoice’s state doesn’t automatically advance without an explicit action.


- collection_methodenumEither charge_automatically, or send_invoice. When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions. Defaults to charge_automatically.

Possible enum values`charge_automatically``send_invoice`
- customerstringThe ID of the customer who will be billed.


- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users. Referenced as ‘memo’ in the Dashboard.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- subscriptionstringThe ID of the subscription to invoice, if any. If set, the created invoice will only include pending invoice items for that subscription. The subscription’s billing cycle and regular subscription events won’t be affected.



### More parametersExpand all

- account_tax_idsarray of strings
- application_fee_amountintegerConnect only
- automatic_taxobject
- currencyenum
- custom_fieldsarray of objects
- days_until_dueinteger
- default_payment_methodstring
- default_sourcestring
- default_tax_ratesarray of strings
- discountsarray of objects
- due_datetimestamp
- effective_attimestamp
- footerstring
- from_invoiceobject
- issuerobjectConnect only
- numberstring
- on_behalf_ofstringConnect only
- payment_settingsobject
- pending_invoice_items_behaviorenum
- renderingobject
- shipping_costobject
- shipping_detailsobject
- statement_descriptorstring
- transfer_dataobjectConnect only

### Returns

Returns the invoice object. Raises an error if the customer ID provided is invalid.

POST/v1/invoicesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/invoices \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d customer=cus_NeZwdNtLEOXuvB`Response`{  "id": "in_1MtHbELkdIwHu7ixl4OzzPMv",  "object": "invoice",  "account_country": "US",  "account_name": "Stripe Docs",  "account_tax_ids": null,  "amount_due": 0,  "amount_paid": 0,  "amount_remaining": 0,  "amount_shipping": 0,  "application": null,  "application_fee_amount": null,  "attempt_count": 0,  "attempted": false,  "auto_advance": false,  "automatic_tax": {    "enabled": false,    "liability": null,    "status": null  },  "billing_reason": "manual",  "charge": null,  "collection_method": "charge_automatically",  "created": 1680644467,  "currency": "usd",  "custom_fields": null,  "customer": "cus_NeZwdNtLEOXuvB",  "customer_address": null,  "customer_email": "jennyrosen@example.com",  "customer_name": "Jenny Rosen",  "customer_phone": null,  "customer_shipping": null,  "customer_tax_exempt": "none",  "customer_tax_ids": [],  "default_payment_method": null,  "default_source": null,  "default_tax_rates": [],  "description": null,  "discount": null,  "discounts": [],  "due_date": null,  "ending_balance": null,  "footer": null,  "from_invoice": null,  "hosted_invoice_url": null,  "invoice_pdf": null,  "issuer": {    "type": "self"  },  "last_finalization_error": null,  "latest_revision": null,  "lines": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"  },  "livemode": false,  "metadata": {},  "next_payment_attempt": null,  "number": null,  "on_behalf_of": null,  "paid": false,  "paid_out_of_band": false,  "payment_intent": null,  "payment_settings": {    "default_mandate": null,    "payment_method_options": null,    "payment_method_types": null  },  "period_end": 1680644467,  "period_start": 1680644467,  "post_payment_credit_notes_amount": 0,  "pre_payment_credit_notes_amount": 0,  "quote": null,  "receipt_number": null,  "rendering_options": null,  "shipping_cost": null,  "shipping_details": null,  "starting_balance": 0,  "statement_descriptor": null,  "status": "draft",  "status_transitions": {    "finalized_at": null,    "marked_uncollectible_at": null,    "paid_at": null,    "voided_at": null  },  "subscription": null,  "subtotal": 0,  "subtotal_excluding_tax": 0,  "tax": null,  "test_clock": null,  "total": 0,  "total_discount_amounts": [],  "total_excluding_tax": 0,  "total_tax_amounts": [],  "transfer_data": null,  "webhooks_delivered_at": 1680644467}`# Create a preview invoice

At any time, you can preview the upcoming invoice for a customer. This will show you all the charges that are pending, including subscription renewal charges, invoice item charges, etc. It will also show you any discounts that are applicable to the invoice.

Note that when you are viewing an upcoming invoice, you are simply viewing a preview – the invoice has not yet been created. As such, the upcoming invoice will not show up in invoice listing calls, and you cannot use the API to pay or edit the invoice. If you want to change the amount that your customer will be billed, you can add, remove, or update pending invoice items, or update the customer’s discount.

You can preview the effects of updating a subscription, including a preview of what proration will take place. To ensure that the actual proration is calculated exactly the same as the previewed proration, you should pass the subscription_details.proration_date parameter when doing the actual subscription update. The recommended way to get only the prorations being previewed is to consider only proration line items where period[start] is equal to the subscription_details.proration_date value passed in the request.

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
- subscription_detailsobject

### Returns

Returns an invoice if valid customer information is provided. Raises an error otherwise.

POST/v1/invoices/create_previewServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/invoices/create_preview \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d customer=cus_NeZwdNtLEOXuvB`Response`{  "id": "upcoming_in_1MtHbELkdIwHu7ixl4OzzPMv",  "object": "invoice",  "account_country": "US",  "account_name": "Stripe Docs",  "account_tax_ids": null,  "amount_due": 0,  "amount_paid": 0,  "amount_remaining": 0,  "amount_shipping": 0,  "application": null,  "application_fee_amount": null,  "attempt_count": 0,  "attempted": false,  "auto_advance": false,  "automatic_tax": {    "enabled": false,    "status": null  },  "billing_reason": "manual",  "charge": null,  "collection_method": "charge_automatically",  "created": 1680644467,  "currency": "usd",  "custom_fields": null,  "customer": "cus_NeZwdNtLEOXuvB",  "customer_address": null,  "customer_email": "jennyrosen@example.com",  "customer_name": "Jenny Rosen",  "customer_phone": null,  "customer_shipping": null,  "customer_tax_exempt": "none",  "customer_tax_ids": [],  "default_payment_method": null,  "default_source": null,  "default_tax_rates": [],  "description": null,  "discount": null,  "discounts": [],  "due_date": null,  "ending_balance": null,  "footer": null,  "from_invoice": null,  "hosted_invoice_url": null,  "invoice_pdf": null,  "last_finalization_error": null,  "latest_revision": null,  "lines": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"  },  "livemode": false,  "metadata": {},  "next_payment_attempt": null,  "number": null,  "on_behalf_of": null,  "paid": false,  "paid_out_of_band": false,  "payment_intent": null,  "payment_settings": {    "default_mandate": null,    "payment_method_options": null,    "payment_method_types": null  },  "period_end": 1680644467,  "period_start": 1680644467,  "post_payment_credit_notes_amount": 0,  "pre_payment_credit_notes_amount": 0,  "quote": null,  "receipt_number": null,  "rendering_options": null,  "shipping_cost": null,  "shipping_details": null,  "starting_balance": 0,  "statement_descriptor": null,  "status": "draft",  "status_transitions": {    "finalized_at": null,    "marked_uncollectible_at": null,    "paid_at": null,    "voided_at": null  },  "subscription": null,  "subtotal": 0,  "subtotal_excluding_tax": 0,  "tax": null,  "test_clock": null,  "total": 0,  "total_discount_amounts": [],  "total_excluding_tax": 0,  "total_tax_amounts": [],  "transfer_data": null,  "webhooks_delivered_at": 1680644467}`# Update an invoice

Draft invoices are fully editable. Once an invoice is finalized, monetary values, as well as collection_method, become uneditable.

If you would like to stop the Stripe Billing engine from automatically finalizing, reattempting payments on, sending reminders for, or automatically reconciling invoices, pass auto_advance=false.

### Parameters

- auto_advancebooleanControls whether Stripe performs automatic collection of the invoice.


- collection_methodenumEither charge_automatically or send_invoice. This field can be updated only on draft invoices.

Possible enum values`charge_automatically``send_invoice`
- descriptionstringAn arbitrary string attached to the object. Often useful for displaying to users. Referenced as ‘memo’ in the Dashboard.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- account_tax_idsarray of strings
- application_fee_amountintegerConnect only
- automatic_taxobject
- custom_fieldsarray of objects
- days_until_dueinteger
- default_payment_methodstring
- default_sourcestring
- default_tax_ratesarray of strings
- discountsarray of objects
- due_datetimestamp
- effective_attimestamp
- footerstring
- issuerobjectConnect only
- numberstring
- on_behalf_ofstringConnect only
- payment_settingsobject
- renderingobject
- shipping_costobject
- shipping_detailsobject
- statement_descriptorstring
- transfer_dataobjectConnect only

### Returns

Returns the invoice object.

POST/v1/invoices/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "in_1MtHbELkdIwHu7ixl4OzzPMv",  "object": "invoice",  "account_country": "US",  "account_name": "Stripe Docs",  "account_tax_ids": null,  "amount_due": 0,  "amount_paid": 0,  "amount_remaining": 0,  "amount_shipping": 0,  "application": null,  "application_fee_amount": null,  "attempt_count": 0,  "attempted": false,  "auto_advance": false,  "automatic_tax": {    "enabled": false,    "liability": null,    "status": null  },  "billing_reason": "manual",  "charge": null,  "collection_method": "charge_automatically",  "created": 1680644467,  "currency": "usd",  "custom_fields": null,  "customer": "cus_NeZwdNtLEOXuvB",  "customer_address": null,  "customer_email": "jennyrosen@example.com",  "customer_name": "Jenny Rosen",  "customer_phone": null,  "customer_shipping": null,  "customer_tax_exempt": "none",  "customer_tax_ids": [],  "default_payment_method": null,  "default_source": null,  "default_tax_rates": [],  "description": null,  "discount": null,  "discounts": [],  "due_date": null,  "ending_balance": null,  "footer": null,  "from_invoice": null,  "hosted_invoice_url": null,  "invoice_pdf": null,  "issuer": {    "type": "self"  },  "last_finalization_error": null,  "latest_revision": null,  "lines": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"  },  "livemode": false,  "metadata": {    "order_id": "6735"  },  "next_payment_attempt": null,  "number": null,  "on_behalf_of": null,  "paid": false,  "paid_out_of_band": false,  "payment_intent": null,  "payment_settings": {    "default_mandate": null,    "payment_method_options": null,    "payment_method_types": null  },  "period_end": 1680644467,  "period_start": 1680644467,  "post_payment_credit_notes_amount": 0,  "pre_payment_credit_notes_amount": 0,  "quote": null,  "receipt_number": null,  "rendering_options": null,  "shipping_cost": null,  "shipping_details": null,  "starting_balance": 0,  "statement_descriptor": null,  "status": "draft",  "status_transitions": {    "finalized_at": null,    "marked_uncollectible_at": null,    "paid_at": null,    "voided_at": null  },  "subscription": null,  "subtotal": 0,  "subtotal_excluding_tax": 0,  "tax": null,  "test_clock": null,  "total": 0,  "total_discount_amounts": [],  "total_excluding_tax": 0,  "total_tax_amounts": [],  "transfer_data": null,  "webhooks_delivered_at": 1680644467}`# Update an invoice's line item

Updates an invoice’s line item. Some fields, such as tax_amounts, only live on the invoice line item, so they can only be updated through this endpoint. Other fields, such as amount, live on both the invoice item and the invoice line item, so updates on this endpoint will propagate to the invoice item as well. Updating an invoice’s line item is only possible before the invoice is finalized.

### Parameters

- invoicestringRequiredInvoice ID of line item


- line_item_idstringRequiredInvoice line item ID


- amountintegerThe integer amount in cents of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer’s account, pass a negative amount.


- descriptionstringAn arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata. For type=recurring line items, the incoming metadata specified on the request is directly used to set this value, in contrast to type=invoiceitem line items, where any existing metadata on the invoice line is merged with the incoming data.


- periodobjectThe period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have Stripe Revenue Recognition enabled, the period will be used to recognize and defer revenue. See the Revenue Recognition documentation for details.

Show child parameters
- pricestringThe ID of the price object.


- quantityintegerNon-negative integer. The quantity of units for the line item.



### More parametersExpand all

- discountableboolean
- discountsarray of objects
- price_dataobject
- tax_amountsarray of objects
- tax_ratesarray of strings

### Returns

The updated invoice’s line item object is returned upon success. Otherwise, this call raises an error.

POST/v1/invoices/:id/lines/:idcURL[](#)[](#)`curl -X POST https://api.stripe.com/v1/invoices/in_1NuhUa2eZvKYlo2CWYVhyvD9/lines/il_tmp_1Nzo1ZGgdF1VjufLzD1UUn9R \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "il_tmp_1Nzo1ZGgdF1VjufLzD1UUn9R",  "object": "line_item",  "amount": 1000,  "amount_excluding_tax": 1000,  "currency": "usd",  "description": "My First Invoice Item (created for API docs)",  "discount_amounts": [],  "discountable": true,  "discounts": [],  "invoice_item": "ii_1Nzo1ZGgdF1VjufLzD1UUn9R",  "livemode": false,  "metadata": {},  "period": {    "end": 1696975413,    "start": 1696975413  },  "price": {    "id": "price_1NzlYfGgdF1VjufL0cVjLJVI",    "object": "price",    "active": true,    "billing_scheme": "per_unit",    "created": 1696965933,    "currency": "usd",    "custom_unit_amount": null,    "livemode": false,    "lookup_key": null,    "metadata": {},    "nickname": null,    "product": "prod_OnMHDH6VBmYlTr",    "recurring": null,    "tax_behavior": "unspecified",    "tiers_mode": null,    "transform_quantity": null,    "type": "one_time",    "unit_amount": 1000,    "unit_amount_decimal": "1000"  },  "proration": false,  "proration_details": {    "credited_items": null  },  "quantity": 1,  "subscription": null,  "tax_amounts": [],  "tax_rates": [],  "type": "invoiceitem",  "unit_amount_excluding_tax": "1000"}`# Retrieve an invoice

Retrieves the invoice with the given ID.

### Parameters

No parameters.

### Returns

Returns an invoice object if a valid invoice ID was provided. Raises an error otherwise.

The invoice object contains a lines hash that contains information about the subscriptions and invoice items that have been applied to the invoice, as well as any prorations that Stripe has automatically calculated. Each line on the invoice has an amount attribute that represents the amount actually contributed to the invoice’s total. For invoice items and prorations, the amount attribute is the same as for the invoice item or proration respectively. For subscriptions, the amount may be different from the plan’s regular price depending on whether the invoice covers a trial period or the invoice period differs from the plan’s usual interval.

The invoice object has both a subtotal and a total. The subtotal represents the total before any discounts, while the total is the final amount to be charged to the customer after all coupons have been applied.

The invoice also has a next_payment_attempt attribute that tells you the next time (as a Unix timestamp) payment for the invoice will be automatically attempted. For invoices with manual payment collection, that have been closed, or that have reached the maximum number of retries (specified in your subscriptions settings), the next_payment_attempt will be null.

GET/v1/invoices/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "in_1MtHbELkdIwHu7ixl4OzzPMv",  "object": "invoice",  "account_country": "US",  "account_name": "Stripe Docs",  "account_tax_ids": null,  "amount_due": 0,  "amount_paid": 0,  "amount_remaining": 0,  "amount_shipping": 0,  "application": null,  "application_fee_amount": null,  "attempt_count": 0,  "attempted": false,  "auto_advance": false,  "automatic_tax": {    "enabled": false,    "liability": null,    "status": null  },  "billing_reason": "manual",  "charge": null,  "collection_method": "charge_automatically",  "created": 1680644467,  "currency": "usd",  "custom_fields": null,  "customer": "cus_NeZwdNtLEOXuvB",  "customer_address": null,  "customer_email": "jennyrosen@example.com",  "customer_name": "Jenny Rosen",  "customer_phone": null,  "customer_shipping": null,  "customer_tax_exempt": "none",  "customer_tax_ids": [],  "default_payment_method": null,  "default_source": null,  "default_tax_rates": [],  "description": null,  "discount": null,  "discounts": [],  "due_date": null,  "ending_balance": null,  "footer": null,  "from_invoice": null,  "hosted_invoice_url": null,  "invoice_pdf": null,  "issuer": {    "type": "self"  },  "last_finalization_error": null,  "latest_revision": null,  "lines": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"  },  "livemode": false,  "metadata": {},  "next_payment_attempt": null,  "number": null,  "on_behalf_of": null,  "paid": false,  "paid_out_of_band": false,  "payment_intent": null,  "payment_settings": {    "default_mandate": null,    "payment_method_options": null,    "payment_method_types": null  },  "period_end": 1680644467,  "period_start": 1680644467,  "post_payment_credit_notes_amount": 0,  "pre_payment_credit_notes_amount": 0,  "quote": null,  "receipt_number": null,  "rendering_options": null,  "shipping_cost": null,  "shipping_details": null,  "starting_balance": 0,  "statement_descriptor": null,  "status": "draft",  "status_transitions": {    "finalized_at": null,    "marked_uncollectible_at": null,    "paid_at": null,    "voided_at": null  },  "subscription": null,  "subtotal": 0,  "subtotal_excluding_tax": 0,  "tax": null,  "test_clock": null,  "total": 0,  "total_discount_amounts": [],  "total_excluding_tax": 0,  "total_tax_amounts": [],  "transfer_data": null,  "webhooks_delivered_at": 1680644467}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`