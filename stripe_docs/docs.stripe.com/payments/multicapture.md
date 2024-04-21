# Capture a payment multiple times

Multicapture allows you to capture a PaymentIntent multiple times for a single authorization, up to the full amount of the PaymentIntent. You can use it when you have orders with multiple shipments, and want to capture funds as you fulfill parts of the order.

[capture a PaymentIntent](/api/payment_intents/capture)

[amount of the PaymentIntent](/api/payment_intents/create#create_payment_intent-amount)

Multicapture is part of the functionality we offer to users on IC+ pricing. If you’re on blended Stripe pricing and want access to this feature, contact Stripe Support.

[IC+ pricing](https://support.stripe.com/questions/understanding-blended-interchange-pricing)

[Stripe Support](https://support.stripe.com/)

## Availability

When using multicapture, be aware of the following restrictions:

- Multicapture is only supported for online card payments

- Only available with Amex, Visa, Discover, and Mastercard

- Separate charges and transfers fund flows using source_transaction aren’t supported

[Separate charges and transfers](/connect/separate-charges-and-transfers)

[source_transaction](/api/transfers/create#create_transfer-source_transaction)

- Stripe allows you to capture up to 50 times for a single PaymentIntent

[PaymentIntent](/api/payment_intents)

Access to multicapture for Cartes Bancaires is a new feature, and currently limited to beta users. Reach out here to gain access.

[here](#)

## Best practices

Where sending separate shipments for one order, proactively notify your end customer with the details of each shipment to avoid inquiries and chargebacks from customers because of confusion with seeing multiple transactions on their bank statement. Here are some best practices for doing so:

- Inform the customer of the estimated delivery date and transaction amount for each shipment at the time of checkout, before purchase.

- Notify your customer upon each shipment, along with the transaction amount.

- Disclose your full refund and cancellation policy.

These best practices might be required under applicable network rules, depending on the network.

You’re responsible for your compliance with all applicable laws, regulations, and network rules when using multicapture. Consult the rules for the card networks that you want to use this feature with to make sure your sales comply with all applicable rules, which vary by network. For example, most card networks restrict multicapture usage to card-not-present transactions for the sale of goods that ship separately. Certain card networks permit multicapture for businesses based on their industry (for example, travel), while some don’t permit multicapture for installment or deposit workflows.

The information provided on this page relating to your compliance with these requirements is for your general guidance, and isn’t legal, tax, accounting, or other professional advice. Consult with a professional if you’re unsure about your obligations.

[Create and confirm an uncaptured PaymentIntent](#create-and-confirm)

## Create and confirm an uncaptured PaymentIntent

To indicate that you want separate authorization and capture, specify the capture_method as manual when creating the PaymentIntent. To learn more about separate authorization and capture, see how to place a hold on a payment method.

[capture_method](/api/payment_intents/create#create_payment_intent-capture_method)

[how to place a hold on a payment method](/payments/place-a-hold-on-a-payment-method)

Use the if_available or never parameters to request multicapture for this payment.

- if_available: The created PaymentIntent will allow multiple captures, if the payment method supports it.

if_available: The created PaymentIntent will allow multiple captures, if the payment method supports it.

- never: The created PaymentIntent won’t allow for multiple captures

never: The created PaymentIntent won’t allow for multiple captures

In the response, the payment_method_details.card.multicapture.status field on the latest_charge contains available or unavailable based on the customer’s payment method.

[latest_charge](/api/charges/object)

[Capture the PaymentIntent](#capture-payment-intent)

## Capture the PaymentIntent

For a PaymentIntent in a requires_capture state where multicapture is available, specifying the optional final_capture parameter to be false tells Stripe not to release the remaining uncaptured funds when calling the capture API. For example, if you confirm a 10 USD payment intent, capturing 7 USD with final_capture=false keeps the remaining 3 USD authorized.

[requires_capture state](/payments/paymentintents/lifecycle)

In the PI capture response, the amount_capturable and amount_received fields update accordingly.

[amount_capturable](/api/payment_intents/object#payment_intent_object-amount_capturable)

[amount_received](/api/payment_intents/object#payment_intent_object-amount_received)

[Final capture](#final-capture)

## Final capture

The PaymentIntent remains in a requires_capture state  until you do one of the following:

- Set final_capture to true

- Make a capture without the final_capture parameter (because final_capture defaults to true)

- The authorization window expires.

At this point, Stripe releases any remaining funds and transitions the PaymentIntent to a succeeded state.

In the PI capture response, the amount_capturable and amount_received fields will be updated accordingly.

[amount_capturable](/api/payment_intents/object#payment_intent_object-amount_capturable)

[amount_received](/api/payment_intents/object#payment_intent_object-amount_received)

Uncaptured PaymentIntents transition to canceled, while partially captured PaymentIntents transition to succeeded.

[OptionalRelease uncaptured funds](#close-payment)

## OptionalRelease uncaptured funds

[Test your integration](#test-your-integration)

## Test your integration

Use a Stripe test card with any CVC, postal code, and future expiration date to test multicapture payments.

[Refunds](#refunds)

## Refunds

For a PaymentIntent in requires_capture state, you can refund any number of times up to the total captured amount minus the total refunded amount, which is the amount_received - amount_refunded. The charge.refunded field transitions to true only when the final capture has been performed and the entire amount_received is refunded.

[refund](/api/refunds)

[amount_received](/api/payment_intents/object#payment_intent_object-amount_received)

[amount_refunded](/api/charges/object#charge_object-amount_refunded)

[charge.refunded](/api/charges/object#charge_object-refunded)

[amount_received](/api/payment_intents/object#payment_intent_object-amount_received)

Stripe doesn’t support partial refunds with refund_application_fee=true or reverse_transfer=true. Instead, you can perform partial fee refunds by manually performing partial fee refunds and transfer reversals using the application fee refund and transfer reversal endpoints. After using the application fee refund or transfer reversal endpoints, Stripe doesn’t support any further refunds with refund_application_fee=true or reverse_transfer=true respectively.

[refund_application_fee=true](/api/refunds/create#create_refund-refund_application_fee)

[reverse_transfer=true](/api/refunds/create#create_refund-reverse_transfer)

[application fee refund](/api/fee_refunds)

[transfer reversal](/api/transfer_reversals)

[Connect](#connect)

## Connect

Multicapture supports all Connect use cases, with the exception of Separate Charges and Transfers with the source_transaction parameter. The application_fee_amount and transfer_data[amount] parameters have some additional validations. Consider the following validations when implementing multicapture with Connect:

[Separate Charges and Transfers](/connect/separate-charges-and-transfers)

[source_transaction](/api/transfers/create#create_transfer-source_transaction)

[application_fee_amount](/api/payment_intents/capture#capture_payment_intent-application_fee_amount)

[transfer_data[amount]](/api/payment_intents/capture#capture_payment_intent-transfer_data-amount)

- Setting application_fee_amount or transfer_data[amount] on the first capture makes it required for all subsequent captures. Each application_fee_amount and transfer_data[amount] passed at capture time overrides the values passed in on PaymentIntent creation, confirmation, and update.

- Stripe doesn’t support partial refunds on multicapture payments with refund_application_fee=true or reverse_transfer=true. You can perform partial fee refunds or transfer reversals using the application fee refund and transfer reversal endpoints.

[application fee refund](/api/fee_refunds)

[transfer reversal](/api/transfer_reversals)

[Webhooks](#multicapture-webhooks)

## Webhooks

We send a charge.updated webhook each time you capture a payment.

[charge.updated](/api/events/types#event_types-charge.updated)

For example, on the first capture of a destination charge multicapture payment with an application_fee_amount, we update these fields from empty to non-empty values.

We send payment_intent.amount_capturable_updated on every capture, regardless of amount_to_capture and final_capture values.

[payment_intent.amount_capturable_updated](/api/events/types#event_types-payment_intent.amount_capturable_updated)

For example, if we capture 1 USD from a PaymentIntent with an amount of 10 USD, the PaymentIntent’s amount_capturable field updates to 9 USD.

We send a charge.captured event for final captures or at the end of the authorization window to reverse the authorization of the uncaptured amount. The captured field for a charge only becomes true after a final capture or authorization reversal.

[charge.captured](/api/events/types#event_types-charge.captured)

[captured](/api/charges/object#charge_object-captured)

For example, if we do a capture with amount=0 and final_capture=true, the captured attribute on the charge changes from false to true.

[captured](/api/charges/object#charge_object-captured)

Multicapture refund webhooks are no different than non-multicapture refund webhooks.

During each partial refund, we’ll send a charge.refunded event. For connected accounts, we’ll additionally send application_fee.refunded events when we refund application fees and transfer.reversed events when we reverse transfers.

[charge.refunded](/api/events/types#event_types-charge.refunded)

[application_fee.refunded](/api/events/types#event_types-application_fee.refunded)

[transfer.reversed](/api/events/types#event_types-transfer.reversed)
