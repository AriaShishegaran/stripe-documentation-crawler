htmlMaking API calls for connected accounts | Stripe Documentation[Skip to content](#main-content)Make API calls for connected accounts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fauthentication)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fauthentication)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Making API calls for connected accounts

Learn how to add the right information to your API calls so you can make calls for your connected accounts.You can make API calls for your connected accounts:

- Server-side with the[Stripe-Account header](#stripe-account-header)and the connected account ID, per request
- Client-side by passing the connected account ID as an argument to the client library

To optimize performance and reliability, Stripe has established rate limits and allocations for API endpoints.

## Adding the Stripe-Account header server-side

For server-side API calls, you can make requests as connected accounts using the special header Stripe-Account with the Stripe account identifier (it starts with the prefix acct_) of your platform user. Here’s an example that shows how to Create a PaymentIntent with your platform’s API secret key and your user’s Account identifier.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d amount=1000 \
  -d currency=usd \
  -d "automatic_payment_methods[enabled]"=true`In the latest version of the API, specifying the automatic_payment_methods parameter is optional because Stripe enables its functionality by default.

The Stripe-Account header approach is implied in any API request that includes the Stripe account ID in the URL. Here’s an example that shows how to Retrieve an account with your user’s Account identifier in the URL.

Command Line[curl](#)`curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`All of Stripe’s server-side libraries support this approach on a per-request basis:

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  --data-urlencode email="person@example.com"`## Adding the connected account ID to a client-side application

Client-side libraries set the connected account ID as an argument to the client application:

HTML + JSReactiOSAndroidReact NativeThe JavaScript code for passing the connected account ID client-side is the same for plain JS and for ESNext.

`var stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY', {
  stripeAccount: {{CONNECTED_ACCOUNT_ID}},
});`## See also

- [Creating charges](/connect/charges)
- [Using subscriptions](/connect/subscriptions)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Adding the Stripe-Account header server-side](#stripe-account-header)[Adding the connected account ID to a client-side application](#adding-the-connected-account-id-to-a-client-side-application)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`