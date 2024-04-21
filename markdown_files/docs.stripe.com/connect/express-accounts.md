htmlUsing Connect with Express accounts | Stripe Documentation[Skip to content](#main-content)Express[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fexpress-accounts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fexpress-accounts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Using Connect with Express accounts

Express accounts enable your platform to manage payout schedules, customize the flow of funds, and control branding. Stripe will handle onboarding, account management, and identity verification for your platform.## Express demo

To see the complete Express onboarding flow in action, try the sample end-to-end Express integration before you start building your own. This demo includes an example of a user onboarding experience and account management for Rocket Rides, an on-demand marketplace.

You can find the demo’s complete source code on GitHub.

![Rocket Rides, a demo of Stripe Connect with Express accounts](https://b.stripecdn.com/docs-statics-srv/assets/rocket-rides-new.e01ced22698d7f5d3d1c915f26175dcd.png)

## Before you begin

To create Express accounts, you must meet all of these requirements:

- Minimum API version: Express requires the API version 2017-05-25 or later.[Capabilities](/connect/account-capabilities)in Express require the API version 2019-02-19 or later.
- Platform in a supported country: Platforms in Australia, Austria, Belgium, Brazil, Bulgaria, Canada, Croatia, Cyprus, the Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hong Kong, Hungary, Ireland, Italy, Japan, Latvia, Lithuania, Luxembourg, Malta, Mexico, the Netherlands, New Zealand, Norway, Poland, Portugal, Romania, Singapore, Slovakia, Slovenia, Spain, Sweden, Switzerland, Thailand, the United Kingdom, and the United States can create Express accounts for most countries[Stripe supports](https://stripe.com/global). For information about country-specific restrictions, or to request notification when Express accounts become available in your country,[let us know](mailto:connect@stripe.com).
- Countries that don’t support self-serve: Due to restrictions that apply when using Connect in the[United Arab Emirates](https://support.stripe.com/questions/connect-availability-in-the-uae)and[Thailand](https://support.stripe.com/questions/stripe-thailand-support-for-marketplace), platform users in these countries can’t self-serve Express Connect accounts. To begin onboarding for Express Accounts in these countries,[contact us](https://stripe.com/contact/sales).
- Platforms in the UAE: Platforms in the UAE can only use Express accounts based in the UAE with the following charge types:[destination_charges](/connect/destination-charges)and[separate charges and transfers](/connect/separate-charges-and-transfers). Destination charges using the[on_behalf_of](/api/payment_intents/object#payment_intent_object-on_behalf_of)attribute are not yet supported for UAE platforms.
- Vetting for fraud: Because your platform is responsible for losses incurred by Express accounts, you must closely examine all accounts that sign up through your platform for potential fraud. Refer to our[risk management best practices guide](/connect/risk-management/best-practices#fraud)for more information.
- Platform profile: You need to complete your[platform’s profile](https://dashboard.stripe.com/connect/registration).

## Onboarding Express Accounts outside of your platform’s country

You can enable onboarding on a per-country basis in the Connect Settings section of your Dashboard.

The Express account onboarding flow is currently localized in English, French, Spanish, Bulgarian, Simplified Chinese, Traditional Chinese, Czech, Danish, Dutch, Estonian, Finnish, German, Greek, Hungarian, Indonesian, Italian, Japanese, Latvian, Lithuanian, Norwegian, Polish, Portuguese, Romanian, Slovak, Slovenian, Swedish, and Thai.

Keep the following in mind when onboarding accounts globally:

- International business:Your platform is responsible for understanding the implications of doing business internationally, such as tax and financial reporting.
- Charge flows:Be sure to review your options for[creating charges](/connect/charges)based on the countries you intend to operate in.
- Service agreement type:Your platform can create connected accounts under the[recipient service agreement](/connect/service-agreement-types#recipient)to enable[cross-border transfers](/connect/account-capabilities#transfers-cross-border). Such accounts have restricted access to capabilities.

[Configure the onboarding experience](#configure-onboarding)Before onboarding your first account, go to the Connect settings page to customize the visual appearance of the form with your brand’s name, color, and icon. Connect Onboarding requires this information.

[Create an Express account and prefill information](#create-account)Use the Create Account API to create a connected account with type set to express. You can prefill any information, but at a minimum, you must specify the type. The country of the account defaults to the same country as your platform, and the account confirms the selection during onboarding.

NoteThis example includes only some of the fields you can set when creating an account. For a full list of the fields you can set, such as address and website_url, see the Create Account API reference.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d type=express`If you know the country and capabilities for your connected account, you can provide that information when you create the account. Connect Onboarding then collects the requirements for those capabilities. To reduce onboarding effort, request only the capabilities you need.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d country=US \
  -d type=express \
  -d "capabilities[card_payments][requested]"=true \
  -d "capabilities[transfers][requested]"=true \
  -d business_type=individual \
  --data-urlencode "business_profile[url]"="https://example.com"`If you’ve already collected information for your connected accounts, you can prefill that information on the account object. You can prefill any account information, including personal and business information, external account information, and so on.

Connect Onboarding doesn’t ask for the prefilled information. However, it does ask the account holder to confirm the prefilled information before accepting the Connect service agreement.

When you onboard an account without its own website and your platform provides it with a personal URL, prefill its business_profile.url. If the account doesn’t have a URL, you can prefill its business_profile.product_description instead.

When testing your integration, prefill account information using test data.

If you omit capabilities, Connect Onboarding uses the settings in the Configuration settings section of the Stripe Dashboard to automatically request capabilities based on the account’s country.

[Create an account link](#create-link)Create an Account Link with the following parameters:

- `account`- use the account ID returned by the API from the previous step
- `refresh_url`
- `return_url`
- `type`=`account_onboarding`

Command Line[curl](#)`curl https://api.stripe.com/v1/account_links \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d account={{CONNECTED_ACCOUNT_ID}} \
  --data-urlencode refresh_url="https://example.com/reauth" \
  --data-urlencode return_url="https://example.com/return" \
  -d type=account_onboarding`[Redirect your account to the account link URL](#redirect-link)An Account Link contains a url. Redirect the account to this link to send your account into the onboarding flow. Each Account Link URL can only be used once because it grants access to the account holder’s personal information. Authenticate the account in your application before redirecting them to this URL.

Before creating the first account link for an Express account, prefill any Know Your Customer (KYC) information. After you create an account link for an Express account, you can’t read or update its KYC information.

Security tipDon’t email, text, or otherwise send account link URLs outside of your platform application. Instead, provide them to the authenticated account holder within your application.

[Handle the user returning to your platform](#return-user)Connect Onboarding requires you to pass both a return_url and refresh_url to handle all cases where the user is redirected to your platform. It’s important that you implement these correctly to provide the best experience for your user.

NoteYou can use HTTP for your return_url and refresh_url while in test mode (for example, to test with localhost), but live mode only accepts HTTPS. Be sure to swap testing URLs for HTTPS URLs before going live.

return_url![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Stripe issues a redirect to this URL when the user completes the Connect Onboarding flow. This doesn’t mean that all information has been collected or that there are no outstanding requirements on the account. This only means the flow was entered and exited properly.

No state is passed through this URL. After a user is redirected to your return_url, check the state of the details_submitted parameter on their account by doing either of the following:

- Listen to`account.updated`events with a[Connect webhook](/connect/webhooks).
- [Retrieve](/api/accounts/retrieve)the account with the API.

refresh_url![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Your user is redirected to the refresh_url in these cases:

- The link is expired (a few minutes went by since the link was created).
- The user already visited the URL (the user refreshed the page or clicked back or forward in the browser).
- Your platform can no longer access the account.
- The account has been rejected.

Your refresh_url should trigger a method on your server to call Account Links again with the same parameters, and redirect the user to the Connect Onboarding flow to create a seamless experience.

[Handle users that have not completed onboarding](#handle-users-not-completed-onboarding)A user that’s redirected to your return_url might not have completed the onboarding process. Retrieve the user’s account and check for charges_enabled. If the account isn’t fully onboarded, provide UI prompts to allow the user to continue onboarding later. The user can complete their account activation through a new account link (generated by your integration). You can check the state of the details_submitted parameter on their account to see if they’ve completed the onboarding process.

## See also

- [Express Dashboard](/connect/express-dashboard)
- [Integrate the Express Dashboard](/connect/integrate-express-dashboard)
- [Customize the Express Dashboard](/connect/customize-express-dashboard)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Express demo](#express-demo)[Before you begin](#prerequisites-for-using-express)[Onboarding Express Accounts outside of your platform’s country](#onboarding-express-accounts-outside-of-your-platforms-country)[Configure the onboarding experience](#configure-onboarding)[Create an Express account and prefill information](#create-account)[Create an account link](#create-link)[Redirect your account to the account link URL](#redirect-link)[Handle the user returning to your platform](#return-user)[Handle users that have not completed onboarding](#handle-users-not-completed-onboarding)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`