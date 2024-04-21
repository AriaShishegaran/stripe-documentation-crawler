# Migrate to direct webhook response

You can now respond directly to a issuing_authorization.request webhook with a real-time authorization decision instead of making an API call to approve and decline endpoints during the webhook.

[respond directly to a issuing_authorization.request webhook](/issuing/controls/real-time-authorizations)

[approve](/api/issuing/authorizations/approve)

[decline](/api/issuing/authorizations/decline)

Responding directly to the webhook event simplifies real-time authorizations, and removes an extra API call that can negatively impact your authorization rate with time outs.

If you’re building a new integration, use the new direct webhook response instead of making approve and decline API calls. We are deprecating the approve and decline endpoints, but existing users will continue to have access until at least the end of 2024. If you have an existing integration with real-time authorization, plan to migrate to direct webhook responses.

This guide only applies if you use the /approve and /decline endpoints for real-time authorizations.

## Legacy API call flow

Previously, you needed to make an API call to /approve or /decline to make a decision for an incoming authorization request before responding to the issuing_authorization.request webhook.

## New direct webhook response flow

You can now respond directly to the issuing_authorization.request webhook with a decision in the response body, without needing to make a separate API call. After the decision, an issuing_authorization.created or issuing_authorization.updated webhook event is still sent.

Learn more about this API in the real-time authorization documentation, and build an integration with our interactive guide.

[real-time authorization documentation](/issuing/controls/real-time-authorizations)

[our interactive guide](/issuing/controls/real-time-authorizations/quickstart)

You must respond with an HTTP status code of 200, a Stripe-Version header set to a specific API version, and a Boolean of approved in the JSON body. The JSON body must correspond with the specified API version.

[specified API version](/api/versioning)

For controllable amount authorizations, partial approvals optionally include amount.

[partial approvals](/issuing/purchases/authorizations?issuing-authorization-type=incremental_authorization#handling-other-authorizations)

For direct webhook response Authorizations, we’ve made several additions:

[Authorizations](/api/issuing/authorizations/object)

- Added value webhook_error to request_history.reason. This value is present if the webhook response fails due to validation errors.

[request_history.reason](/api/issuing/authorizations/object#issuing_authorization_object-request_history-reason)

- New field request_history.reason_message, which includes a detailed error message if the request_history.reason is webhook_error.

## Migrate to direct response

You can try the direct webhook response in test mode. As a best practice, we recommend gradually shifting over from the legacy API call to responding directly to the webhook.

If you call an API method and include the direct webhook response body, the API method decision takes priority.

Here’s an example of what a migration to the direct webhook might look like in Ruby. For other languages, see our interactive guide.

[our interactive guide](/issuing/controls/real-time-authorizations/quickstart)

After testing in test mode, gradually shift traffic to the direct webhook response.

[https://stripe.com/docs/api/versioning](https://stripe.com/docs/api/versioning)
