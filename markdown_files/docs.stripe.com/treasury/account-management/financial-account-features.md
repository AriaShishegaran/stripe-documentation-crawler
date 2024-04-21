htmlFinancial account features | Stripe Documentation[Skip to content](#main-content)Financial account features[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Faccount-management%2Ffinancial-account-features)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Faccount-management%2Ffinancial-account-features)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)[Treasury](#)
[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Treasury](/treasury)·[Home](/docs)[Banking as a service](/docs/financial-services)[Treasury](/docs/treasury)# Financial account features

Learn about the features available for financial accounts.You add features to financial accounts to provide the functionality that enables you to move money between accounts, attach payment cards, and more. You typically assign the Feature objects you want when creating FinancialAccount objects, but you can add or remove them at any time. Some Features require that the connected account associated with the financial account have particular capabilities active. For example, a connected account must have the card_issuing capability active before you can request the card_issuing feature on the financial account attached to that connected account.

## Available features

The following table lists the available Features for a FinancialAccount and the capabilities the associated connected account must have active to add them.

NoteYou must request or have the following capabilities active before you can request the treasury capability for connected accounts:

- `transfers`
- `card_payments`

FeatureDescriptionRequired capabilities`card_issuing`Allows the creation of a[Card object](/api/#issuing_card_object)associated with this financial account.`card_issuing``deposit_insurance`Requests FDIC insurance eligibility for the financial account.`treasury``financial_addresses.aba`Triggers the creation of a`FinancialAddress`object of type ABA associated with this financial account. When this feature is active, the address can receive money over ACH or wire, and external bank accounts can debit it.`treasury``inbound_transfers.ach`Allows creation of`InboundTransfer`objects to fund the financial account by debiting an external US bank account.`treasury`,`us_bank_account_ach_payments``intra_stripe_flows`Enables this financial account to send money to or receive money from other financial accounts over the`stripe`network. Both financial accounts (originator and recipient) need this feature enabled for`stripe`network outbound payments to work.`treasury``outbound_payments.ach`Allows this financial account to send ACH transfers using the`OutboundPayment`objects of the Stripe API.`treasury`,`us_bank_account_ach_payments``outbound_payments.us_domestic_wire`Allows this financial account to send US domestic wire transfers using`OutboundPayment`objects of the Stripe API.`treasury``outbound_transfers.ach`Allows this financial account to send ACH transfers using`OutboundTransfer`objects of the Stripe API.`treasury`,`us_bank_account_ach_payments``outbound_transfers.us_domestic_wire`Allows this financial account to send US domestic wire transfers using`OutboundTransfer`objects of the Stripe API.`treasury`Same Day ACH beta Same Day ACH is currently in beta and entry is subject to Stripe review and approval. Reach out to treasury-support@stripe.com to enter the waitlist for this feature. API calls that include Same Day ACH related features or parameters result in an error if you don’t have access to the beta.

The following features enable financial accounts to use Same Day ACH functionality. You must request the corresponding *.ach feature on the financial account to use Same Day ACH functionality. For example, you must request outbound_payments.ach and outbound_payments.ach.same_day on the financial account to enable a financial account to send a same day OutboundPayment:

FeatureDescriptionRequired capabilities`outbound_payments.ach.same_day`Allows this financial account to send ACH transfers using`OutboundPayment`objects that arrive in the destination account within the same business day.`treasury`,`us_bank_account_ach_payments``outbound_transfers.ach.same_day`Allows this financial account to send ACH transfers using`OutboundTransfer`objects that arrive in the destination account within the same business day.`treasury`,`us_bank_account_ach_payments``inbound_payments.ach.same_day`Allows creation of`InboundTransfer`objects to fund the financial account within the same business day.`treasury`,`us_bank_account_ach_payments`## Requesting Features

Typically, you request features on your Treasury financial account when you create the financial account. The following request creates a financial account and requests features in the same call.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/financial_accounts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "supported_currencies[]"=usd \
  -d "features[card_issuing][requested]"=true \
  -d "features[financial_addresses][aba][requested]"=true`If you’re working with existing financial accounts, use POST /v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/features to request additional features.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/features \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "card_issuing[requested]"=true \
  -d "deposit_insurance[requested]"=true \
  -d "financial_addresses[aba][requested]"=true \
  -d "inbound_transfers[ach][requested]"=true \
  -d "intra_stripe_flows[requested]"=true \
  -d "outbound_payments[ach][requested]"=true \
  -d "outbound_payments[us_domestic_wire][requested]"=true \
  -d "outbound_transfers[ach][requested]"=true \
  -d "outbound_transfers[us_domestic_wire][requested]"=true`### Feature activation

After you request a feature and satisfy all verification requirements to onboard the connected account to your platform, the feature activates. Activation might be instantaneous for some features (for example, card_issuing). Other features, like financial_addresses.aba, activate asynchronously. As demonstrated previously, the following API call creates a financial account and requests the features mentioned.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/financial_accounts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "supported_currencies[]"=usd \
  -d "features[financial_addresses][aba][requested]"=true \
  -d "features[card_issuing][requested]"=true`The response when you request features on financial account creation indicates their status in the active_features, pending_features, and restricted_features parameters. See the Retrieving features section for more information on feature statuses.

`{
  "object": "treasury.financial_account",
  "created": 1612927106,
  "id": "fa_123",
  "country": "US",
  "supported_currencies": ["usd"],
  "active_features": ["card_issuing"],
  "pending_features": ["financial_addresses.aba"],
  "restricted_features": [],
  // No FinancialAddress added as the financial_addresses.aba feature is not yet active
  "financial_addresses": [],
  "livemode": true,
  "status": "open",
  ...
}`You can use GET /v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/features to retrieve the features for the financial account created in the previous example.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/features \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"`The response shows financial_addresses.aba with a status of pending and status_details with a code of activating.

`{
  "object": "treasury.financial_account_features",
  "financial_addresses": {
    "aba": {
      "requested": true,
      "status": "pending",
      "status_details": [
        {
          "code": "activating"
        }
      ]
    }
  },
  "card_issuing": {
    "requested": true,
    "status": "active",
    "status_details": []
  },
  ...
}`A feature could remain in this state for up to 30 minutes while Stripe communicates with external systems. When the financial_addresses.aba feature activates, the financial account receives a FinancialAddress object and triggers a treasury.financial_account.features_status_updated webhook.

The following request retrieves the FinancialAccount details with the financial_addresses.aba details expanded.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/financial_accounts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "expand[]"="financial_addresses.aba.account_number" \
  -d "supported_currencies[]"=usd`The response provides the account details, including the complete financial address information.

`{
  "object": "treasury.financial_account",
  "id": "{{FINANCIAL_ACCOUNT_ID}}",
  "country": "US",
  "supported_currencies": ["usd"],
  "active_features": ["card_issuing", "financial_addresses.aba"],
  "pending_features": [],
  "restricted_features": [],
  "financial_addresses": [
    {
      "type": "aba",
      "supported_networks": ["ach", "domestic_wire_us"],
      "aba": {
        "account_number_last4": "7890",
        "account_number": "1234567890",
        "routing_number": "000000001",
        "bank_name": "Goldman Sachs"
      }
    }
  ],
  "livemode": true,
  ...
}`The financial account can now receive credits or debits to this ABA financial address.

## Removing features

As with requesting features, use POST /v1/treasury/financial_accounts/{{FINANCIALACCOUNT_ID}}/features to also remove features, but set the value of the Feature you want to remove to false.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/features \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "card_issuing[requested]"=false`If successful, you receive the Features object as a response with the feature you removed absent from the object.

## Retrieving features

Use GET /v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/features to retrieve the features of the financial account with the associated ID.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/features \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"`The JSON response provides the feature details defined by three properties:

- `requested`—indicates whether the feature has been requested.
- `status`—describes the current state of the feature:`active`,`pending`, or`restricted`.
- `status_details`—array of hashes containing a code and resolution.

`{
  "card_issuing": {
    "requested": true,
    "status": "active",
    "status_details": []
  },
  "deposit_insurance": {
    "requested": true,
    "status": "restricted",
    "status_details": [
      {
        "code": "requirements_past_due",
        "resolution": "provide_information"
      }
    ]
  }
}`The following table identifies the possible combinations of status and status_details.

StatusStatus details codeStatus details resolutionDescription`pending``activating`Stripe is currently activating the feature.`pending``requirements_pending_verification`The requirements for the associated capability on the connected account have been submitted but haven’t completed verification.`restricted``requirements_past_due``provide_information`The connected account has requirements that must be fulfilled before this feature can be enabled.`restricted``rejected_unsupported_business``contact_stripe`The account is rejected because this type of business isn’t currently supported. Contact support for more information at[treasury-support@stripe.com](mailto:treasury-support@stripe.com).`restricted``rejected_other``contact_stripe`The account is rejected for other reasons. Contact support for more information at[treasury-support@stripe.com](mailto:treasury-support@stripe.com).`restricted``restricted_by_platform``remove_restriction`The platform has restricted this feature using the[platform_restrictions](/api/treasury/financial_accounts/object#financial_account_object-platform_restrictions)hash.`restricted``financial_account_closed`This feature is unavailable because the financial account is closed.`restricted``restricted_other``contact_stripe`This feature is restricted for other reasons. Contact support for more information at[treasury-support@stripe.com](mailto:treasury-support@stripe.com).## Restricted features

You can restrict money movement in financial accounts on your platform to not allow inbound flows (inbound_flows), outbound flows (outbound_flows), or both types of flows using the platform_restrictions hash. When you restrict a flow, the restriction impacts certain features that might be associated with the financial account and rely completely or partially on that flow. For example, to prevent money from moving out of a financial account, call POST /v1/treasury/financial_accounts/{{FINANCIALACCOUNT_ID}}.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "platform_restrictions[outbound_flows]"=restricted`If successful, the response returns the financial account object with the appropriate flow set as restricted.

`{
  "object": "treasury.financial_account",
  "id": "{{FINANCIAL_ACCOUNT_ID}}",
  "status": "open",
  ...
  "platform_restrictions": {
    "inbound_flows": "unrestricted",
    "outbound_flows": "restricted"
  },
  "active_features": ["card_issuing", "deposit_insurance", "inbound_transfers.ach"],
  "pending_features": [],
  "restricted_features": ["financial_addresses.aba", "intra_stripe_flows", "outbound_payments.ach", "outbound_payments.us_domestic_wire", "outbound_transfers.ach", "outbound_transfers.us_domestic_wire"]
}`As the previous response shows, when you restrict outbound_flows on the FinancialAccount, financial_addresses.aba, intra_stripe_flows, and inbound_transfers.ach it adds features to the restricted_features array.

Features in the restricted_features array might be only partially restricted, though. For example, financial_addresses.aba is part of the restricted_features array in the preceding response because restricting outbound_flows prevents debits to the financial address. That financial address can still receive ACH or wire transfers, however, because inbound_flows aren’t restricted.

Similarly, the intra_stripe_flows feature is restricted because the outbound_flows restriction prevents using this financial account as the source of an outbound payment to another financial account. The financial account can still be the destination of an outbound payment, though, so the feature isn’t completely restricted.

The following request retrieves feature details for a financial account with restricted flows.

Command Line[curl](#)`curl https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/features \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"`The response provides the Feature object that includes status_details with a code of restricted_by_platform. The restriction property provides a reference to the platform_restriction applied.

`{
  "object": "treasury.financial_account_features",
  "financial_addresses": {
    "aba": {
      "requested": true,
      "status": "restricted",
      "status_details": [
        {
          "code": "restricted_by_platform",
          "resolution": "remove_restriction",
          "restriction": "inbound_flows"
        }
      ]
    }
  },
  ...
}`The following table outlines the impacts to features by platform_restrictions.

NoteRestricting inbound flows for the financial_addresses.aba feature doesn’t block inbound wires.

FeatureImpact of inbound_flows restrictionImpact of outbound_flows restriction`card_issuing`N/AN/A`deposit_insurance`N/AN/A`financial_addresses.aba`Prevents the ABA financial address from receiving credits over ACH.Prevents debits from the ABA financial address.`inbound_transfers.ach`Disables the feature.N/A`intra_stripe_flows`Prevents the financial account from receiving outbound payments from other financial accounts.Outbound payments can’t be made from this financial account to other financial accounts.`outbound_payments.ach`N/ADisables the feature.`outbound_payments.us_domestic_wire`N/ADisables the feature.`outbound_transfers.ach`N/ADisables the feature.`outbound_transfers.us_domestic_wire`N/ADisables the feature.## Webhooks

To perform an action with webhooks when one or more features have transitioned to a certain status, compare your local state with the latest state of the feature. While the previous_attributes property of the treasury.financial_account.features_status_updated webhook also indicates which features have changed from one status to another, events might be received out of order, or might be duplicated. See the webhooks best practices for more information.

- `account.updated`  - When requesting new features, the platform might get an`account.updated`webhook prompting that the`requirements`hash has changed and some new fields are now in`pending_verification`.


- `treasury.financial_account.features_status_updated`  - Indicates that one or more features have changed status. This is reflected in changes to the`active_features`,`pending_features`or`restricted_features`arrays.



Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Available features](#available-features)[Requesting Features](#requesting-features)[Removing features](#removing-features)[Retrieving features](#retrieving-features)[Restricted features](#restricted-features)[Webhooks](#webhooks)Products Used[Treasury](/treasury)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`