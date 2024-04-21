# Treasury platform end user onboarding guide

With Stripe Treasury, platforms can offer financial services that offer fraud prevention and regulatory compliance. Use this guide to onboard your users and reduce friction in the onboarding process.

Know Your Customer (KYC) and Know Your Business (KYB) are client data collection procedures that financial services providers must employ to verify a user’s identity and prevent fraud or financial crimes. Building a compliant KYC process is one key part of the onboarding process. The onboarding flow also improves customer conversion rates, mitigates risk, and helps your customers be successful with your product.

This guide describes how to build your onboarding process, including:

- How to maintain a compliant KYC and KYB flow

- How to create efficient and frictionless customer onboarding

- How to implement onboarding to Stripe Treasury (hosted versus custom)

## KYC and KYB onboarding

Before you launch your embedded finance capabilities, implement an onboarding flow that collects the necessary KYC and KYB information from your users. The US Financial Crimes Enforcement Network (FinCEN) sets and enforces the requirements for customer due diligence, which each financial institution or partner can then supplement with additional requirements.

[US Financial Crimes Enforcement Network](https://www.fincen.gov/resources/statutes-and-regulations/cdd-final-rule#:~:text=It%20requires%20covered%20financial%20institutions,owners%20of%20companies%20opening%20accounts)

With Treasury, Stripe only presents your platform with the core requirements needed for your business to be compliant while onboarding users. You, as the platform, are then responsible for collecting the required KYC information from your platform’s connected account owners and passing it to Stripe using Hosted Onboarding or through the Stripe API. After you collect this data, Stripe performs checks to determine if these connected accounts meet KYC and KYB requirements and flag potential risks of money laundering or fraud. These checks include:

[Hosted Onboarding](/connect/custom/hosted-onboarding)

[Stripe API](/connect/custom-accounts#create)

- Verifying ID documents against public and private databases to make sure they’re valid

- Screening application information against lists of criminals (such as known terrorists and money launderers)

- Checking applicant information against databases of known fraudulent actors

- Validating addresses

- Making sure that the application is from a registered business with the appropriate licenses

Information you need to collect to open a Treasury financial account for your end users include (but aren’t limited to):

- Business name

- Legal entity type

- Tax ID number

- Merchant category code (MCC)

- Company name

- Company address

- Company owner information

- SSN of company owners

- Owners dates of birth

- Owner title

- Ownership percent of company

You can review the full requirements for opening a Financial Account associated with a Connected Account here.

[here](/connect/required-verification-information#US-full-company--card_payments%7Ctransfers%7Cus_bank_account_ach_payments)

## Ways to onboard end users to Treasury

You can use two methods to onboard your users onto Connect and Treasury—use the Stripe hosted onboarding flow or the Stripe API to pass verification information to Stripe.

Both options offer different benefits:

- With Stripe hosted onboarding, you don’t need to design or build a custom onboarding UI. Stripe provides a customizable web form that collects the required identity information from your users.

[Stripe hosted onboarding](/connect/custom/hosted-onboarding)

- Hosted onboarding dynamically adjusts input fields depending on account capabilities, product usage, country, and business type.

- You can use hosted onboarding if you need support for mobile browsers, accessibility, and localization.

- Hosted onboarding allows you to automatically collect all currently required information up front or incrementally, depending on what’s needed from the user (see onboarding flows for more information). To use Stripe Treasury, end users must provide all information to satisfy KYC requirements, whereas information collection can be incremental for Stripe Payments onboarding.

[onboarding flows](/connect/identity-verification#onboarding-flows)

- API onboarding (custom onboarding) gives you full control over the onboarding UI and user experience.

[API onboarding (custom onboarding)](/connect/custom-accounts#create)

- You don’t need to redirect users to an external Stripe-hosted page.

- You can design the information collection flow for your users.

## Keep up with changing requirements

Changing requirements can necessitate gathering additional information from users. While hosted onboarding dynamically updates to reflect new requirements, platforms using API onboarding need to make sure they update their UI and collect this information. If a user has already onboarded using hosted onboarding and the requirements change, forwarding them the hosted onboarding link to hosted prompts them to provide the new required information. You can obtain new requirements for accounts using the methods detailed in the Required verification information guide.

[Required verification information](/connect/required-verification-information)

You can also use a mixture of hosted and API onboarding. If you use hosted onboarding but have already collected some information from users from a different source, you can pass this information to Stripe through the identity verification process and prefill the hosted onboarding page with the provided information. In this case, the user can modify or verify the information within the Stripe-hosted UI.

[identity verification process](/connect/custom-accounts#identity-verification)

## Tips for onboarding

To make sure onboarding is successful and boost user conversion for your Treasury product, keep the following tips in mind:

- Consider onboarding users to the treasury capability to start, even if you don’t plan to create a Treasury financial account until later. If you decide to perform Treasury onboarding later, set clear expectations during onboarding that additional information might be required to use all aspects of the product to head off any potential friction.

Consider onboarding users to the treasury capability to start, even if you don’t plan to create a Treasury financial account until later. If you decide to perform Treasury onboarding later, set clear expectations during onboarding that additional information might be required to use all aspects of the product to head off any potential friction.

- If you already have a Connect integration, or have otherwise collected identifying information from your end users, you can use the API to pass data you already have to reduce the amount of information a user needs to provide through hosted onboarding.

If you already have a Connect integration, or have otherwise collected identifying information from your end users, you can use the API to pass data you already have to reduce the amount of information a user needs to provide through hosted onboarding.

- For issued cards, provide the card use case to help users understand how it works.

For issued cards, provide the card use case to help users understand how it works.

- If a user has recently incorporated their business, they might not have their TIN entered in the IRS database yet, so their TIN might come back as unverified until the IRS database updates. The account is still usable, and Stripe periodically attempts to reverify the TIN.

If a user has recently incorporated their business, they might not have their TIN entered in the IRS database yet, so their TIN might come back as unverified until the IRS database updates. The account is still usable, and Stripe periodically attempts to reverify the TIN.

- Hosted onboarding allows you to test out your integration. If you want more customization, you can switch to custom onboarding.

Hosted onboarding allows you to test out your integration. If you want more customization, you can switch to custom onboarding.

- Only onboard users that are supportable on Stripe and Treasury. Review the Treasury requirements for supportability, and the guidelines on how to market Treasury to users.

Only onboard users that are supportable on Stripe and Treasury. Review the Treasury requirements for supportability, and the guidelines on how to market Treasury to users.

[Treasury requirements](/treasury/requirements)

[market Treasury to users](/treasury/compliance)

- Offering incentives to onboard, such as a free subscription period or incentive funds, can help boost early user activation and engagement.

Offering incentives to onboard, such as a free subscription period or incentive funds, can help boost early user activation and engagement.

- Incremental versus upfront onboarding documentation

[Incremental versus upfront onboarding documentation](/connect/identity-verification#onboarding-flows)

- Testing API onboarding

[Testing API onboarding](/connect/testing-verification)

- Connect onboarding documentation

[Connect onboarding documentation](/connect/custom/hosted-onboarding)

- Treasury documentation on opening Custom Connect accounts

[Treasury documentation on opening Custom Connect accounts](/treasury/account-management/connected-accounts#requirements)

- Documentation on opening Treasury financial accounts

[Documentation on opening Treasury financial accounts](/treasury/account-management/financial-accounts)
