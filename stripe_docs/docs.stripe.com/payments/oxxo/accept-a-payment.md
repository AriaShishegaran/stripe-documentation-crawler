# Accept an OXXO payment

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

OXXO is a single use payment method where customers are required to take additional steps to complete their payment. Customers pay by providing an OXXO voucher with a generated number and cash payment at an OXXO convenience store.

[single use](/payments/payment-methods#usage)

[take additional steps](/payments/payment-methods#customer-actions)

[Customers](/api/customers)

[Determine compatibility](#compatibility)

## Determine compatibility

Supported business locations: MX

Supported currencies: mxn

Presentment currencies: mxn

Payment mode: Yes

Setup mode: No

Subscription mode: No

A Checkout Session must satisfy all of the following conditions to support OXXO payments:

- Prices for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.

[Prices](/api/prices)

- You can only use one-time line items (recurring subscription plans are not supported).

[subscription](/billing/subscriptions/creating)

[Accept a payment](#accept-a-payment)

## Accept a payment

Build an integration to accept a payment with Checkout before using this guide.

[accept a payment](/payments/accept-a-payment?integration=checkout)

Use this guide to learn how to enable OXXO—it shows the differences between accepting a card payment and using OXXO.

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add oxxo to the list of payment_method_types

- Make sure all your line_items use the mxn currency.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

You can specify an optional expires_after_days parameter in the payment method options for your Session that sets the number of calendar days before an OXXO voucher expires. For example, if you create an OXXO voucher on Monday and you set expires_after_days to 2, the OXXO voucher will expire on Wednesday at 23:59 America/Mexico_City (UTC-6) time. The expires_after_days parameter can be set from 1 to 7 days. The default is 3 days.

[payment method options](/api/checkout/sessions/create#create_checkout_session-payment_method_options-oxxo-expires_after_days)

After submitting the Checkout form successfully, the customer is redirected to the hosted_voucher_url. The customer can find the barcode or print the OXXO voucher from the hosted voucher page. You can locate the hosted_voucher_url in payment_intent.next_action.oxxo_display_details.

[payment_intent.next_action.oxxo_display_details](/api/payment_intents/object#payment_intent_object-next_action-oxxo_display_details-hosted_voucher_url)

Stripe allows customization of customer-facing UIs on the Branding Settings page. The following brand settings can be applied to the voucher:

[Branding Settings](https://dashboard.stripe.com/account/branding)

- Icon—your brand image and public business name

- Accent color—used as the color of Print button

- Brand color—used as the background color

Because OXXO is a delayed notification payment method, you need to use a method such as webhooks to monitor the payment status and handle order fulfillment. Learn more about setting up webhooks and fulfilling orders.

[webhooks](/webhooks)

[setting up webhooks and fulfilling orders](/payments/checkout/fulfill-orders)

The following events are sent when the payment status changes:

checkout.session.completed

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

The customer has successfully submitted the Checkout form. Stripe has generated the OXXO voucher.

You can choose to email the hosted_voucher_url to your customer in case they lose the OXXO voucher.

Wait for the customer to pay the OXXO voucher.

[checkout.session.async_payment_succeeded](/api/events/types#event_types-checkout.session.async_payment_succeeded)

[checkout.session.async_payment_failed](/api/events/types#event_types-checkout.session.async_payment_failed)

[Test your integration](#test-integration)

## Test your integration

When testing your Checkout integration, select OXXO as the payment method and click the Pay button.

{any_prefix}@{any_domain}

Simulates an OXXO voucher which a customer pays after 3 minutes and the payment_intent.succeeded webhook arrives after about 3 minutes. In production, this webhook arrives after 1 business day.

Example: fulano@test.com

{any_prefix}succeed_immediately@{any_domain}

Simulates an OXXO voucher which a customer pays immediately and the payment_intent.succeeded webhook arrives within several seconds. In production, this webhook arrives after 1 business day.

Example: succeed_immediately@test.com

{any_prefix}expire_immediately@{any_domain}

Simulates an OXXO voucher which expires before a customer pays and the payment_intent.payment_failed webhook arrives within several seconds.

The expires_after field in next_action.oxxo_display_details is set to the current time regardless of what the expires_after_days parameter in payment method options is set to.

[next_action.oxxo_display_details](/api/payment_intents/object#payment_intent_object-next_action-oxxo_display_details-expires_after)

[payment method options](/api/payment_intents/create#create_payment_intent-payment_method_options-oxxo-expires_after_days)

Example: expire_immediately@test.com

{any_prefix}expire_with_delay@{any_domain}

Simulates an OXXO voucher which expires before a customer pays and the payment_intent.payment_failed webhook arrives after about 3 minutes.

The expires_after field in next_action.oxxo_display_details is set to 3 minutes in the future regardless of what the expires_after_days parameter in payment method options is set to.

[next_action.oxxo_display_details](/api/payment_intents/object#payment_intent_object-next_action-oxxo_display_details-expires_after)

[payment method options](/api/payment_intents/create#create_payment_intent-payment_method_options-oxxo-expires_after_days)

Example: expire_with_delay@test.com

{any_prefix}fill_never@{any_domain}

Simulates an OXXO voucher which expires before a customer pays and the payment_intent.payment_failed webhook arrives after 1 business day and 2 calendar days. In production, this webhook arrives at the same time as in testmode.

Example: fill_never@test.com

[OptionalSend payment instruction emails](#instruction-emails)

## OptionalSend payment instruction emails

## See also

- After the Payment

[After the Payment](/payments/checkout/fulfill-orders)

- Customizing Checkout

[Customizing Checkout](/payments/checkout/customization)
