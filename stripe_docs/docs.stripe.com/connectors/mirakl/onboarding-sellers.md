# Onboarding sellers

You can use Express or Custom accounts with the transfers capability to onboard your sellers.

[Express](/connect/express-accounts)

[Custom](/connect/custom-accounts)

[transfers](/connect/account-capabilities#transfers)

Standard accounts aren’t supported.

[Standard accounts](/connect/standard-accounts)

## Seller account initiation

The workflow starts when you create a new shop. If you invite the seller via email, the workflow starts when they submit the initial Mirakl form.

- The onboarding job fetches newly created Mirakl shops.

[onboarding job](/connectors/mirakl/reference#onboarding)

- The connector adds an onboarding link to each shop.

- The seller finds the link in their Mirakl back office under My Account.

- They complete their KYC/KYB on Stripe.

- The seller is redirected to the REDIRECT_ONBOARDING URL.

Stripe then performs verification, asking for more information when needed. To handle this, see the communication guidelines.

[communication](#communication)

You can build your own onboarding flow and then use the following API request to map the Stripe account with the Mirakl shop:

## Seller account update

The workflow starts with the seller intending to update their information on Stripe.

- The seller finds the link in their Mirakl back office under My Account.

- They update their information on Stripe.

- The shop custom field is updated with a fresh login link to their Express dashboard.

[Express dashboard](/connect/express-dashboard)

- The KYC status is updated on Mirakl.

The last two steps are also performed when accounts are updated by the connector during the account initiation workflow or when accounts are updated by Stripe, for example, a new document needs to be provided. You can receive a notification when that happens, see the Account updated notification.

[account initiation workflow](#account-initiation-workflow)

[Account updated](/connectors/mirakl/reference#account-updated)

Stripe then performs verification, asking for more information when needed. To handle this, see the communication guidelines.

[communication](#communication)

## Communication

You can customize the visual appearance of the Stripe form with your brand’s name, color, and icon in your Connect settings page.

[Connect settings page](https://dashboard.stripe.com/account/applications/settings)

Be sure to tell your sellers about the link available in their Mirakl account settings and the need to complete the onboarding on Stripe to receive their payouts. For example, you could customize some of the email templates sent to your sellers by Mirakl under Settings > Notifications.

If we require more information from your sellers, we’ll email them directly for Express accounts. You must inform the sellers yourself if you decided to use Custom accounts.

In test mode, no emails are sent.

## See also

- Integration steps.

[Integration steps](/connectors/mirakl#integration-steps)
