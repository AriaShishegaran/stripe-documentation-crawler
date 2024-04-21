htmlGet started with API access to Treasury and Issuing | Stripe Documentation[Skip to content](#main-content)Get started with API access[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Faccess)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Faccess)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)[Treasury](#)
[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Treasury](/treasury)·[Home](/docs)[Banking as a service](/docs/financial-services)[Treasury](/docs/treasury)# Get started with API access to Treasury and Issuing

Immediately access test mode to experiment before going live.Regional considerationsUnited StatesStripe Treasury is available in the United States only.

You can use Stripe Treasury and Issuing in test mode to see what functionality you want to enable in your live integration.

## Get test mode access to Treasury and Issuing

Enable your Stripe account to request issuing and treasury capabilities on connected accounts.

To issue cards to your own company or employees, activate Issuing in test mode) without connected accounts from the Dashboard.

Connected accounts are always required for Treasury.

Activate Test Mode in the Dashboard

Click Activate Test Mode in the Dashboard then, from the Dashboard, click Get started > Enable Test mode.

NoteYou must be an account administrator to complete the Treasury onboarding steps for a platform.

## Start with test mode

There are a few ways to start testing the Issuing and Treasury APIs.

### Test with the Issuing and Treasury sample application

Use the Issuing and Treasury sample application to onboard your first test mode connected account, create a financial account and card, and make test transactions.

### Test from the Dashboard

You must use the API or sample app to create financial accounts and cards linked to financial accounts. After you create a financial account, you can use the Dashboard to view activity, copy routing and account numbers, and move funds from your platform Treasury balance into the financial account. After you create a card, you can use the Dashboard to make test authorizations. See Use the Dashboard for Issuing with connect.

### Test Treasury only (without Issuing)

To test Treasury without Issuing, request the treasury capability on a connected account and don’t request card_issuing. When you activate test mode through the link above, it gives your platform the ability to request both capabilities independently.

### Confirm test mode is enabled

To confirm you’ve enabled Treasury and Issuing in test mode, click Treasury in the Dashboard to access the Financial Accounts page. If you can’t access Financial Accounts then you haven’t enabled access.

## Configure your account to go live

Enabling Treasury and Issuing through the link above lets you try out basic functionality in test mode. However, this is a temporary state, and after you’re approved for a supported business use case, your account loses access to any test mode objects you created in this mode, such as test financial accounts, cardholders and cards.

Speak to sales to get approved for a supported business use case, and configure your account for live mode and ongoing test mode access.

CautionSpeak to sales before building a full API integration, because some functionality could change.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Get test mode access to Treasury and Issuing](#get-test-mode-access-to-treasury-and-issuing)[Start with test mode](#start-with-test-mode)[Configure your account to go live](#configure-your-account-to-go-live)Products Used[Treasury](/treasury)[Issuing](/issuing)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`