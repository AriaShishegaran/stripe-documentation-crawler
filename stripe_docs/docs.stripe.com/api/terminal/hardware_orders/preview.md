- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# Test mode: Mark a Terminal Hardware Order as ShippedTest helperPreview feature

[Test mode: Mark a Terminal Hardware Order as Shipped](/api/terminal/hardware_orders/test_mode_ship)

Updates a test mode TerminalHardwareOrder object’s status as shipped.

No parameters.

Returns a TerminalHardwareOrder object.

# Test mode: Mark a Terminal Hardware Order as UndeliverableTest helperPreview feature

[Test mode: Mark a Terminal Hardware Order as Undeliverable](/api/terminal/hardware_orders/test_mode_mark_undeliverable)

Updates a test mode TerminalHardwareOrder object’s status as undeliverable.

No parameters.

Returns a TerminalHardwareOrder object.
