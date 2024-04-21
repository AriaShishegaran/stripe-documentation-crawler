# Working with connected accounts in Treasury

To use Stripe Treasury, your platform must have a Stripe Connect integration. Stripe Connect enables a platform to provide connected accounts to sellers and service providers. For an overview of how connected accounts fit into the Stripe Treasury account structure, see the Stripe Treasury accounts structure guide.

[Connect](/connect)

[Stripe Treasury accounts structure](/treasury/account-management/treasury-accounts-structure)

There are three types of connected accounts available with Connect: Standard, Express, and Custom. Currently, Treasury only supports Custom connected accounts.

Financial accounts can be attached to Custom connected accounts only.

Connected accounts require specific capabilities enabled on the account to use features of Treasury. Different features require different capabilities, which might require additional information about your connected account owners. The treasury capability, for example, is a requirement on connected accounts for Treasury access. When you request treasury for an account, additional fields become required for that connected account before the account can use Treasury.

Before you create Custom connected accounts in live mode for your Treasury integration, we recommend you first create test connected accounts in test mode. Test mode connected accounts can’t receive or send real money and can’t be used in live mode, but are otherwise identical in configuration and functionality.

[test mode](/test-mode)

## Checking current connected account types

If your platform already has a Connect integration with connected accounts but are unsure of their type, you can use the Dashboard or API to retrieve this information.

Navigate to the Connected accounts page in the Dashboard. We list your connected accounts in a table format. The Type column contains information about the account type.

[Connected accounts page](https://dashboard.stripe.com/test/connect/accounts/overview)

Account types

You can also select an account in the table to open the detailed view. There, you can find the account type in the Identity > Account details section.

Account details

## Create a new connected account with the treasury capability

This guide demonstrates how to create a new Custom connected account using the Stripe API for Treasury and isn’t exhaustive. For complete documentation on creating a Custom connected account, including through hosted onboarding, see Using Connect with Custom accounts.

[Using Connect with Custom accounts](/connect/custom-accounts)

Use POST /v1/accounts to create a new connected account. Request the following capabilities for the account, which are required to use Stripe Treasury:

- transfers (required for all connected accounts)

- treasury

You can update the account later to request these capabilities if you don’t do so when creating the account.

If you want to issue cards with Stripe Issuing to your connected account, you must request the card_issuing capability, as well. See the Working with Stripe Issuing cards guide for more information.

[Working with Stripe Issuing cards](/treasury/account-management/issuing-cards)

If you want to leverage ACH to transfer funds to or from an external account, you must also request the us_bank_account_ach_payments capability.

With all the previous options included, the request resembles the following:

If successful, the response you receive confirms the connected account and requested capabilities.

To learn more about connected account capabilities, see the Account capabilities guide for Connect.

[Account capabilities](/connect/account-capabilities)

## Update a connected account to include the treasury capability

If you already have a connected account with card_payments enabled, use POST /v1/accounts/{{CONNECTED_ACCOUNT_ID}} to update the account with the associated ID with a request for the treasury capability. The following request updates a connected account with a request for the treasury capability, and includes the optional capabilities of card_issuing and us_bank_account_ach_payments:

Use POST /v1/accounts/{{CONNECTED_ACCOUNT_ID}} to update connected account capabilities for connected accounts that already have a FinancialAccount assigned. See Working with financial accounts or the FinancialAccount object API documentation for more information.

[Working with financial accounts](/treasury/account-management/financial-accounts)

[FinancialAccount object](/api/treasury/financial_accounts/object)

## Onboard the connected account

After you create an account, you must onboard the seller or service provider to the account for ownership. The Account object that represents the connected account has a requirements hash that contains currently_due identity verification requirements. The seller or service provider on your platform must provide the details itemized in the requirements hash to enable charges and payouts on their connected account and enable all requested features of their financial account.

[Account](/api/accounts/object#account_object-requirements-currently_due)

[identity verification](/connect/handling-api-verification)

[payouts](/payouts)

There are two options for onboarding connected accounts owners to Treasury: hosted onboarding and custom onboarding. Hosted onboarding is recommended, but it’s not required.

[hosted onboarding](/treasury/account-management/connected-accounts#using-hosted-onboarding)

[custom onboarding](/treasury/account-management/connected-accounts#using-custom-onboarding)

If you create an Account object in test mode and want to bypass onboarding requirements to test functionality, use POST /v1/accounts/{{CONNECTED_ACCOUNT_ID}} to provide test values that fulfill all the requirements. The following request uses a previously created connected account to apply the required account details.

[provide test values](/connect/testing-verification)

[https://bestcookieco.com](https://bestcookieco.com)

The most efficient way to collect required information is to integrate Connect Onboarding for Custom accounts, which offloads the verification complexity from your platform to Stripe and collects the terms of the service agreement. Otherwise, you must not only write your own API requests for initial integration, but also continue to monitor for changes to compliance requirements to keep your onboarding workflow current.

[Connect Onboarding for Custom accounts](/connect/custom/hosted-onboarding)

Before you can use Connect Onboarding, you must provide the name, color, and icon of your brand in the Branding section of your Connect settings page. Doing so customizes the visual appearance of the form that sellers and service providers interact with when onboarding to your platform.

[Connect settings page](https://dashboard.stripe.com/test/settings/connect)

To take advantage of Connect Onboarding, use POST /v1/account_links to create an AccountLink to provide to the seller or service provider who’s going to take ownership of the connected account:

For security, don’t email, text, or otherwise send account link URLs directly to your user. Instead, redirect the authenticated user to the account link URL from within your platform’s application.

[https://example.com/reauth](https://example.com/reauth)

[https://example.com/return](https://example.com/return)

The response you receive includes the URL to provide to your user.

[https://connect.stripe.com/setup/s/iCtLfmYb2tEU](https://connect.stripe.com/setup/s/iCtLfmYb2tEU)

If you prefer to build custom onboarding for your users, use POST /v1/accounts/{{CONNECTED_ACCOUNT_ID}} and POST /v1/accounts/{{CONNECTED_ACCOUNT_ID}}/persons/{{PERSON_ID}} to update the relevant Account and Person objects with the required information.

You must also confirm that the connected account owner has read and agreed to the Stripe Treasury Agreement. See Handling verification with the API for additional details on fulfilling onboarding requirements.

[Stripe Treasury Agreement](https://stripe.com/treasury-connect-account/legal)

[Handling verification with the API](/connect/handling-api-verification)

The fields in the following table are required for Treasury users.

- Business names (customer facing and legal)

- Legal entity type

- Business address

- Business phone number

- Product or service description

- Industry or Merchant category code

- Tax ID Number (SSN, ITIN, or EIN)

- Treasury TOS acceptance

- Stripe TOS acceptance

- Legal name

- Date of birth

- Email address

- Residential address

- Full SSN, or ID document scan for non-US persons or if SSN can’t be verified

- Title

- Phone number

- Business names (customer facing and legal)

- Legal entity type

- Business address

- Business phone number

- Product or service description

- Industry or Merchant category code

- Tax ID Number (EIN)

- Treasury TOS acceptance

- Stripe TOS acceptance

- Legal name

- Date of birth

- Email address

- Residential address

- Phone number

- Title

- Percent ownership of company

- Full SSN, or ID document scan for non-US persons or if SSN can’t be verified

The connected account onboarding process is complete when you receive an account.updated webhook confirming the following fields on your connected account:

[webhook](/webhooks)

Account onboarding latency when your platform’s bank partner is Evolve Bank & Trust is less than 5 minutes.

To adapt to changes in financial regulations, Stripe must occasionally update information collection requirements for Treasury. The requirements.eventually_due array on the Account object captures the updated information required by these regulation changes. To learn more about the requirements hash, read the requirements definition in the API reference.

[requirements](/api/accounts/object#account_object-requirements)
