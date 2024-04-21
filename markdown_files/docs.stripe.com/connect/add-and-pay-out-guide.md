htmlPay out money | Stripe Documentation[Skip to content](#main-content)Pay out money[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fadd-and-pay-out-guide)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fadd-and-pay-out-guide)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Pay out money

Add money to your Stripe balance and pay out your sellers or service providers.NoteMost platforms can pay out funds only to connected accounts in the same region and in local currencies. Platforms based in the US can make cross-border payouts to accounts in other regions, subject to restrictions.

APINo codeUse this guide to learn how to add funds to your account balance and transfer the funds into your users’ bank accounts, without processing payments through Stripe. This guide uses an example of a Q&A product that pays its writers a portion of the advertising revenue that their answers generate. The platform and connected accounts are both in the US.

NoteOnly team members with administrator access to the platform Stripe account and two-factor authentication enabled can add funds.

When adding funds to your balance, best practice is to use a manual payout schedule. If you enable automatic payouts, you can’t control whether the system uses added funds for payouts. You can configure your schedule in your payout settings.

## Prerequisites

1. [Register your platform](https://dashboard.stripe.com/connect/tasklist).
2. Add business details to[activate your account](https://dashboard.stripe.com/account/onboarding).
3. [Complete your platform profile](https://dashboard.stripe.com/connect/settings/profile).
4. [Customize your brand settings](https://dashboard.stripe.com/settings/connect). (Stripe-hosted onboarding only) Add a business name, icon, and brand color.

[Set up StripeServer-side](#with-code-setup)Install Stripe’s official libraries so you can access the API from your application:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`[Create a connected account](#with-code-create-connected-account)When a user (seller or service provider) signs up on your platform, create a user Account (referred to as a connected account) so you can accept payments and move funds to their bank account. Connected accounts represent your users in Stripe’s API and facilitate the collection of information requirements so Stripe can verify the user’s identity. For a Q&A product that pays for answers, the connected account represents the writer.

NoteThis guide uses Express accounts which have certain restrictions. You can evaluate Custom accounts as an alternative.

### 1. Customize your signup form

In your platform settings, customize your Express signup form by changing the color and logos that users see when they click your Connect link.

![](https://b.stripecdn.com/docs-statics-srv/assets/oauth-form.4b13fc5edc56abd16004b4ccdff27fb6.png)

Default Express signup form

![](https://b.stripecdn.com/docs-statics-srv/assets/branding-settings-payouts.20c99c810389a4e7f5c55238e80a9fc8.png)

Branding settings

### 2. Create an Express connected account and prefill information

Use the /v1/accounts API to create an Express account and set type to express in the account creation request.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d type=express`If you’ve already collected information for your connected accounts, you can prefill that information on the account object. You can prefill any account information, including personal and business information, external account information, and so on.

Connect Onboarding doesn’t ask for the prefilled information. However, it does ask the account holder to confirm the prefilled information before accepting the Connect service agreement.

When testing your integration, prefill account information using test data.

### 3. Create an account link

Create an Account Link with the following arguments:

- `account`
- `refresh_url`
- `return_url`
- `type`=`account_onboarding`

Command Line[curl](#)`curl https://api.stripe.com/v1/account_links \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d account={{CONNECTED_ACCOUNT_ID}} \
  --data-urlencode refresh_url="https://example.com/reauth" \
  --data-urlencode return_url="https://example.com/return" \
  -d type=account_onboarding`### 4. Redirect your user to the account link

The response to your Account Links request includes a value for the key url. Redirect your user to this link. URLs from the Account Links API are temporary and can be used only once because they grant access to the account holder’s personal information. Authenticate the user in your application before redirecting them to this URL. If you want to prefill information, you must do so before generating the account link. After you create the account link, you won’t be able to read or write information for the connected account.

Security tipDon’t email, text, or otherwise send account link URLs outside of your platform application. Instead, provide them to the authenticated account holder within your application.

### 5. Handle the user returning to your platform

Connect Onboarding requires you to pass both a return_url and refresh_url to handle all cases where the user is redirected to your platform. It’s important that you implement these correctly to provide the best experience for your user.

NoteYou can use HTTP for your return_url and refresh_url while in test mode (for example, to test with localhost), but live mode only accepts HTTPS. Be sure to update testing URLs to HTTPS URLs before going live.

return_url![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Stripe issues a redirect to this URL when the user completes the Connect Onboarding flow. This doesn’t mean that all information has been collected or that there are no outstanding requirements on the account. This only means the flow was entered and exited properly.

No state is passed through this URL. After a user is redirected to your return_url, check the state of the details_submitted parameter on their account by doing either of the following:

- Listening to`account.updated`events.
- Calling the[Accounts](/api/accounts)API and inspecting the returned object.

refresh_url![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Your user is redirected to the refresh_url when:

- The link has expired (a few minutes have passed since the link was created).
- The link was already visited (the user refreshed the page or clicked back or forward in their browser).
- The link was shared in a third-party application such as a messaging client that attempts to access the URL to preview it. Many clients automatically visit links which cause them to become expired.
- Your platform is no longer able to access the account.
- The account has been rejected.

The refresh_url should call Account Links again on your server with the same parameters and redirect the user to the Connect Onboarding flow to create a seamless experience.

### 6. Handle users that haven’t completed onboarding

A user that’s redirected to your return_url might not have completed the onboarding process. Use the /v1/accounts endpoint to retrieve the user’s account and check for charges_enabled. If the account is not fully onboarded, provide UI prompts to allow the user to continue onboarding later. The user can complete their account activation through a new account link (generated by your integration). You can check the state of the details_submitted parameter on their account to see if they’ve completed the onboarding process.

[Add funds to your balance](#with-code-add-funds)To add funds, go to the Balance section in the Dashboard. Click Add to balance and select why you are adding funds to your account.

![](https://b.stripecdn.com/docs-statics-srv/assets/add_funds_modal_with_issuing.f3dc58497698fb2a62b6461b7ed4fba6.png)

Select Pay out connected accounts to add funds to pay out to your connected accounts. If you are adding funds to your balance to cover future refunds and disputes, or to repay your platform’s negative balance, select Cover negative balances and see adding funds to your Stripe balance.

### Verify your bank account

Go through the verification process in the Dashboard when you first attempt to add funds from an unverified bank account. If your bank account is unverified, you’ll need to confirm two microdeposits from Stripe. These deposits appear in your online banking statement within 1-2 business days. You’ll see ACCTVERIFY as the statement description.

Stripe notifies you in the Dashboard and through email when the microdeposits have arrived in your account. To complete the verification process, click the Dashboard notification in the Balance section, enter the two microdeposit amounts, and click Verify account.

![](https://b.stripecdn.com/docs-statics-srv/assets/top-ups4.85d1f2d8440f525714d0f2d20775e2d1.png)

### Create a top-up

Once verified, create a top-up to add funds to your account balance.

Command Line[curl](#)`curl https://api.stripe.com/v1/topups \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=2000 \
  -d currency=usd \
  -d description="Top-up for week of May 31" \
  -d statement_descriptor="Weekly top-up"`When you transfer funds, a statement descriptor appears on your banking statement for the transaction. The default statement descriptor is Top-up. You can customize the statement descriptor and internal description for the top-up.

### View funds

View your funds in the Dashboard on Top-ups tab under the Balance page. Each time you add funds, a top-up object is made that has a unique ID in the format tu_XXXXXX, which you can see on the detailed view for the top-up.

### Settlement timing

US platforms add funds via ACH debit and can take 5-6 business days to become available in your Stripe balance. You can request a review of your account for faster settlement timing by contacting Stripe Support.

As we learn more about your account, Stripe might be able to decrease your settlement timing automatically.

Adding funds for future refunds and disputes or to repay a negative balance can happen through bank or wire transfers and are available in 1-2 business days.

[Pay out to your userServer-side](#with-code-pay-out-to-user)You can transfer available funds to a connected account using the API. For example, make the following call to transfer 10 USD to an account:

Command Line[curl](#)`curl https://api.stripe.com/v1/transfers \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d amount=1000 \
  -d currency="usd" \
  -d destination="{{CONNECTED_STRIPE_ACCOUNT_ID}}"`By default, any funds that you transfer to a connected account accumulates in the connected account’s Stripe balance and is paid out on a daily rolling basis. You can change the payout schedule as needed.

[Test your integration](#with-code-testing)From your account Dashboard, you can view an account and its balance.

![](https://b.stripecdn.com/docs-statics-srv/assets/dashboard-account-payout.94e15f1be4a11a54d18fc305433e50f4.png)

Use the test bank tokens to simulate flows for accounts and onboarding, payouts, and adding funds.

## See also

- [Collect payments then pay out](/connect/collect-then-transfer-guide)
- [Manage connected accounts in the Dashboard](/connect/dashboard)
- [Debit a connected account](/connect/account-debits)
- [Integrate with the Express Dashboard](/connect/express-dashboard)
- [Collect information required for US taxes](/connect/account-capabilities#tax-reporting)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Prerequisites](#prerequisites)[Set up Stripe](#with-code-setup)[Create a connected account](#with-code-create-connected-account)[Add funds to your balance](#with-code-add-funds)[Pay out to your user](#with-code-pay-out-to-user)[Test your integration](#with-code-testing)[See also](#with-code-see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`