# Place an extended hold on an online card payment

Extended authorizations have a longer authorization validity period, which allows you to hold customer funds for longer. The default authorization validity period is 7 days, whereas extended validity periods can go up to 31 days depending on the card network. For more information about placing holds, see place a hold on a payment method.

[place a hold on a payment method](/payments/place-a-hold-on-a-payment-method)

## Availability

When using extended authorizations, be aware of the following restrictions:

- They’re only available with Visa, Mastercard, American Express, and Discover.

- Certain card brands have merchant category restrictions. Refer to the network availability table below.

- This page describes extended authorizations for online card payments. For in-person card payments using extended authorizations, refer to the Terminal documentation.

[Terminal documentation](/terminal/features/extended-authorizations)

- Checkout doesn’t support extended authorizations.

We offer extended authorizations to users on IC+ pricing. If you’re on blended Stripe pricing and want access to this feature, you learn more at support.stripe.com.

[IC+](https://support.stripe.com/questions/understanding-blended-interchange-pricing)

[support.stripe.com](https://support.stripe.com/)

Every card network has different rules that determine which payments have extended authorizations available, and how long they’re valid. The following table shows the validity windows and transaction types that extended authorization is available for using Visa, Mastercard, American Express, and Discover. However, we recommend that you rely on the capture_before field to confirm the validity window for any given payment because these rules can change without prior notice.

[capture_before field](/api/charges/object#charge_object-payment_method_details-card-capture_before)

* The specific extended authorization window for Visa is 29 days and 18 hours to allow time for clearing processes.** While your validity window is extended to 30 days, you must capture the authorized funds no later than the end of the duration of your customer’s stay or rental.

## Best Practices

Customers see their funds held longer when you use extended authorizations. Use clear statement descriptors to avoid increased disputes from unrecognized payments.

[statement descriptors](/get-started/account/statement-descriptors)

You’re responsible for your compliance with all applicable laws, regulations, and network rules when using extended authorization. Consult the network specifications for the card networks that you plan to accept using this feature with to make sure your sales are compliant with the applicable rules, which vary by network. For instance, for many networks extended validity windows are only for cases where you don’t know the final amount that you’ll capture at the time of authorization.

The information provided on this page relating to your compliance with these requirements is for your general guidance, and is not legal, tax, accounting, or other professional advice. Consult with a professional if you’re unsure about your obligations.

## Request an extended authorization

By default, an authorization for an online card payment is valid for 7 days. To increase the validity period, you can request an extended authorization by using if_available with the request_extended_authorization parameter.

[request_extended_authorization](/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-card-request_extended_authorization)

Rely on the capture_before field to confirm the validity window for a given payment. The validity window won’t change after the PaymentIntent is confirmed. To determine if the authorization is extended after confirming the PaymentIntent, look at the extended_authorization.status field on the associated Charge.

[capture_before field](/api/charges/object#charge_object-payment_method_details-card-capture_before)

[extended_authorization.status field](/api/charges/object#charge_object-payment_method_details-card-extended_authorization-status)

## Test your integration

Use any of the below Stripe test cards with any CVC and future expiration date to request extended authorizations while in test mode. If extended authorizations are available on payments for a given network in test mode, they’re also available in live mode.

## See also

- Place a hold on a payment method

[Place a hold on a payment method](/payments/place-a-hold-on-a-payment-method)
