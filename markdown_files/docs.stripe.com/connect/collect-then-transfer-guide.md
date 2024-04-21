htmlCollect payments then pay out | Stripe Documentation[Skip to content](#main-content)Collect payments then pay out[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fcollect-then-transfer-guide)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fcollect-then-transfer-guide)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Collect payments then pay out

Collect payments from customers and pay them out to sellers or service providers.WebiOSAndroidReact NativeNo codeThis guide explains how to accept payments and move funds to the bank accounts of your service providers or sellers. For demonstration purposes, we’ll build a home-rental marketplace that connects homeowners to potential tenants. We’ll also show you how to accept payments from tenants (customers) and pay out homeowners (your platform’s users).

## Prerequisites

1. [Register your platform](https://dashboard.stripe.com/connect/tasklist).
2. Add business details to[activate your account](https://dashboard.stripe.com/account/onboarding).
3. [Complete your platform profile](https://dashboard.stripe.com/connect/settings/profile).
4. [Customize your brand settings](https://dashboard.stripe.com/settings/connect). (Stripe-hosted onboarding only) Add a business name, icon, and brand color.

[Set up StripeServer-side](#setup)Install Stripe’s official libraries to access the API from your application:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`[Create a connected account](#create-account)When a user (seller or service provider) signs up on your marketplace, you must create a corresponding user Account (referred to as a connected account). You can’t accept payments and move funds to the bank account of your user without a connected account. Connected accounts represent your users in the Stripe API and collect the information required to verify the user’s identity. In our home-rental example, the connected account represents the homeowner.

### Create an Express connected account and prefill information

Use the /v1/accounts API to create an Express account and set type to express in the account creation request.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d type=express`If you’ve already collected information for your connected accounts, you can prefill that information on the account object. You can prefill any account information, including personal and business information, external account information, and so on.

Connect Onboarding doesn’t ask for the prefilled information. However, it does ask the account holder to confirm the prefilled information before accepting the Connect service agreement.

When testing your integration, prefill account information using test data.

### Create an account link

You can create an account link by calling the Account Links API with the following parameters:

- `account`
- `refresh_url`
- `return_url`
- `type`=`account_onboarding`

Command Line[curl](#)`curl https://api.stripe.com/v1/account_links \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d account={{CONNECTED_ACCOUNT_ID}} \
  --data-urlencode refresh_url="https://example.com/reauth" \
  --data-urlencode return_url="https://example.com/return" \
  -d type=account_onboarding`### Redirect your user to the account link URL

The response to your Account Links request includes a value for the key url. Redirect to this link to send your user into the flow. URLs from the Account Links API are temporary and are single-use only, because they grant access to the connected account user’s personal information. Authenticate the user in your application before redirecting them to this URL. If you want to prefill information, you must do so before generating the account link. After you create the account link, you can’t read or write information for the connected account.

Security tipDon’t email, text, or otherwise send account link URLs outside of your platform application. Instead, provide them to the authenticated account holder within your application.

### Handle the user returning to your platform

Connect Onboarding requires you to pass both a return_url and refresh_url to handle all cases where the user is redirected to your platform. It’s important that you implement these correctly to provide the best experience for your user.

NoteYou can use HTTP for your return_url and refresh_url while in test mode (for example, to test with localhost), but live mode only accepts HTTPS. Be sure to swap testing URLs for HTTPS URLs before going live.

return_url![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Stripe issues a redirect to this URL when the user completes the Connect Onboarding flow. This doesn’t mean that all information has been collected or that there are no outstanding requirements on the account. This only means the flow was entered and exited properly.

No state is passed through this URL. After a user is redirected to your return_url, check the state of the details_submitted parameter on their account by doing either of the following:

- Listening to`account.updated`webhooks
- Calling the[Accounts](/api/accounts)API and inspecting the returned object

refresh_url![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Stripe redirects your user to the refresh_url in these cases:

- The link is expired (a few minutes went by since the link was created).
- The user already visited the URL (the user refreshed the page or clicked back or forward in the browser).
- Your platform is no longer able to access the account.
- The account has been rejected.

Your refresh_url should trigger a method on your server to call Account Links again with the same parameters, and redirect the user to the Connect Onboarding flow to create a seamless experience.

### Handle users that haven’t completed onboarding

A user that’s redirected to your return_url might not have completed the onboarding process. Use the /v1/accounts endpoint to retrieve the user’s account and check for charges_enabled. If the account isn’t fully onboarded, provide UI prompts to allow the user to continue onboarding later. The user can complete their account activation through a new account link (generated by your integration). You can check the state of the details_submitted parameter on their account to see if they’ve completed the onboarding process.

[Enable payment methods](#enable-payment-methods)View your payment methods settings and enable the payment methods you want to support. Card payments, Google Pay, and Apple Pay are enabled by default but you can enable and disable payment methods as needed.

Before the payment form is displayed, Stripe evaluates the currency, payment method restrictions, and other parameters to determine the list of supported payment methods. Payment methods that increase conversion and that are most relevant to the currency and customer’s location are prioritized. Lower priority payment methods are hidden in an overflow menu.

[Accept a payment](#accept-payment)Use Stripe Checkout to accept payments. Checkout supports multiple payment methods and automatically shows the most relevant ones to your customer. You can accept payments with Checkout using a Stripe-hosted page or add a prebuilt embeddable payment form directly in your website. You can also create a custom flow (using Payment Element) to accept multiple payment methods with a single front-end integration.

Stripe-hosted pageEmbedded formCustom flow### Create a Checkout Session Client and Server

A Checkout Session controls what your customer sees in the Stripe-hosted payment page such as line items, the order amount and currency, and acceptable payment methods.

Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

checkout.html`<html>
  <head>
    <title>Checkout</title>
  </head>
  <body>
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>`On your server, make the following call to Stripe’s API. After creating a Checkout Session, redirect your customer to the URL returned in the response.

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d mode=payment \
  -d "line_items[0][price]"={{PRICE_ID}} \
  -d "line_items[0][quantity]"=1 \
  -d "payment_intent_data[application_fee_amount]"=123 \
  -d "payment_intent_data[transfer_data][destination]"={{CONNECTED_ACCOUNT_ID}} \
  --data-urlencode success_url="https://example.com/success" \
  --data-urlencode cancel_url="https://example.com/cancel"`- `line_items`- This argument represents the items the customer is purchasing. The items are displayed in the Stripe-hosted user interface.
- `success_url`- This argument redirects a user after they complete a payment.
- `cancel_url`- This argument redirects a user after they click cancel.
- `payment_intent_data[application_fee_amount]`- This argument specifies the amount your platform plans to take from the transaction. The full charge amount is immediately transferred from the platform to the connected account that’s specified by`transfer_data[destination]`after the charge is captured. The`application_fee_amount`is then transferred back to the platform, and the Stripe fee is deducted from the platform’s amount.
- `payment_intent_data[transfer_data][destination]`- This argument indicates that this is a[destination charge](/connect/destination-charges). A destination charge means the charge is processed on the platform and then the funds are immediately and automatically transferred to the connected account’s pending balance. For our home-rental example, we want to build an experience where the customer pays through the platform and the homeowner gets paid by the platform.

![](https://b.stripecdn.com/docs-statics-srv/assets/application_fee_amount.837aa2339469b3c1a4319672971c1367.svg)

Checkout uses the brand settings of your platform account for destination charges. For more information, see Customize branding.

This Session creates a destination charge. If you need to control the timing of transfers or need to transfer funds from a single payment to multiple parties, use separate charges and transfers instead. To use separate charges, see Enable other businesses to accept payments directly.

### Handle post-payment events  Server-side

Stripe sends a checkout.session.completed event when the payment completes. Use a webhook to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes. Some payment methods also take 2-14 days for payment confirmation. Setting up your integration to listen for asynchronous events enables you to accept multiple payment methods with a single integration.

In addition to handling the checkout.session.completed event, we recommend handling two other events when collecting payments with Checkout:

EventDescriptionNext steps[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)The customer has successfully authorized the payment by submitting the Checkout form.Wait for the payment to succeed or fail.[checkout.session.async_payment_succeeded](/api/events/types#event_types-checkout.session.async_payment_succeeded)The customer’s payment succeeded.Fulfill the purchased goods or services.[checkout.session.async_payment_failed](/api/events/types#event_types-checkout.session.async_payment_failed)The payment was declined, or failed for some other reason.Contact the customer through email and request that they place a new order.These events all include the Checkout Session object. After the payment succeeds, the underlying PaymentIntent status changes from processing to succeeded.

[Testing](#testing)Test your account creation flow by creating accounts and using OAuth.

CardsWalletsBank redirectsBank debitsVouchersCard numberScenarioHow to test4242424242424242The card payment succeeds and doesn’t require authentication.Fill out the credit card form using the credit card number with any expiration, CVC, and postal code.4000002500003155The card payment requires[authentication](/strong-customer-authentication).Fill out the credit card form using the credit card number with any expiration, CVC, and postal code.4000000000009995The card is declined with a decline code like`insufficient_funds`.Fill out the credit card form using the credit card number with any expiration, CVC, and postal code.6205500000000000004The UnionPay card has a variable length of 13-19 digits.Fill out the credit card form using the credit card number with any expiration, CVC, and postal code.See Testing for additional information to test your integration.

## Disputes

As the settlement merchant on charges, your platform is responsible for disputes. Make sure you understand the best practices for responding to disputes.

## Payouts

By default, any funds that you transfer to a connected account accumulate in the connected account’s Stripe balance and are paid out on a daily rolling basis. You can change the payout frequency by going into the connected account’s detail page, clicking the right-most button in the Balance section, and selecting Edit payout schedule.

## Refunds

To issue refunds, go to the Payments page. Select individual payments by clicking the checkbox to the left of any payments you want to refund. After you select a payment, Stripe displays a Refund button in the upper-right corner of the page. Click the Refund button to issue a refund to customers for all payments you have selected.

NoteConnected accounts can’t initiate refunds for payments from the Express Dashboard. If your connected accounts use the Express Dashboard, you must process refunds for them.

## See also

- [Manage connected accounts in the Dashboard](/connect/dashboard)
- [Issue refunds](/connect/direct-charges#issue-refunds)
- [Customize statement descriptors](/connect/statement-descriptors)
- [Work with multiple currencies](/connect/currencies)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Prerequisites](#prerequisites)[Set up Stripe](#setup)[Create a connected account](#create-account)[Enable payment methods](#enable-payment-methods)[Accept a payment](#accept-payment)[Testing](#testing)[Disputes](#disputes)[Payouts](#payouts)[Refunds](#refunds)[See also](#see-also)Products Used[Connect](/connect)[Checkout](/payments/checkout)[Payment Links](/payments/payment-links)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`