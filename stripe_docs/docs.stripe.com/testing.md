# Testing

Check out our no-code docs, use a prebuilt solution from our partner directory, or hire a Stripe-certified expert.

[no-code docs](/no-code)

[prebuilt solution](https://stripe.com/partners/directory)

[Stripe-certified expert](https://stripe.com/partners/directory?t=Consulting)

To confirm that your integration works correctly, simulate transactions without moving any money using special values in test mode.

[test mode](/test-mode)

Test cards let you simulate several scenarios:

- Successful payments by card brand or country

[card brand](#cards)

[country](#international-cards)

- Card errors due to declines, fraud, or invalid data

[declines](#declined-payments)

[fraud](#fraud-prevention)

[invalid data](#invalid-data)

- Disputes and refunds

[Disputes](#disputes)

[refunds](/testing#refunds)

- Authentication with 3D Secure and PINs

[3D Secure](#regulatory-cards)

[PINs](#terminal)

Testing non-card payments works similarly. Each payment method has its own special values. Because of rate limits, we don’t recommend using test mode to load-test your integration. Instead, see our documentation on load testing.

[Each payment method](#non-card-payments)

[rate limits](/testing#rate-limits)

[documentation on load testing](/rate-limits#load-testing)

## How to use test cards

Any time you work with a test card, use test API keys in all API calls. This is true whether you’re serving a payment form to test interactively or writing test code.

[test API keys](/keys#obtain-api-keys)

Don’t use real card details. The Stripe Services Agreement prohibits testing in live mode using real payment method details. Use your test API keys and the card numbers below.

[Stripe Services Agreement](https://stripe.com/legal/ssa#1-your-stripe-account)

When testing interactively, use a card number, such as 4242 4242 4242 4242.  Enter the card number in the Dashboard or in any payment form.

[4242 4242 4242 4242](/testing?testing-method=card-numbers#visa)

- Use a valid future date, such as 12/34.

- Use any three-digit CVC (four digits for American Express cards).

- Use any value you like for other form fields.

Testing a form interactively with the test card number 4242 4242 4242 4242

When writing test code, use a PaymentMethod such as pm_card_visa instead of a card number. We don’t recommend using card numbers directly in API calls or server-side code, even in test mode. If you do use them, your code might not be PCI-compliant when you go live. By default, a PaymentMethod isn’t attached to a Customer.

[pm_card_visa](/testing?testing-method=payment-methods#visa)

[Customer](/api/customers)

Most integrations don’t use Tokens anymore, but we make test Tokens such as tok_visa available if you need them.

[tok_visa](/testing?testing-method=tokens#visa)

When you’re ready to take your integration live, replace your test publishable and secret API keys with live ones. You can’t process live payments if your integration is still using your test API keys.

[API keys](/keys)

## Cards by brand

To simulate a successful payment, use test cards from the following list. The billing country for each test card is set to the United States. If you need to create test card payments using cards for other billing countries, use international test cards.

[international test cards](#international-cards)

Cross border fees are assessed based on the country of the card issuer. While each of the cards in this section use US as the billing country, cards where the issuer country isn’t the US (such as JCB and UnionPay) might be subject to a cross border fee, even in test mode.

Most Cartes Bancaires and eftpos cards are co-branded with either Visa or Mastercard. The test cards in the following table simulate successful payments with co-branded cards.

## Cards by country

To simulate successful payments from specific countries, use test cards from the following sections.

Strong Customer Authentication regulations require 3D Secure authentication for online payments within the European Economic Area. The test cards in this section simulate a payment that succeeds without authentication. We recommend also testing scenarios that involve authentication, using 3D Secure test cards.

[Strong Customer Authentication](/strong-customer-authentication)

[3D Secure](/payments/3d-secure)

[European Economic Area](https://en.wikipedia.org/wiki/European_Economic_Area)

[3D Secure test cards](/testing#regulatory-cards)

To test subscriptions that require mandates and pre-debit notifications, see India recurring payments.

[India recurring payments](/india-recurring-payments?integration=paymentIntents-setupIntents#testing)

## Declined payments

To test your integration’s error-handling logic by simulating payments that the issuer declines for various reasons, use test cards from this section. Using one of these cards results in a card error with the given error code and decline code.

[card error](/error-handling#payment-errors)

[error code](/error-codes)

[decline code](/declines/codes)

To simulate an incorrect CVC, you must provide one using any three-digit number. If you don’t provide a CVC, Stripe doesn’t perform the CVC check, so the check can’t fail.

[card_declined](/error-codes#card-declined)

[generic_decline](/declines/codes#generic_decline)

[card_declined](/error-codes#card-declined)

[insufficient_funds](/declines/codes#insufficient_funds)

[card_declined](/error-codes#card-declined)

[lost_card](/declines/codes#lost_card)

[card_declined](/error-codes#card-declined)

[stolen_card](/declines/codes#stolen_card)

[expired_card](/error-codes#expired-card)

[incorrect_cvc](/error-codes#incorrect-cvc)

[processing_error](/error-codes#processing-error)

[incorrect_number](/error-codes#incorrect-number)

[card_declined](/error-codes#card-declined)

[card_velocity_exceeded](/declines/codes#card_velocity_exceeded)

The cards in the previous table can’t be attached to a Customer object. To simulate a declined payment with a successfully attached card, use the next one.

[Customer](/api/customers)

## Fraud prevention

Stripe’s fraud prevention system, Radar, can block payments when they have a high risk level or fail verification checks. You can use the cards in this section to test your Radar settings. You can also use them to test how your integration responds to blocked payments.

Each card simulates specific risk factors. Your Radar settings determine which risk factors cause it to block a payment. Blocked payments result in card errors with an error code of fraud.

[card errors with an error code of fraud](/error-handling)

To simulate a failed CVC check, you must provide a CVC using any three-digit number. To simulate a failed postal code check, you must provide any valid postal code. If you don’t provide those values, Radar doesn’t perform the corresponding checks, so the checks can’t fail.

Always blocked

The charge has a risk level of “highest”

[risk level of “highest”](/radar/risk-evaluation#high-risk)

Radar always blocks it.

Highest risk

The charge has a risk level of “highest”

[risk level of “highest”](/radar/risk-evaluation#high-risk)

Radar might block it depending on your settings.

[depending on your settings](/radar/risk-settings)

Elevated risk

The charge has a risk level of “elevated”

[risk level of “elevated”](/radar/risk-evaluation#elevated-risk)

If you use Radar for Fraud Teams, Radar might queue it for review.

[queue it for review](/radar/reviews)

CVC check fails

If you provide a CVC number, the CVC check fails.

Radar might block it depending on your settings.

[depending on your settings.](/radar/rules#traditional-bank-checks)

Postal code check fails

If you provide a postal code, the postal code check fails.

Radar might block it depending on your settings.

[depending on your settings.](/radar/rules#traditional-bank-checks)

Line1 check fails

The address line 1 check fails.

The payment succeeds unless you block it with a custom Radar rule.

[block it with a custom Radar rule](/radar/rules/reference#post-authorization-attributes)

Address checks fail

The address postal code check and address line 1 check both fail.

Radar might block it depending on your settings.

[depending on your settings.](/radar/rules#traditional-bank-checks)

Address unavailable

The address postal code check and address line 1 check are both unavailable.

The payment succeeds unless you block it with a custom Radar rule.

[block it with a custom Radar rule](/radar/rules/reference#post-authorization-attributes)

## Invalid data

To test errors resulting from invalid data, provide invalid details. You don’t need a special test card for this. Any invalid value works. For instance:

- invalid_expiry_month: Use an invalid month, such as 13.

[invalid_expiry_month](/error-codes#invalid-expiry-month)

- invalid_expiry_year: Use a year up to 50 years in the past, such as 95.

[invalid_expiry_year](/error-codes#invalid-expiry-year)

- invalid_cvc: Use a two-digit number, such as 99.

[invalid_cvc](/error-codes#invalid-cvc)

- incorrect_number: Use a card number that fails the Luhn check, such as 4242424242424241.

[incorrect_number](/error-codes#incorrect-number)

[Luhn check](https://en.wikipedia.org/wiki/Luhn_algorithm)

## Disputes

To simulate a disputed transaction, use the test cards in this section. Then, to simulate winning or losing the dispute, provide winning or losing evidence.

[disputed transaction](/disputes)

[winning or losing evidence](#evidence)

[fraudulent](/disputes/categories)

[protected](/payments/3d-secure/authentication-flow#disputed-payments)

[product not received](/disputes/categories)

[isn’t protected](/payments/3d-secure/authentication-flow#disputed-payments)

[an inquiry](/disputes/how-disputes-work#inquiries)

[an early fraud warning](/disputes/how-disputes-work#early-fraud-warnings)

[multiple times](/disputes/how-disputes-work#multiple-disputes)

To simulate winning or losing the dispute, respond with one of the evidence values from the table below.

- If you respond using the API, pass the value from the table as uncategorized_text.

[respond using the API](/disputes/api)

[uncategorized_text](/api/disputes/update#update_dispute-evidence-uncategorized_text)

- If you respond in the Dashboard, enter the value from the table in the Additional information field. Then, click Submit evidence.

[respond in the Dashboard](/disputes/responding)

## Refunds

In live mode, refunds are asynchronous: a refund can appear to succeed and later fail, or can appear as pending at first and later succeed. To simulate refunds with those behaviors, use the test cards in this section. (With all other test cards, refunds succeed immediately and don’t change status after that.)

[webhook](/api/events/types#event_types-charge.refund.updated)

[webhook](/api/events/types#event_types-charge.refund.updated)

## Available balance

To send the funds from a test transaction directly to your available balance, use the test cards in this section. Other test cards send funds from a successful payment to your pending balance.

## 3D Secure authentication

3D Secure requires an additional layer of authentication for credit card transactions. The test cards in this section allow you to simulate triggering authentication in different payment flows.

Only cards in this section effectively test your 3D Secure integration by simulating defined 3DS behavior, such as a challenge flow or an unsupported card. Other Stripe testing cards might still trigger 3DS, but we return attempt_acknowledged to bypass the additional steps since 3DS testing isn’t the objective for those cards.

3D Secure redirects won’t occur for payments created directly in the Stripe Dashboard. Instead, use your integration’s own frontend or an API call.

To simulate payment flows that include authentication, use the test cards in this section. Some of these cards can also be set up for future payments, or have already been.

[set up](/payments/save-and-reuse)

[set it up](/payments/save-and-reuse)

[one-time](/payments/accept-a-payment?platform=web)

[on-session](/payments/save-during-payment#web-submit-payment)

[set up](/payments/save-and-reuse)

[one-time payments](/payments/accept-a-payment?platform=web)

[set up](/payments/save-and-reuse)

Stripe requests authentication when required by regulation or when triggered by your Radar rules or custom code. Even if authentication is requested, it can’t always be performed—for instance, the customer’s card might not be enrolled, or an error might occur. Use the test cards in this section to simulate various combinations of these factors.

All 3DS references indicate 3D Secure 2.

[3D Secure 2](https://stripe.com/guides/3d-secure-2)

In a mobile payment, several challenge flows for authentication—where the customer has to interact with prompts in the UI—are available. Use the test cards in this section to trigger a specific challenge flow for test purposes. These cards aren’t useful in browser-based payment forms or in API calls. In those environments, they work but don’t trigger any special behavior. Because they’re not useful in API calls, we don’t provide any PaymentMethod or Token values to test with.

## Payments with PINs

Use the test cards in this section to simulate successful in-person payments where a PIN is involved. There are many other options for testing in-person payments, including a simulated reader and physical test cards. See Test Stripe Terminal for more information.

[Test Stripe Terminal](/terminal/references/testing)

[cardholder_verification_method](/api/charges/object#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method)

[cardholder_verification_method](/api/charges/object#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method)

[cardholder_verification_method](/api/charges/object#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method)

[cardholder_verification_method](/api/charges/object#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method)

## Webhooks

To test webhooks, you have two options:

[webhooks](/webhooks)

- Perform actions in test mode that send legitimate events to your endpoint. For instance, to trigger the charge.succeeded event, you can use a test card that produces a successful charge.

[charge.succeeded](/api#event_types-charge.succeeded)

[test card that produces a successful charge](#cards)

- Trigger events using the Stripe CLI or using Stripe for Visual Studio Code.

[Trigger events using the Stripe CLI](/webhooks#test-webhook)

[using Stripe for Visual Studio Code](/stripe-vscode#webhooks)

## Rate limits

If your requests in test mode begin to receive 429 HTTP errors, make them less frequently. These errors come from our rate limiter, which is stricter in test mode than in live mode.

[rate limiter](/rate-limits)

We don’t recommend load testing your integration using the Stripe API in test mode. Because the load limiter is stricter in test mode, you might see errors that you wouldn’t see in production. See load testing for an alternative approach.

[load testing](/rate-limits#load-testing)

## Non-card payments

Any time you use a test non-card payment method, use test API keys in all API calls. This is true whether you’re serving a payment form you can test interactively or writing test code.

[test API keys](/keys#obtain-api-keys)

Different payment methods have different test procedures:

Learn how to test scenarios with instant verifications using Financial Connections.

[Financial Connections](/financial-connections/testing#web-how-to-use-test-accounts)

After you collect the bank account details and accept a mandate, send the mandate confirmation and microdeposit verification emails in test mode. To do this, provide an email in the payment_method_data.billing_details[email] field in the form of {any-prefix}+test_email@{any_domain} when you collect the payment method details.

[payment method details](#web-collect-details)

You need to activate your Stripe account before you can trigger these emails in Test mode.

[activate your Stripe account](/get-started/account/activate)

Stripe provides several test account numbers and corresponding tokens you can use to make sure your integration for manually-entered bank accounts is ready for production.

[PaymentIntent cancellation](/api/payment_intents/cancel)

Before test transactions can complete, you need to verify all test accounts that automatically succeed or fail the payment. To do so, use the test microdeposit amounts or descriptor codes below.

To mimic different scenarios, use these microdeposit amounts or 0.01 descriptor code values.

## Redirects

To test your integration’s redirect-handling logic by simulating a payment that uses a redirect flow (for example, iDEAL), use a supported payment method that requires redirects.

[requires redirects](/payments/payment-methods/integration-options#additional-api-supportability)

To create a test PaymentIntent that either succeeds or fails:

- Navigate to the payment methods settings in the Dashboard and enable a supported payment method by clicking Turn on in test mode.

[payment methods settings in the Dashboard](https://dashboard.stripe.com/settings/payment_methods)

- Collect payment details.

- Submit the payment to Stripe.

- Authorize or fail the test payment.

Make sure that the page (corresponding to return_url) on your website provides the status of the payment.

## See also

- Testing your Connect integration

[Testing your Connect integration](/connect/testing)

- Testing your Billing integration

[Testing your Billing integration](/billing/testing)

- Testing your Terminal integration

[Testing your Terminal integration](/terminal/references/testing)

- Load testing

[Load testing](/rate-limits#load-testing)
