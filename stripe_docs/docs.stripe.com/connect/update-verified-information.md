# Update verified user information

[account types](https://stripe.com/docs/connect/accounts)

For connected accounts where your platform collects updated information for due or changed requirements, you collect the required information for each account during onboarding, and Stripe verifies it. If you update verified user information, Stripe must review it. If Stripe can’t verify it, you have a grace period of 14 days to resolve any issues and complete verification.

[required information](/connect/required-verification-information)

During this grace period, the account functionality remains the same. For example, if charges or payouts were previously enabled, they’ll continue to be enabled until the grace period ends. The value of requirements.current_deadline determines the end of the grace period and isn’t extended if you update additional information. Resolve all requirements by the end of the grace period to prevent charges or payouts from being disabled.

[payouts](/payouts)

[requirements.current_deadline](/api/capabilities/object#capability_object-requirements-current_deadline)

These fields can be updated, with a grace period, after they’ve been verified:

- Business name

- Business type

- First name

- Last name

- Date of birth

- Business tax ID

- Tax ID registrar

- Personal ID number

These fields can’t be updated after a company has been verified:

- Verification documents

## Change the account representative

You must specify a representative to activate the account, agree to Stripe’s terms, and act as primary contact for the account. You can change the account representative for any reason (for example, the designated representative left the company or they no longer serve as owner or executive).

Do the following to change the account representative:

- If necessary, add a Person object for the new representative. Stripe recommends that you verify the Person before proceeding, whether you designate an existing Person as the new representative or add a new Person.

[Person](/api/persons/object#person_object-verification)

- Update the Person object to remove them as the current representative:

[Person](/api/persons/object#person_object-verification)

- Update the Person object to nominate the new representative:

[Person](/api/persons/object#person_object-verification)

- Monitor the requirements.currently_due and requirements.past_due arrays to make sure that verification of the new representative is complete. Even if the new representative Person is already verified, there might be additional requirements for the representative role.

After you set a representative to false, Stripe allows a grace period of 14 days for you to set the new representative to true and to complete verification.

## Update the account tax identification number

Connected account owners in Brazil can’t update Tax IDs (personal* or business) after verification.

When your connected account updates its verified Tax ID (personal* or business), the account must agree again to the Stripe Services Agreement (SSA). Doing so accepts the transfer of ownership of their account and its balances from the entity assigned the initial Tax ID to the one assigned the new Tax ID. The information below describes the process for collecting this requirement when changing an account’s verified Tax ID.

- This applies when you update or resubmit a verified representative’s existing ID number and ssn_last_4.

After the account updates its Tax ID, the account enters a 14-day grace period during which it must agree once again to the Stripe Services Agreement (SSA) and make sure it’s compliant with all requirements. If the connected account can’t meet its requirements after 14 days, then charges and payouts for the account are paused

You have a few ways to collect this requirement:

- If you use Connect Onboarding, you can provide a link to Stripe’s onboarding flow. From there, the account can fulfill any necessary requirements.For accounts with access to the Stripe Express Dashboard, you can create a single-use Dashboard login link that allows the account to edit their tax identification number and agree once again to the Stripe Services Agreement (SSA).For accounts with no Stripe-hosted Dashboard access, you can provide a link to Connect Onboarding, where your account can edit their tax identification number and agree once again to the Stripe Services Agreement (SSA).

If you use Connect Onboarding, you can provide a link to Stripe’s onboarding flow. From there, the account can fulfill any necessary requirements.

- For accounts with access to the Stripe Express Dashboard, you can create a single-use Dashboard login link that allows the account to edit their tax identification number and agree once again to the Stripe Services Agreement (SSA).

[the Stripe Express Dashboard](/connect/express-dashboard)

- For accounts with no Stripe-hosted Dashboard access, you can provide a link to Connect Onboarding, where your account can edit their tax identification number and agree once again to the Stripe Services Agreement (SSA).

[Connect Onboarding](/connect/custom/hosted-onboarding#account_update)

- If you onboard your connected accounts through your platform rather than using Connect Onboarding, you must collect this requirement by following the instructions in the following section.

If you onboard your connected accounts through your platform rather than using Connect Onboarding, you must collect this requirement by following the instructions in the following section.

If you allow accounts with no Stripe-hosted Dashboard access, including Custom accounts, to update their verified Tax ID through your platform, you must add a section to make it clear that the account agrees once again to the Stripe Services Agreement (SSA). You must also make it clear that the account owner associated with the original TIN agrees to transfer ownership of the account and its balances to the owner associated with the updated TIN.

One way to achieve this is by including a clear reference and link to the agreement language below, then documenting that the account agrees using the update account API:

[update account](/api/accounts/update)

If you own the Stripe account associated with the original TIN, you agree to transfer ownership of the account and balances to the updated account owner (associated with the updated TIN), and that the updated owner has agreed to assume your agreements with Stripe. If you are the updated owner, you acknowledge that the ownership of this Stripe account has been transferred to you and that you assume the agreements that the prior account owner has with Stripe.

Use the update account API to collect the requirements, providing the user’s IP address and the acceptance date as a timestamp. The acceptance date of the signature (tos_acceptance[date]) must be the time that your connected account requested the update to the Tax ID number. It can also be any time after they requested the update.

[update account](/api/accounts/update)
