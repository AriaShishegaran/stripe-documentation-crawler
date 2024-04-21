# Manage payout accounts for connected accounts

[account types](https://stripe.com/docs/connect/accounts)

Payout accounts can be bank accounts or debit cards. Stripe recommends collecting external account details with the Connect Onboarding web form, which helps you:

[Payout](/payouts)

- Save design and development time.

- Eliminate the need to store sensitive data such as account and routing numbers on your server.

- Eliminate the need to build form validations when users enter account details.

In the US, we also recommend using Stripe Financial Connections, which lets your users securely link their financial accounts to your business. It helps you:

[Stripe Financial Connections](/financial-connections)

- Increase onboarding conversion by preventing your accounts from having to interrupt the process to locate their account and routing numbers.

- Reduce first payout failure rates by eliminating errors that result from manual entry of account and routing numbers.

- Eliminate the need to store sensitive data such as account and routing numbers on your server.

- Eliminate the need to build form validations when accounts enter account details in custom onboarding forms.

- Enable your accounts to authenticate in fewer steps by reusing bank account details they’ve saved to Link. Accounts that save their account information at any of the Stripe businesses using Link can share their account details with your platform the next time they use Financial Connections.

[Link](https://support.stripe.com/questions/link-for-financial-connections-support-for-businesses)

- Access additional information on an account’s external bank account, such as balances, ownership details, and transactions. You can mitigate fraud during onboarding by verifying that information, such as the name and address of the external bank account holder.

[balances](/financial-connections/balances)

[ownership details](/financial-connections/ownership)

[transactions](/financial-connections/transactions)

Financial Connections is free when you include Link. Otherwise, using it incurs fees.

[incurs fees](https://stripe.com/financial-connections#pricing)

Alternatively, if you use API onboarding for your connected accounts, you can collect payout account details with a custom form in your account onboarding flow.

Stripe-hosted onboarding for connected accounts uses a web form hosted by Stripe to collect the information required to onboard connected accounts. You can use Financial Connections with Stripe-hosted onboarding to collect external bank account details, but not debit card details.

[Stripe-hosted onboarding for connected accounts](/connect/custom/hosted-onboarding)

Stripe platforms in the US can enable Stripe Financial Connections within the Stripe-hosted onboarding form by following these steps:

[Stripe Financial Connections](/financial-connections)

- Navigate to your External Account settings, where you manage optional Connect onboarding features.

[External Account settings](https://dashboard.stripe.com/settings/connect/payouts/external_accounts)

- For connected accounts where your platform collects account information when requirements change, including for Custom accounts, you must allow Stripe-hosted onboarding to collect external account details. Under Stripe-hosted onboarding for Custom accounts, allow Stripe to collect external account information by turning on the toggle.

- Under How will bank account details be collected?, select Financial Connections.

- (Optional) Request permission to access additional data on the accounts instantly verified with Financial Connections, such as balances, ownership details, and transactions. If you opt to request this additional information, you’ll be prompted to sign up for Stripe Financial Connections.

When external account detail collection is enabled, all connected accounts are prompted to authenticate their bank account using the Stripe-hosted modal UI embedded within the onboarding form.

A Connect onboarding flow using Stripe Financial Connections to collect a payout account.

If a connected account can’t instantly verify their bank account using Financial Connections, the verification process automatically falls back to manual entry:

A Connect onboarding flow using the Stripe Financial Connections modal to collect a payout account using manual entry.

After onboarding, the specified bank account automatically attaches to the connected account.

You can determine if your user linked a Financial Connections Account by retrieving any linked Financial Connections Accounts using their connected account ID. Be sure to specify their account ID in the Stripe-Account header.

This returns an API response similar to the following:

If any Financial Connections accounts are listed, it indicates that the connected account linked them during the onboarding process. You can use the id value to access or refresh the data you specified in your External Account settings. To protect the privacy of your connected account’s data, you can only access the data you specified.

[External Account settings](https://dashboard.stripe.com/settings/connect/payouts/external_accounts)

To start retrieving account data, follow the guides for balances, ownership, and transactions. On all subsequent account retrieval and refresh requests, be sure to include the Stripe-Account header with the connected account ID:

[balances](/financial-connections/balances)

[ownership](/financial-connections/ownership)

[transactions](/financial-connections/transactions)
