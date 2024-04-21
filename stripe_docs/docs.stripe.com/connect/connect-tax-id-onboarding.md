# Tax ID Additional Verification

Connect dynamically requires onboarding information to keep your accounts compliant, but you can influence what information Connect requires in your platform by adding additional verifications (AVs) to accounts. Requesting an additional verification requires your connected accounts to provide certain information, which is then verified.

[dynamically requires onboarding information](/connect/required-verification-information)

[accounts](/connect/accounts)

Platforms might be subject to IRS fines up to 290 USD per submission if they file 1099s with incorrect information (for example, name or tax ID mismatches). The Tax ID AV provides a way for platforms to collect certified tax IDs throughout the year directly from your connected accounts before issuing 1099s, to make sure the appropriate 1099 tax forms use the correct Taxpayer Identification Number (TIN).

The Tax ID Additional Verification performs a name and TIN check either at the personal level or business level based on required verification information for taxes.

[required verification information for taxes](/connect/required-verification-information-taxes)

## How it works

The Tax ID Additional Verification allows you to enforce the mandatory collection and verification of tax ID requirements for a connected account. Platforms add requirements for Tax ID collection/verification for a connected account using the Accounts API.

[Accounts API](/api/connected_accounts)

For Custom Connect platforms, after you add the requirements on a connected account, your platform can Create an account link to redirect the user from your platform to Connect Onboarding. Alternatively, you can collect the requirements directly from your platform, and then send it to Stripe using Update an account. For Express Connect platforms, Stripe sends the Express connected accounts an email to complete the missing or invalid requirements using the Express Dashboard.

[Create an account link](/api/account_links/create)

[Connect Onboarding](/connect/express-accounts)

[Update an account](/api/accounts/update)

[Express Dashboard](/connect/express-dashboard)

After Stripe receives the user’s TIN, we automatically verify it by comparing it with the IRS database. If the IRS database confirms the TIN is a match, the requirements are considered satisfied. If the IRS database doesn’t return a TIN match with the connected account’s tax details, then enforcement limits are triggered.

Platforms have full customization in setting enforcement limits to determine when Connected Accounts are required to provide a verified TIN. You can set the following enforcement limits to impose disablement of payouts or payouts or payments if a verified TIN isn’t on file:

- Upfront: Block payouts or payments if a verified TIN isn’t on file immediately.

- Volume: Block payouts or payments if a verified TIN isn’t on file after processing x USD.

- Time: Block payouts or payments if a verified TIN isn’t on file after x days.

- Combo: Block payouts or payments if a verified TIN isn’t on file after x days or after processing x USD.

## Get started

Currently, access to Stripe’s Tax ID Additional Verification is limited to US beta users. To request access to the beta, reach out to your account team or contact Stripe for more information.

[contact Stripe](https://stripe.com/contact/sales)