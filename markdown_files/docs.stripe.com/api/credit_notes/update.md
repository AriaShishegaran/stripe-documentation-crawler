htmlUpdate a credit note | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Update a credit note

Updates an existing credit note.

### Parameters

- memostringCredit note memo.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns the updated credit note object if the call succeeded.

POST/v1/credit_notes/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/credit_notes/cn_1MxvRqLkdIwHu7ixY0xbUcxk \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "cn_1MxvRqLkdIwHu7ixY0xbUcxk",  "object": "credit_note",  "amount": 1099,  "amount_shipping": 0,  "created": 1681750958,  "currency": "usd",  "customer": "cus_NjLgPhUokHubJC",  "customer_balance_transaction": null,  "discount_amount": 0,  "discount_amounts": [],  "invoice": "in_1MxvRkLkdIwHu7ixABNtI99m",  "lines": {    "object": "list",    "data": [      {        "id": "cnli_1MxvRqLkdIwHu7ixFpdhBFQf",        "object": "credit_note_line_item",        "amount": 1099,        "amount_excluding_tax": 1099,        "description": "T-shirt",        "discount_amount": 0,        "discount_amounts": [],        "invoice_line_item": "il_1MxvRlLkdIwHu7ixnkbntxUV",        "livemode": false,        "quantity": 1,        "tax_amounts": [],        "tax_rates": [],        "type": "invoice_line_item",        "unit_amount": 1099,        "unit_amount_decimal": "1099",        "unit_amount_excluding_tax": "1099"      }    ],    "has_more": false,    "url": "/v1/credit_notes/cn_1MxvRqLkdIwHu7ixY0xbUcxk/lines"  },  "livemode": false,  "memo": null,  "metadata": {    "order_id": "6735"  },  "number": "C9E0C52C-0036-CN-01",  "out_of_band_amount": null,  "pdf": "https://pay.stripe.com/credit_notes/acct_1M2JTkLkdIwHu7ix/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9Oak9FOUtQNFlPdk52UXhFd2Z4SU45alpEd21kd0Y4LDcyMjkxNzU50200cROQsSK2/pdf?s=ap",  "reason": null,  "refund": null,  "shipping_cost": null,  "status": "issued",  "subtotal": 1099,  "subtotal_excluding_tax": 1099,  "tax_amounts": [],  "total": 1099,  "total_excluding_tax": 1099,  "type": "pre_payment",  "voided_at": null}`# Retrieve a credit note's line items

When retrieving a credit note, you’ll get a lines property containing the the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

### Parameters

No parameters.

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

Returns a list of line_item objects.

GET/v1/credit_notes/:id/linesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/credit_notes/cn_1NPtPy2eZvKYlo2CPaEMGMY8/lines \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/credit_notes/cn_1NPtPy2eZvKYlo2CPaEMGMY8/lines",  "has_more": false,  "data": [    {      "object": "list",      "url": "/v1/credit_notes/cn_1Nn7fB2eZvKYlo2CuJ0wZBlA/lines",      "has_more": false,      "data": [        {          "id": "cnli_1Nn7fB2eZvKYlo2COYgPG88j",          "object": "credit_note_line_item",          "amount": 799,          "amount_excluding_tax": 799,          "description": "My First Invoice Item (created for API docs)",          "discount_amount": 0,          "discount_amounts": [],          "invoice_line_item": "il_1Nn7fB2eZvKYlo2C3GKZP9wi",          "livemode": false,          "quantity": 1,          "tax_amounts": [],          "tax_rates": [],          "type": "invoice_line_item",          "unit_amount": null,          "unit_amount_decimal": null,          "unit_amount_excluding_tax": "799"        }      ]    }    {...}    {...}  ],}`# Retrieve a credit note preview's line items

When retrieving a credit note preview, you’ll get a lines property containing the first handful of those items. This URL you can retrieve the full (paginated) list of line items.

### Parameters

- invoicestringRequiredID of the invoice.


- linesarray of objectsLine items that make up the credit note.

Show child parameters
- memostringThe credit note’s memo appears on the credit note PDF.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- reasonenumReason for issuing this credit note, one of duplicate, fraudulent, order_change, or product_unsatisfactory

Possible enum values`duplicate``fraudulent``order_change``product_unsatisfactory`

### More parametersExpand all

- amountinteger
- credit_amountinteger
- effective_attimestamp
- ending_beforestring
- limitinteger
- out_of_band_amountinteger
- refundstring
- refund_amountinteger
- shipping_costobject
- starting_afterstring

### Returns

Returns a list of line_item objects.

GET/v1/credit_notes/preview/linesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/credit_notes/preview/lines \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d invoice=in_1Nn8592eZvKYlo2Ci4yFC46f`Response`{  "id": "cn_1Nn7fB2eZvKYlo2CuJ0wZBlA",  "object": "credit_note",  "amount": 1451,  "amount_shipping": 0,  "created": 1693952641,  "currency": "usd",  "customer": "cus_9s6XKzkNRiz8i3",  "customer_balance_transaction": null,  "discount_amount": 0,  "discount_amounts": [],  "effective_at": null,  "invoice": "in_1Nn7fB2eZvKYlo2C7meA67Xp",  "lines": {    "object": "list",    "data": [      {        "id": "cnli_1Nn7fB2eZvKYlo2Cp8nLMci9",        "object": "credit_note_line_item",        "amount": 951,        "amount_excluding_tax": 951,        "description": "My First Invoice Item (created for API docs)",        "discount_amount": 0,        "discount_amounts": [],        "invoice_line_item": "il_1Nn7fB2eZvKYlo2ChKG2H1tv",        "livemode": false,        "quantity": 1,        "tax_amounts": [          {            "amount": 152,            "inclusive": false,            "tax_rate": "txr_1Nn7fB2eZvKYlo2CcbF7zzmD",            "taxability_reason": null,            "taxable_amount": 799          }        ],        "tax_rates": [          {            "id": "txr_1Nn7fB2eZvKYlo2CcbF7zzmD",            "object": "tax_rate",            "active": true,            "country": "DE",            "created": 1693952641,            "description": "VAT Germany",            "display_name": "VAT",            "effective_percentage": null,            "inclusive": false,            "jurisdiction": "DE",            "livemode": false,            "metadata": {},            "percentage": 19,            "state": null,            "tax_type": "vat"          }        ],        "type": "invoice_line_item",        "unit_amount": null,        "unit_amount_decimal": null,        "unit_amount_excluding_tax": "951"      },      {        "id": "cnli_1Nn7fB2eZvKYlo2C7OxQLHdz",        "object": "credit_note_line_item",        "amount": 500,        "amount_excluding_tax": 500,        "description": "Service credit",        "discount_amount": 0,        "discount_amounts": [],        "livemode": false,        "quantity": 1,        "tax_amounts": [],        "tax_rates": [],        "type": "custom_line_item",        "unit_amount": 500,        "unit_amount_decimal": "500",        "unit_amount_excluding_tax": "500"      }    ],    "has_more": false,    "url": "/v1/credit_notes/cn_1Nn7fB2eZvKYlo2CuJ0wZBlA/lines"  },  "livemode": false,  "memo": null,  "metadata": {},  "number": "ABCD-1234-CN-01",  "out_of_band_amount": null,  "pdf": "https://pay.stripe.com/credit_notes/acct_1032D82eZvKYlo2C/cnst_123456789/pdf?s=ap",  "reason": null,  "refund": null,  "shipping_cost": null,  "status": "issued",  "subtotal": 1451,  "subtotal_excluding_tax": 1451,  "tax_amounts": [    {      "amount": 152,      "inclusive": false,      "tax_rate": "txr_1Nn7fB2eZvKYlo2CcbF7zzmD",      "taxability_reason": null,      "taxable_amount": 799    }  ],  "total": 1451,  "total_excluding_tax": null,  "type": "pre_payment",  "voided_at": null}`# Retrieve a credit note

Retrieves the credit note object with the given identifier.

### Parameters

No parameters.

### Returns

Returns a credit note object if a valid identifier was provided.

GET/v1/credit_notes/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/credit_notes/cn_1MxvRqLkdIwHu7ixY0xbUcxk \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "cn_1MxvRqLkdIwHu7ixY0xbUcxk",  "object": "credit_note",  "amount": 1099,  "amount_shipping": 0,  "created": 1681750958,  "currency": "usd",  "customer": "cus_NjLgPhUokHubJC",  "customer_balance_transaction": null,  "discount_amount": 0,  "discount_amounts": [],  "invoice": "in_1MxvRkLkdIwHu7ixABNtI99m",  "lines": {    "object": "list",    "data": [      {        "id": "cnli_1MxvRqLkdIwHu7ixFpdhBFQf",        "object": "credit_note_line_item",        "amount": 1099,        "amount_excluding_tax": 1099,        "description": "T-shirt",        "discount_amount": 0,        "discount_amounts": [],        "invoice_line_item": "il_1MxvRlLkdIwHu7ixnkbntxUV",        "livemode": false,        "quantity": 1,        "tax_amounts": [],        "tax_rates": [],        "type": "invoice_line_item",        "unit_amount": 1099,        "unit_amount_decimal": "1099",        "unit_amount_excluding_tax": "1099"      }    ],    "has_more": false,    "url": "/v1/credit_notes/cn_1MxvRqLkdIwHu7ixY0xbUcxk/lines"  },  "livemode": false,  "memo": null,  "metadata": {},  "number": "C9E0C52C-0036-CN-01",  "out_of_band_amount": null,  "pdf": "https://pay.stripe.com/credit_notes/acct_1M2JTkLkdIwHu7ix/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9Oak9FOUtQNFlPdk52UXhFd2Z4SU45alpEd21kd0Y4LDcyMjkxNzU50200cROQsSK2/pdf?s=ap",  "reason": null,  "refund": null,  "shipping_cost": null,  "status": "issued",  "subtotal": 1099,  "subtotal_excluding_tax": 1099,  "tax_amounts": [],  "total": 1099,  "total_excluding_tax": 1099,  "type": "pre_payment",  "voided_at": null}`# List all credit notes

Returns a list of credit notes.

### Parameters

- invoicestringOnly return credit notes for the invoice specified by this invoice ID.



### More parametersExpand all

- createdobject
- customerstring
- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit credit notes, starting after credit note starting_after. Each entry in the array is a separate credit note object. If no more credit notes are available, the resulting array will be empty.

GET/v1/credit_notesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/credit_notes \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/credit_notes",  "has_more": false,  "data": [    {      "id": "cn_1MxvRqLkdIwHu7ixY0xbUcxk",      "object": "credit_note",      "amount": 1099,      "amount_shipping": 0,      "created": 1681750958,      "currency": "usd",      "customer": "cus_NjLgPhUokHubJC",      "customer_balance_transaction": null,      "discount_amount": 0,      "discount_amounts": [],      "invoice": "in_1MxvRkLkdIwHu7ixABNtI99m",      "lines": {        "object": "list",        "data": [          {            "id": "cnli_1MxvRqLkdIwHu7ixFpdhBFQf",            "object": "credit_note_line_item",            "amount": 1099,            "amount_excluding_tax": 1099,            "description": "T-shirt",            "discount_amount": 0,            "discount_amounts": [],            "invoice_line_item": "il_1MxvRlLkdIwHu7ixnkbntxUV",            "livemode": false,            "quantity": 1,            "tax_amounts": [],            "tax_rates": [],            "type": "invoice_line_item",            "unit_amount": 1099,            "unit_amount_decimal": "1099",            "unit_amount_excluding_tax": "1099"          }        ],        "has_more": false,        "url": "/v1/credit_notes/cn_1MxvRqLkdIwHu7ixY0xbUcxk/lines"      },      "livemode": false,      "memo": null,      "metadata": {},      "number": "C9E0C52C-0036-CN-01",      "out_of_band_amount": null,      "pdf": "https://pay.stripe.com/credit_notes/acct_1M2JTkLkdIwHu7ix/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9Oak9FOUtQNFlPdk52UXhFd2Z4SU45alpEd21kd0Y4LDcyMjkxNzU50200cROQsSK2/pdf?s=ap",      "reason": null,      "refund": null,      "shipping_cost": null,      "status": "issued",      "subtotal": 1099,      "subtotal_excluding_tax": 1099,      "tax_amounts": [],      "total": 1099,      "total_excluding_tax": 1099,      "type": "pre_payment",      "voided_at": null    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`