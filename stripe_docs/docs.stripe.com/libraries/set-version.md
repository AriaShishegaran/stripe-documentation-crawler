# Set a Stripe API version

Your account has a default API version, which defines how you call the API, what functionality you have access to and what you’re guaranteed to get back as part of the response. Webhook event objects are based on your default API version, which might be different from the API version used by the SDK. To make sure these versions match, we recommend registering a webhook endpoint with the same API version used as the SDK. To find your version, see View your default API version.

[registering a webhook endpoint](/webhooks#register-webhook)

[API version](/api/webhook_endpoints/create#create_webhook_endpoint-api_version)

[View your default API version](/development/dashboard/request-logs#view-your-default-api-version)

## Versioning basics

We’ve covered a few fundamental concepts you need to know about API versions used in SDKs. Choose your SDK language to get started.

The stripe-ruby library allows you to set the API version globally or on a per-request basis. If you don’t set an API version, recent versions of stripe-ruby use the API version that was latest at the time your version of stripe-ruby was released. Versions of stripe-ruby before v9 use your account’s default API version.

[v9](https://github.com/stripe/stripe-ruby/blob/master/CHANGELOG.md#900---2023-08-16)

To set the API version globally with the SDK, assign the version to the Stripe.api_version property:

Or set the version per-request:

When you override the version globally or per-request, the API response objects are also returned in that version.

Before updating your API version, carefully review the following resources:

[your API version](/development/dashboard/request-logs#view-your-default-api-version)

- Stripe API changelog

[Stripe API changelog](/upgrades#api-versions)

- Upgrading your API version

[Upgrading your API version](/upgrades#how-can-i-upgrade-my-api)

You can upgrade your account’s default API version in the Developers Dashboard. Update your code to use the latest version of the Ruby SDK and set the new API version when making your calls.

[Developers Dashboard](https://dashboard.stripe.com/developers)

## See also

Stripe SDKs follow their own versioning policy. See the link below to learn more.

- Stripe versioning and support policies

[Stripe versioning and support policies](/libraries/versioning)
