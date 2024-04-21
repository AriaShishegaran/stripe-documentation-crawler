htmlCreate an invoice item | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Create an invoice item

Creates an item to be added to a draft invoice (up to 250 items per invoice). If no invoice is specified, the item will be on the next invoice created for the customer specified.

### Parameters

- customerstringRequiredThe ID of the customer who will be billed when this invoice item is billed.


- amountintegerThe integer amount in cents of the charge to be applied to the upcoming invoice. Passing in a negative amount will reduce the amount_due on the invoice.


- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- descriptionstringAn arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- periodobjectThe period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have Stripe Revenue Recognition enabled, the period will be used to recognize and defer revenue. See the Revenue Recognition documentation for details.

Show child parameters
- pricestringThe ID of the price object.



### More parametersExpand all

- discountableboolean
- discountsarray of objects
- invoicestring
- price_dataobject
- quantityinteger
- subscriptionstring
- tax_behaviorenum
- tax_codestring
- tax_ratesarray of strings
- unit_amountinteger
- unit_amount_decimalstring

### Returns

The created invoice item object is returned if successful. Otherwise, this call raises an error.

POST/v1/invoiceitemsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/invoiceitems \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d customer=cus_NeZei8imSbMVvi \  -d price=price_1MtGUsLkdIwHu7ix1be5Ljaj`Response`{  "id": "ii_1MtGUtLkdIwHu7ixBYwjAM00",  "object": "invoiceitem",  "amount": 1099,  "currency": "usd",  "customer": "cus_NeZei8imSbMVvi",  "date": 1680640231,  "description": "T-shirt",  "discountable": true,  "discounts": [],  "invoice": null,  "livemode": false,  "metadata": {},  "period": {    "end": 1680640231,    "start": 1680640231  },  "plan": null,  "price": {    "id": "price_1MtGUsLkdIwHu7ix1be5Ljaj",    "object": "price",    "active": true,    "billing_scheme": "per_unit",    "created": 1680640229,    "currency": "usd",    "custom_unit_amount": null,    "livemode": false,    "lookup_key": null,    "metadata": {},    "nickname": null,    "product": "prod_NeZe7xbBdJT8EN",    "recurring": null,    "tax_behavior": "unspecified",    "tiers_mode": null,    "transform_quantity": null,    "type": "one_time",    "unit_amount": 1099,    "unit_amount_decimal": "1099"  },  "proration": false,  "quantity": 1,  "subscription": null,  "tax_rates": [],  "test_clock": null,  "unit_amount": 1099,  "unit_amount_decimal": "1099"}`# Update an invoice item

Updates the amount or description of an invoice item on an upcoming invoice. Updating an invoice item is only possible before the invoice it’s attached to is closed.

### Parameters

- amountintegerThe integer amount in cents of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer’s account, pass a negative amount.


- descriptionstringAn arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- periodobjectThe period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have Stripe Revenue Recognition enabled, the period will be used to recognize and defer revenue. See the Revenue Recognition documentation for details.

Show child parameters
- pricestringThe ID of the price object.



### More parametersExpand all

- discountableboolean
- discountsarray of objects
- price_dataobject
- quantityinteger
- tax_behaviorenum
- tax_codestring
- tax_ratesarray of strings
- unit_amountinteger
- unit_amount_decimalstring

### Returns

The updated invoice item object is returned upon success. Otherwise, this call raises an error.

POST/v1/invoiceitems/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/invoiceitems/ii_1MtGUtLkdIwHu7ixBYwjAM00 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "ii_1MtGUtLkdIwHu7ixBYwjAM00",  "object": "invoiceitem",  "amount": 1099,  "currency": "usd",  "customer": "cus_NeZei8imSbMVvi",  "date": 1680640231,  "description": "T-shirt",  "discountable": true,  "discounts": [],  "invoice": null,  "livemode": false,  "metadata": {    "order_id": "6735"  },  "period": {    "end": 1680640231,    "start": 1680640231  },  "plan": null,  "price": {    "id": "price_1MtGUsLkdIwHu7ix1be5Ljaj",    "object": "price",    "active": true,    "billing_scheme": "per_unit",    "created": 1680640229,    "currency": "usd",    "custom_unit_amount": null,    "livemode": false,    "lookup_key": null,    "metadata": {},    "nickname": null,    "product": "prod_NeZe7xbBdJT8EN",    "recurring": null,    "tax_behavior": "unspecified",    "tiers_mode": null,    "transform_quantity": null,    "type": "one_time",    "unit_amount": 1099,    "unit_amount_decimal": "1099"  },  "proration": false,  "quantity": 1,  "subscription": null,  "tax_rates": [],  "test_clock": null,  "unit_amount": 1099,  "unit_amount_decimal": "1099"}`# Retrieve an invoice item

Retrieves the invoice item with the given ID.

### Parameters

No parameters.

### Returns

Returns an invoice item if a valid invoice item ID was provided. Raises an error otherwise.

GET/v1/invoiceitems/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/invoiceitems/ii_1MtGUtLkdIwHu7ixBYwjAM00 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "ii_1MtGUtLkdIwHu7ixBYwjAM00",  "object": "invoiceitem",  "amount": 1099,  "currency": "usd",  "customer": "cus_NeZei8imSbMVvi",  "date": 1680640231,  "description": "T-shirt",  "discountable": true,  "discounts": [],  "invoice": null,  "livemode": false,  "metadata": {},  "period": {    "end": 1680640231,    "start": 1680640231  },  "plan": null,  "price": {    "id": "price_1MtGUsLkdIwHu7ix1be5Ljaj",    "object": "price",    "active": true,    "billing_scheme": "per_unit",    "created": 1680640229,    "currency": "usd",    "custom_unit_amount": null,    "livemode": false,    "lookup_key": null,    "metadata": {},    "nickname": null,    "product": "prod_NeZe7xbBdJT8EN",    "recurring": null,    "tax_behavior": "unspecified",    "tiers_mode": null,    "transform_quantity": null,    "type": "one_time",    "unit_amount": 1099,    "unit_amount_decimal": "1099"  },  "proration": false,  "quantity": 1,  "subscription": null,  "tax_rates": [],  "test_clock": null,  "unit_amount": 1099,  "unit_amount_decimal": "1099"}`# List all invoice items

Returns a list of your invoice items. Invoice items are returned sorted by creation date, with the most recently created invoice items appearing first.

### Parameters

- customerstringThe identifier of the customer whose invoice items to return. If none is provided, all invoice items will be returned.



### More parametersExpand all

- createdobject
- ending_beforestring
- invoicestring
- limitinteger
- pendingboolean
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit invoice items, starting after invoice item starting_after. Each entry in the array is a separate invoice item object. If no more invoice items are available, the resulting array will be empty.

GET/v1/invoiceitemsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/invoiceitems \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/invoiceitems",  "has_more": false,  "data": [    {      "id": "ii_1MtGUtLkdIwHu7ixBYwjAM00",      "object": "invoiceitem",      "amount": 1099,      "currency": "usd",      "customer": "cus_NeZei8imSbMVvi",      "date": 1680640231,      "description": "T-shirt",      "discountable": true,      "discounts": [],      "invoice": null,      "livemode": false,      "metadata": {},      "period": {        "end": 1680640231,        "start": 1680640231      },      "plan": null,      "price": {        "id": "price_1MtGUsLkdIwHu7ix1be5Ljaj",        "object": "price",        "active": true,        "billing_scheme": "per_unit",        "created": 1680640229,        "currency": "usd",        "custom_unit_amount": null,        "livemode": false,        "lookup_key": null,        "metadata": {},        "nickname": null,        "product": "prod_NeZe7xbBdJT8EN",        "recurring": null,        "tax_behavior": "unspecified",        "tiers_mode": null,        "transform_quantity": null,        "type": "one_time",        "unit_amount": 1099,        "unit_amount_decimal": "1099"      },      "proration": false,      "quantity": 1,      "subscription": null,      "tax_rates": [],      "test_clock": null,      "unit_amount": 1099,      "unit_amount_decimal": "1099"    }    {...}    {...}  ],}`# Delete an invoice item

Deletes an invoice item, removing it from an invoice. Deleting invoice items is only possible when they’re not attached to invoices, or if it’s attached to a draft invoice.

### Parameters

No parameters.

### Returns

An object with the deleted invoice item’s ID and a deleted flag upon success. Otherwise, this call raises an error, such as if the invoice item has already been deleted.

DELETE/v1/invoiceitems/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X DELETE https://api.stripe.com/v1/invoiceitems/ii_1MtGUtLkdIwHu7ixBYwjAM00 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "ii_1MtGUtLkdIwHu7ixBYwjAM00",  "object": "invoiceitem",  "deleted": true}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`