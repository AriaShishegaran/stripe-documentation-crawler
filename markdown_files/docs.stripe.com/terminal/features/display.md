htmlDisplay cart details | Stripe Documentation[Skip to content](#main-content)Cart display[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Fdisplay)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Fdisplay)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)# Display cart details

Dynamically update cart details on the reader screen.The built-in screen of the Verifone P400,  BBPOS WisePOS E and Stripe Reader S700 can display line items. During the checkout process, you can update the reader’s screen to show individual items in the transaction, along with the total price.

![Cart details](https://b.stripecdn.com/docs-statics-srv/assets/wpe-darkmode-display.7ef124617c921eb0051fc480e9b450cb.png)

Cart details screen

## Set the reader display

### SDK Reference

- [setReaderDisplay (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)setReaderDisplay:completion:)
- [setReaderDisplay (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/set-reader-display.html)
- [setReaderDisplay (JavaScript)](/terminal/references/api/js-sdk#set-reader-display)
- [setReaderDisplay (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#setReaderDisplay)

To set the line items and total displayed on the reader during a payment, pass line items and total information into the setReaderDisplay method. The object you pass in will drive the contents displayed on the reader’s screen.

The amounts passed to the setReaderDisplay method are only used for display purposes. The reader won’t automatically calculate tax or the total—your application must calculate the tax and total before displaying the values. You can use the Stripe Tax API to calculate taxes. Similarly, the total passed to setReaderDisplay doesn’t control the amount charged to the customer. Make sure the amount displayed on the reader matches the amount you’re charging your customer.

Server-drivenJavaScriptiOSAndroidReact NativeCommand Line[curl](#)`curl https://api.stripe.com/v1/terminal/readers/tmr_xxx/set_reader_display \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d type=cart \
  -d "cart[line_items][0][description]"="Caramel latte" \
  -d "cart[line_items][0][amount]"=659 \
  -d "cart[line_items][0][quantity]"=1 \
  -d "cart[line_items][1][description]"="Dozen donuts" \
  -d "cart[line_items][1][amount]"=1239 \
  -d "cart[line_items][1][quantity]"=1 \
  -d "cart[currency]"=usd \
  -d "cart[tax]"=100 \
  -d "cart[total]"=1998`To clear reader display on the server-driven integration, call the cancel_action endpoint.

## Pre-dip a card

NotePre-dipping a card is only supported for payments in the US.

The Verifone P400, BBPOS WisePOS E, and Stripe Reader S700 support the ability to present a card to the reader before the transaction amount is finalized.

This option—known as pre-dip, pre-tap, or pre-swipe—can help speed up transaction times by allowing a customer to present a payment method before the end of the transaction.

The setReaderDisplay method prepares the reader for pre-dipping. The customer can present a payment method at any point after the method is called.

Even if a customer pre-dips their card, your application must still complete the full payment flow.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set the reader display](#set-the-reader-display)[Pre-dip a card](#pre-dip-a-card)Products Used[Terminal](/terminal)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`