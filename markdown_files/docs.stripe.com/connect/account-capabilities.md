htmlAccount capabilities | Stripe Documentation[Skip to content](#main-content)Account capabilities[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Faccount-capabilities)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Faccount-capabilities)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Account capabilities

Learn about capabilities you can enable for accounts and the requirements you must satisfy to use them.The capabilities you request for a connected account determine the information you need to collect for that account. To reduce onboarding effort, only request the capabilities you need. The more capabilities you request, the more information you must collect.

You can start by completing the platform profile to understand which capabilities might be appropriate for your platform.

NoteFor most capabilities, requesting them enables them permanently. Attempting to remove or unrequest a permanent capability returns an error.

## Supported capabilities

Following is a list of available capabilities. Click an item to expand or collapse it.

### Transfers

### Card payments

### US tax reporting

### Payment methods

### India international payments

## Multiple capabilities

Requesting multiple capabilities for a connected account is common, but involves the following considerations:

- Capabilities operate independently of each other.
- If a connected account has both`card_payments`and`transfers`, and the`status`of either one is`inactive`, then both capabilities are disabled.
- You can request or unrequest a capability for a connected account at any time during the account’s lifecycle.

Capabilities also allow you to collect information for multiple purposes at the same time, so users are not asked to submit the same information more than once. For example, you can collect both required tax information and the information required for a requested capability. If you’re onboarding a user with the transfers capability and they’re required to file an IRS FORM 1099-MISC (a US federal tax reporting form), you can collect information for both at the same time.

## Create an account with capabilities

Capabilities are set on the Account object. To find the list of available capabilities, use the list_capabilities endpoint.

Account creation and requesting capabilities differ for connected accounts in different configurations.

- Capabilities are automatically requested on any accounts that you set up with access to the full Stripe Dashboard, including Standard accounts.
- For accounts with access to the Express Dashboard, including Express accounts, you can either request capabilities when creating the account or use the[onboarding configuration settings](https://dashboard.stripe.com/settings/connect/onboarding-options/countries)to automate requested capabilities.
- You must request capabilities when you create connected accounts without access to a Stripe-hosted dashboard, including Custom accounts.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d country=US \
  -d type=custom \
  -d "capabilities[card_payments][requested]"=true \
  -d "capabilities[transfers][requested]"=true`Information requirements vary depending on the capability, but they often relate to identity verification or other information specific to a payment type.

When your connected account is successfully created, you can view what its requirements are:

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`In the response, check the requirements hash to see what information is needed. The values for payouts_enabled and charges_enabled indicate whether payouts and charges are enabled for the account.

## More about capabilities

The basics of account creation are covered above. However, there are instances where you want to preview information requirements or manage capabilities on existing accounts. The following sections describe how to perform these actions using the Capabilities API.

### Preview information requirements

You can preview what information is needed from your user for a particular capability either before or after that capability has been requested.

When you request capabilities, account.updated webhooks fire and the account’s requirements might change. If you preview the requirements first, collect what’s required for the account, and then request the capability, you can assist in enabling charges and payouts for the account more quickly. You also avoid the possibility of the account getting disabled since the information was already collected in advance.

Below is an example that lists the requirements for the card_payments capability for a specific account.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/capabilities/card_payments \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`In the response, check the requirements hash to see what information is needed:

`{
  "id": "card_payments",
  "object": "capability",
  "account": "{{CONNECTED_ACCOUNT_ID}}",
  "requested": false,
  "requested_at": null,
  "requirements": {
    "past_due": [],
    "currently_due": ["company.tax_id", ...],
    "eventually_due": [...],
    "disabled_reason": ...,
    "current_deadline": ...,
  },
  "status": "unrequested"
}`The value for status identifies whether the capability has been requested. When it is requested, requirements are activated for the account.

While these steps demonstrate how to preview a capability’s requirements before requesting it, you can use the same endpoint to view what the current requirements are for a capability. This can help you stay informed of what a capability’s requirements are and also of any requirement changes.

### Request and unrequest capabilities

After creating most accounts, you can request additional capabilities and remove existing capabilities. To request a capability, set the capability’s requested value to true by updating the account. If the request succeeds, the API returns requested: true in the response. You can’t request capabilities for connected accounts with access to the full Stripe Dashboard, including Standard accounts.

To unrequest a capability, set the capability’s requested value to false by updating the account. If the capability can’t be removed, this call returns an error. If the call succeeds, the API returns requested: false in the response.

You can also request and remove an account’s capabilities from the Dashboard. If a capability can’t be removed, its Remove button is disabled.

The example below requests the transfers capability for a specific connected account:

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/capabilities/transfers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d requested=true`The example below requests multiple capabilities for a specific connected account:

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "capabilities[bancontact_payments][requested]"=true \
  -d "capabilities[eps_payments][requested]"=true \
  -d "capabilities[giropay_payments][requested]"=true \
  -d "capabilities[ideal_payments][requested]"=true \
  -d "capabilities[p24_payments][requested]"=true \
  -d "capabilities[sofort_payments][requested]"=true \
  -d "capabilities[sepa_debit_payments][requested]"=true`## See also

- [Create a charge](/connect/charges)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Supported capabilities](#supported-capabilities)[Multiple capabilities](#multiple-capabilities)[Create an account with capabilities](#creating)[More about capabilities](#more-about-capabilities)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`