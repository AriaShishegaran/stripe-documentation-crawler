# Reviewing uncaptured payments

By default, you create Stripe payments in one step, which requires no further action on your part to send the funds to your bank account.

[create Stripe payments](/payments/accept-a-payment)

However, Stripe also supports two-step payments, often called auth and capture.  If your integration uses this technique, keep in mind that approving a review and capturing a payment are separate actions.

[auth and capture](https://support.stripe.com/questions/does-stripe-support-authorize-and-capture)

## Reviewing uncaptured payments in the Dashboard

When Stripe places an uncaptured payment in review, the Dashboard displays a Capture button in addition to the set of buttons for closing the review by approving or refunding it. Also, because refunding uncaptured payments is often called “releasing” or “reversing,” uncaptured payments have a Cancel button instead of a Refund button.

[reversing](/refunds#refund-requests)

Approving the review doesn’t automatically capture the charge.  You still need to click Capture.

## Using the API to automatically capture approved payments

Through the API, you can set up your integration to:

- Immediately capture payments not placed in review

- Leave payments placed in review uncaptured

- When the review is approved, capture the payment

To create an uncaptured payment, set the capture behavior accordingly in the API request.  On success, check the payment intent’s review attribute. If the attribute is empty, capture the charge.

[review](/api/payment_intents/object#payment_intent_object-review)

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

By design, the previous step left the payments in review uncaptured.  In this step, use webhooks to automate the process of capturing these payments upon approval.

[webhooks](/webhooks)

Start by configuring your webhooks to listen for the review.closed event. The event data includes the review object, and the object’s reason attribute indicates whether the review was approved, or if it was closed for some other reason (for example, the payment was refunded).

[configuring your webhooks](/webhooks#register-webhook)

[review object](/api#review_object)

If reason is approved, capture the charge.

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

To capture approved payments, the review process must be completed within 7 days.  Otherwise, as with any other uncaptured payment, the authorization automatically expires and you can no longer capture the payment.
