# SCA migration guide for Connect platforms

Strong Customer Authentication applies to businesses based in the European Economic Area (EEA) that accept online payments from customers located in the EEA. Many card payments require additional authentication through 3D Secure. As of September 14, 2019, transactions that don’t follow the new authentication guidelines may be declined by a customer’s bank.

[Strong Customer Authentication](/strong-customer-authentication)

[European Economic Area](https://en.wikipedia.org/wiki/European_Economic_Area)

[3D Secure](/payments/3d-secure)

You need to update your platform if you create any of the following charges:

- Direct charges on a connected account based in the EEA.

[Direct charges](/connect/direct-charges)

- Destination charges if the on_behalf_of parameter is set and specifies a connected account based in the EEA.

[Destination charges](/connect/destination-charges)

- Separate charges and transfers if your platform is based in the EEA or if the on_behalf_of parameter is set and specifies a connected account based in the EEA.

[Separate charges and transfers](/connect/separate-charges-and-transfers)

[Choose an SCA-ready integration](#choose-integration)

## Choose an SCA-ready integration

You need to update your Stripe integration to meet SCA requirements. For example, SCA requires off-session payments to be authenticated when customers enter payment details, and subsequent off-session payments may require notifying the customer to return to the application to re-authenticate. Refer to the SCA migration guide to review the integration paths for Stripe Checkout, Stripe Billing, and the Payment Intents API.

[SCA migration guide](/strong-customer-authentication/migration#step-1)

[Payment Intents API](/payments/payment-intents)

Choose Stripe Checkout if it supports the features your integration requires. Checkout is a hosted payment page that can be branded by businesses, supports recurring subscriptions, and is the easiest way to provide SCA support to your connected accounts. It supports creating direct charges and destination charges for Connect.

[Stripe Checkout](/payments/checkout)

[subscriptions](/billing/subscriptions/creating)

[creating direct charges and destination charges](/connect/creating-a-payments-page)

[Connect](/connect)

If you want to build a custom payments experience, use the Payment Intents API as the legacy Charges API isn’t SCA-ready. The Payment Intents API supports the same set of Connect features as the Charges API.

[Payment Intents API](/payments/payment-intents)

[Examine Connect-specific changes](#examine-connect-specific-changes)

## Examine Connect-specific changes

If you’re using the destination, destination[account], or destination[amount] parameters with the Charges API, note that these parameters have been replaced with transfer_data[destination] and transfer_data[amount] in both the Charges and the Payment Intents APIs. See the following table for more information.

[transfer_data[destination]](/api/payment_intents/object#payment_intent_object-transfer_data-destination)

[transfer_data[destination]](/api/payment_intents/object#payment_intent_object-transfer_data-destination)

[on_behalf_of](/api/payment_intents/object#payment_intent_object-on_behalf_of)

[application_fee_amount](/api/payment_intents/object#payment_intent_object-application_fee_amount)

[transfer_data[amount]](/api/payment_intents/object#payment_intent_object-transfer_data)

Stripe Checkout and the Payment Intents API triggers dynamic 3D Secure authentication based on Radar rules. With Connect, the rules you create only apply to payments created on the platform account. Payments created directly on the connected account are subject to the connected account’s rules. Configure your default rules and test your integration with 3D Secure test cards.

[dynamic 3D Secure authentication](/payments/3d-secure/authentication-flow#three-ds-radar)

[Radar rules](/radar/rules)

[created directly on the connected account](/connect/direct-charges)

[3D Secure test cards](/payments/3d-secure/authentication-flow#three-ds-cards)

Under SCA, authentication is required when saving a card in order to collect customer permission and qualify for off-session exemptions for subsequent off-session payments. To reduce the rate of customers having to authenticate their payment method, update your integration to use the off-session API.

[off-session exemptions](https://stripe.com/guides/strong-customer-authentication#merchant-initiated-transactions-including-variable-subscriptions)

[update your integration to use the off-session API](/strong-customer-authentication/migration#recurring)

If you clone saved payment methods to reuse across multiple connected accounts, note that sharing a payment method with a connected account automatically shares customer permission as well. This allows the platform to make off-session payments on any of their connected accounts without requiring the customer to authenticate their payment method again.

[clone saved payment methods](/connect/cloning-customers-across-accounts)

[Determine whether connected accounts need to make changes](#connected-account-changes)

## Determine whether connected accounts need to make changes

In most cases, once you update your payments integration for SCA, your connected accounts don’t have to do any additional work.

If you provide your own payments API to your connected accounts in addition to or on top of Stripe’s API, your connected accounts may need to make changes to continue accepting payments on your platform. For example, if you run a subscriptions platform on Stripe in which your connected accounts pass payment information to you via your own API, and then you pass those payment details to Stripe’s API, you’ll need to ensure both APIs are SCA-ready. If this is the case for your platform, provide guidance to your connected accounts on any changes they need to make.

[Implement and test the new integration path](#implement-changes)

## Implement and test the new integration path

After you have identified your integration path and determined if your connected accounts need to make changes, follow the relevant migration guides for Stripe Checkout, Stripe Billing, or the Payment Intents API.

[Stripe Checkout](/payments/checkout/migration)

[Stripe Billing](/billing/migration/strong-customer-authentication)

[Payment Intents API](/payments/payment-intents/migration)

Once implementation is complete, configure your Dynamic 3D Secure rules to test your integration using 3D Secure test cards. Make sure to test both cases when the authentication is successful and unsuccessful.

[Dynamic 3D Secure rules](/payments/3d-secure/authentication-flow#three-ds-radar)

[3D Secure test cards](/payments/3d-secure/authentication-flow#three-ds-cards)

[Educate your connected accounts](#educate)

## Educate your connected accounts

Finally, inform your connected accounts about how SCA can affect them and when your platform will be SCA-ready, regardless of whether they need to make any changes.

[make any changes](#implement-changes)

In particular, provide them with the following information, tailored for your business:

Strong Customer Authentication (SCA) is a new European regulatory requirement to reduce fraud and make online payments more secure. Since SCA took effect September 14, 2019, online payments require additional customer authentication. Transactions that don’t adhere to the new guidelines may be declined by your customers’ banks. This regulation applies to transactions where both the business and the cardholder’s bank are located in the European Economic Area (EEA).

[Customer](/api/customers)

If you’d like, you can also send along the SCA video and guide.

[SCA video](https://stripe.com/payments/strong-customer-authentication)

[guide](https://stripe.com/guides/strong-customer-authentication)

If you’re not migrating to an SCA-ready solution, reach out to any of your connected accounts with significant business from European customers so they can move to a new solution before experiencing declines due to SCA.

If no action is required on their end, let your connected accounts know. Similarly, if action is required, provide them with instructions on the necessary changes.

SCA changes the checkout flow for card payments. Payments that require authentication ask for 3D Secure (often known by its brand names, “Verified by Visa” or “Mastercard SecureCode”), which typically adds an extra step in which the cardholder must provide additional information, such as a one-time passcode or biometric ID.

[3D Secure](/payments/3d-secure)
