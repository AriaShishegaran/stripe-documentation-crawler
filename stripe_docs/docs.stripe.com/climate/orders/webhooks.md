# Webhooks for Climate Orders API

Stripe uses webhooks to notify your application when an event happens in your account. Set up a webhook endpoint to listen for product availability and delivery updates.

[webhook endpoint](/webhooks/quickstart)

## Using product webhook events

[climate.product.created](/api/events/types#event_types-climate.product.created)

Stripe sends this event when Frontier adds a new product to the carbon removal inventory. Use this event to keep your application up to date on the latest available products from Frontier.

[carbon removal inventory](/climate/orders/carbon-removal-inventory)

[climate.product.pricing_updated](/api/events/types#event_types-climate.product.pricing_updated)

Stripe sends this event when the price changes for a product. We’ll notify you by email two weeks in advance, and then send this event when the price changes. Prices never change for confirmed orders. If we update the availability of a product, we’ll only notify you through this event.

## Using order webhook events

You receive an event anytime the status of your order changes.

[climate.order.delivered](/api/events/types#event_types-climate.order.delivered)

When Frontier delivers your order, Stripe sends the climate.order.delivered event. This event confirms that Frontier has received carbon removal from the supplier, verified the delivery, and retired the carbon removal units on behalf of you or your designated beneficiary.

[climate.order.delivered](/api/events/types#event_types-climate.order.delivered)

[climate.order.delayed](/api/events/types#event_types-climate.order.delayed)

If Frontier is unable to fulfill your order by the delivery date, Stripe sends the climate.order.delayed event and an email at least 60 days before the end of the delivery year. The event includes the order’s updated expected_delivery_year.

[climate.order.delayed](/api/events/types#event_types-climate.order.delayed)

You can decide whether to accept the delay or cancel the order within 30 days to receive a full refund. If you don’t take any action, we’ll attempt to deliver the tons by the updated expected_delivery_year.

[cancel the order](/api/climate/order/cancel)

[climate.order.product_substituted](/api/events/types#event_types-climate.order.product_substituted)

If you’re ordering a product from an individual supplier and the supplier fails, Frontier tries to substitute the product with a similar one from another supplier in the Frontier portfolio. Stripe sends the climate.order.product_substituted event along with an email with replacement details at least 60 days before the end of the delivery year. If you don’t want a substitute, you can cancel the order within 30 days and receive a full refund.

[climate.order.product_substituted](/api/events/types#event_types-climate.order.product_substituted)

[cancel the order](/api/climate/order/cancel)

[climate.order.canceled](/api/events/types#event_types-climate.order.canceled)

If Frontier can’t fulfill your order within 2 years of the original expected delivery date, you receive a full refund. We expect this to be a rare circumstance because we actively manage the portfolio to minimize delivery risk.

Frontier makes cancellation decisions at least 60 days before the order is due. When an order is canceled, Stripe sends an email and the climate.order.canceled event.

[climate.order.canceled](/api/events/types#event_types-climate.order.canceled)

## See also

- Webhooks quickstart

[Webhooks quickstart](/webhooks/quickstart)

- Webhooks best practices

[Webhooks best practices](/webhooks#best-practices)
