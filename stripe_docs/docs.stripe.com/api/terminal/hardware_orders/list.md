- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# Cancel a Terminal Hardware OrderPreview feature

[Cancel a Terminal Hardware Order](/api/terminal/hardware_orders/cancel)

Sets the status of a terminal hardware order from pending to canceled.

No parameters.

Returns the TerminalHardwareOrder object.

# Preview a Terminal Hardware OrderPreview feature

[Preview a Terminal Hardware Order](/api/terminal/hardware_orders/preview)

Get a preview of a TerminalHardwareOrder without creating it.

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

Returns a TerminalHardwareOrder object (that has not been created) if the preview succeeds.

# Test mode: Mark a Terminal Hardware Order as Ready To ShipTest helperPreview feature

[Test mode: Mark a Terminal Hardware Order as Ready To Ship](/api/terminal/hardware_orders/test_mode_mark_ready_to_ship)

Updates a test mode TerminalHardwareOrder object’s status as ready_to_ship.

No parameters.

Returns a TerminalHardwareOrder object.

# Test mode: Mark a Terminal Hardware Order as DeliveredTest helperPreview feature

[Test mode: Mark a Terminal Hardware Order as Delivered](/api/terminal/hardware_orders/test_mode_deliver)

Updates a test mode TerminalHardwareOrder object’s status as delivered.

No parameters.

Returns a TerminalHardwareOrder object.
