# Checkout migration guide

If you want to embed a payment form within an existing page, consider using Stripe Elements.

[Stripe Elements](/payments/elements)

The legacy version of Checkout presented customers with a modal dialog that collected card information, and returned a token or a source to your website. In contrast, the current version of Checkout is a smart payment page hosted by Stripe that creates payments or subscriptions. It supports Apple Pay, Dynamic 3D Secure, and many other features.

[subscriptions](/billing/subscriptions/creating)

[3D Secure](/payments/3d-secure)

[many other features](/payments/checkout)

The current version of Checkout provides more flexibility, with support for dynamic line items, Connect, re-using existing Customers, and advanced subscription features. You can also use the client-only integration if you want to get started more quickly or if you have a simpler product catalog.

[Connect](/connect)

[Customers](/api/customers)

To migrate from the legacy version to the current version, follow the guide that most closely represents your business model. Each guide recommends an integration path along with example code.

- Dynamic product catalog and pricingIf you have a large product catalog or require support for dynamically generated line items (such as donations or taxes).

Dynamic product catalog and pricing

[Dynamic product catalog and pricing](#api-products)

If you have a large product catalog or require support for dynamically generated line items (such as donations or taxes).

- Dynamic subscriptionsIf you’re a SaaS provider billing users and need support for advanced features.

Dynamic subscriptions

[Dynamic subscriptions](#api-subscriptions)

If you’re a SaaS provider billing users and need support for advanced features.

- Connect platforms and marketplacesIf you’re operating a marketplace connecting service providers with customers.

Connect platforms and marketplaces

[Connect platforms and marketplaces](#connect)

If you’re operating a marketplace connecting service providers with customers.

- Saving payment methods for future useIf you’re operating a business which doesn’t charge the customer until after services rendered.

Saving payment methods for future use

[Saving payment methods for future use](#setup-mode)

If you’re operating a business which doesn’t charge the customer until after services rendered.

- Simple product catalog with fixed pricingIf you’re selling a few products with pre-determined prices.

Simple product catalog with fixed pricing

[Simple product catalog with fixed pricing](#client-products)

If you’re selling a few products with pre-determined prices.

- Simple subscriptionsIf you’re a SaaS provider with a monthly subscription plan.

Simple subscriptions

[Simple subscriptions](#client-subscriptions)

If you’re a SaaS provider with a monthly subscription plan.

As you follow the relevant migration guide, you can also reference the conversion table for a mapping of specific parameters and configuration options between the two versions of Checkout.

[conversion table](#parameter-conversion)

## Dynamic product catalog and pricing

If you’re selling products where the amount or line items are determined dynamically (say, with a large product catalog or for donations), see accepting one-time payments.

[accepting one-time payments](/payments/accept-a-payment?integration=checkout)

You may have used the legacy version of Checkout to create a token or source on the client, and passed it to your server to create a charge. The current version of the Checkout server integration reverses this flow—you create a Session on your server, pass its ID to your client, redirect your customer to Checkout, who then gets redirected back to your application upon success.

With the legacy version of Checkout, you’d display the dynamic amount and description and collect card information from your customer.

[https://checkout.stripe.com/checkout.js](https://checkout.stripe.com/checkout.js)

Next, you’d send the resulting token or source to your server and charge it.

With the current version of Checkout, first create a Checkout Session on your server.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

If you use one of our Client libraries, upgrade to the latest version of the library in order to use the Checkout Sessions API.

[Client libraries](/libraries)

Next, pass the Session ID to your client and redirect your customer to Checkout to complete payment.

The customer is redirected to the success_url after they complete payment.

If you need to fulfill purchased goods after the payment, refer to Checkout Purchase Fulfillment.

[Checkout Purchase Fulfillment](/payments/checkout/fulfill-orders)

## Dynamic subscriptions

If you’re providing subscription services that are dynamically determined or require support for other advanced features, see setting up a subscription.

[setting up a subscription](/billing/subscriptions/build-subscriptions)

You may have used the legacy version of Checkout to create a token or source on the client, and passed it to your server to create a customer and subscription. The current version of the Checkout server integration reverses this flow—you first create a Session on your server, pass its ID to your client, redirect your customer to Checkout, who then gets redirected back to your application upon success.

With the legacy version of Checkout, you’d display the subscription information and collect card information from your customer.

[https://checkout.stripe.com/checkout.js](https://checkout.stripe.com/checkout.js)

Next, you’d send the resulting token or source to your server to create a customer and a subscription.

With the current version of Checkout, first create a Checkout Session on your server.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

If you use one of our Client libraries, upgrade to the latest version of the library in order to use the Checkout Sessions API.

[Client libraries](/libraries)

Next, pass the Session ID to your client and redirect your customer to Checkout to complete payment.

The customer is redirected to the success_url after the customer and subscription have been created.

If you need to fulfill purchased services after the payment, refer to Checkout Purchase Fulfillment.

[Checkout Purchase Fulfillment](/payments/checkout/fulfill-orders)

You can also update subscription information using Checkout.

[update subscription information](/payments/checkout/subscriptions/update-payment-details)

## Connect platforms and marketplaces

If you’re operating a Connect platform or marketplace and create payments involving connected accounts, consider using the current version of the Checkout server integration. Follow the instructions in the Connect guide to migrate your integration.

[Connect guide](/connect/creating-a-payments-page)

The following example demonstrates using the Checkout Sessions API to process a direct charge. Follow the Connect guide for details on how to create destination charges.

[Connect guide](/connect/creating-a-payments-page)

With the legacy version of Checkout, you would collect card information from your customer on the client.

[https://checkout.stripe.com/checkout.js](https://checkout.stripe.com/checkout.js)

Next, you’d send the resulting token or source to your server and charge it on behalf of the connected account.

With the current version of Checkout, first create a Checkout Session on your server on behalf of the connected account.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

If you use one of our Client libraries, upgrade to the latest version of the library to use the Checkout Sessions API.

[Client libraries](/libraries)

Next, pass the Session ID to your client and redirect your customer to Checkout to complete payment. Make sure to provide the connected account’s ID when initializing Stripe.js.

The customer is redirected to the success_url after they complete payment.

If you need to fulfill purchased goods or services after the payment, refer to Checkout Purchase Fulfillment.

[Checkout Purchase Fulfillment](/payments/checkout/fulfill-orders)

## Saving payment methods for future use

If you’re providing services that don’t charge your customers immediately, see setting up future payments.

[setting up future payments](/payments/save-and-reuse?platform=checkout)

You may have used the legacy version of Checkout to create a token or source on the client, and passed it to your server to save for later use. The current version of the Checkout server integration reverses this flow—you first create a Session on your server, pass its ID to your client, redirect your customer to Checkout, who then gets redirected back to your application upon success.

With the legacy version of Checkout, you’d display the charge information and collect card information from your customer.

[https://checkout.stripe.com/checkout.js](https://checkout.stripe.com/checkout.js)

Next, you would send the resulting token or source to your server to eventually create a charge.

With the current version of Checkout, first create a Checkout Session on your server using setup mode.

[setup mode](/payments/save-and-reuse?platform=checkout)

[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})

[https://example.com/cancel](https://example.com/cancel)

If you use one of our Client libraries, upgrade to the latest version of the library to use the Checkout Sessions API.

[Client libraries](/libraries)

Next, pass the Session ID to your client and redirect your customer to Checkout to gather payment method details.

The customer is redirected to the success_url after they complete the flow.

From there, you can retrieve the Setup Intent from the Checkout flow and use it to prepare your transaction.

[retrieve the Setup Intent](/payments/save-and-reuse#retrieve-checkout-session)

## Simple product catalog with fixed pricing

If you’re selling products with fixed pricing (such as t-shirts or e-books), see the guide on one-time payments to learn how to generate a code snippet to add to your website.

[one-time payments](/payments/checkout/client)

You may have used the legacy version of Checkout to create a token or source on the client, and passed it to your server to create a charge. The current version of Checkout automatically creates the payment for you, and no server integration is required.

[https://checkout.stripe.com/checkout.js](https://checkout.stripe.com/checkout.js)

[https://js.stripe.com/v3](https://js.stripe.com/v3)

[https://www.example.com/success](https://www.example.com/success)

[https://www.example.com/cancel](https://www.example.com/cancel)

The current version of Checkout automatically creates payments for you. After your customer pays, they’re redirected to the successUrl configured on the client. Then learn how to fulfill orders after the payment.

[successUrl](/js/deprecated/redirect_to_checkout#stripe_checkout_redirect_to_checkout-options-successUrl)

[fulfill orders](/payments/checkout/fulfill-orders)

The conversion table below provides a mapping of configuration options between the two versions of Checkout. For a full list of configuration options for the current version, see the redirectToCheckout reference.

[conversion table](#parameter-conversion)

[redirectToCheckout](/js#stripe-redirect-to-checkout)

## Simple subscriptions

If you’re providing a simple subscription service (such as monthly access to software), see the guide on subscriptions to learn how to create a plan in the Dashboard and generate a code snippet to add to your website.

[subscriptions](/billing/quickstart)

You may have used the legacy version of Checkout to create a token or source on the client, and passed it to your server to create a customer and a subscription. The current version of Checkout, however, automatically creates both the customer and the subscription for you, and no server integration is required.

[https://checkout.stripe.com/checkout.js](https://checkout.stripe.com/checkout.js)

[https://js.stripe.com/v3](https://js.stripe.com/v3)

[https://www.example.com/success](https://www.example.com/success)

[https://www.example.com/cancel](https://www.example.com/cancel)

The current version of Checkout automatically creates subscriptions for you. After the subscription is created, your customer is redirected to the successUrl configured on the client. Then learn how to fulfill orders after the payment.

[successUrl](/js/deprecated/redirect_to_checkout#stripe_checkout_redirect_to_checkout-options-successUrl)

[fulfill orders](/payments/checkout/fulfill-orders)

The conversion table below provides a mapping of configuration options between the two versions of Checkout. For a full list of configuration options for the current version, see the redirectToCheckout reference.

[conversion table](#parameter-conversion)

[redirectToCheckout](/js#stripe-redirect-to-checkout)

## Parameter conversion

The current version of Checkout supports most of the functionality of the legacy version of Checkout. However, the two versions do not share the same API. The table below maps parameters and configuration options between the legacy version and the current version.

For a full list of configuration options accepted by the current version of Checkout, see the Stripe.js reference and the API reference for Checkout Sessions.

[Stripe.js reference](/js#stripe-redirect-to-checkout)

[API reference](/api/checkout/sessions)

- Not supported

[Checkout Session](/api/checkout/sessions/create)

- Automatically calculated as the sum of amounts over all line_items.

- Client-only integration: Automatically calculated as the sum of amounts over all prices.

- Session.billing_address_collection

- Client-only integration: billingAddressCollection

- Session.billing_address_collection

- Client-only integration: billingAddressCollection

- cancelUrl

- Session.currency

- Client-only integration: The price’s currency

- Session.line_items.description or product.description

- Client-only integration: The price’s product.description

- Session.customer_email

- Client-only integration: customerEmail

- Business branding Upload your business logo or icon in the Dashboard.

- Product images Specify images for each line item withproduct.images

[branding](/payments/checkout/customization#branding)

- No longer a parameter passed to Checkout

- Session.locale

- Client-only integration: locale

[locale](/payments/checkout/customization#localization)

- product.name for prices specified in Session.line_items

- Client-only integration: The product.name for the price

- submit_type

[submit_type](/payments/checkout/customization#submit-button)

- session.shipping_address_collection

[Collect shipping address information](/payments/collect-addresses?payment-ui=checkout)

- successUrl

- Automatically collected by Checkout
