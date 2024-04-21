# React Stripe.js reference

Want to see how React Stripe.js works or help develop it? Check out the project on GitHub.

[project on GitHub](https://github.com/stripe/react-stripe-js)

React Stripe.js is a thin wrapper around Stripe Elements. It allows you to add Elements to any React app.

[Stripe Elements](/payments/elements)

The Stripe.js reference covers complete Elements customization details.

[Stripe.js reference](/js/elements_object/create_payment_element#payment_element_create-options)

You can use Elements with any Stripe product to collect online payments. To find the right integration path for your business, explore our docs.

[explore our docs](/)

This reference covers the full React Stripe.js API. If you prefer to learn by doing, check out our documentation on accepting a payment or take a look at a sample integration.

[accepting a payment](/payments/accept-a-payment?platform=web)

[sample integration](/payments/quickstart)

## Before you begin

This doc assumes that you already have a basic working knowledge of React and that you have already set up a React project. If you’re new to React, we recommend that you take a look at the Getting Started guide before continuing.

[React](https://reactjs.org/)

[Getting Started](https://react.dev/learn)

## Setup

Install React Stripe.js and the Stripe.js loader from the npm public registry.

[npm public registry](https://www.npmjs.com/package/@stripe/react-stripe-js)

## Elements provider

The Elements provider allows you to use Element components and access the Stripe object in any nested component. Render an Elements provider at the root of your React app so that it is available everywhere you need it.

[Element components](#element-components)

[Stripe object](/js/initializing)

To use the Elements provider, call loadStripe from @stripe/stripe-js with your publishable key. The loadStripe function asynchronously loads the Stripe.js script and initializes a Stripe object. Pass the returned Promise to Elements.

[loadStripe](https://github.com/stripe/stripe-js/blob/master/README.md#loadstripe)

stripe

required Stripe | null | Promise<Stripe | null>

A Stripe object or a Promise resolving to a Stripe object. The easiest way to initialize a Stripe object is with the Stripe.js wrapper module. After this prop has been set, it can not be changed.

[Stripe object](/js/initializing)

[Stripe.js wrapper module](https://github.com/stripe/stripe-js/blob/master/README.md#readme)

You can also pass in null or a Promise resolving to null if you’re performing an initial server-side render or when generating a static site.

options

optional Object

Optional Elements configuration options. See available options. Once the stripe prop has been set, these options can’t be changed. If you want to use Payment Element, it is required to pass in the clientSecret.

[See available options](/js/elements_object/create#stripe_elements-options)

## Element components

Element components provide a flexible way to securely collect payment information in your React app.

You can mount individual Element components inside of your Elements tree. Note that you can only mount one of each type of Element in a single <Elements> group.

id

optional string

Passes through to the Element’s container.

[Element’s container](/js/element/the_element_container)

className

optional string

Passes through to the Element’s container.

[Element’s container](/js/element/the_element_container)

options

optional Object

An object containing Element configuration options. See available options for the Payment Element or available options for individual payment method Elements.

[See available options](/js/elements_object/create_payment_element#payment_element_create-options)

[available options](/js/elements_object/create_element?type=card#elements_create-options)

onBlur

optional () => void

Triggered when the Element loses focus.

onChange

optional (event: Object) => void

Triggered when data exposed by this Element is changed (for example, when there is an error).

For more information, refer to the Stripe.js reference.

[Stripe.js reference](/js/element/events/on_change?type=paymentElement#element_on_change-handler)

onClick

optional (event: Object) => void

Triggered by the <PaymentRequestButtonElement> when it is clicked.

For more information, refer to the Stripe.js reference.

[Stripe.js reference](/js/element/events/on_click#element_on_click-handler)

onFocus

optional () => void

Triggered when the Element receives focus.

onReady

optional (element: Element) => void

Triggered when the Element is fully rendered and can accept imperative element.focus() calls. Called with a reference to the underlying Element instance.

There are many different kinds of Elements, useful for collecting different kinds of payment information. These are the available Elements today.

[Address Element](/elements/address-element/collect-addresses?platform=web&client=react)

[Express Checkout Element](/elements/express-checkout-element)

[Link Authentication Element](/payments/elements/link-authentication-element)

[25+ payment methods](/payments/payment-methods/integration-options)

[Payment Element](/payments/accept-a-payment?platform=web&ui=elements&client=react)

[Payment Request Button](/stripe-js/elements/payment-request-button)

## useElements hook

To safely pass the payment information collected by the Payment Element to the Stripe API, access the Elements instance so that you can use it with stripe.confirmPayment. If you use the React Hooks API, then useElements is the recommended way to access a mounted Element. If you need to access an Element from a class component, use ElementsConsumer instead.

[stripe.confirmPayment](/js/payment_intents/confirm_payment)

[React Hooks API](https://react.dev/reference/react)

[ElementsConsumer](#elements-consumer)

Note that if you pass a Promise to the Elements provider and the Promise hasn’t yet resolved, then useElements will return null.

[Elements provider](#elements-provider)

[https://example.com/order/123/complete](https://example.com/order/123/complete)

## useStripe hook

The useStripe hook returns a reference to the Stripe instance passed to the Elements provider. If you need to access the Stripe object from a class component, use ElementsConsumer instead.

[hook](https://react.dev/reference/react)

[Stripe](/js/initializing)

[Elements](#elements-provider)

[ElementsConsumer](#elements-consumer)

Note that if you pass a Promise to the Elements provider and the Promise hasn’t yet resolved, then useStripe will return null.

[Elements provider](#elements-provider)

[https://example.com/order/123/complete](https://example.com/order/123/complete)

## ElementsConsumer

To safely pass the payment information collected by the Payment Element to the Stripe API, access the Elements instance so that you can use it with stripe.confirmPayment. If you need to access the Stripe object or an Element from a class component, then ElementsConsumer provides an alternative to the useElements and useStripe hooks.

[stripe.confirmPayment](/js/payment_intents/confirm_payment)

[useElements](#useElements-hook)

[useStripe](#useStripe-hook)

[https://example.com/order/123/complete](https://example.com/order/123/complete)

children

required ({elements, stripe}) => ReactNode

This component takes a function as child. The function that you provide will be called with the Elements object that is managing your Element components and the Stripe object that you passed to <Elements>.

[function as child](https://reactjs.org/docs/render-props.html#using-props-other-than-render)

[Elements object](/js/elements_object)

[Stripe object](/js/initializing)

[<Elements>](#elements-provider)

Note that if you pass a Promise to the Elements provider and the Promise hasn’t yet resolved, then stripe and elements will be null.

[Elements provider](#elements-provider)

## Customization and styling

We recognize that the use of iframes makes styling an Element more difficult, but they shift the burden of securely handling payment data to Stripe and allows you to keep your site compliant with industry regulation.

[compliant with industry regulation](/security/guide#validating-pci-compliance)

Each element is mounted in an iframe, which means that Elements probably won’t work with any existing styling and component frameworks that you have. Despite this, you can still configure Elements to match the design of your site.  Customizing Elements consists of responding to events and configuring Elements with the appearance option. The layout of each Element stays consistent, but you can modify colors, fonts, borders, padding, and more.

[responding to events](/js/element/events)

[appearance](/elements/appearance-api)

## Next steps

Build an integration with React Stripe.js and Elements.

- Accept a payment

[Accept a payment](/payments/quickstart)

- Accept a payment with the Express Checkout Element

[Accept a payment with the Express Checkout Element](/elements/express-checkout-element/accept-a-payment)

- Adding the Payment Request Button

[Adding the Payment Request Button](/stripe-js/elements/payment-request-button)

- Learn about the Elements Appearance API

[Learn about the Elements Appearance API](/elements/appearance-api)

- Stripe.js reference

[Stripe.js reference](/js)
