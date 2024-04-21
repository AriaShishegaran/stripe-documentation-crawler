# Previous authorization agreements

If you’re affected by SCA, update your Stripe integration now, even if some of your payments can use previous authorization agreements. Stripe provides migration guides to help.

[update your Stripe integration](/strong-customer-authentication#preparing)

[migration guides](/strong-customer-authentication/migration)

## Eligibility

Strong Customer Authentication requires an additional step of customer authentication, but sometimes you collect payments when your customer isn’t actively using your application. Even if they authenticated in the past, SCA may require your customer to come back online and re-authenticate. To reduce friction in these off-session payments, Stripe APIs enable upfront authentication—so you can authenticate your customer on-session once and reuse the card off-session repeatedly. As of September 14, 2019, you need to use these APIs to reduce the chance of failed payments when reusing cards or creating subscriptions and invoices.

[Strong Customer Authentication](/strong-customer-authentication)

[reusing cards](/payments/save-and-reuse)

[creating subscriptions and invoices](/billing/migration/strong-customer-authentication)

However, you can use previous authorization agreements for off-session payments that meet the following criteria:

- Cards from EU customers saved before December 31, 2020

- Cards from UK customers saved before September 14, 2021

This means you don’t have to use Stripe’s new APIs to set up saved cards again, and your off-session payments can proceed normally—without re-authentication from customers.

## How it works

You can use previous authorization agreements for all off-session payments that meet both of these conditions, regardless of payment amount and frequency:

- You saved the card details before the eligibility cutoff

[eligibility](#eligibility)

- You explicitly tell Stripe the transaction is off-session

Stripe automatically looks for a transaction made with the card prior to the eligibility cutoff. If found, Stripe uses the previous authorization agreement for the current transaction. If the bank accepts the previous authorization agreement, the transaction is categorized as out of scope for SCA and can proceed without additional authentication.

If the bank declines the previous authorization agreement, it’s like any other PaymentIntent failing the confirmation step. The PaymentIntent’s status changes to requires_payment_method, and you have to notify your customer to complete the payment.

[status changes](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)

[requires_payment_method](/upgrades#2019-02-11)

[notify your customer to complete the payment](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)

## Saving cards after the eligibility period

Now that SCA has taken effect, save and reuse cards with the Payment Intents and Setup Intents APIs to qualify for off-session exemptions. You can also save cards using Stripe Checkout.

[save and reuse cards](/payments/save-and-reuse)

[Setup Intents APIs](/api/setup_intents)

[Stripe Checkout](/payments/save-and-reuse?platform=checkout)

## Preparing your saved cards for SCA

For Stripe to reuse authorization agreements, you need to use PaymentIntents and tell Stripe the payment is off-session.

[token](/saving-cards)

[source](/sources/cards)

[payment method](/payments/save-during-payment)

[off-session flag](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)

[SetupIntent](/payments/save-and-reuse)

[setup_future_usage](/api/payment_intents/create#create_payment_intent-setup_future_usage)

[off-session flag](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)

For subscriptions and invoices managed with Stripe Billing, refer to the Billing SCA guide.

[subscriptions](/billing/subscriptions/creating)

[invoices](/api/invoices)

[Billing SCA guide](/billing/migration/strong-customer-authentication#previous-agreements)

## See also

- Payment Intents Overview

[Payment Intents Overview](/payments/payment-intents)

- Payment Intents Migration Guide

[Payment Intents Migration Guide](/payments/payment-intents/migration)
