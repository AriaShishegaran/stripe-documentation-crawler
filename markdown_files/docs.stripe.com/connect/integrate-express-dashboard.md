htmlIntegrate the Express Dashboard | Stripe Documentation[Skip to content](#main-content)Integrate the Express Dashboard[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fintegrate-express-dashboard)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fintegrate-express-dashboard)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Express Dashboard](/docs/connect/express-dashboard)# Integrate the Express Dashboard

Learn how to direct your users to their Express Dashboard from your platform.The Express Dashboard allows users (connected accounts) to view their available balance, see upcoming payouts, and track their earnings in real time. In this guide, you’ll learn how to redirect users to the Express Dashboard from your platform.

Users can log into the Express Dashboard by clicking a link on the user interface of your website or mobile application. After they click the link, Stripe redirects your users to the Express Dashboard login page. On the login page, users must verify their identity through SMS authentication to view and manage their Express Dashboard.

NoteYour onboarded users can also access the Express Dashboard by signing in to Stripe Express. However, we recommend providing users a link to the Express Dashboard from your platform.

[Create a login link](#create-login-link)Use the Login Link API to generate a single-use URL. This URL takes users to the Express Dashboard login page.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/login_links \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`When the request successfully completes, the response includes a generated login URL:

`{
  "object": "login_link",
  "created": 1495580507,
  "url": "https://stripe.com/express/Ln7FfnNpUcCU"
}`Typically, you’ll use the API to generate the URL on demand (when a user intends to visit the Express Dashboard). If users click a call to action on your application, your application creates a URL using the Login Link API and redirects them to the Express Dashboard with the URL returned by the API.

WarningDon’t email, text, or otherwise send login link URLs directly to your user. Instead, redirect the authenticated user to the login link URL from within your platform’s application.

On the login page, users must enter an SMS authentication code (automatically sent from Stripe) to view their Express Dashboard. Stripe uses SMS authentication to verify a user’s identity and grant access to their Express Dashboard.

NoteIf a user no longer has access to the original phone number your platform used to create their Express Account, they can change their phone number by clicking “I no longer have access to this phone number”. Then, the user can retrieve a verification code sent to their Express Account email. The user must submit this code to add a new mobile number. Stripe redirects the user back to the login page and sends an SMS authentication code to the new number.

## See also

- [Customize the Express Dashboard](/connect/customize-express-dashboard)
- [Collect payments and then pay out](/connect/collect-then-transfer-guide)(if you process payments with Stripe)
- [Pay out money](/connect/add-and-pay-out-guide)(if you add money from a bank account to pay out)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a login link](#create-login-link)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`