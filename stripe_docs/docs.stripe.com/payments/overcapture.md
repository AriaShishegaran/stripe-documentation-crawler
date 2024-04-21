# Capture more than the authorized amount on a payment

Overcapture allows you to capture with an amount that’s higher than the authorized amount for a card payment. Unlike incremental authorizations, overcapture doesn’t result in additional authorizations with the card networks. When you overcapture a PaymentIntent, your customer won’t see any immediate updates on their credit card statement. After the captured amount settles, the initial pending authorization gets updated with the final captured amount.

[incremental authorizations](/payments/incremental-authorization)

## Availability

When using overcapture, be aware of the following restrictions:

- Only available with Visa, Mastercard, American Express, or Discover.

- Only eligible for online card payments. For in-person card payments see how to collect tips.

[collect tips](/terminal/features/collecting-tips/overview)

- Card brands limit the amount that you can overcapture (generally calculated as a percentage of the authorized amount), and impose additional constraints, including country, card type, and merchant category restrictions (see below).

We offer overcapture to users on IC+ pricing. If you’re on standard Stripe pricing and want access to this feature, learn more at support.stripe.com.

[IC+ pricing](https://support.stripe.com/questions/understanding-blended-interchange-pricing)

[support.stripe.com](https://support.stripe.com/)

* Excludes merchants in the European Economic Area (“EEA”) where the card is also issued in the EEA

** For cardholder-initiated transactions

*** Card must also be issued in the United States

**** The percent limit for debit and prepaid card payments is 20%

If you and the cardholder are in a country that has Strong Customer Authentication (SCA) requirements, keep in mind the limitations of overcapture availability.

- Under SCA requirements, you generally need to authenticate an amount that’s greater than or equal to the amount that you eventually capture. For this reason, you need to authenticate and authorize for the highest estimated amount that you plan to capture, rather than using overcapture as outlined elsewhere on this page. Subsequently, you can capture up to the full amount authenticated, depending on the total amount for the goods or services provided. If you find it necessary to capture an amount beyond the originally authorized and authenticated amount, you must cancel the original payment and create a new one with the correct amount. However, there are some exceptions to this requirement (see below).

- There are a number of transaction exemptions for SCA where overcapture might be permissible. For example, merchant-initiated transactions (MIT) where the customer isn’t physically present during the checkout flow are potentially exempt. See when to categorize a transaction as MIT.

[transaction exemptions](https://support.stripe.com/questions/transaction-exemptions-for-strong-customer-authentication-%28sca%29)

[when to categorize a transaction as MIT](https://support.stripe.com/questions/merchant-initiated-transactions-(mits)-when-to-categorize-a-transaction-as-mit)

You need to familiarize yourself with the complete documentation to gain a comprehensive understanding of overcapture and SCA requirements.  See our SCA guide for more information.

[SCA guide](https://stripe.com/guides/strong-customer-authentication)

You’re responsible for your compliance with all applicable laws, regulations, and network rules when using overcapture. Make sure to review the rules for the card networks that you plan to use this feature with to make sure your sales comply with the applicable rules, which vary by network. For example, some card networks don’t allow overcapture for transactions where the final transaction amount should be known at the time of authorization.

The information provided on this page relating to your compliance with these requirements is for your general guidance, and isn’t legal, tax, accounting, or other professional advice. Consult with a professional if you’re unsure about your obligations.

[Create and confirm an uncaptured PaymentIntent](#confirm-payment-intent)

## Create and confirm an uncaptured PaymentIntent

You can only perform overcapture on uncaptured payments after PaymentIntent confirmation. To indicate you want to separate the authorization and capture, specify the capture_method as manual when creating the PaymentIntent. To learn more about separate authorization and capture, see how to place a hold on a payment method.

[PaymentIntent confirmation](/api/payment_intents/confirm)

[capture_method](/api/payment_intents/create#create_payment_intent-capture_method)

[how to place a hold on a payment method](/payments/place-a-hold-on-a-payment-method)

You must specify the PaymentIntents you plan to overcapture by using if_available with the request_overcapture parameter.

[request_overcapture](/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-card-request_overcapture)

Look at the overcapture.status field on the latest_charge in the PaymentIntent confirmation response to determine if overcapture is available for the payment based on availability. If available, the maximum_amount_capturable field indicates the maximum amount capturable for the PaymentIntent. If unavailable, the maximum_amount_capturable is the amount authorized.

[overcapture.status](/api/charges/object#charge_object-payment_method_details-card-overcapture)

[latest_charge](/api/charges/object)

[availability](#availability)

[maximum_amount_capturable](/api/charges/object#charge_object-payment_method_details-card-overcapture-maximum_amount_capturable)

[Capture the PaymentIntent](#capture-payment-intent)

## Capture the PaymentIntent

To capture more than the currently authorized amount on a PaymentIntent, use the capture endpoint and provide an amount_to_capture up to the maximum_amount_capturable.

[capture](/api/payment_intents/capture)

[amount_to_capture](/api/payment_intents/capture#capture_payment_intent-amount_to_capture)

[maximum_amount_capturable](/api/charges/object#charge_object-payment_method_details-card-overcapture)

If you need to capture an amount larger than the maximum_amount_capturable, perform an incremental authorization to increase the authorized amount, where available.

[incremental authorization](/payments/incremental-authorization)

The amount_capturable and amount_received fields update accordingly in the PaymentIntent capture response for a successful overcapture. The captured PaymentIntent that returns has an updated amount to reflect the total monetary amount moved for this payment. Use the amount_authorized field on the associated Charge to reference the initial amount authorized for a successfully overcaptured payment.

[amount_capturable](/api/payment_intents/object#payment_intent_object-amount_capturable)

[amount_received](/api/payment_intents/object#payment_intent_object-amount_received)

[amount](/api/payment_intents/object#payment_intent_object-amount)

[amount_authorized](/api/charges/object#charge_object-payment_method_details-card-amount_authorized)

## Test your integration

Use any of the below Stripe test cards with any CVC and future expiration date to request and perform overcaptures while in test mode. If overcapture is available on payments for a given network in test mode, it is also available in live mode.
