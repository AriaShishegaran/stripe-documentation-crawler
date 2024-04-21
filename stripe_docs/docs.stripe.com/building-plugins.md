# Legacy pluginsDeprecated

You can no longer request API keys from users. Stripe Apps is the new method for authenticating users and includes support for OAuth 2.0.

View the migration docs

[migration docs](/stripe-apps/onboarding-plugin)

Become a Stripe Partner to reach businesses on Stripe who are looking to add capabilities to their platforms.

[Become a Stripe Partner](https://stripe.com/partner-program)

Follow these best practices to make sure your users can safely process on Stripe’s platform without disruption as our API evolves. If you have questions along the way, reach out to plugins@stripe.com.

[plugins@stripe.com](mailto:plugins@stripe.com)

- Register your plugin by creating a Stripe account or using an existing one

- Identify your plugin using setAppInfo and registerAppInfo so we can alert you to any potential issues we notice

[Identify your plugin](#identify-plugin)

- Set Stripe’s API version in your plugin to avoid potentially breaking changes for your users

[Stripe’s API version](#set-api-version)

- Use client-side tokenization to securely collect payment details in the browser

[client-side tokenization](#tokenization)

You can also take a few steps to improve the quality of your connector:

- Add the Express Checkout Element to offer multiple one-click payment buttons to your customers, including Apple Pay, Google Pay, Link, and PayPal

[Express Checkout Element](#express-checkout-element)

[Apple Pay](/apple-pay)

[Google Pay](/google-pay)

[Link](/payments/link)

[PayPal](/payments/paypal)

- Enable multiple payment methods beyond credit cards to support international users

[multiple payment methods](#apms)

- Verify your users have HTTPS enabled to improve their security

[have HTTPS enabled](#https)

- Subscribe to our mailing list to keep up to speed with changes to Stripe’s API

[mailing list](#subscribe)

## Identifying your plugin

Provide identifying information so that we can contact you if there’s an issue with your connector or critical update to the API.

If you use the APIs to create server-side requests, use setAppInfo with a hash containing the following options:

- name (required): your plugin’s name

- partner_id (required for Stripe Verified Partners, optional otherwise): your Partner ID from the Partners section of the Dashboard

[Stripe Verified Partners](https://stripe.com/partner-program)

[Partners](https://dashboard.stripe.com/partners/settings)

- version (optional): your plugin’s version

- url (optional): the URL for your plugin’s website with your contact details

[https://example.com](https://example.com)

If your connector is designed for a particular platform, include that platform in the name field (for example, WordPress MyStripePlugin or WooCommerce MyStripePlugin).

If you’re building a connector and not using one of our official libraries, set the value of the User-Agent header on requests made to the Stripe API as name/version (url).

The following is an example:

For frontend libraries that use Stripe.js, use registerAppInfo with the same options as setAppInfo above. For example, using JavaScript:

[https://example.com](https://example.com)

## Setting the API version

Your plugin should use the setApiVersion function, which will set the Stripe-Version HTTP header on all requests. Your users will use their own API keys to access Stripe, but this header will be included with every request. We recommend that you use the most recently published version of the API. The current API version and details on our versioning policy can be found in the API reference.

[versioning policy](/api#versioning)

New Stripe users automatically default to the latest version of the API. This header ensures that your connector is pinned to a specific API version, which keeps the occasional backwards-incompatible change from breaking your connector’s functionality.

[backwards-incompatible change](/upgrades#what-changes-does-stripe-consider-to-be-backwards-compatible)

Users can upgrade their own API version through the Stripe Dashboard. If your connector relies on webhook events, their data format and structure depend on the user’s account API version. You should instruct your users to set the version in their Dashboard to match your plugin.

[Stripe Dashboard](/upgrades#how-can-i-upgrade-my-api)

[webhook](/webhooks)

API versions can’t be downgraded. You should regularly release new versions of your connector to correctly handle any changes to JSON responses.

## Subscribing to our mailing list for updates

We regularly release new versions of the Stripe API that bring new features and bug fixes. You can subscribe to the api-announce mailing list to be notified of updates that may affect users of your connector.

[api-announce](https://groups.google.com/a/lists.stripe.com/forum/#!forum/api-announce)

## Securely collecting payment details

Stripe users are subject to PCI compliance, which specifies how credit card data should be securely stored, processed, and transmitted. Their businesses could face stiff penalties for noncompliance or potential breaches, so it’s important to help them safely process on Stripe.

[PCI compliance](https://stripe.com/guides/pci-compliance)

Since your connector will make API calls on behalf of a Stripe user, you must transmit credit card data securely using client-side tokenization. Customers submit their personal information through their web browser or mobile app directly to Stripe, and in exchange a simple token will be sent to the Stripe user. This allows your users to securely collect card details without sensitive data ever touching their server.

[Customers](/api/customers)

If your connector includes a client-side payment form in the browser, we recommend that you use either Stripe.js and Elements or Checkout:

[Stripe.js and Elements](/payments/elements)

[Checkout](/payments/checkout)

- Elements provides prebuilt UI components and complete control over the look and feel of payment forms

- Checkout provides a complete checkout experience and can be quickly added to a Stripe user’s website

Both of these options provide client-side tokenization.

If your plugin only operates in a backend environment, please include a note in your connector’s documentation asking users to tokenize payment details using Elements or Checkout. Tokenization helps Stripe users process as safely as possible on our platform.

## Add the Express Checkout Element

The Express Checkout Element gives you a single integration for accepting payments through one-click payment buttons, including Apple Pay, Google Pay, Link, or PayPal.

[Express Checkout Element](/elements/express-checkout-element)

[Apple Pay](/apple-pay)

[Google Pay](/google-pay)

[Link](/payments/link)

[PayPal](/payments/paypal)

The Express Checkout Element allows you to display multiple buttons at the same time. Customers see different payment buttons depending on what their device and browser combination supports.

## Enabling multiple payment methods

Stripe supports multiple payment methods, aside from credit cards. We’ve published a guide to payment methods that introduces terminology, key considerations, and how we support each method on our platform.

[guide to payment methods](https://stripe.com/payments/payment-methods-guide)

The Payment Methods API enables your users to collect payments using additional payment methods (for example, Alipay, iDEAL, Sofort). You can add these payment methods using one integration path.

[Payment Methods API](/payments/payment-methods)

[payment methods](/payments/payment-methods#supported-payment-methods)

## Verifying that HTTPS is enabled

If your plugin presents a payment form in a web browser, it should check if the form is being served over HTTPS. We require our users to enable HTTPS: you should present a clear error to your user if they’re not properly secured.

Here are a few examples to verify whether your users have HTTPS enabled:

If your connector has a front-end component, check whether HTTPS is being used from the browser. For example, using JavaScript:
