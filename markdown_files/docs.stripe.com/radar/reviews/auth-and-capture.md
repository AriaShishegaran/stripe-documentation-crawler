htmlReviewing uncaptured payments | Stripe Documentation[Skip to content](#main-content)Uncaptured payments[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fradar%2Freviews%2Fauth-and-capture)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fradar%2Freviews%2Fauth-and-capture)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)
[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Radar](/radar)·[Home](/docs)[Get started](/docs/get-started)[Protect against fraud](/docs/radar)[Reviews](/docs/radar/reviews)# Reviewing uncaptured payments

Learn how to use reviews if your Stripe integration uses auth and capture.By default, you create Stripe payments in one step, which requires no further action on your part to send the funds to your bank account.

However, Stripe also supports two-step payments, often called auth and capture.  If your integration uses this technique, keep in mind that approving a review and capturing a payment are separate actions.

## Reviewing uncaptured payments in the Dashboard

When Stripe places an uncaptured payment in review, the Dashboard displays a Capture button in addition to the set of buttons for closing the review by approving or refunding it. Also, because refunding uncaptured payments is often called “releasing” or “reversing,” uncaptured payments have a Cancel button instead of a Refund button.

NoteApproving the review doesn’t automatically capture the charge.  You still need to click Capture.

![](https://b.stripecdn.com/docs-statics-srv/assets/uncaptured-payment.b9aab5781bebea8e1cc8f349dc2092bf.png)

## Using the API to automatically capture approved payments

Through the API, you can set up your integration to:

- Immediately capture paymentsnotplaced in`review`
- Leave payments placed in`review`uncaptured
- When the review is approved, capture the payment

### Immediately capture payments not placed in review

To create an uncaptured payment, set the capture behavior accordingly in the API request.  On success, check the payment intent’s review attribute. If the attribute is empty, capture the charge.

[Ruby](#)`# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

# Get the credit card details submitted by the form
# Create a PaymentIntent with manual capture
payment_intent = Stripe::PaymentIntent.create({
  amount: 1000,
  currency: 'usd',
  payment_method: '{{PAYMENT_METHOD_ID}}',
  description: 'Example charge',
  confirm: true,
  capture_method: 'manual',
})

# Check if the payment is in review. If not, capture it.
if !payment_intent.review
  payment_intent.capture
end`### Capturing a payment after a review is approved

By design, the previous step left the payments in review uncaptured.  In this step, use webhooks to automate the process of capturing these payments upon approval.

Start by configuring your webhooks to listen for the review.closed event. The event data includes the review object, and the object’s reason attribute indicates whether the review was approved, or if it was closed for some other reason (for example, the payment was refunded).

`// Review object included in review.closed event webhook.
{
  "id": "prv_08voh1589O8KAxCGPcIQpmkz",
  "object": "review",
  "payment_intent": "pi_1D0CsEITpIrAk4QYdrWDnbRS",
  "created": 1474379631,
  "livemode": false,
  "open": false,
  "reason": "approved"
}`If reason is approved, capture the charge.

`# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

post "/my/webhook/url" do
  event_json = JSON.parse(request.body.read)
  event = Stripe::Event.retrieve(event_json["id"])

  if event.type == 'review.closed'
    review = event.object
    if review.reason == 'approved'
      pi = Stripe::PaymentIntent.retrieve(review.payment_intent)
      pi.capture
    end
  end

  status 200
end`To capture approved payments, the review process must be completed within 7 days.  Otherwise, as with any other uncaptured payment, the authorization automatically expires and you can no longer capture the payment.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Reviewing uncaptured payments in the Dashboard](#reviewing-uncaptured-payments-in-the-dashboard)[Using the API to automatically capture approved payments](#using-the-api-to-automatically-capture-approved-payments)Products Used[Radar](/radar)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`