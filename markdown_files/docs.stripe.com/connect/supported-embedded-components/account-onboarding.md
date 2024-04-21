htmlAccount onboarding | Stripe Documentation[Skip to content](#main-content)Account onboarding[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Faccount-onboarding)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Faccount-onboarding)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Supported Connect embedded components](/docs/connect/supported-embedded-components)# Account onboarding

Show a localized onboarding form that validates data.The Account onboarding component uses the Accounts API to read requirements and generate an onboarding form that’s localized for all Stripe-supported countries and that validates data. In addition, Embedded onboarding handles all business types, various configurations of company representatives, document uploads, identity verification, and verification statuses.

## Requirements collection options

With embedded onboarding, you can control the collection of currently_due or eventually_due requirements, along with the inclusion of future requirements. You can customize this behavior by using the collectionOptions attribute when integrating the account onboarding component.

### External account collection

Use the external_account_collection feature to control whether the account onboarding component collects external account information. This parameter is enabled by default and can only be set to false for custom accounts. Note that when this option is enabled for custom accounts, user authentication will be required for certain embedded components like account onboarding.

## Customize policies shown to your users

Stripe’s service agreement and Privacy Policy are surfaced to users in embedded onboarding. Users who have not accepted Stripe’s services agreement are asked to accept it on the final screen of onboarding. Embedded onboarding also has a footer with links to Stripe’s service agreement and Privacy Policy.

For Custom accounts, you have additional options to customize the experience, outlined below.

### Handle service agreement acceptance on your own

If you’re a platform onboarding Custom accounts, you can collect Terms of Service acceptance using your own process instead of in our embedded account onboarding component. In that case, the final onboarding screen only asks your users to confirm the information they entered, and you must secure their acceptance of Stripe’s service agreement.

Embedded onboarding still has links to the terms of service (for example, in the footer) that you can choose to replace by surfacing your own policies.

### Surfacing links to your agreements and privacy policy in embedded onboarding

Users see the Stripe service agreement and Privacy Policy throughout embedded onboarding. For your Custom accounts, you can replace those links with your own agreements and policy. To do so, follow these instructions to incorporate the Stripe services agreement and link to the Stripe Privacy Policy.

## Creating an Account Session

When creating an Account Session, enable account management by specifying account_onboarding in the components parameter.

Command Line[curl](#)`curl https://api.stripe.com/v1/account_sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d account={{CONNECTED_ACCOUNT_ID}} \
  -d "components[account_onboarding][enabled]"=true \
  -d "components[account_onboarding][features][external_account_collection]"=true`After creating the Account Session and initializing ConnectJS, you can render the Account onboarding component in the front end:

account-onboarding.js[JavaScript](#)`// Include this element in your HTML
const accountOnboarding = stripeConnectInstance.create('account-onboarding');
accountOnboarding.setOnExit(() => {
  console.log('User exited the onboarding flow');
});
container.appendChild(accountOnboarding);

// Optional: make sure to follow our policy instructions above
// accountOnboarding.setFullTermsOfServiceUrl('{{URL}}')
// accountOnboarding.setRecipientTermsOfServiceUrl('{{URL}}')
// accountOnboarding.setPrivacyPolicyUrl('{{URL}}')
// accountOnboarding.setSkipTermsOfServiceCollection(false)
// accountOnboarding.setCollectionOptions({
//   fields: 'eventually_due',
//   futureRequirements: 'include',
// })`HTML + JSReactMethodTypeDescriptionDefault`setFullTermsOfServiceUrl``string`Absolute URL to your[full terms of service](/connect/service-agreement-types#full)agreement.[Stripe’s full service agreement](https://stripe.com/connect-account/legal/full)`setRecipientTermsOfServiceUrl``string`Absolute URL to your[recipient terms of service](/connect/service-agreement-types#recipient)agreement.[Stripe’s recipient service agreement](https://stripe.com/connect-account/legal/recipient)`setPrivacyPolicyUrl``string`Absolute URL to your privacy policy.[Stripe’s privacy policy](https://stripe.com/privacy)`setSkipTermsOfServiceCollection``string`If true, embedded onboarding skips terms of service collection and you must[collect terms acceptance yourself](/connect/updating-service-agreements#indicating-acceptance).false`setCollectionOptions``{ fields: 'currently_due' | 'eventually_due', future_requirements: 'omit' | 'include' }`Customizes collecting`currently_due`or`eventually_due`requirements and controls whether to include[future requirements](/api/accounts/object#account_object-future_requirements). Specifying`eventually_due`collects both`eventually_due`and`currently_due`requirements.`{fields: 'currently_due', futureRequirements: 'omit'}``setOnExit``() => void`The connected account has exited the onboarding processTo use this component to set up new accounts:

1. Create a[connected account](/api/accounts). You can prefill information on the account object in this API call.
2. [Initialize Connect embedded components](/connect/get-started-connect-embedded-components#account-sessions)using the ID of the connected account.
3. Include the`account-onboarding`element to show the onboarding flow to the connected account.
4. Listen for the`exit`event emitted from this component. Stripe sends this event when the connected account exits the onboarding process.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Requirements collection options](#requirements-collection-options)[Customize policies shown to your users](#customize-policies-shown-to-your-users)[Creating an Account Session](#creating-an-account-session)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`