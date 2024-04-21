# ES Module Stripe.js SDK

To see how ES Module Stripe.js works or to help develop it, check out the project on GitHub.

[project on GitHub](https://github.com/stripe/stripe-js)

This introductory guide shows you how to install the ES Module Stripe.js client-side SDK with a script tag or package manager. The SDK wraps the global Stripe function provided by the Stripe.js script as an ES module. It allows you to use Elements, our prebuilt UI components, to create a payment form that lets you securely collect a customer’s card details without handling the sensitive data.

[ES Module Stripe.js](https://github.com/stripe/stripe-js)

[Elements](/payments/elements)

## Before you begin

Enable the payment methods you want to support on the payment methods settings page.

[payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

[Manually load the Stripe.js script](#web-stripejs-html)

## Manually load the Stripe.js script

To install by script, add the Stripe.js ES Module as a script to the <head> element of your HTML. This allows any newly created Stripe objects to be globally accessible in your code.

[Stripe.js ES Module](https://github.com/stripe/stripe-js)

[Stripe objects](/js#stripe-function)

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

Next, set the API publishable key to allow Stripe to tokenize customer information and collect sensitive payment details. For example:

[API publishable key](https://dashboard.stripe.com/test/apikeys)

[tokenize](/api/tokens)

[Load Stripe.js as an ES Module](#web-stripejs-esmodule)

## Load Stripe.js as an ES Module

To install by package manager, install the Stripe.js ES Module from the npm public registry.

[Stripe.js ES Module](https://github.com/stripe/stripe-js)

[npm public registry](https://www.npmjs.com/)

Next, import the module into a JavaScript file. The following function returns a Promise that resolves with a newly created Stripe object after Stripe.js loads.

[Stripe object](/js#stripe-function)

## See also

This wraps up the introductory guide to setting up the ES Module Stripe.js SDK. See the links below to get started with your integration.

- Accept a payment with a payment element on GitHub

[Accept a payment with a payment element on GitHub](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)

- Accept a payment with a payment element in Docs

[Accept a payment with a payment element in Docs](/payments/accept-a-payment?ui=elements&client=html)

- Custom payment flow builder

[Custom payment flow builder](/payments/quickstart)

- Stripe.js reference

[Stripe.js reference](/js)
