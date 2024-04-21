htmlCreate a reversal transaction | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Create a reversal transaction

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

GET/v1/tax/transactions/:id/line_itemsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tax/transactions/tax_1NaTVd2eZvKYlo2CoOX2Nf7P/line_items \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "tax_1NaTVd2eZvKYlo2CoOX2Nf7P",  "object": "list",  "url": "/v1/tax/transactions/tax_1NaTVd2eZvKYlo2CoOX2Nf7P/line_items",  "has_more": false,  "data": [    {      "id": "tax_li_ONDxh8JZw14sP8",      "object": "tax.transaction_line_item",      "amount": 1499,      "amount_tax": 148,      "livemode": false,      "metadata": null,      "product": null,      "quantity": 1,      "reference": "Pepperoni Pizza",      "reversal": null,      "tax_behavior": "exclusive",      "tax_code": "txcd_40060003",      "type": "transaction"    }  ]}`# Retrieve a transaction

Retrieves a Tax Transaction object.

### Parameters

No parameters.

### Returns

A Tax Transaction object.

GET/v1/tax/transactions/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tax/transactions/tax_1NaS0I2eZvKYlo2CRuMhUcmz \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "tax_1NaS0I2eZvKYlo2CRuMhUcmz",  "object": "tax.transaction",  "created": 1690932566,  "currency": "usd",  "customer": null,  "customer_details": {    "address": {      "city": "South San Francisco",      "country": "US",      "line1": "354 Oyster Point Blvd",      "line2": "",      "postal_code": "94080",      "state": "CA"    },    "address_source": "shipping",    "ip_address": null,    "tax_ids": [],    "taxability_override": "none"  },  "line_items": {    "object": "list",    "data": [      {        "id": "tax_li_ONCP443tgfS8I1",        "object": "tax.transaction_line_item",        "amount": 1499,        "amount_tax": 148,        "livemode": false,        "metadata": null,        "product": null,        "quantity": 1,        "reference": "Pepperoni Pizza",        "reversal": null,        "tax_behavior": "exclusive",        "tax_code": "txcd_40060003",        "type": "transaction"      }    ],    "has_more": false,    "url": "/v1/tax/transactions/tax_1NaS0I2eZvKYlo2CRuMhUcmz/line_items"  },  "livemode": false,  "metadata": null,  "reference": "myOrder_123",  "reversal": null,  "shipping_cost": {    "amount": 300,    "amount_tax": 0,    "tax_behavior": "exclusive",    "tax_code": "txcd_92010001"  },  "ship_from_details": {    "address": {      "postal_code": "75001",      "state": "TX",      "country": "US"    }  },  "tax_date": 1690932566,  "type": "transaction"}`# Tax Settings

You can use Tax Settings to manage configurations used by Stripe Tax calculations.

Related guide: Using the Settings API

Endpoints
Show

# Verification Session

A VerificationSession guides you through the process of collecting and verifying the identities of your users. It contains details about the type of verification, such as what verification check to perform. Only create one VerificationSession for each verification in your system.

A VerificationSession transitions through multiple statuses throughout its lifetime as it progresses through the verification flow. The VerificationSession contains the user’s verified data after verification checks are complete.

Related guide: The Verification Sessions API

Endpoints
Show

# Verification Report

A VerificationReport is the result of an attempt to collect and verify data from a user. The collection of verification checks performed is determined from the type and options parameters used. You can find the result of each verification check performed in the appropriate sub-resource: document, id_number, selfie.

Each VerificationReport contains a copy of any data collected by the user as well as reference IDs which can be used to access collected images through the FileUpload API. To configure and create VerificationReports, use the VerificationSession API.

Related guides: Accessing verification results.

Endpoints
Show

# Crypto Onramp Session

A Crypto Onramp Session represents your customer’s session as they purchase cryptocurrency through Stripe. Once payment is successful, Stripe will fulfill the delivery of cryptocurrency to your user’s wallet and contain a reference to the crypto transaction ID.

You can create an onramp session on your server and embed the widget on your frontend. Alternatively, you can redirect your users to the standalone hosted onramp.

Related guide: Integrate the onramp

Endpoints
Show

# Crypto Onramp Quotes

Crypto Onramp Quotes are estimated quotes for onramp conversions into all the different cryptocurrencies on different networks. The Quotes API allows you to display quotes in your product UI before directing the user to the onramp widget.

Related guide: Quotes API

Endpoints
Show

# Climate Order

Orders represent your intent to purchase a particular Climate product. When you create an order, the payment is deducted from your merchant balance.

Endpoints
Show

# Climate Product

A Climate product represents a type of carbon removal unit available for reservation. You can retrieve it to see the current price and availability.

Endpoints
Show

# Climate Supplier

A supplier of carbon removal.

Endpoints
Show

# Forwarding RequestPreview feature

Instructs Stripe to make a request on your behalf using the destination URL. The destination URL is activated by Stripe at the time of onboarding. Stripe verifies requests with your credentials provided during onboarding, and injects card details from the payment_method into the request.

Stripe redacts all sensitive fields and headers, including authentication credentials and card numbers, before storing the request and response data in the forwarding Request object, which are subject to a 30-day retention period.

You can provide a Stripe idempotency key to make sure that requests with the same key result in only one outbound request. The Stripe idempotency key provided should be unique and different from any idempotency keys provided on the underlying third-party request.

Forwarding Requests are synchronous requests that return a response or time out according to Stripe’s limits.

Related guide: Forward card details to third-party API endpoints.

Endpoints
Show

# Webhook Endpoints

You can configure webhook endpoints via the API to be notified about events that happen in your Stripe account or connected accounts.

Most users configure webhooks from the dashboard, which provides a user interface for registering and testing your webhook endpoints.

Related guide: Setting up webhooks

Endpoints
Show

Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`