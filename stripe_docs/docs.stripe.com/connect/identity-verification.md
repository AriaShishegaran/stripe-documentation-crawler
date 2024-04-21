# Identity verification for connected accounts

[account types](https://stripe.com/docs/connect/accounts)

Every country has its own requirements that accounts must meet for Stripe to be able to pay out funds to individuals and companies. These are typically known as Know Your Customer (KYC) requirements. Regardless of the country, broadly speaking, the requirements Stripe must meet are:

[Know Your Customer](https://support.stripe.com/questions/know-your-customer-obligations)

- Collecting information about the individual or company receiving funds

- Verifying information to establish that we know who our customers are

Connect platforms collect the required information from users and provide it to Stripe. This may include information about the legal entity and personal information about the representative of the business, as well as those who own or control the business. Stripe then attempts verification. In some cases, Stripe may be able to verify an account by confirming some or all of the keyed-in data provided. In other cases, Stripe may require additional information, including, for example, a scan of a valid government-issued ID, a proof of address document, or both.

[Connect](/connect)

This page explains the verification flow options to meet Stripe KYC requirements, but the easiest way to manage verification is to integrate Connect Onboarding, which lets Stripe take care of the complexity around the basic KYC obligations associated with an account’s capabilities. Handling the details of account verification is initially complex and requires vigilance to keep up with the constantly evolving regulatory changes around the world.

[Connect Onboarding](/connect/custom/hosted-onboarding)

Stripe recommends using Connect Onboarding. If you decide to handle account verification yourself, continue reading to learn about the verification flow options, how API fields translate to companies and individuals, and how to localize information requests. Also, read Handling Identity Verification with the API to learn how to programmatically provide information and handle requests.

[Handling Identity Verification with the API](/connect/handling-api-verification)

Even after Stripe verifies a connected account, platforms still must monitor for and prevent fraud. Don’t rely on Stripe’s verification to meet any independent legal KYC or verification requirements.

[monitor for and prevent fraud](/connect/risk-management/best-practices#fraud)

## Verification requirements

Verification requirements for connected accounts vary by account, depending on:

- Country

- Capabilities

- Business type (for example, individual, company)

- Business structure (for example, public corporation, private partnership)

- The service agreement type between Stripe and the connected account

- The risk level

You must collect and verify specific information to enable charges and payouts. For example, for a company in the US, you might need to collect:

[payouts](/payouts)

- Information about the business (for example, name, address, tax ID number).

- Information about the person opening the Stripe account (for example, name, date of birth).

- Information about beneficial owners (for example, name, email).

[beneficial owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)

At certain variable thresholds—usually when a specified amount of time has passed or volume of charges have been made—you may need to collect and verify additional information. Stripe temporarily pauses charges or payouts if the information isn’t provided or verified according to the thresholds for required information. For example, additional information might include verification of the company tax ID number.

[required information](/connect/required-verification-information)

## Onboarding flows

As the platform, you must decide if you want to collect the required information from your connected accounts upfront or incrementally. Upfront onboarding collects the eventually_due requirements for the account, while incremental onboarding only collects the currently_due requirements.

- Entails a single request for information (normally)

- Creates fewer problems in receiving payouts and maintaining processing ability

- Exposes potential fraudsters or connected accounts who refuse to provide required information later

- Onboards connected accounts quickly

- Results in higher onboarding rates

- Onboarding connected accounts can take longer

- Some legitimate new connected accounts might turn away due to the amount of information required before they complete the onboarding process

- Creates a higher likelihood of disrupting business of an ongoing connected account

To determine whether to use upfront or incremental onboarding, review the required information for the countries where your connected accounts are located to understand the requirements that are eventually due. While Stripe tries to minimize any impact to connected accounts, requirements might change over time.

[required information](/connect/required-verification-information)

## Business type

The specific KYC information depends on the type of business entity. They are:

[type of business entity](/api/accounts/object#account_object-business_type)

- individual—Collect information about the person.

- company—Collect information about the company. Depending on the countries your connected accounts are in, you might also have to collect information about beneficial owners.

[beneficial owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)

- non_profit—Collect information about the non-profit organization.

- government_entity (available for US connected accounts only)—Collect information about the government entity.

If you or your users are unsure of their entity type, the information might be in the business formation documents or tax documents for that entity.

See the list of requirements for different business types by country. When you know what information to collect, you can read more about handling identity verification with the API.

[list of requirements](/connect/required-verification-information)

[handling identity verification with the API](/connect/handling-api-verification)

## Business structure

For all business types other than individual, you can further classify your user’s business by identifying its legal (business) structure. A business structure describes the details of a business entity such as day-to-day operations, tax burdens, liability, and organizational schema. You can classify it by using company[structure] in the Account object.

[company[structure]](/api/accounts/create#create_account-company-structure)

Providing this information to Stripe gets you the most accurate business classification for compliance purposes. While it isn’t required, it can reduce onboarding requirements. For example, owner information is required for private companies, but not required for public companies. By default, a company is considered private if information on the company.structure isn’t provided.

See the table below for descriptions of the different business structures that you can use to classify a company. Refer to the US required verification information section for more details on requirements.

[US required verification information](/connect/required-verification-information#minimum-verification-requirements-for-united-states)

If you or your users think the entity type should be company but are unsure, the information might be in the business formation documents or tax documents for that entity.

See the table below for descriptions of the different business structures that you can use to classify a non_profit with. Refer to the US required verification information section for more details on requirements.

[US required verification information](/connect/required-verification-information#minimum-verification-requirements-for-united-states)

See the table below for descriptions of the different business structures that you can use to classify a government_entity with. Refer to the US required verification information section for more details on requirements.

[US required verification information](/connect/required-verification-information#minimum-verification-requirements-for-united-states)

## Internationalization and localization

If you support users in multiple countries, consider internationalization and localization when asking for information. Creating an interface that uses not only the user’s preferred language but also the proper localized terminology results in a smoother onboarding experience.

For example, instead of requesting a business tax ID from your users, regardless of country, request:

- EIN, US

- Business Number, Canada

- Company Number, UK

You can find recommended country-specific labels along with the other required verification information.

[required verification information](/connect/required-verification-information)

## See also

- Connect Onboarding for Custom accounts

[Connect Onboarding for Custom accounts](/connect/custom/hosted-onboarding)

- Updating Accounts

[Updating Accounts](/connect/updating-service-agreements)

- Handling Identity Verification with the API

[Handling Identity Verification with the API](/connect/handling-api-verification)

- Account Tokens

[Account Tokens](/connect/account-tokens)

- Required Verification Information

[Required Verification Information](/connect/required-verification-information)

- Testing Custom Account Identity Verification

[Testing Custom Account Identity Verification](/connect/testing-verification)
