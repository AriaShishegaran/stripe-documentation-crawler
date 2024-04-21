# Embeddable pricing table for SaaS businesses

You can use the Stripe Dashboard to create a table that displays different subscription pricing levels to your customers. You don’t need to write any custom code to create or embed a pricing table. This guide describes how to:

- Use the Stripe Dashboard to configure the UI component

- Copy the generated code from the Dashboard

- Embed the code on your website to show your customers pricing information and take them to a checkout page

[Overview](#overview)

## Overview

Embed a pricing table on your website to display pricing details and convert customers to checkout.

A pricing table is an embeddable UI that:

- Displays pricing information and takes customers to a prebuilt checkout flow. The checkout flow uses Stripe Checkout to complete the purchase.

[pricing information](/products-prices/pricing-models)

[Stripe Checkout](/payments/checkout)

- Supports common subscription business models like flat-rate, per-seat, tiered pricing, and free trials.

[flat-rate](/products-prices/pricing-models#flat-rate)

[per-seat](/products-prices/pricing-models#per-seat)

[tiered pricing](/products-prices/pricing-models#tiered-pricing)

- Lets you configure, customize, and update product and pricing information directly in the Dashboard, without needing to write any code.

- Embeds into your website with a <script> tag and web component. Stripe automatically generates the tag. You copy and paste it into your website’s code.

The diagram below summarizes how the customer goes from viewing a pricing table to completing checkout.

[Create pricing table](#Create)

## Create pricing table

- In the Dashboard, go to More > Product catalog > pricing tables.

[pricing tables](https://dashboard.stripe.com/pricing-tables)

- Click +Create pricing table.

- Add products relevant to your customers (up to four per pricing interval). Optionally, include a free trial.

- Adjust the look and feel in Display settings. You can highlight a specific product and customize the language, colors, font, and button design.

- Configure payment settings by clicking Continue. Customize what customers see on the payments page and whether to display a confirmation page or redirect customers back to your site after a successful purchase.

- Configure the customer portal by clicking Continue.

[customer portal](/no-code/customer-portal)

- Click Copy code to copy the generated code and embed it into your website.

[embed it into your website](/no-code/pricing-table#embed)

Customize your pricing table

Configure payment settings

[Embed pricing table](#embed)

## Embed pricing table

After creating a pricing table, Stripe automatically returns an embed code composed of a <script> tag and a <stripe-pricing-table> web component. Click the Copy code button to copy the code and paste it into your website.

Copy the pricing table’s code and embed it on your website.

If you’re using HTML, paste the embed code into the HTML. If you’re using React, include the script tag in your index.html page to mount the <stripe-pricing-table> component.

The pricing table uses your account’s publishable API key. If you revoke the API key, you need to update the embed code with your new publishable API key.

[publishable API key](/keys)

[https://js.stripe.com/v3/pricing-table.js](https://js.stripe.com/v3/pricing-table.js)

[Track subscriptions](#track-subscriptions)

## Track subscriptions

When a customer purchases a subscription, you’ll see it on the subscriptions page in the Dashboard.

[subscriptions page](https://dashboard.stripe.com/subscriptions)

The pricing table component uses Stripe Checkout to render a prebuilt, hosted payment page. When a payment is completed using Checkout, Stripe sends the checkout.session.completed webhook that you can use for fulfillment and reconciliation. Make sure to listen to additional webhooks if you enable payment methods like bank debits or vouchers, which can take 2-14 days to confirm the payment. For more information, see the guide for fulfilling orders after a customer pays.

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

[webhook](/webhooks)

[additional webhooks](/payments/checkout/fulfill-orders#delayed-notification)

[guide for fulfilling orders after a customer pays](/payments/checkout/fulfill-orders)

The <stripe-pricing-table> web component supports setting the client-reference-id property. When the property is set, the pricing table passes it to the Checkout Session’s client_reference_id attribute to help you reconcile the Checkout Session with your internal system. This can be an authenticated user ID or a similar string. client-reference-id can be composed of alphanumeric characters, dashes, or underscores, and be any value up to 200 characters. Invalid values are silently dropped and your pricing table will continue to work as expected.

[client_reference_id](/api/checkout/sessions/object#checkout_session_object-client_reference_id)

Since the pricing table is embedded on your website and is accessible to anyone, check that client-reference-id does not include sensitive information or secrets, such as passwords or API keys.

[https://js.stripe.com/v3/pricing-table.js](https://js.stripe.com/v3/pricing-table.js)

[OptionalAdd product marketing features](#product-marketing-features)

## OptionalAdd product marketing features

[OptionalAdd a custom call-to-action](#custom-cta)

## OptionalAdd a custom call-to-action

[OptionalPass the customer email](#customer-email)

## OptionalPass the customer email

[OptionalPass an existing customer](#customer-session)

## OptionalPass an existing customer

[OptionalCustomize the post-purchase experience](#post-purchase-experience)

## OptionalCustomize the post-purchase experience

[OptionalUpdate pricing table](#update)

## OptionalUpdate pricing table

[OptionalConfigure free trials](#free-trials)

## OptionalConfigure free trials

[OptionalContent Security Policy](#csp)

## OptionalContent Security Policy

[OptionalLet customers manage their subscriptionsNo code](#customer-portal)

## OptionalLet customers manage their subscriptionsNo code

[OptionalPresent local currencies](#price-localization)

## OptionalPresent local currencies

[OptionalAdd custom fields](#custom-fields)

## OptionalAdd custom fields

[Limitations](#limitations)

## Limitations

- Business models—The pricing table supports common subscription business models like flat-rate, per-seat, tiered pricing, and trials. Other advanced pricing models aren’t supported.

[advanced pricing models](/billing/subscriptions/usage-based/pricing-models#advanced)

- Product and price limits—You can configure the pricing table to display a maximum of four products, with up to three prices per product. You can only configure three unique pricing intervals across all products.

- Account creation—The pricing table call-to-action takes customers directly to checkout. It doesn’t currently support adding an intermediate step (for example, asking the customer to create an account on your website before checking out).

- Rate limit—The pricing table has a rate limit of up to 50 read operations per second. If you have multiple pricing tables, the rate limit is shared.

[rate limit](/rate-limits)

- Checkout redirect—The pricing table can’t redirect customers to checkout if your website provider sandboxes the embed code in an iframe without the allow-top-navigation attribute enabled. Contact your website provider to enable this setting.

- Testing the pricing table locally—The pricing table requires a website domain to render. To test the pricing table locally, run a local HTTP server to host your website’s index.html file over the localhost domain. To run a local HTTP server, use Python’s SimpleHTTPServer or the http-server npm module.

[SimpleHTTPServer](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server#running_a_simple_local_http_server)

[http-server](https://www.npmjs.com/package/http-server)

[Limit customers to one subscription](#limit-subscriptions)

## Limit customers to one subscription

You can redirect customers that already have a subscription to the customer portal or your website to manage their subscription. Learn more about limiting customers to one subscription.

[customer portal](/billing/subscriptions/customer-portal)

[limiting customers to one subscription](/payments/checkout/limit-subscriptions)
