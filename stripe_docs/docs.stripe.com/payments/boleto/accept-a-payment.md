# Boleto payments

Stripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

[Accept a payment](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

[Subscription mode](/billing/subscriptions/payment-methods-setting)

[migrate to the dashboard](/payments/dashboard-payment-methods)

Boleto is a single use payment method where customers are required to take additional steps to complete their payment. Customers pay by using a Boleto voucher with a generated number either in ATMs, banks, bank portals or authorized agencies.

[single use](/payments/payment-methods#usage)

[take additional steps](/payments/payment-methods#customer-actions)

[Customers](/api/customers)

[Determine compatibility](#compatibility)

## Determine compatibility

Supported business locations: BR

Supported currencies: brl

Presentment currencies: brl

Payment mode: Yes

Setup mode: No

Subscription mode: No

A Checkout Session must satisfy all of the following conditions to support Boleto payments:

- Prices for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.

[Prices](/api/prices)

- You can only use one-time line items (recurring subscription plans are not supported).

[subscription](/billing/subscriptions/creating)

[Accept a payment](#accept-a-payment)

## Accept a payment

Build an integration to accept a payment with Checkout before using this guide.

[accept a payment](/payments/accept-a-payment?integration=checkout)

Use this guide to learn how to enable Boleto—it shows the differences between accepting a card payment and using Boleto.

When creating a new Checkout Session, you need to:

[Checkout Session](/api/checkout/sessions)

- Add boleto to the list of payment_method_types

- Make sure all your line_items use the brl currency.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

You can specify an optional expires_after_days parameter in the payment method options for your Session that sets the number of calendar days before a Boleto voucher expires. For example, if you create a Boleto voucher on Monday and you set expires_after_days to 2, the Boleto voucher expires on Wednesday at 23:59 America/Sao_Paulo (UTC-3) time. If you set it to 0, the Boleto voucher expires at the end of the day. The expires_after_days parameter can be set from 0 to 60 days. The default is 3 days. You can customize the default expiration days on your account in the Payment methods settings

[payment method options](/api/checkout/sessions/create#create_checkout_session-payment_method_options-boleto-expires_after_days)

[Payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

Unlike card payments, the customer won’t be redirected to the success_url with Boleto payment.

[success_url](/api/checkout/sessions/object#checkout_session_object-success_url)

After submitting the Checkout form successfully, the customer is redirected to the hosted_voucher_url. The customer can copy the Boleto number or download the voucher PDF from the hosted voucher page.

Stripe sends a payment_intent.requires_action event when a Boleto voucher is created successfully. If you need to email your customers the voucher link, you can locate the hosted_voucher_url in payment_intent.next_action.boleto_display_details. Learn more about how to monitor a PaymentIntent with webhooks.

[payment_intent.requires_action](/api/events/types#event_types-payment_intent.requires_action)

[payment_intent.next_action.boleto_display_details](/api/payment_intents/object#payment_intent_object-next_action-boleto_display_details-hosted_voucher_url)

[monitor a PaymentIntent with webhooks](/payments/payment-intents/verifying-status#webhooks)

Stripe allows customization of customer-facing UIs on the Branding Settings page. The following brand settings can be applied to the voucher:

[Branding Settings](https://dashboard.stripe.com/account/branding)

- Icon—your brand image and public business name

- Accent color—used as the color of the Copy Number button

- Brand color—used as the background color

Because Boleto is a delayed notification payment method, you need to use a method such as webhooks to monitor the payment status and handle order fulfillment. Learn more about setting up webhooks and fulfilling orders.

[webhooks](/webhooks)

[setting up webhooks and fulfilling orders](/payments/checkout/fulfill-orders)

The following events are sent when the payment status changes:

checkout.session.completed

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

The customer has successfully submitted the Checkout form. Stripe has generated the Boleto voucher.

You can choose to email the hosted_voucher_url to your customer in case they lose the Boleto voucher.

Wait for the customer to pay the Boleto.

[checkout.session.async_payment_succeeded](/api/events/types#event_types-checkout.session.async_payment_succeeded)

[checkout.session.async_payment_failed](/api/events/types#event_types-checkout.session.async_payment_failed)

[Test your integration](#test-integration)

## Test your integration

When testing your Checkout integration, select Boleto as the payment method and click the Pay button.

{any_prefix}@{any_domain}

Simulates a Boleto voucher which a customer pays after 3 minutes and the payment_intent.succeeded webhook arrives after about 3 minutes. In production, this webhook arrives 1 business day after a payment.

Example: fulaninho@example.com

{any_prefix}succeed_immediately@{any_domain}

Simulates a Boleto voucher which a customer pays immediately and the payment_intent.succeeded webhook arrives within several seconds. In production, this webhook arrives 1 business day after a payment.

Example: succeed_immediately@example.com

{any_prefix}expire_immediately@{any_domain}

Simulates a Boleto voucher which expires before a customer pays and the payment_intent.payment_failed webhook arrives within several seconds.

The expires_at field in next_action.boleto_display_details is set to the current time regardless of what the expires_after_days parameter in payment method options is set to.

[next_action.boleto_display_details](/api/payment_intents/object#payment_intent_object-next_action-boleto_display_details-expires_at)

[payment method options](/api/payment_intents/create#create_payment_intent-payment_method_options-boleto-expires_after_days)

Example: expire_immediately@example.com

{any_prefix}expire_with_delay@{any_domain}

Simulates a Boleto voucher which expires before a customer pays and the payment_intent.payment_failed webhook arrives after about 3 minutes.

The expires_at field in next_action.boleto_display_details is set to 3 minutes in the future regardless of what the expires_after_days parameter in payment method options is set to.

[next_action.boleto_display_details](/api/payment_intents/object#payment_intent_object-next_action-boleto_display_details-expires_at)

[payment method options](/api/payment_intents/create#create_payment_intent-payment_method_options-boleto-expires_after_days)

Example: expire_with_delay@example.com

{any_prefix}fill_never@{any_domain}

Simulates a Boleto voucher which never succeeds; it expires according to the expires_at field in next_action.boleto_display_details per the provided parameters in the payment method options and the payment_intent.payment_failed webhook arrives after that.

[next_action.boleto_display_details](/api/payment_intents/object#payment_intent_object-next_action-boleto_display_details-expires_at)

[payment method options](/api/payment_intents/create#create_payment_intent-payment_method_options-boleto-expires_after_days)

Example: fill_never@example.com

CPF 000.000.000-00

CNPJ 00.000.000/0000-00

In test mode, set tax_id to these values, so they bypass the tax ID validation.

[Handle refunds](#refunds)

## Handle refunds

Boleto payments can’t be refunded. Some merchants have created a separate process to credit their customers who reach out directly.

[Handle disputes](#disputes)

## Handle disputes

Boleto payments can’t be disputed by the customer.

[OptionalSend payment instruction emails](#instruction-emails)

## OptionalSend payment instruction emails

## See also

- After the Payment

[After the Payment](/payments/checkout/fulfill-orders)

- Customizing Checkout

[Customizing Checkout](/payments/checkout/customization)
