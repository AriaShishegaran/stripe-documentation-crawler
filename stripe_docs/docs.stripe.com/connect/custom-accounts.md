# Using Connect with Custom accounts

Identity verification requirements are updated as laws and regulations change around the world. If you’re building your own onboarding flow to onboard accounts, you must plan on reviewing and updating onboarding requirements at least every six months. To avoid this maintenance obligation, use Connect Onboarding for Custom Accounts.

[Connect Onboarding for Custom Accounts](/connect/custom/hosted-onboarding)

A Custom Stripe account is almost completely invisible to the account holder. You, the platform, are responsible for all interactions with your users and for collecting all the information needed to verify the account.

With Custom accounts you can modify the connected account’s details and settings through the API, including managing their bank accounts and payout schedule. Since Custom account holders can’t log into Stripe, it’s up to you to build the onboarding flow, user dashboard, reporting functionality, and communication channels.

[payout](/payouts)

Although a simple API call creates a Custom account, there are three steps to consider for each account you create:

- Properly identify the country to use.

[country](#country)

- Create the account.

[Create](#create)

- Move onto the identity verification process.

[identity verification](#identity-verification)

But first, ensure you meet the minimum requirements.

[minimum requirements](#requirements)

French platforms must use account tokens, which are an alternative to the agent model for platform PSD2 compliance. The key benefit of tokens for French platforms is that information is transferred from the user directly to Stripe. Not having to store PII data is still a benefit, but not necessarily a requirement. For platforms in other countries, account tokens are optional but recommended.

[PSD2](https://stripe.com/connect/eu-guide)

## Requirements for creating Custom accounts

To use Custom accounts, you must meet all of these requirements:

- Minimum API version: You must be using an API version at least as recent as 2014-12-17. You can view and upgrade your API version in the Dashboard if needed.

[view and upgrade](https://dashboard.stripe.com/developers)

- Terms of Service update: Creating Custom accounts requires an update to your terms of service, as it must include a reference to Stripe’s services agreement. Stripe recommends that you consult with your attorneys on whether you should update your terms acceptance language to include reference to Stripe’s terms.

[update to your terms of service](/connect/updating-service-agreements#tos-acceptance)

- Handling information requests: Instead of requesting information—such as a Social Security Number or passport scan—directly from your user, Stripe requests the information it needs from you. You must collect this information from your user and provide it to Stripe. Otherwise, Stripe may disable payouts to the connected account.

- Platform in a supported country: Platforms in Australia, Austria, Belgium, Brazil, Bulgaria, Canada, Cyprus, the Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hong Kong, Hungary, India, Ireland, Italy, Japan, Latvia, Lithuania, Luxembourg, Malta, Mexico, the Netherlands, New Zealand, Norway, Poland, Portugal, Romania, Singapore, Slovakia, Slovenia, Spain, Sweden, Switzerland, Thailand, the United Kingdom, and the United States can create Custom accounts for any country Stripe supports. Contact us to be notified when platforms in your country can use Custom accounts.

[Stripe supports](https://stripe.com/global)

[Contact us](mailto:connect@stripe.com)

- Countries that don’t support self-serve: Due to restrictions that apply when using Connect in the United Arab Emirates, India, and Thailand, platform users in these countries can’t self-serve Custom Connect accounts. To begin onboarding for Custom Connect Accounts in these countries, contact us.

[United Arab Emirates](https://support.stripe.com/questions/connect-availability-in-the-uae)

[India](https://support.stripe.com/questions/stripe-india-support-for-marketplaces)

[Thailand](https://support.stripe.com/questions/stripe-thailand-support-for-marketplace)

[contact us](https://stripe.com/contact/sales)

- Platforms in the UAE: Platforms in the UAE can only use Custom accounts based in the UAE with the following charge types: destination_charges and separate charges and transfers. Destination charges using the on_behalf_of attribute are not yet supported for UAE platforms.

[destination_charges](/connect/destination-charges)

[separate charges and transfers](/connect/separate-charges-and-transfers)

[on_behalf_of](/api/payment_intents/object#payment_intent_object-on_behalf_of)

Platforms outside of Mexico that want to create Custom accounts in Mexico and make them settlement merchants require further review. Contact us to start the process.

[settlement merchants](/connect/account-capabilities#card-payments)

[Contact us](https://support.stripe.com/contact)

- Vetting for fraud: Because your platform is responsible for losses incurred by Custom accounts, you must scrutinize all accounts that sign up via your platform for potential fraud. Refer to our risk management best practices guide for more information.

[risk management best practices guide](/connect/risk-management/best-practices)

Note there’s an additional cost for active Custom accounts. A Custom account is considered active if it has received at least one successful payout in a given month.

[additional cost](https://stripe.com/connect/pricing)

[Identify the country to use](#country)

## Identify the country to use

The only piece of information you need to create a Custom account is the country the individual or business will primarily operate in. Everything else can be collected and updated at a later time.

For example, if you are in the United States and the business or user you’re creating an account for is legally represented in Canada, use CA as the country for the account being created.

The country value also determines the required verification information for the connected account.

[required verification information](/connect/required-verification-information)

[Create a Custom account](#create)

## Create a Custom account

At the bare minimum, to create and connect a Custom account, set type to custom in the account creation request and provide a country and the appropriate capabilities.

[appropriate capabilities](/connect/account-capabilities#supported-capabilities)

US platforms can create accounts for cross-border transfers by specifying the recipient service agreement.

[cross-border transfers](/connect/account-capabilities#transfers-cross-border)

[specifying the recipient service agreement](/connect/service-agreement-types#choosing-type-with-api)

The result of a successful API call is the user’s account information:

Store the id in your database—it’s the account ID. You’ll provide this value to authenticate as the connected account by passing it into requests in the Stripe-Account header.

[authenticate](/connect/authentication)

Store the received account ID. You need this information to perform requests on the user’s behalf.

[Start the identity verification process](#identity-verification)

## Start the identity verification process

An account created with only a country is fairly limited: it can only receive a small amount of funds. If you wish to enable payouts and keep the account in good standing, you need to provide more information about the account holder. The required verification information page lists the minimum and likely identity verification requirements.

[provide more information](/connect/identity-verification)

[required verification information](/connect/required-verification-information)

The easiest way to collect this information is to integrate Connect Onboarding, which lets Stripe take care of the verification complexity. Otherwise, you must not only write your own API calls for initial integration, but also continue to check for changing onboarding requirements because of changing regulations around the world.

[Connect Onboarding](/connect/custom/hosted-onboarding)

You can collect required information when you create the account or by updating the account later. At the very least, we recommend collecting and providing the user’s name and date of birth upfront. If you collect address information upfront, make sure to validate the state value for US, CA, and AU connected accounts in your onboarding flow.

[create the account](/api#create_account)

[updating the account](/api#update_account)

[address information](https://support.stripe.com/questions/connect-address-validation)

For accounts with business_type set to individual, provide at least one individual property (for example, individual.first_name) and a Person object is created automatically. If you don’t, or for accounts with the business_type set to company, you need to create each Person for the account.

[business_type](/api/accounts/object#account_object-business_type)

[Person](/api/persons/object)

[create each Person](/api/persons/create)

## Webhooks

After an account is created, all notifications about changes to the account are sent to your webhooks as account.updated events. Provide your Connect webhook URL in your account settings and then watch for these events and respond to them as needed.

[webhooks](/connect/webhooks)

[Connect](/connect)

[webhook](/webhooks)

[account settings](https://dashboard.stripe.com/account/webhooks)

## See also

Learn more about working with Custom accounts.

- Onboarding Accounts

[Onboarding Accounts](/connect/custom/onboarding)

- Updating Accounts

[Updating Accounts](/connect/updating-service-agreements)

- Identity Verification

[Identity Verification](/connect/identity-verification)

- Authentication

[Authentication](/connect/authentication)

- Creating Charges

[Creating Charges](/connect/charges)

- Full API reference

[Full API reference](/api)
