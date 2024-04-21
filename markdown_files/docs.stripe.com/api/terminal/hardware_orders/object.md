htmlThe TerminalHardwareOrder object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The TerminalHardwareOrder objectPreview feature

### Attributes

- idstringUnique identifier for the object.


- amountintegerA positive integer in the smallest currency unit. Represents the total cost for the order.


- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- hardware_order_itemsarray of objectsAn array of line items ordered.

Show child attributes
- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- payment_typeenumOne of monthly_invoice, payment_intent, or none.


- shippingobjectShipping address for the order.

Show child attributes
- shipping_methodstringThe Shipping Method for the order.


- statusenumThe status of the terminal hardware order.

Possible enum values`canceled`Order was canceled. Please create a new order to receive these items.

`delivered`Order has been delivered!

`pending`Order has been received and can still be canceled.

`ready_to_ship`Order has been confirmed and is pending shipment. It cannot be canceled.

`shipped`Order has been shipped, and can no longer be canceled.

`undeliverable`One or more of the order’s items could not be delivered.



### More attributesExpand all

- objectstring
- createdtimestamp
- livemodeboolean
- po_numbernullablestring
- shipment_trackingarray of objects
- taxinteger
- total_tax_amountsarray of objects
- updatednullabletimestamp

The TerminalHardwareOrder object`{  "id": "thor_1Nj6mu2eZvKYlo2CRG74vB9n",  "object": "terminal.hardware_order",  "amount": 13602,  "created": 1692995962,  "currency": "usd",  "hardware_order_items": [    {      "amount": 11800,      "currency": "usd",      "quantity": 2,      "terminal_hardware_sku": {        "id": "thsku_L5fys7HZ5o02Nc",        "amount": 450,        "country": "AT",        "currency": "eur",        "product": "thpr_MJfof7SLvdkG6T"      }    }  ],  "livemode": true,  "metadata": {},  "payment_type": "monthly_invoice",  "po_number": null,  "shipment_tracking": [],  "shipping": {    "address": {      "city": "San Francisco",      "country": "US",      "line1": "1234 Main Street",      "line2": "",      "postal_code": "94111",      "state": "CA"    },    "amount": 800,    "company": "Rocket Rides",    "currency": "usd",    "email": "test@example.com",    "name": "Jenny Rosen",    "phone": "15555555555"  },  "shipping_method": "standard",  "status": "pending",  "tax": 1002,  "total_tax_amounts": [    {      "amount": 1002,      "inclusive": false,      "rate": {        "display_name": "Sales Tax",        "jurisdiction": "LOS ANGELES",        "percentage": 8.25      }    }  ],  "updated": null}`# Create a Terminal Hardware OrderPreview feature

Creates a new TerminalHardwareOrder object.

### Parameters

- hardware_order_itemsarray of objectsRequiredAn array of line items to order.

Show child parameters
- payment_typeenumRequiredThe method of payment for this order.


- shippingobjectRequiredShipping address for the order.

Show child parameters
- shipping_methodstringRequiredThe Shipping Method for the order.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- po_numberstring

### Returns

Returns a TerminalHardwareOrder object if creation succeeds.

POST/v1/terminal/hardware_orderscURL[](#)[](#)`curl https://api.stripe.com/v1/terminal/hardware_orders \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "hardware_order_items[0][terminal_hardware_sku]"=thsku_L5fys7HZ5o02Nc \  -d "hardware_order_items[0][quantity]"=2 \  -d payment_type=monthly_invoice \  -d "shipping[address][line1]"="1234 Main St." \  -d "shipping[address][city]"="San Francisco" \  -d "shipping[address][state]"=CA \  -d "shipping[address][zip]"=94111 \  -d "shipping[address][country]"=US \  -d "shipping[phone]"=15555555555 \  --data-urlencode "shipping[email]"="test@example.com" \  -d "shipping[name]"="Jenny Rosen"`Response`{  "id": "thor_1Nj6mu2eZvKYlo2CRG74vB9n",  "object": "terminal.hardware_order",  "amount": 13602,  "created": 1692995962,  "currency": "usd",  "hardware_order_items": [    {      "amount": 11800,      "currency": "usd",      "quantity": 2,      "terminal_hardware_sku": {        "id": "thsku_L5fys7HZ5o02Nc",        "amount": 450,        "country": "AT",        "currency": "eur",        "product": "thpr_MJfof7SLvdkG6T"      }    }  ],  "livemode": true,  "metadata": {},  "payment_type": "monthly_invoice",  "po_number": null,  "shipment_tracking": [],  "shipping": {    "address": {      "city": "San Francisco",      "country": "US",      "line1": "1234 Main Street",      "line2": "",      "postal_code": "94111",      "state": "CA"    },    "amount": 800,    "company": "Rocket Rides",    "currency": "usd",    "email": "test@example.com",    "name": "Jenny Rosen",    "phone": "15555555555"  },  "shipping_method": "standard",  "status": "pending",  "tax": 1002,  "total_tax_amounts": [    {      "amount": 1002,      "inclusive": false,      "rate": {        "display_name": "Sales Tax",        "jurisdiction": "LOS ANGELES",        "percentage": 8.25      }    }  ],  "updated": null}`# Retrieve a Terminal Hardware OrderPreview feature

Retrieves a TerminalHardwareOrder object.

### Parameters

No parameters.

### Returns

Returns a TerminalHardwareOrder object if a valid identifier was provided.

GET/v1/terminal/hardware_orders/:idcURL[](#)[](#)`curl https://api.stripe.com/v1/terminal/hardware_orders/thor_1Nj6mu2eZvKYlo2CRG74vB9n \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "thor_1Nj6mu2eZvKYlo2CRG74vB9n",  "object": "terminal.hardware_order",  "amount": 13602,  "created": 1692995962,  "currency": "usd",  "hardware_order_items": [    {      "amount": 11800,      "currency": "usd",      "quantity": 2,      "terminal_hardware_sku": {        "id": "thsku_L5fys7HZ5o02Nc",        "amount": 450,        "country": "AT",        "currency": "eur",        "product": "thpr_MJfof7SLvdkG6T"      }    }  ],  "livemode": true,  "metadata": {},  "payment_type": "monthly_invoice",  "po_number": null,  "shipment_tracking": [],  "shipping": {    "address": {      "city": "San Francisco",      "country": "US",      "line1": "1234 Main Street",      "line2": "",      "postal_code": "94111",      "state": "CA"    },    "amount": 800,    "company": "Rocket Rides",    "currency": "usd",    "email": "test@example.com",    "name": "Jenny Rosen",    "phone": "15555555555"  },  "shipping_method": "standard",  "status": "pending",  "tax": 1002,  "total_tax_amounts": [    {      "amount": 1002,      "inclusive": false,      "rate": {        "display_name": "Sales Tax",        "jurisdiction": "LOS ANGELES",        "percentage": 8.25      }    }  ],  "updated": null}`# List all Terminal Hardware OrdersPreview feature

List all TerminalHardwareOrder objects.

### Parameters

- statusenumOnly return orders that have the given status.

Possible enum values`canceled`Order was canceled. Please create a new order to receive these items.

`delivered`Order has been delivered!

`pending`Order has been received and can still be canceled.

`ready_to_ship`Order has been confirmed and is pending shipment. It cannot be canceled.

`shipped`Order has been shipped, and can no longer be canceled.

`undeliverable`One or more of the order’s items could not be delivered.



### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of terminal hardware orders. Each entry in the array is a separate order object.

GET/v1/terminal/hardware_orderscURL[](#)[](#)`curl -G https://api.stripe.com/v1/terminal/hardware_orders \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/terminal/hardware_orders",  "has_more": false,  "data": [    {      "id": "thor_1Nj6mu2eZvKYlo2CRG74vB9n",      "object": "terminal.hardware_order",      "amount": 13602,      "created": 1692995962,      "currency": "usd",      "hardware_order_items": [        {          "amount": 11800,          "currency": "usd",          "quantity": 2,          "terminal_hardware_sku": {            "id": "thsku_L5fys7HZ5o02Nc",            "amount": 450,            "country": "AT",            "currency": "eur",            "product": "thpr_MJfof7SLvdkG6T"          }        }      ],      "livemode": true,      "metadata": {},      "payment_type": "monthly_invoice",      "po_number": null,      "shipment_tracking": [],      "shipping": {        "address": {          "city": "San Francisco",          "country": "US",          "line1": "1234 Main Street",          "line2": "",          "postal_code": "94111",          "state": "CA"        },        "amount": 800,        "company": "Rocket Rides",        "currency": "usd",        "email": "test@example.com",        "name": "Jenny Rosen",        "phone": "15555555555"      },      "shipping_method": "standard",      "status": "pending",      "tax": 1002,      "total_tax_amounts": [        {          "amount": 1002,          "inclusive": false,          "rate": {            "display_name": "Sales Tax",            "jurisdiction": "LOS ANGELES",            "percentage": 8.25          }        }      ],      "updated": null    }    {...}    {...}  ],}`# Cancel a Terminal Hardware OrderPreview feature

Sets the status of a terminal hardware order from pending to canceled.

### Parameters

No parameters.

### Returns

Returns the TerminalHardwareOrder object.

POST/v1/terminal/hardware_orders/:id/cancelcURL[](#)[](#)`curl -X POST https://api.stripe.com/v1/terminal/hardware_orders/thor_1Nj6mu2eZvKYlo2CRG74vB9n/cancel \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "thor_1Nj6mu2eZvKYlo2CRG74vB9n",  "object": "terminal.hardware_order",  "amount": 13602,  "created": 1692995962,  "currency": "usd",  "hardware_order_items": [    {      "amount": 11800,      "currency": "usd",      "quantity": 2,      "terminal_hardware_sku": {        "id": "thsku_L5fys7HZ5o02Nc",        "amount": 450,        "country": "AT",        "currency": "eur",        "product": "thpr_MJfof7SLvdkG6T"      }    }  ],  "livemode": true,  "metadata": {},  "payment_type": "monthly_invoice",  "po_number": null,  "shipment_tracking": [],  "shipping": {    "address": {      "city": "San Francisco",      "country": "US",      "line1": "1234 Main Street",      "line2": "",      "postal_code": "94111",      "state": "CA"    },    "amount": 800,    "company": "Rocket Rides",    "currency": "usd",    "email": "test@example.com",    "name": "Jenny Rosen",    "phone": "15555555555"  },  "shipping_method": "standard",  "status": "canceled",  "tax": 1002,  "total_tax_amounts": [    {      "amount": 1002,      "inclusive": false,      "rate": {        "display_name": "Sales Tax",        "jurisdiction": "LOS ANGELES",        "percentage": 8.25      }    }  ],  "updated": null}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`