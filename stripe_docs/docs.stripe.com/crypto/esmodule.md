# Stripe Crypto SDK ES ModuleBeta

View the package on npm to learn how ES Module Stripe crypto SDK works.

[npm](https://www.npmjs.com/@stripe/crypto)

This introductory guide shows you how to install the Stripe crypto ES module  client-side SDK with a script tag or package manager. The SDK wraps the global StripeOnramp function provided by the Stripe crypto script as an ES module. It allows you to use the onramp widget to help your customers to acquire crypto using fiat.

[Stripe crypto ES module](https://www.npmjs.com/@stripe/crypto)

[onramp](/crypto/overview)

[Manually load the Stripe crypto script](#web-stripejs-html)

## Manually load the Stripe crypto script

Include the following scripts using script tags within the <head> element of your HTML. These scripts must always load directly from Stripe’s domains, https://js.stripe.com and https://crypto-js.stripe.com, for compatibility and PCI compliance. Don’t include the scripts in a bundle or host a copy yourself. If you do, your integration might break without warning.

[PCI compliance](/security/guide#validating-pci-compliance)

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

[https://crypto-js.stripe.com/crypto-onramp-outer.js](https://crypto-js.stripe.com/crypto-onramp-outer.js)

Set the API publishable key to allow Stripe to retrieve the OnrampSession object created by your backend. For example:

[API publishable key](https://dashboard.stripe.com/test/apikeys)

[Load Stripe crypto SDK as an ES module](#web-stripejs-esmodule)

## Load Stripe crypto SDK as an ES module

To install through the package manager, install the Stripe.js ES module and Stripe crypto ES module from the npm public registry. The package includes Typescript type definitions.

[Stripe.js ES module](https://github.com/stripe/stripe-js)

[Stripe crypto ES module](https://www.npmjs.com/package/@stripe/crypto)

[npm public registry](https://www.npmjs.com/)

Import the module and set the API publishable key to allow Stripe to retrieve the OnrampSession object created by your backend. The function returns a Promise object that resolves with a newly created StripeOnramp object after the scripts load.

[API publishable key](https://dashboard.stripe.com/test/apikeys)

## See also

- Integrate the onramp

[Integrate the onramp](/crypto/integrate-the-onramp)
