htmlExample applications | Stripe Documentation[Skip to content](#main-content)Example applications[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fexample-applications)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fexample-applications)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)# Example applications

Try Stripe Terminal by using the example applications and simulated reader.NoteFor a more immersive guide, check out the sample integration.

A Stripe Terminal integration starts with your point of sale application running at a physical location. Your point of sale application communicates with a reader through the Terminal SDK to collect in-person payments from your customers. Your backend works with your point of sale application to authenticate the Terminal SDK and finalize payments.

![](https://b.stripecdn.com/docs-statics-srv/assets/example-app-simulator-integration-architecture.c687f5119cda8972233e61f684ae56a5.png)

Before starting your own integration, we recommend setting up one of the Terminal example applications. This will give you a better feel for how the components of a Terminal integration fit together and show you the interactions between the SDK, the reader, your point of sale application, and your backend code.

[Deploy the example backend](#set-up-backend)To get started with the example applications, set up the Sinatra-based example backend by following the instructions in the README. You can either run the backend locally or deploy it to Render with a free account. The example backend works with the example application to authenticate the Terminal SDK and finalize payments.

[Run the example application](#run-example-app)Build and run one of the example applications:

JavaScriptiOSAndroidReact Native1. Clone the example from[GitHub](https://github.com/stripe/stripe-terminal-js-demo):

Command Line`git clone https://github.com/stripe/stripe-terminal-js-demo.git`1. Run the following commands to run the example:

Command Line`cd stripe-terminal-js-demo
npm install
npm run start`1. In the running example, enter the URL of the example backend that you deployed in[step 1](#set-up-backend).

[Connect to a simulated reader](#connect-simulated-reader)JavaScriptiOSAndroidReact NativeAfter you have the example running, select Use simulator to connect to a simulated reader.

![](https://b.stripecdn.com/docs-statics-srv/assets/js-example-app-simulator.c226b6ba5461d0c5b3b8f06c0c1a3469.png)

The JavaScript example app connected to a simulated reader

The simulated reader handles events just like a physical reader, so you can continue to collecting your first payment.

The simulated reader functionality is built into the SDK, so you can use it to develop and test your own point of sale application without connecting to a physical device.

[Collect your first payment](#collect-payment)Collect your first payment using the example application and a simulated reader. Each of the examples features an event log for you to reference as you integrate Terminal in your own application. As you collect your first payment, you’ll see the following sequence:

- Create payment: The example application collects a payment method using the SDK.
- Collect payment method: The simulated reader receives a card.
- Process and capture: The example application and backend finalize the payment.

Note(Optional) Use separate authorization and capture to add a reconciliation step before finalizing the transaction. You can also automatically capture Terminal transactions.

JavaScriptiOSAndroidReact Native![Javascript example app connected to simulated reader](https://b.stripecdn.com/docs-statics-srv/assets/js-example-app-payment.8069a69561566519d001038a46bfe6b5.png)

Collecting a payment, using the JavaScript example app and a simulated reader

## Next steps

- [Design an integration](/terminal/designing-integration)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Deploy the example backend](#set-up-backend)[Run the example application](#run-example-app)[Connect to a simulated reader](#connect-simulated-reader)[Collect your first payment](#collect-payment)[See also](#next-steps)Products Used[Terminal](/terminal)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`