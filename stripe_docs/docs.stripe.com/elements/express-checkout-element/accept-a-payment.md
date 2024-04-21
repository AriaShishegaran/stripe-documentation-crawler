# Accept a payment with the Express Checkout Element

It’s preferred to collect payment details before creating an Intent when using the Express Checkout Element. If you previously integrated with the Payment Element, you might need to update your integration.

[Payment Element](/payments/payment-element)

[update your integration](/payments/accept-a-payment-deferred)

The Express Checkout Element gives you a single integration for accepting payments through one-click payment buttons, including Link, PayPal, Apple Pay, Google Pay, and Amazon Pay.

[Express Checkout Element](/elements/express-checkout-element)

[Link](/payments/link)

[PayPal](/payments/paypal)

[Apple Pay](/apple-pay)

[Google Pay](/google-pay)

[Amazon Pay](/payments/amazon-pay)

Customers see different payment buttons depending on what their device and browser combination supports. Compatible devices automatically support Google Pay and Link. Supporting Apple Pay and PayPal requires additional steps.

[Customers](/api/customers)

[Prerequisites](#prerequisites)

## Prerequisites

Before you start, you must:

- Add a payment method to your browser. For example, you can add a card to your Google Pay account or to your Wallet for Safari.

- Serve your application over HTTPS. This is required in development and in production. You can use a service such as ngrok.

[ngrok](https://ngrok.com/)

- Register and verify your domain in both test mode and live mode.

[Register and verify your domain](/payments/payment-methods/pmd-registration)

- Create a PayPal Sandbox account to test your integration.

[Create a PayPal Sandbox account](https://developer.paypal.com/tools/sandbox/accounts/)

[Set up StripeServer-side](#set-up-stripe)

## Set up StripeServer-side

First, create a Stripe account or sign in.

[create a Stripe account](https://dashboard.stripe.com/register)

[sign in](https://dashboard.stripe.com/login)

Use our official libraries to access the Stripe API from your application:

[Enable payment methods](#enable-payment-methods)

## Enable payment methods

Enable the payment methods you want to support in your payment methods settings. You must enable at least one payment method.

[payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

By default, Stripe enables cards and other common payment methods. You can enable additional payment methods that are relevant for your business and customers. See our payment method integration options for product and payment method support and our pricing page for fees.

[payment method integration options](/payments/payment-methods/integration-options#payment-method-product-support)

[pricing page](https://stripe.com/pricing/local-payment-methods)

[Set up Stripe ElementsClient-side](#set-up-elements)

## Set up Stripe ElementsClient-side

The Express Checkout Element is automatically available as a feature of Stripe.js. Include the Stripe.js script on your checkout page by adding it to the head of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

Create an instance of Stripe with the following JavaScript on your checkout page:

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

Then, create an instance of Elements with the mode (payment, setup, or subscription), amount, and currency. These values determine which payment methods to show to your customer. See the next step for more configurable Elements options.

[OptionalAdditional elements optionsClient-side](#additional-options)

## OptionalAdditional elements optionsClient-side

[Create and mount the Express Checkout ElementClient-side](#create-and-mount)

## Create and mount the Express Checkout ElementClient-side

The Express Checkout Element contains an iframe that securely sends the payment information to Stripe over an HTTPS connection. The checkout page address must also start with https://, rather than http://, for your integration to work.

The Express Checkout Element needs a place to live on your payment page. Create an empty DOM node (container) with a unique ID in your payment form.

When the form above has loaded, create an instance of the Express Checkout Element and mount it to the container DOM node.

[OptionalFilter card brandsClient-sideBeta](#filter-card-brands)

## OptionalFilter card brandsClient-sideBeta

[OptionalListen to the ready eventClient-side](#ready-event)

## OptionalListen to the ready eventClient-side

[OptionalControl when to show Apple Pay, Google Pay, and LinkClient-side](#wallet-control)

## OptionalControl when to show Apple Pay, Google Pay, and LinkClient-side

[OptionalStyle the buttonClient-side](#style-button)

## OptionalStyle the buttonClient-side

[OptionalConfigure the payment interfaceClient-side](#handle-click-event)

## OptionalConfigure the payment interfaceClient-side

[OptionalCreate a ConfirmationTokenClient-side](#create-ct)

## OptionalCreate a ConfirmationTokenClient-side

[Submit the payment to StripeClient-side](#submit-the-payment)

## Submit the payment to StripeClient-side

Use stripe.confirmPayment to complete the payment using details from the Express Checkout Element.

[stripe.confirmPayment](/js/payment_intents/confirm_payment)

For Amazon Pay, the amount you confirm in the PaymentIntent must match the amount the buyer pre-authorized to prevent the payment from being declined.

Provide a return_url to this function to indicate where Stripe should redirect the user after they complete the payment. Your user might be initially redirected to an intermediate site before being redirected to the return_url. Payments immediately redirect to the return_url when a payment is successful.

[return_url](/api/payment_intents/create#create_payment_intent-return_url)

If you don’t want to redirect after payment completion, set redirect to if_required. This only redirects customers that check out with redirect-based payment methods.

[redirect](/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect)

[https://example.com/order/123/complete](https://example.com/order/123/complete)

[Test the integration](#test-integration)

## Test the integration

Click the tabs below to view details for each payment method. See more information on supported browsers to see which payment methods work with specific browsers. If you use the Express Checkout Element within an iframe, the iframe must have the allow attribute set to equal “payment *”.

[supported browsers](/elements/express-checkout-element#supported-browsers)

[allow](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attr-allowpaymentrequest)

Don’t store real user data in test mode Link accounts. Treat them as if they’re publicly available, because these test accounts are associated with your publishable key.

[test mode](/test-mode)

Currently, Link only works with credit cards, debit cards, and qualified US bank account purchases. Link requires domain registration.

[domain registration](/payments/payment-methods/pmd-registration)

You can create test mode accounts for Link using any valid email address. The following table shows the fixed one-time passcode values that Stripe accepts for authenticating test mode accounts:

See our testing docs for test card numbers.

[testing docs](/testing)

[OptionalUse with Stripe Connect](#connect)

## OptionalUse with Stripe Connect

[Disclose Stripe to your customers](#disclose-cookies)

## Disclose Stripe to your customers

Stripe collects information on customer interactions with Elements to provide services to you, prevent fraud, and improve its services. This includes using cookies and IP addresses to identify which Elements a customer saw during a single checkout session. You’re responsible for disclosing and obtaining all rights and consents necessary for Stripe to use data in these ways. For more information, visit our privacy center.

[privacy center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe)

## See also

- Stripe Elements

[Stripe Elements](/payments/elements)

- Collect payment details before creating an Intent

[Collect payment details before creating an Intent](/payments/accept-a-payment-deferred)

- Finalize payments on the server

[Finalize payments on the server](/payments/finalize-payments-on-the-server)
