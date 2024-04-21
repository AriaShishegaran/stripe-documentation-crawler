htmlStripe hosted onboarding for Custom accounts | Stripe Documentation[Skip to content](#main-content)Stripe hosted onboarding for Custom accounts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fcustom%2Fhosted-onboarding)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fcustom%2Fhosted-onboarding)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Custom](/docs/connect/custom-accounts)[Onboard Custom accounts](/docs/connect/custom/onboarding)# Stripe hosted onboarding for Custom accounts

Let Stripe collect identity verification information for your Custom connected accounts.Connect Onboarding for Custom Accounts is a web form hosted by Stripe that takes care of collecting identity verification information from users. It dynamically adjusts the information that it collects to reflect the connected account’s capabilities, country, and business type. Connect Onboarding is the recommended solution to collect identity verification information for Custom accounts, and ensures that your flow is optimized for:

- Mobile browsers
- Accessibility
- Internationalization and localization
- Conversion rate
- Intelligently requesting requirements based on what’s already provided on the account

Here’s what the form looks like for Stripe’s sample integration, Rocket Deliveries:

![Screenshot of Connect Onboarding form](https://b.stripecdn.com/docs-statics-srv/assets/hosted_onboarding_form.37ff5a6f7d39a33ebda671e33419971c.png)

## How to use Connect Onboarding for Custom Accounts

1. Go to your[Connect settings page](https://dashboard.stripe.com/account/applications/settings)to customize the visual appearance of the form: you can provide the name, color, and icon of your brand. You must provide this information for Connect Onboarding to work. Stripe recommends[collecting bank account details within the form](https://dashboard.stripe.com/settings/connect/custom).
2. Create a new account and get the account ID, or use an existing account ID (in the form of`acct_XXXXXXXX`).
3. If you have information about the account holder (like their name, address, or other details), you can proactively provide this through the[account create or update methods](/api/accounts). The more information provide through the API, the less information Connect Onboarding prompts your user for.
4. Call the[Account Links](/api/account_links)with the following parameters (see the[API ref](/api/account_links)for more):  - `account`
  - `refresh_url`
  - `return_url`
  - `type`
  - `collection_options`(optional)


5. In the onboarding flow for your own platform, redirect your user to the`url`returned by[Account Links](/api/account_links).
6. Handle additional account states, redirecting your user back into the Connect Onboarding flow if necessary. To handle user-initiated updates to information they’ve already provided, create a way for your user to get a new redirect to the Connect Onboarding form from your platform’s Dashboard.

[Determine the information to collect](#info-to-collect)Connect Onboarding for Custom Accounts supports upfront or incremental onboarding. Upfront onboarding collects the eventually_due requirements for the account, while incremental onboarding collects the currently_due requirements. For the advantages and disadvantages of each, see the onboarding flows documentation.

The currently_due requirements request only the user information needed for verification at this specific point in time; the eventually_due requirements include a more complete set of questions that we’ll eventually need to collect.

Based on the needs of your platform, pass either currently_due or eventually_due as the value of the collection_options.fields parameter in your calls to Account Links. Here’s an example request:

Command Line[curl](#)`curl https://api.stripe.com/v1/account_links \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d account={{CONNECTED_ACCOUNT_ID}} \
  --data-urlencode refresh_url="https://example.com/reauth" \
  --data-urlencode return_url="https://example.com/return" \
  -d type=account_onboarding \
  -d "collection_options[fields]"=eventually_due`[Redirect your user to the Account Link URL](#redirect)The response to your Account Links request includes a value for the key url. Redirect your user to this link to send them into the flow. You can only use your Account Link URLs one time because they grant access to the account holder’s personal information. Authenticate the user in your application before redirecting them to this URL. If you enable Collect bank account information for payouts in your Connect Custom settings, or if the treasury capability is requested, the user must set up additional authentication with Stripe before entering the onboarding flow.

Security tipDon’t email, text, or otherwise send account link URLs outside of your platform application. Instead, provide them to the authenticated account holder within your application.

[Handle the user returning to your platform](#return)Connect Onboarding requires you to pass both a return_url and refresh_url to handle all cases in which the user will be redirected back to your platform. It’s important that you implement these correctly to provide the best experience for your user.

NoteYou can use HTTP for your return_url and refresh_url while you’re in test mode (for example, to test with localhost), but for live mode only HTTPS is accepted. Be sure you’ve swapped any testing URLs for HTTPS URLs before going live.

return_url![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Stripe will issue a redirect back to this URL when the user completes the Connect Onboarding flow, or clicks Save for later at any point in the flow. It does not mean that all information has been collected, or that there are no outstanding requirements on the account. It only means the flow was entered and exited properly.

No state is passed with this URL. After a user is redirected to your return_url, check the state of the requirements attribute on their account. You can either listen to account.updated webhooks or retrieve the Account object and inspect the state of its requirements attribute. See more details in Step 4 below.

refresh_url![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Your user will be redirected to the refresh_url in these cases:

- The link is expired (a few minutes went by since the link was created)
- The link was already visited (the user refreshed the page or clicked theback/forwardbutton)
- The link was shared in a third-party application such as a messaging client that attempts to access the URL to preview it. Many clients automatically visit links which cause them to become expired

Your refresh_url should trigger a method on your server to call Account Links again, with the same parameters, and redirect the user back into the Connect Onboarding flow to create a seamless experience.

[Handle the case of new requirements becoming due](#new-reqs-due)Set up your integration to listen for changes to account requirements, if you haven’t already done so. We recommend using webhooks to do so. You can test handling new requirements (and how they may disable charges and payouts) with our test mode trigger cards.

When upcoming requirements updates affect your connected accounts, we’ll notify you.

If you use embedded or Stripe-hosted onboarding, you can proactively collect information to fulfill future requirements. For embedded onboarding, include the collectionOptions attribute in the embedded onboarding component. For Stripe-hosted onboarding, specify the collection_options parameter when creating account links.

Based on the verification needs of your application, send the user back into Connect Onboarding as necessary to satisfy currently_due or eventually_due requirements as described in step 1. You can use this as a signal of when to send your user back into the flow. Keep in mind that using Connect Onboarding means you don’t really need to worry about what the requirements are – sending the user back into Connect Onboarding means it will collect the right information.

For example, if your user mistypes their information and they can’t be verified, they could be asked to provide an Identity Document (for example, a Driver’s License in the United States). Sending this user into Connect Onboarding prompts them to upload such a document to ensure they become verified.

NoteConnect Onboarding for Custom Accounts doesn’t collect the external_account requirement by default. To collect external_account, enable Collect bank account information for payouts in your Connect Custom settings. Learn more about managing bank accounts and debit cards.

[Handle the case of user-initiated updates](#user-updates)Most Connect Onboarding usage discussed thus far has been about prompting the user to provide new information. Connect Onboarding also supports user-initiated updates to the information they’ve already provided in the type parameter of the Account Link. type accepts one of two values: account_onboarding or account_update.

account_onboarding![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

This value for type provides a form for inputting outstanding requirements. Use it when you’re onboarding a new user, or when an existing user has new requirements; such as when a user had already provided enough information, but you requested a new capability that needs additional info. Send the user to the form in this mode to just collect the new information you need.

account_update![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

This value for type displays the attributes that are already populated on the account object and allows your user to edit previously provided information. Provide an access point in your platform website to a type=account_update Account Link for users to make updates themselves (for example, when their address changes). Consider framing the link as “edit my profile” or “update my verification information.”

## Supported browsers

Hosted onboarding supports the same set of browsers that the Stripe Dashboard currently supports:

- The last 20 major versions of Chrome and Firefox
- The last two major versions of Safari and Edge
- The last two major versions of mobile Safari on iOS

Hosted onboarding isn’t supported when embedded through webviews. It’s only supported in standalone browsers.

## See also

- [Identity verification](/connect/identity-verification)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[How to use Connect Onboarding for Custom Accounts](#how-to-use-connect-onboarding-for-custom-accounts)[Determine the information to collect](#info-to-collect)[Redirect your user to the Account Link URL](#redirect)[Handle the user returning to your platform](#return)[Handle the case of new requirements becoming due](#new-reqs-due)[Handle the case of user-initiated updates](#user-updates)[Supported browsers](#supported-browsers)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`