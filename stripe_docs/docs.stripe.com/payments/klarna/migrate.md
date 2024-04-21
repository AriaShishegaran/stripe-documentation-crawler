# Migrate Klarna from Sources

Klarna is launching a new checkout process that requires the Payment Methods API and the Payment Intents API. This guide outlines several recommended paths to migrate from using the Sources API, including a low-code option that uses Stripe Checkout.

[Payment Methods API](/api/payment_methods)

[Payment Intents API](/api/payment_intents)

[Sources API](/api/sources)

[Stripe Checkout](/payments/checkout)

We have deprecated Sources API support for Klarna, and we plan to remove it entirely in early 2024. If you’re still using the Sources API to process Klarna payments, migrate now to use PaymentMethods and PaymentIntents.

Initiating the Klarna payment on PaymentIntents

Completing the Klarna payment on PaymentIntents

- Klarna product selection: You don’t need to specify the Klarna product type in your integration. Instead, customers now choose a product on the Klarna redirect page. Don’t include a separate button on your checkout site for each supported Klarna payment option. Only include a single Klarna button.

- Klarna SDK inline display isn’t supported: Customers must now redirect to the Klarna site from your payment page to authorize the payment. As a result, you don’t need to load the Klarna SDK or render any inline components.

- Payment confirmation is synchronous in all markets: Previously, confirmation of a successful payment was asynchronous in some cases. Now, you can detect whether the payment is successful immediately after your customer authorizes it.

If you currently use a plugin for your Stripe integration, the plugin developer must migrate their plugin to use PaymentMethods and PaymentIntents. Reach out to them to understand if there are any changes you need to make to your Stripe or plugin settings.

## Migrate your payment flow

To migrate your Klarna integration for web payments, you need to update your server and frontend to use the PaymentIntents API. There are three typical integration options:

[PaymentIntents API](/api/payment_intents)

- Redirect to Stripe Checkout for your payment flow.

[Stripe Checkout](/payments/checkout)

- Use the Stripe Payment Element on your own payment page.

[Payment Element](/payments/payment-element)

- Build your own form and use the Stripe JS SDK to complete the payment.

Use Stripe Checkout or the Payment Element to add and manage most payment methods from the Stripe Dashboard without making code changes.

[Stripe Checkout](/payments/checkout)

[Payment Element](/payments/payment-element)

Below is a high level comparison of the old integration steps with the new integrations:

Low complexity

Medium complexity

High complexity

Load the Klarna widget with the Klarna SDK to authorize the payment

OR

Redirect to Klarna to authorize the payment

Not needed

Pass the client secret to the frontend and use the Stripe JS SDK to render a Payment Element to complete the payment.

Pass the client secret to the frontend. Use your own form to collect additional details from your customer and use the Stripe JS SDK to redirect to Klarna

A PaymentIntent is the object that represents a payment in the new integration, and it creates a Charge when you confirm the payment on the frontend. If you previously stored references to the Charge in your databases, you can continue to do so by fetching the Charge ID from the PaymentIntent after the customer completes the payment. However, we also recommend that you store the PaymentIntent ID.

[Option 1: Use a Checkout Session](#checkout)

## Option 1: Use a Checkout Session

Stripe Checkout is a low-code hosted payment solution that can accept Klarna payments, as well as a variety of other payment methods supported by Stripe. If you currently have a payment page hosted on your site and instead want to use Stripe Checkout, do the following:

[Stripe Checkout](/payments/checkout)

- Make sure Klarna is enabled in your Dashboard.

[enabled in your Dashboard](https://dashboard.stripe.com/settings/payment_methods)

- Create a Checkout Session on your server. You can either explicitly set klarna as one of the payment_method_types, or use dynamic payment methods.

[Create a Checkout Session on your server](/payments/klarna/accept-a-payment?platform=web&ui=stripe-hosted#accept-a-payment)

[dynamic payment methods](/payments/dashboard-payment-methods)

- If you sell physical goods, enable shipping address collection or include the shipping address in the shipping_details hash.

[enable shipping address collection](/api/checkout/sessions/object#checkout_session_object-shipping_address_collection)

[the shipping_details hash](/api/checkout/sessions/object#checkout_session_object-shipping_details)

- Redirect to the Session URL when the customer is ready to pay.

[Option 2: Use the Payment Element](#payment-element)

## Option 2: Use the Payment Element

Stripe Payment Element is a single embedded UI component for your payment page that supports Klarna as well as other payment methods. It provides many of the features of Stripe Checkout, but displayed on your own payment page. To use the Payment Element, do the following:

[Stripe Payment Element](/payments/payment-element)

- Make sure that Klarna is enabled in your Dashboard.

[enabled in your Dashboard](https://dashboard.stripe.com/settings/payment_methods)

- Create a PaymentIntent on your server

You can explicitly enable Klarna by setting it as one of the payment_method_types.

[payment_method_types](/api/payment_intents/create#create_payment_intent-payment_method_types)

- Pass the PaymentIntent client secret to the frontend and initialize the Stripe Elements UI library.

[initialize the Stripe Elements UI library](/payments/accept-a-payment?platform=web&ui=elements#web-collect-payment-details)

- Create a Payment Element and embed it on the page. This element automatically collects any additional fields needed for the payment method selected by the customer.

[Create a Payment Element](/payments/accept-a-payment?platform=web&ui=elements#add-the-payment-element-to-your-payment-page)

- Call confirmPayment on the Payment Element when the user submits their payment. Make sure that you pass a return_url.

[Call confirmPayment on the Payment Element](/payments/accept-a-payment?platform=web&ui=elements#web-submit-payment)

[Option 3: Build your own form](#custom-form)

## Option 3: Build your own form

You can build your own form components and complete a Klarna payment by using the Stripe JS SDK. Read more about the full integration. To integrate in this method, do the following:

[full integration](/payments/klarna/accept-a-payment?platform=web&ui=direct-api)

- Make sure that Klarna is enabled in your Dashboard.

[enabled in your Dashboard](https://dashboard.stripe.com/settings/payment_methods)

- Create a PaymentIntent on your server.

[Create a PaymentIntent](/payments/klarna/accept-a-payment?platform=web&ui=direct-api#web-create-payment-intent)

If you don’t want to manage payment methods through the Dashboard, you can explicity enable Klarna by setting it as one of the payment_method_types.

[payment_method_types](/api/payment_intents/create#create_payment_intent-payment_method_types)

- Use a form to collect your customer’s email and billing country.

- Initialize Stripe.JS on your payment page and call confirmKlarnaPayment with the PaymentIntent’s client secret when the customer is ready to authorize the payment. Make sure that their email and billing country are in the billing_details[email] and billing_details[address][country] fields.

[Initialize Stripe.JS on your payment page and call confirmKlarnaPayment](/payments/klarna/accept-a-payment?platform=web&ui=direct-api#web-submit-payment)

## Field mapping reference

If you use the Payment Element or your own form, you must remap the fields previously on the Source to the PaymentIntent. The table below is a mapping of the old fields to the new fields. If you sell physical goods, we recommend that you pass shipping details. All other fields are optional, and Klarna collects necessary additional information on their page.

[API reference](/api/payment_intents/create#create_payment_intent-shipping-address)

[our docs](/payments/klarna/accept-a-payment?platform=web&ui=direct-api#supported-locales-and-currencies)

[separate auth and capture](/payments/klarna/accept-a-payment?platform=web&ui=direct-api#manual-capture)

If you currently use the klarna[attachment] parameter or the order[items] parameter on the Source, then we will contact you with details about these parameters.

[klarna[attachment] parameter](/payments/klarna/accept-a-payment)

## After the purchase

The following changes are required for any integration points you have after a payment has completed.

Previously, your integration should have checked both the status of the Source and the status of the Charge after each API call. You no longer need to check two statuses—you only need to check the status of the PaymentIntent or the Checkout Session after you confirm it on the frontend.

Always confirm the status of the PaymentIntent by fetching it on your server or listening for the webhooks on your server. Don’t rely solely on the user returning to the return_url that’s provided when you confirm the PaymentIntent. Read more about this here.

[here](/payments/klarna/accept-a-payment?platform=web&ui=direct-api#web-fulfillment)

You can continue to call the Refunds API with a Charge that the PaymentIntent creates. The ID of the Charge is accessible on the latest_charge parameter. Alternatively, you can provide the PaymentIntent ID to the Refunds API instead of the Charge.

## Error handling

Previously, you had to handle errors on the Sources were created. In PaymentIntents, you don’t need to check for errors on a Source, and instead need to check for errors on the PaymentIntent when it’s created and after the customer has authorized the payment. Most errors on the PaymentIntent are on the type field returned in an invalid request.

[the type field](/api/errors#errors-type)

## Webhooks

If you previously listened to Source events, you might need to update your integration to listen to new event types. Below is a reference of the new event types to listen for.

[expires](/api/checkout/sessions/create#create_checkout_session-expires_at)
