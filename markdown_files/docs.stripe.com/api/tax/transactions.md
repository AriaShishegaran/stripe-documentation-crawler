htmlTax Transactions | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Tax Transactions

A Tax Transaction records the tax collected from or refunded to your customer.

Related guide: Calculate tax in your custom payment flow

Endpoints
# The Tax Transaction object

### Attributes

- idstringUnique identifier for the transaction.


- objectstringString representing the object’s type. Objects of the same type share the same value.


- currencystringThree-letter ISO currency code, in lowercase. Must be a supported currency.


- customer_detailsobjectThe customer’s details, such as address and tax IDs.

Show child attributes
- line_itemsnullableobjectExpandableThe tax collected or refunded, by line item.

Show child attributes
- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- referencestringA custom unique identifier, such as ‘myOrder_123’.


- typeenumIf reversal, this transaction reverses an earlier transaction.

Possible enum values`reversal`Represents a partial or full reversal of an earlier transaction.

`transaction`Represents a customer sale or order.



### More attributesExpand all

- createdtimestamp
- customernullablestring
- livemodeboolean
- reversalnullableobject
- shipping_costnullableobject
- tax_datetimestamp

The Tax Transaction object`{  "id": "tax_1NaS0I2eZvKYlo2CRuMhUcmz",  "object": "tax.transaction",  "created": 1690932566,  "currency": "usd",  "customer": null,  "customer_details": {    "address": {      "city": "South San Francisco",      "country": "US",      "line1": "354 Oyster Point Blvd",      "line2": "",      "postal_code": "94080",      "state": "CA"    },    "address_source": "shipping",    "ip_address": null,    "tax_ids": [],    "taxability_override": "none"  },  "line_items": {    "object": "list",    "data": [      {        "id": "tax_li_ONCP443tgfS8I1",        "object": "tax.transaction_line_item",        "amount": 1499,        "amount_tax": 148,        "livemode": false,        "metadata": null,        "product": null,        "quantity": 1,        "reference": "Pepperoni Pizza",        "reversal": null,        "tax_behavior": "exclusive",        "tax_code": "txcd_40060003",        "type": "transaction"      }    ],    "has_more": false,    "url": "/v1/tax/transactions/tax_1NaS0I2eZvKYlo2CRuMhUcmz/line_items"  },  "livemode": false,  "metadata": null,  "reference": "myOrder_123",  "reversal": null,  "shipping_cost": {    "amount": 300,    "amount_tax": 0,    "tax_behavior": "exclusive",    "tax_code": "txcd_92010001"  },  "ship_from_details": {    "address": {      "postal_code": "75001",      "state": "TX",      "country": "US"    }  },  "tax_date": 1690932566,  "type": "transaction"}`# Create a reversal transaction

Partially or fully reverses a previously created Transaction.

### Parameters

- modeenumRequiredIf partial, the provided line item or shipping cost amounts are reversed. If full, the original transaction is fully reversed.

Possible enum values`full`The original transaction is fully reversed.

`partial`The provided line item amounts are reversed.


- original_transactionstringRequiredThe ID of the Transaction to partially or fully reverse.


- referencestringRequiredA custom identifier for this reversal, such as myOrder_123-refund_1, which must be unique across all transactions. The reference helps identify this reversal transaction in exported tax reports.


- flat_amountintegerRequired if mode=partial and line_items nor shipping_cost providedA flat amount to reverse across the entire transaction, in the smallest currency unit in negative. This value represents the total amount to refund from the transaction, including taxes.


- line_itemsarray of objectsRequired if mode=partial and neither shipping_cost nor flat_amount is providedThe line item amounts to reverse.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- shipping_costobjectRequired if mode=partial and neither line_items nor flat_amount is provided

### Returns

A new Tax Transaction object representing the reversal.

POST/v1/tax/transactions/create_reversalServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tax/transactions/create_reversal \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d mode=partial \  -d original_transaction=tax_1NaTVd2eZvKYlo2CoOX2Nf7P \  -d reference=myOrder_123-refund_1 \  -d "line_items[0][amount]"=-1499 \  -d "line_items[0][amount_tax]"=-148 \  -d "line_items[0][original_line_item]"=tax_li_ONDxh8JZw14sP8 \  -d "line_items[0][reference]"="refund of Pepperoni Pizza" \  -d "expand[0]"=line_items`Response`{  "id": "tax_1NaTVd2eZvKYlo2CoOX2Nf7P",  "object": "tax.transaction",  "created": 1690938353,  "currency": "usd",  "customer": null,  "customer_details": {    "address": {      "city": null,      "country": "US",      "line1": "354 Oyster Point Blvd",      "line2": "",      "postal_code": "94080",      "state": "CA"    },    "address_source": "shipping",    "ip_address": null,    "tax_ids": [],    "taxability_override": "none"  },  "line_items": {    "object": "list",    "data": [      {        "id": "tax_li_ONDxh8JZw14sP8",        "object": "tax.transaction_line_item",        "amount": 1499,        "amount_tax": 148,        "livemode": false,        "metadata": null,        "product": null,        "quantity": 1,        "reference": "Pepperoni Pizza",        "reversal": null,        "tax_behavior": "exclusive",        "tax_code": "txcd_40060003",        "type": "transaction"      }    ],    "has_more": false,    "url": "/v1/tax/transactions/tax_1NaTVd2eZvKYlo2CoOX2Nf7P/line_items"  },  "livemode": false,  "metadata": null,  "reference": "myOrder_123",  "reversal": null,  "shipping_cost": {    "amount": 300,    "amount_tax": 0,    "tax_behavior": "exclusive",    "tax_code": "txcd_92010001"  },  "tax_date": 1690938353,  "type": "transaction"}`# Create a transaction from a calculation

Creates a Tax Transaction from a calculation.

### Parameters

- calculationstringRequiredTax Calculation ID to be used as input when creating the transaction.


- referencestringRequiredA custom order or sale identifier, such as ‘myOrder_123’. Must be unique across all transactions, including reversals.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

A Tax Transaction object.

POST/v1/tax/transactions/create_from_calculationServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tax/transactions/create_from_calculation \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d calculation=taxcalc_1NaTVT2eZvKYlo2CsqGeLeU2 \  -d reference=myOrder_123 \  -d "expand[]"=line_items`Response`{  "id": "tax_1NaTVd2eZvKYlo2CoOX2Nf7P",  "object": "tax.transaction",  "created": 1690938353,  "currency": "usd",  "customer": null,  "customer_details": {    "address": {      "city": null,      "country": "US",      "line1": "354 Oyster Point Blvd",      "line2": "",      "postal_code": "94080",      "state": "CA"    },    "address_source": "shipping",    "ip_address": null,    "tax_ids": [],    "taxability_override": "none"  },  "line_items": {    "object": "list",    "data": [      {        "id": "tax_li_ONDxh8JZw14sP8",        "object": "tax.transaction_line_item",        "amount": 1499,        "amount_tax": 148,        "livemode": false,        "metadata": null,        "product": null,        "quantity": 1,        "reference": "Pepperoni Pizza",        "reversal": null,        "tax_behavior": "exclusive",        "tax_code": "txcd_40060003",        "type": "transaction"      }    ],    "has_more": false,    "url": "/v1/tax/transactions/tax_1NaTVd2eZvKYlo2CoOX2Nf7P/line_items"  },  "livemode": false,  "metadata": null,  "reference": "myOrder_123",  "reversal": null,  "shipping_cost": {    "amount": 300,    "amount_tax": 0,    "tax_behavior": "exclusive",    "tax_code": "txcd_92010001"  },  "tax_date": 1690938353,  "type": "transaction"}`# Retrieve a transaction's line items

Retrieves the line items of a committed standalone transaction as a collection.

### Parameters

- ending_beforestringA cursor for use in pagination. ending_before is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_bar, your subsequent call can include ending_before=obj_bar in order to fetch the previous page of the list.


- limitintegerA limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.


- starting_afterstringA cursor for use in pagination. starting_after is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include starting_after=obj_foo in order to fetch the next page of the list.



### Returns

A list of Line Item objects if the Tax Transaction is found. Otherwise returns a ‘not found’ error.

GET/v1/tax/transactions/:id/line_itemsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tax/transactions/tax_1NaTVd2eZvKYlo2CoOX2Nf7P/line_items \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "tax_1NaTVd2eZvKYlo2CoOX2Nf7P",  "object": "list",  "url": "/v1/tax/transactions/tax_1NaTVd2eZvKYlo2CoOX2Nf7P/line_items",  "has_more": false,  "data": [    {      "id": "tax_li_ONDxh8JZw14sP8",      "object": "tax.transaction_line_item",      "amount": 1499,      "amount_tax": 148,      "livemode": false,      "metadata": null,      "product": null,      "quantity": 1,      "reference": "Pepperoni Pizza",      "reversal": null,      "tax_behavior": "exclusive",      "tax_code": "txcd_40060003",      "type": "transaction"    }  ]}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`