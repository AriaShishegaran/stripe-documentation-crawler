htmlUsing Connect with Standard accounts | Stripe Documentation[Skip to content](#main-content)Standard[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fstandard-accounts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fstandard-accounts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Using Connect with Standard accounts

Integrate with Standard accounts to get started using Connect right away, and let Stripe handle the majority of the user experience and user communication.### Connect Onboarding

This is the recommended method for creating standard accounts. If you’re an extension or an application that needs access to an existing account so you can provide services to your users, you can still use OAuth.

A Standard Stripe account is a conventional Stripe account where the account holder (that is, your platform’s user) has a relationship with Stripe, is able to log in to the Dashboard, and can process charges on their own.

Stripe’s sample integration, Kavholm, shows you how to use Connect Onboarding for a seamless user onboarding experience.

![Screenshot of Connect Onboarding form](https://b.stripecdn.com/docs-statics-srv/assets/Kavholm-Seamless-Standard.78b64d90c0bf87130c8b6ba1ef53df7f.png)

## Get started

If you’re new to Connect, start with a guide to use Standard accounts to enable other businesses to accept payments directly.

## How to use Connect Onboarding for Standard accounts

1. Go to your Connect settings page to customize the visual appearance of the form with the name, color, and icon of your brand. Connect Onboarding requires this information.


2. Use the /v1/accounts API to create a new account and get the account ID. You can prefill information on the account object for the user before you generate the account link. You must pass the following parameter:

  - `type`=`standard`

NoteAfter you create the new account, check to see that the account displays in the Dashboard.


3. Call the Account Links API to create a link for the account to onboard with.


4. In the onboarding flow for your own platform, redirect your user to the url returned by Account Links.


5. Handle additional account states, redirecting your account to the Connect Onboarding flow if necessary.


6. Optional: You can add additional procedures, such as Tax or Climate, to the Connect Onboarding flow through the platform product configuration in the Dashboard.



[Create a Standard account and prefill information](#create-account)Use the Create Account API to create a connected account with type set to standard. You can prefill any information, but at a minimum, you must specify the type. The country of the account defaults to the same country as your platform, and the account confirms the selection during onboarding.

NoteThis example includes only some of the fields you can set when creating an account. For a full list of the fields you can set, such as address and website_url, see the Create Account API reference.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d type=standard`If you’ve already collected information for your connected accounts, you can prefill that information on the account object. You can prefill any account information, including personal and business information, external account information, and so on.

Connect Onboarding doesn’t ask for the prefilled information. However, it does ask the account holder to confirm the prefilled information before accepting the Connect service agreement.

When testing your integration, prefill account information using test data.

[Create an account link](#create-link)You can create an account link by calling the Account Links API with the following parameters:

- `account`- use the account ID returned by the API from the previous step
- `refresh_url`
- `return_url`
- `type`=`account_onboarding`

Command Line[curl](#)`curl https://api.stripe.com/v1/account_links \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d account={{CONNECTED_ACCOUNT_ID}} \
  --data-urlencode refresh_url="https://example.com/reauth" \
  --data-urlencode return_url="https://example.com/return" \
  -d type=account_onboarding`[Redirect your user to the account link URL](#redirect-link)The response to your Account Links request includes a value for the key url. Redirect to this link to send your user into the flow. You can only use URLs from the account links once because they grant access to the account holder’s personal information. Authenticate the user in your application before redirecting them to this URL. After you create an account link on a Standard account, you won’t be able to read or write Know Your Customer (KYC) information. Prefill any KYC information before creating the first account link.

Security tipDon’t email, text, or otherwise send account link URLs outside of your platform application. Instead, provide them to the authenticated account holder within your application.

[Handle the user returning to your platform](#return-user)Connect Onboarding requires you to pass both a return_url and refresh_url to handle all cases where you redirect the user to your platform. It’s important that you implement these correctly to provide the best experience for your user.

NoteYou can use HTTP for your return_url and refresh_url while in test mode (for example, to test with localhost), but you can only use HTTPS in live mode. Be sure to swap testing URLs for HTTPS URLs before going live.

return_url![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Stripe issues a redirect to this URL when the user completes the Connect Onboarding flow. This doesn’t mean that all information has been collected or that there are no outstanding requirements on the account. This only means the flow was entered and exited properly.

No state is passed through this URL. After redirecting a user to your return_url, check the state of the details_submitted parameter on their account by doing either of the following:

- Listening to`account.updated`[webhooks](/webhooks)
- Calling the[Accounts](/api/accounts)API and inspecting the returned object

refresh_url![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Your user redirects to the refresh_url in these cases:

- The link expired (a few minutes went by since the link was created)
- The user already visited the link (they refreshed the page, or clicked back or forward in the browser)
- Your platform is no longer able to access the account
- The account has been rejected

Your refresh_url triggers a method on your server to call Account Links again with the same parameters, and redirect the user to the Connect Onboarding flow to create a seamless experience.

[Handle users that have not completed onboarding](#handle-users)A user that is redirected to your return_url might not have completed the onboarding process. Use the /v1/accounts endpoint to retrieve the user’s account and check for charges_enabled. If the account isn’t fully onboarded, provide UI prompts to allow the user to continue onboarding later. The user can complete their account activation through a new account link (generated by your integration). You can check the state of the details_submitted parameter on their account to see if they’ve completed the onboarding process.

[OptionalEnable Stripe Tax obligation monitoring](#enable-stripe-tax)## See also

- [Creating charges](/connect/charges)
- [Authentication](/connect/authentication)
- [OAuth reference](/connect/oauth-reference)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Get started](#get-started)[How to use Connect Onboarding for Standard accounts](#how-to-use-connect-onboarding-for-standard-accounts)[Create a Standard account and prefill information](#create-account)[Create an account link](#create-link)[Redirect your user to the account link URL](#redirect-link)[Handle the user returning to your platform](#return-user)[Handle users that have not completed onboarding](#handle-users)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`