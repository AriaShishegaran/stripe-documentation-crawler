htmlHandling verification with the API | Stripe Documentation[Skip to content](#main-content)Handle verification with the API[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fhandling-api-verification)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fhandling-api-verification)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Required verification information](/docs/connect/required-verification-information)# Handling verification with the API

Learn how Connect platforms can use webhooks and the API to handle verification of connected accounts.Platforms with accounts created using the API can provide Stripe with necessary information about their users for Know Your Customer (KYC) purposes. Platforms can use Connect Onboarding to collect KYC information, or use the Accounts and Persons APIs to provide Stripe with required information. We’ll then perform verification, asking for more information when needed.

The rest of this page goes through how platforms:

- Discover verification requirements for a connected account
- Provide the necessary information to Stripe

Platforms that use Custom connected accounts can also read Identity Verification for Custom Accounts to learn about verification flow options, how the API fields translate to both companies and individuals, and how to localize information requests.

NoteYou can’t use the API to respond to Stripe risk reviews. You can enable your connected accounts to respond using embedded components, Stripe-hosted onboarding, or remediation links. You can also use the Dashboard to respond to risk reviews on behalf of your connected accounts.

## Verification process

Before enabling charges and payouts for a connected account, Stripe needs certain information that varies based on:

- The origin country of the connected accounts
- The[service agreement type](/connect/service-agreement-types)applicable to the connected accounts
- The[capabilities](/connect/account-capabilities)requested for the connected accounts
- The[business type](/api/accounts/object#account_object-business_type)(for example, individual or company) and[company.structure](/api/accounts/object#account_object-company-structure)(for example, public corporation or private partnership)

Platforms need to choose the proper onboarding flow for their business and users to meet the KYC requirements. Broadly speaking, this means providing all the requisite information upfront or incrementally. Either way, set up your integration to watch for and respond to requests from Stripe.

1. Establish a[Connect webhook](/connect/webhooks)URL in your[webhook settings](https://dashboard.stripe.com/account/webhooks)to watch for activity, especially events of the`account.updated`type. When using the[Persons API](/api/persons), you should also watch for`person.updated`events.
2. Immediately after creating an account, check the`Account`object’s[requirements.currently_due](/api/accounts/object#account_object-requirements-currently_due)attribute for any additional requirements. Obtain any required information from the user and update the connected account.
3. Continue watching for`account.updated`event notifications to see if the`requirements`hash changes, and reach out to your user for additional information as needed.

When you provide additional information, you don’t need to resubmit any previously verified details. For example, if the dob is already verified, you don’t need to provide it again in subsequent updates.

CautionWhen requirements.currently_due isn’t empty, additional information is required. Connected accounts might be blocked from creating charges, receiving payouts, or performing certain tasks if you don’t provide this information in a timely manner.

### Change information after verification

After an individual or company is verified, you can change some of their information, with limitations. See the Update Account API for limitations based on the configuration of the connected account. Contact support to make changes outside of these limitations.

## Determine if verification is needed

When you receive an account.updated event to your webhook or fetch an account with the API, you receive an Account object. The Account object’s charges_enabled and payouts_enabled attributes indicate whether the account can create charges and accept payouts.

The Account object has a requirements hash, representing the requirements needed to verify the account.

The requirements hash has the following arrays:

- `eventually_due`: Fields that you might need to collect, assuming all thresholds are reached. As they become required, they appear in`currently_due`and set the`current_deadline`. All required information starts in this array.
- `currently_due`: Fields that you must collect by the`current_deadline`for the connected account to remain enabled.`currently_due`is a subset of`eventually_due`.
- `past_due`: Fields you didn’t submit by the deadline, which disabled the connected account.`past_due`is a subset of`currently_due`.
- `errors`: The list of reasons why a particular field in`eventually_due`,`currently_due`, or`past_due`must be collected again because validation or verification failed.
- `disabled_reason`: Describes why the connected account isn’t enabled.
- `current_deadline`: Date by which the fields in`currently_due`must be collected to keep the account enabled. The account may be disabled sooner if the next threshold is reached before the`currently_due`fields are collected.
- `pending_verification`: Fields that might become required depending on the results of verification or review. It’s an empty array unless an asynchronous verification is pending. If verification fails, these fields move to`eventually_due`,`currently_due`, or`past_due`. Fields might appear in`eventually_due`,`currently_due`, or`past_due`and in`pending_verification`if verification fails but another verification is still pending.

The example below shows what the requirements hash might look like for an account that has some information that’s currently_due, some information that’s eventually_due, and some information that’s raising verification errors.

`{
  "id": "{{CONNECTED_ACCOUNT_ID}}",
  "object": "account",
  "requirements": {
      "disabled_reason": null,
      "current_deadline": 1529085600,
      "past_due": [],
      "currently_due": [
          "company.tax_id",
          "company.verification.document",
          "tos_acceptance.date",
          "tos_acceptance.ip"
      ],
      "eventually_due": [
          "company.address.city",
          "company.address.line1",
          "company.address.postal_code",
          "company.address.state",
          "company.tax_id",
          "company.verification.document",
          "external_account",
          "tos_acceptance.date",
          "tos_acceptance.ip"
      ],
      "errors": [
          {
            "requirement": "company.verification.document",
            "reason": "The company name on the account couldn't be verified. Either update your business name or upload a document containing the business name.",
            "code": "failed_name_match"
          },
      ]
  },
  ...
}`If requirements.currently_due contains entries, check requirements.current_deadline. The current_deadline is a Unix timestamp identifying when information is needed. Usually, if Stripe doesn’t receive the information by the current_deadline, payouts on the account are disabled. However, other consequences might apply in some situations. For example, if payouts are already disabled and the account is unresponsive to our inquiries, Stripe might also disable the ability to process charges.

Separately, the requirements.disabled_reason property can have a value. The value is a string describing the reason why this account is unable to make payouts or charges. In some instances, platforms and connected accounts can submit a form to resolve or appeal the reason.

- Standard connected accounts can access additional information (if available) on their Dashboard.
- Platforms in any Connect configuration can navigate to[Accounts to review](/connect/dashboard/review-actionable-accounts)to understand an account’s`disabled_reason`. You might be able to provide additional information on behalf of your connected accounts. If the disabled reason is associated with an appeal, you can generate a link to a form for the account to resolve the appeal.

ReasonMeaning`action_required.requested_capabilities`You need to request capabilities for the connected account. For details, see[Request and unrequest capabilities](/connect/account-capabilities#requesting-unrequesting).`listed`Account might be on a prohibited persons or companies list (Stripe investigates and either rejects or reinstates the account accordingly).`rejected.fraud`Account is rejected due to suspected fraud or illegal activity.`rejected.incomplete_verification`The account is rejected from incomplete verification requirements within the required threshold.`rejected.listed`Account is rejected because it’s on a third-party prohibited persons or companies list (such as financial services provider or government).`rejected.other`Account is rejected for another reason.`rejected.terms_of_service`Account is rejected due to suspected terms of service violations.`requirements.past_due`Additional verification information is required to enable capabilities on this account.`requirements.pending_verification`Stripe is currently verifying information on the connected account. No action is required. Inspect the[requirements.pending_verification](/api/accounts/object#account_object-requirements-pending_verification)array to see the information being verified.`under_review`The account is under review by Stripe.## Validation and verification errors

The Account object includes a requirements.errors array that explains why the validation or verification requirements haven’t been met, which are needed to enable your account and capabilities. The errors array has the following attributes:

- `requirement`: Specifies which information from the`currently_due`array is needed.
- `code`: Indicates the type of error that occurred. See the[API reference](/api/accounts/object#account_object-requirements-errors-code)for all possible error codes.
- `reason`: Explains why the error occurred and how to resolve the error.

Below is an example that shows what the errors array might look like for an account with requirements that are currently_due. The example shows the reason why the submitted information can’t be used to enable the account, and how to resolve the error. If verification or validation is unsuccessful, requirements can reappear in currently_due with error information. Set a Connect webhook to receive the account.updated event to receive these updates.

`{
  "id": "{{CONNECTED_ACCOUNT_ID}}",
  "object": "account",
  "requirements": {
      "current_deadline": 1234567800,
      "currently_due": [
          "company.address.line1",
          "{{PERSON_ID}}.verification.document",
      ],
      "errors": [
          {
            "requirement": "company.address.line1",
            "code": "invalid_street_address",
            "reason": "The provided street address cannot be found. Please verify the street name and number are correct in \"10 Downing Street\"",
          },
          {
            "requirement": "{{PERSON_ID}}.verification.document",
            "code": "verification_document_failed_greyscale",
            "reason": "Greyscale documents cannot be read. Please upload a color copy of the document.",
          }
      ]
  },
  ...
}`If verification or validation is unsuccessful but no requirements are currently due, a webhook triggers indicating that required information is eventually due.

## Business information

When information about a business is submitted, Stripe verifies the new information. For example, Stripe might verify that the provided business URL is valid, reachable, and includes information about the business. To retrieve the status of verification information regarding a business, utilize the requirements on the Account object.

Below is a list of errors related to business information verification:

ErrorResolution`invalid_business_profile_name`Business names must be easy for people to understand and must consist of recognizable words.`invalid_business_profile_name_denylisted`Generic or well-known business names aren’t supported. Make sure the provided business name matches the account’s business.`invalid_product_description_length`A product description must be at least 10 characters.`invalid_product_description_url_match`A product description must be different from the URL of the business.invalid_url_denylisted

invalid_url_format

invalid_url_web_presence_detected

invalid_url_website_business_information_mismatch

invalid_url_website_empty

invalid_url_website_inaccessible

invalid_url_website_inaccessible_geoblocked

invalid_url_website_inaccessible_password_protected

invalid_url_website_incomplete

invalid_url_website_incomplete_cancellation_policy

invalid_url_website_incomplete_customer_service_details

invalid_url_website_incomplete_legal_restrictions

invalid_url_website_incomplete_refund_policy

invalid_url_website_incomplete_return_policy

invalid_url_website_incomplete_terms_and_conditions

invalid_url_website_incomplete_under_construction

invalid_url_website_other

See handling URL verification errors below.

## Statement descriptors

Stripe validates the statement descriptor and statement descriptor prefix when set on an account. For example, Stripe might verify that the provided statement descriptor matches the description of the business. When validating the statement descriptor matches the business description, Stripe uses the first 22 characters of the statement descriptor, representing the part that is provided to the card networks. A business description is a close match of the account’s business_profile.name, business_profile.url, or the name of the company or individual.

To retrieve the status of verification information regarding statement descriptors, review the requirements on the Account object. Below is a list of errors related to statement descriptor verification:

ErrorResolution`invalid_statement_descriptor_length`A statement descriptor must be at least 5 characters.`invalid_statement_descriptor_business_mismatch`A statement descriptor must be similar to the business name, legal entity name, or URL of the account.invalid_statement_descriptor_denylisted

invalid_statement_descriptor_prefix_denylisted

Generic or well-known statement descriptors aren’t supported.

`invalid_statement_descriptor_prefix_mismatch`The statement descriptor prefix must be similar to your statement descriptor, business name, legal entity name, or URL.## Person information

During the verification process, information about the persons associated with an account needs to be collected. If you onboard:

- Only companies, use the[Persons](/api/persons)API to collect this information.
- Only individuals, you can use the[Persons](/api/persons)API or the[individual](/api/accounts/object#account_object-individual)hash on the Account object.
- A combination of individuals and companies, use the[Persons](/api/persons)API to collect this information. This way you collect information in the same manner regardless of business type.

To retrieve the status of verification information regarding a person, utilize the Person object’s verification subhash:

`{
  "id": "{{PERSON_ID}}",
  "object": "person",
  ...
  "verification": {
    "document": null
  }
  ...
}`You can look up the definition for each verification attribute on the Person object. The two attributes worth noting are status and details.

status indicates the state of verification for the person:

- `pending`: Stripe is currently trying to verify this entity.
- `unverified`: Stripe isn’t able to verify this entity right now, either because verification has failed or because we don’t have enough information to attempt verification.
- `verified`: Stripe has successfully verified this entity.

Note that an unverified status isn’t necessarily an urgent issue, but it does mean that Stripe might request more information soon.

The details attribute provides an explanation for the current status.

Below is a list of errors related to person verification:

ErrorResolution`invalid_address_city_state_postal_code`Stripe couldn’t validate the combination of the city, state, and postal code in the provided address.`invalid_address_highway_contract_box`The address of the person must be a valid physical address from which the account conducts business and can’t be a Highway Contract Box.`invalid_address_private_mailbox`The address of the person must be a valid physical address from which the account conducts business and can’t be a private mailbox.`invalid_dob_age_under_minimum`The person must be at least 13 years old.`invalid_dob_age_over_maximum`The person’s date of birth must be within the past 120 years.`invalid_phone_number`Stripe couldn’t validate the phone number on the account. Make sure the formatting matches the country of the person.`invalid_street_address`Stripe couldn’t validate the street name and/or number for the provided address.invalid_tax_id

invalid_tax_id_format

Tax IDs must be a unique set of 9 numbers without dashes or other special characters.

## Acceptable verification documents by country

Below is a listing of documents that Stripe can accept as proof of identity, address, and entity for each country Stripe supports.

Some forms of documentation require scans of both the front and back of the document. For these, use the document_back parameter to provide the back of the document. Unless explicitly noted, only a scan of the front of the document is required.

Country:AlbaniaAlgeriaAngolaAntigua & BarbudaArgentinaArmeniaAustraliaAustriaAzerbaijanBahamasBahrainBangladeshBelgiumBeninBhutanBoliviaBosnia & HerzegovinaBotswanaBrazilBruneiBulgariaCambodiaCanadaChileColombiaCôte d’IvoireCroatiaCyprusCzech RepublicDenmarkDominican RepublicEcuadorEgyptEl SalvadorEstoniaEthiopiaFinlandFranceGabonGambiaGermanyGhanaGibraltarGreeceGuatemalaGuyanaHong KongHungaryIndiaIcelandIndonesiaIrelandIsraelItalyJapanJamaicaJordanKazakhstanKenyaKuwaitLaosLatviaLiechtensteinLithuaniaLuxembourgMacao SAR ChinaMadagascarMalaysiaMaltaMauritiusMexicoMoldovaMonacoMongoliaMoroccoMozambiqueNamibiaNigerNigeriaNetherlandsNew ZealandNorth MacedoniaNorwayOmanPakistanPanamaParaguayPeruPhilippinesPolandPortugalQatarRomaniaRwandaSt. LuciaSan MarinoSaudi ArabiaSenegalSerbiaSingaporeSlovakiaSloveniaSouth AfricaSouth KoreaSpainSri LankaSwedenSwitzerlandTaiwanTanzaniaThailandTrinidad & TobagoTunisiaTurkeyUnited Arab EmiratesUnited KingdomUnited StatesUruguayUzbekistanVietnamIdentity DocumentsCompany/Entity DocumentsAcceptable identity documents vary by country, however, a passport scan for identity verification is always acceptable and is preferred.Acceptable forms of identification:

- Letërnjoftimi (National Identity Card)
- Passport
- Leje Drejtimi (Driving License)

## Company information

During the verification process, you might need to collect information about the company for an account.

To retrieve the status of verification information regarding an account’s company, use the Account’s company.verification subhash:

`{
  "id": "{{CONNECTED_ACCOUNT_ID}}",
  "object": "account",
  ...
  "company": {
    "verification": {
      "document": null
    },
    ...
  },
  ...
}`You can look up the definition for each verification attribute on the Account object.

## Handle document verification problems

Many complications with the verification process involve the uploaded document itself. To help you recognize and handle the most common problems, the table below lists possible values for the error code (in the requirements.errors array) and the likely resolutions for each error.

Below is a list of errors related to document upload:

ErrorResolutionverification_document_corrupt

verification_document_failed_copy

verification_document_failed_greyscale

verification_document_incomplete

verification_document_not_readable

verification_document_not_uploaded

verification_document_not_signed

verification_document_missing_back

verification_document_missing_front

verification_document_too_large

The upload failed due to a problem with the file itself. Ask your user to provide a new file that meets these requirements:

- Color image (8,000 pixels by 8,000 pixels or smaller)
- 10 MB or less
- Identity documents are JPG or PNG format
- Address or legal entity documents are JPG, PNG, or PDF format
- Legal entity documents must include all pages
- Must not be password protected

verification_document_country_not_supported

verification_document_invalid

verification_document_type_not_supported

The provided file isn’t an acceptable form of ID from a supported country, or isn’t a type of legal entity document that is expected. Ask your user to provide a new file that meets that requirement. For a list, see Acceptable ID types by country.

verification_failed_other

verification_document_failed_other

Your team can contact Stripe to learn more about why identity verification failed.

verification_document_expired

verification_document_issue_or_expiry_date_missing

The issue or expiry date is missing on the document, or the document is expired. If it’s an identity document, its expiration date must be after the date the document was submitted. If it’s an address document, the issue date must be within the last six months.

Below is a list of errors related to identity verification:

ErrorResolution`verification_failed_keyed_identity`The name on the account couldn’t be verified. Ask your user to verify that they have provided their full legal name and to also provide a photo ID matching that name.verification_document_name_mismatch

verification_document_dob_mismatch

verification_document_address_mismatch

verification_document_id_number_mismatch

verification_document_photo_mismatch

The information on the ID document doesn’t match the information provided by the user. Ask your user to verify and correct the provided information on the account.

verification_document_fraudulent

verification_document_manipulated

The document might have been altered so it couldn’t be verified. Your team can contact Stripe to learn more.

Below is a list of errors related to business verification:

ErrorResolutionverification_failed_keyed_match

verification_failed_document_match

The information on the account couldn’t be verified. Your user can either upload a document to confirm their account details, or update their information on their account.

verification_failed_tax_id_not_issued

verification_failed_tax_id_match

The information that your user provided couldn’t be verified with the IRS. Ask your user to correct any possible errors in the company name or tax ID, or upload a document that contains those fields. (US only)

verification_failed_id_number_match

verification_failed_name_match

verification_failed_address_match

The information on the document doesn’t match the information provided by the user. Ask your user to verify and correct the provided information on the account, or upload a document with information that matches the account.

verification_document_address_missing

verification_document_id_number_missing

verification_document_name_missing

The uploaded document is missing a required field. Ask your user to upload another document that contains the missing field.

CautionDon’t resubmit a file that previously failed. Duplicate uploads immediately trigger an error and aren’t rechecked.

## Handle URL verification errors

URLs for e-commerce businesses need to conform to certain card network standards. See the website checklist for best practices for URLs and common elements for e-commerce businesses. Stripe conducts a number of verifications for URL integrity. There are two methods to resolve URL integrity errors:

- Using the API- Use the error code to handle the URL issue. If you need to update the URL, use the[Update Account](/api/accounts/update)API, which also causes Stripe to verify the updated URL. If you don’t have to update the URL, Stripe still needs to clear the error by verifying the URL again. After you make any other required updates, trigger reverification by using the API to change the URL to any other value and then change it back.
- Using the Dashboard- Platforms can use the[Accounts to review](/connect/dashboard/review-actionable-accounts)page in the Stripe Dashboard to understand the impact to their connected accounts and what actions to take.

Not all URL-related issues can be resolved using the API. Certain types of URL integrity errors require additional information on how to access the connected account’s webpage or to attest that the account is exempt from URL requirements. These types of issues require that you or your connected account provide supplemental information. Visit your Accounts to review page to resolve the error, or direct your connected account to contact Stripe Support.

NoteStripe’s Terms of Service requires all e-commerce businesses to populate the business_profile.url property with a working URL of their business website when activating an account with the card_payments capability. An account is considered an e-commerce business if it promotes or sells any products or services through an online website, social media profile, or mobile application. If the account doesn’t operate a website to promote their business, sell products, or accept payments, they’re required to provide business_profile.product_description instead. A product description needs to detail the type of products being sold as well as the manner in which the account’s customers are being charged (i.e. in person transactions).

To help you handle the most common errors associated with the business_profile.url field, the following table lists the related error codes (in the requirements.errors array) and possible resolutions.

ErrorResolution`invalid_url_denylisted`The URL provided for the account matches a generic business website URL. A URL that is specific to the business of the account must be provided.`invalid_url_format`The URL provided for the account is in the incorrect format. A URL in a correct format must be provided, such as`https://example.com`.`invalid_url_website_inaccessible`We can’t reach the website at the URL provided for the account. To resolve this issue, update the account with a reachable URL. If the problem persists, go to your[Accounts to review Dashboard page](/connect/dashboard/review-actionable-accounts)and respond to the intervention in theActions requiredlist or contact Stripe support.`invalid_url_website_business_information_mismatch`Information on the account’s website does not match information on the account’s Stripe account. Please view your Accounts to review page in the Dashboard or the account must make sure that the information on the website matches the account’s business.`invalid_url_website_incomplete`The account’s website seems to be missing some required information. Learn more about[the information a website must include](https://support.stripe.com/questions/information-required-on-your-business-website-to-use-stripe).`invalid_url_website_other`We’re unable to verify the account’s business using the URL of the website, social media profile, or mobile application provided. A new URL must be provided. View your Accounts to review page or the account must contact Stripe support if no URL exists.`invalid_url_web_presence_detected`We have detected that the account uses a website, social media profile, or mobile application to sell or promote products or services, but a URL hasn’t been provided for the account. The account should have a URL that isn’t a generic URL for the website or social media provider.`invalid_url_website_incomplete_customer_service_details`The account’s website doesn’t contain customer service details, which are required for the business type of the account. Please view your Accounts to review page in the Dashboard or the account must add these details to its website.`invalid_url_website_incomplete_return_policy`The account’s website doesn’t contain a return policy and process, which are required for the business type of the account. Please view your Accounts to review page in the Dashboard or the account must add a return policy and process to its website.`invalid_url_website_incomplete_refund_policy`The account’s website doesn’t contain a refund policy, which is required for the business type of the account. Please view your Accounts to review page in the Dashboard or the account must add a refund policy to its website.`invalid_url_website_incomplete_cancellation_policy`The account’s website doesn’t contain a cancellation policy, which is required for the business type of the account. Please view your Accounts to review page in the Dashboard or the account must add a cancellation policy to its website.`invalid_url_website_incomplete_legal_restrictions`The account’s website suggests that it’s selling goods that have either legal or export restrictions. View your Accounts to review page or the account must remove those goods from its website.`invalid_url_website_incomplete_terms_and_conditions`The account’s website doesn’t contain terms and conditions, which are required for the business type of the account. Please view your Accounts to review page in the Dashboard or the account must add terms and conditions to its website.`invalid_url_website_incomplete_under_construction`The account’s website is under construction. Please view your Accounts to review page in the Dashboard or the account must complete construction of its website.`invalid_url_website_inaccessible_password_protected`The account’s website is password-protected. Please view your Accounts to review page in the Dashboard or the account must contact Stripe Support with instructions to access the website.`invalid_url_website_inaccessible_geoblocked`Stripe couldn’t access the account’s website because it is geoblocked. Please view your Accounts to review page in the Dashboard or the account must contact Stripe Support with instructions to access the website.`invalid_url_website_empty`The account’s website doesn’t have any content. Please view your Accounts to review page in the Dashboard or the account must add content that represents its products and services.## Handle identity verification

You can respond in two ways to an identity verification change. The first is to perform an Update Account call, correcting or adding information.

Secondarily, we might ask you to upload a document. Depending on how much of the user’s information Stripe has been able to verify, we might require three different types of document uploads. You can determine what documents to upload based on the fields listed in requirements.currently_due:

- `person.verification.document`: Requires a color scan or photo of an acceptable form of ID.
- `person.verification.additional_document`: Requires a color scan or photo of a document verifying the user’s address, such as a utility bill.
- `company.verification.document`: Requires a proof of entity document establishing the business’ entity ID number, such as the company’s articles of incorporation.

Uploading a document is a two-step process:

1. Upload the file to Stripe
2. Attach the file to the account

NoteFor security reasons, Stripe doesn’t accept copies of IDs sent by email.

### Upload a file

To upload a file, use the Create File API by using a POST to send the file data as part of a multipart/form-data request.

The uploaded file must meet these requirements:

- Color image (8,000 pixels by 8,000 pixels or smaller)
- 10 MB or less
- Identity documents are JPG or PNG format
- Address or legal entity documents are JPG, PNG, or PDF format

Pass the file data in the file parameter and set the purpose parameter to identity_document:

Command Line[curl](#)`curl https://files.stripe.com/v1/files \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -H "Stripe-Account: {{CONNECTED_STRIPE_ACCOUNT_ID}}" \
  -F "purpose"="identity_document" \
  -F "file"="@/path/to/a/file"`This request uploads the file and returns a token:

`{
  "id": "{{FILE_ID}}",
  "created": 1403047735,
  "size": 4908
}`You may then use the token’s id value to attach the file to a connected account for identity verification.

### Attach the file

After you upload the file and receive a representative token, provide the file ID using the appropriate field in your Update Account call.

Below is an example for an ID document:

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/persons/{{PERSON_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "verification[document][front]"={{FILE_ID}}`Below is an example for a company document:

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "company[verification][document][front]"={{FILE_ID}}`This update changes verification.status to pending. If an additional person needs to be verified, use the Persons API to update them.

### Confirm ID verification

If the color scan or photo of the ID passes Stripe’s checks, the document requirement is removed from requirements.currently_due. Satisfying all verification requirements for the person or company triggers an account.updated webhook notification signaling the verification process is complete.

Verification can take Stripe from a few minutes, to a couple business days to complete, depending on how readable the provided image is.

If the verification attempt fails, the requirements.errors array contains an error stating the cause. The error[reason], such as “The image supplied isn’t readable,” is safe to present to your user, but isn’t localized. The response also contains an error[code] value, such as verification_document_not_readable, which you can use to localize errors for your users. Upon failure, requirements.currently_due indicates that a new ID upload is required. If the deadline for verification is near, requirements.current_deadline might also be populated with a date. Verification failure also triggers an account.updated webhook notification.

Interested in receiving risk-related requirements?As part of a current beta, you can handle current and upcoming risk-related account issues with the requirements attribute. To participate, submit your email.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.## See also

- [Updating Accounts](/connect/updating-service-agreements)
- [File Upload Guide](/file-upload)
- [Identity Verification for Custom Accounts](/connect/identity-verification)
- [Account Tokens](/connect/account-tokens)
- [Testing Connect](/connect/testing)
- [Testing Custom Account Identity Verification](/connect/testing-verification)
- [Required Verification Information](/connect/required-verification-information)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Verification process](#verification-process)[Determine if verification is needed](#determine-if-verification-is-needed)[Validation and verification errors](#validation-and-verification-errors)[Business information](#business-information)[Statement descriptors](#statement-descriptors)[Person information](#person-information)[Acceptable verification documents by country](#acceptable-verification-documents)[Company information](#company-information)[Handle document verification problems](#handle-document-verification-problems)[Handle URL verification errors](#url-verification)[Handle identity verification](#handle-identity-verification)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`