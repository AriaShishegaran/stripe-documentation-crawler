# Fraud challengesBeta

Turn on fraud challenges to:

- Minimize accidental blocks on transactions that appear fraudulent, but are in fact legitimate

- Conduct additional verification on authorizations Stripe deems high risk

- Conduct additional verification on authorizations you determine require it

Fraud challenges allow your cardholders to retry non-fraudulent transactions that would otherwise be blocked by fraud controls. All cardholders with an associated phone number can use fraud challenges.

## Before you begin

- Make sure you’re collecting phone numbers for your cardholders

[phone numbers](/api/issuing/cardholders/object#issuing_cardholder_object-phone_number)

- Enable fraud challenges in your card issuing settings

[card issuing settings](https://dashboard.stripe.com/settings/issuing/authorizations)

## High-risk transactions

Stripe blocks transactions above a certain risk level. The risk level of a transaction is determined by the network you’re using. High-risk authorizations are identified by a value of suspected_fraud in the request_history.reason field, and won’t trigger issuing.authorization_request webhooks when declined.

[request_history.reason](/api/issuing/authorizations/object#issuing_authorization_object-request_history-reason)

[issuing.authorization_request webhooks](/issuing/controls/real-time-authorizations)

## Fraud challenge flow

Stripe starts sending fraud challenges on high-risk authorizations as soon as you enable the feature in your card issuing settings.

[card issuing settings](https://dashboard.stripe.com/settings/issuing/authorizations)

You can see fraud challenge activity with the Authorizations API. Declined authorizations that were fraud-challenged have a value in the fraud_challenges field. Subsequent authorizations that the cardholder verifies as genuine have a value of true in the verified_by_fraud_challenge field.

[Authorizations API](/api/issuing/authorizations)

[fraud_challenges](/api/issuing/authorizations/object#issuing_authorization_object-fraud_challenges)

[verified_by_fraud_challenge](/api/issuing/authorizations/object#issuing_authorization_object-verified_by_fraud_challenge)

The following shows an example of a fraud-challenged and declined authorization:

This example shows a subsequent authorization that has been verified by the cardholder:

Verified, genuine authorizations trigger issuing_authorization.request webhooks. If you use real-time authorization, consider verified_by_fraud_challenge when deciding whether to approve an authorization. If your cardholder has explicitly confirmed a transaction as genuine, we recommend that you don’t apply any of your own risk controls.

[real-time authorization](/issuing/controls/real-time-authorizations)

To use fraud challenges, make sure that:

- The phone number associated with your cardholder is valid and correct

- Existing transaction decline logic in any issuing_authorization.request webhook handler doesn’t conflict with fraud challenges

Your cardholders might receive a challenge and contact your company’s customer service to learn more. Make sure your internal teams are prepared to answer questions that they might receive from your customers about these challenges.

When a cardholder receives a fraud challenge, they can override the declined transaction by verifying that the suspicious transaction is legitimate and initiated by them. Fraud challenges are only available to cardholders with an associated phone number.

[phone number](/api/issuing/cardholders/object#issuing_cardholder_object-phone_number)

The cardholder verifies the override with a one-time SMS prompt with the following language:

Did you attempt a [amount] transaction at [merchant]? Reply YES if you did, or NO if not. Reply STOP to opt out

If the cardholder replies “YES”, they receive the following:

Thanks, please wait a moment and try again.

To complete the purchase, the cardholder needs to initiate the transaction a second time. After retrying, they won’t receive the SMS prompt, and Stripe will not block the transaction for being high-risk. If the cardholder instead replies “NO”, they receive the following:

This transaction was declined. We recommend you cancel your card and request a new one. Review your account for other suspicious transactions.

Cardholders can reply “STOP” to opt out of fraud challenges, and “START” to opt back in again.

## Trigger fraud challenges yourself

To send fraud challenges on authorizations that haven’t been blocked by Stripe, use real-time authorization webhooks. To trigger challenges in scenarios where you detect spending that appears suspicious and want additional verification (for example, a cardholder using their card out of the country), decline the issuing_authorization.request webhook and include the send_fraud_challenges field with the ["sms"] value.

[real-time authorization webhooks](/issuing/controls/real-time-authorizations)

Here’s an example of how to trigger a fraud challenge in a webhook response:

[https://youtu.be/rPR2aJ6XnAc](https://youtu.be/rPR2aJ6XnAc)

## Fraud challenges for Connect platforms

If you use Connect with Stripe Issuing, turning on fraud challenges enables it for all cardholders across all connected accounts.

[Connect](/issuing/connect)
