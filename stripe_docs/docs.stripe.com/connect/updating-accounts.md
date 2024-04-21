# Updating service agreements

[account types](https://stripe.com/docs/connect/accounts)

Working with connected accounts where your platform is liable for negative balances, including Custom and Express accounts, provides a lot of flexibility. You can access almost every Stripe account property through the API.

[account](/api/accounts)

Some of the reasons for Platforms to update connected accounts include:

- Handle acceptance and re-acceptance of the Stripe Connected Account Agreement (for accounts with no Stripe-hosted Dashboard access, including Custom accounts)

- Handle identity verification (for accounts with no Stripe-hosted Dashboard access, including Custom accounts)

- Manage the connected business’s information, such as the name, logo, and URL

- Set some charge behaviors

- Establish payout handling

[payout](/payouts)

All the above can be done through an update account call, demonstrated in the next code example, although identity verification and payouts are more complex.

[update account](/api#update_account)

[identity verification](/connect/identity-verification)

[payouts](/connect/payouts-connected-accounts)

## Viewing an account’s Dashboard

You, as the platform, can update some account settings without using the API by viewing the Connected accounts section of your Dashboard.

[Connected accounts](https://dashboard.stripe.com/connect/accounts/overview)

Click any connected account in the list to see more details about that account

This allows you—or your support team—to see the status of payouts, search for payments, and update some of the connected account’s information if needed. The information that you can view and change depends on the type of connected account.

## Stripe’s service agreement acceptance

To provide Stripe Connect services to your users, Stripe must establish a direct contractual relationship with those users. That requires all Connected Accounts with no Stripe-hosted Dashboard access to accept the correct Stripe service agreement. The service agreement your users must accept depends on whether they are merchants subject to Stripe’s full terms of service or are payment recipients subject to the recipient service agreement. It’s your responsibility to make sure your users agree to the correct service agreement before accepting or receiving payments through Stripe on your platform.

If, after onboarding, your user transfers ownership of their account or updates the verified tax identification number associated with their account, the current account owner must provide their agreement to the Stripe service agreement. You are responsible for obtaining this renewed agreement from your user.

As a minimum requirement, you must present your users with a link to the correct agreement and they must expressly consent to it prior to using Stripe (for example, at the point of activating their account).

Register Your Account

By registering your account, you agree to our Services Agreement and the Stripe Connected Account Agreement.

[Stripe Connected Account Agreement](https://stripe.com/connect-account/legal/full)

One way to secure acceptance of Stripe’s service agreement is to include it in your terms of service. In your terms, include a link to the correct Stripe service agreement and clearly state that accepting your terms includes accepting the Stripe service agreement.



Payment processing services for [account holder term, for example, drivers or sellers] on [platform name] are provided by Stripe and are subject to the Stripe Connected Account Agreement, which includes the Stripe Terms of Service (collectively, the “Stripe Services Agreement”). By agreeing to [this agreement / these terms / and so on] or continuing to operate as a [account holder term] on [platform name], you agree to be bound by the Stripe Services Agreement, as the same may be modified by Stripe from time to time. As a condition of [platform name] enabling payment processing services through Stripe, you agree to provide [platform name] accurate and complete information about you and your business, and you authorize [platform name] to share it and transaction information related to your use of the payment processing services provided by Stripe.

[Stripe Connected Account Agreement](https://stripe.com/connect-account/legal/full)

[Stripe Terms of Service](https://stripe.com/legal)

For connected accounts where the platform collects updated information for due or changed requirements, you must collect the updated acceptance of Stripe’s service agreement.

To indicate to Stripe that a connected account accepted Stripe’s service agreement, perform an update account call, providing the acceptance date as a timestamp and the user’s IP address:

To meet Stripe’s Financial Partner requirements, you must advise your connected accounts of Stripe’s acquirers and their contact information in a clear and conspicuous manner, including this disclosure. You do not need to include this disclosure when your accounts fall solely under the Recipient Service Agreement.

[this disclosure](https://stripe.com/legal/acquirer-disclosure)

If you are relying on a Stripe onboarding product for collection of Stripe’s service agreement acceptance, we include that disclosure.

## Disclosing how Stripe processes user data

While providing your users with Connect Services, Stripe processes their data as explained in Stripe’s Privacy Policy.  You must disclose that to your users by providing them with a link to that policy.

[Stripe’s Privacy Policy](https://stripe.com/privacy)

In addition, users in Canada must consent to allow Stripe to obtain information from credit agencies to verify their identities.  You can obtain that consent by incorporating language like the following into your onboarding flow where users agree to your terms of service:

Our payment processor can obtain information from credit agencies to verify your identity. That information will be used for the purposes described in their Privacy Policy.

If you are using a Stripe onboarding product like embedded onboarding, but providing your own Privacy Policy link, your privacy policy must include a link to Stripe’s Privacy Policy and the following language:

When you provide personal data in connection with the [Payment Services], Stripe receives that personal data and processes it in accordance with Stripe’s Privacy Policy.

You can replace the term “Payment Services” with any defined term you use to identify the services Stripe provides to your users.

For Stripe to lawfully process personal data according to your instructions, you can be legally required to provide additional disclosures or obtain additional consents. Talk to your lawyer about those possible disclosures and consents.

## See also

- Identity Verification

[Identity Verification](/connect/identity-verification)

- Account Tokens

[Account Tokens](/connect/account-tokens)

- Control Bank and Debit Card Payouts

[Control Bank and Debit Card Payouts](/connect/payouts-connected-accounts)

- Manage bank accounts and debit cards

[Manage bank accounts and debit cards](/connect/payouts-bank-accounts)

- Receive payouts

[Receive payouts](/payouts)

- Full API reference

[Full API reference](/api)
