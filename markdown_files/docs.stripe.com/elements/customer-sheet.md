htmlIntegrate the Customer Sheet | Stripe Documentation[Skip to content](#main-content)Customer Sheet[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Felements%2Fcustomer-sheet)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Felements%2Fcustomer-sheet)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)
Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[Mobile Elements](/docs/payments/mobile)# Integrate the Customer Sheet

Offer a prebuilt UI for your customers to manage their saved payment methods.iOSAndroidReact NativeBetaThis feature is currently in beta for Android.

The Customer Sheet is a prebuilt UI component that lets your customers manage their saved payment methods. It has a flexible architecture that supports advanced use cases and allows you to customize the underlying behavior. You can use the Customer Sheet UI outside of a checkout flow, and the appearance and styling is customizable to match the appearance and aesthetic of your app. Customers can add and remove payment methods, which get saved to the customer object, and set their default payment method stored locally on the device. Use both Mobile Payment Element and Customer Sheet to provide customers a consistent end-to-end solution for saved payment methods.

![Screenshot of Customer Sheet presenting multiple saved payment methods in an iOS app.](https://b.stripecdn.com/docs-statics-srv/assets/ios-landing.6c4969968fd6efe3d39fe673628f8284.png)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`