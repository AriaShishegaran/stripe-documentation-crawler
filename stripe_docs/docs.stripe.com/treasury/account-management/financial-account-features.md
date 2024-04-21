# Financial account features

You add features to financial accounts to provide the functionality that enables you to move money between accounts, attach payment cards, and more. You typically assign the Feature objects you want when creating FinancialAccount objects, but you can add or remove them at any time. Some Features require that the connected account associated with the financial account have particular capabilities active. For example, a connected account must have the card_issuing capability active before you can request the card_issuing feature on the financial account attached to that connected account.

[financial accounts](/treasury/account-management/financial-accounts)

## Available features

The following table lists the available Features for a FinancialAccount and the capabilities the associated connected account must have active to add them.

You must request or have the following capabilities active before you can request the treasury capability for connected accounts:

- transfers

- card_payments

[Card object](/api/#issuing_card_object)

Same Day ACH beta Same Day ACH is currently in beta and entry is subject to Stripe review and approval. Reach out to treasury-support@stripe.com to enter the waitlist for this feature. API calls that include Same Day ACH related features or parameters result in an error if you don’t have access to the beta.

[treasury-support@stripe.com](mailto:treasury-support@stripe.com)

The following features enable financial accounts to use Same Day ACH functionality. You must request the corresponding *.ach feature on the financial account to use Same Day ACH functionality. For example, you must request outbound_payments.ach and outbound_payments.ach.same_day on the financial account to enable a financial account to send a same day OutboundPayment:

[OutboundPayment](/treasury/moving-money/financial-accounts/out-of/outbound-payments)

## Requesting Features

Typically, you request features on your Treasury financial account when you create the financial account. The following request creates a financial account and requests features in the same call.

[create the financial account](/treasury/account-management/financial-accounts#create-a-financialaccount)

If you’re working with existing financial accounts, use POST /v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/features to request additional features.

After you request a feature and satisfy all verification requirements to onboard the connected account to your platform, the feature activates. Activation might be instantaneous for some features (for example, card_issuing). Other features, like financial_addresses.aba, activate asynchronously. As demonstrated previously, the following API call creates a financial account and requests the features mentioned.

[activate asynchronously](#webhooks)

The response when you request features on financial account creation indicates their status in the active_features, pending_features, and restricted_features parameters. See the Retrieving features section for more information on feature statuses.

[Retrieving features](#retrieving-features)

You can use GET /v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/features to retrieve the features for the financial account created in the previous example.

The response shows financial_addresses.aba with a status of pending and status_details with a code of activating.

A feature could remain in this state for up to 30 minutes while Stripe communicates with external systems. When the financial_addresses.aba feature activates, the financial account receives a FinancialAddress object and triggers a treasury.financial_account.features_status_updated webhook.

[webhook](/webhooks)

The following request retrieves the FinancialAccount details with the financial_addresses.aba details expanded.

The response provides the account details, including the complete financial address information.

The financial account can now receive credits or debits to this ABA financial address.

## Removing features

As with requesting features, use POST /v1/treasury/financial_accounts/{{FINANCIALACCOUNT_ID}}/features to also remove features, but set the value of the Feature you want to remove to false.

If successful, you receive the Features object as a response with the feature you removed absent from the object.

[Features object](/api/treasury/financial_account_features)

## Retrieving features

Use GET /v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/features to retrieve the features of the financial account with the associated ID.

The JSON response provides the feature details defined by three properties:

- requested—indicates whether the feature has been requested.

- status—describes the current state of the feature: active, pending, or restricted.

- status_details—array of hashes containing a code and resolution.

The following table identifies the possible combinations of status and status_details.

[treasury-support@stripe.com](mailto:treasury-support@stripe.com)

[treasury-support@stripe.com](mailto:treasury-support@stripe.com)

[platform_restrictions](/api/treasury/financial_accounts/object#financial_account_object-platform_restrictions)

[treasury-support@stripe.com](mailto:treasury-support@stripe.com)

## Restricted features

You can restrict money movement in financial accounts on your platform to not allow inbound flows (inbound_flows), outbound flows (outbound_flows), or both types of flows using the platform_restrictions hash. When you restrict a flow, the restriction impacts certain features that might be associated with the financial account and rely completely or partially on that flow. For example, to prevent money from moving out of a financial account, call POST /v1/treasury/financial_accounts/{{FINANCIALACCOUNT_ID}}.

[platform_restrictions](/api/treasury/financial_accounts/object#financial_account_object-platform_restrictions)

If successful, the response returns the financial account object with the appropriate flow set as restricted.

As the previous response shows, when you restrict outbound_flows on the FinancialAccount, financial_addresses.aba, intra_stripe_flows, and inbound_transfers.ach it adds features to the restricted_features array.

Features in the restricted_features array might be only partially restricted, though. For example, financial_addresses.aba is part of the restricted_features array in the preceding response because restricting outbound_flows prevents debits to the financial address. That financial address can still receive ACH or wire transfers, however, because inbound_flows aren’t restricted.

Similarly, the intra_stripe_flows feature is restricted because the outbound_flows restriction prevents using this financial account as the source of an outbound payment to another financial account. The financial account can still be the destination of an outbound payment, though, so the feature isn’t completely restricted.

The following request retrieves feature details for a financial account with restricted flows.

The response provides the Feature object that includes status_details with a code of restricted_by_platform. The restriction property provides a reference to the platform_restriction applied.

The following table outlines the impacts to features by platform_restrictions.

Restricting inbound flows for the financial_addresses.aba feature doesn’t block inbound wires.

## Webhooks

To perform an action with webhooks when one or more features have transitioned to a certain status, compare your local state with the latest state of the feature. While the previous_attributes property of the treasury.financial_account.features_status_updated webhook also indicates which features have changed from one status to another, events might be received out of order, or might be duplicated. See the webhooks best practices for more information.

[webhooks](/webhooks)

[webhooks best practices](/webhooks#best-practices)

- account.updatedWhen requesting new features, the platform might get an account.updated webhook prompting that the requirements hash has changed and some new fields are now in pending_verification.

- When requesting new features, the platform might get an account.updated webhook prompting that the requirements hash has changed and some new fields are now in pending_verification.

- treasury.financial_account.features_status_updatedIndicates that one or more features have changed status. This is reflected in changes to the active_features, pending_features or restricted_features arrays.

- Indicates that one or more features have changed status. This is reflected in changes to the active_features, pending_features or restricted_features arrays.
