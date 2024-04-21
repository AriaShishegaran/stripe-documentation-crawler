htmlUpcoming requirements updates | Stripe Documentation[Skip to content](#main-content)Upcoming requirements updates[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fupcoming-requirements-updates)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fupcoming-requirements-updates)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Upcoming requirements updates

Learn about the changes to required verification information and how this impacts your integration with Stripe.Payments regulations aim to create a safer, more secure financial ecosystem by helping prevent crimes such as money laundering, fraud, and tax evasion. Financial regulators around the world enforce Know Your Customer (KYC) requirements to make sure that identity information is collected, verified, and maintained from certain types of businesses, and for any individuals who ultimately own, control, or direct the business. These requirements are frequently updated by financial service regulators, card networks, and other financial institutions.

This guide provides an overview of the upcoming changes, and highlights the most significant changes. For the exhaustive list of requirements, refer to Required verification information.

To change how you integrate with Stripe, see Onboarding solutions for Custom accounts.

Program:USCanadaSingaporeLast updated: January 4, 2023

## What’s changing

- Required information collected from connected accounts:We’re updating the information we require from sole proprietorships, non-profits and single-member LLCs and simplifying how we obtain legal guardian consent for accounts opened by minors. In addition, an email for the account representative is now required for all legal entity types, and a change for government entities and public companies.
- How we verify business information and provide new detailed verification responses:We’re updating our criteria for valid business information and introducing new verification error codes when we unable to accept or verify information provided.
- Threshold at which we verify tax identification numbers (TINs):For Custom and Express connected accounts, we’re lowering the payments volume threshold at which we verify TINs to align with current federal tax reporting thresholds.
- How we prefill statement descriptors and statement descriptor prefixes:If a statement descriptor isn’t provided, the prefill logic has changed to use either the business profile name, the business URL, or the legal entity name of the connected account.

These changes will affect all users with a requested card_payments capability in the US.

## Required information collected from connected accounts

New information collected and new fields added to the API:

- Businesses that are[company.structure](/api/accounts/create#create_account-company-structure)of`sole_proprietorship`and`single_member_llc`, must provide their business address (“company address”). In the event that the business address is the same as the representative’s personal address, your connected accounts can provide the same values for both.
- Legal entities that are[company.structure](/api/accounts/create#create_account-company-structure)of`government_instrumentality`,`tax_exempt_government_instrumentality`,`governmental_unit`,`public_company`, and`public_corporation`,`public_partnership`must provide an email for the account representative. This requirement now applies to all legal entity types.
- To simplify how we obtain a legal guardian’s consent for accounts opened by minors, the[Persons API](/api/persons)has been updated with a new relationship type of`legal_guardian`as well as an`additional_tos_acceptances`field to record the legal guardian’s agreement to the Stripe Terms of Service. If the account representative’s date of birth indicates the individual is a minor, then an account requirement is triggered to add a`legal_guardian`before the account can be activated.

## How we verify business information and provide new detailed verification responses

### Updates to the information we already collect

We’ll request the following information from your connected accounts:

FieldUpdated requirementsAdditional considerationsSSN or ITIN collected from US-resident Representatives (Reps)Last 4 digits required at onboarding for all account types (including Custom and Express connected accounts)This is the current behavior for Standard connected accountsSSN or ITIN collected from US-resident Representatives (Reps)If the last 4 digits fail to verify at onboarding, Reps will need to provide the full 9 digits at onboardingSSN or ITIN collected from US-resident Representatives (Reps) or OwnersFull 9 digits required once payments volume exceeds $500KA Representative (Rep) is defined as a person with significant responsibility to control, manage, or direct the organization; and is authorized by the organization to agree to Stripe’s terms. For a representative, the full 9 digits are required at $500K only if no Owners are listed on the account.### New verification error codes

When we’re unable to verify information provided by your connected accounts, we’ll surface detailed verification responses as new error codes in the requirements.errors array. View docs.

Synchronous errors![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

FieldNew error codeError messageProduct Description`invalid_product_description_length`Your product description must be at least 10 characters.Product Description`invalid_product_description_url_match`Your product description must be different from your URL.(Full) Statement Descriptor`invalid_statement_descriptor_length`Your statement descriptor must be between 5 and 22 characters.(Full) Statement Descriptor`invalid_statement_descriptor_business_mismatch`Your statement descriptor must be similar to your business name, legal entity name, or URL.(Full) Statement Descriptor`invalid_statement_descriptor_denylisted`Generic or well-known statement descriptors aren’t supported.(Short) Statement Descriptor`invalid_statement_descriptor_prefix_mismatch`The statement descriptor prefix must be similar to your statement descriptor, business name, legal entity name, or URL.(Short) Statement Descriptor`invalid_statement_descriptor_prefix_denylisted`Generic or well-known statement descriptor prefixes aren’t supported.LE Business Name`invalid_company_name_denylisted`Generic or well-known business names aren’t supported.Business Profile Name (DBA)`invalid_business_profile_name_denylisted`Generic or well-known business names aren’t supported.Business Profile Name (DBA)`invalid_business_profile_name`Business profile names must consist of recognizable words.Persons DOB`invalid_dob_age_under_minimum`Person must be at least 13 years old.Persons DOB`invalid_dob_age_over_maximum`Date of birth must be within in the last 120 years.Persons phone`invalid_phone_number`The phone number doesn’t seem to be valid. Make sure it’s formatted correctly.LE Business Phone`invalid_phone_number`The phone number doesn’t seem to be valid. Make sure it’s formatted correctly.Company TaxID`invalid_tax_id_format`Tax IDs must be a unique set of 9 numbers without dashes or other special characters.URL`invalid_url_format`Format as https://example.comURL`invalid_url_denylisted`Generic business URLs aren’t supported.Asynchronous errors![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

FieldNew error codeError messageURL`invalid_url_website_inaccessible`This URL couldn’t be reached. Make sure it’s available and entered correctly or provide another.URL`invalid_url_website_business_information_mismatch`The business information on your website must match the details you provided to Stripe.URL`invalid_url_website_incomplete`Your website seems to be missing some required information. Learn about website requirementsURL`invalid_url_website_other`We weren’t able to verify your business using the URL you provided. Make sure it’s entered correctly or provide another URL.URL`invalid_url_web_presence_detected`Because you use a website, app, social media page, or online profile to sell products or services, you must provide a URL for your business.### Update to the threshold at which we verify tax identification numbers (TINs)

To align with the IRS reporting thresholds for Forms 1099-K, 1099-NEC, and 1099-MISC, we’re updating the threshold at which we verify the TIN to when your payments volume reaches $600 or within 30 days of first charge, whichever comes first.

### How we prefill statement descriptors and statement descriptor prefixes

If not provided, the statement descriptor is prefilled using the following supplied fields (in this order): business_profile.name (“doing business as”), business_profile.url, the legal entity name (either individual.first_name + individual.last_name or company.name)`. In addition, if the statement descriptor prefix isn’t provided, it’s prefilled from the first 10 characters of the statement descriptor.

## See also

- [Connect onboarding for Custom accounts](/connect/custom/hosted-onboarding)
- [Onboarding solutions for Custom accounts](/connect/custom/onboarding)
- [Required verification information](/connect/required-verification-information)
- [Updating accounts](/connect/updating-service-agreements)
- [Handling identity verification with the API](/connect/handling-api-verification)
- [Testing Custom account identity verification](/connect/testing-verification)
- [Accepted verification documents](/acceptable-verification-documents)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[What’s changing](#what’s-changing)[Required information collected from connected accounts](#required-information-collected-from-connected-accounts)[How we verify business information and provide new detailed verification responses](#how-we-verify-business-information-and-provide-new-detailed-verification-responses)[Why this is happening](#why-this-is-happening)[What’s changing](#what’s-changing)[Non-profit organization and registered charity classification](#non-profit-organization-and-registered-charity-classification)[Legal entity and personal information collected](#legal-entity-and-personal-information-collected)[How legal entity and personal information is verified](#how-legal-entity-and-personal-information-is-verified)[New verification error codes](#new-verification-error-codes)[When information collection and verification is required](#when-information-collection-and-verification-is-required)[Identity verification provider](#identity-verification-provider)[What’s changing](#what’s-changing)[Business types and structures supported](#business-types-and-structures-supported)[Required business and personal information](#required-business-and-personal-information)[How we verify business and personal information](#how-we-verify-business-and-personal-information)[New verification error codes](#new-verification-error-codes)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`