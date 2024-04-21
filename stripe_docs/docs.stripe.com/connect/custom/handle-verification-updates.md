# Handle verification updates

Before your connected accounts can accept payments and send payouts, you must fulfill what are typically called Know Your Customer (KYC) requirements. To do so, you must collect certain information about your connected accounts and send it to Stripe for verification.

[certain information about your connected accounts](/connect/required-verification-information)

Stripe frequently updates KYC requirements, often due to changes implemented by financial regulators, card networks, and other financial institutions.

As part of a current beta, you can handle current and upcoming risk-related account issues with the account.requirements attribute. To learn more about how to participate in the beta, submit your email.

[account.requirements](/api/accounts/object#account_object-requirements)

[submit your email.](#)

These updates might require you to take the following actions:

- Modify your onboarding flow to account for the changed requirements.

- Collect updated information from affected connected accounts and handle verification responses.

When upcoming requirements updates affect your connected accounts, we’ll notify you.

[upcoming requirements updates](https://support.stripe.com/user/questions/onboarding-requirements-updates)

If you use embedded or Stripe-hosted onboarding, you can proactively collect information to fulfill future requirements. For embedded onboarding, include the collectionOptions attribute in the embedded onboarding component. For Stripe-hosted onboarding, specify the collection_options parameter when creating account links.

[future requirements](/api/accounts/object#account_object-future_requirements)

[embedded onboarding component](/connect/supported-embedded-components/account-onboarding)

[creating account links](/api/account_links/create#create_account_link-collection_options)

In API version 2023-10-16 and later, the account object’s requirements.errors array specifies the latest verification error types in the code attribute. We recommend upgrading to API version 2023-10-16 and using requirements.errors.

[API version 2023-10-16](/upgrades#2023-10-16)

[requirements.errors](/api/accounts/object#account_object-requirements-errors)

If you can’t update to version 2023-10-16, earlier versions of the requirements.errors array include a detailed_code field to hold verification errors that weren’t compatible with the code attribute. The detailed_code attribute doesn’t appear in the API reference.

[Modify your onboarding flow](#modify-your-onboarding-flow)

## Modify your onboarding flow

When requirements change, we update Stripe-hosted and embedded onboarding flows to reflect the changes. However, if you use a custom API-based onboarding flow, you must update it to handle any changed requirements.

Regardless of the onboarding flow type, you must address requirements changes for your existing Custom accounts.

[API-based](/connect/custom/onboarding#api-based-onboarding)

[Embedded](/connect/custom/onboarding#embedded-onboarding)

[highly themeable](/connect/customize-connect-embedded-components)

[customizable](/connect/embedded-onboarding#customize-policies-shown-to-your-users)

[Stripe-hosted](/connect/custom/onboarding#stripe-hosted-onboarding)

If you use embedded components or Stripe-hosted onboarding, requirements changes don’t require you to update your onboarding flow. Skip to the section on collecting updated information.

[collecting updated information](#collect-updated-information-from-affected-users)

If you use a custom API-based onboarding flow, handle updated requirements by following these steps or by replacing your onboarding flow with embedded components or Stripe-hosted onboarding.

You can’t use the API to respond to Stripe risk reviews. You can enable your connected accounts to respond using embedded components, Stripe-hosted onboarding, or remediation links. You can also use the Dashboard to respond to risk reviews on behalf of your connected accounts.

When verification requirements change, you must collect updated information by a certain date. Otherwise, connected accounts won’t be able to use the capabilities you request (for example, card_payments). See details about the information you need to collect based on an account’s region, capabilities requested, and other factors.

[a certain date](https://support.stripe.com/user/questions/onboarding-requirements-updates)

[information you need to collect](/connect/required-verification-information)

You can avoid disruption of your connected accounts’ capabilities by planning the collection of updated information before the current_deadline. To preview information about upcoming requirements changes, look at the Account object’s future_requirements hash.

[future_requirements hash](/api/accounts/object#account_object-future_requirements)

If you use Stripe Data, you can retrieve the future_requirements hash using a Sigma query.

[Stripe Data](/stripe-data)

[a Sigma query](/stripe-data/query-connect-data#account-requirements)

When you’ve identified the updated information you need to collect, add corresponding fields to your onboarding flow and update your connected accounts using the Accounts API.

To avoid disruption to your connected accounts, have your onboarding flow address all requirements listed in the Account object’s future_requirements.currently_due list.

[future_requirements.currently_due](/api/accounts/object#account_object-future_requirements-currently_due)

You can also prepare for requirements that will apply when an account reaches their thresholds by considering the future_requirements.eventually_due list.

[future_requirements.eventually_due](/api/accounts/object#account_object-future_requirements-eventually_due)

To simulate future verification requirements, create a test account using the Accounts API with enforce_future_requirements in the email field. That populates the account’s requirements hash with all known future verification requirements.

To verify that your updated onboarding flow fulfills the account requirements, onboard the test account and check its requirements hash. If your flow covers all the requirements, the currently_due list is empty.

[currently_due](/api/accounts/object#account_object-requirements-currently_due)

Detect account status changes by listening to the account.updated event. After an account has gone through your onboarding flow, inspect the currently_due and pending_verification lists in the account’s requirements hash. When both are empty, and requirements.disabled_reason is null, you can enable functionality for the account. When payouts_enabled is true, the account can receive payouts. When charges_enabled is true, unlock payments for the account.

[Collect updated information from accounts with outstanding requirements](#collect-updated-information-from-affected-users)

## Collect updated information from accounts with outstanding requirements

You can collect updated information from your connected accounts using embedded components, Stripe-hosted onboarding, or the Stripe API. We recommend either integrating embedded components or directing your connected accounts to Stripe-hosted onboarding using Account Links.

[Stripe-hosted onboarding using Account Links](/connect/custom/hosted-onboarding)

In all cases, follow these steps:

When Stripe receives updated information about your connected accounts, it takes time to verify the associated account fields. Until we complete verification, assume that any related functionality remains disabled. To detect field verification updates, listen for account.updated events and inspect them for verification errors. If you don’t resolve an error before its deadline, it disables requested capabilities for affected accounts.

[account.updated](/api/events/types#event_types-account.updated)

[verification errors](/connect/handling-api-verification#validation-and-verification-errors)

A disabled capability’s requirements hash contains a disabled_reason that you can use to determine the action you must take. To investigate or to provide required information, use the Accounts to review tab in your Connect Dashboard.

[disabled_reason](/api/capabilities/object#capability_object-requirements-disabled_reason)

[Accounts to review tab](/connect/dashboard/review-actionable-accounts)

In your Connect Dashboard, select Accounts to review. It displays a list of connected accounts with current or future outstanding requirements. You can filter the list by account issue and status.

[Accounts to review](https://dashboard.stripe.com/connect/accounts_to_review)

You can also see what information each connected account must provide, and the deadline, in the account object’s future_requirements hash or by using a Sigma query.

[future_requirements](/api/accounts/object#account_object-future_requirements)

[Sigma query](/stripe-data/query-connect-data)

On the enforcement date for an account (future_requirements.current_deadline), the contents of the future_requirements hash move to the requirements hash and Stripe generates an account.updated event. Because this enforcement can cause more accounts to require review, use the enforcement date as a reminder to check the Accounts to review tab in your Connect Dashboard.

[account.updated](/api/events/types#event_types-account.updated)

[Accounts to review tab](/connect/dashboard/review-actionable-accounts)

We plan to introduce a feature that lets you start enforcing requirements before the deadline by applying updated verification requirements to connected accounts. It will let you proactively catch and resolve issues in your updated integration by applying requirements to connected accounts in batches.

If any account has currently_due requirements or verification errors, you must address them by the requirements current_deadline. At that deadline, the requirements in the requirements.currently_due array are added to the requirements.past_due array and any associated capabilities become disabled until you provide the information and resolve the errors.

[currently_due](/api/accounts/object#account_object-requirements-currently_due)

[verification errors](/api/accounts/object#account_object-requirements-errors)

[current_deadline](/api/accounts/object#account_object-requirements-current_deadline)

Future requirements can immediately affect an account’s capabilities when they become current requirements. Make sure to address all requirements before their deadlines, even if they’re still in future_requirements.

When your accounts have requirements that are currently_due, direct your accounts to address any issues according to your onboarding flow or with remediation links:

- API-based onboarding: Use your custom onboarding flow, optionally collecting future_requirements as well.

[custom onboarding flow](/connect/custom/onboarding#api-based-onboarding)

- Embedded onboarding: Render the embedded onboarding component for affected accounts.

[embedded onboarding component](/connect/custom/onboarding#embedded-onboarding)

- Stripe-hosted onboarding: Use the Account Links API to generate a single-use link to Stripe-hosted onboarding. Send your connected accounts to this link from your application.

[Account Links API](/api/account_links)

[Stripe-hosted onboarding](/connect/custom/onboarding#stripe-hosted-onboarding)

- Remediation links: Use the Dashboard to generate remediation links that your connected accounts can use to provide required information.

[remediation links](/connect/dashboard/remediation-links)

## See also

- Handling verification with the API

[Handling verification with the API](/connect/handling-api-verification)

- Required Verification Information

[Required Verification Information](/connect/required-verification-information)

- Testing Connect

[Testing Connect](/connect/testing)

- Testing Custom Account Identity Verification

[Testing Custom Account Identity Verification](/connect/testing-verification)
