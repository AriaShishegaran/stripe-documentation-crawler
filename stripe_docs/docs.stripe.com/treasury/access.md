# Get started with API access to Treasury and Issuing

Stripe Treasury is available in the United States only.

You can use Stripe Treasury and Issuing in test mode to see what functionality you want to enable in your live integration.

## Get test mode access to Treasury and Issuing

Enable your Stripe account to request issuing and treasury capabilities on connected accounts.

To issue cards to your own company or employees, activate Issuing in test mode) without connected accounts from the Dashboard.

[activate Issuing in test mode](https://dashboard.stripe.com/test/issuing/overview)

Connected accounts are always required for Treasury.

[always required for Treasury](/treasury/account-management/treasury-accounts-structure)

Activate Test Mode in the Dashboard

[Activate Test Mode in the Dashboard](https://dashboard.stripe.com/setup/treasury/activate?a=1)

Click Activate Test Mode in the Dashboard then, from the Dashboard, click Get started > Enable Test mode.

You must be an account administrator to complete the Treasury onboarding steps for a platform.

[account administrator](/get-started/account/teams/roles)

## Start with test mode

There are a few ways to start testing the Issuing and Treasury APIs.

Use the Issuing and Treasury sample application to onboard your first test mode connected account, create a financial account and card, and make test transactions.

[Issuing and Treasury sample application](/treasury/examples/sample-app)

You must use the API or sample app to create financial accounts and cards linked to financial accounts. After you create a financial account, you can use the Dashboard to view activity, copy routing and account numbers, and move funds from your platform Treasury balance into the financial account. After you create a card, you can use the Dashboard to make test authorizations. See Use the Dashboard for Issuing with connect.

[Use the Dashboard for Issuing with connect](/issuing/connect#using-dashboard-issuing)

To test Treasury without Issuing, request the treasury capability on a connected account and don’t request card_issuing. When you activate test mode through the link above, it gives your platform the ability to request both capabilities independently.

To confirm you’ve enabled Treasury and Issuing in test mode, click Treasury in the Dashboard to access the Financial Accounts page. If you can’t access Financial Accounts then you haven’t enabled access.

[Financial Accounts page](https://dashboard.stripe.com/test/connect/financial-accounts)

## Configure your account to go live

Enabling Treasury and Issuing through the link above lets you try out basic functionality in test mode. However, this is a temporary state, and after you’re approved for a supported business use case, your account loses access to any test mode objects you created in this mode, such as test financial accounts, cardholders and cards.

[supported business use case](https://support.stripe.com/questions/supported-business-use-cases-for-stripe-issuing)

Speak to sales to get approved for a supported business use case, and configure your account for live mode and ongoing test mode access.

[Speak to sales](https://go.stripe.global/treasury-inquiry)

Speak to sales before building a full API integration, because some functionality could change.
