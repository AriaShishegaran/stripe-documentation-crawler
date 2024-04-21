htmlExpress Checkout Element | Stripe Documentation[Skip to content](#main-content)Express Checkout Element[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Felements%2Fexpress-checkout-element)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Felements%2Fexpress-checkout-element)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)
[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Elements](/payments/elements)·[Home](/docs)[Payments](/docs/payments)[Web Elements](/docs/payments/elements)# Express Checkout Element

Show multiple one-click payment buttons with a single component.![Add Link to the Express Checkout Element](https://b.stripecdn.com/docs-statics-srv/assets/link-in-express-checkout-element.67be6745e5a37c1c09074b0f43763cff.png)

The Express Checkout Element gives you a single integration for accepting payments through one-click payment buttons. Supported payment methods include Link, Apple Pay, Google Pay, PayPal, and Amazon Pay.

With this integration, you can:

- Dynamically sort payment buttons based on a customer’s location.
- Add payment buttons without any frontend changes.
- Integrate Elements seamlessly by reusing an existing Elements instance to save time.

[Try the demo](#try-demo)In the following demo, you can toggle some of the prebuilt options to change the background color, layout, size, and shipping address collection of the payment interface. The demo displays Google Pay and Apple Pay only on their available platforms. Payment Method buttons are only shown in their supported countries.

If you don’t see the demo, try viewing this page in a supported browser.

[Start with a guide](#start-with-guide)[Accept a paymentBuild an integration with the Express Checkout Element.](/elements/express-checkout-element/accept-a-payment)[Migrate to the Express Checkout ElementMigrate from the Payment Request Button Element to the web Express Checkout Element.](/elements/express-checkout-element/migration)[View the Stripe.js reference](/docs/js/element/express_checkout_element)## Create an Express Checkout Element

This code creates an elements group with an Express Checkout Element and mounts it to the DOM.

`const appearance = { /* appearance */ }
const options = { /* options */ }
const elements = stripe.elements({
  mode: 'payment',
  amount: 1099,
  currency: 'usd',
  appearance,
})
const expressCheckoutElement = elements.create('expressCheckout', options)
expressCheckoutElement.mount('#express-checkout-element')`## Payment methods

The Express Checkout Element presents one-click payment methods that are active, supported, and set up.

- Some payment methods[require activation in the Dashboard](https://dashboard.stripe.com/settings/connect/payment_methods).
- Payment methods are only available when the customer uses a supported browser and pays in a supported currency.
- Some payment methods require setup actions from the customer. For example, a customer won’t see a Google Pay button if they don’t have Google Pay set up.

The element sorts payment methods by relevance to your customer.

To control these behaviors, you can customize the payment methods.

## Supported browsers

Certain payment methods work with specific browsers.

Apple PayGoogle PayLinkPayPalAmazon PayChrome1EdgeFirefoxOperaSafari2Chrome and Firefox on iOS 16+Edge on iOS 16+1Other chromium browsers might be supported. For more information, see supported browsers. 2When using an iframe, its origin must match the top-level origin (except for Safari 17 when specifying allow="payment" attribute). Two pages have the same origin if the protocol, host (full domain name), and port (if specified) are the same for both pages.

## Layout

By default, when the Express Checkout Element displays multiple buttons, it arranges the buttons in a grid based on available space, and shows an overflow menu if necessary.

You can override this default and specify a grid layout yourself with the layout option.

## Text

You can control a button’s text by selecting a buttonType. Each wallet offers its own types.

LinkApple PayGoogle PayPayPalAmazon PayLink only offers one button type, with the “Pay faster” call to action.

We attempt to detect your customer’s locale and use it to localize the button text. You can also specify a locale.

This example code includes the call to action “Buy” or “Buy now” for buttons that support it. Then, it specifies the locale de to get their German equivalents.

`const expressCheckoutOptions = {
  buttonType: {
    applePay: 'buy',
    googlePay: 'buy',
    paypal: 'buynow'
  }
}
const elements = stripe.elements({
  locale: 'de',
  mode: 'payment',`See all 18 lines## Appearance

You can’t fully customize the appearance of Express Checkout Element buttons because each payment method sets its own logo and brand colors. You can customize the following options:

- [Button height](/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-buttonHeight)
- Border radius using variables with the[Appearance](/elements/appearance-api)API
- [Button themes](/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-buttonTheme)

This example code sets up an elements group with a light theme and 36px border radius, makes buttons 50px tall, and overrides the theme to use the white-outline version of the Apple Pay button.

`const appearance = {
  theme: 'stripe',
  variables: {
    borderRadius: '36px',
  }
}
const expressCheckoutOptions = {
  buttonHeight: '50',
  buttonTheme: {`See all 23 linesWe support the following themes:

LinkPayPalApple PayGoogle PayAmazon PayLink has a single button theme, which is readable on either a light or a dark background.

## Customize payment methods

You can’t specify which payment methods to display. For example, you can’t force a Google Pay button to appear if your customer’s device doesn’t support Google Pay.

But you can customize payment method behavior in various ways, such as:

- You can activate or deactivate payment methods from the[Dashboard](https://dashboard.stripe.com/settings/payment_methods).
- You can override Stripe’s default logic of sorting payment methods by relevance. Use the[paymentMethodOrder](/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-paymentMethodOrder)option to set your preferred order.
- If there is too little room in the layout, low-relevance payment methods might appear in an overflow menu. Customize when the menu appears using the[layout](/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-layout)option.
- To prevent Apple Pay or Google Pay from appearing, set[wallets.applePay](/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-wallets-applePay)or[wallets.googlePay](/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-wallets-applePay)to`never`.
- To allow Apple Pay or Google Pay to appear when they’re not set up, set[wallets.applePay](/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-wallets-applePay)or[wallets.googlePay](/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-wallets-applePay)to`always`. This still won’t force them to appear on unsupported platforms, or when the payment is in an unsupported currency.

Regional considerationsFinlandSwedenRegulations in Finland and Sweden require you to present debit payment methods first before showing credit payment methods at checkout in these countries.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Try the demo](#try-demo)[Start with a guide](#start-with-guide)[Create an Express Checkout Element](#create-an-express-checkout-element)[Payment methods](#payment-methods)[Supported browsers](#supported-browsers)[Layout](#layout)[Text](#text)[Appearance](#appearance)[Customize payment methods](#customize-payment-methods)Products Used[Payments](/payments)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`