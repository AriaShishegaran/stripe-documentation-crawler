htmlReact Stripe.js reference | Stripe Documentation[Skip to content](#main-content)React Stripe.js[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-js%2Freact)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-js%2Freact)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)
[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[SDKs](/docs/libraries)# React Stripe.js reference

Learn about React components for Stripe.js and Stripe Elements.### See the code

Want to see how React Stripe.js works or help develop it? Check out the project on GitHub.

React Stripe.js is a thin wrapper around Stripe Elements. It allows you to add Elements to any React app.

The Stripe.js reference covers complete Elements customization details.

You can use Elements with any Stripe product to collect online payments. To find the right integration path for your business, explore our docs.

NoteThis reference covers the full React Stripe.js API. If you prefer to learn by doing, check out our documentation on accepting a payment or take a look at a sample integration.

## Before you begin

This doc assumes that you already have a basic working knowledge of React and that you have already set up a React project. If you’re new to React, we recommend that you take a look at the Getting Started guide before continuing.

## Setup

npmumdInstall React Stripe.js and the Stripe.js loader from the npm public registry.

Command Line`npm install --save @stripe/react-stripe-js @stripe/stripe-js`## Elements provider

The Elements provider allows you to use Element components and access the Stripe object in any nested component. Render an Elements provider at the root of your React app so that it is available everywhere you need it.

To use the Elements provider, call loadStripe from @stripe/stripe-js with your publishable key. The loadStripe function asynchronously loads the Stripe.js script and initializes a Stripe object. Pass the returned Promise to Elements.

index.js`import {Elements} from '@stripe/react-stripe-js';
import {loadStripe} from '@stripe/stripe-js';

// Make sure to call `loadStripe` outside of a component’s render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');

export default function App() {
  const options = {
    // passing the client secret obtained from the server
    clientSecret: '{{CLIENT_SECRET}}',
  };

  return (
    <Elements stripe={stripePromise} options={options}>
      <CheckoutForm />
    </Elements>
  );
};`propdescriptionstripe

required Stripe | null | Promise<Stripe | null>

A Stripe object or a Promise resolving to a Stripe object. The easiest way to initialize a Stripe object is with the Stripe.js wrapper module. After this prop has been set, it can not be changed.

You can also pass in null or a Promise resolving to null if you’re performing an initial server-side render or when generating a static site.

options

optional Object

Optional Elements configuration options. See available options. Once the stripe prop has been set, these options can’t be changed. If you want to use Payment Element, it is required to pass in the clientSecret.

## Element components

Element components provide a flexible way to securely collect payment information in your React app.

You can mount individual Element components inside of your Elements tree. Note that you can only mount one of each type of Element in a single <Elements> group.

CheckoutForm.js`import {PaymentElement} from '@stripe/react-stripe-js';

const CheckoutForm = () => {
  return (
    <form>
      <PaymentElement />
      <button>Submit</button>
    </form>
  );
};

export default CheckoutForm;`propdescriptionid

optional string

Passes through to the Element’s container.

className

optional string

Passes through to the Element’s container.

options

optional Object

An object containing Element configuration options. See available options for the Payment Element or available options for individual payment method Elements.

onBlur

optional () => void

Triggered when the Element loses focus.

onChange

optional (event: Object) => void

Triggered when data exposed by this Element is changed (for example, when there is an error).

For more information, refer to the Stripe.js reference.

onClick

optional (event: Object) => void

Triggered by the <PaymentRequestButtonElement> when it is clicked.

For more information, refer to the Stripe.js reference.

onFocus

optional () => void

Triggered when the Element receives focus.

onReady

optional (element: Element) => void

Triggered when the Element is fully rendered and can accept imperative element.focus() calls. Called with a reference to the underlying Element instance.

### Available Element components

There are many different kinds of Elements, useful for collecting different kinds of payment information. These are the available Elements today.

ComponentUsage`AddressElement`Collects address details for 236+ regional formats. See the[Address Element](/elements/address-element/collect-addresses?platform=web&client=react)docs.`AfterpayClearpayMessageElement`Displays installments messaging for Afterpay payments.`AuBankAccountElement`Collects Australian bank account information (BSB and account number) for use with BECS Direct Debit payments.`CardCvcElement`Collects the card‘s CVC number.`CardElement`A flexible single-line input that collects all necessary card details.`CardExpiryElement`Collects the card‘s expiration date.`CardNumberElement`Collects the card number.`ExpressCheckoutElement`Allows you to accept card or wallet payments through one or more payment buttons, including Apple Pay, Google Pay, Link, or PayPal. See the[Express Checkout Element](/elements/express-checkout-element)docs.`FpxBankElement`The customer’s bank, for use with FPX payments.`IbanElement`The International Bank Account Number (IBAN). Available for SEPA countries.`IdealBankElement`The customer’s bank, for use with iDEAL payments.`LinkAuthenticationElement`Collects email addresses and allows users to log in to Link. See the[Link Authentication Element](/payments/elements/link-authentication-element)docs.`PaymentElement`Collects payment details for[25+ payment methods](/payments/payment-methods/integration-options)from around the globe. See the[Payment Element](/payments/accept-a-payment?platform=web&ui=elements&client=react)docs.`PaymentRequestButtonElement`An all-in-one checkout button backed by either Apple Pay or the Payment Request API. See the[Payment Request Button](/stripe-js/elements/payment-request-button)docs.## useElements hook

`useElements(): Elements | null`To safely pass the payment information collected by the Payment Element to the Stripe API, access the Elements instance so that you can use it with stripe.confirmPayment. If you use the React Hooks API, then useElements is the recommended way to access a mounted Element. If you need to access an Element from a class component, use ElementsConsumer instead.

NoteNote that if you pass a Promise to the Elements provider and the Promise hasn’t yet resolved, then useElements will return null.

CheckoutForm.js`import {useStripe, useElements, PaymentElement} from '@stripe/react-stripe-js';

const CheckoutForm = () => {
  const stripe = useStripe();
  const elements = useElements();

  const handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    if (!stripe || !elements) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }

    const result = await stripe.confirmPayment({
      //`Elements` instance that was used to create the Payment Element
      elements,
      confirmParams: {
        return_url: "https://example.com/order/123/complete",
      },
    });

    if (result.error) {
      // Show error to your customer (for example, payment details incomplete)
      console.log(result.error.message);
    } else {
      // Your customer will be redirected to your `return_url`. For some payment
      // methods like iDEAL, your customer will be redirected to an intermediate
      // site first to authorize the payment, then redirected to the `return_url`.
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <PaymentElement />
      <button disabled={!stripe}>Submit</button>
    </form>
  )
};

export default CheckoutForm;`## useStripe hook

`useStripe(): Stripe | null`The useStripe hook returns a reference to the Stripe instance passed to the Elements provider. If you need to access the Stripe object from a class component, use ElementsConsumer instead.

NoteNote that if you pass a Promise to the Elements provider and the Promise hasn’t yet resolved, then useStripe will return null.

CheckoutForm.js`import {useStripe, useElements, PaymentElement} from '@stripe/react-stripe-js';

const CheckoutForm = () => {
  const stripe = useStripe();
  const elements = useElements();

  const handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    if (!stripe || !elements) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }

    const result = await stripe.confirmPayment({
      //`Elements` instance that was used to create the Payment Element
      elements,
      confirmParams: {
        return_url: "https://example.com/order/123/complete",
      },
    });


    if (result.error) {
      // Show error to your customer (for example, payment details incomplete)
      console.log(result.error.message);
    } else {
      // Your customer will be redirected to your `return_url`. For some payment
      // methods like iDEAL, your customer will be redirected to an intermediate
      // site first to authorize the payment, then redirected to the `return_url`.
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <PaymentElement />
      <button disabled={!stripe}>Submit</button>
    </form>
  )
};

export default CheckoutForm;`## ElementsConsumer

To safely pass the payment information collected by the Payment Element to the Stripe API, access the Elements instance so that you can use it with stripe.confirmPayment. If you need to access the Stripe object or an Element from a class component, then ElementsConsumer provides an alternative to the useElements and useStripe hooks.

CheckoutForm.js`import {ElementsConsumer, PaymentElement} from '@stripe/react-stripe-js';

class CheckoutForm extends React.Component {
  handleSubmit = async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    const {stripe, elements} = this.props;

    if (!stripe || !elements) {
      // Stripe.js hasn't yet loaded.
      // Make sure to disable form submission until Stripe.js has loaded.
      return;
    }

    const result = await stripe.confirmPayment({
      //`Elements` instance that was used to create the Payment Element
      elements,
      confirmParams: {
        return_url: "https://example.com/order/123/complete",
      },
    });

    if (result.error) {
      // Show error to your customer (for example, payment details incomplete)
      console.log(result.error.message);
    } else {
      // Your customer will be redirected to your `return_url`. For some payment
      // methods like iDEAL, your customer will be redirected to an intermediate
      // site first to authorize the payment, then redirected to the `return_url`.
    }
  };

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <PaymentElement />
        <button disabled={!this.props.stripe}>Submit</button>
      </form>
    );
  }
}

export default function InjectedCheckoutForm() {
  return (
    <ElementsConsumer>
      {({stripe, elements}) => (
        <CheckoutForm stripe={stripe} elements={elements} />
      )}
    </ElementsConsumer>
  )
}`propdescriptionchildren

required ({elements, stripe}) => ReactNode

This component takes a function as child. The function that you provide will be called with the Elements object that is managing your Element components and the Stripe object that you passed to <Elements>.

Note that if you pass a Promise to the Elements provider and the Promise hasn’t yet resolved, then stripe and elements will be null.

## Customization and styling

### Why iframes?

We recognize that the use of iframes makes styling an Element more difficult, but they shift the burden of securely handling payment data to Stripe and allows you to keep your site compliant with industry regulation.

Each element is mounted in an iframe, which means that Elements probably won’t work with any existing styling and component frameworks that you have. Despite this, you can still configure Elements to match the design of your site.  Customizing Elements consists of responding to events and configuring Elements with the appearance option. The layout of each Element stays consistent, but you can modify colors, fonts, borders, padding, and more.

Customer locationUnited States (USD)SizeDesktopThemeDefaultLayoutTabsThis demo only displays Google Pay or Apple Pay if you have an active card with either wallet.## Next steps

Build an integration with React Stripe.js and Elements.

- [Accept a payment](/payments/quickstart)
- [Accept a payment with the Express Checkout Element](/elements/express-checkout-element/accept-a-payment)
- [Adding the Payment Request Button](/stripe-js/elements/payment-request-button)
- [Learn about the Elements Appearance API](/elements/appearance-api)
- [Stripe.js reference](/js)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Setup](#setup)[Elements provider](#elements-provider)[Element components](#element-components)[useElements hook](#useelements-hook)[useStripe hook](#usestripe-hook)[ElementsConsumer](#elements-consumer)[Customization and styling](#customization-and-styling)[See also](#next-steps)Products Used[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`