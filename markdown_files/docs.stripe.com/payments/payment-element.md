htmlStripe Payment Element | Stripe Documentation[Skip to content](#main-content)Payment Element[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-element)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-element)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)
[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Elements](/payments/elements)·[Home](/docs)[Payments](/docs/payments)[Web Elements](/docs/payments/elements)# Stripe Payment Element

Accept payment methods from around the globe with a secure, embeddable UI component.Interested in using Stripe Tax, discounts, shipping, or currency conversion?We’re developing a Payment Element integration that manages tax, discounts, shipping, and currency conversion. Read the Build a checkout page guide to learn more.

The Payment Element is a UI component for the web that accepts 40+ payment methods, validates input, and handles errors. Use it alone or with other elements in your web app’s frontend.

Customer locationUnited States (USD)SizeDesktopThemeDefaultLayoutTabsThis demo only displays Google Pay or Apple Pay if you have an active card with either wallet.To try the Payment Element for yourself, start with one of these examples:

[QuickstartCode and instructions for accepting a payment using the Payment Element.](/payments/quickstart)[Clone a sample app on GitHubHTML · React · Vue](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)[API reference](/docs/js/element/payment_element)## Create a Payment Element

This code creates a Payment Element and mounts it to the DOM:

index.js[View full sample](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)`const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');

const appearance = { /* appearance */ };
const options = { /* options */ };
const elements = stripe.elements({ clientSecret, appearance });
const paymentElement = elements.create('payment', options);
paymentElement.mount('#payment-element');`Accepting payments with the Payment Element requires additional backend code. See the quickstart or sample app to learn how this works.

## Combine elements

The Payment Element interoperates with other elements. For instance, this form uses one additional element to autofill checkout details, and another to collect the shipping address.

![A form with contact info, shipping address, and payment fields. The contact info is labeled Link Authentication Element, the shipping address is labeled Address Element, and the payment fields are labeled Payment Element](https://b.stripecdn.com/docs-statics-srv/assets/link-with-elements.f60af275f69b6e6e73c766d1f9928457.png)

For the complete code for this Link example, see Add Link to an Elements integration.

## Payment methods

Stripe enables certain payment methods for you by default. We might also enable additional payment methods after notifying you. Use the Dashboard to enable or disable payment methods at any time. With the Payment Element, you can use Dynamic payment methods to:

- Manage payment methods in the[Dashboard](https://dashboard.stripe.com/settings/payment_methods)without coding
- Dynamically display the most relevant payment options based on factors such as location, currency, and transaction amount

For instance, if a customer in Germany is paying in EUR, they see all the active payment methods that accept EUR, starting with ones that are widely used in Germany.

![A variety of payment methods.](https://b.stripecdn.com/docs-statics-srv/assets/payment-element-methods.26cae03aff199d6f02b0d92bd324c219.png)

Show payment methods in order of relevance to your customer

To further customize how payment methods render, such as by filtering card brands that you don’t want to support, see Customize payment methods. To add payment methods integrated outside of Stripe, see External payment methods.

If your integration requires you to list payment methods manually, see Manually list payment methods.

## Layout

You can customize the Payment Element’s layout to fit your checkout flow. The following image is the same Payment Element rendered using different layout configurations.

![Examples of the three checkout forms. The image shows the tab option, where customers pick from payment methods shown as tabs or the two accordion options, where payment methods are vertically listed. You can choose to either display radio buttons or not in the accordion view. ](https://b.stripecdn.com/docs-statics-srv/assets/pe_layout_example.525f78bcb99b95e49be92e5dd34df439.png)

Payment Element with different layouts.

TabsAccordion with radio buttonsAccordion without radio buttonsThe tabs layout displays payment methods horizontally using tabs. To use this layout, set the value for layout.type to tabs. You can also specify other properties, such as layout.defaultCollapsed.

index.js[View full sample](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)`const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');

const appearance = { /* appearance */ };
const options = {
  layout: {
    type: 'tabs',
    defaultCollapsed: false,
  }
};`See all 12 lines## Appearance

Use the Appearance API to control the style of all elements. Choose a theme or update specific details.

![Examples of light and dark modes for the payment element checkout form.](https://b.stripecdn.com/docs-statics-srv/assets/appearance_example.e076cc750983bf552baf26c305e7fc90.png)

For instance, choose the “flat” theme and override the primary text color.

index.js[View full sample](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)`const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');

const appearance = {
  theme: 'flat',
  variables: { colorPrimaryText: '#262626' }
};`See all 10 linesSee the Appearance API documentation for a full list of themes and variables.

## Options

Stripe elements support more options than these. For instance, display your business name using the business option.

index.js[View full sample](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)`const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');

const appearance = { /* appearance */};
const options = {
  business: "RocketRides"
};`See all 10 linesThe Payment Element supports the following options. See each options’s reference entry for more information.

[layout](/js/elements_object/create_payment_element#payment_element_create-options-layout)Layout for the Payment Element.[defaultValues](/js/elements_object/create_payment_element#payment_element_create-options-defaultValues)Initial customer information to display in the Payment Element.[business](/js/elements_object/create_payment_element#payment_element_create-options-business)Information about your business to display in the Payment Element.[paymentMethodOrder](/js/elements_object/create_payment_element#payment_element_create-options-business)Order to list payment methods in.[fields](/js/elements_object/create_payment_element#payment_element_create-options-business)Whether to display certain fields.[readOnly](/js/elements_object/create_payment_element#payment_element_create-options-readOnly)Whether payment details can be changed.[terms](/js/elements_object/create_payment_element#payment_element_create-options-terms)Whether mandates or other legal agreements are displayed in the Payment Element. The default behavior is to show them only when necessary.[wallets](/js/elements_object/create_payment_element)Whether to show wallets like Apple Pay or Google Pay. The default is to show them when possible.Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`