htmlCheckout migration guide | Stripe Documentation[Skip to content](#main-content)Migrate from legacy Checkout[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fmigration)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fmigration)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Checkout](/payments/checkout)·[Home](/docs)[Payments](/docs/payments)[Checkout](/docs/payments/checkout)# Checkout migration guide

Learn how to migrate from the legacy version of Checkout to the current version.![](https://b.stripecdn.com/docs-statics-srv/assets/migration.4db0b4061fb36d6a43762c3f23ef9c00.png)

### Stripe Elements

If you want to embed a payment form within an existing page, consider using Stripe Elements.

The legacy version of Checkout presented customers with a modal dialog that collected card information, and returned a token or a source to your website. In contrast, the current version of Checkout is a smart payment page hosted by Stripe that creates payments or subscriptions. It supports Apple Pay, Dynamic 3D Secure, and many other features.

The current version of Checkout provides more flexibility, with support for dynamic line items, Connect, re-using existing Customers, and advanced subscription features. You can also use the client-only integration if you want to get started more quickly or if you have a simpler product catalog.

To migrate from the legacy version to the current version, follow the guide that most closely represents your business model. Each guide recommends an integration path along with example code.

- Dynamic product catalog and pricing

If you have a large product catalog or require support for dynamically generated line items (such as donations or taxes).


- Dynamic subscriptions

If you’re a SaaS provider billing users and need support for advanced features.


- Connect platforms and marketplaces

If you’re operating a marketplace connecting service providers with customers.


- Saving payment methods for future use

If you’re operating a business which doesn’t charge the customer until after services rendered.


- Simple product catalog with fixed pricing

If you’re selling a few products with pre-determined prices.


- Simple subscriptions

If you’re a SaaS provider with a monthly subscription plan.



As you follow the relevant migration guide, you can also reference the conversion table for a mapping of specific parameters and configuration options between the two versions of Checkout.

## Dynamic product catalog and pricing

If you’re selling products where the amount or line items are determined dynamically (say, with a large product catalog or for donations), see accepting one-time payments.

You may have used the legacy version of Checkout to create a token or source on the client, and passed it to your server to create a charge. The current version of the Checkout server integration reverses this flow—you create a Session on your server, pass its ID to your client, redirect your customer to Checkout, who then gets redirected back to your application upon success.

### Before

With the legacy version of Checkout, you’d display the dynamic amount and description and collect card information from your customer.

client.html`<form action="/purchase" method="POST">
  <script
    src="https://checkout.stripe.com/checkout.js"
    class="stripe-button"
    data-key="pk_test_VOOyyYjgzqdm8I3SrBqmh9qY"
    data-name="Custom t-shirt"
    data-description="Your custom designed t-shirt"
    data-amount="{{ORDER_AMOUNT}}"
    data-currency="usd">
  </script>
</form>`Next, you’d send the resulting token or source to your server and charge it.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "email"="customer@example.com" \
  -d "source"="{{STRIPE_TOKEN}}"
curl https://api.stripe.com/v1/charges \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "customer"="{{CUSTOMER_ID}}" \
  -d "description"="Custom t-shirt" \
  -d "amount"="{{ORDER_AMOUNT}}" \
  -d "currency"="usd"`### After

With the current version of Checkout, first create a Checkout Session on your server.

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "payment_method_types[]"="card" \
  -d "line_items[][price_data][product]"="{{PRODUCT_ID}}" \
  -d "line_items[][price_data][unit_amount]"=1500 \
  -d "line_items[][price_data][currency]"="usd" \
  -d "line_items[][quantity]"=1 \
  -d "mode"="payment" \
  -d "success_url"="https://example.com/success" \
  -d "cancel_url"="https://example.com/cancel"`NoteIf you use one of our Client libraries, upgrade to the latest version of the library in order to use the Checkout Sessions API.

Next, pass the Session ID to your client and redirect your customer to Checkout to complete payment.

`const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');
const checkoutButton = document.getElementById('checkout-button');

checkoutButton.addEventListener('click', () => {
  stripe.redirectToCheckout({
    // Make the id field from the Checkout Session creation API response
    // available to this file, so you can provide it as argument here
    // instead of the {{CHECKOUT_SESSION_ID}} placeholder.
    sessionId: '{{CHECKOUT_SESSION_ID}}'
  })
  // If `redirectToCheckout` fails due to a browser or network
  // error, display the localized error message to your customer
  // using `error.message`.
});`The customer is redirected to the success_url after they complete payment.

If you need to fulfill purchased goods after the payment, refer to Checkout Purchase Fulfillment.

## Dynamic subscriptions

If you’re providing subscription services that are dynamically determined or require support for other advanced features, see setting up a subscription.

You may have used the legacy version of Checkout to create a token or source on the client, and passed it to your server to create a customer and subscription. The current version of the Checkout server integration reverses this flow—you first create a Session on your server, pass its ID to your client, redirect your customer to Checkout, who then gets redirected back to your application upon success.

### Before

With the legacy version of Checkout, you’d display the subscription information and collect card information from your customer.

client.html`<form action="/subscribe" method="POST">
  <script
    src="https://checkout.stripe.com/checkout.js"
    class="stripe-button"
    data-key="pk_test_VOOyyYjgzqdm8I3SrBqmh9qY"
    data-name="Gold Tier"
    data-description="Monthly subscription with 30 days trial"
    data-amount="2000"
    data-label="Subscribe">
  </script>
</form>`Next, you’d send the resulting token or source to your server to create a customer and a subscription.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "email"="customer@example.com" \
  -d "source"="{{STRIPE_TOKEN}}"
curl https://api.stripe.com/v1/subscriptions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "customer"="{{CUSTOMER_ID}}" \
  -d "items[0][price]"="{PRICE_ID}" \
  -d "trial_period_days"=30`### After

With the current version of Checkout, first create a Checkout Session on your server.

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "payment_method_types[]"="card" \
  -d "subscription_data[trial_period_days]"=30 \
  -d "line_items[][price]"="{PRICE_ID}" \
  -d "line_items[][quantity]"=1 \
  -d "mode"="subscription" \
  -d "success_url"="https://example.com/success" \
  -d "cancel_url"="https://example.com/cancel"`NoteIf you use one of our Client libraries, upgrade to the latest version of the library in order to use the Checkout Sessions API.

Next, pass the Session ID to your client and redirect your customer to Checkout to complete payment.

`const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');
const checkoutButton = document.getElementById('checkout-button');

checkoutButton.addEventListener('click', () => {
  stripe.redirectToCheckout({
    // Make the id field from the Checkout Session creation API response
    // available to this file, so you can provide it as argument here
    // instead of the {{CHECKOUT_SESSION_ID}} placeholder.
    sessionId: '{{CHECKOUT_SESSION_ID}}'
  })
  // If `redirectToCheckout` fails due to a browser or network
  // error, display the localized error message to your customer
  // using `error.message`.
});`The customer is redirected to the success_url after the customer and subscription have been created.

If you need to fulfill purchased services after the payment, refer to Checkout Purchase Fulfillment.

You can also update subscription information using Checkout.

## Connect platforms and marketplaces

If you’re operating a Connect platform or marketplace and create payments involving connected accounts, consider using the current version of the Checkout server integration. Follow the instructions in the Connect guide to migrate your integration.

The following example demonstrates using the Checkout Sessions API to process a direct charge. Follow the Connect guide for details on how to create destination charges.

### Before

With the legacy version of Checkout, you would collect card information from your customer on the client.

client.html`<form action="/purchase" method="POST">
  <script
    src="https://checkout.stripe.com/checkout.js"
    class="stripe-button"
    data-key="pk_test_VOOyyYjgzqdm8I3SrBqmh9qY"
    data-name="Food Marketplace"
    data-description="10 cucumbers from Roger's Farm"
    data-amount="2000">
  </script>
</form>`Next, you’d send the resulting token or source to your server and charge it on behalf of the connected account.

Command Line[curl](#)`curl https://api.stripe.com/v1/charges \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "source"="{{TOKEN_ID}}" \
  -d "description"="10 cucumbers from Roger\"s Farm" \
  -d "amount"=2000 \
  -d "currency"="usd" \
  -d "application_fee_amount"=200 \
  -H "Stripe-Account: {{CONNECTED_STRIPE_ACCOUNT_ID}}"`### After

With the current version of Checkout, first create a Checkout Session on your server on behalf of the connected account.

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "payment_method_types[]"="card" \
  -d "line_items[][price]"="{{PRICE_ID}}" \
  -d "line_items[][quantity]"=1 \
  -d "payment_intent_data[application_fee_amount]"=200 \
  -d "mode"="payment" \
  -d "success_url"="https://example.com/success" \
  -d "cancel_url"="https://example.com/cancel" \
  -H "Stripe-Account: {{CONNECTED_STRIPE_ACCOUNT_ID}}"`NoteIf you use one of our Client libraries, upgrade to the latest version of the library to use the Checkout Sessions API.

Next, pass the Session ID to your client and redirect your customer to Checkout to complete payment. Make sure to provide the connected account’s ID when initializing Stripe.js.

`// Initialize Stripe.js with the same connected account ID used when creating
// the Checkout Session.
const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY', {
  stripeAccount: '{{CONNECTED_ACCOUNT_ID}}'
});
const checkoutButton = document.getElementById('checkout-button');

checkoutButton.addEventListener('click', () => {
  stripe.redirectToCheckout({
    // Make the id field from the Checkout Session creation API response
    // available to this file, so you can provide it as argument here
    // instead of the {{CHECKOUT_SESSION_ID}} placeholder.
    sessionId: '{{CHECKOUT_SESSION_ID}}'
  })
  // If `redirectToCheckout` fails due to a browser or network
  // error, display the localized error message to your customer
  // using `error.message`.
});`The customer is redirected to the success_url after they complete payment.

If you need to fulfill purchased goods or services after the payment, refer to Checkout Purchase Fulfillment.

## Saving payment methods for future use

If you’re providing services that don’t charge your customers immediately, see setting up future payments.

You may have used the legacy version of Checkout to create a token or source on the client, and passed it to your server to save for later use. The current version of the Checkout server integration reverses this flow—you first create a Session on your server, pass its ID to your client, redirect your customer to Checkout, who then gets redirected back to your application upon success.

### Before

With the legacy version of Checkout, you’d display the charge information and collect card information from your customer.

client.html`<form action="/subscribe" method="POST">
  <script
    src="https://checkout.stripe.com/checkout.js"
    class="stripe-button"
    data-key="pk_test_VOOyyYjgzqdm8I3SrBqmh9qY"
    data-name="Cleaning Service"
    data-description="Charged after your home is spotless"
    data-amount="2000">
  </script>
</form>`Next, you would send the resulting token or source to your server to eventually create a charge.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "email"="customer@example.com" \
  -d "source"="{{STRIPE_TOKEN}}"
curl https://api.stripe.com/v1/charges \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "customer"="{{CUSTOMER_ID}}" \
  -d "description"="Cleaning service" \
  -d "amount"="{{ORDER_AMOUNT}}" \
  -d "currency"="usd"`### After

With the current version of Checkout, first create a Checkout Session on your server using setup mode.

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "payment_method_types[]"="card" \
  -d "mode"="setup" \
  -d "success_url"="https://example.com/success?session_id={CHECKOUT_SESSION_ID}" \
  -d "cancel_url"="https://example.com/cancel"`NoteIf you use one of our Client libraries, upgrade to the latest version of the library to use the Checkout Sessions API.

Next, pass the Session ID to your client and redirect your customer to Checkout to gather payment method details.

`const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');
const checkoutButton = document.getElementById('checkout-button');

checkoutButton.addEventListener('click', () => {
  stripe.redirectToCheckout({
    // Make the id field from the Checkout Session creation API response
    // available to this file, so you can provide it as argument here
    // instead of the {{CHECKOUT_SESSION_ID}} placeholder.
    sessionId: '{{CHECKOUT_SESSION_ID}}'
  })
  // If `redirectToCheckout` fails due to a browser or network
  // error, display the localized error message to your customer
  // using `error.message`.
});`The customer is redirected to the success_url after they complete the flow.

From there, you can retrieve the Setup Intent from the Checkout flow and use it to prepare your transaction.

## Simple product catalog with fixed pricing

If you’re selling products with fixed pricing (such as t-shirts or e-books), see the guide on one-time payments to learn how to generate a code snippet to add to your website.

You may have used the legacy version of Checkout to create a token or source on the client, and passed it to your server to create a charge. The current version of Checkout automatically creates the payment for you, and no server integration is required.

### Client-side code

JavaScriptJavascript (ESNext)BeforeAfterclient.html`<form action="/pay" method="POST">
  <script
    src="https://checkout.stripe.com/checkout.js"
    class="stripe-button"
    data-key="pk_test_VOOyyYjgzqdm8I3SrBqmh9qY"
    data-name="T-shirt"
    data-description="Comfortable cotton t-shirt"
    data-amount="500"
    data-currency="usd">
  </script>
</form>`client.html`<script src="https://js.stripe.com/v3"></script>
<button type="button" id="checkout-button">Pay</button>`client.js`var stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');

var checkoutButton = document.querySelector('#checkout-button');
checkoutButton.addEventListener('click', function () {
  stripe.redirectToCheckout({
    lineItems: [{
      // Define the product and price in the Dashboard first, and use the price
      // ID in your client-side code.
      price: '{PRICE_ID}',
      quantity: 1
    }],
    mode: 'payment',
    successUrl: 'https://www.example.com/success',
    cancelUrl: 'https://www.example.com/cancel'
  });
});`### Server-side code

curlRubyPythonPHPJavaNodeGo.NETBeforeAfterCommand Line`curl https://api.stripe.com/v1/customers \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "email"="{{STRIPE_EMAIL}}" \
  -d "source"="{{STRIPE_TOKEN}}"
curl https://api.stripe.com/v1/charges \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "customer"="{{CUSTOMER_ID}}" \
  -d "description"="T-shirt" \
  -d "amount"=500 \
  -d "currency"="usd"`The current version of Checkout automatically creates payments for you. After your customer pays, they’re redirected to the successUrl configured on the client. Then learn how to fulfill orders after the payment.

The conversion table below provides a mapping of configuration options between the two versions of Checkout. For a full list of configuration options for the current version, see the redirectToCheckout reference.

## Simple subscriptions

If you’re providing a simple subscription service (such as monthly access to software), see the guide on subscriptions to learn how to create a plan in the Dashboard and generate a code snippet to add to your website.

You may have used the legacy version of Checkout to create a token or source on the client, and passed it to your server to create a customer and a subscription. The current version of Checkout, however, automatically creates both the customer and the subscription for you, and no server integration is required.

### Client-side code

JavaScriptJavascript (ESNext)BeforeAfterclient.html`<form action="/subscribe" method="POST">
  <script
    src="https://checkout.stripe.com/checkout.js"
    class="stripe-button"
    data-key="pk_test_VOOyyYjgzqdm8I3SrBqmh9qY"
    data-name="Gold Tier"
    data-description="Monthly subscription"
    data-amount="2000"
    data-currency="usd"
    data-label="Subscribe">
  </script>
</form>`client.html`<script src="https://js.stripe.com/v3"></script>
<button type="button" id="checkout-button">Subscribe</button>`client.js`var stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');

var checkoutButton = document.querySelector('#checkout-button');
checkoutButton.addEventListener('click', function () {
  stripe.redirectToCheckout({
    lineItems: [{
      // Define the product and price in the Dashboard first, and use the price
      // ID in your client-side code. You may also pass a SKU id into the `price`
      // field
      price: '{PRICE_ID}',
      quantity: 1
    }],
    mode: 'subscription',
    successUrl: 'https://www.example.com/success',
    cancelUrl: 'https://www.example.com/cancel'
  });
});`### Server-side code

curlRubyPythonPHPJavaNodeGo.NETBeforeAfterCommand Line`curl https://api.stripe.com/v1/customers \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "email"="{{STRIPE_EMAIL}}" \
  -d "source"="{{STRIPE_TOKEN}}"
curl https://api.stripe.com/v1/subscriptions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "customer"="{{CUSTOMER_ID}}" \
  -d "items[][price]"="{PRICE_ID}" \
  -d "items[][quantity]"=1`The current version of Checkout automatically creates subscriptions for you. After the subscription is created, your customer is redirected to the successUrl configured on the client. Then learn how to fulfill orders after the payment.

The conversion table below provides a mapping of configuration options between the two versions of Checkout. For a full list of configuration options for the current version, see the redirectToCheckout reference.

## Parameter conversion

The current version of Checkout supports most of the functionality of the legacy version of Checkout. However, the two versions do not share the same API. The table below maps parameters and configuration options between the legacy version and the current version.

For a full list of configuration options accepted by the current version of Checkout, see the Stripe.js reference and the API reference for Checkout Sessions.

Legacy versionCurrent versionIntegration tips`allowRememberMe`- Not supported

The current version of Checkout doesn’t support Remember Me. To reuse existing customers, we recommend specifying the`customer`parameter when creating a[Checkout Session](/api/checkout/sessions/create).`amount`- Automatically calculated as the sum of amounts over all`line_items`.
- Client-only integration: Automatically calculated as the sum of amounts over all prices.

The total amount is the sum of the line items you pass to Checkout.`billingAddress`- `Session.billing_address_collection`
- Client-only integration:`billingAddressCollection`

Checkout automatically collects the billing address when required for fraud-prevention or regulatory purposes. Set this parameter to`required`to always collect the billing address.`billingAddress`- `Session.billing_address_collection`
- Client-only integration:`billingAddressCollection`

Checkout automatically collects the billing address when required for fraud-prevention or regulatory purposes. Set this parameter to`required`to always collect the billing address.`closed`- `cancelUrl`

When a customer wants to close Checkout, they either close the browser tab or navigate to the`cancelUrl`.`currency`- `Session.currency`
- Client-only integration: The price’s`currency`

`description`- `Session.line_items.description`or`product.description`
- Client-only integration: The price’s`product.description`

If you specify a price, Checkout displays an automatically computed description of how often payments occur. If you specify`Session.line_items`, Checkout displays the`name`for each line item.`email`- `Session.customer_email`
- Client-only integration:`customerEmail`

If you already know your customer’s email, specify it here so they do not need to enter it again.`image`- Business brandingUpload your business logo or icon in the Dashboard.
- Product imagesSpecify images for each line item with`product.images`

Checkout uses specific images for your business’s[branding](/payments/checkout/customization#branding)and for the products you’re selling. Checkout displays your business logo by default and falls back to your business icon alongside your business name.`key`- No longer a parameter passed to Checkout

`locale`- `Session.locale`
- Client-only integration:`locale`

You can specify a supported[locale](/payments/checkout/customization#localization)when creating a Checkout Session.`name`- `product.name`for prices specified in`Session.line_items`
- Client-only integration: The`product.name`for the price

If you specify a price, Checkout displays the name of the product that belongs to the price. If you specify`Session.line_items`, Checkout displays the`name`for each line item.`panelLabel`- `submit_type`

Checkout automatically customizes the button text depending on the items you’re selling. For one-time payments, use[submit_type](/payments/checkout/customization#submit-button)to customize the button text.`shippingAddress`- `session.shipping_address_collection`

[Collect shipping address information](/payments/collect-addresses?payment-ui=checkout)by passing an array of`allowed_countries`that you want to ship to.`token`or`source`- `successUrl`

There is no longer a callback in JavaScript when the payment completes. As your customer is paying on a different page, set the`successUrl`to redirect your customer after they’ve completed payment.`zipCode`- Automatically collected by Checkout

Checkout automatically collects the postal code when required for fraud-prevention or regulatory purposes.Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Dynamic product catalog and pricing](#api-products)[Dynamic subscriptions](#api-subscriptions)[Connect platforms and marketplaces](#connect)[Saving payment methods for future use](#setup-mode)[Simple product catalog with fixed pricing](#client-products)[Simple subscriptions](#client-subscriptions)[Parameter conversion](#parameter-conversion)Products Used[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`