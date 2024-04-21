# Collect payment details before creating an Intent

The Payment Element allows you to accept multiple payment methods using a single integration. In this integration, learn how to build a custom payment flow where you render the Payment Element, create the PaymentIntent, and confirm the payment from the buyer’s browser. If you prefer to confirm the payment from the server instead, see Finalize payments on the server.

[PaymentIntent](/payments/payment-intents)

[Finalize payments on the server](/payments/finalize-payments-on-the-server)

[Set up StripeServer-side](#set-up-stripe)

## Set up StripeServer-side

First, create a Stripe account or sign in.

[create a Stripe account](https://dashboard.stripe.com/register)

[sign in](https://dashboard.stripe.com/login)

Use our official libraries to access the Stripe API from your application:

[Enable payment methods](#enable-payment-methods)

## Enable payment methods

Stripe doesn’t currently support BLIK for this integration path.

View your payment methods settings and enable the payment methods you want to support. You need at least one payment method enabled to create a PaymentIntent.

[payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

[PaymentIntent](/payments/payment-intents)

By default, Stripe enables cards and other prevalent payment methods that can help you reach more customers, but we recommend turning on additional payment methods that are relevant for your business and customers. See Payment method integration options for product and payment method support, and our pricing page for fees.

[Payment method integration options](/payments/payment-methods/integration-options#payment-method-product-support)

[pricing page](https://stripe.com/pricing/local-payment-methods)

[Collect payment detailsClient-side](#web-collect-payment-details)

## Collect payment detailsClient-side

You’re ready to collect payment details on the client with the Payment Element. The Payment Element is a prebuilt UI component that simplifies collecting payment details for a variety of payment methods.

The Payment Element contains an iframe that securely sends payment information to Stripe over an HTTPS connection. Avoid placing the Payment Element within another iframe because some payment methods require redirecting to another page for payment confirmation.

The checkout page address must start with https:// rather than http:// for your integration to work. You can test your integration without using HTTPS, but remember to enable it when you’re ready to accept live payments.

[enable it](/security/guide#tls)

The Payment Element is automatically available as a feature of Stripe.js. Include the Stripe.js script on your checkout page by adding it to the head of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

Create an instance of Stripe with the following JavaScript on your checkout page:

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

The Payment Element needs a place to live on your checkout page. Create an empty DOM node (container) with a unique ID in your payment form:

When the form above has loaded, create an Elements instance with the mode, amount, and currency. These values determine which payment methods are shown to your customer.

Then, create an instance of the Payment Element and mount it to the container DOM node.

The Payment Element renders a dynamic form that allows your customer to pick a payment method. The form automatically collects all necessary payments details for the payment method selected by the customer.

You can customize the Payment Element to match the design of your site by passing the appearance object into options when creating the Elements provider.

[appearance object](/elements/appearance-api)

By default, the Payment Element only collects the necessary billing address details. To collect a customer’s full billing address (to calculate the tax for digital goods and services, for example) or shipping address, use the Address Element.

[Address Element](/elements/address-element)

[OptionalCustomize the layoutClient-side](#customize-layout)

## OptionalCustomize the layoutClient-side

[OptionalCustomize the appearanceClient-side](#customize-appearance)

## OptionalCustomize the appearanceClient-side

[OptionalDynamically update payment detailsClient-side](#dynamic-updates)

## OptionalDynamically update payment detailsClient-side

[OptionalAdditional elements optionsClient-side](#additional-options)

## OptionalAdditional elements optionsClient-side

[OptionalCreate a ConfirmationToken](#create-ct)

## OptionalCreate a ConfirmationToken

[Create a PaymentIntentServer-side](#create-intent)

## Create a PaymentIntentServer-side

Navigate to step 5 in the finalize payments guide to run your custom business logic immediately before payment confirmation. Otherwise, follow the steps below for a simpler integration, which uses stripe.confirmPayment on the client to both confirm the payment and handle any next actions.

[step 5](/payments/finalize-payments-on-the-server?platform=web&type=payment#submit-payment)

When the customer submits your payment form, use a PaymentIntent to facilitate the confirmation and payment process. Create a PaymentIntent on your server with an amount and currency enabled. In the latest version of the API, specifying the automatic_payment_methods parameter is optional because Stripe enables its functionality by default. You can manage payment methods from the Dashboard. Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow. To prevent malicious customers from choosing their own prices, always decide how much to charge on the server-side (a trusted environment) and not the client.

[PaymentIntent](/payments/payment-intents)

[Dashboard](https://dashboard.stripe.com/settings/payment_methods)

Included on a PaymentIntent is a client secret. Return this value to your client for Stripe.js to use to securely complete the payment process.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

[Submit the payment to StripeClient-side](#submit-the-payment)

## Submit the payment to StripeClient-side

Use stripe.confirmPayment to complete the payment using details from the Payment Element.

[stripe.confirmPayment](/js/payment_intents/confirm_payment)

Provide a return_url to this function to indicate where Stripe should redirect the user after they complete the payment. Your user might be initially redirected to an intermediate site, like a bank authorization page, before being redirected to the return_url. Card payments immediately redirect to the return_url when a payment is successful.

[return_url](/api/payment_intents/create#create_payment_intent-return_url)

If you don’t want to redirect for card payments after payment completion, you can set redirect to if_required. This only redirects customers that check out with redirect-based payment methods.

[redirect](/js/payment_intents/confirm_payment#confirm_payment_intent-options-redirect)

[https://example.com/order/123/complete](https://example.com/order/123/complete)

[OptionalHandle post-payment events](#web-fulfillment)

## OptionalHandle post-payment events
