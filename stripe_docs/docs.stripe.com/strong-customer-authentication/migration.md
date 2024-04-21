# Update your integration for SCA

Updating your integration to support Strong Customer Authentication consists of the following steps:

[Strong Customer Authentication](/strong-customer-authentication)

- Identify your payment flow

- Determine your integration path

- Implement the new integration path

- Test dynamic authentication

Start updating your integration today. After your integration is live, 3D Secure authentication is displayed when required by SCA.

[3D Secure](/payments/3d-secure)

## 1. Identify your payment flow

First, identify the payment flow that most closely matches your business. Read more about various flows to design a payment flow for SCA.

[design a payment flow for SCA](https://stripe.com/guides/sca-payment-flows)

[E-commerce](https://stripe.com/guides/sca-payment-flows#e-commerce)

[Gym membership](https://stripe.com/guides/sca-payment-flows#gym-membership)

[utility bill](https://stripe.com/guides/sca-payment-flows#utility-bill)

[separate authorize and capture](/payments/place-a-hold-on-a-payment-method)

[Ridesharing](https://stripe.com/guides/sca-payment-flows#ridesharing)

[Crowdfunding](https://stripe.com/guides/sca-payment-flows#crowdfunding)

[car rental](https://stripe.com/guides/sca-payment-flows#car-rental)

## 2. Determine your integration path

Choose an integration option based on your payment flow below:

[One-time payments](#one-time)

## One-time payments

For one-time payments, you can complete the full integration today.

Get prebuilt, conversion-optimized checkout flows with minimal code. Choose this option if you prefer a low-maintenance integration. For this payment flow, you can complete the full integration, and handling exemptions doesn’t require any additional work.

- See how to integrate Stripe Checkout to learn more.

[how to integrate Stripe Checkout](/payments/accept-a-payment?integration=checkout)

Build dynamic payment flows and custom checkout pages by migrating to the Payment Intents API with one of our client libraries:

- Stripe.js & Elements

[Stripe.js & Elements](/payments/payment-intents/migration)

- Stripe iOS SDK

[Stripe iOS SDK](/payments/accept-a-payment?platform=ios#setup-client-side)

- Stripe Android SDK

[Stripe Android SDK](/payments/accept-a-payment?platform=android#setup-client-side)

For this payment flow, you can complete the full integration, and handling exemptions requires no additional work.

- See how to use the Payment Intents API to learn more.

[how to use the Payment Intents API](/payments/payment-intents)

[Recurring payments](#recurring)

## Recurring payments

SCA requires customers to complete 3D Secure for some payments. When this step is required by the bank, the customer must be online to complete authentication. ​​This introduces complexity for businesses that save cards and charge them later when the customer is no longer on the website or application and can’t complete authentication. This is also known as off-session payments. Examples of this include fixed-amount subscriptions, metered-billing subscriptions, crowdfunding campaigns, and car rentals.

[SCA](/strong-customer-authentication)

[3D Secure](/payments/3d-secure)

[fixed-amount subscriptions](https://stripe.com/guides/sca-payment-flows#gym-membership)

[metered-billing subscriptions](https://stripe.com/guides/sca-payment-flows#utility-bill)

[crowdfunding campaigns](https://stripe.com/guides/sca-payment-flows#crowdfunding)

[car rentals](https://stripe.com/guides/sca-payment-flows#car-rental)

Stripe products and APIs now allow merchants to meet SCA requirements for off-session payments:

- Mandate collection. A mandate represents the agreement you have with the customer on how you plan to use their card in the future. In your checkout flow, add some consent text. State that by completing checkout, the customer consents to your initiation of payment on their behalf. State the anticipated frequency of payments. Explain how the amount of the payments will be determined.

Mandate collection. A mandate represents the agreement you have with the customer on how you plan to use their card in the future. In your checkout flow, add some consent text. State that by completing checkout, the customer consents to your initiation of payment on their behalf. State the anticipated frequency of payments. Explain how the amount of the payments will be determined.

- Strong authentication of the first transaction. Merchants are required to authenticate the customer when the mandate is set up. This can either be done by the first payment with the card or when saving the card to a customer without making an initial payment.

Strong authentication of the first transaction. Merchants are required to authenticate the customer when the mandate is set up. This can either be done by the first payment with the card or when saving the card to a customer without making an initial payment.

- Flagging subsequent transactions. Any payment made with a saved card when a user is off-session must be marked accordingly, with reference to the first authenticated transaction. Stripe handles this for you.

Flagging subsequent transactions. Any payment made with a saved card when a user is off-session must be marked accordingly, with reference to the first authenticated transaction. Stripe handles this for you.

By updating your payments integration to use these new APIs and flows, Stripe can request exemptions such as fixed-amount subscriptions and merchant-initiated transactions to process later payments made with a saved card. However, banks can decide to reject a request for exemption. Build a way to notify customers that they need to return to your application and complete authentication if required.

[fixed-amount subscriptions](https://stripe.com/guides/strong-customer-authentication#fixed-amount-subscriptions)

[merchant-initiated transactions](https://stripe.com/guides/strong-customer-authentication#merchant-initiated-transactions-including-variable-subscriptions)

[a way to notify customers](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)

Checkout is a prebuilt checkout page that lets you collect payments and manage simple subscriptions with a single integration.

[subscriptions](/billing/subscriptions/creating)

- See how to build subscriptions to learn more.

[how to build subscriptions](/billing/subscriptions/build-subscriptions)

Take advantage of automated tools to protect your revenue and scale your business. Build your own custom checkout experience.

- Update your client-side integration to save and reuse cards.

[save and reuse cards](/payments/save-and-reuse)

- Then, implement SCA-changes for Stripe Billing.

[implement SCA-changes for Stripe Billing](/billing/migration/strong-customer-authentication)

Build your own off-session payments logic and handle getting users back on-session to complete re-authentication as needed. While this approach takes more work than using Stripe Billing, it provides more flexibility.

There are three parts to building an off-session payment flow:

- Save a card to a customer. You can save a card to a customer in a checkout flow (as the customer is making a payment) with the Payment Intents API, or outside of the checkout flow with the Setup Intents API.  You can also use Stripe Checkout to save cards to a customer in a checkout flow or outside of the checkout flow.

[in a checkout flow](/payments/save-during-payment)

[outside of the checkout flow](/payments/save-and-reuse)

[in a checkout flow](/payments/checkout/customization)

[outside of the checkout flow](/payments/save-and-reuse?platform=checkout)

- Use a saved card to make a payment. Once you have cards saved to a customer, you can make both on-session or off-session payments.

[off-session payments](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)

- Build a recovery flow. While Stripe requests exemptions to reduce the need for customer reauthentication, there is always a risk that the cardholder’s bank will reject the exemption request. You should always build a recovery flow to bring a customer back on-session in case they need to authenticate again.

[recovery flow](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)

[Payments with separate authorize and capture within 7 days](#separate-auth-capture)

## Payments with separate authorize and capture within 7 days

For payments with separate authorize and capture, you can complete the full integration today.

Get prebuilt, conversion-optimized checkout flows with minimal code. Choose this option if you prefer a low-maintenance integration. For this payment flow, you can complete the full integration today, and no additional work will be needed to handle exemptions.Use Stripe Checkout with separate auth and capture

Use Stripe Checkout with separate auth and capture

[Use Stripe Checkout with separate auth and capture](/payments/accept-a-payment?integration=checkout)

Build dynamic payment flows and custom checkout pages by migrating to the Payment Intents API with one of our client libraries:

- Stripe.js & Elements

[Stripe.js & Elements](/payments/payment-intents/migration)

- Stripe iOS SDK

[Stripe iOS SDK](/payments/accept-a-payment?platform=ios#setup-client-side)

- Stripe Android SDK

[Stripe Android SDK](/payments/accept-a-payment?platform=android#setup-client-side)

For this payment flow, you can complete the full integration, and handling exemptions requires no additional work.

- See how to use the Payment Intents API to learn more.

[how to use the Payment Intents API](/payments/payment-intents)

[Payment captured more than seven days after authorization](#deferred-auth)

## Payment captured more than seven days after authorization

SCA requires customers to complete 3D Secure for some payments. When this step is required by the bank, the customer must be online to complete authentication. ​​This introduces complexity for businesses that save cards and charge them later when the customer is no longer on the website or application and can’t complete authentication. This is also known as off-session payments. Examples of this include fixed-amount subscriptions, metered-billing subscriptions, crowdfunding campaigns, and car rentals.

[SCA](/strong-customer-authentication)

[3D Secure](/payments/3d-secure)

[fixed-amount subscriptions](https://stripe.com/guides/sca-payment-flows#gym-membership)

[metered-billing subscriptions](https://stripe.com/guides/sca-payment-flows#utility-bill)

[crowdfunding campaigns](https://stripe.com/guides/sca-payment-flows#crowdfunding)

[car rentals](https://stripe.com/guides/sca-payment-flows#car-rental)

Stripe products and APIs now allow merchants to meet SCA requirements for off-session payments:

- Mandate collection. A mandate represents the agreement you have with the customer on how you plan to use their card in the future. In your checkout flow, add some consent text. State that by completing checkout, the customer consents to your initiation of payment on their behalf. State the anticipated frequency of payments. Explain how the amount of the payments will be determined.

Mandate collection. A mandate represents the agreement you have with the customer on how you plan to use their card in the future. In your checkout flow, add some consent text. State that by completing checkout, the customer consents to your initiation of payment on their behalf. State the anticipated frequency of payments. Explain how the amount of the payments will be determined.

- Strong authentication of the first transaction. Merchants are required to authenticate the customer when the mandate is set up. This can either be done by the first payment with the card or when saving the card to a customer without making an initial payment.

Strong authentication of the first transaction. Merchants are required to authenticate the customer when the mandate is set up. This can either be done by the first payment with the card or when saving the card to a customer without making an initial payment.

- Flagging subsequent transactions. Any payment made with a saved card when a user is off-session must be marked accordingly, with reference to the first authenticated transaction. Stripe handles this for you.

Flagging subsequent transactions. Any payment made with a saved card when a user is off-session must be marked accordingly, with reference to the first authenticated transaction. Stripe handles this for you.

By updating your payments integration to use these new APIs and flows, Stripe can request exemptions such as fixed-amount subscriptions and merchant-initiated transactions to process later payments made with a saved card. However, banks can decide to reject a request for exemption. Build a way to notify customers that they need to return to your application and complete authentication if required.

[fixed-amount subscriptions](https://stripe.com/guides/strong-customer-authentication#fixed-amount-subscriptions)

[merchant-initiated transactions](https://stripe.com/guides/strong-customer-authentication#merchant-initiated-transactions-including-variable-subscriptions)

[a way to notify customers](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)

Build your own off-session payments logic and handle getting users back on-session to complete re-authentication as needed. While this approach takes more work than using Stripe Billing, it provides more flexibility.

There are three parts to building an off-session payment flow:

- Save a card to a customer. You can save a card to a customer in a checkout flow (as the customer is making a payment) with the Payment Intents API, or outside of the checkout flow with the Setup Intents API.  You can also use Stripe Checkout to save cards to a customer in a checkout flow or outside of the checkout flow.

[in a checkout flow](/payments/save-during-payment)

[outside of the checkout flow](/payments/save-and-reuse)

[in a checkout flow](/payments/checkout/customization)

[outside of the checkout flow](/payments/save-and-reuse?platform=checkout)

- Use a saved card to make a payment. Once you have cards saved to a customer, you can make both on-session or off-session payments.

[off-session payments](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)

- Build a recovery flow. While Stripe requests exemptions to reduce the need for customer reauthentication, there is always a risk that the cardholder’s bank will reject the exemption request. You should always build a recovery flow to bring a customer back on-session in case they need to authenticate again.

[recovery flow](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)

[Other off-session payments](#other-off-session)

## Other off-session payments

SCA requires customers to complete 3D Secure for some payments. When this step is required by the bank, the customer must be online to complete authentication. ​​This introduces complexity for businesses that save cards and charge them later when the customer is no longer on the website or application and can’t complete authentication. This is also known as off-session payments. Examples of this include fixed-amount subscriptions, metered-billing subscriptions, crowdfunding campaigns, and car rentals.

[SCA](/strong-customer-authentication)

[3D Secure](/payments/3d-secure)

[fixed-amount subscriptions](https://stripe.com/guides/sca-payment-flows#gym-membership)

[metered-billing subscriptions](https://stripe.com/guides/sca-payment-flows#utility-bill)

[crowdfunding campaigns](https://stripe.com/guides/sca-payment-flows#crowdfunding)

[car rentals](https://stripe.com/guides/sca-payment-flows#car-rental)

Stripe products and APIs now allow merchants to meet SCA requirements for off-session payments:

- Mandate collection. A mandate represents the agreement you have with the customer on how you plan to use their card in the future. In your checkout flow, add some consent text. State that by completing checkout, the customer consents to your initiation of payment on their behalf. State the anticipated frequency of payments. Explain how the amount of the payments will be determined.

Mandate collection. A mandate represents the agreement you have with the customer on how you plan to use their card in the future. In your checkout flow, add some consent text. State that by completing checkout, the customer consents to your initiation of payment on their behalf. State the anticipated frequency of payments. Explain how the amount of the payments will be determined.

- Strong authentication of the first transaction. Merchants are required to authenticate the customer when the mandate is set up. This can either be done by the first payment with the card or when saving the card to a customer without making an initial payment.

Strong authentication of the first transaction. Merchants are required to authenticate the customer when the mandate is set up. This can either be done by the first payment with the card or when saving the card to a customer without making an initial payment.

- Flagging subsequent transactions. Any payment made with a saved card when a user is off-session must be marked accordingly, with reference to the first authenticated transaction. Stripe handles this for you.

Flagging subsequent transactions. Any payment made with a saved card when a user is off-session must be marked accordingly, with reference to the first authenticated transaction. Stripe handles this for you.

By updating your payments integration to use these new APIs and flows, Stripe can request exemptions such as fixed-amount subscriptions and merchant-initiated transactions to process later payments made with a saved card. However, banks can decide to reject a request for exemption. Build a way to notify customers that they need to return to your application and complete authentication if required.

[fixed-amount subscriptions](https://stripe.com/guides/strong-customer-authentication#fixed-amount-subscriptions)

[merchant-initiated transactions](https://stripe.com/guides/strong-customer-authentication#merchant-initiated-transactions-including-variable-subscriptions)

[a way to notify customers](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)

Build your own off-session payments logic and handle getting users back on-session to complete re-authentication as needed. While this approach takes more work than using Stripe Billing, it provides more flexibility.

There are three parts to building an off-session payment flow:

- Save a card to a customer. You can save a card to a customer in a checkout flow (as the customer is making a payment) with the Payment Intents API, or outside of the checkout flow with the Setup Intents API.  You can also use Stripe Checkout to save cards to a customer in a checkout flow or outside of the checkout flow.

[in a checkout flow](/payments/save-during-payment)

[outside of the checkout flow](/payments/save-and-reuse)

[in a checkout flow](/payments/checkout/customization)

[outside of the checkout flow](/payments/save-and-reuse?platform=checkout)

- Use a saved card to make a payment. Once you have cards saved to a customer, you can make both on-session or off-session payments.

[off-session payments](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)

- Build a recovery flow. While Stripe requests exemptions to reduce the need for customer reauthentication, there is always a risk that the cardholder’s bank will reject the exemption request. You should always build a recovery flow to bring a customer back on-session in case they need to authenticate again.

[recovery flow](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)

If you don’t use Stripe.js, the legacy version of Checkout, or our mobile SDKs to collect payment details, contact support or connect with our sales team.

[contact support](https://stripe.com/contact)

[connect with our sales team](https://stripe.com/contact/sales)

## 3. Implement the new integration path

You need to make server-side and client-side changes.

Use the Payment Intents API to create a payment. A PaymentIntent tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by SCA.

[Payment Intents API](/payments/payment-intents)

[PaymentIntent](/api/payment_intents/object)

Follow the migration guide to learn how to migrate from the Charges API to the Payment Intents API.

[migration guide](/payments/payment-intents/migration)

In order to dynamically display 3D Secure authentication for card payments, client-side changes are also required alongside server-side changes for the Payment Intents API.

[3D Secure](/payments/3d-secure)

Follow the guides to learn how to use the Payment Intents API with Stripe.js & Elements, iOS, and Android.

[Stripe.js & Elements](/payments/accept-a-payment?platform=web)

[iOS](/payments/accept-a-payment?platform=ios)

[Android](/payments/accept-a-payment?platform=android)

Follow the guides to integrate Checkout for one-time and subscriptions.

[one-time](/payments/accept-a-payment?integration=checkout)

[subscriptions](/billing/subscriptions/build-subscriptions)

## 4. Test dynamic authentication

To verify that your updated integration handles 3D Secure correctly, be sure to test both successful and unsuccessful authentication flows, using the regulatory test cards.

[regulatory test cards](/testing#regulatory-cards)

By default, 3D Secure authentication is only shown when the customer’s bank requires it, so your checkout conversion isn’t negatively affected. As of September 14, 2019, your updated integration displays the 3D Secure authentication flow automatically whenever required by SCA.

## See also

- Stripe Checkout Overview

[Stripe Checkout Overview](/payments/checkout)

- Payment Intents Overview

[Payment Intents Overview](/payments/payment-intents)

- Payment Intents Migration Guide

[Payment Intents Migration Guide](/payments/payment-intents/migration)
