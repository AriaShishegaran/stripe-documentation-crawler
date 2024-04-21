# Service agreement types

The connected account’s service agreement type determines what capabilities the account has access to, and which service agreement applies to the platform’s users.

[service agreement type](/api/accounts/object#account_object-tos_acceptance)

[capabilities](/connect/account-capabilities)

Connect platforms can work with three different account types.

[Connect](/connect)

[account types](/connect/accounts)

The content on this page applies only to Express and Custom accounts.

## Supported agreement types

Connected accounts can be under one of the following service agreement types: full or recipient. After the connected account’s service agreement is accepted, the type of service agreement can’t be modified.

A full service agreement creates a service relationship between Stripe and the connected account holder. Connected accounts under the full service agreement can process card payments and request the card_payments capability.

[card_payments](/connect/account-capabilities#card-payments)

For the legal language, see the Stripe Connected Account Agreement.

[Stripe Connected Account Agreement](https://stripe.com/connect-account/legal/full)

A recipient service agreement clarifies that there is no service relationship between Stripe and the recipient, and that the recipient’s relationship is with the platform. Connected accounts under the recipient service agreement can’t process payments or request the card_payments capability.

Transfers to recipient accounts take an extra 24 hours to become available in the connected account’s balance. To learn more about pending balances, see the account balances page.

[account balances](/connect/account-balances)

Cross-border payouts only work with accounts under the recipient service agreement. You must explicitly pass in the country code if it differs from the platform country.

[Cross-border payouts](/connect/cross-border-payouts)

Stripe isn’t responsible for providing direct support for accounts on the recipient service agreement. However, the platform can reach out to Stripe for support for these accounts.

For the legal language, see the Stripe Recipient Agreement.

[Stripe Recipient Agreement](https://stripe.com/connect-account/legal/recipient)

## Choosing the agreement type

You can specify the agreement type through the Accounts API.

[Accounts](/api/accounts)

To choose a recipient service agreement when creating an account, specify the agreement type with tos_acceptance[service_agreement]:

[creating an account](/api#create_account)

[tos_acceptance[service_agreement]](/api/accounts/object#account_object-tos_acceptance)

The same principle applies when updating an account:

[updating an account](/api#update_account)

Changing the service agreement type fails if the service agreement has already been accepted; in those cases, create a new account with the desired service agreement.

To choose a recipient service agreement for all new Express accounts, select the Transfers option with the Restricted Capability Access icon in the Configuration settings section of the Stripe Dashboard.

[Configuration settings](https://dashboard.stripe.com/account/applications/settings/express)

You can override the Configuration settings for an individual account by specifying its capabilities and service agreement type with the Accounts API.

## Accepting the correct agreement

For Express and Connect Onboarding for Custom accounts, Stripe handles the service agreement acceptance.

[Connect Onboarding for Custom](/connect/custom/hosted-onboarding)

For other Custom accounts, the platform must attest that their user has seen and accepted the service agreement. See service agreement acceptance for more information.

[Custom accounts](/connect/custom-accounts)

[service agreement acceptance](/connect/updating-service-agreements#tos-acceptance)
