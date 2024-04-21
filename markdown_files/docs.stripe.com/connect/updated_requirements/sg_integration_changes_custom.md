htmlRequired verification information in Singapore | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fupdated_requirements%2Fsg_integration_changes_custom)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fupdated_requirements%2Fsg_integration_changes_custom)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# Required verification information in Singapore

Learn about how to comply with the Payment Services Act (2019).Last updated: Nov 21, 2021

To comply with the Payment Services Act, we’ve made some changes to the onboarding form for new Singapore connected accounts. These changes require additional identification and verification details for certain users. We’re introducing these changes to existing accounts gradually. We require Custom Connect platforms to incorporate these changes within their onboarding forms. For Standard and Express platforms, we’ll incorporate these changes to our onboarding forms and roll the changes out to your connected accounts.

The following list contains additional identification and verification information that we require for each business type.

In addition, we now require additional verification for some connected accounts. These are connected accounts onboarding as individuals, or accounts used for the following activities: financial services, receiving donations, or rewards-based crowdfunding. We classify users who require these additional identification steps as Customer Due Diligence (CDD) users, and those who don’t require these steps as Basic Due Diligence (BDD) Users.

You can find the full list of required identification and verification information for onboarding Singapore Stripe accounts on our required verification information page.

## Corporations and private limited companies

InformationAPI parameterChange in requirement (BDD users)Change in requirement (CDD users)Account informationMerchant category code`business_profile.mcc`New requirementNew requirementWebsite or product description

business_profile.url

business_profile.product_description

New requirement

New requirement

Usage surveyUsage surveyThe usage survey is only shown when you use Connect Onboarding. It determines whether to categorize the user as BDD or CDD. If you don’t need to show the survey to the user, update your Connect[regional settings](https://dashboard.stripe.com/settings/connect/regional)CompanyPhone number`company.phone`New requirementNew requirementAccount opener detailsAlternate names / aliases`representative.full_name_aliases`New requirementNew requirementEmail address`representative.email`New requirementNew requirementPhone number`representative.phone`New requirementNew requirementNationality`representative.nationality`New requirementNew requirementJob title`representative.relationship.title`New requirementNew requirementEnhanced identity verification`representative.verification.proof_of_liveness`New requirement. Collect this information using Connect OnboardingOwnerBeneficial owner details`owner.*`Previously required, no longer requiredRequiredAlternate names / aliases`owner.full_name_aliases`New requirementEmail address`owner.email`New requirementJob title`owner.relationship.title`New requirementDirectorBusiness director details

director.*

New requirement

See required verification information

## Charities, non-profits, clubs, societies, or other unincorporated entities

InformationAPI parameterChange in requirement (BDD users)Change in requirement (CDD users)Account informationMerchant category code`business_profile.mcc`New requirementNew requirementWebsite or product description

business_profile.url

business_profile.product_description

New requirement

New requirement

EntityTax ID (UEN)`company.tax_id`New requirementNew requirementPhone number`company.phone`New requirementNew requirementUsage surveyUsage surveyThe usage survey is only shown when you use Connect Onboarding. It determines whether to categorize the user as BDD or CDD. If you don’t need to show the survey to the user, update your Connect[regional settings](https://dashboard.stripe.com/settings/connect/regional)Account opener detailsAlternate names / aliases`representative.full_name_aliases`New requirementNew requirementEmail address`representative.email`New requirementNew requirementPhone number`representative.phone`New requirementNew requirementNationality`representative.nationality`New requirementNew requirementJob title`representative.relationship.title`New requirementNew requirementEnhanced identity verification`representative.verification.proof_of_liveness`New requirement. Collect this information using Connect Onboarding## Individuals

InformationAPI parameterChange in requirementAccount informationMerchant category code`business_profile.mcc`New requirementWebsite or product description

business_profile.url

business_profile.product_description

New requirement

Account opener detailsAlternate names / aliases`representative.full_name_aliases`New requirementPersonal ID number (NRIC / passport)`representative.id_number`Only Singapore-issued IDs acceptedEmail address`representative.email`New requirementPhone number`representative.phone`New requirementNationality`representative.nationality`New requirementEnhanced identity verification`representative.verification.proof_of_liveness`New requirement. Collect this information using Connect Onboarding## Partnerships and sole proprietors

We now support creating custom connect accounts for partnerships and sole proprietors as new entity types. Refer to the requirements for partnerships and sole proprietors.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Corporations and private limited companies](#corporations-and-private-limited-companies)[Charities, non-profits, clubs, societies, or other unincorporated entities](#charities,-non-profits,-clubs,-societies,-or-other-unincorporated-entities)[Individuals](#individuals)[Partnerships and sole proprietors](#partnerships-and-sole-proprietors)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`