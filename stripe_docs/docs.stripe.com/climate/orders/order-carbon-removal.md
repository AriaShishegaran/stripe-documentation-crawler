# Order carbon removal

[Fund a climate order](#fund-a-climate-order)

## Fund a climate order

When you purchase carbon removal, we deduct the funds from your Stripe balance. You can fund your balance using a Top-up, Invoice, or Checkout session. For an example of how to fund a climate order from your application, see the Climate Orders quickstart.

[Top-up](/get-started/account/add-funds)

[Invoice](/invoicing/quickstart-guide)

[Checkout session](/checkout/quickstart)

[Climate Orders quickstart](/climate/orders/quickstart)

[Create a climate order](#create-a-climate-order)

## Create a climate order

Reserve and pay for carbon removal by creating a climate order. You can use the order to track your products through confirmation and delivery. When you create your order, we immediately deduct the funds from your Stripe balance.

You have 30 days to cancel a climate order and receive a refund of the purchase amount, but fees won’t be refunded.

If you’re programmatically funding your account, make this call in the corresponding webhook handler for your funding source.

[Track your climate orders](#track-your-climate-orders)

## Track your climate orders

You can track the status of your climate orders in the Dashboard.

[Dashboard](https://dashboard.stripe.com/climate/orders)

To get updates about a climate order, listen for events on your Stripe account. When the order status changes, you receive an event with the details. When your order is delivered, you receive a climate.order.delivered event. See Webhooks for climate orders for other possible event types.

[Webhooks for climate orders](/climate/orders/webhooks)
