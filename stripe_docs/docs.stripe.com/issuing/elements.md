# Using Issuing Elements

Stripe.js includes a browser-side JavaScript library you can use to display the sensitive data of your Issuing cards on the web in compliance with PCI requirements. The sensitive data renders inside Stripe-hosted iframes and never touches your servers.

[Stripe.js](/js)

Stripe.js collects extra data to protect our users. Learn more about how Stripe collects data for advanced fraud detection.

[advanced fraud detection](/disputes/prevention/advanced-fraud-detection)

## Ephemeral key authentication

Stripe.js uses ephemeral keys to securely retrieve Card information from the Stripe API without publicly exposing your secret keys. You need to do some of the ephemeral key exchange on the server-side to set this up.

The ephemeral key creation process begins in the browser, by creating a nonce using Stripe.js. A nonce is a single-use token that creates an ephemeral key. This nonce is sent to your server, where you exchange it for an ephemeral key by calling the Stripe API (using your secret key).

After creating an ephemeral key server-side, pass it back to the browser for Stripe.js to use.

[Create a secure endpointServer-side](#create-secure-endpoint)

## Create a secure endpointServer-side

The first step to integrating with Issuing Elements is to create a secure, server-side endpoint to generate ephemeral keys for the card you want to show. Your Issuing Elements web integration calls this endpoint.

Here’s how you might implement an ephemeral key creation endpoint in web applications framework across various languages:

[https://youtu.be/rPR2aJ6XnAc](https://youtu.be/rPR2aJ6XnAc)

You must specify the API version when creating ephemeral keys. Currently, the required version is 2020-03-02. You must also pass in an ephemeral key nonce, which you can create in your web integration.

[Web API integrationClient-side](#web-api-integration)

## Web API integrationClient-side

First, include Stripe.js on your page. For more information on how to set up Stripe.js, refer to including Stripe.js.

[including Stripe.js.](/js/including)

Create a Stripe instance and an ephemeral key nonce for the card you want to retrieve using stripe.createEphemeralKeyNonce. Use the nonce to retrieve the ephemeral key by calling the server-side endpoint that you created:

[stripe.createEphemeralKeyNonce](/js/issuing/create_ephemeral_key_nonce)

[server-side endpoint](#create-secure-endpoint)

Now that you have an ephemeral key, you’re ready to show sensitive card details. You can do so using any of the following Elements, and you can re-use the same nonce and ephemeral key pair for multiple Elements on the same page:

Each Element takes the following configuration:

[Style object](/js/appendix/style)

If you decide to use issuingCardPinDisplay, then you must implement appropriate methods to ensure that access is limited to your authorized users. In particular, you must apply two-factor authentication (2FA) before providing access to a page using issuingCardPinDisplay. If Stripe decides that you don’t have sufficient security measures in place, we might suspend your access to this Element.

The following is an example of how to display one of these Elements, using the nonce and ephemeral key pair created in the example above:

## Adding a copy button

In addition to the “card data display elements” that we’ve already described, we also provide an issuingCardCopyButton element. This takes a toCopy argument and renders a transparent “copy to clipboard” button that takes up the space of its parent <div>. This allows it to intercept all click events with a click handler that takes the corresponding card data specified at initialization and copies it to the clipboard.

With this, you can display “copy to clipboard” buttons next to the card number, expiry, and cvc, which prevents your cardholders from manually copying card data. We restrict the copy functionality to Stripe’s PCI-compliant <iframe>.

The issuingCardCopyButton element takes the following configuration:

[Style object](/js/appendix/style)

An example of how to use this component is below:

If you’re having trouble with your button responding to clicks, be sure to line up the iframe to your button correctly. You can customize your image and containing <div> in your stylesheets however you want.

As a last step, provide an “after click feedback” option to your users. To do so, use the issuingCardCopyButton Element’s on click event. This could be temporarily showing a new icon as shown below.

[on click event](/js/element/events/on_click)

## Additional details

The returned card object has PCI fields (such as the number) fully removed from the result.issuingCard payload.

In addition to .mount() in the example above, the Elements also support the following methods:

- .destroy()

- .unmount()

- .update({style})

## Issuing Elements and native applications

Issuing Elements does not directly support native application platforms such as iOS, Android, or React Native.

To display sensitive card details with Issuing Elements in your native app, use a web view. Build a web integration on your servers following this guide, and then point a web view’s URL to that integration. To learn about implementing web views for native apps, see these external resources:

- iOS and iPadOS: WKWebView

[WKWebView](https://developer.apple.com/documentation/webkit/wkwebview)

- Android: WebView

[WebView](https://developer.android.com/reference/android/webkit/WebView)

- React Native: react-native-webview

[react-native-webview](https://github.com/react-native-webview/react-native-webview)

- Flutter: webview-flutter

[webview-flutter](https://pub.dev/packages/webview_flutter)
