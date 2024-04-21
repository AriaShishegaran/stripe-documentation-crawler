htmlFraud challenges | Stripe Documentation[Skip to content](#main-content)Fraud challenges[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcontrols%2Ffraud-challenges)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/issuing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcontrols%2Ffraud-challenges)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)
[Treasury](#)[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Issuing](/issuing)·[Home](/docs)[Banking as a service](/docs/financial-services)[Issuing cards](/docs/issuing)[Advanced fraud tools](/docs/issuing/controls/advanced-fraud-tools)# Fraud challengesBeta

Learn about fraud challenges, an additional layer of verification for authorizations.Turn on fraud challenges to:

- Minimize accidental blocks on transactions that appear fraudulent, but are in fact legitimate
- Conduct additional verification on authorizations Stripe deems high risk
- Conduct additional verification on authorizations you determine require it

Fraud challenges allow your cardholders to retry non-fraudulent transactions that would otherwise be blocked by fraud controls. All cardholders with an associated phone number can use fraud challenges.

## Before you begin

- Make sure you’re collecting[phone numbers](/api/issuing/cardholders/object#issuing_cardholder_object-phone_number)for your cardholders
- Enable fraud challenges in your[card issuing settings](https://dashboard.stripe.com/settings/issuing/authorizations)

## High-risk transactions

Stripe blocks transactions above a certain risk level. The risk level of a transaction is determined by the network you’re using. High-risk authorizations are identified by a value of suspected_fraud in the request_history.reason field, and won’t trigger issuing.authorization_request webhooks when declined.

## Fraud challenge flow

Stripe starts sending fraud challenges on high-risk authorizations as soon as you enable the feature in your card issuing settings.

You can see fraud challenge activity with the Authorizations API. Declined authorizations that were fraud-challenged have a value in the fraud_challenges field. Subsequent authorizations that the cardholder verifies as genuine have a value of true in the verified_by_fraud_challenge field.

The following shows an example of a fraud-challenged and declined authorization:

`{
  "id": "iauth_1CmMk2IyNTgGDVfzFKlCm0gU",
  "object": "issuing_authorization",
  "approved": false,
  ...
  "fraud_challenges": [{
    "channel": "sms",
    "status": "pending"
  }]
}`This example shows a subsequent authorization that has been verified by the cardholder:

`{
  "id": "iauth_1CmMk28Jx923VfJJwMCejmX",
  "object": "issuing_authorization",
  "approved": true,
  ...
  "verified_by_fraud_challenge": true
}`NoteVerified, genuine authorizations trigger issuing_authorization.request webhooks. If you use real-time authorization, consider verified_by_fraud_challenge when deciding whether to approve an authorization. If your cardholder has explicitly confirmed a transaction as genuine, we recommend that you don’t apply any of your own risk controls.

To use fraud challenges, make sure that:

- The phone number associated with your cardholder is valid and correct
- Existing transaction decline logic in any`issuing_authorization.request`webhook handler doesn’t conflict with fraud challenges

### Cardholder flow

Your cardholders might receive a challenge and contact your company’s customer service to learn more. Make sure your internal teams are prepared to answer questions that they might receive from your customers about these challenges.

When a cardholder receives a fraud challenge, they can override the declined transaction by verifying that the suspicious transaction is legitimate and initiated by them. Fraud challenges are only available to cardholders with an associated phone number.

The cardholder verifies the override with a one-time SMS prompt with the following language:

Did you attempt a [amount] transaction at [merchant]? Reply YES if you did, or NO if not. Reply STOP to opt out

If the cardholder replies “YES”, they receive the following:

Thanks, please wait a moment and try again.

To complete the purchase, the cardholder needs to initiate the transaction a second time. After retrying, they won’t receive the SMS prompt, and Stripe will not block the transaction for being high-risk. If the cardholder instead replies “NO”, they receive the following:

This transaction was declined. We recommend you cancel your card and request a new one. Review your account for other suspicious transactions.

Cardholders can reply “STOP” to opt out of fraud challenges, and “START” to opt back in again.

## Trigger fraud challenges yourself

To send fraud challenges on authorizations that haven’t been blocked by Stripe, use real-time authorization webhooks. To trigger challenges in scenarios where you detect spending that appears suspicious and want additional verification (for example, a cardholder using their card out of the country), decline the issuing_authorization.request webhook and include the send_fraud_challenges field with the ["sms"] value.

Here’s an example of how to trigger a fraud challenge in a webhook response:

[Node](#)`// This example sets up an endpoint using the Express framework.
// Watch this video to get started: https://youtu.be/rPR2aJ6XnAc

const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.urlencoded({ extended: true }));

const stripe = require('stripe')('sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz');

// Replace with a real secret. You can find your endpoint's secret in your webhook settings.
webhookSecret = 'whsec_...'

app.post('/authorization_requests', (request, response) => {
  const sig = request.headers['stripe-signature'];
  const event = stripe.webhooks.constructEvent(request.body, sig, webhookSecret);

  if (event.type === 'issuing_authorization.request') {
    const auth = event.data.object;

    response.status(200).json({
      approved: false,
      send_fraud_challenges: ['sms']
    });
  }
});

app.listen(4242);`## Fraud challenges for Connect platforms

If you use Connect with Stripe Issuing, turning on fraud challenges enables it for all cardholders across all connected accounts.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[High-risk transactions](#high-risk-transactions)[Fraud challenge flow](#fraud-challenge-flow)[Trigger fraud challenges yourself](#define-your-own-logic)[Fraud challenges for Connect platforms](#fraud-challenges-for-connect-platforms)Products Used[Issuing](/issuing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`