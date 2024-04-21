# Provide Radar additional fraud data

If you perform card tokenization yourself, through a third-party, or send raw credit card numbers to Stripe from your servers, critical device details won’t be automatically captured. With fewer data points, Radar might produce less accurate fraud scores. Inaccurate fraud scores can result in fraudulent charges not being blocked.

[Radar](/radar)

By using Radar Sessions, you can capture critical fraud information without tokenizing on Stripe. A Radar Session is a snapshot of the browser metadata and device details that helps Radar make more accurate predictions on your payments. This metadata includes information like IP address, browser, screen or device information, and other device characteristics. You can find more details about how Radar uses this data by reading about how Radar performs advanced fraud detection.

[advanced fraud detection](/disputes/prevention/advanced-fraud-detection)

The best way to tokenize your payment information is with a preferred Stripe integration, which handles the secure collection and tokenization of payment information. On a preferred Stripe integration,  Radar has visibility on your checkout flows and leverages the additional data to provide better fraud protection. If you use a preferred Stripe integration, don’t use Radar Sessions because you automatically send Stripe sufficient information.

[preferred Stripe integration](/radar/integration#integration-types)

This guide shows you how to provide Stripe with complete fraud information for these charges. It requires four steps:

- Set up Stripe.js and mobile SDKs

[Set up Stripe.js and mobile SDKs](#setup)

- Create a Radar Session from your client and send it to your server

[Create a Radar Session from your client and send it to your server](#create-radar-session)

- Send a Radar Session from your server to Stripe

[Send a Radar Session from your server to Stripe](#submit-payment-info)

- Verify that your integration works

[Verify that your integration works](#verify)

[Set up Stripe.js and mobile SDKs](#setup)

## Set up Stripe.js and mobile SDKs

Include Stripe.js on your website. To get started with Radar Sessions using the mobile SDKs, see the documentation for iOS (v21.6.0 or later) and Android (v16.9.0 or later).

[Stripe.js](/js/including)

[iOS](https://github.com/stripe/stripe-ios)

[Android](https://github.com/stripe/stripe-android)

[Create a Radar Session from your client and it send to your server](#create-radar-session)

## Create a Radar Session from your client and it send to your server

You need to create a Radar Session in your checkout flow or when saving card details. Stripe uses the Radar Session to associate the client information captured by Stripe libraries with subsequent server-side API requests.

Call createRadarSession as late in your checkout flow as possible. Your payment details or confirmation pages are good candidates.

[Send a Radar Session from your server to Stripe](#submit-payment-info)

## Send a Radar Session from your server to Stripe

You have some customizable choices on how to complete this step based on your particular use case and payments scenario.

Radar Sessions only works with Payment Intents API creation requests that result in a charge attempt. Therefore, when you create a PaymentIntent and are providing a Radar Session you must also specify confirm=true.

If you have an existing Payment Intent, you can attach a Radar Session to it when it’s confirmed.

Although not required, if your customers visit your site and make on-session payments, it’s always best to send a Radar Session when you create or confirm a Payment Intent and when you create a Payment Method. Any charges created using a Payment Method with a Radar Session use the client information associated with that Radar Session.

This allows Radar to use both sessions (when a user added a Payment Method and when the user actually made a payment with that Payment Method) to deliver better fraud protection by comparing browser information between the two events.

To send a Radar Session for off-session payments, which means completing the payment without the customer’s direct involvement, you need to attach a Radar Session when creating a Payment Method for your customer.

[Verify that your integration works](#verify)

## Verify that your integration works

Verify your integration by ensuring that the following is present in your API responses when you attach the session to Payment Intents, or Payment Methods. You can separately issue a GET for each of those resources and see the radar_options field when Radar Sessions were successfully attached.
