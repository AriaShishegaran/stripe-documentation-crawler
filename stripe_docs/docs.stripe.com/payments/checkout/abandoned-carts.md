# Recover abandoned carts

Customers may leave Checkout before completing their purchase. In e-commerce, this is known as cart abandonment. To help bring customers back to Checkout, create a recovery flow where you follow up with customers over email to complete their purchases. You can do this with webhooks (see below) or with no-code Cart Recovery Emails.

[Customers](/api/customers)

[cart abandonment](/payments/checkout/compliant-promotional-emails)

[no-code Cart Recovery Emails](/no-code/cart-recovery-emails)

Cart abandonment emails fall into the broader category of promotional emails, which includes emails that inform customers of new products and that share coupons and discounts. Customers must agree to receive promotional emails before you can contact them.

Checkout helps you:

- Collect consent from customers to send them promotional emails.

- Get notified when customers abandon Checkout so you can send cart abandonment emails.

[Collect promotional consent](#collect-promotional-consent)

## Collect promotional consent

Configure Checkout to collect consent for promotional content. See the full guide for more details.

[full guide](/payments/checkout/promotional-emails-consent)

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

If you collect the customer’s email address and request consent for promotional content before redirecting to Checkout, you may skip using consent_collection[promotions].

[Configure recovery](#configure-recovery)

## Configure recovery

A Checkout Session becomes abandoned when it reaches its expires_at timestamp and the buyer hasn’t completed checking out. When this occurs, the session is no longer accessible and Stripe fires the checkout.session.expired webhook, which you can listen to and try to bring the customer back to a new Checkout Session to complete their purchase.

[expires_at](/api/checkout/sessions/object#checkout_session_object-expires_at)

[webhook](/webhooks)

To use this feature, enable after_expiration.recovery when you create the session.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

[Get notified of abandonment](#webhook)

## Get notified of abandonment

Listen to the checkout.session.expired webhook to be notified when customers abandon Checkout and sessions expire. When the session expires with recovery enabled, the webhook payload contains after_expiration, which includes a URL denoted by after_expiration.recovery.url that you can embed in cart abandonment emails. When the customer opens this URL, it creates a new Checkout Session that’s a copy of the original expired session. The customer uses this copied session to complete the purchase on a Stripe-hosted payment page.

[after_expiration](/api/checkout/sessions/object#checkout_session_object-after_expiration-recovery)

For security purposes, the recovery URL for a session is usable for 30 days, denoted by the after_expiration.recovery.expires_at timestamp.

[https://buy.stripe.com/r/live_asAb1724](https://buy.stripe.com/r/live_asAb1724)

[Send recovery emails](#send-recovery-emails)

## Send recovery emails

To send recovery emails, create a webhook handler for expired sessions and send an email that embeds the session’s recovery URL. One customer may abandon multiple Checkout Sessions, each triggering its own checkout.session.expired webhook so make sure to record when you send recovery emails to customers and avoid spamming them.

[OptionalAdjust session expiration](#adjust-session-expiration)

## OptionalAdjust session expiration

[OptionalTrack conversion](#track-conversion)

## OptionalTrack conversion

[OptionalOffer promotion codes in recovery emails](#promotion-codes)

## OptionalOffer promotion codes in recovery emails
