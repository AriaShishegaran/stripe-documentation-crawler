htmlCancel a Terminal Hardware Order | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Cancel a Terminal Hardware OrderPreview feature

Sets the status of a terminal hardware order from pending to canceled.

### Parameters

No parameters.

### Returns

Returns the TerminalHardwareOrder object.

POST/v1/terminal/hardware_orders/:id/cancelcURL[](#)[](#)`curl -X POST https://api.stripe.com/v1/terminal/hardware_orders/thor_1Nj6mu2eZvKYlo2CRG74vB9n/cancel \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "thor_1Nj6mu2eZvKYlo2CRG74vB9n",  "object": "terminal.hardware_order",  "amount": 13602,  "created": 1692995962,  "currency": "usd",  "hardware_order_items": [    {      "amount": 11800,      "currency": "usd",      "quantity": 2,      "terminal_hardware_sku": {        "id": "thsku_L5fys7HZ5o02Nc",        "amount": 450,        "country": "AT",        "currency": "eur",        "product": "thpr_MJfof7SLvdkG6T"      }    }  ],  "livemode": true,  "metadata": {},  "payment_type": "monthly_invoice",  "po_number": null,  "shipment_tracking": [],  "shipping": {    "address": {      "city": "San Francisco",      "country": "US",      "line1": "1234 Main Street",      "line2": "",      "postal_code": "94111",      "state": "CA"    },    "amount": 800,    "company": "Rocket Rides",    "currency": "usd",    "email": "test@example.com",    "name": "Jenny Rosen",    "phone": "15555555555"  },  "shipping_method": "standard",  "status": "canceled",  "tax": 1002,  "total_tax_amounts": [    {      "amount": 1002,      "inclusive": false,      "rate": {        "display_name": "Sales Tax",        "jurisdiction": "LOS ANGELES",        "percentage": 8.25      }    }  ],  "updated": null}`# Preview a Terminal Hardware OrderPreview feature

Get a preview of a TerminalHardwareOrder without creating it.

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

Returns a TerminalHardwareOrder object (that has not been created) if the preview succeeds.

GET/v1/terminal/hardware_orders/previewcURL[](#)[](#)`curl -G https://api.stripe.com/v1/terminal/hardware_orders/preview \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "shipping[name]"="Jenny Rosen" \  -d "shipping[address][line1]"="1234 Main Street" \  -d "shipping[address][city]"="San Francisco" \  -d "shipping[address][state]"=CA \  -d "shipping[address][country]"=US \  -d "shipping[address][postal_code]"=94111 \  -d "shipping[company]"="Rocket Rides" \  -d "shipping[phone]"=15555555555 \  --data-urlencode "shipping[email]"="test@example.com" \  -d shipping_method=thsm_MfuTjLaPEgXMa4 \  -d payment_type=monthly_invoice \  -d "hardware_order_items[0][terminal_hardware_sku]"=thsku_L5fys7HZ5o02Nc \  -d "hardware_order_items[0][quantity]"=2`Response`{  "object": "terminal.hardware_order",  "amount": 13602,  "currency": "usd",  "hardware_order_items": [    {      "amount": 11800,      "currency": "usd",      "quantity": 2,      "terminal_hardware_sku": {        "id": "thsku_L5fys7HZ5o02Nc",        "amount": 450,        "country": "AT",        "currency": "eur",        "product": "thpr_MJfof7SLvdkG6T"      }    }  ],  "livemode": true,  "metadata": {},  "payment_type": "monthly_invoice",  "po_number": null,  "shipment_tracking": [],  "shipping": {    "address": {      "city": "San Francisco",      "country": "US",      "line1": "1234 Main Street",      "line2": "",      "postal_code": "94111",      "state": "CA"    },    "amount": 800,    "company": "Rocket Rides",    "currency": "usd",    "email": "test@example.com",    "name": "Jenny Rosen",    "phone": "15555555555"  },  "shipping_method": "standard",  "status": "pending",  "tax": 1002,  "total_tax_amounts": [    {      "amount": 1002,      "inclusive": false,      "rate": {        "display_name": "Sales Tax",        "jurisdiction": "LOS ANGELES",        "percentage": 8.25      }    }  ]}`# Test mode: Mark a Terminal Hardware Order as Ready To ShipTest helperPreview feature

Updates a test mode TerminalHardwareOrder object’s status as ready_to_ship.

### Parameters

No parameters.

### Returns

Returns a TerminalHardwareOrder object.

POST/v1/test_helpers/terminal/hardware_orders/:id/mark_ready_to_shipcURL[](#)[](#)`curl -X POST https://api.stripe.com/v1/test_helpers/terminal/hardware_orders/thor_1Nj6mu2eZvKYlo2CRG74vB9n/mark_ready_to_ship \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "thor_1Nj6mu2eZvKYlo2CRG74vB9n",  "object": "terminal.hardware_order",  "amount": 13602,  "created": 1692995962,  "currency": "usd",  "hardware_order_items": [    {      "amount": 11800,      "currency": "usd",      "quantity": 2,      "terminal_hardware_sku": {        "id": "thsku_L5fys7HZ5o02Nc",        "amount": 450,        "country": "AT",        "currency": "eur",        "product": "thpr_MJfof7SLvdkG6T"      }    }  ],  "livemode": true,  "metadata": {},  "payment_type": "monthly_invoice",  "po_number": null,  "shipment_tracking": [],  "shipping": {    "address": {      "city": "San Francisco",      "country": "US",      "line1": "1234 Main Street",      "line2": "",      "postal_code": "94111",      "state": "CA"    },    "amount": 800,    "company": "Rocket Rides",    "currency": "usd",    "email": "test@example.com",    "name": "Jenny Rosen",    "phone": "15555555555"  },  "shipping_method": "standard",  "status": "ready_to_ship",  "tax": 1002,  "total_tax_amounts": [    {      "amount": 1002,      "inclusive": false,      "rate": {        "display_name": "Sales Tax",        "jurisdiction": "LOS ANGELES",        "percentage": 8.25      }    }  ],  "updated": null}`# Test mode: Mark a Terminal Hardware Order as DeliveredTest helperPreview feature

Updates a test mode TerminalHardwareOrder object’s status as delivered.

### Parameters

No parameters.

### Returns

Returns a TerminalHardwareOrder object.

POST/v1/test_helpers/terminal/hardware_orders/:id/delivercURL[](#)[](#)`curl -X POST https://api.stripe.com/v1/test_helpers/terminal/hardware_orders/thor_1Nj6mu2eZvKYlo2CRG74vB9n/deliver \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "thor_1Nj6mu2eZvKYlo2CRG74vB9n",  "object": "terminal.hardware_order",  "amount": 13602,  "created": 1692995962,  "currency": "usd",  "hardware_order_items": [    {      "amount": 11800,      "currency": "usd",      "quantity": 2,      "terminal_hardware_sku": {        "id": "thsku_L5fys7HZ5o02Nc",        "amount": 450,        "country": "AT",        "currency": "eur",        "product": "thpr_MJfof7SLvdkG6T"      }    }  ],  "livemode": true,  "metadata": {},  "payment_type": "monthly_invoice",  "po_number": null,  "shipment_tracking": [],  "shipping": {    "address": {      "city": "San Francisco",      "country": "US",      "line1": "1234 Main Street",      "line2": "",      "postal_code": "94111",      "state": "CA"    },    "amount": 800,    "company": "Rocket Rides",    "currency": "usd",    "email": "test@example.com",    "name": "Jenny Rosen",    "phone": "15555555555"  },  "shipping_method": "standard",  "status": "delivered",  "tax": 1002,  "total_tax_amounts": [    {      "amount": 1002,      "inclusive": false,      "rate": {        "display_name": "Sales Tax",        "jurisdiction": "LOS ANGELES",        "percentage": 8.25      }    }  ],  "updated": null}`# Test mode: Mark a Terminal Hardware Order as ShippedTest helperPreview feature

Updates a test mode TerminalHardwareOrder object’s status as shipped.

### Parameters

No parameters.

### Returns

Returns a TerminalHardwareOrder object.

POST/v1/test_helpers/terminal/hardware_orders/:id/shipcURL[](#)[](#)`curl -X POST https://api.stripe.com/v1/test_helpers/terminal/hardware_orders/thor_1Nj6mu2eZvKYlo2CRG74vB9n/ship \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "thor_1Nj6mu2eZvKYlo2CRG74vB9n",  "object": "terminal.hardware_order",  "amount": 13602,  "created": 1692995962,  "currency": "usd",  "hardware_order_items": [    {      "amount": 11800,      "currency": "usd",      "quantity": 2,      "terminal_hardware_sku": {        "id": "thsku_L5fys7HZ5o02Nc",        "amount": 450,        "country": "AT",        "currency": "eur",        "product": "thpr_MJfof7SLvdkG6T"      }    }  ],  "livemode": true,  "metadata": {},  "payment_type": "monthly_invoice",  "po_number": null,  "shipment_tracking": [],  "shipping": {    "address": {      "city": "San Francisco",      "country": "US",      "line1": "1234 Main Street",      "line2": "",      "postal_code": "94111",      "state": "CA"    },    "amount": 800,    "company": "Rocket Rides",    "currency": "usd",    "email": "test@example.com",    "name": "Jenny Rosen",    "phone": "15555555555"  },  "shipping_method": "standard",  "status": "shipped",  "tax": 1002,  "total_tax_amounts": [    {      "amount": 1002,      "inclusive": false,      "rate": {        "display_name": "Sales Tax",        "jurisdiction": "LOS ANGELES",        "percentage": 8.25      }    }  ],  "updated": null}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`