# Issuing real-time authorizations

Your synchronous webhook is only used for authorization requests. All other notifications are sent to your regular webhook endpoint.

Using the synchronous webhook, you can approve or decline authorization requests in real time.

Your webhook endpoint can be configured in your settings. When a card is used to make a purchase, Stripe creates an issuing_authorization.request and sends it to your configured endpoint for your approval.

[settings](https://dashboard.stripe.com/account/issuing)

Get started with our interactive guide to real-time authorizations.

[interactive guide to real-time authorizations](/issuing/controls/real-time-authorizations/quickstart)

## Responding to authorization requests

You can respond to authorizations requests by responding directly to the webhook event.

Respond to the issuing_authorization.request webhook event directly to either approve or decline an authorization after it’s received.

Our webhook accepts JSON responses with the following parameters:

Status code: Return 200 to indicate success.

Header:

Body:

[key-value pairs](/api/metadata)

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

This documentation is maintained for existing users. If you’re a new user, respond directly to the webhook. If you’re an existing user, plan to migrate to the direct webhook response. You can follow our direct webhook migration guide.

[our direct webhook migration guide](/issuing/controls/real-time-authorizations/direct-webhook-migration)

Make an API call to either approve or decline the request and include the Authorization ID. If you use this method, your webhook must approve or decline each authorization before responding to the incoming webhook request.

[approve](/api/issuing/authorizations/approve)

[decline](/api/issuing/authorizations/decline)

[Authorization](/api/issuing/authorizations/object)

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

We recommend that you only use one of these two methods to respond to authorization requests. For users migrating from one method to another, both methods are supported during a migration. In the event both methods are used on the same authorization, the API call takes precedence over the direct response. For migrations, we recommend only using one method on a given request at a time.

If Stripe doesn’t receive your approve or decline response or request within 2 seconds, the Authorization is automatically approved or declined based on your timeout settings.

[timeout settings](https://dashboard.stripe.com/account/issuing)

If your Issuing balance has insufficient funds for the incoming authorization, the authorization will be denied and your webhook endpoint will not receive the issuing_authorization.request event. To learn more about funding your Issuing balance, read here.

[read here](/issuing/funding/balance)

## Authorization requests

When an authorization request is sent to your webhook, the amount requested is stored in pending_request.

The top-level amount in the request is set to 0 and approved is false. Once you respond to the request, the top-level amount reflects the total amount approved or declined, the approved field is updated, and pending_request is set to null.

To test webhooks locally, you can use Stripe CLI. Once you have it installed, you can forward events to your server:

[Stripe CLI](/stripe-cli)

In another terminal, you can then manually trigger issuing_authorization.request events from the CLI for more streamlined testing. Issuing users in the UK or Europe can add a .gb or .eu suffix to trigger an authorization request in their local currency.

Learn more about setting up webhooks.

[setting up webhooks](/webhooks)

## Autopilot Beta

Autopilot is a set of fallback options that allow you to continue making real-time authorization decisions in the event your systems are down or don’t respond to an authorization request within the allotted time window.

For users with their own dedicated Bank Identification Numbers (BIN), we also offer Autopilot in the event that Stripe can’t communicate with the network to prevent any continuity issues that might result.

In both cases, we make an authorization decision on your behalf based on a predefined set of rules. We create authorization objects for transmission, so that reconciliation can take place for the Autopilot transactions. When an authorization is approved or declined through Autopilot while you’re down, the request_history.reason field within the issuing_authorization.created webhook changes to webhook_timeout. When an authorization is approved or declined through Autopilot while Stripe is down, the request_history.reason field within the issuing_authorization.created webhook changes to network_stip.

Access to Autopilot is currently limited to US beta users. You must be an Issuing customer to join the beta. To request access to the beta, log in to your Stripe account and refresh the page. Contact Stripe for more information.

[Contact Stripe](https://stripe.com/contact/sales)

## Fraud challenges Beta

Fraud challenges allow your cardholders to retry non-fraudulent transactions that would have otherwise been blocked.

[Fraud challenges](/issuing/controls/fraud-challenges)

To manage the rules that dictate when a fraud challenge is sent, adjust your response to the  issuing_authorization.request webhook. You can trigger fraud challenges in scenarios where you detect spending that appears suspicious and want additional verification (for example, a cardholder using their card out of the country).

To do so, decline the issuing_authorization.request webhook and include the send_fraud_challenges field with the ["sms"] value.

Fraud challenges are currently limited to beta users. You must be an Issuing customer to join the beta. To request access to the beta, log in to your Stripe account and refresh the page. Contact Stripe for more information.

[Contact Stripe](https://stripe.com/contact/sales)
