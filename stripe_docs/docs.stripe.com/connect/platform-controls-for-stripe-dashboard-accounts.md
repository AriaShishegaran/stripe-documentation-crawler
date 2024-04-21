# Platform controls in the Stripe Dashboard

[account types](https://stripe.com/docs/connect/accounts)

Thousands of platforms and marketplaces use Stripe Connect to facilitate payments and pay out recipients. Using the Stripe Dashboard and relying on Stripe to manage onboarding, reporting, and loss liability is already the fastest way to enable your customs to accept payments directly. Now you can manage more features on behalf of your connected accounts with platform controls.

[Stripe Connect](https://stripe.com/connect)

[Stripe Dashboard](/connect/stripe-dashboard)

- Control payout timing

[Control payout timing](#control-payout-timing)

- Access consolidated reporting

[Access consolidated reporting](#access-consolidated-reporting)

- Co-brand your connected accounts

[Co-brand your connected accounts](#co-brand-your-connected-account-experience)

Starting in June 2021, Platforms using OAuth with read_write scope won’t be able to connect to accounts that are controlled by another platform. Learn more about OAuth changes for Standard Platforms.

[OAuth changes for Standard Platforms](/connect/oauth-changes-for-standard-platforms)

## Configuring platform controls

Navigate to the third-party extensions page.

[third-party extensions](https://dashboard.stripe.com/settings/connect/stripe-dashboard/extensions)

Select the options for your connected accounts there. These options apply to all of your new connected accounts moving forward. Visit the connected accounts page to change settings for individual connected accounts.

[connected accounts](https://dashboard.stripe.com/connect/accounts/overview)

## Control payout timing

As the platform, you can now update your connected accounts’ payouts programmatically using the Stripe API or in the Stripe Dashboard.

[payouts](/payouts)

[using the Stripe API](/connect/manage-payout-schedule)

[in the Stripe Dashboard](/connect/dashboard/managing-individual-accounts#updating-accounts)

You can also initiate payouts on behalf of your connected accounts programmatically using the Stripe API or via the Dashboard.

[using the Stripe API](/connect/manual-payouts)

[via the Dashboard](/connect/dashboard/managing-individual-accounts#sending-funds)

Navigate to the payout schedules page to determine whether connected accounts can manage their own payout schedules. Connected accounts can still make manual payouts after you, as the platform, choose to restrict connected accounts from updating their own payout schedule.

[payout schedules](https://dashboard.stripe.com/settings/connect/payouts/schedules)

If you need full control over your connected accounts’ payouts and want to restrict your connected accounts from being able to make their own payouts, contact us with a detailed description of your use case.

[contact us](https://support.stripe.com/contact)

## Access consolidated reporting

You can access reporting across all connected accounts that you control using the built in-Dashboard reporting as well as within Stripe Sigma, a custom reporting solution that makes all of your data available as an interactive SQL environment in the Dashboard. To learn more:

- Stripe Financial reports

[Stripe Financial reports](/reports)

- Stripe Sigma for Connect platforms

[Stripe Sigma for Connect platforms](/stripe-data/query-connect-data)

## Co-brand your connected accounts

As the platform, you can manage your brand settings within the Connect Settings > Stripe Dashboard section. All new accounts onboarding to your platform will see your icon and branding color in their dashboard. To understand changes for connected accounts, see this Support article.

[Support article](https://support.stripe.com/questions/platform-administered-stripe-accounts)

These features apply only to new accounts onboarding to your platform, denoted by true in the is_controller property for the Account object. Existing accounts aren’t eligible for these features.

[Account object](/api/accounts/object#account_object-controller-is_controller)

## Remove accounts

From the connected account details page in your Dashboard, click the overflow menu () and choose Remove account. This action disconnects the account and revokes access in the same way as the OAuth de-authorize endpoint. Removing an account from your platform resets any platform controls (such as payout timing) you’ve configured for the connected account. If the account reconnects later, prior platform controls aren’t reinstated.

[Dashboard](https://dashboard.stripe.com/connect/accounts/overview)
