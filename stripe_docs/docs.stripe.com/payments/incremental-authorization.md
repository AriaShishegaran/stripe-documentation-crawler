# Increment an authorization

Incremental authorization allows you to increase the authorized amount on a confirmed PaymentIntent before you capture it. Before capture, each incremental authorization appears on the credit card statement as an additional pending entry (for example, a 10 USD authorization incremented to 15 USD appears as separate 10 USD and 5 USD pending entries). After capture, the pending authorizations are removed, and the total captured amount appears as one final entry.

## Availability

When using incremental authorizations, be aware of the following restrictions:

- Not currently available if you and the cardholder are in a country with Strong Customer Authentication requirements or similar authentication requirements.

[Strong Customer Authentication](/strong-customer-authentication#impacted-businesses)

- Only available with Visa, Mastercard, or Discover.

- Certain card brands have merchant category restrictions (see below).

For learning more about incremental authorization and in-person payments made using Terminal, see Incremental Authorizations.

[Incremental Authorizations](/terminal/features/incremental-authorizations)

We offer incremental authorizations to users on IC+ pricing. If you’re on standard Stripe pricing and want access to this feature, learn more at support.stripe.com.

[IC+](https://support.stripe.com/questions/understanding-blended-interchange-pricing)

[support.stripe.com](https://support.stripe.com/)

Use incremental authorizations on payments that fulfill the criteria below. You can find your user category in the Dashboard.

[Dashboard](https://dashboard.stripe.com/settings/update/company/update)

Attempting to perform an incremental authorization on a payment that doesn’t fulfill the below criteria results in an error.

* Excludes MX users and JPY transactions for JP users

## Best practices

When using incremental authorization, proactively notify your end customer with the details of any authorizations for estimated amounts, which might be followed by incremental authorizations that increase those amounts. Here are some best practices for doing so:

- Disclose that an authorization is for an estimated amount and that subsequent authorization requests might follow at the time of checkout, before purchase.

- Base estimated amounts on a genuine estimate of what the total transaction amount will be.

These best practices might be required under applicable network rules, depending on the network.

You’re responsible for your compliance with all applicable laws, regulations, and network rules when using incremental authorization. Consult the network rules for the card networks that you plan to use this feature with to make sure your sales comply with applicable rules, which vary by network. For example, most card networks restrict how you can calculate estimated amounts included in the initial authorization, and prohibit the use of incremental authorizations for transactions where the transaction amount should be known at the time of authorization (for example, charges for recurring subscriptions).

The information provided on this page relating to your compliance with these requirements is for your general guidance, and isn’t legal, tax, accounting, or other professional advice. Consult with a professional if you’re unsure about your obligations.

[Create and confirm an uncaptured PaymentIntent](#confirm-payment-intent)

## Create and confirm an uncaptured PaymentIntent

You can use the request_incremental_authorization parameter to specify the PaymentIntents you plan to increment.

All PaymentIntents are incrementable by default. Use the if_available or never parameters to determine when to start incrementing a PaymentIntent:

- if_available: The created PaymentIntent allows for future increments based on incremental authorization support availability.

if_available: The created PaymentIntent allows for future increments based on incremental authorization support availability.

[incremental authorization support availability](#availability)

- never: The created PaymentIntent doesn’t allow for future increments.

never: The created PaymentIntent doesn’t allow for future increments.

You can only perform incremental authorizations on uncaptured payments after PaymentIntent confirmation. To adjust the amount of a payment before confirmation, use update method instead.

[PaymentIntent confirmation](/api/payment_intents/confirm)

[update method](/api/payment_intents/update)

In the PaymentIntent confirmation response, the payment_method_details field on the latest_charge contains available or unavailable based on the customer’s payment method and the availability criteria mentioned above, which determines whether a PaymentIntent is eligible for incremental authorization or not. (If you didn’t request incremental authorization in your PaymentIntent confirmation request, it will be unavailable.)

[payment_method_details](/api/charges/object#charge_object-payment_method_details)

[latest_charge](/api/charges/object)

[the availability criteria mentioned above](#availability)

[Perform an incremental authorization](#increment-authorization)

## Perform an incremental authorization

To increase the authorized amount on a PaymentIntent, use the increment_authorization endpoint and provide the updated total authorization amount to increment to, which must be greater than the original authorized amount. This attempts to authorize for a higher amount on your customer’s card. A single PaymentIntent can call this endpoint multiple times to further increase the authorized amount.

[increment_authorization](/api/payment_intents/increment_authorization)

[authorization amount](/api/payment_intents/increment_authorization#increment_authorization-amount)

You have a maximum of 10 incremental authorization attempts per PaymentIntent.

If the incremental authorization succeeds, it returns the PaymentIntent object with the updated amount. If the authorization fails, it returns a card_declined error instead. The PaymentIntent object remains capturable for the previously authorized amount. Any potential updates to other PaymentIntent fields (for example, application_fee_amount, transfer_data, metadata, description, and statement_descriptor) aren’t saved if the incremental authorization fails.

[card_declined](/error-codes#card-declined)

[application_fee_amount](/api/payment_intents/capture#capture_payment_intent-application_fee_amount)

[transfer_data](/api/payment_intents/capture#capture_payment_intent-transfer_data)

[metadata](/api/payment_intents/capture#capture_payment_intent-metadata)

[description](/api/payment_intents/capture#capture_payment_intent-description)

[statement_descriptor](/api/payment_intents/capture#capture_payment_intent-statement_descriptor)

The underlying Charge object for the PaymentIntent contains an amount_updates array field that’s appended with the results of the incremental authorization. It shows whether the authorization succeeded or failed, and any details associated with the result.

[amount_updates](/api/charges/object#charge_object-amount_updates)

Incremental authorization has a maximum cap of either +50 USD (or local equivalent) or +50% of the previously authorized amount (whichever is higher) for each individual increment. If you need access to higher limits, you can contact support.

[support](https://support.stripe.com/contact)

[Capture the PaymentIntent](#capture-payment-intent)

## Capture the PaymentIntent

Whether you increase the authorized amount on a PaymentIntent with an incremental authorization or not, you need to capture the funds before the initial authorization expires–incremental authorizations don’t extend the validity period. To capture the authorized amount on a PaymentIntent with prior incremental authorizations, use the capture endpoint as usual.

[the validity period](/payments/place-a-hold-on-a-payment-method)

[capture endpoint](/api/payment_intents/capture)

If the incremental authorization succeeds, it returns the captured PaymentIntent object with the updated amount. If the authorization fails, it returns a card_declined error instead. The PaymentIntent isn’t captured, but it remains capturable for the previously authorized amount. Any potential updates to other PaymentIntent fields (for example, application_fee_amount, transfer_data, metadata, description and statement_descriptor) aren’t saved if the incremental authorization fails.

[card_declined error](/error-codes#card-declined)

[application_fee_amount](/api/payment_intents/capture#capture_payment_intent-application_fee_amount)

[transfer_data](/api/payment_intents/capture#capture_payment_intent-transfer_data)

[metadata](/api/payment_intents/capture#capture_payment_intent-metadata)

[description](/api/payment_intents/capture#capture_payment_intent-description)

[statement_descriptor](/api/payment_intents/capture#capture_payment_intent-statement_descriptor)

[Test your integration](#test-your-integration)

## Test your integration

Use the incremental authorization Stripe test card with any CVC, postal code, and future expiration to trigger incremental authorization while in test mode:

- First create the PaymentIntent using the test card in the create and confirm PaymentIntent step above.

First create the PaymentIntent using the test card in the create and confirm PaymentIntent step above.

[create and confirm PaymentIntent step](#confirm-payment-intent)

- Perform the incremental authorization with the parameters specified in the perform an incremental authorization step above, and use the test card to trigger an incremental authorization.

Perform the incremental authorization with the parameters specified in the perform an incremental authorization step above, and use the test card to trigger an incremental authorization.

[perform an incremental authorization step](#increment-authorization)
