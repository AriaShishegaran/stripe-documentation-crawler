# Payouts

Renders the balance summary, the payout schedule, and a list of payouts for the connected account. It can also allow the user to perform instant or manual payouts.

When creating an Account Session, enable the payouts embedded component by specifying payouts in the components parameter. You can enable or disable individual features of the payouts component by specifying the features parameter under payouts:

[creating an Account Session](/api/account_sessions/create)

After creating the account session and initializing ConnectJS, you can render the payouts component in the front end:

[initializing ConnectJS](/connect/get-started-connect-embedded-components#account-sessions)

Enabling Instant Payouts might require additional steps:

- If your platform collects fees for a connected account, you must set up Instant Payout monetization in the Dashboard.

[Dashboard](https://dashboard.stripe.com/settings/connect/payouts/instant-payouts)

- If your platform is liable for a connected account’s negative balances, your platform must be in a supported country and the account must be in the same country as the platform.

[same country as the platform](/connect/instant-payouts#eligible-connected-accounts)

- If Stripe is liable for a connected account’s negative balances, Stripe controls eligibility for the account.

[Stripe controls eligibility](/payouts/instant-payouts#eligibility-and-daily-volume-limits)

To use standard manual payouts, the connected account needs to have their payout schedule set to manual. You can enable payout schedule editing in the payouts component by setting the edit_payout_schedule feature to true.

[payout schedule](/connect/manage-payout-schedule)
