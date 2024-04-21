# Manage limited inventory with Checkout

For some types of limited-inventory businesses, it’s necessary to prevent customers from reserving items for a long time without completing the purchase. For example, an event ticket seller wants to allow customers only a few minutes to buy their selected tickets before cancelling the sale and making those tickets available again. You can cancel a pending sale by expiring the Checkout Session.

[Checkout Session](/api/checkout/sessions)

When a Checkout Session expires, its status property changes to expired.

[status property](/api/checkout/sessions/object#checkout_session_object-status)

Checkout supports both manual and timed session expiration.

## Manual expiration

To immediately expire an open Checkout Session and cancel any pending purchase, use the expire endpoint.

[expire](/api/checkout/sessions/expire)

## Set an expiration time

When you create a Checkout Session, specify an expiration timestamp by setting the expires_at parameter. The value must be between 30 minutes and 24 hours after the current time. If you don’t specify expires_at, the default value is 24 hours after the current time.

[expires_at](/api/checkout/sessions/create#create_checkout_session-expires_at)

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

## Return items to your inventory

When a Checkout Session expires, it triggers the checkout.session.expired event. Configure your webhook endpoint to listen for this event so your webhook handler can return to inventory any items reserved in the expired session. For more information, see Expire a Session.

[Checkout Session](/api/checkout/sessions)

[Expire a Session](/api/checkout/sessions/expire)
