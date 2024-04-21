htmlMigrating accounts to Stripe | Stripe Documentation[Skip to content](#main-content)Migrate to Stripe[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fmigrate-to-stripe)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fmigrate-to-stripe)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Migrating accounts to Stripe

Start processing accounts on Stripe without disrupting payments.Stripe enables you to migrate your existing connected accounts along with your payment and customer data. Doing so allows you to continue to collect payments and pay out or enable other businesses to accept payments directly. To successfully bring your existing platform business to Stripe, you need to:

1. Create a migration plan and timeline
2. Update your integration for connected accounts
3. Create and onboard accounts
4. Handle outstanding and ongoing requirements
5. Migrate payment and customer data to Stripe

## Create a migration plan

A successful migration to Stripe includes a migration plan, a timeline, and KYC information for connected accounts, as well as payment and customer data.

Connected accounts must onboard to Stripe, which requires sending Stripe Know Your Customer (KYC) data for each account. Stripe’s requirements can require collecting additional information from your accounts. Perform an analysis to understand what data has been collected with your previous provider and what data Stripe requires. Stripe verifies KYC data before activating connected accounts. Monitor account verification status using the account.updated event or the Retrieve Account API. Accounts that fail to verify require action before they’re activated.

Include a hard cutover date for payment data after onboarding accounts to Stripe. Payment and customer data requires a PAN import as part of the cutover. We recommend that you import accounts in batches.

## Update your integration

Your application can require changes as part of the integration updates to migrate to Stripe. For example, consider any changes to your connected accounts’ usage of your platform, such as pricing updates. Stripe recommends communicating any changes to your accounts ahead of time.

### Stripe terms of service agreement

Your connected accounts must accept the Stripe terms of service before they’re activated.

For accounts where Stripe is responsible for collecting updated information when requirements are due or change (including Standard and Express accounts), the account accepts Stripe’s terms of service as part of the onboarding flow.

For Custom accounts, you can wrap Stripe’s terms of service in your own terms of service. We recommend placing terms of service acceptance at the end of the onboarding flow, but you can also have it at the start if that makes more sense for your business. When creating or updating connected accounts, record acceptance of the updated Terms of Service information to send to Stripe, and communicate that to the accounts.

### Onboard connected accounts to Stripe

Stripe offers different levels of onboarding support for your connected accounts. Build an onboarding flow for your connected accounts using any of the following methods:

MethodProsCons[API-based onboarding](/connect/custom/onboarding#api-based-onboarding)Exercise full control over your own UI- Expensive and time-consuming to build
- Continuing high maintenance, especially to keep in compliance with changing global requirements
- Can’t resolve Stripe risk reviews

[Embedded onboarding](/connect/custom/onboarding#embedded-onboarding)new- [Highly themeable](/connect/customize-connect-embedded-components)
- Limited or no Stripe branding
- Connected accounts remain in the flow of your site
- Low effort integration

Limited control over the flow logic[Stripe-hosted onboarding](/connect/custom/onboarding#stripe-hosted-onboarding)Lowest effort integration- Stripe-branded with limited platform branding
- Limited control over the flow logic
- Connected accounts redirect to Stripe instead of completing the process without leaving your site

## Create and onboard accounts

The following is an overview of the process:

### Establish account requirements

The following factors affect the onboarding requirements for your connected accounts:

- The origin country of the connected accounts
- The[service agreement type](/connect/service-agreement-types)applicable to the connected accounts
- The[capabilities](/connect/account-capabilities)requested for the connected accounts
- The[business type](/api/accounts/object#account_object-business_type)(for example, individual or company) and[company.structure](/api/accounts/object#account_object-company-structure)(for example, public corporation or private partnership)

The following interactive form shows how these factors affect the requirements by letting you set different values for them.

Inspect all the requirements necessary for your selected combinations. Pay particular attention to the Requirement column. That column lists specific parameters on the account that you must collect to onboard it with the capabilities requested. Some parameters are only required at certain thresholds, as noted in the Required Before column.

Loading required verification informationProcessing live charges and receiving payouts![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

In the UAE, company documents such as the Trade License and Proof of Bank Account as well as relevant identity documents must be verified before a connected account can start processing live charges and receiving payouts. For all businesses except sole establishments and free zone establishments, the Memorandum of Association must be verified as well.

Uploading identity documents![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

For the company representative, beneficial owner(s) and executive(s), we require the following identity documents for verification:

- Passport: all individuals
- Emirates ID: UAE nationals & UAE residents
- Residence visa: foreign nationals who are resident in the UAE

The Emirates ID can be provided in the parameter called verification.document. Passport(s) and residence visa(s) should be provided under a separate parameter called documents.

Keeping up to date with expired verification documents![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

In the UAE, Stripe is required to keep up to date with a company’s Trade License in addition to the primary identity document of the company’s representative, beneficial owners and executives. The primary identity document is either the Emirates ID for UAE nationals and residents, otherwise it is an individual’s Passport. Companies will have up to 28 days after the expiry date of these documents to provide an updated version. Expired documents will appear under company requirements or individual requirements and marked as currently due for two weeks before capabilities become disabled.

Ultimate Beneficial Owners![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Stripe is required to verify all the beneficial owners of a business. These are the individuals who own 25% or more of the primary business. If a holding company has 25% or more ownership of the business, then the Memorandum of Association of this holding company as well that of the primary business must be uploaded. These documents must show the person(s) where relationship.owner is set to true.

Additional information on the company representative![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

This connected account needs to be activated by a person, known as the company representative, with significant responsibility to control, manage, or direct the organization and is authorized by the organization to agree to Stripe’s terms. The representative must either be an owner or an executive, which you specify by setting relationship.owner to true or relationship.executive to true. For a sole establishment or free zone establishment, the account must be activated by the owner of the business.

VAT Information![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Stripe does not charge UAE VAT on Stripe fees to customers located in the UAE, where a valid UAE VAT ID has been provided. Local UAE VAT self-assessment obligations may be triggered upon receipt of a monthly invoice from Stripe. Stripe does charge UAE VAT at 5% on Stripe fees to customers located in the UAE, where a valid UAE VAT ID hasn’t been provided.

Power of Attorney![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If the company representative does not appear on the company’s Trade License or the Memorandum of Association, then you must upload a Power of Attorney that shows that the company representative has the authority to act on behalf of the company or a notarized letter of authorization.

Supported business structures![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

In the UAE, the only possible business type is company and the following business structures are accepted:

- `sole_establishment`
- `free_zone_establishment`
- `llc`
- `free_zone_llc`

Additional information on the account![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If Stripe is unable to verify the company, or if there are possible concerns about sanctions, you must collect a proof-of-entity document to enable payouts. Collect it using the company.verification.document.front and company.verification.document.back arguments.

Additional information on the individual![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Depending on the situation, you might need to collect a scan of an ID document to enable payouts. That can happen if Stripe is unable to verify the individual or if there are possible concerns about sanctions.

Collect ID information using the individual.verification.document.front and individual.verification.document.back arguments.

Additional information on the representative![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

A person known as a representative must activate this connected account. This person must be a beneficial owner who is authorized to sign for the company. Indicate this relationship to Stripe by setting relationship.executive to true, or, if the representative owns 25% or more of the company, by setting relationship.owner to true.

Depending on the situation, you might need to collect a scan of an ID document to enable payouts. That can happen if Stripe is unable to verify the representative or if there are possible concerns about sanctions. Collect ID information using the verification.document.front and verification.document.back arguments.

Optionally, you can collect the representative’s ownership information using relationship.representative and relationship.percent_ownership.

Additional information on directors![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

For companies (excluding partnerships), you must collect information on all directors. Directors are members of the governing board of the company. When you have finished collecting the required information from all directors, or if your company does not have any directors, you must inform Stripe by setting company.directors_provided to true.

If there are possible concerns about sanctions, you must collect a scan of an ID document to enable payouts. Collect ID information using the verification.document.front and verification.document.back arguments.

Additional information on beneficial owners (for both executives and owners)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You must collect information on all beneficial owners. Beneficial owners are persons who exercise significant management control over the company (executives) or who own 25% or more of the company (owners). When you have finished collecting the required information from all beneficial owners, you must inform Stripe by setting both company.owners_provided and company.executives_provided to true.

Depending on the situation, you might need to collect a scan of an ID document to enable payouts. That can happen if Stripe is unable to verify a beneficial owner or if there are possible concerns about sanctions. Collect ID information using the verification.document.front and verification.document.back arguments.

Optionally, you can collect ownership information on each person who owns 25% or more of the company using relationship.owner and relationship.percent_ownership.

Additional information on the account![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If Stripe can’t verify the company, or if there are possible concerns about sanctions, you must collect a proof-of-entity document to enable payouts. Collect it using the company.verification.document.front and company.verification.document.back arguments.

Additional information on the representative![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If Stripe can’t verify the representative, they need to provide proof of liveness, which entails taking a selfie and uploading an ID document using Stripe Identity. Your platform needs to integrate with Connect Onboarding to satisfy this requirement.

Alternatively, you can provide a scan of an ID document and a scan of an address document. To collect an ID document, use the verification.document.front and verification.document.back fields. To collect an address document, use the verification.additional_document.front and verification.additional_document.back fields. You can’t provide the same document for both identity and address verification.

Additional information on the individual![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Individuals that Stripe can’t verify must provide proof of liveness, which entails taking a selfie and uploading an ID document using Stripe Identity. Your platform needs to integrate with Connect Onboarding to allow such individuals to complete this requirement.

Alternatively, your platform can collect scans of an individual’s ID and address documents and upload them to Stripe. After uploading, submit the individual’s ID document with the individual.verification.document.front and individual.verification.document.back fields and the address document with the individual.verification.additional_document.front and individual.verification.additional_document.back fields. You can’t provide the same document for both identity and address verification.

Additional information on owners![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You must collect information on all owners. Owners are any individual who owns 25% or more of the company (owners). When you finish collecting the required information from all owners, set company.owners_provided to true. This lets Stripe know that you have completed this requirement.

Optionally, you can collect ownership information on each person who owns 25% or more of the company with relationship.owner and relationship.percent_ownership.

Additionally, for partnerships you need to provide a relationship.percent_ownership value for any owners added to the account.

Additional information on directors![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

We check the director information you supply against the registry and results in one of these outcomes:

- The business is found in the registry, and the information matches. The account fully onboards, and requires no additional action.
- The business is found in the registry, but the director information doesn’t match. You must upload a[proof of registration document](/connect/handling-api-verification?country=CA&document-type=relationship#acceptable-verification-documents)using the[documents.proof_of_registration.files](/api/accounts/create#create_account-documents-proof_of_registration-files)field.Pass the file in the`file`parameter and set the`purpose`parameter to`account_requirement`.

Command Line[curl](#)`curl https://files.stripe.com/v1/files \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -H "Stripe-Account: {{CONNECTED_STRIPE_ACCOUNT_ID}}" \
  -F "purpose"="account_requirement" \
  -F "file"="@/path/to/a/file"`This request uploads the file and returns a token:

`{
  "id": "file_5dtoJkOhAxrMWb",
  "created": 1403047735,
  "size": 4908
}`You can then use the token’s id value to attach the file to a connected account for identity verification.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_STRIPE_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "documents[proof_of_registration][files][]"=file_5dtoJkOhAxrMWb`Additional information on registration statuses![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If Stripe can’t verify the registration status of the charity, you need to collect a proof-of-entity document to enable payouts. Collect this with the documents.company_registration_verification.files field.

### Universal Beneficial Ownership Verification

After supplying the beneficial owner information, it is checked against the National Registry of Businesses (NRB). Depending on the results of this check, there are three outcomes:

- The business is found in the NRB, and the information matches. The account is fully onboarded, and no additional action is required.
- The business is found in the NRB, but the information doesn’t match. The account is fully onboarded, and no additional action is required. A discrepancy report is sent to the NRB.
- The business isn’t found in the NRB. An attestation consisting of an IP address, date, and user agent of the person submitting the information must be provided. The person is attesting that the business is registered with the NRB, and the information given to Stripe matches.

In the case where the business isn’t found in the NRB, attesting that the beneficial ownership information is complete and correct is accomplished by providing the company.ownership_declaration.date and company.ownership_declaration.ip arguments.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_STRIPE_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "company[ownership_declaration][date]"=1609798905 \
  -d "company[ownership_declaration][ip]"="8.8.8.8" \
  --data-urlencode "company[ownership_declaration][user_agent]"="Mozilla/5.0"`### Universal Beneficial Ownership Verification

After supplying the beneficial owner information, it is checked against the National Registry of Businesses (NRB). Depending on the results of this check, there are three outcomes:

- The business is found in the NRB, and the information matches. The account is fully onboarded, and no additional action is required.
- The business is found in the NRB, but the information doesn’t match. The account is fully onboarded, and no additional action is required. A discrepancy report is sent to the NRB.
- The business isn’t found in the NRB. An attestation consisting of an IP address, date, and user agent of the person submitting the information must be provided. The person is attesting that the business is registered with the NRB, and the information given to Stripe matches.

In the case where the business isn’t found in the NRB, attesting that the beneficial ownership information is complete and correct is accomplished by providing the company.ownership_declaration.date and company.ownership_declaration.ip arguments.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_STRIPE_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "company[ownership_declaration][date]"=1609798905 \
  -d "company[ownership_declaration][ip]"="8.8.8.8" \
  --data-urlencode "company[ownership_declaration][user_agent]"="Mozilla/5.0"`Additional information on the account![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If Stripe is unable to verify the company, or if there are possible concerns about sanctions, you must collect a proof-of-entity document to enable payouts. Collect it using the company.verification.document.front and company.verification.document.back arguments.

Additional information on the individual![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Depending on the situation, you might need to collect a scan of an ID document, an address document, or both to enable payouts. That can happen if Stripe can’t verify the individual or if there are possible concerns about sanctions. In some cases, depending on various calculated risk factors, Stripe can use Simplified Due Diligence and request only one document for verification at a later time.

Collect ID information using the individual.verification.document.front and individual.verification.document.back arguments, and address information using the verification.additional_document.front and verification.additional_document.back arguments.

Additional information on the representative![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

A person known as a representative must activate this connected account. The representative must be a beneficial owner who is authorized to sign for the company. Indicate this relationship to Stripe by setting relationship.executive to true, or, if the representative owns 25% or more of the company, by setting relationship.owner to true.

You might need to collect a scan of an ID document and an address document to enable payouts. That can happen if Stripe can’t verify the representative’s provided information or if there are possible concerns about sanctions. In some cases, depending on various calculated risk factors, Stripe can use Simplified Due Diligence and request only one document for verification at a later time.

Additionally, for partnerships you must provide a relationship.percent_ownership value.

You can collect ID information with the verification.document.front and verification.document.back arguments.

Additional information on directors![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

For companies, excluding partnerships, you must collect information on all directors. Directors are members of the governing board of the company. When you have finished collecting the required information from all directors, or if your company does not have any directors, you must inform Stripe by setting company.directors_provided to true.

You might need to collect a scan of an ID document and an address document to enable payouts. That can happen if Stripe can’t verify the director’s provided information or if there are possible concerns about sanctions. In some cases, depending on various calculated risk factors, Stripe can use Simplified Due Diligence and request only one document for verification at a later time.

You can collect ID information using the verification.document.front and verification.document.back arguments, and address information using the verification.additional_document.front and verification.additional_document.back arguments.

Additional information on beneficial owners (for both executives and owners)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You must collect information on all beneficial owners. Beneficial owners are persons who exercise significant management control over the company (executives) or who own 25% or more of the company (owners). When you have finished collecting the required information from all beneficial owners, you must inform Stripe by setting both company.owners_provided and company.executives_provided to true.

You might need to collect a scan of an ID document and an address document to enable payouts. That can happen if Stripe can’t verify the beneficial owner’s provided information or if there are possible concerns about sanctions. In some cases, depending on various calculated risk factors, Stripe can use Simplified Due Diligence and request only one document for verification at a later time.

You can collect ID information using the verification.document.front and verification.document.back arguments, and address information using the verification.additional_document.front and verification.additional_document.back arguments.

Optionally, you can collect ownership information on each person who owns 25% or more of the company with relationship.owner and relationship.percent_ownership.

Additionally, for partnerships you need to provide a relationship.percent_ownership value for any owners added to the account.

### Universal Beneficial Ownership Verification

After supplying the beneficial owner information, it is checked against the National Registry of Businesses (NRB). Depending on the results of this check, there are three outcomes:

- The business is found in the NRB, and the information matches. The account is fully onboarded, and no additional action is required.
- The business is found in the NRB, but the information doesn’t match. The account is fully onboarded, and no additional action is required. A discrepancy report is sent to the NRB.
- The business isn’t found in the NRB. An attestation consisting of an IP address, date, and user agent of the person submitting the information must be provided. The person is attesting that the business is registered with the NRB, and the information given to Stripe matches.

In the case where the business isn’t found in the NRB, attesting that the beneficial ownership information is complete and correct is accomplished by providing the company.ownership_declaration.date and company.ownership_declaration.ip arguments.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_STRIPE_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "company[ownership_declaration][date]"=1609798905 \
  -d "company[ownership_declaration][ip]"="8.8.8.8" \
  --data-urlencode "company[ownership_declaration][user_agent]"="Mozilla/5.0"`Additional information on the representative![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If Stripe is unable to verify the representative, you need to provide a scan of an ID document. This can be collected with the verification.document.front and verification.document.back arguments.

Additional information on the owner![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If Stripe is unable to verify the owner, you need to provide a scan of an ID document. This can be collected with the verification.document.front and verification.document.back arguments.

Additional information on the individual![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If Stripe is unable to verify the individual, you need to provide a scan of an ID document. This can be collected with the individual.verification.document.front and individual.verification.document.back arguments.

### Universal Beneficial Ownership Verification

After supplying the beneficial owner information, it is checked against the National Registry of Businesses (NRB). Depending on the results of this check, there are three outcomes:

- The business is found in the NRB, and the information matches. The account is fully onboarded, and no additional action is required.
- The business is found in the NRB, but the information doesn’t match. The account is fully onboarded, no additional action is required. A discrepancy report is sent to the NRB.
- The business is not found in the NRB. A proof of registration document (screenshot of the registration or copy of the confirmation email) is required to be uploaded.

### Uploading proof of registration Custom accounts

In the case the business is not found in the NRB, a screenshot of the beneficial owner information from the NRB must be uploaded using the documents.proof_of_registration.files argument.

Pass the file in the file parameter and set the purpose parameter to account_requirement:

Command Line[curl](#)`curl https://files.stripe.com/v1/files \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -H "Stripe-Account: {{CONNECTED_STRIPE_ACCOUNT_ID}}" \
  -F "purpose"="account_requirement" \
  -F "file"="@/path/to/a/file"`This request uploads the file and returns a token:

`{
  "id": "file_5dtoJkOhAxrMWb",
  "created": 1403047735,
  "size": 4908
}`You may then use the token’s id value to attach the file to a connected account for identity verification.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_STRIPE_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "documents[proof_of_registration][files][]"=file_5dtoJkOhAxrMWb`Additional information on bank accounts![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

We’ll verify that the legal owner of each payout bank account matches that of the Stripe account.

If Stripe can’t verify the owner of the bank account, we’ll transition the status of the ExternalAccount to verification_failed. You’ll need to collect a scan of a cancelled check or bank statement to prove the legal owner of the bank account. Collect this information with the documents.bank_account_ownership_verification.files argument.

Provide ID document for the representative![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You must provide a scan of an ID document for the representative. To collect this scan, use the verification.document.front and verification.document.back arguments.

Identity verification documents must be issued in Japan and show the representative’s residency status.

Provide ID document for the individual![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You must collect a scan of an ID document for an individual. To collect this scan, use the individual.verification.document.front and individual.verification.document.back arguments.

Identity verification documents must be issued in Japan and show the individual’s residency status.

Special considerations![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Collecting information for Japanese accounts is unique in that both kana and kanji language variations are required for a number of parameters:

- `first_name_kana`
- `first_name_kanji`
- `last_name_kana`
- `last_name_kanji`
- `name_kana`
- `name_kanji`
- `address_kana`
- `address_kanji`

You need to submit information for these parameters instead of their counterparts (that is, instead of first_name, last_name, and so forth). It might seem counterintuitive to provide two arguments that represent the same onboarding requirement, but Stripe can’t verify a Japanese account until we’ve received information for both language variations. These variations may be composed of full- or half-width hiragana, katakana, or Latin characters, with kanji-specific API parameters also allowing for kanji characters.

Japanese addresses![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Both kana and kanji language variations apply to Japanese address requirements as well.

postal_code is always required when providing a Japanese address of either language variation. Stripe validates submitted addresses, and for a valid postal_code, we attempt to automatically fill attributes for matching state, city, and town for bothj address_kana and address_kanji.

Requests with address details that are incompatible with the provided postal_code fail.

line2 should contain the building name in addition to the room number if applicable. This attribute can be omitted when the address does not contain building details.

Here’s an example representation of a Japanese address, with explanations for how each part maps to its corresponding Stripe API attribute:

`// 〒150-0001 東京都渋谷区神宮前1-5-8 神宮前タワービルディング22F
{
  "country": "JP",
  "legal_entity": {
    "address_kana": {
      "country": "JP", // 2-letter country code
      "postal_code": "1500001", // Zip/Postal Code
      "state": "ﾄｳｷﾖｳﾄ", // Prefecture
      "city": "ｼﾌﾞﾔ", // City/Ward
      "town": "ｼﾞﾝｸﾞｳﾏｴ 1-", // Town/cho-me
      "line1": "5-8", // Block/Building number
      "line2": "ｼﾞﾝｸﾞｳﾏｴﾀﾜｰﾋﾞﾙﾃﾞｨﾝｸﾞ22F", // Building details (optional)
    },
    "address_kanji": {
      "country": "JP", // 2-letter country code
      "postal_code": "１５００００１", // Zip/Postal Code
      "state": "東京都", // Prefecture
      "city": "渋谷区", // City/Ward
      "town": "神宮前　１丁目", // Town/cho-me (no kanji numerals)
      "line1": "５－８", // Block/Building number
      "line2": "神宮前タワービルディング22F", // Building details (optional)
    }
  }
}`Statement descriptors![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Statement descriptors explain charges or payments and include information that banks and card networks require to help customers understand their statements.

We recommend setting the static components of statement descriptors in all three supported scripts (kanji, kana, and Latin characters) for Japanese connected accounts.

PARAMETERStatement descriptorsettings.payments.statement_descriptorStatement descriptor (kanji)settings.payments.statement_descriptor_kanjiStatement descriptor (kana)settings.payments.statement_descriptor_kanaStatement descriptor prefixsettings.card_payments.statement_descriptor_prefixStatement descriptor prefix (kanji)settings.card_payments.statement_descriptor_prefix_kanjiStatement descriptor prefix (kana)settings.card_payments.statement_descriptor_prefix_kanaYou can set these fields with API.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d type=custom \
  -d country=JP \
  -d business_type=company \
  -d "capabilities[card_payments][requested]"=true \
  -d "capabilities[transfers][requested]"=true \
  -d "settings[payments][statement_descriptor]"="example descriptor" \
  -d "settings[payments][statement_descriptor_kanji]"="漢字明細" \
  -d "settings[payments][statement_descriptor_kana]"="カナメイサイ"`See Japanese statement descriptors for more details.

### Universal Beneficial Ownership Verification

After supplying the beneficial owner information, it is checked against the National Registry of Businesses (NRB). Depending on the results of this check, there are three outcomes:

- The business is found in the NRB, and the information matches. The account is fully onboarded, and no additional action is required.
- The business is found in the NRB, but the information doesn’t match. The account is fully onboarded, and no additional action is required. A discrepancy report is sent to the NRB.
- The business isn’t found in the NRB. An attestation consisting of an IP address, date, and user agent of the person submitting the information must be provided. The person is attesting that the business is registered with the NRB, and the information given to Stripe matches.

In the case where the business isn’t found in the NRB, attesting that the beneficial ownership information is complete and correct is accomplished by providing the company.ownership_declaration.date and company.ownership_declaration.ip arguments.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_STRIPE_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "company[ownership_declaration][date]"=1609798905 \
  -d "company[ownership_declaration][ip]"="8.8.8.8" \
  --data-urlencode "company[ownership_declaration][user_agent]"="Mozilla/5.0"`Additional information on the account![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If Stripe is unable to verify the business entity, the entity doesn’t have a company.tax_id, or there are possible concerns about sanctions, you need to collect a proof of entity document to enable payouts. Collect it using the company.verification.document.front and company.verification.document.back arguments.

Companies with the card_payments capability![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

company refers to these types of entities:

- Sociedad Anónima (S.A.)
- Sociedad de Responsabilidad Limitada (S. de R.L.)
- Sociedad Anónima Promotora de Inversión (S.A.P.I.)
- Sociedad por Acciones Simplificada (S.A.S.)

Additional information on the individual![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If the individual fails verification, doesn’t have an individual.id_number, or there are possible concerns about sanctions, then an ID document scan is required to enable payouts. You can collect that information using the individual.verification.document.front and individual.verification.document.back arguments.

Additional information on the representative![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

A person known as a representative must activate this connected account. The representative must be an authorized signatory with legal powers to represent the company as set forth under the relevant corporate documents, and must be authorized to agree to Stripe’s terms.

If Stripe is unable to verify the representative, the representative doesn’t have a representative.id_number, or there are possible concerns about sanctions, you must collect a scan of an ID document to enable payouts. Collect ID information using the verification.document.front and verification.document.back arguments.

Additional information on owners![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You must collect information on all owners with more than 25% ownership of the company. When you have finished collecting the required owner information, you must inform Stripe by setting company.owners_provided to true.

If Stripe is unable to verify an owner, an owner doesn’t have an owners.id_number, or there are possible concerns about sanctions, you must collect a scan of an ID document to enable payouts. Collect ID information using the verification.document.front and verification.document.back arguments.

Optionally, you can collect ownership information on each person using the relationship.owner and relationship.percent_ownership arguments.

Additional information on the account![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If Stripe is unable to verify the company, or if there are possible concerns about sanctions, you must collect a proof-of-entity document to enable payouts. Collect it using the company.verification.document.front and company.verification.document.back arguments.

Additional information on the individual![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Depending on the situation, you might need to collect a scan of an ID document, an address document, or both to enable payouts. That can happen if Stripe is unable to verify the individual or if there are possible concerns about sanctions. Collect ID information using the individual.verification.document.front and individual.verification.document.back arguments.

Additional information on the representative![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

A person known as a representative must activate this connected account. The representative must be a beneficial owner who is authorized to sign for the company. Indicate that relationship to Stripe by setting relationship.executive to true, or, if the representative owns 25% or more of the company, by setting relationship.owner to true.

Depending on the situation, you might need to collect a scan of an ID document to enable payouts. That can happen if Stripe is unable to verify the representative or if there are possible concerns about sanctions. Collect ID information using the verification.document.front and verification.document.back arguments.

Optionally, you can collect the representative’s ownership information using the relationship.representative and relationship.percent_ownership arguments.

Additional information on directors![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

For companies (excluding partnerships), you must collect information on all directors. Directors are members of the governing board of the company. When you have finished collecting the required information from all directors, or if your company does not have any directors, you must notify Stripe by setting company.directors_provided to true.

If there are possible concerns about sanctions, you must collect a scan of an ID document to enable payouts. Collect ID information using the verification.document.front and verification.document.back arguments.

Additional information on beneficial owners (for both executives and owners)![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You must collect information on all beneficial owners. Beneficial owners are persons who exercise significant management control over the company (executives) or who own 25% or more of the company (owners). When you have finished collecting the required information from all beneficial owners, you must notify Stripe by setting both company.owners_provided and company.executives_provided to true.

Depending on the situation, you might need to collect a scan of an ID document to enable payouts. That can happen if Stripe is unable to verify a beneficial owner or if there are possible concerns about sanctions. Collect ID information using the verification.document.front and verification.document.back arguments.

Optionally, you can collect ownership information on each person who owns 25% or more of the company using the relationship.owner and relationship.percent_ownership arguments.

Additional information on the individual![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

WarningIf you don’t integrate with Connect Onboarding, you won’t be able to onboard connected accounts subject to enhanced identity verification.

To comply with Singapore’s Payment Services Act 2019, we require individuals to verify their identities either by using MyInfo or by taking a selfie with their identity document through Stripe Identity. Additionally, your platform needs to integrate with Connect Onboarding to satisfy the proof_of_liveness identity verification requirement. We verify addresses with MyInfo or request documents, such as utility bills or bank statements, when necessary.

Additional information on the representative![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

WarningIf you don’t integrate with Connect Onboarding, you won’t be able to onboard connected accounts subject to enhanced identity verification.

To comply with Singapore’s Payment Services Act 2019, we require individuals to verify their identities either by using MyInfo or by taking a selfie with their identity document through Stripe Identity. Additionally, your platform needs to integrate with Connect Onboarding to satisfy the proof_of_liveness identity verification requirement. We verify addresses with MyInfo or request documents, such as utility bills or bank statements, when necessary.

An account’s legal representative must be an owner of the business entity with at least 25% ownership, or a controller, defined as an individual with significant management responsibility for the entity, such as a Director, or Partner.

Additional information on the representative![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

WarningIf you don’t integrate with Connect Onboarding, you won’t be able to onboard connected accounts subject to enhanced identity verification.

To comply with Singapore’s Payment Services Act 2019, we require individuals to verify their identities either by using MyInfo or by taking a selfie with their identity document through Stripe Identity. Additionally, your platform needs to integrate with Connect Onboarding to satisfy the proof_of_liveness identity verification requirement. We verify addresses with MyInfo or request documents, such as utility bills or bank statements, when necessary.

An account’s legal representative must be an owner of the business entity with at least 25% ownership, or a controller, defined as an individual with significant management responsibility for the entity, such as a Director, or Partner.

Additional information on the beneficial owners and directors![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Accounts that belong to companies must provide information on all their beneficial owners and directors. Beneficial owners are natural persons who hold ultimate effective control over the account:

- Companies:  - All natural persons owning (directly or indirectly, through a[holding company](https://support.stripe.com/questions/beneficial-ownership-verification-for-holding-companies)) more than 25% of the shares, or owning more than 10% if no one owns more than 25%
  - All Directors of the Company


- Partnerships:  - All Partners
  - All Managers



If Stripe is unable to verify a beneficial owner, you need to provide a scan of an ID document. To collect an ID document, use the verification.document.front and verification.document.back arguments.

Additional information on the beneficial owners and directors![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Accounts that belong to non-profits must provide information on all their beneficial owners and directors. Beneficial owners are natural persons who hold ultimate effective control over the account. In the case of non-profits, these are the key officers and members of the Governing Board.

If Stripe is unable to verify a beneficial owner, you need to provide a scan of an ID document. To collect an ID document, use the verification.document.front and verification.document.back arguments.

Closure of unverified accounts![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

As required under Singapore’s Payment Services Act, we’re permanently closing Singapore accounts that remain unverified for over 120 business days. These are accounts whose charges or payouts have already been suspended, so this closure affects only inactive accounts.

To help you identify affected accounts, we upload monthly reports titled “Unverified account list” to your Dashboard under the reporting and documents section, in which you’ll find the list of impacted accounts and their requirement deadlines. Any accounts closed in the last month are in the report titled “Closed unverified account list.”

We’ll close any account that hasn’t been verified by its designated deadline. The account owner needs to provide the missing verification information before the deadline to keep the account open. If the information is provided after the deadline has passed, we’ll release any remaining balance to the account holder’s bank account, but we won’t be able to reactivate their Stripe account.

Stripe sends emails to Standard and Express accounts that remain unverified for too long, to inform them of the impending closure and to remind them to update their account details. Stripe won’t communicate with Custom connected accounts directly. That means you, as the platform, can contact them to avoid account closures.

Accounts that are closed under this process have their disabled_reason set to rejected.other.

Unique Entity Number (UEN) verification![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

UEN information might be verified with the data made available at https://data.gov.sg under the terms of the Singapore Open Data License version 1.0.

Additional identity verification![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

To comply with regulatory requirements in Thailand, we require additional identity verification for certain connected accounts. This entails taking a selfie and uploading an ID document using Stripe Identity. Your platform needs to integrate with Connect Onboarding to satisfy this identity verification requirement.

Additional identity verification applies to the representatives and beneficial owners of connected accounts belonging to individuals, sole proprietors and unregistered partnerships.

WarningIf you don’t integrate with Connect Onboarding, you won’t be able to onboard connected accounts subject to additional identity verification.

Registered address requirement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

The registered address requirement refers to the Household Registration address. Please provide an address as per the ‘Tabien Bann’ or Household Registration book, also known as the Blue book for Thai nationals, or Yellow book for non-Thai nationals. To collect a Household Registration address, use the registered_address parameter.

If the user is neither a Thai national nor resident of Thailand, collect their current residential address with the same parameter instead.

ID number requirement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

The ID number requirement refers to the 13-digit code found on the front of a Thai ID card, and secondary ID number requirement refers to the laser code found at the back of a Thai ID card. To collect a Thai ID number use the id_number parameter, and to collect a laser code use the id_number_secondary parameter.

These requirements are only applicable to Thai nationals, so leave the parameters empty if the user isn’t a Thai national.

Additional information on the individual![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If Stripe is unable to verify the individual or if they’re not a Thai national, you need to collect a scan of an ID document. To collect an ID document, use the individual.verification.document.front and individual.verification.document.back parameters.

Additional information on the representative![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If Stripe is unable to verify the account representative or if they’re not a Thai national, you need to provide a scan of an ID document. To collect an ID document, use the verification.document.front and verification.document.back parameters.

Additional information on beneficial owners![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Accounts belonging to companies and registered partnerships are required to provide information on all beneficial owners. A beneficial owner is defined as any individual who owns 25% or more shares of the business. If there is no such person, then any individual who exercises significant control over the company is considered a beneficial owner. Otherwise, please provide information on any individual holding the position of senior management.

If Stripe is unable to verify a beneficial owner or if they’re not a Thai national, you need to provide a scan of an ID document. To collect an ID document, use the verification.document.front and verification.document.back parameters.

Additional information on the company![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If Stripe is unable to verify the company, you need to provide a scan of a company verification document issued less than 6 months ago. To collect the company verification document scan, use the company.verification.document.front and company.verification.document.back parameters on the Account object.

Additional tax information![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If Stripe is unable to verify the company.tax_id, upload a copy of an IRS Letter 147C document or an IRS SS-4 confirmation letter as an alternate attempt at verification. This information can be collected with the company.verification.document.front argument, and should include the connected account’s company.name and company.tax_id.

Additional information on the account![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

To enable card payments, a validated city, state, and ZIP code for company.address is required. Card payments will be disabled if the company.tax_id (EIN) hasn’t been verified before 30 days or 1,500 USD in payments, whichever comes first.

To enable payouts, company.address needs to be a validated full address and the company.tax_id (EIN) needs to be verified. Payouts will be disabled if a full address hasn’t been validated or the company.tax_id is not verified before 30 days.

Additional information on the individual![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

To enable card payments, a validated city, state, and ZIP code for individual.address is required.

To enable payouts, individual.address needs to be a validated full address. Payouts will be disabled if a full address hasn’t been validated before 30 days.

If the individual fails verification with ssn_last_4, then the full SSN is required and their identity needs to be verified to enable card payments. Use the individual.id_number argument to collect this information.

Additional information on the representative![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

This connected account needs to be activated by a person, known as a representative, with significant responsibility to control, manage, or direct the organization; and is authorized by the organization to agree to Stripe’s terms. The representative must either be an owner or an executive, which you specify by setting relationship.owner to true or relationship.executive to true.

If the representative fails verification with ssn_last_4, then the full SSN is required and their identity needs to be verified to enable card payments. Use the person.id_number argument to collect this information.

If Stripe is unable to verify the representative or if the person doesn’t have an SSN, you need to collect a scan of an ID document to enable card payments. This information can be collected with the verification.document.front and verification.document.back arguments.

Additional information for minors![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If the account representative is a minor, you must verify the minor’s legal guardian. A legal guardian is a Person on the account with relationship.legal_guardian set to true. Additionally, the legal guardian must provide their information and sign the Stripe terms of service, which we store on the Person object with relationship.legal_guardian set to true. Store the legal guardian’s terms of service acceptance in the additional_tos_acceptances hash.

If the legal guardian fails verification with ssn_last_4, then the full SSN is required and their identity needs to be verified to enable card payments. Use the person.id_number argument to collect this information.

If Stripe is unable to verify the legal guardian or if the person doesn’t have an SSN, you need to collect a scan of an ID document to enable card payments. This information can be collected with the verification.document.front and verification.document.back arguments.

Additional information on owners![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Information on all owners with 25% or more ownership of the company must be collected. When you have finished collecting the required owner information, you need to attest this by setting company.owners_provided to true. This lets Stripe know that you have completed this requirement.

If there are any unverified owners in the company, payouts on the connected account can become disabled at 750,000 USD in charges and charges can become disabled at 1 million USD, unless the following information is collected:

- `owners.dob.day`
- `owners.dob.month`
- `owners.dob.year`
- `owners.address`
- `owners.ssn_last_4`
- `owners.phone`

If the owner fails verification with ssn_last_4, then the full SSN is required and their identity needs to be verified to enable card payments. Use the person.id_number argument to collect this information.

If Stripe is unable to verify an owner or if an owner doesn’t have an SSN, you need to collect a scan of an ID document. This information can be collected with the verification.document.front and verification.document.back arguments.

Optionally, you can collect company ownership information. This can be done using the relationship.owner and relationship.percent_ownership attributes. Set relationship.owner to true and relationship.percent_ownership to the user’s ownership percentage. If relationship.percent_ownership is unspecified, the default is 25%.

Supported business structures![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Optionally, you can collect information on the legal structure of your user’s business with the company.structure argument. See Business structure for more details.

Below lists the supported business structures for privately held companies:

- `multi_member_llc`
- `single_member_llc`
- `private_partnership`
- `private_corporation`
- `unincorporated_association`

Below lists the supported business structures for publicly traded companies. If you further classify the business with any of these structures, the representative doesn’t need to be an owner nor an executive, and you do not need to provide information on additional owners.

- `public_corporation`
- `public_partnership`

Supported business structures![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Optionally, you can collect information on the legal structure of your user’s business. This can be done using the company.structure argument. See Business structure for more details.

Below lists the supported business structures for government entities:

- `governmental_unit`
- `government_instrumentality`

If your user is an instrumentality with tax-exempt status, you can set the company.structure to tax_exempt_government_instrumentality.

Supported business structures![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

While uncommon, there are circumstances where an individual business operates and is treated more like a company, such as a single-member LLC. For these users, you can optionally collect information on their legal structure with the company.structure argument.

If your user’s business has only one member or owner and is registered as an LLC with a US state, you can set the business_type to company and the company.structure to single_member_llc. You collect the same required information, except you use the company hash and the Persons API, instead of the individual hash. For any requirement in the individual hash, you need to map it to the account’s representative, such as setting representative.first_name instead of individual.first_name.

If your user has obtained a business identification (for example, has a tax ID that’s separate from their personal ID, or a business address that’s different than their home address), you can set the business_type to company and the company.structure to sole_proprietorship. You collect the same required information, except you use the company hash and the Persons API, instead of the individual hash since it pertains to the natural person. For any requirement in the individual hash, you need to map it to the account’s representative, such as setting representative.first_name instead of individual.first_name.

Supported business structures![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Optionally, you can collect information on the legal structure of your user’s business with the company.structure argument. See Business structure for more details.

Below lists the supported business structures for non-profit organizations:

- `incorporated_non_profit`
- `unincorporated_non_profit`

The US federal government grants tax-exempt status to certain government entities that are considered non-profit. If your user is an instrumentality with tax-exempt status, you can set the business_type to government_entity and the company.structure to tax_exempt_government_instrumentality. Then, collect the appropriate verification requirements from them.

Tax reporting information![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

By default, the requirements for transfers do not collect all information at the appropriate thresholds to file IRS Form 1099-K or Form 1099-MISC. If your business has US federal 1099 filing requirements and plans to file these through Stripe, request the appropriate tax reporting capability and make sure to collect the necessary information from your users.

Threshold information![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

In addition to the onboarding requirements, there is a second threshold to keep payouts enabled, which depends on your industry and Stripe’s review of your platform profile. The company.tax_id (EIN) needs to be verified before 10,000 USD in charges for some platforms, and before 3,000 USD for other platforms.

Threshold information![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

In addition to the onboarding requirements, there is a second threshold to keep payouts enabled, which depends on your industry and Stripe’s review of your platform profile. The company.tax_id (EIN) needs to be verified before 10,000 USD in charges for some platforms, and before 3,000 USD for other platforms.

- `individual.dob.day`
- `individual.dob.month`
- `individual.dob.year`
- `individual.ssn_last_4`

Payments threshold information![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

When an account with card_payments reaches 500,000 USD in lifetime charges, we require a full id_number (SSN) for them to continue accepting payments. If they’ve already provided the full number, they don’t have to provide it again.

For accounts with business_type set to individual, and where the owner isn’t a minor, update the account’s individual.id_number. For other accounts, which have persons with relationship.legal_guardian, relationship.representative, or relationship.owner, update the appropriate person’s id_number.

### Create the connected account

For each account to be migrated to Stripe, create an associated Account.

StandardExpressCustomController propertiesUse the Create Account API to create a connected account with controller set to the desired account preferences. You can prefill any information, but at a minimum, you must specify the controller. The country of the account defaults to the same country as your platform, and the account confirms the selection during onboarding.

NoteThis example includes only some of the fields you can set when creating an account. For a full list of the fields you can set, such as address and website_url, see the Create Account API reference.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "controller[fees][payer]"=account \
  -d "controller[losses][payments]"=stripe \
  -d "controller[stripe_dashboard][type]"=none \
  -d "controller[requirement_collection]"=stripe \
  -d country=US \
  -d "capabilities[card_payments][requested]"=true \
  -d "capabilities[transfers][requested]"=true`If you’ve already collected information for your connected accounts, you can prefill that information on the account object. You can prefill any account information, including personal and business information, external account information, and so on.

Connect Onboarding doesn’t ask for the prefilled information. However, it does ask the account holder to confirm the prefilled information before accepting the Connect service agreement.

When testing your integration, prefill account information using test data.

Successful creation returns the account object. Inspect the object for the connected account id and store the value in your database.

`{
  ...
  "id": "{{CONNECTED_ACCOUNT_ID}}",
  ...
}`After updating Stripe with all existing data, look for any outstanding requirements. Any outstanding requirements are listed in the currently_due array. All currently_due requirements need to be collected from the account for Stripe to verify the account and activate the account’s capabilities.

`{
  ...
  "requirements": {
    "alternatives": [],
    "current_deadline": null,
    "currently_due": [
      "business_profile.url",
      "external_account",
      "individual.first_name",
      "individual.last_name",
      "tos_acceptance.date",
      "tos_acceptance.ip"
    ],
    "disabled_reason": "requirements.past_due",
    "errors": [],`See all 36 linesAfter providing all existing data on an account, direct the account to a Stripe UI to set up Stripe credentials, confirm the information, and accept the Stripe terms of service.

### Take new accounts through an onboarding flow

In addition to migrating existing accounts, build a flow for new accounts to onboard to Stripe. You can also use this onboarding flow to collect missing data for accounts being migrated.

Review onboarding options to create your onboarding flow.

## Handle outstanding and ongoing requirements

When the connected account’s data is submitted, Stripe verifies it. This process might take minutes or hours depending on the nature of the verification required. During this process, the capabilities you requested have a pending status.

### Review status

You can retrieve the status of your connected account’s capabilities by:

- Inspecting the Account object’s[capabilities](/api/accounts/object#account_object-capabilities)hash for the relevant capability.
- Requesting capabilities directly from the[Capabilities API](/api/capabilities/retrieve)and inspecting the status of the relevant capability.
- Listening for`account.updated`[events](/api/events/types#event_types-account.updated)in your[webhook](/connect/webhooks)endpoint and inspecting the`capabilities`hash for the relevant capability.

After verifications are complete, the capability becomes active and available to the connected account. Account verifications run continuously, and if a future verification fails, a capability can transition out of active. Listen for account.updated events to detect changes to capability states.

Confirm that your Connect integration is compliant and operational by checking that the account’s charges_enabled and payouts_enabled are both true. You can use the API or listen for account.updated events. For details on other relevant fields, check the account’s requirements hash. You can’t confirm the integration based on a single value because statuses can vary depending on the application and related policies.

- [charges_enabled](/api/accounts/object#account_object-charges_enabled)confirms that your full charge path including the charge and transfer works correctly and evaluates if either`card_payments`or`transfers`capabilities are active.
- [payouts_enabled](/api/accounts/object#account_object-payouts_enabled)evaluates whether your connected account can pay out to an external account. Depending on your risk policies, you can allow your connected account to start transacting without payouts enabled. You[must eventually enable payouts](/connect/manage-payout-schedule)to pay your connected accounts.

You can use the following logic as a starting point for defining a summary status to display to your connected account.

[Ruby](#)`# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

def account_state(account)
  reqs = account.requirements

  if reqs.disabled_reason && reqs.disabled_reason.include?("rejected")
    "rejected"
  elsif account.payouts_enabled && account.charges_enabled
    if reqs.pending_verification
      "pending enablement"
    elsif !reqs.disabled_reason && !reqs.currently_due
      if !reqs.eventually_due
        "complete"
      else
        "enabled"
      end
    else
      "restricted"
    end
  elsif !account.payouts_enabled && account.charges_enabled
    "restricted (payouts disabled)"
  elsif !account.charges_enabled && account.payouts_enabled
    "restricted (charges disabled)"
  elsif reqs.past_due
    "restricted (past due)"
  elsif reqs.pending_verification
    "pending (disabled)"
  else
    "restricted"
  end
end

accounts = Stripe::Account.list(limit: 10)

accounts.each do |account|
    puts "#{account.id} has state: #{account_state(account)}"
end`### Handle verification errors

Handle verification failures differently depending on your onboarding flow.

NoteYou can’t use the API to respond to Stripe risk reviews. You can enable your connected accounts to respond using embedded components, Stripe-hosted onboarding, or remediation links. You can also use the Dashboard to respond to risk reviews on behalf of your connected accounts.

APIEmbeddedHostedListen to the account.updated event. If the account contains any currently_due fields when the current_deadline arrives, the corresponding functionality is disabled and those fields are added to past_due.

Create a form with clear instructions that the account can use to correct the information. Notify the account, then submit the corrected information using the Accounts API.

If you plan to create custom flows to handle all your verification errors:

- Review the details regarding all possible[verification errors and how to handle them](/connect/handling-api-verification).
- [Test verification states](/connect/testing-verification).

## Migrate payment and customer data to Stripe

After your connected accounts are created on Stripe, request a PAN data import, which migrates your payment and customer data for use on Stripe.

## See also

- [Choose your onboarding configuration](/connect/onboarding)
- [Handling identity verification with the API](/connect/handling-api-verification)
- [Testing account identity verification](/connect/testing-verification)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a migration plan](#create-a-migration-plan)[Update your integration](#update-your-integration)[Create and onboard accounts](#create-and-onboard-accounts)[Handle outstanding and ongoing requirements](#handle-outstanding-and-ongoing-requirements)[Migrate payment and customer data to Stripe](#migrate-payment-and-customer-data-to-stripe)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`