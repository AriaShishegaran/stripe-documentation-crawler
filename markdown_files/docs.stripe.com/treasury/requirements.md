htmlTreasury requirements | Stripe Documentation[Skip to content](#main-content)Treasury requirements[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Frequirements)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Frequirements)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)[Treasury](#)
[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Treasury](/treasury)·[Home](/docs)[Banking as a service](/docs/financial-services)[Treasury](/docs/treasury)# Treasury requirements

Understand the requirements for using Stripe Treasury.Treasury has additional compliance requirements from those needed for Stripe Payments. These requirements apply to both the platform and the connected accounts created for sellers and service providers that use the platform. For a smooth onboarding experience, follow these guidelines to make sure you offer your Treasury-based financial services only to businesses that meet the requirements.

## Supported countries

Stripe Treasury is available only to platforms and connected accounts located in the United States.

## Business use cases only

Stripe Treasury is currently available only to platforms with business use cases. Stripe isn’t offering financial accounts to consumers or providing Treasury for consumer purposes.

## Connected account types

Stripe Treasury is available only for integrations that use Custom connected accounts. As a user with a Custom connected account, you’re responsible for maintaining a minimum API version, communicating terms of service updates to your users, handling information requests from your users, and providing user support. In addition, as your platform is ultimately responsible for losses Custom accounts incur, you’re responsible for vetting your users for fraud. To learn more about platform responsibilities for Custom accounts, see Using Connect with Custom accounts.

## Supported countries of residence

Stripe Treasury currently supports businesses in the US only, but the business owners and authorized persons of those businesses can reside in over 150 countries. Some countries of residence, however, might require a more detailed review before you can onboard them to your platform.

Stripe prohibits using Treasury for any dealings, engagement, or sale of goods or services linked directly or indirectly with jurisdictions Stripe has deemed high risk, such as Cuba, Iran, North Korea, Crimea region, and Syria.

### Standard review countries of residence

Business owners, beneficial owners, and authorized persons that have a primary address in one of the following countries are supported, typically without an enhanced review:

- Australia
- Austria
- Belgium
- Bermuda
- Canada
- Chile
- Czech Republic
- Denmark
- Germany
- Finland
- France
- Gibraltar
- Greece
- Guam
- Hong Kong
- Iceland
- Ireland
- Isle of Man
- Italy
- Japan
- Jersey
- Korea
- Luxembourg
- Netherlands
- New Zealand
- Norway
- Poland
- Portugal
- Puerto Rico
- Singapore
- Slovakia
- Slovenia
- South Africa
- Spain
- Sweden
- Switzerland
- Taiwan
- United Kingdom
- United States
- Virgin Islands, British
- Virgin Islands, US

### Enhanced review countries of residence

Business owners, beneficial owners, and authorized persons that have a primary address in one of the following countries are supported, but subject to an enhanced review:

- Albania
- Algeria
- Andorra
- Angola
- Antigua and Barbuda
- Argentina
- Armenia
- Bahamas
- Bahrain
- Bangladesh
- Barbados
- Belize
- Benin
- Bhutan
- Bolivia
- Botswana
- Brazil
- Brunei
- Bulgaria
- Burkina Faso
- Cambodia
- Cameroon
- Cape Verde
- Cayman Islands
- China
- Colombia
- Comoros
- Costa Rica
- Croatia
- Cyprus
- Djibouti
- Dominica
- Dominican Republic
- East Timor
- Ecuador
- Egypt
- El Salvador
- Estonia
- Eswatini
- Ethiopia
- Fiji
- Gabon
- Georgia
- Ghana
- Grenada
- Guatemala
- Guernsey
- Guyana
- Honduras
- Hungary
- India
- Indonesia
- Israel
- Jamaica
- Jordan
- Kazakhstan
- Kenya
- Kiribati
- Kuwait
- Kyrgyzstan
- Laos
- Latvia
- Lesotho
- Liechtenstein
- Lithuania
- Macau
- North Macedonia
- Madagascar
- Malawi
- Maldives
- Malta
- Marshall Islands
- Mauritius
- Mexico
- Micronesia
- Moldova
- Monaco
- Mongolia
- Montenegro
- Morocco
- Mozambique
- Namibia
- Nepal
- Nicaragua
- Oman
- Palau
- Panama
- Papua New Guinea
- Paraguay
- Peru
- Philippines
- Qatar
- Republic of the Congo
- Romania
- Rwanda
- Samoa
- San Marino
- Saudi Arabia
- Senegal
- Serbia
- Seychelles
- Solomon Islands
- Sri Lanka
- St Lucia
- St Vincent and the Grenadines
- Suriname
- Tajikistan
- Tanzania
- Thailand
- The Gambia
- Togo
- Tonga
- Tunisia
- Turkey
- Tuvalu
- Uruguay
- Vietnam
- Zambia

## Prohibited and restricted business types

The businesses and business practices in the following categories are either restricted or prohibited from using Stripe Treasury. Financial network rules or the requirements of our financial services providers might determine whether Stripe can provide services. In some cases, a business in one of the categories may use Treasury after getting explicit approval from Stripe.

WarningBusinesses that offer illegal products or services are never eligible to use Stripe Treasury.

For more information about businesses restricted by Stripe Payments, and by extension Treasury, see Prohibited and Restricted Businesses.

### Prohibited business types

The businesses and business practices in the following categories are classified as prohibited and are therefore not eligible to use Treasury:

- Adult industry, escort, or dating services
- Arms trading—retail or manufacturing
- Casinos or gaming
- Cryptocurrency
- Marijuana, tobacco, or illegal drug products and services
- Money services and currency exchange
- Unfair, predatory, or deceptive practices, including multi-level marketing and pyramid schemes
- Payday lending and tax anticipation programs
- Stock promotion
- Tattoo and massage parlors
- Waste or hazardous material management

### Restricted business types

The following categories of businesses and business practices are classified as restricted and subject to enhanced review:

Regulated industries such as:![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Virtual currencies and cryptocurrencies, non-fungible tokens (NFTs), and mining services
- Investment and brokerage services
- Insurance services
- Debt collection, debt relief, and credit restoration agencies
- Bail bonds
- Lending and cash advance services
- Student loan assistance companies
- Unregistered charities

Businesses that may pose elevated financial risk such as:![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Art dealers, antique dealers, or auction houses
- Import, export, and freight transport of physical commodities
- Jewelry, gems, precious metals—dealers or wholesalers
- Games of skill and chance, including lotteries, fantasy sports, and sweepstakes
- Direct marketing businesses, including telemarketing, “As Seen on TV”, and door-to-door sales
- Telecommunication or surveillance equipment providers
- Talent and model agencies
- Vehicle sales
- Secondhand shops and pawnshops
- Warranties and lifetime guarantees
- Travel agencies, including tour operators, hotel reservation services, and resort promotions
- Pharmaceutical, vitamin, and supplement sales

## Politically exposed persons

Stripe screens users’ applications to identify if any are a politically exposed person (PEP). All PEPs are subject to enhanced review.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Supported countries](#supported-countries)[Business use cases only](#business-use-cases-only)[Connected account types](#connected-account-types)[Supported countries of residence](#supported-countries-of-residence)[Prohibited and restricted business types](#prohibited-and-restricted-business-types)[Politically exposed persons](#politically-exposed-persons)Products Used[Treasury](/treasury)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`