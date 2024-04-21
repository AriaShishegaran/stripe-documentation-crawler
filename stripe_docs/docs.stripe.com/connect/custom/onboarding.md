# Onboarding solutions for Custom accounts

Stripe offers several ways to onboard Custom connected accounts. You can choose the best onboarding method for your business.

We recommend using embedded onboarding components or Stripe-hosted onboarding. Both automatically update to handle changing requirements when they apply to a connected account. With embedded components, you can match them to your branding and control which policies and terms are shown.

[match them to your branding](/connect/customize-connect-embedded-components)

[control which policies and terms are shown](/connect/embedded-onboarding#customize-policies-shown-to-your-users)

[API-based onboarding](/connect/custom/onboarding#api-based-onboarding)

- Expensive and time-consuming to build

- Continuing high maintenance, especially to keep in compliance with changing global requirements

- Can’t resolve Stripe risk reviews

[Embedded onboarding](/connect/custom/onboarding#embedded-onboarding)

- Highly themeable

[Highly themeable](/connect/customize-connect-embedded-components)

- Limited or no Stripe branding

- Connected accounts remain in the flow of your site

- Low effort integration

[Stripe-hosted onboarding](/connect/custom/onboarding#stripe-hosted-onboarding)

- Stripe-branded with limited platform branding

- Limited control over the flow logic

- Connected accounts redirect to Stripe instead of completing the process without leaving your site

## API-based onboarding

API-based onboarding involves building out each aspect of your site’s onboarding user interface to call the corresponding Stripe APIs. Your integration must satisfy all of Stripe’s onboarding requirements.

The following factors affect the onboarding requirements for your connected accounts:

[onboarding requirements](/connect/required-verification-information)

- The origin country of the connected accounts

- The service agreement type applicable to the connected accounts

[service agreement type](/connect/service-agreement-types)

- The capabilities requested for the connected accounts

[capabilities](/connect/account-capabilities)

- The business type (for example, individual or company) and company.structure (for example, public corporation or private partnership)

[business type](/api/accounts/object#account_object-business_type)

[company.structure](/api/accounts/object#account_object-company-structure)

The following interactive form shows how these factors affect the requirements by letting you set different values for them.

Inspect all the requirements necessary for your selected combinations. Pay particular attention to the Requirement column. That column lists specific parameters on the account that you must collect to onboard it with the capabilities requested. Some parameters are only required at certain thresholds, as noted in the Required Before column.

In the UAE, company documents such as the Trade License and Proof of Bank Account as well as relevant identity documents must be verified before a connected account can start processing live charges and receiving payouts. For all businesses except sole establishments and free zone establishments, the Memorandum of Association must be verified as well.

[Trade License](/api/accounts/create#create_account-documents-company_license)

[Proof of Bank Account](/api/accounts/create#create_account-documents-bank_account_ownership_verification)

[payouts](/payouts)

[Memorandum of Association](/api/accounts/create#create_account-documents-company_memorandum_of_association)

For the company representative, beneficial owner(s) and executive(s), we require the following identity documents for verification:

- Passport: all individuals

- Emirates ID: UAE nationals & UAE residents

- Residence visa: foreign nationals who are resident in the UAE

The Emirates ID can be provided in the parameter called verification.document. Passport(s) and residence visa(s) should be provided under a separate parameter called documents.

[verification.document](/api/persons/create#create_person-verification-document)

[documents](/api/persons/create#create_person-documents)

In the UAE, Stripe is required to keep up to date with a company’s Trade License in addition to the primary identity document of the company’s representative, beneficial owners and executives. The primary identity document is either the Emirates ID for UAE nationals and residents, otherwise it is an individual’s Passport. Companies will have up to 28 days after the expiry date of these documents to provide an updated version. Expired documents will appear under company requirements or individual requirements and marked as currently due for two weeks before capabilities become disabled.

[Trade License](/api/accounts/update#update_account-documents-company_license)

[Passport](/api/persons/update#update_person-documents-passport)

[company requirements](/api/accounts/object#account_object-requirements-currently_due)

[individual requirements](/api/persons/object#person_object-requirements-currently_due)

Stripe is required to verify all the beneficial owners of a business. These are the individuals who own 25% or more of the primary business. If a holding company has 25% or more ownership of the business, then the Memorandum of Association of this holding company as well that of the primary business must be uploaded. These documents must show the person(s) where relationship.owner is set to true.

[beneficial owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)

[holding company](https://support.stripe.com/questions/beneficial-ownership-by-a-trust-holding-company-or-other-legal-entity)

[relationship.owner](/api/persons/object#person_object-relationship-owner)

This connected account needs to be activated by a person, known as the company representative, with significant responsibility to control, manage, or direct the organization and is authorized by the organization to agree to Stripe’s terms. The representative must either be an owner or an executive, which you specify by setting relationship.owner to true or relationship.executive to true. For a sole establishment or free zone establishment, the account must be activated by the owner of the business.

[an owner or an executive](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)

[relationship.owner](/api/persons/object#person_object-relationship-owner)

[relationship.executive](/api/persons/object#person_object-relationship-executive)

Stripe does not charge UAE VAT on Stripe fees to customers located in the UAE, where a valid UAE VAT ID has been provided. Local UAE VAT self-assessment obligations may be triggered upon receipt of a monthly invoice from Stripe. Stripe does charge UAE VAT at 5% on Stripe fees to customers located in the UAE, where a valid UAE VAT ID hasn’t been provided.

[invoice](/api/invoices)

If the company representative does not appear on the company’s Trade License or the Memorandum of Association, then you must upload a Power of Attorney that shows that the company representative has the authority to act on behalf of the company or a notarized letter of authorization.

[Power of Attorney](/api/persons/update#update_person-documents-company_authorization)

In the UAE, the only possible business type is company and the following business structures are accepted:

[business structures](/connect/identity-verification#business-structure)

- sole_establishment

- free_zone_establishment

- llc

- free_zone_llc

If Stripe is unable to verify the company, or if there are possible concerns about sanctions, you must collect a proof-of-entity document to enable payouts. Collect it using the company.verification.document.front and company.verification.document.back arguments.

[sanctions](/connect/risk-management/best-practices#sanctions-concerns)

[proof-of-entity document](/connect/handling-api-verification#acceptable-verification-documents)

[payouts](/payouts)

[company.verification.document.front](/api/accounts/object#account_object-company-verification-document-front)

[company.verification.document.back](/api/accounts/object#account_object-company-verification-document-back)

Depending on the situation, you might need to collect a scan of an ID document to enable payouts. That can happen if Stripe is unable to verify the individual or if there are possible concerns about sanctions.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[sanctions](/connect/risk-management/best-practices#sanctions-concerns)

Collect ID information using the individual.verification.document.front and individual.verification.document.back arguments.

[individual.verification.document.front](/api/accounts/update#update_account-individual-verification-document-front)

[individual.verification.document.back](/api/accounts/update#update_account-individual-verification-document-back)

A person known as a representative must activate this connected account. This person must be a beneficial owner who is authorized to sign for the company. Indicate this relationship to Stripe by setting relationship.executive to true, or, if the representative owns 25% or more of the company, by setting relationship.owner to true.

[beneficial owner](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)

[relationship.executive](/api/persons/object#person_object-relationship-executive)

[relationship.owner](/api/persons/object#person_object-relationship-owner)

Depending on the situation, you might need to collect a scan of an ID document to enable payouts. That can happen if Stripe is unable to verify the representative or if there are possible concerns about sanctions. Collect ID information using the verification.document.front and verification.document.back arguments.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[sanctions](/connect/risk-management/best-practices#sanctions-concerns)

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

Optionally, you can collect the representative’s ownership information using relationship.representative and relationship.percent_ownership.

[relationship.representative](/api/persons/object#person_object-relationship-representative)

[relationship.percent_ownership](/api/persons/object#person_object-relationship-percent_ownership)

For companies (excluding partnerships), you must collect information on all directors. Directors are members of the governing board of the company. When you have finished collecting the required information from all directors, or if your company does not have any directors, you must inform Stripe by setting company.directors_provided to true.

[directors](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)

[company.directors_provided](/api/accounts/object#account_object-company-directors_provided)

If there are possible concerns about sanctions, you must collect a scan of an ID document to enable payouts. Collect ID information using the verification.document.front and verification.document.back arguments.

[sanctions](/connect/risk-management/best-practices#sanctions-concerns)

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

You must collect information on all beneficial owners. Beneficial owners are persons who exercise significant management control over the company (executives) or who own 25% or more of the company (owners). When you have finished collecting the required information from all beneficial owners, you must inform Stripe by setting both company.owners_provided and company.executives_provided to true.

[beneficial owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)

[company.owners_provided](/api/accounts/object#account_object-company-owners_provided)

[company.executives_provided](/api/accounts/object#account_object-company-executives_provided)

Depending on the situation, you might need to collect a scan of an ID document to enable payouts. That can happen if Stripe is unable to verify a beneficial owner or if there are possible concerns about sanctions. Collect ID information using the verification.document.front and verification.document.back arguments.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[sanctions](/connect/risk-management/best-practices#sanctions-concerns)

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

Optionally, you can collect ownership information on each person who owns 25% or more of the company using relationship.owner and relationship.percent_ownership.

[relationship.owner](/api/persons/object#person_object-relationship-owner)

[relationship.percent_ownership](/api/persons/object#person_object-relationship-percent_ownership)

If Stripe can’t verify the company, or if there are possible concerns about sanctions, you must collect a proof-of-entity document to enable payouts. Collect it using the company.verification.document.front and company.verification.document.back arguments.

[sanctions](/connect/risk-management/best-practices#sanctions-concerns)

[proof-of-entity document](/connect/handling-api-verification?country=CA&document-type=entity#acceptable-verification-documents)

[payouts](/payouts)

[company.verification.document.front](/api/accounts/object#account_object-company-verification-document-front)

[company.verification.document.back](/api/accounts/object#account_object-company-verification-document-back)

If Stripe can’t verify the representative, they need to provide proof of liveness, which entails taking a selfie and uploading an ID document using Stripe Identity. Your platform needs to integrate with Connect Onboarding to satisfy this requirement.

[ID document](/connect/handling-api-verification?country=CA&document-type=identity#acceptable-verification-documents)

[Stripe Identity](/identity)

[Connect Onboarding](https://stripe.com/connect/onboarding)

Alternatively, you can provide a scan of an ID document and a scan of an address document. To collect an ID document, use the verification.document.front and verification.document.back fields. To collect an address document, use the verification.additional_document.front and verification.additional_document.back fields. You can’t provide the same document for both identity and address verification.

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

[verification.additional_document.front](/api/persons/object#person_object-verification-additional_document-front)

[verification.additional_document.back](/api/persons/object#person_object-verification-additional_document-back)

Individuals that Stripe can’t verify must provide proof of liveness, which entails taking a selfie and uploading an ID document using Stripe Identity. Your platform needs to integrate with Connect Onboarding to allow such individuals to complete this requirement.

[ID document](/connect/handling-api-verification?country=CA&document-type=identity#acceptable-verification-documents)

[Stripe Identity](/identity)

[Connect Onboarding](https://stripe.com/connect/onboarding)

Alternatively, your platform can collect scans of an individual’s ID and address documents and upload them to Stripe. After uploading, submit the individual’s ID document with the individual.verification.document.front and individual.verification.document.back fields and the address document with the individual.verification.additional_document.front and individual.verification.additional_document.back fields. You can’t provide the same document for both identity and address verification.

[upload them](/api/files/create)

[individual.verification.document.front](/api/accounts/object#account_object-individual-verification-document-front)

[individual.verification.document.back](/api/accounts/object#account_object-individual-verification-document-back)

[individual.verification.additional_document.front](/api/accounts/object#account_object-individual-verification-additional_document-front)

[individual.verification.additional_document.back](/api/accounts/object#account_object-individual-verification-additional_document-back)

You must collect information on all owners. Owners are any individual who owns 25% or more of the company (owners). When you finish collecting the required information from all owners, set company.owners_provided to true. This lets Stripe know that you have completed this requirement.

[owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)

[company.owners_provided](/api/accounts/object#account_object-company-owners_provided)

Optionally, you can collect ownership information on each person who owns 25% or more of the company with relationship.owner and relationship.percent_ownership.

[relationship.owner](/api/persons/object#person_object-relationship-owner)

[relationship.percent_ownership](/api/persons/object#person_object-relationship-percent_ownership)

Additionally, for partnerships you need to provide a relationship.percent_ownership value for any owners added to the account.

[relationship.percent_ownership](/api/persons/object#person_object-relationship-percent_ownership)

We check the director information you supply against the registry and results in one of these outcomes:

[director](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)

- The business is found in the registry, and the information matches. The account fully onboards, and requires no additional action.

- The business is found in the registry, but the director information doesn’t match. You must upload a proof of registration document using the documents.proof_of_registration.files field. Pass the file in the file parameter and set the purpose parameter to account_requirement.

[proof of registration document](/connect/handling-api-verification?country=CA&document-type=relationship#acceptable-verification-documents)

[documents.proof_of_registration.files](/api/accounts/create#create_account-documents-proof_of_registration-files)

This request uploads the file and returns a token:

You can then use the token’s id value to attach the file to a connected account for identity verification.

If Stripe can’t verify the registration status of the charity, you need to collect a proof-of-entity document to enable payouts. Collect this with the documents.company_registration_verification.files field.

[proof-of-entity document](/connect/handling-api-verification?country=CA&document-type=entity#acceptable-verification-documents)

[payouts](/payouts)

[documents.company_registration_verification.files](/api/accounts/update#update_account-documents-company_registration_verification-files)

After supplying the beneficial owner information, it is checked against the National Registry of Businesses (NRB). Depending on the results of this check, there are three outcomes:

- The business is found in the NRB, and the information matches. The account is fully onboarded, and no additional action is required.

- The business is found in the NRB, but the information doesn’t match. The account is fully onboarded, and no additional action is required. A discrepancy report is sent to the NRB.

- The business isn’t found in the NRB. An attestation consisting of an IP address, date, and user agent of the person submitting the information must be provided. The person is attesting that the business is registered with the NRB, and the information given to Stripe matches.

In the case where the business isn’t found in the NRB, attesting that the beneficial ownership information is complete and correct is accomplished by providing the company.ownership_declaration.date and company.ownership_declaration.ip arguments.

[company.ownership_declaration.date](/api/accounts/object#account_object-company-ownership_declaration-date)

[company.ownership_declaration.ip](/api/accounts/object#account_object-company-ownership_declaration-ip)

After supplying the beneficial owner information, it is checked against the National Registry of Businesses (NRB). Depending on the results of this check, there are three outcomes:

- The business is found in the NRB, and the information matches. The account is fully onboarded, and no additional action is required.

- The business is found in the NRB, but the information doesn’t match. The account is fully onboarded, and no additional action is required. A discrepancy report is sent to the NRB.

- The business isn’t found in the NRB. An attestation consisting of an IP address, date, and user agent of the person submitting the information must be provided. The person is attesting that the business is registered with the NRB, and the information given to Stripe matches.

In the case where the business isn’t found in the NRB, attesting that the beneficial ownership information is complete and correct is accomplished by providing the company.ownership_declaration.date and company.ownership_declaration.ip arguments.

[company.ownership_declaration.date](/api/accounts/object#account_object-company-ownership_declaration-date)

[company.ownership_declaration.ip](/api/accounts/object#account_object-company-ownership_declaration-ip)

If Stripe is unable to verify the company, or if there are possible concerns about sanctions, you must collect a proof-of-entity document to enable payouts. Collect it using the company.verification.document.front and company.verification.document.back arguments.

[sanctions](/connect/risk-management/best-practices#sanctions-concerns)

[proof-of-entity document](/connect/handling-api-verification#acceptable-verification-documents)

[payouts](/payouts)

[company.verification.document.front](/api/accounts/object#account_object-company-verification-document-front)

[company.verification.document.back](/api/accounts/object#account_object-company-verification-document-back)

Depending on the situation, you might need to collect a scan of an ID document, an address document, or both to enable payouts. That can happen if Stripe can’t verify the individual or if there are possible concerns about sanctions. In some cases, depending on various calculated risk factors, Stripe can use Simplified Due Diligence and request only one document for verification at a later time.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[sanctions](/connect/risk-management/best-practices#sanctions-concerns)

Collect ID information using the individual.verification.document.front and individual.verification.document.back arguments, and address information using the verification.additional_document.front and verification.additional_document.back arguments.

[individual.verification.document.front](/api/accounts/update#update_account-individual-verification-document-front)

[individual.verification.document.back](/api/accounts/update#update_account-individual-verification-document-back)

[verification.additional_document.front](/api/persons/object#person_object-verification-additional_document-front)

[verification.additional_document.back](/api/persons/object#person_object-verification-additional_document-back)

A person known as a representative must activate this connected account. The representative must be a beneficial owner who is authorized to sign for the company. Indicate this relationship to Stripe by setting relationship.executive to true, or, if the representative owns 25% or more of the company, by setting relationship.owner to true.

[beneficial owner](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)

[relationship.executive](/api/persons/object#person_object-relationship-executive)

[relationship.owner](/api/persons/object#person_object-relationship-owner)

You might need to collect a scan of an ID document and an address document to enable payouts. That can happen if Stripe can’t verify the representative’s provided information or if there are possible concerns about sanctions. In some cases, depending on various calculated risk factors, Stripe can use Simplified Due Diligence and request only one document for verification at a later time.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[address document](/connect/handling-api-verification#acceptable-verification-documents)

[sanctions](/connect/risk-management/best-practices#sanctions-concerns)

Additionally, for partnerships you must provide a relationship.percent_ownership value.

[relationship.percent_ownership](/api/persons/object#person_object-relationship-percent_ownership)

You can collect ID information with the verification.document.front and verification.document.back arguments.

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

For companies, excluding partnerships, you must collect information on all directors. Directors are members of the governing board of the company. When you have finished collecting the required information from all directors, or if your company does not have any directors, you must inform Stripe by setting company.directors_provided to true.

[directors](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)

[company.directors_provided](/api/accounts/object#account_object-company-directors_provided)

You might need to collect a scan of an ID document and an address document to enable payouts. That can happen if Stripe can’t verify the director’s provided information or if there are possible concerns about sanctions. In some cases, depending on various calculated risk factors, Stripe can use Simplified Due Diligence and request only one document for verification at a later time.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[address document](/connect/handling-api-verification#acceptable-verification-documents)

[sanctions](/connect/risk-management/best-practices#sanctions-concerns)

You can collect ID information using the verification.document.front and verification.document.back arguments, and address information using the verification.additional_document.front and verification.additional_document.back arguments.

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

[verification.additional_document.front](/api/persons/object#person_object-verification-additional_document-front)

[verification.additional_document.back](/api/persons/object#person_object-verification-additional_document-back)

You must collect information on all beneficial owners. Beneficial owners are persons who exercise significant management control over the company (executives) or who own 25% or more of the company (owners). When you have finished collecting the required information from all beneficial owners, you must inform Stripe by setting both company.owners_provided and company.executives_provided to true.

[beneficial owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)

[company.owners_provided](/api/accounts/object#account_object-company-owners_provided)

[company.executives_provided](/api/accounts/object#account_object-company-executives_provided)

You might need to collect a scan of an ID document and an address document to enable payouts. That can happen if Stripe can’t verify the beneficial owner’s provided information or if there are possible concerns about sanctions. In some cases, depending on various calculated risk factors, Stripe can use Simplified Due Diligence and request only one document for verification at a later time.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[address document](/connect/handling-api-verification#acceptable-verification-documents)

[sanctions](/connect/risk-management/best-practices#sanctions-concerns)

You can collect ID information using the verification.document.front and verification.document.back arguments, and address information using the verification.additional_document.front and verification.additional_document.back arguments.

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

[verification.additional_document.front](/api/persons/object#person_object-verification-additional_document-front)

[verification.additional_document.back](/api/persons/object#person_object-verification-additional_document-back)

Optionally, you can collect ownership information on each person who owns 25% or more of the company with relationship.owner and relationship.percent_ownership.

[relationship.owner](/api/persons/object#person_object-relationship-owner)

[relationship.percent_ownership](/api/persons/object#person_object-relationship-percent_ownership)

Additionally, for partnerships you need to provide a relationship.percent_ownership value for any owners added to the account.

[relationship.percent_ownership](/api/persons/object#person_object-relationship-percent_ownership)

After supplying the beneficial owner information, it is checked against the National Registry of Businesses (NRB). Depending on the results of this check, there are three outcomes:

- The business is found in the NRB, and the information matches. The account is fully onboarded, and no additional action is required.

- The business is found in the NRB, but the information doesn’t match. The account is fully onboarded, and no additional action is required. A discrepancy report is sent to the NRB.

- The business isn’t found in the NRB. An attestation consisting of an IP address, date, and user agent of the person submitting the information must be provided. The person is attesting that the business is registered with the NRB, and the information given to Stripe matches.

In the case where the business isn’t found in the NRB, attesting that the beneficial ownership information is complete and correct is accomplished by providing the company.ownership_declaration.date and company.ownership_declaration.ip arguments.

[company.ownership_declaration.date](/api/accounts/object#account_object-company-ownership_declaration-date)

[company.ownership_declaration.ip](/api/accounts/object#account_object-company-ownership_declaration-ip)

If Stripe is unable to verify the representative, you need to provide a scan of an ID document. This can be collected with the verification.document.front and verification.document.back arguments.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

If Stripe is unable to verify the owner, you need to provide a scan of an ID document. This can be collected with the verification.document.front and verification.document.back arguments.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

If Stripe is unable to verify the individual, you need to provide a scan of an ID document. This can be collected with the individual.verification.document.front and individual.verification.document.back arguments.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[individual.verification.document.front](/api/accounts/update#update_account-individual-verification-document-front)

[individual.verification.document.back](/api/accounts/update#update_account-individual-verification-document-back)

After supplying the beneficial owner information, it is checked against the National Registry of Businesses (NRB). Depending on the results of this check, there are three outcomes:

- The business is found in the NRB, and the information matches. The account is fully onboarded, and no additional action is required.

- The business is found in the NRB, but the information doesn’t match. The account is fully onboarded, no additional action is required. A discrepancy report is sent to the NRB.

- The business is not found in the NRB. A proof of registration document (screenshot of the registration or copy of the confirmation email) is required to be uploaded.

In the case the business is not found in the NRB, a screenshot of the beneficial owner information from the NRB must be uploaded using the documents.proof_of_registration.files argument.

[documents.proof_of_registration.files](/api/accounts/create#create_account-documents-proof_of_registration-files)

Pass the file in the file parameter and set the purpose parameter to account_requirement:

This request uploads the file and returns a token:

You may then use the token’s id value to attach the file to a connected account for identity verification.

We’ll verify that the legal owner of each payout bank account matches that of the Stripe account.

[matches that of the Stripe account](https://support.stripe.com/questions/bank-account-ownership-verification)

If Stripe can’t verify the owner of the bank account, we’ll transition the status of the ExternalAccount to verification_failed. You’ll need to collect a scan of a cancelled check or bank statement to prove the legal owner of the bank account. Collect this information with the documents.bank_account_ownership_verification.files argument.

[documents.bank_account_ownership_verification.files](/api/accounts/update#update_account-external_account-documents-bank_account_ownership_verification)

You must provide a scan of an ID document for the representative. To collect this scan, use the verification.document.front and verification.document.back arguments.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

Identity verification documents must be issued in Japan and show the representative’s residency status.

You must collect a scan of an ID document for an individual. To collect this scan, use the individual.verification.document.front and individual.verification.document.back arguments.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[individual.verification.document.front](/api/accounts/update#update_account-individual-verification-document-front)

[individual.verification.document.back](/api/accounts/update#update_account-individual-verification-document-back)

Identity verification documents must be issued in Japan and show the individual’s residency status.

Collecting information for Japanese accounts is unique in that both kana and kanji language variations are required for a number of parameters:

- first_name_kana

- first_name_kanji

- last_name_kana

- last_name_kanji

- name_kana

- name_kanji

- address_kana

- address_kanji

You need to submit information for these parameters instead of their counterparts (that is, instead of first_name, last_name, and so forth). It might seem counterintuitive to provide two arguments that represent the same onboarding requirement, but Stripe can’t verify a Japanese account until we’ve received information for both language variations. These variations may be composed of full- or half-width hiragana, katakana, or Latin characters, with kanji-specific API parameters also allowing for kanji characters.

Both kana and kanji language variations apply to Japanese address requirements as well.

postal_code is always required when providing a Japanese address of either language variation. Stripe validates submitted addresses, and for a valid postal_code, we attempt to automatically fill attributes for matching state, city, and town for bothj address_kana and address_kanji.

Requests with address details that are incompatible with the provided postal_code fail.

line2 should contain the building name in addition to the room number if applicable. This attribute can be omitted when the address does not contain building details.

Here’s an example representation of a Japanese address, with explanations for how each part maps to its corresponding Stripe API attribute:

Statement descriptors explain charges or payments and include information that banks and card networks require to help customers understand their statements.

We recommend setting the static components of statement descriptors in all three supported scripts (kanji, kana, and Latin characters) for Japanese connected accounts.

[static](/get-started/account/statement-descriptors#static)

You can set these fields with API.

[API](/api/accounts/create#create_account-settings-payments-statement_descriptor)

See Japanese statement descriptors for more details.

[Japanese statement descriptors](/get-started/account/statement-descriptors#set-japanese-statement-descriptors)

After supplying the beneficial owner information, it is checked against the National Registry of Businesses (NRB). Depending on the results of this check, there are three outcomes:

- The business is found in the NRB, and the information matches. The account is fully onboarded, and no additional action is required.

- The business is found in the NRB, but the information doesn’t match. The account is fully onboarded, and no additional action is required. A discrepancy report is sent to the NRB.

- The business isn’t found in the NRB. An attestation consisting of an IP address, date, and user agent of the person submitting the information must be provided. The person is attesting that the business is registered with the NRB, and the information given to Stripe matches.

In the case where the business isn’t found in the NRB, attesting that the beneficial ownership information is complete and correct is accomplished by providing the company.ownership_declaration.date and company.ownership_declaration.ip arguments.

[company.ownership_declaration.date](/api/accounts/object#account_object-company-ownership_declaration-date)

[company.ownership_declaration.ip](/api/accounts/object#account_object-company-ownership_declaration-ip)

If Stripe is unable to verify the business entity, the entity doesn’t have a company.tax_id, or there are possible concerns about sanctions, you need to collect a proof of entity document to enable payouts. Collect it using the company.verification.document.front and company.verification.document.back arguments.

[sanctions](/connect/risk-management/best-practices#sanctions-concerns)

[payouts](/payouts)

[company.verification.document.front](/api/accounts/object#account_object-company-verification-document-front)

[company.verification.document.back](/api/accounts/object#account_object-company-verification-document-back)

company refers to these types of entities:

- Sociedad Anónima (S.A.)

- Sociedad de Responsabilidad Limitada (S. de R.L.)

- Sociedad Anónima Promotora de Inversión (S.A.P.I.)

- Sociedad por Acciones Simplificada (S.A.S.)

If the individual fails verification, doesn’t have an individual.id_number, or there are possible concerns about sanctions, then an ID document scan is required to enable payouts. You can collect that information using the individual.verification.document.front and individual.verification.document.back arguments.

[sanctions](/connect/risk-management/best-practices#sanctions-concerns)

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[individual.verification.document.front](/api/accounts/update#update_account-individual-verification-document-front)

[individual.verification.document.back](/api/accounts/update#update_account-individual-verification-document-back)

A person known as a representative must activate this connected account. The representative must be an authorized signatory with legal powers to represent the company as set forth under the relevant corporate documents, and must be authorized to agree to Stripe’s terms.

If Stripe is unable to verify the representative, the representative doesn’t have a representative.id_number, or there are possible concerns about sanctions, you must collect a scan of an ID document to enable payouts. Collect ID information using the verification.document.front and verification.document.back arguments.

[representative.id_number](/api/persons/update#update_person-id_number)

[sanctions](/connect/risk-management/best-practices#sanctions-concerns)

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

You must collect information on all owners with more than 25% ownership of the company. When you have finished collecting the required owner information, you must inform Stripe by setting company.owners_provided to true.

[owners](https://support.stripe.com/questions/beneficial-owner-and-director-definition)

[company.owners_provided](/api/accounts/object#account_object-company-owners_provided)

If Stripe is unable to verify an owner, an owner doesn’t have an owners.id_number, or there are possible concerns about sanctions, you must collect a scan of an ID document to enable payouts. Collect ID information using the verification.document.front and verification.document.back arguments.

[owners.id_number](/api/persons/update#update_person-id_number)

[sanctions](/connect/risk-management/best-practices#sanctions-concerns)

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

Optionally, you can collect ownership information on each person using the relationship.owner and relationship.percent_ownership arguments.

[relationship.owner](/api/persons/object#person_object-relationship-owner)

[relationship.percent_ownership](/api/persons/object#person_object-relationship-percent_ownership)

If Stripe is unable to verify the company, or if there are possible concerns about sanctions, you must collect a proof-of-entity document to enable payouts. Collect it using the company.verification.document.front and company.verification.document.back arguments.

[sanctions](/connect/risk-management/best-practices#sanctions-concerns)

[proof-of-entity document](/connect/handling-api-verification#acceptable-verification-documents)

[payouts](/payouts)

[company.verification.document.front](/api/accounts/object#account_object-company-verification-document-front)

[company.verification.document.back](/api/accounts/object#account_object-company-verification-document-back)

Depending on the situation, you might need to collect a scan of an ID document, an address document, or both to enable payouts. That can happen if Stripe is unable to verify the individual or if there are possible concerns about sanctions. Collect ID information using the individual.verification.document.front and individual.verification.document.back arguments.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[sanctions](/connect/risk-management/best-practices#sanctions-concerns)

[individual.verification.document.front](/api/accounts/update#update_account-individual-verification-document-front)

[individual.verification.document.back](/api/accounts/update#update_account-individual-verification-document-back)

A person known as a representative must activate this connected account. The representative must be a beneficial owner who is authorized to sign for the company. Indicate that relationship to Stripe by setting relationship.executive to true, or, if the representative owns 25% or more of the company, by setting relationship.owner to true.

[beneficial owner](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)

[relationship.executive](/api/persons/object#person_object-relationship-executive)

[relationship.owner](/api/persons/object#person_object-relationship-owner)

Depending on the situation, you might need to collect a scan of an ID document to enable payouts. That can happen if Stripe is unable to verify the representative or if there are possible concerns about sanctions. Collect ID information using the verification.document.front and verification.document.back arguments.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[sanctions](/connect/risk-management/best-practices#sanctions-concerns)

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

Optionally, you can collect the representative’s ownership information using the relationship.representative and relationship.percent_ownership arguments.

[relationship.representative](/api/persons/object#person_object-relationship-representative)

[relationship.percent_ownership](/api/persons/object#person_object-relationship-percent_ownership)

For companies (excluding partnerships), you must collect information on all directors. Directors are members of the governing board of the company. When you have finished collecting the required information from all directors, or if your company does not have any directors, you must notify Stripe by setting company.directors_provided to true.

[directors](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)

[company.directors_provided](/api/accounts/object#account_object-company-directors_provided)

If there are possible concerns about sanctions, you must collect a scan of an ID document to enable payouts. Collect ID information using the verification.document.front and verification.document.back arguments.

[sanctions](/connect/risk-management/best-practices#sanctions-concerns)

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

You must collect information on all beneficial owners. Beneficial owners are persons who exercise significant management control over the company (executives) or who own 25% or more of the company (owners). When you have finished collecting the required information from all beneficial owners, you must notify Stripe by setting both company.owners_provided and company.executives_provided to true.

[beneficial owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)

[company.owners_provided](/api/accounts/object#account_object-company-owners_provided)

[company.executives_provided](/api/accounts/object#account_object-company-executives_provided)

Depending on the situation, you might need to collect a scan of an ID document to enable payouts. That can happen if Stripe is unable to verify a beneficial owner or if there are possible concerns about sanctions. Collect ID information using the verification.document.front and verification.document.back arguments.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[sanctions](/connect/risk-management/best-practices#sanctions-concerns)

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

Optionally, you can collect ownership information on each person who owns 25% or more of the company using the relationship.owner and relationship.percent_ownership arguments.

[relationship.owner](/api/persons/object#person_object-relationship-owner)

[relationship.percent_ownership](/api/persons/object#person_object-relationship-percent_ownership)

If you don’t integrate with Connect Onboarding, you won’t be able to onboard connected accounts subject to enhanced identity verification.

[Connect Onboarding](https://stripe.com/connect/onboarding)

To comply with Singapore’s Payment Services Act 2019, we require individuals to verify their identities either by using MyInfo or by taking a selfie with their identity document through Stripe Identity. Additionally, your platform needs to integrate with Connect Onboarding to satisfy the proof_of_liveness identity verification requirement. We verify addresses with MyInfo or request documents, such as utility bills or bank statements, when necessary.

[Payment Services Act 2019](https://stripe.com/guides/sg-payment-services-act-2019)

[MyInfo](https://www.singpass.gov.sg/main/individuals/)

[Connect Onboarding](https://stripe.com/connect/onboarding)

If you don’t integrate with Connect Onboarding, you won’t be able to onboard connected accounts subject to enhanced identity verification.

[Connect Onboarding](https://stripe.com/connect/onboarding)

To comply with Singapore’s Payment Services Act 2019, we require individuals to verify their identities either by using MyInfo or by taking a selfie with their identity document through Stripe Identity. Additionally, your platform needs to integrate with Connect Onboarding to satisfy the proof_of_liveness identity verification requirement. We verify addresses with MyInfo or request documents, such as utility bills or bank statements, when necessary.

[Payment Services Act 2019](https://stripe.com/guides/sg-payment-services-act-2019)

[MyInfo](https://www.singpass.gov.sg/main/individuals/)

[Connect Onboarding](https://stripe.com/connect/onboarding)

An account’s legal representative must be an owner of the business entity with at least 25% ownership, or a controller, defined as an individual with significant management responsibility for the entity, such as a Director, or Partner.

If you don’t integrate with Connect Onboarding, you won’t be able to onboard connected accounts subject to enhanced identity verification.

[Connect Onboarding](https://stripe.com/connect/onboarding)

To comply with Singapore’s Payment Services Act 2019, we require individuals to verify their identities either by using MyInfo or by taking a selfie with their identity document through Stripe Identity. Additionally, your platform needs to integrate with Connect Onboarding to satisfy the proof_of_liveness identity verification requirement. We verify addresses with MyInfo or request documents, such as utility bills or bank statements, when necessary.

[Payment Services Act 2019](https://stripe.com/guides/sg-payment-services-act-2019)

[MyInfo](https://www.singpass.gov.sg/main/individuals/)

[Connect Onboarding](https://stripe.com/connect/onboarding)

An account’s legal representative must be an owner of the business entity with at least 25% ownership, or a controller, defined as an individual with significant management responsibility for the entity, such as a Director, or Partner.

Accounts that belong to companies must provide information on all their beneficial owners and directors. Beneficial owners are natural persons who hold ultimate effective control over the account:

- Companies:All natural persons owning (directly or indirectly, through a holding company) more than 25% of the shares, or owning more than 10% if no one owns more than 25%All Directors of the Company

- All natural persons owning (directly or indirectly, through a holding company) more than 25% of the shares, or owning more than 10% if no one owns more than 25%

[holding company](https://support.stripe.com/questions/beneficial-ownership-verification-for-holding-companies)

- All Directors of the Company

- Partnerships:All PartnersAll Managers

- All Partners

- All Managers

If Stripe is unable to verify a beneficial owner, you need to provide a scan of an ID document. To collect an ID document, use the verification.document.front and verification.document.back arguments.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

Accounts that belong to non-profits must provide information on all their beneficial owners and directors. Beneficial owners are natural persons who hold ultimate effective control over the account. In the case of non-profits, these are the key officers and members of the Governing Board.

If Stripe is unable to verify a beneficial owner, you need to provide a scan of an ID document. To collect an ID document, use the verification.document.front and verification.document.back arguments.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

As required under Singapore’s Payment Services Act, we’re permanently closing Singapore accounts that remain unverified for over 120 business days. These are accounts whose charges or payouts have already been suspended, so this closure affects only inactive accounts.

[Singapore’s Payment Services Act](https://stripe.com/guides/sg-payment-services-act-2019)

To help you identify affected accounts, we upload monthly reports titled “Unverified account list” to your Dashboard under the reporting and documents section, in which you’ll find the list of impacted accounts and their requirement deadlines. Any accounts closed in the last month are in the report titled “Closed unverified account list.”

We’ll close any account that hasn’t been verified by its designated deadline. The account owner needs to provide the missing verification information before the deadline to keep the account open. If the information is provided after the deadline has passed, we’ll release any remaining balance to the account holder’s bank account, but we won’t be able to reactivate their Stripe account.

Stripe sends emails to Standard and Express accounts that remain unverified for too long, to inform them of the impending closure and to remind them to update their account details. Stripe won’t communicate with Custom connected accounts directly. That means you, as the platform, can contact them to avoid account closures.

Accounts that are closed under this process have their disabled_reason set to rejected.other.

[disabled_reason](/api/accounts/object#account_object-requirements-disabled_reason)

UEN information might be verified with the data made available at https://data.gov.sg under the terms of the Singapore Open Data License version 1.0.

[Singapore Open Data License version 1.0](https://data.gov.sg/open-data-licence)

To comply with regulatory requirements in Thailand, we require additional identity verification for certain connected accounts. This entails taking a selfie and uploading an ID document using Stripe Identity. Your platform needs to integrate with Connect Onboarding to satisfy this identity verification requirement.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[Stripe Identity](/identity)

[Connect Onboarding](https://stripe.com/connect/onboarding)

Additional identity verification applies to the representatives and beneficial owners of connected accounts belonging to individuals, sole proprietors and unregistered partnerships.

If you don’t integrate with Connect Onboarding, you won’t be able to onboard connected accounts subject to additional identity verification.

[Connect Onboarding](https://stripe.com/connect/onboarding)

The registered address requirement refers to the Household Registration address. Please provide an address as per the ‘Tabien Bann’ or Household Registration book, also known as the Blue book for Thai nationals, or Yellow book for non-Thai nationals. To collect a Household Registration address, use the registered_address parameter.

[registered_address](/api/persons/object#person_object-registered_address)

If the user is neither a Thai national nor resident of Thailand, collect their current residential address with the same parameter instead.

The ID number requirement refers to the 13-digit code found on the front of a Thai ID card, and secondary ID number requirement refers to the laser code found at the back of a Thai ID card. To collect a Thai ID number use the id_number parameter, and to collect a laser code use the id_number_secondary parameter.

[id_number](/api/persons/create#create_person-id_number)

[id_number_secondary](/api/persons/create#create_person-id_number_secondary)

These requirements are only applicable to Thai nationals, so leave the parameters empty if the user isn’t a Thai national.

If Stripe is unable to verify the individual or if they’re not a Thai national, you need to collect a scan of an ID document. To collect an ID document, use the individual.verification.document.front and individual.verification.document.back parameters.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[individual.verification.document.front](/api/accounts/update#update_account-individual-verification-document-front)

[individual.verification.document.back](/api/accounts/update#update_account-individual-verification-document-back)

If Stripe is unable to verify the account representative or if they’re not a Thai national, you need to provide a scan of an ID document. To collect an ID document, use the verification.document.front and verification.document.back parameters.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

Accounts belonging to companies and registered partnerships are required to provide information on all beneficial owners. A beneficial owner is defined as any individual who owns 25% or more shares of the business. If there is no such person, then any individual who exercises significant control over the company is considered a beneficial owner. Otherwise, please provide information on any individual holding the position of senior management.

If Stripe is unable to verify a beneficial owner or if they’re not a Thai national, you need to provide a scan of an ID document. To collect an ID document, use the verification.document.front and verification.document.back parameters.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

If Stripe is unable to verify the company, you need to provide a scan of a company verification document issued less than 6 months ago. To collect the company verification document scan, use the company.verification.document.front and company.verification.document.back parameters on the Account object.

[company verification document](/connect/handling-api-verification#acceptable-verification-documents)

[company.verification.document.front](/api/accounts/object#account_object-company-verification-document-front)

[company.verification.document.back](/api/accounts/object#account_object-company-verification-document-back)

If Stripe is unable to verify the company.tax_id, upload a copy of an IRS Letter 147C document or an IRS SS-4 confirmation letter as an alternate attempt at verification. This information can be collected with the company.verification.document.front argument, and should include the connected account’s company.name and company.tax_id.

[an IRS Letter 147C document or an IRS SS-4 confirmation letter](https://support.stripe.com/questions/using-irs-documentation-as-reference-when-entering-business-name-and-tax-id-number-tin-for-us-based-businesses)

[company.verification.document.front](/api/accounts/object#account_object-company-verification-document-front)

To enable card payments, a validated city, state, and ZIP code for company.address is required. Card payments will be disabled if the company.tax_id (EIN) hasn’t been verified before 30 days or 1,500 USD in payments, whichever comes first.

To enable payouts, company.address needs to be a validated full address and the company.tax_id (EIN) needs to be verified. Payouts will be disabled if a full address hasn’t been validated or the company.tax_id is not verified before 30 days.

[payouts](/payouts)

To enable card payments, a validated city, state, and ZIP code for individual.address is required.

To enable payouts, individual.address needs to be a validated full address. Payouts will be disabled if a full address hasn’t been validated before 30 days.

If the individual fails verification with ssn_last_4, then the full SSN is required and their identity needs to be verified to enable card payments. Use the individual.id_number argument to collect this information.

[individual.id_number](/api/accounts/update#update_account-individual-id_number)

This connected account needs to be activated by a person, known as a representative, with significant responsibility to control, manage, or direct the organization; and is authorized by the organization to agree to Stripe’s terms. The representative must either be an owner or an executive, which you specify by setting relationship.owner to true or relationship.executive to true.

[an owner or an executive](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)

[relationship.owner](/api/persons/object#person_object-relationship-owner)

[relationship.executive](/api/persons/object#person_object-relationship-executive)

If the representative fails verification with ssn_last_4, then the full SSN is required and their identity needs to be verified to enable card payments. Use the person.id_number argument to collect this information.

[person.id_number](/api/persons/update#update_person-id_number)

If Stripe is unable to verify the representative or if the person doesn’t have an SSN, you need to collect a scan of an ID document to enable card payments. This information can be collected with the verification.document.front and verification.document.back arguments.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

If the account representative is a minor, you must verify the minor’s legal guardian. A legal guardian is a Person on the account with relationship.legal_guardian set to true. Additionally, the legal guardian must provide their information and sign the Stripe terms of service, which we store on the Person object with relationship.legal_guardian set to true. Store the legal guardian’s terms of service acceptance in the additional_tos_acceptances hash.

[Person](/api/persons)

[relationship.legal_guardian](/api/persons/create#create_person-relationship-legal_guardian)

[additional_tos_acceptances](/api/persons/create#create_person-additional_tos_acceptances)

If the legal guardian fails verification with ssn_last_4, then the full SSN is required and their identity needs to be verified to enable card payments. Use the person.id_number argument to collect this information.

[person.id_number](/api/persons/update#update_person-id_number)

If Stripe is unable to verify the legal guardian or if the person doesn’t have an SSN, you need to collect a scan of an ID document to enable card payments. This information can be collected with the verification.document.front and verification.document.back arguments.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

Information on all owners with 25% or more ownership of the company must be collected. When you have finished collecting the required owner information, you need to attest this by setting company.owners_provided to true. This lets Stripe know that you have completed this requirement.

[owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)

If there are any unverified owners in the company, payouts on the connected account can become disabled at 750,000 USD in charges and charges can become disabled at 1 million USD, unless the following information is collected:

- owners.dob.day

- owners.dob.month

- owners.dob.year

- owners.address

- owners.ssn_last_4

- owners.phone

If the owner fails verification with ssn_last_4, then the full SSN is required and their identity needs to be verified to enable card payments. Use the person.id_number argument to collect this information.

[person.id_number](/api/persons/update#update_person-id_number)

If Stripe is unable to verify an owner or if an owner doesn’t have an SSN, you need to collect a scan of an ID document. This information can be collected with the verification.document.front and verification.document.back arguments.

[ID document](/connect/handling-api-verification#acceptable-verification-documents)

[verification.document.front](/api/persons/object#person_object-verification-document-front)

[verification.document.back](/api/persons/object#person_object-verification-document-back)

Optionally, you can collect company ownership information. This can be done using the relationship.owner and relationship.percent_ownership attributes. Set relationship.owner to true and relationship.percent_ownership to the user’s ownership percentage. If relationship.percent_ownership is unspecified, the default is 25%.

[relationship.owner](/api/persons/object#person_object-relationship-owner)

[relationship.percent_ownership](/api/persons/object#person_object-relationship-percent_ownership)

Optionally, you can collect information on the legal structure of your user’s business with the company.structure argument. See Business structure for more details.

[company.structure](/api/accounts/create#create_account-company-structure)

[Business structure](/connect/identity-verification#business-structure)

Below lists the supported business structures for privately held companies:

- multi_member_llc

- single_member_llc

- private_partnership

- private_corporation

- unincorporated_association

Below lists the supported business structures for publicly traded companies. If you further classify the business with any of these structures, the representative doesn’t need to be an owner nor an executive, and you do not need to provide information on additional owners.

[representative](#additional-company-card-representative-us)

- public_corporation

- public_partnership

Optionally, you can collect information on the legal structure of your user’s business. This can be done using the company.structure argument. See Business structure for more details.

[company.structure](/api/accounts/create#create_account-company-structure)

[Business structure](/connect/identity-verification#business-structure)

Below lists the supported business structures for government entities:

- governmental_unit

- government_instrumentality

If your user is an instrumentality with tax-exempt status, you can set the company.structure to tax_exempt_government_instrumentality.

While uncommon, there are circumstances where an individual business operates and is treated more like a company, such as a single-member LLC. For these users, you can optionally collect information on their legal structure with the company.structure argument.

[legal structure](/connect/identity-verification#business-structure)

[company.structure](/api/accounts/create#create_account-company-structure)

If your user’s business has only one member or owner and is registered as an LLC with a US state, you can set the business_type to company and the company.structure to single_member_llc. You collect the same required information, except you use the company hash and the Persons API, instead of the individual hash. For any requirement in the individual hash, you need to map it to the account’s representative, such as setting representative.first_name instead of individual.first_name.

[company](/api/accounts/object#account_object-company)

[Persons](/api/persons)

If your user has obtained a business identification (for example, has a tax ID that’s separate from their personal ID, or a business address that’s different than their home address), you can set the business_type to company and the company.structure to sole_proprietorship. You collect the same required information, except you use the company hash and the Persons API, instead of the individual hash since it pertains to the natural person. For any requirement in the individual hash, you need to map it to the account’s representative, such as setting representative.first_name instead of individual.first_name.

[company](/api/accounts/object#account_object-company)

[Persons](/api/persons)

Optionally, you can collect information on the legal structure of your user’s business with the company.structure argument. See Business structure for more details.

[company.structure](/api/accounts/create#create_account-company-structure)

[Business structure](/connect/identity-verification#business-structure)

Below lists the supported business structures for non-profit organizations:

- incorporated_non_profit

- unincorporated_non_profit

The US federal government grants tax-exempt status to certain government entities that are considered non-profit. If your user is an instrumentality with tax-exempt status, you can set the business_type to government_entity and the company.structure to tax_exempt_government_instrumentality. Then, collect the appropriate verification requirements from them.

[appropriate verification requirements](#government-entity-card-us)

By default, the requirements for transfers do not collect all information at the appropriate thresholds to file IRS Form 1099-K or Form 1099-MISC. If your business has US federal 1099 filing requirements and plans to file these through Stripe, request the appropriate tax reporting capability and make sure to collect the necessary information from your users.

[appropriate tax reporting capability](/connect/account-capabilities#tax-reporting)

[necessary information](/connect/required-verification-information-taxes)

In addition to the onboarding requirements, there is a second threshold to keep payouts enabled, which depends on your industry and Stripe’s review of your platform profile. The company.tax_id (EIN) needs to be verified before 10,000 USD in charges for some platforms, and before 3,000 USD for other platforms.

In addition to the onboarding requirements, there is a second threshold to keep payouts enabled, which depends on your industry and Stripe’s review of your platform profile. The company.tax_id (EIN) needs to be verified before 10,000 USD in charges for some platforms, and before 3,000 USD for other platforms.

- individual.dob.day

- individual.dob.month

- individual.dob.year

- individual.ssn_last_4

When an account with card_payments reaches 500,000 USD in lifetime charges, we require a full id_number (SSN) for them to continue accepting payments. If they’ve already provided the full number, they don’t have to provide it again.

For accounts with business_type set to individual, and where the owner isn’t a minor, update the account’s individual.id_number. For other accounts, which have persons with relationship.legal_guardian, relationship.representative, or relationship.owner, update the appropriate person’s id_number.

[update the account’s individual.id_number](/api/accounts/update#update_account-individual-id_number)

[relationship.legal_guardian](/api/persons/object#person_object-relationship-representative)

[relationship.representative](/api/persons/object#person_object-relationship-representative)

[relationship.owner](/api/persons/object#person_object-relationship-owner)

[update the appropriate person’s id_number](/api/persons/update#update_person-id_number)

As a best practice, organize the required parameters into logical groupings or forms in your onboarding flow. You might wish to encode a mapping between the Stripe parameters and the logical groupings. Suggested logical groupings for parameters are shown in the first column of the example requirements table.

After you encode the required parameters into your application, generate UIs for the parameters corresponding to these requirements. For each parameter, design a UI form that includes:

- Parameter label, localized to each supported country and language

- Parameter description, localized to each supported country and language

- Parameter input fields with data validation logic and document uploading where required

It’s important to architect your application logic to account for the possibility of additional parameters in the future. For example, Stripe might introduce new parameters, new verifications, or new thresholds that you must incorporate into your onboarding flows over time.

Changing any of the factors that determine your connected accounts requirements means you must also adjust your collection forms. Country and service agreement type are immutable, while capabilities and business type are mutable.

[Country](/api/accounts/object#account_object-country)

[service agreement type](/api/accounts/object#account_object-tos_acceptance-service_agreement)

[capabilities](/api/accounts/object#account_object-capabilities)

[business type](/api/accounts/object#account_object-business_type)

- To change an immutable field such as country or service agreement type, create a new connected account with the new values. Doing so produces new requirements for you to incorporate in your collection flows.

- To change a mutable field such as capabilities or business type, update the connected account. Doing so produces new requirements for you to incorporate in your collection flows.

Your connected accounts must accept Stripe terms of service before they can be activated. You can wrap Stripe terms of service in your own terms of service.

[wrap Stripe terms of service in your own terms of service](/connect/updating-service-agreements#adding-stripes-service-agreement-to-your-terms-of-service)

Use the Create Account API to create a connected account with country, service type agreement, desired capabilities, business type, and any other information matching your requirements. At a minimum, you must specify capabilities and type. If you don’t specify other parameters, they’re assigned the following default values:

[Create Account](/api/accounts/create)

[requirements](#establish-requirements)

- The service type agreement (tos_acceptance.service_agreement) defaults to full.

- The country defaults to the same country as your platform.

The following code sample creates a Custom connected account with card_payments and transfers capabilities under a full service agreement for an individual.

This example includes only some of the fields you can set when creating an account. For a full list of the fields you can set, such as address and website_url, see the Create Account API reference.

[Create Account API reference](/api/accounts/create)

You can enable connected accounts in either of two ways:

- Incremental onboarding strategy: Collect the minimum required information up front and the rest later

[required information](#establish-requirements)

- Upfront onboarding strategy: Collect all information up front

The incremental onboarding strategy speeds up initial onboarding but requires additional information collection later on. The upfront onboarding strategy minimizes enablement disruption throughout the connected account’s lifecycle at the expense of a lengthier application process. You can decide which strategy better suits your use case.

To implement your onboarding strategy, inspect the requirements hash of the connected account you created. The requirements hash provides a complete list of parameters you must collect to activate the connected account.

- If you choose the incremental onboarding strategy, inspect the currently_due field in the requirements hash and build an onboarding flow that only collects for the listed parameters.

- If you choose the upfront onboarding strategy, inspect the eventually_due field in the requirements hash and build an onboarding flow that collects for all the listed parameters.

Update the connected account object with new information as it progresses through your onboarding flow. Perform an Update Account call, identifying the connected account by the id value you stored earlier.

[Update Account](/api/accounts/update)

[https://furever.dev](https://furever.dev)

Stripe validates every update to a connected account. Update the account at each step in onboarding to allow Stripe to validate information as soon as it’s added, while your users continue through the onboarding flow. After Stripe confirms acceptance of our terms of service, any changes to the connected account trigger reverification. For example, if you change the connected account’s name and ID number, Stripe reruns verifications.

When updating a connected account, you must handle any verification errors or HTTP error codes returned by the Accounts API.

[verification errors](#verification-handling)

[HTTP error codes](/error-handling)

## Embedded onboarding

Embedded onboarding is a highly themeable onboarding UI with limited Stripe branding. Connected account users interact with the embedded component without ever leaving your application. Embedded onboarding uses the Accounts API to read the requirements and generate an onboarding form with robust data validation and that is localized for all Stripe-supported countries. In addition, embedded onboarding handles all:

[Accounts API](/api/accounts)

- Business types

- Configurations of company representatives

- Verification document uploading

- Identify verification and statuses

- International bank accounts

- Error states

You can integrate embedded onboarding in a few lines of code, while API-based onboarding requires you to construct custom logic. To integrate embedded onboarding, follow our embedded components guide and integrate the Account onboarding embedded component.

[embedded components guide](/connect/get-started-connect-embedded-components)

[Account onboarding](/connect/supported-embedded-components/account-onboarding)

## Stripe hosted onboarding

Stripe hosted onboarding allows you to redirect your user to Stripe to complete the onboarding process in a co-branded interface. Create an Account Link and direct your user to the hosted onboarding flow. The return_url allows Stripe to return the user to your application and allow you to progress the connected account accordingly.

[Account Link](/api/account_links)

[return_url](/api/account_links/create#create_account_link-return_url)

To integrate Stripe hosted onboarding, follow our Stripe hosted onboarding guide.

[Stripe hosted onboarding guide](/connect/custom/hosted-onboarding)

## Verification handling

When the connected account’s data is submitted, Stripe verifies it. This process might take minutes or hours depending on the nature of the verification required. During this process, the capabilities you requested have a pending status.

[a pending status](/api/accounts/object#account_object-capabilities)

You can retrieve the status of your connected account’s capabilities by:

- Inspecting the Account object’s capabilities hash for the relevant capability.

[capabilities](/api/accounts/object#account_object-capabilities)

- Requesting capabilities directly from the Capabilities API and inspecting the status of the relevant capability.

[Capabilities API](/api/capabilities/retrieve)

- Listening for account.updated events in your webhook endpoint and inspecting the capabilities hash for the relevant capability.

[events](/api/events/types#event_types-account.updated)

[webhook](/connect/webhooks)

After verifications are complete, the capability becomes active and available to the connected account. Account verifications run continuously, and if a future verification fails, a capability can transition out of active. Listen for account.updated events to detect changes to capability states.

Confirm that your Connect integration is compliant and operational by checking that the account’s charges_enabled and payouts_enabled are both true. You can use the API or listen for account.updated events. For details on other relevant fields, check the account’s requirements hash. You can’t confirm the integration based on a single value because statuses can vary depending on the application and related policies.

[requirements](/api/accounts/object#account_object-requirements)

- charges_enabled confirms that your full charge path including the charge and transfer works correctly and evaluates if either card_payments or transfers capabilities are active.

[charges_enabled](/api/accounts/object#account_object-charges_enabled)

- payouts_enabled evaluates whether your connected account can pay out to an external account. Depending on your risk policies, you can allow your connected account to start transacting without payouts enabled. You must eventually enable payouts to pay your connected accounts.

[payouts_enabled](/api/accounts/object#account_object-payouts_enabled)

[must eventually enable payouts](/connect/manage-payout-schedule)

You can use the following logic as a starting point for defining a summary status to display to your connected account.

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

Handle verification failures differently depending on your onboarding flow.

You can’t use the API to respond to Stripe risk reviews. You can enable your connected accounts to respond using embedded components, Stripe-hosted onboarding, or remediation links. You can also use the Dashboard to respond to risk reviews on behalf of your connected accounts.

Listen to the account.updated event. If the account contains any currently_due fields when the current_deadline arrives, the corresponding functionality is disabled and those fields are added to past_due.

[account.updated](/api/events/types#event_types-account.updated)

Create a form with clear instructions that the account can use to correct the information. Notify the account, then submit the corrected information using the Accounts API.

[Create a form](#create-forms-to-collect-information)

[submit the corrected information](#update-the-connected-account)

If you plan to create custom flows to handle all your verification errors:

- Review the details regarding all possible verification errors and how to handle them.

[verification errors and how to handle them](/connect/handling-api-verification)

- Test verification states.

[Test verification states](/connect/testing-verification)

## See also

Learn more about working with Custom accounts.

- Handle verification updates

[Handle verification updates](/connect/custom/handle-verification-updates)

- Updating Accounts

[Updating Accounts](/connect/updating-service-agreements)

- Identity Verification

[Identity Verification](/connect/identity-verification)
