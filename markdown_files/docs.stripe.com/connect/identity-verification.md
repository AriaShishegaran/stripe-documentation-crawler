htmlIdentity verification for connected accounts | Stripe Documentation[Skip to content](#main-content)Identity verification for Custom accounts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fidentity-verification)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fidentity-verification)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Required verification information](/docs/connect/required-verification-information)# Identity verification for connected accounts

Use identity verification to reduce risk on your platform when using Connect.### Account types

Connect platforms can work with three different[account types](https://stripe.com/docs/connect/accounts).This content applies only to Custom accounts.Every country has its own requirements that accounts must meet for Stripe to be able to pay out funds to individuals and companies. These are typically known as Know Your Customer (KYC) requirements. Regardless of the country, broadly speaking, the requirements Stripe must meet are:

- Collecting information about the individual or company receiving funds
- Verifying information to establish that we know who our customers are

Connect platforms collect the required information from users and provide it to Stripe. This may include information about the legal entity and personal information about the representative of the business, as well as those who own or control the business. Stripe then attempts verification. In some cases, Stripe may be able to verify an account by confirming some or all of the keyed-in data provided. In other cases, Stripe may require additional information, including, for example, a scan of a valid government-issued ID, a proof of address document, or both.

This page explains the verification flow options to meet Stripe KYC requirements, but the easiest way to manage verification is to integrate Connect Onboarding, which lets Stripe take care of the complexity around the basic KYC obligations associated with an account’s capabilities. Handling the details of account verification is initially complex and requires vigilance to keep up with the constantly evolving regulatory changes around the world.

Stripe recommends using Connect Onboarding. If you decide to handle account verification yourself, continue reading to learn about the verification flow options, how API fields translate to companies and individuals, and how to localize information requests. Also, read Handling Identity Verification with the API to learn how to programmatically provide information and handle requests.

Even after Stripe verifies a connected account, platforms still must monitor for and prevent fraud. Don’t rely on Stripe’s verification to meet any independent legal KYC or verification requirements.

## Verification requirements

Verification requirements for connected accounts vary by account, depending on:

- Country
- Capabilities
- Business type (for example, individual, company)
- Business structure (for example, public corporation, private partnership)
- The service agreement type between Stripe and the connected account
- The risk level

You must collect and verify specific information to enable charges and payouts. For example, for a company in the US, you might need to collect:

- Information about the business (for example, name, address, tax ID number).
- Information about the person opening the Stripe account (for example, name, date of birth).
- Information about[beneficial owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)(for example, name, email).

At certain variable thresholds—usually when a specified amount of time has passed or volume of charges have been made—you may need to collect and verify additional information. Stripe temporarily pauses charges or payouts if the information isn’t provided or verified according to the thresholds for required information. For example, additional information might include verification of the company tax ID number.

## Onboarding flows

As the platform, you must decide if you want to collect the required information from your connected accounts upfront or incrementally. Upfront onboarding collects the eventually_due requirements for the account, while incremental onboarding only collects the currently_due requirements.

Upfront onboardingIncremental onboardingAdvantages- Entails a single request for information (normally)
- Creates fewer problems in receiving payouts and maintaining processing ability
- Exposes potential fraudsters or connected accounts who refuse to provide required information later

- Onboards connected accounts quickly
- Results in higher onboarding rates

Disadvantages- Onboarding connected accounts can take longer
- Some legitimate new connected accounts might turn away due to the amount of information required before they complete the onboarding process

- Creates a higher likelihood of disrupting business of an ongoing connected account

To determine whether to use upfront or incremental onboarding, review the required information for the countries where your connected accounts are located to understand the requirements that are eventually due. While Stripe tries to minimize any impact to connected accounts, requirements might change over time.

## Business type

The specific KYC information depends on the type of business entity. They are:

- `individual`—Collect information about the person.
- `company`—Collect information about the company. Depending on the countries your connected accounts are in, you might also have to collect information about[beneficial owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions).
- `non_profit`—Collect information about the non-profit organization.
- `government_entity`(available for US connected accounts only)—Collect information about the government entity.

If you or your users are unsure of their entity type, the information might be in the business formation documents or tax documents for that entity.

See the list of requirements for different business types by country. When you know what information to collect, you can read more about handling identity verification with the API.

## Business structure

For all business types other than individual, you can further classify your user’s business by identifying its legal (business) structure. A business structure describes the details of a business entity such as day-to-day operations, tax burdens, liability, and organizational schema. You can classify it by using company[structure] in the Account object.

Providing this information to Stripe gets you the most accurate business classification for compliance purposes. While it isn’t required, it can reduce onboarding requirements. For example, owner information is required for private companies, but not required for public companies. By default, a company is considered private if information on the company.structure isn’t provided.

Country:Canada (CA)Germany (DE)Singapore (SG)Thailand (TH)United Arab Emirates (AE)United States (US)### Companies

See the table below for descriptions of the different business structures that you can use to classify a company. Refer to the US required verification information section for more details on requirements.

If you or your users think the entity type should be company but are unsure, the information might be in the business formation documents or tax documents for that entity.

Business structureDescription`multi_member_llc`A business with multiple owners or members that’s registered in a US state as a Limited Liability Company (LLC).`private_corporation`A business incorporated in a US state that’s privately owned. It doesn’t have shares that are traded on a public stock exchange. It’s also called a closely-held corporation. If you’re a single-member LLC that has elected to be treated as a corporation for tax purposes, use this classification.`private_partnership`A business jointly owned by two or more people that’s created through a partnership agreement.`public_corporation`A business incorporated under the laws of a US state. Ownership shares of this corporation are traded on a public stock exchange.`public_partnership`A business formed by a partnership agreement with one or more people, but has shares that are publicly traded on a stock exchange.`single_member_llc`A business entity registered with a US state as a limited liability company (LLC) and that has only one member or owner.`sole_proprietorship`A business that isn’t a separate legal entity from its individual owner.`unincorporated_association`A business venture of two or more people that doesn’t have a formal corporate or entity structure.### Non-profits

See the table below for descriptions of the different business structures that you can use to classify a non_profit with. Refer to the US required verification information section for more details on requirements.

Business structureDescription`incorporated_non_profit`An organization incorporated under the laws of a US state that has obtained tax-exempt status as a non-profit entity under either state or federal law (for example, 501(c)(3)).`unincorporated_non_profit`An organization that’s pursuing an objective other than profits, such as a social cause, and has obtained tax-exempt status in the US under either state or federal law (for example, 501(c)(3)) but hasn’t formally incorporated.### Government entities

See the table below for descriptions of the different business structures that you can use to classify a government_entity with. Refer to the US required verification information section for more details on requirements.

Business structureDescription`government_instrumentality`An organization formed by a government statute or body based in the US to perform a certain function, but not the actual government body itself.`governmental_unit`A branch of the state, local, or federal government of the US`tax_exempt_government_instrumentality`An organization created by or pursuant to government statute and operated for public purposes. It has obtained federal tax-exempt status under state or federal law (for example, 501(c)(3)).## Internationalization and localization

If you support users in multiple countries, consider internationalization and localization when asking for information. Creating an interface that uses not only the user’s preferred language but also the proper localized terminology results in a smoother onboarding experience.

For example, instead of requesting a business tax ID from your users, regardless of country, request:

- EIN, US
- Business Number, Canada
- Company Number, UK

You can find recommended country-specific labels along with the other required verification information.

## See also

- [Connect Onboarding for Custom accounts](/connect/custom/hosted-onboarding)
- [Updating Accounts](/connect/updating-service-agreements)
- [Handling Identity Verification with the API](/connect/handling-api-verification)
- [Account Tokens](/connect/account-tokens)
- [Required Verification Information](/connect/required-verification-information)
- [Testing Custom Account Identity Verification](/connect/testing-verification)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Verification requirements](#verification-requirements)[Onboarding flows](#onboarding-flows)[Business type](#business-type)[Business structure](#business-structure)[Internationalization and localization](#internationalization-and-localization)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`