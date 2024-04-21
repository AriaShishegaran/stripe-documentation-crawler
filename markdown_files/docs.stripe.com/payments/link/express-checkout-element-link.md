htmlLink in the Express Checkout Element | Stripe Documentation[Skip to content](#main-content)Link in the Express Checkout Element[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Flink%2Fexpress-checkout-element-link)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Flink%2Fexpress-checkout-element-link)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)
Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[Faster checkout with Link](/docs/payments/link)[Link with Web Elements](/docs/payments/link/elements-link)# Link in the Express Checkout Element

Let customers check out faster with Link and the Express Checkout Element.The Express Checkout Element gives you a single integration for accepting payments through one-click payment buttons. Supported payment methods include Link, Apple Pay, Google Pay, PayPal, and Amazon Pay.

With this integration, you can:

- Dynamically sort payment buttons based on a customer’s location.
- Add payment buttons without any frontend changes.
- Integrate Elements seamlessly by reusing an existing Elements instance to save time.

![Add Link to the Express Checkout Element](https://b.stripecdn.com/docs-statics-srv/assets/link-in-express-checkout-element.67be6745e5a37c1c09074b0f43763cff.png)

Add Link to the Express Checkout Element

## Create an Express Checkout Element

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
expressCheckoutElement.mount('#express-checkout-element')`## See also

- [Stripe Web Elements](/payments/elements)
- [Link Authentication Element](/payments/elements/link-authentication-element)
- [Address Element](/elements/address-element)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create an Express Checkout Element](#create-an-express-checkout-element)[See also](#see-also)Related Guides[Accept a payment with the Express Checkout Element](/docs/elements/express-checkout-element/accept-a-payment)Products Used[Payments](/payments)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`