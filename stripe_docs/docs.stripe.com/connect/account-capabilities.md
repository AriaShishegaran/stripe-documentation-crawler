# Account capabilities

The capabilities you request for a connected account determine the information you need to collect for that account. To reduce onboarding effort, only request the capabilities you need. The more capabilities you request, the more information you must collect.

You can start by completing the platform profile to understand which capabilities might be appropriate for your platform.

[platform profile](https://dashboard.stripe.com/connect/profile)

For most capabilities, requesting them enables them permanently. Attempting to remove or unrequest a permanent capability returns an error.

## Supported capabilities

Following is a list of available capabilities. Click an item to expand or collapse it.

## Multiple capabilities

Requesting multiple capabilities for a connected account is common, but involves the following considerations:

- Capabilities operate independently of each other.

- If a connected account has both card_payments and transfers, and the status of either one is inactive, then both capabilities are disabled.

- You can request or unrequest a capability for a connected account at any time during the account’s lifecycle.

Capabilities also allow you to collect information for multiple purposes at the same time, so users are not asked to submit the same information more than once. For example, you can collect both required tax information and the information required for a requested capability. If you’re onboarding a user with the transfers capability and they’re required to file an IRS FORM 1099-MISC (a US federal tax reporting form), you can collect information for both at the same time.

## Create an account with capabilities

Capabilities are set on the Account object. To find the list of available capabilities, use the list_capabilities endpoint.

[Account](/api/accounts/object)

[list_capabilities](/api/capabilities/list?lang=curl)

Account creation and requesting capabilities differ for connected accounts in different configurations.

- Capabilities are automatically requested on any accounts that you set up with access to the full Stripe Dashboard, including Standard accounts.

- For accounts with access to the Express Dashboard, including Express accounts, you can either request capabilities when creating the account or use the onboarding configuration settings to automate requested capabilities.

[onboarding configuration settings](https://dashboard.stripe.com/settings/connect/onboarding-options/countries)

- You must request capabilities when you create connected accounts without access to a Stripe-hosted dashboard, including Custom accounts.

Information requirements vary depending on the capability, but they often relate to identity verification or other information specific to a payment type.

When your connected account is successfully created, you can view what its requirements are:

[view](/api/accounts/retrieve)

In the response, check the requirements hash to see what information is needed. The values for payouts_enabled and charges_enabled indicate whether payouts and charges are enabled for the account.

## More about capabilities

The basics of account creation are covered above. However, there are instances where you want to preview information requirements or manage capabilities on existing accounts. The following sections describe how to perform these actions using the Capabilities API.

[Capabilities API](/api/capabilities)

You can preview what information is needed from your user for a particular capability either before or after that capability has been requested.

When you request capabilities, account.updated webhooks fire and the account’s requirements might change. If you preview the requirements first, collect what’s required for the account, and then request the capability, you can assist in enabling charges and payouts for the account more quickly. You also avoid the possibility of the account getting disabled since the information was already collected in advance.

[webhooks](/webhooks)

Below is an example that lists the requirements for the card_payments capability for a specific account.

[lists](/api/capabilities/retrieve)

In the response, check the requirements hash to see what information is needed:

The value for status identifies whether the capability has been requested. When it is requested, requirements are activated for the account.

[requested](#requesting-unrequesting)

While these steps demonstrate how to preview a capability’s requirements before requesting it, you can use the same endpoint to view what the current requirements are for a capability. This can help you stay informed of what a capability’s requirements are and also of any requirement changes.

After creating most accounts, you can request additional capabilities and remove existing capabilities. To request a capability, set the capability’s requested value to true by updating the account. If the request succeeds, the API returns requested: true in the response. You can’t request capabilities for connected accounts with access to the full Stripe Dashboard, including Standard accounts.

[updating the account](/api/capabilities/update)

To unrequest a capability, set the capability’s requested value to false by updating the account. If the capability can’t be removed, this call returns an error. If the call succeeds, the API returns requested: false in the response.

[updating the account](/api/capabilities/update)

You can also request and remove an account’s capabilities from the Dashboard. If a capability can’t be removed, its Remove button is disabled.

[request and remove an account’s capabilities](/connect/dashboard/managing-individual-accounts#updating-capabilities)

The example below requests the transfers capability for a specific connected account:

The example below requests multiple capabilities for a specific connected account:

## See also

- Create a charge

[Create a charge](/connect/charges)
