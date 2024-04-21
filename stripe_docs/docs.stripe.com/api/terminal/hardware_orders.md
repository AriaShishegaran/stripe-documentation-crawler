- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Terminal Hardware OrderPreview feature

[Terminal Hardware Order](/api/terminal/hardware_orders)

A TerminalHardwareOrder represents an order for Terminal hardware, containing information such as the price, shipping information and the items ordered.

[POST/v1/terminal/hardware_orders](/api/terminal/hardware_orders/create)

[GET/v1/terminal/hardware_orders/:id](/api/terminal/hardware_orders/retrieve)

[GET/v1/terminal/hardware_orders](/api/terminal/hardware_orders/list)

[POST/v1/terminal/hardware_orders/:id/cancel](/api/terminal/hardware_orders/cancel)

[GET/v1/terminal/hardware_orders/preview](/api/terminal/hardware_orders/preview)

[POST/v1/test_helpers/terminal/hardware_orders/:id/mark_ready_to_ship](/api/terminal/hardware_orders/test_mode_mark_ready_to_ship)

[POST/v1/test_helpers/terminal/hardware_orders/:id/deliver](/api/terminal/hardware_orders/test_mode_deliver)

[POST/v1/test_helpers/terminal/hardware_orders/:id/ship](/api/terminal/hardware_orders/test_mode_ship)

[POST/v1/test_helpers/terminal/hardware_orders/:id/mark_undeliverable](/api/terminal/hardware_orders/test_mode_mark_undeliverable)

# The TerminalHardwareOrder objectPreview feature

[The TerminalHardwareOrder object](/api/terminal/hardware_orders/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- amountintegerA positive integer in the smallest currency unit. Represents the total cost for the order.

A positive integer in the smallest currency unit. Represents the total cost for the order.

[smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)

- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- hardware_order_itemsarray of objectsAn array of line items ordered.Show child attributes

An array of line items ordered.

- metadatanullable objectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- payment_typeenumOne of monthly_invoice, payment_intent, or none.

One of monthly_invoice, payment_intent, or none.

- shippingobjectShipping address for the order.Show child attributes

Shipping address for the order.

- shipping_methodstringThe Shipping Method for the order.

The Shipping Method for the order.

[Shipping Method](/api/terminal/hardware_shipping_methods/object)

- statusenumThe status of the terminal hardware order.Possible enum valuescanceledOrder was canceled. Please create a new order to receive these items.deliveredOrder has been delivered!pendingOrder has been received and can still be canceled.ready_to_shipOrder has been confirmed and is pending shipment. It cannot be canceled.shippedOrder has been shipped, and can no longer be canceled.undeliverableOne or more of the order’s items could not be delivered.

The status of the terminal hardware order.

Order was canceled. Please create a new order to receive these items.

Order has been delivered!

Order has been received and can still be canceled.

Order has been confirmed and is pending shipment. It cannot be canceled.

Order has been shipped, and can no longer be canceled.

One or more of the order’s items could not be delivered.

- objectstring

- createdtimestamp

- livemodeboolean

- po_numbernullable string

- shipment_trackingarray of objects

- taxinteger

- total_tax_amountsarray of objects

- updatednullable timestamp

# Create a Terminal Hardware OrderPreview feature

[Create a Terminal Hardware Order](/api/terminal/hardware_orders/create)

Creates a new TerminalHardwareOrder object.

- hardware_order_itemsarray of objectsRequiredAn array of line items to order.Show child parameters

An array of line items to order.

- payment_typeenumRequiredThe method of payment for this order.

The method of payment for this order.

- shippingobjectRequiredShipping address for the order.Show child parameters

Shipping address for the order.

- shipping_methodstringRequiredThe Shipping Method for the order.

The Shipping Method for the order.

[Shipping Method](/api/terminal/hardware_shipping_methods/object)

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- po_numberstring

Returns a TerminalHardwareOrder object if creation succeeds.

# Retrieve a Terminal Hardware OrderPreview feature

[Retrieve a Terminal Hardware Order](/api/terminal/hardware_orders/retrieve)

Retrieves a TerminalHardwareOrder object.

No parameters.

Returns a TerminalHardwareOrder object if a valid identifier was provided.

# List all Terminal Hardware OrdersPreview feature

[List all Terminal Hardware Orders](/api/terminal/hardware_orders/list)

List all TerminalHardwareOrder objects.

- statusenumOnly return orders that have the given status.Possible enum valuescanceledOrder was canceled. Please create a new order to receive these items.deliveredOrder has been delivered!pendingOrder has been received and can still be canceled.ready_to_shipOrder has been confirmed and is pending shipment. It cannot be canceled.shippedOrder has been shipped, and can no longer be canceled.undeliverableOne or more of the order’s items could not be delivered.

Only return orders that have the given status.

Order was canceled. Please create a new order to receive these items.

Order has been delivered!

Order has been received and can still be canceled.

Order has been confirmed and is pending shipment. It cannot be canceled.

Order has been shipped, and can no longer be canceled.

One or more of the order’s items could not be delivered.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of terminal hardware orders. Each entry in the array is a separate order object.
