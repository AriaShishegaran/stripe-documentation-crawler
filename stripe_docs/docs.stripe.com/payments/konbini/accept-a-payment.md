# Konbini payments

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

Konbini is a single use payment method where customers are required to take additional steps to complete their payment. Customers pay by providing a payment code, confirmation number, and cash payment at Japanese convenience stores. Stripe notifies you when the payment is completed.

[single use](/payments/payment-methods#usage)

[take additional steps](/payments/payment-methods#customer-actions)

[Determine compatibility](#compatibility)

## Determine compatibility

Supported business locations: JP

Supported currencies: jpy

Presentment currencies: jpy

Payment mode: Yes

Setup mode: No

Subscription mode: No

A Checkout Session must satisfy all of the following conditions to support Konbini payments:

- Prices for all line items must be in the same currency (JPY).

[Prices](/api/prices)

- You can only use one-time line items (recurring subscription plans are not supported).

[subscription](/billing/subscriptions/creating)

[Accept a payment](#accept-a-payment)

## Accept a payment

Build an integration to accept a payment with Checkout before using this guide.

[accept a payment](/payments/accept-a-payment?integration=checkout)

Use this guide to learn how to enable Konbini—it shows the differences between accepting a card payment and using Konbini.

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add konbini to the list of payment_method_types

- Make sure all your line_items use the jpy currency.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

Payment method options can be specified in the payment method options under the konbini key.

[payment method options](/api/checkout/sessions/create#create_checkout_session-payment_method_options-konbini)

[Expiration](#checkout-additional-options-expiration)

Pending Konbini payments expire right before midnight (23:59:59 JST) on the specified date. For example if expires_after_days is set to 2 and the PaymentIntent is confirmed on Monday, the pending Konbini payment will expire on Wednesday at 23:59:59 Japan (UTC+9) time.

On the Konbini checkout form, your customers can optionally supply a phone number to use as their confirmation number. This simplifies their payment process at a convenience store where the in-store UI asks for the customer to provide a payment code and their confirmation number. Both are reflected in the payment instructions that Stripe displays after the customer submits their checkout form. If your customer doesn’t provide a phone number, Stripe generates a random confirmation number.

Stripe proactively blocks phone numbers consisting of only zeros.

Unlike card payments, the customer won’t be redirected to the success_url with Konbini payment.

[success_url](/api/checkout/sessions/object#checkout_session_object-success_url)

After submitting the Checkout form successfully, the customer is redirected to the hosted_voucher_url. The customer can reference the hosted page’s payment instructions for details on how to complete their payment. The page is viewable on desktop and mobile, as well as being printable.

Stripe sends a payment_intent.requires_action event when a Konbini voucher is created successfully. If you need to email your customers the voucher’s payment instructions link, you can locate the hosted_voucher_url in payment_intent.next_action.konbini_display_details. Learn more about how to monitor a PaymentIntent with webhooks.

[payment_intent.requires_action](/api/events/types#event_types-payment_intent.requires_action)

[payment_intent.next_action.konbini_display_details](/api/payment_intents/object#payment_intent_object-next_action-konbini_display_details-hosted_voucher_url)

[monitor a PaymentIntent with webhooks](/payments/payment-intents/verifying-status#webhooks)

Stripe allows customization of customer-facing UIs on the Branding Settings page. The following brand settings can be applied to the voucher:

[Branding Settings](https://dashboard.stripe.com/account/branding)

- Icon—your brand image and public business name

- Accent color—used as the color of the Copy Number button

- Brand color—used as the background color

Because Konbini is a delayed notification payment method, you need to use a method such as webhooks to monitor the payment status and handle order fulfillment. Learn more about setting up webhooks and fulfilling orders.

[webhooks](/webhooks)

[setting up webhooks and fulfilling orders](/payments/checkout/fulfill-orders)

The following events are sent when the payment status changes:

checkout.session.completed

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

The customer has successfully submitted the Checkout form. Stripe has generated the Konbini voucher.

You can choose to email the hosted_voucher_url to your customer in case they lose the Konbini voucher.

Wait for the customer to pay at a Konbini.

[checkout.session.async_payment_succeeded](/api/events/types#event_types-checkout.session.async_payment_succeeded)

[checkout.session.async_payment_failed](/api/events/types#event_types-checkout.session.async_payment_failed)

[Test your integration](#test-integration)

## Test your integration

When testing your Checkout integration, select Konbini as the payment method and click the Pay button.

Provide the following values in the Checkout form to test different scenarios. You can either test with a special confirmation number or an email pattern. If both are provided the behavior of the special confirmation number applies.

{any_prefix}@{any_domain}

11111111110

Simulates a Konbini payment which succeeds after 3 minutes and the payment_intent.succeeded webhook arrives after that.

Example: hanako@test.com

{any_prefix}succeed_immediately@{any_domain}

22222222220

Simulates a Konbini payment which succeeds immediately and the payment_intent.succeeded webhook arrives after that.

Example: succeed_immediately@test.com

{any_prefix}expire_immediately@{any_domain}

33333333330

Simulates a Konbini payment which expires immediately and the payment_intent.payment_failed webhook arrives after that.

The expires_at field in next_action.konbini_display_details is set to the current time regardless of what the expires_after_days or expires_at parameter in payment method options is set to.

[next_action.konbini_display_details](/api/payment_intents/object#payment_intent_object-next_action-konbini_display_details-expires_at)

[payment method options](/api/payment_intents/create#create_payment_intent-payment_method_options-konbini-expires_after_days)

Example: expire_immediately@test.com

{any_prefix}expire_with_delay@{any_domain}

44444444440

Simulates a Konbini payment which never succeeds; it expires in 3 minutes and the payment_intent.payment_failed webhook arrives after that.

The expires_at field in next_action.konbini_display_details is set to 3 minutes in the future regardless of what the expires_after_days or expires_at parameter in payment method options is set to.

[next_action.konbini_display_details](/api/payment_intents/object#payment_intent_object-next_action-konbini_display_details-expires_at)

[payment method options](/api/payment_intents/create#create_payment_intent-payment_method_options-konbini-expires_after_days)

Example: expire_with_delay@test.com

{any_prefix}fill_never@{any_domain}

55555555550

Simulates a Konbini payment which never succeeds; it expires according to the expires_at field in next_action.konbini_display_details per the provided parameters in the payment method options and the payment_intent.payment_failed webhook arrives after that.

[payment method options](/api/payment_intents/create#create_payment_intent-payment_method_options-konbini-expires_after_days)

Example: fill_never@test.com

In order to test confirmation number errors you may use the following values:

[confirmation number](#web-confirm-payment-intent-additional-options-confirmation-number)

- 01234567890 simulates a confirmation number rejection.

- 00000000000 results in a validation error.

[Expiration and cancellation](#web-expiration-and-cancellation)

## Expiration and cancellation

After the time specified by the expires_at value in the next_action.konbini_display_details, the customer can no longer initiate the payment process for a pending Konbini payment at a convenience store kiosk. However, if they issued a valid payment slip before the deadline they may be able to complete the payment at the cash register after the expires_at time.

[next_action.konbini_display_details](/api/payment_intents/object#payment_intent_object-next_action-konbini_display_details-expires_at)

There is a buffer period to avoid premature payment failures in such an event. The PaymentIntent’s status changes to requires_payment_method. At this point, you can cancel or confirm the PaymentIntent with another payment method.

You can also cancel a pending Konbini payment after confirmation and before the time specified by next_action.konbini_display_details.expires_at. Updating the PaymentIntent or confirming it with another payment method will also implicitly cancel the existing Konbini payment.

If the customer is currently paying for the Konbini payment at the convenience store, the cancellation request will fail. Cancellation may be re-attempted if the customer abandons the payment attempt and after the payment slip expires.

Note that temporary payment method availability issues also affect (both explicit as well as implicit) cancellation requests.

[temporary payment method availability issues](#web-handling-temporary-availability-issues)

When you cancel a pending payment the original payment instructions become invalid. For most use cases we suggest you reach out to your customer to inform them of the cancellation.

When you successfully reconfirm a PaymentIntent in status requires_action we create new instructions and a new hosted_voucher_url. You need to ensure that your customer is made aware of these.

[Refunds](#refunds)

## Refunds

It is possible to refund Konbini payments through the Dashboard or API.

[Dashboard](https://dashboard.stripe.com/payments)

[API](/api#create_refund)

To complete a refund sent to the customer’s bank account directly, your customer must provide the bank account details where they would like to receive the funds. Stripe contacts the customer at the email address from the billing details on the payment method and requests these details from them. After we receive the bank details, we process the refund automatically.

The refund’s status transitions as follows:

If the customer’s bank can’t successfully complete the transfer, the funds are returned to Stripe and the refund transitions to requires_action. This can happen if the account holder’s name doesn’t match what the recipient bank has on file or if the provided bank account number has a typo. In these cases, Stripe emails the customer to inform them of the failure and to request that they resubmit their bank account details.

If your customer does not provide their bank account details within 45 days, the refund’s status transitions to failed and the charge.refund.updated event is sent. This means that Stripe is unable to process the refund, and you must return the funds to your customer outside of Stripe.

[charge.refund.updated](/api/events/types#event_types-charge.refund.updated)

[return the funds to your customer outside of Stripe](/refunds#failed-refunds)

The instructions_email field on the refund is the email that the refund was sent to. While a refund is waiting for a response from the customer, details of the email sent to the customer can also be found under the next_action.display_details.email_sent field on the refund.

[instructions_email](/api/refunds/object#refund_object-instructions_email)

[next_action.display_details.email_sent](/api/refunds/object#refund_object-next_action-display_details-email_sent)

Each individual refund (including each partial refund) may incur a fee. Please reach out to your point of contact at Stripe to learn more about this.

You can test refund behavior in testmode using the following test bank accounts on the bank account details collection page linked in the email sent to the customer. Bank account details outside of these test bank accounts will not be accepted.

1100000

1111113

1111116

1111113

3333335

4444440

Refund fails.

You can make an API call to simulate the expiry of a testmode refund.

## See also

- After the Payment

[After the Payment](/payments/checkout/fulfill-orders)

- Customizing Checkout

[Customizing Checkout](/payments/checkout/customization)
