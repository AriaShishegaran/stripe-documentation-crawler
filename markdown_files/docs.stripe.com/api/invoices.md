htmlInvoices | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Invoices

Invoices are statements of amounts owed by a customer, and are either generated one-off, or generated periodically from a subscription.

They contain invoice items, and proration adjustments that may be caused by subscription upgrades/downgrades (if necessary).

If your invoice is configured to be billed through automatic charges, Stripe automatically finalizes your invoice and attempts payment.  Note that finalizing the invoice, when automatic, does not happen immediately as the invoice is created. Stripe waits until one hour after the last webhook was successfully sent (or the last webhook timed out after failing). If you (and the platforms you may have connected to) have no webhooks configured, Stripe waits one hour after creation to finalize the invoice.

If your invoice is configured to be billed by sending an email, then based on your email settings, Stripe will email the invoice to your customer and await payment. These emails can contain a link to a hosted page to pay the invoice.

Stripe applies any customer credit on the account before determining the amount due for the invoice (i.e., the amount that will be actually charged). If the amount due for the invoice is less than Stripe’s minimum allowed charge per currency, the invoice is automatically marked paid, and we add the amount due to the customer’s credit balance which is applied to the next invoice.

More details on the customer’s credit balance are here.

Related guide: Send invoices to customers

Endpoints
# The Invoice object

### Attributes

- idstringUnique identifier for the object. This property is always present unless the invoice is an upcoming invoice. See Retrieve an upcoming invoice for more details.


- auto_advancebooleanControls whether Stripe performs automatic collection of the invoice. If false, the invoice’s state doesn’t automatically advance without an explicit action.


- chargenullablestringExpandableID of the latest charge generated for this invoice, if any.


- collection_methodenumEither charge_automatically, or send_invoice. When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions.

Possible enum values`charge_automatically`Attempt payment using the default source attached to the customer.

`send_invoice`Email payment instructions to the customer.


- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- customerstringExpandableThe ID of the customer who will be billed.


- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users. Referenced as ‘memo’ in the Dashboard.


- hosted_invoice_urlnullablestringThe URL for the hosted invoice page, which allows customers to view and pay an invoice. If the invoice has not been finalized yet, this will be null.


- linesobjectThe individual line items that make up the invoice. lines is sorted as follows: (1) pending invoice items (including prorations) in reverse chronological order, (2) subscription items in reverse chronological order, and (3) invoice items added after invoice creation in chronological order.

Show child attributes
- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- payment_intentnullablestringExpandableThe PaymentIntent associated with this invoice. The PaymentIntent is generated when the invoice is finalized, and can then be used to pay the invoice. Note that voiding an invoice will cancel the PaymentIntent.


- period_endtimestampEnd of the usage period during which invoice items were added to this invoice.


- period_starttimestampStart of the usage period during which invoice items were added to this invoice.


- statusnullableenumThe status of the invoice, one of draft, open, paid, uncollectible, or void. Learn more


- subscriptionnullablestringExpandableThe subscription that this invoice was prepared for, if any.


- totalintegerTotal after discounts and taxes.



### More attributesExpand all

- objectstring
- account_countrynullablestring
- account_namenullablestring
- account_tax_idsnullablearray of stringsExpandable
- amount_dueinteger
- amount_paidinteger
- amount_remaininginteger
- amount_shippinginteger
- applicationnullablestringExpandableConnect only
- application_fee_amountnullableintegerConnect only
- attempt_countinteger
- attemptedboolean
- automatic_taxobject
- billing_reasonnullableenum
- createdtimestamp
- custom_fieldsnullablearray of objects
- customer_addressnullableobject
- customer_emailnullablestring
- customer_namenullablestring
- customer_phonenullablestring
- customer_shippingnullableobject
- customer_tax_exemptnullableenum
- customer_tax_idsnullablearray of objects
- default_payment_methodnullablestringExpandable
- default_sourcenullablestringExpandable
- default_tax_ratesarray of objects
- discountnullableobjectDeprecated
- discountsarray of stringsExpandable
- due_datenullabletimestamp
- effective_atnullabletimestamp
- ending_balancenullableinteger
- footernullablestring
- from_invoicenullableobject
- invoice_pdfnullablestring
- issuerobjectConnect only
- last_finalization_errornullableobject
- latest_revisionnullablestringExpandable
- livemodeboolean
- next_payment_attemptnullabletimestamp
- numbernullablestring
- on_behalf_ofnullablestringExpandableConnect only
- paidboolean
- paid_out_of_bandboolean
- payment_settingsobject
- post_payment_credit_notes_amountinteger
- pre_payment_credit_notes_amountinteger
- quotenullablestringExpandable
- receipt_numbernullablestring
- renderingnullableobject
- shipping_costnullableobject
- shipping_detailsnullableobject
- starting_balanceinteger
- statement_descriptornullablestring
- status_transitionsobject
- subscription_detailsnullableobject
- subscription_proration_datenullableinteger
- subtotalinteger
- subtotal_excluding_taxnullableinteger
- taxnullableinteger
- test_clocknullablestringExpandable
- threshold_reasonnullableobject
- total_discount_amountsnullablearray of objects
- total_excluding_taxnullableinteger
- total_tax_amountsarray of objects
- transfer_datanullableobjectConnect only
- webhooks_delivered_atnullabletimestamp

The Invoice object`{  "id": "in_1MtHbELkdIwHu7ixl4OzzPMv",  "object": "invoice",  "account_country": "US",  "account_name": "Stripe Docs",  "account_tax_ids": null,  "amount_due": 0,  "amount_paid": 0,  "amount_remaining": 0,  "amount_shipping": 0,  "application": null,  "application_fee_amount": null,  "attempt_count": 0,  "attempted": false,  "auto_advance": false,  "automatic_tax": {    "enabled": false,    "liability": null,    "status": null  },  "billing_reason": "manual",  "charge": null,  "collection_method": "charge_automatically",  "created": 1680644467,  "currency": "usd",  "custom_fields": null,  "customer": "cus_NeZwdNtLEOXuvB",  "customer_address": null,  "customer_email": "jennyrosen@example.com",  "customer_name": "Jenny Rosen",  "customer_phone": null,  "customer_shipping": null,  "customer_tax_exempt": "none",  "customer_tax_ids": [],  "default_payment_method": null,  "default_source": null,  "default_tax_rates": [],  "description": null,  "discount": null,  "discounts": [],  "due_date": null,  "ending_balance": null,  "footer": null,  "from_invoice": null,  "hosted_invoice_url": null,  "invoice_pdf": null,  "issuer": {    "type": "self"  },  "last_finalization_error": null,  "latest_revision": null,  "lines": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"  },  "livemode": false,  "metadata": {},  "next_payment_attempt": null,  "number": null,  "on_behalf_of": null,  "paid": false,  "paid_out_of_band": false,  "payment_intent": null,  "payment_settings": {    "default_mandate": null,    "payment_method_options": null,    "payment_method_types": null  },  "period_end": 1680644467,  "period_start": 1680644467,  "post_payment_credit_notes_amount": 0,  "pre_payment_credit_notes_amount": 0,  "quote": null,  "receipt_number": null,  "rendering_options": null,  "shipping_cost": null,  "shipping_details": null,  "starting_balance": 0,  "statement_descriptor": null,  "status": "draft",  "status_transitions": {    "finalized_at": null,    "marked_uncollectible_at": null,    "paid_at": null,    "voided_at": null  },  "subscription": null,  "subtotal": 0,  "subtotal_excluding_tax": 0,  "tax": null,  "test_clock": null,  "total": 0,  "total_discount_amounts": [],  "total_excluding_tax": 0,  "total_tax_amounts": [],  "transfer_data": null,  "webhooks_delivered_at": 1680644467}`# The Invoice Line Item object

### Attributes

- idstringUnique identifier for the object.


- amountintegerThe amount, in cents.


- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users.


- invoicenullablestringThe ID of the invoice that contains this line item.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Note that for line items with type=subscription, metadata reflects the current metadata from the subscription associated with the line item, unless the invoice line was directly updated with different metadata after creation.


- periodobjectThe period this line_item covers. For subscription line items, this is the subscription period. For prorations, this starts when the proration was calculated, and ends at the period end of the subscription. For invoice items, this is the time at which the invoice item was created or the period of the item. If you have Stripe Revenue Recognition enabled, the period will be used to recognize and defer revenue. See the Revenue Recognition documentation for details.

Show child attributes
- pricenullableobjectThe price of the line item.

Show child attributes
- prorationbooleanWhether this is a proration.


- quantitynullableintegerThe quantity of the subscription, if the line item is a subscription or a proration.


- typeenumA string identifying the type of the source of this line item, either an invoiceitem or a subscription.

Possible enum values`invoiceitem``subscription`

### More attributesExpand all

- objectstring
- amount_excluding_taxnullableinteger
- discount_amountsnullablearray of objects
- discountableboolean
- discountsarray of stringsExpandable
- invoice_itemnullablestringExpandable
- livemodeboolean
- proration_detailsnullableobject
- subscriptionnullablestringExpandable
- subscription_itemnullablestringExpandable
- tax_amountsarray of objects
- tax_ratesarray of objects
- unit_amount_excluding_taxnullabledecimal string

The Invoice Line Item object`{  "id": "il_tmp_1Nzo1ZGgdF1VjufLzD1UUn9R",  "object": "line_item",  "amount": 1000,  "amount_excluding_tax": 1000,  "currency": "usd",  "description": "My First Invoice Item (created for API docs)",  "discount_amounts": [],  "discountable": true,  "discounts": [],  "invoice_item": "ii_1Nzo1ZGgdF1VjufLzD1UUn9R",  "livemode": false,  "metadata": {},  "period": {    "end": 1696975413,    "start": 1696975413  },  "price": {    "id": "price_1NzlYfGgdF1VjufL0cVjLJVI",    "object": "price",    "active": true,    "billing_scheme": "per_unit",    "created": 1696965933,    "currency": "usd",    "custom_unit_amount": null,    "livemode": false,    "lookup_key": null,    "metadata": {},    "nickname": null,    "product": "prod_OnMHDH6VBmYlTr",    "recurring": null,    "tax_behavior": "unspecified",    "tiers_mode": null,    "transform_quantity": null,    "type": "one_time",    "unit_amount": 1000,    "unit_amount_decimal": "1000"  },  "proration": false,  "proration_details": {    "credited_items": null  },  "quantity": 1,  "subscription": null,  "tax_amounts": [],  "tax_rates": [],  "type": "invoiceitem",  "unit_amount_excluding_tax": "1000"}`# Create an invoice

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

POST/v1/invoices/create_previewServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/invoices/create_preview \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d customer=cus_NeZwdNtLEOXuvB`Response`{  "id": "upcoming_in_1MtHbELkdIwHu7ixl4OzzPMv",  "object": "invoice",  "account_country": "US",  "account_name": "Stripe Docs",  "account_tax_ids": null,  "amount_due": 0,  "amount_paid": 0,  "amount_remaining": 0,  "amount_shipping": 0,  "application": null,  "application_fee_amount": null,  "attempt_count": 0,  "attempted": false,  "auto_advance": false,  "automatic_tax": {    "enabled": false,    "status": null  },  "billing_reason": "manual",  "charge": null,  "collection_method": "charge_automatically",  "created": 1680644467,  "currency": "usd",  "custom_fields": null,  "customer": "cus_NeZwdNtLEOXuvB",  "customer_address": null,  "customer_email": "jennyrosen@example.com",  "customer_name": "Jenny Rosen",  "customer_phone": null,  "customer_shipping": null,  "customer_tax_exempt": "none",  "customer_tax_ids": [],  "default_payment_method": null,  "default_source": null,  "default_tax_rates": [],  "description": null,  "discount": null,  "discounts": [],  "due_date": null,  "ending_balance": null,  "footer": null,  "from_invoice": null,  "hosted_invoice_url": null,  "invoice_pdf": null,  "last_finalization_error": null,  "latest_revision": null,  "lines": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/invoices/in_1MtHbELkdIwHu7ixl4OzzPMv/lines"  },  "livemode": false,  "metadata": {},  "next_payment_attempt": null,  "number": null,  "on_behalf_of": null,  "paid": false,  "paid_out_of_band": false,  "payment_intent": null,  "payment_settings": {    "default_mandate": null,    "payment_method_options": null,    "payment_method_types": null  },  "period_end": 1680644467,  "period_start": 1680644467,  "post_payment_credit_notes_amount": 0,  "pre_payment_credit_notes_amount": 0,  "quote": null,  "receipt_number": null,  "rendering_options": null,  "shipping_cost": null,  "shipping_details": null,  "starting_balance": 0,  "statement_descriptor": null,  "status": "draft",  "status_transitions": {    "finalized_at": null,    "marked_uncollectible_at": null,    "paid_at": null,    "voided_at": null  },  "subscription": null,  "subtotal": 0,  "subtotal_excluding_tax": 0,  "tax": null,  "test_clock": null,  "total": 0,  "total_discount_amounts": [],  "total_excluding_tax": 0,  "total_tax_amounts": [],  "transfer_data": null,  "webhooks_delivered_at": 1680644467}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`