# Upcoming requirements updates

Payments regulations aim to create a safer, more secure financial ecosystem by helping prevent crimes such as money laundering, fraud, and tax evasion. Financial regulators around the world enforce Know Your Customer (KYC) requirements to make sure that identity information is collected, verified, and maintained from certain types of businesses, and for any individuals who ultimately own, control, or direct the business. These requirements are frequently updated by financial service regulators, card networks, and other financial institutions.

[Know Your Customer (KYC) requirements](https://support.stripe.com/questions/know-your-customer)

This guide provides an overview of the upcoming changes, and highlights the most significant changes. For the exhaustive list of requirements, refer to Required verification information.

[Required verification information](/connect/required-verification-information)

To change how you integrate with Stripe, see Onboarding solutions for Custom accounts.

[Onboarding solutions for Custom accounts](/connect/custom/onboarding)

Last updated: January 4, 2023

## What’s changing

- Required information collected from connected accounts: We’re updating the information we require from sole proprietorships, non-profits and single-member LLCs and simplifying how we obtain legal guardian consent for accounts opened by minors. In addition, an email for the account representative is now required for all legal entity types, and a change for government entities and public companies.

- How we verify business information and provide new detailed verification responses: We’re updating our criteria for valid business information and introducing new verification error codes when we unable to accept or verify information provided.

- Threshold at which we verify tax identification numbers (TINs): For Custom and Express connected accounts, we’re lowering the payments volume threshold at which we verify TINs to align with current federal tax reporting thresholds.

- How we prefill statement descriptors and statement descriptor prefixes: If a statement descriptor isn’t provided, the prefill logic has changed to use either the business profile name, the business URL, or the legal entity name of the connected account.

These changes will affect all users with a requested card_payments capability in the US.

[card_payments](/api/accounts/object#account_object-capabilities-card_payments)

## Required information collected from connected accounts

New information collected and new fields added to the API:

- Businesses that are company.structure of sole_proprietorship and single_member_llc, must provide their business address (“company address”). In the event that the business address is the same as the representative’s personal address, your connected accounts can provide the same values for both.

[company.structure](/api/accounts/create#create_account-company-structure)

- Legal entities that are company.structure of government_instrumentality, tax_exempt_government_instrumentality, governmental_unit, public_company, and public_corporation, public_partnership must provide an email for the account representative. This requirement now applies to all legal entity types.

[company.structure](/api/accounts/create#create_account-company-structure)

- To simplify how we obtain a legal guardian’s consent for accounts opened by minors, the Persons API has been updated with a new relationship type of legal_guardian as well as an additional_tos_acceptances field to record the legal guardian’s agreement to the Stripe Terms of Service. If the account representative’s date of birth indicates the individual is a minor, then an account requirement is triggered to add a legal_guardian before the account can be activated.

[Persons API](/api/persons)

## How we verify business information and provide new detailed verification responses

We’ll request the following information from your connected accounts:

When we’re unable to verify information provided by your connected accounts, we’ll surface detailed verification responses as new error codes in the requirements.errors array. View docs.

[requirements.errors](/api/accounts/object#account_object-requirements-errors)

[View docs](/connect/handling-api-verification#validation-and-verification-errors)

To align with the IRS reporting thresholds for Forms 1099-K, 1099-NEC, and 1099-MISC, we’re updating the threshold at which we verify the TIN to when your payments volume reaches $600 or within 30 days of first charge, whichever comes first.

If not provided, the statement descriptor is prefilled using the following supplied fields (in this order): business_profile.name (“doing business as”), business_profile.url, the legal entity name (either individual.first_name + individual.last_name or company.name)`. In addition, if the statement descriptor prefix isn’t provided, it’s prefilled from the first 10 characters of the statement descriptor.

[business_profile.name](/api/accounts/object#account_object-business_profile-name)

[business_profile.url](/api/accounts/object#account_object-business_profile-url)

[individual.first_name](/api/accounts/object#account_object-individual-first_name)

[individual.last_name](/api/accounts/object#account_object-individual-last_name)

[company.name](/api/accounts/object#account_object-company-name)

## See also

- Connect onboarding for Custom accounts

[Connect onboarding for Custom accounts](/connect/custom/hosted-onboarding)

- Onboarding solutions for Custom accounts

[Onboarding solutions for Custom accounts](/connect/custom/onboarding)

- Required verification information

[Required verification information](/connect/required-verification-information)

- Updating accounts

[Updating accounts](/connect/updating-service-agreements)

- Handling identity verification with the API

[Handling identity verification with the API](/connect/handling-api-verification)

- Testing Custom account identity verification

[Testing Custom account identity verification](/connect/testing-verification)

- Accepted verification documents

[Accepted verification documents](/acceptable-verification-documents)
