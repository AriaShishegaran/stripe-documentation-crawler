# Account onboarding

The Account onboarding component uses the Accounts API to read requirements and generate an onboarding form that’s localized for all Stripe-supported countries and that validates data. In addition, Embedded onboarding handles all business types, various configurations of company representatives, document uploads, identity verification, and verification statuses.

[Accounts API](/api/accounts)

## Requirements collection options

With embedded onboarding, you can control the collection of currently_due or eventually_due requirements, along with the inclusion of future requirements. You can customize this behavior by using the collectionOptions attribute when integrating the account onboarding component.

[future requirements](/connect/custom/handle-verification-updates)

Use the external_account_collection feature to control whether the account onboarding component collects external account information. This parameter is enabled by default and can only be set to false for custom accounts. Note that when this option is enabled for custom accounts, user authentication will be required for certain embedded components like account onboarding.

[external_account_collection](/api/account_sessions/create#create_account_session-components-account_onboarding-features-external_account_collection)

[user authentication](/connect/get-started-connect-embedded-components#user-authentication-in-connect-embedded-components)

## Customize policies shown to your users

Stripe’s service agreement and Privacy Policy are surfaced to users in embedded onboarding. Users who have not accepted Stripe’s services agreement are asked to accept it on the final screen of onboarding. Embedded onboarding also has a footer with links to Stripe’s service agreement and Privacy Policy.

[Privacy Policy](https://stripe.com/privacy)

[accepted Stripe’s services agreement](/connect/service-agreement-types#accepting-the-correct-agreement)

[Privacy Policy](https://stripe.com/privacy)

For Custom accounts, you have additional options to customize the experience, outlined below.

[Custom](/connect/custom-accounts)

If you’re a platform onboarding Custom accounts, you can collect Terms of Service acceptance using your own process instead of in our embedded account onboarding component. In that case, the final onboarding screen only asks your users to confirm the information they entered, and you must secure their acceptance of Stripe’s service agreement.

[Custom](/connect/custom-accounts)

[collect Terms of Service acceptance](/connect/updating-service-agreements#tos-acceptance)

Embedded onboarding still has links to the terms of service (for example, in the footer) that you can choose to replace by surfacing your own policies.

[surfacing your own policies](#surfacing-links-to-your-agreements-and-privacy-policy-in-embedded-onboarding)

Users see the Stripe service agreement and Privacy Policy throughout embedded onboarding. For your Custom accounts, you can replace those links with your own agreements and policy. To do so, follow these instructions to incorporate the Stripe services agreement and link to the Stripe Privacy Policy.

[Privacy Policy](https://stripe.com/privacy)

[Custom](/connect/custom-accounts)

[incorporate the Stripe services agreement](/connect/updating-service-agreements#adding-stripes-service-agreement-to-your-terms-of-service)

[link to the Stripe Privacy Policy](/connect/updating-service-agreements#disclosing-how-stripe-processes-user-data)

## Creating an Account Session

When creating an Account Session, enable account management by specifying account_onboarding in the components parameter.

[creating an Account Session](/api/account_sessions/create)

After creating the Account Session and initializing ConnectJS, you can render the Account onboarding component in the front end:

[initializing ConnectJS](/connect/get-started-connect-embedded-components#account-sessions)

[full terms of service](/connect/service-agreement-types#full)

[Stripe’s full service agreement](https://stripe.com/connect-account/legal/full)

[recipient terms of service](/connect/service-agreement-types#recipient)

[Stripe’s recipient service agreement](https://stripe.com/connect-account/legal/recipient)

[Stripe’s privacy policy](https://stripe.com/privacy)

[collect terms acceptance yourself](/connect/updating-service-agreements#indicating-acceptance)

[future requirements](/api/accounts/object#account_object-future_requirements)

To use this component to set up new accounts:

- Create a connected account. You can prefill information on the account object in this API call.

[connected account](/api/accounts)

- Initialize Connect embedded components using the ID of the connected account.

[Initialize Connect embedded components](/connect/get-started-connect-embedded-components#account-sessions)

- Include the account-onboarding element to show the onboarding flow to the connected account.

- Listen for the exit event emitted from this component. Stripe sends this event when the connected account exits the onboarding process.
