# Testing Stripe Connect

Use testing to make sure your Connect integration handles different flows correctly. Use test mode to simulate live mode while taking advantage of Stripe-provided special tokens to use in your tests. Take a look at our payments testing guide for more information on testing charges, disputes, and so on.

[Connect](/connect)

[test mode](/test-mode)

[payments testing guide](/testing)

## Create test accounts

You can create multiple test accounts and use any account type you might need (for example, representing multiple countries).

[account type](/connect/accounts)

You can create test accounts using the Accounts API or in the Stripe Dashboard.

[Accounts API](/api/accounts/create)

[Stripe Dashboard](/connect/dashboard/managing-individual-accounts#creating-accounts)

Use 000-000 as the SMS code when prompted for test accounts.

## Test the OAuth flow

You can test your OAuth integration with connected accounts that use a Stripe-hosted dashboard using your test mode client_id.

Your test mode client_id is ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb. You can find this in your Connect OAuth settings.

[Connect OAuth settings](https://dashboard.stripe.com/settings/connect/onboarding-options/oauth)

Your test mode client_id allows you to:

- Set your redirect_uri to a non-HTTPS URL

- Set your redirect_uri to localhost

- Force-skip the account form instead of having to fill out an entire account application (Stripe Dashboard accounts only)

- Get test access tokens for connected accounts

To test the OAuth flow, create a new account after clicking the OAuth link. You can also test connecting an existing Stripe account only if the email is different from your platform account.

[OAuth](/connect/oauth-standard-accounts)

## Identity verification

Because verification is a crucial component for onboarding accounts, we’ve created a dedicated guide to testing verification.

[guide to testing verification](/connect/testing-verification)

After creating a test connected account, you can use tokens to test different verification statuses to make sure you’re handling different requirements and account states. You can use the following tokens to test verification with test accounts.

Use these dates of birth (DOB) to trigger certain verification conditions.

[webhook](/webhooks)

Use these addresses for line1 to trigger certain verification conditions. You must pass in legitimate values for the city, state, and postal_code arguments.

Use these personal ID numbers for individual.id_number or the id_number attribute on the Person object to trigger certain verification conditions.

[individual.id_number](/api/accounts/create#create_account-individual-id_number)

[id_number](/api/persons/create#create_person-id_number)

[webhook](/webhooks)

For testing, use file tokens instead of uploading your own test IDs. For details, refer to Uploading a file.

[Uploading a file](/connect/handling-api-verification#upload-a-file)

Use these file tokens to trigger certain identity verification conditions.

## Business information verification

In some countries, the business address associated with your connected account must be validated before charges, payouts, or both can be enabled on the connected account.

[payouts](/payouts)

Use these addresses for line1 to trigger certain validation conditions. You must pass in legitimate values for the city, state, and postal_code arguments.

Make sure you start with an address token that has the least permissive validation condition you want to test for. This is because you can’t use an address token that has a more restrictive validation condition than the previous token used. For example, if you provided address_full_match to have both charges and payouts enabled, you can’t disable payouts or charges afterward by changing the token to an invalid one. You can work around this by creating a new account with the relevant token.

[requirements](/api/accounts/object#account_object-requirements)

[requirements](/api/accounts/object#account_object-requirements)

Use these business tax ID numbers for company.tax_id to trigger certain verification conditions.

[company.tax_id](/api/accounts/create#create_account-company-tax_id)

[webhook](/webhooks)

Trigger director verification for an Account object by using this token for the individual.first_name. attribute and setting the individual.relationship.director attribute to true.

[individual.first_name.](/api/accounts/create#create_account-individual-first_name)

[individual.relationship.director](/api/accounts/object#account_object-individual-relationship-director)

Trigger company name verification for an Account object by using this token for the company.name attribute.

[company.name](/api/accounts/object#account_object-company-name)

Trigger statement descriptor verification for an Account object by using this token for the settings.payments.statement_descriptor attribute.

[settings.payments.statement_descriptor](/api/accounts/object#account_object-settings-payments-statement_descriptor)

Trigger statement descriptor prefix verification for an Account object by using this token for the settings.payments.statement_descriptor_prefix attribute.

[settings.payments.statement_descriptor_prefix](/api/accounts/object#account_object-settings-payments-statement_descriptor_prefix)

Trigger URL verification for an Account object by using this token for the business_profile.url attribute.

[business_profile.url](/api/accounts/object#account_object-business_profile-url)

Trigger DBA verification for an Account object by using this token for the business_profile.name attribute.

[business_profile.name](/api/accounts/object#account_object-business_profile-name)

Trigger product description verification for an Account object by using this token for the business_profile.product_description attribute.

[business_profile.product_description](/api/accounts/object#account_object-business_profile-product_description)

## Trigger or advance verification

Use these card numbers to trigger various conditions when you’re testing both requirements and tiered verification. For the trigger actions to work, you must use these cards with a Connect charge by setting on_behalf_of, or creating the charge directly on the connected account.

[on_behalf_of](/connect/separate-charges-and-transfers#settlement-merchant)

[directly on the connected account](/connect/direct-charges)

Live mode can require additional verification information when a connected account processes a certain amount of volume. This card sets any additional verification information to be required immediately. If no additional information is required, nothing appears.

If required information isn’t provided by the deadline, Stripe disables the connected account’s charges or payouts. These cards disable the connected account and move any currently due requirements to overdue. These cards have no effect until an account provides the initial information that’s required to enable charges and payouts.

Connected accounts in the United States and India are subject to Bank account ownership verification. You can complete this verification by uploading supporting documents with the Connect Dashboard or with the API through the documents[bank_account_ownership_verification] hash.

[Bank account ownership verification](https://support.stripe.com/questions/bank-account-ownership-verification)

[documents[bank_account_ownership_verification]](/api/accounts/update#update_account-documents-bank_account_ownership_verification-files)

In test mode, you can simulate the US bank account ownership verification process. Use the following test bank account numbers to trigger the verification process. One number presumes successful verification and the other prompts you to upload test images or file tokens to complete the verification process. These test accounts are only available for US accounts.

If your platform has connected accounts in different countries or plans to, you might need to verify a person’s address as well as their identity (depending on the country). Stripe provides a sample date of birth (DOB) and sample addresses to test for this requirement.

[date of birth](#test-dobs)

[addresses](#test-verification-addresses)

## Add funds to Stripe balance

To test adding funds to your Stripe balance from a bank account in the Dashboard, enable test mode and select the desired test bank account in the drop-down menu within the Add to balance dialog. You can simulate success or failure due to insufficient funds.

[adding funds](/connect/top-ups)

To test adding funds in the API, use the following test bank tokens as the source while in test mode. Each token simulates a specific kind of event.

## Payouts

Use the following test bank and debit card numbers to trigger certain events during payout testing. You can only use these values in test mode with test secret keys.

[payout](/connect/payouts-connected-accounts)

Test mode payouts simulate a live payout but aren’t processed with the bank. Test mode accounts with Stripe Dashboard access always have payouts enabled, as long as valid external bank information and other relevant conditions are met, and never requires real identity verification.

You can’t use test bank and debit card numbers in the Stripe Dashboard on a live mode connected account. If you’ve entered your bank account information on a live mode account, you can still use test mode, and test mode payouts will simulate a live payout without processing actual money.

Use these test bank account numbers to test payouts. You can only use them with test secret keys.

Use these test debit card numbers to test payouts to a debit card. These can only be used with test secret keys.
