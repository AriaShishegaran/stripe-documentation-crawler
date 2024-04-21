# Designing an integration

Before you start building your subscription integration, you need to choose the right integration path, especially if you’re not writing the code yourself and need to collaborate with others. Use this guide to help you decide on the best way to build your integration, and follow the links to in-depth, step-by-step guides.

[subscription](/billing/subscriptions/creating)

This guide is for users who aren’t necessarily writing code, but want to learn about the high-level subscription integration process so that they can create plans and organize resources.

If you already know how you’re going to build your integration, or if you want to start coding right away, see our integration builder.

[integration builder](/billing/quickstart)

[Subscription models](#subscription-models)

## Subscription models

You need to understand the available subscription models to help you make later choices, such as which pricing model and payment form to use. First, consider your business model:

- If you want customers to pay, then provision access to your service, click the pay up front tab below to learn more.

- If you want to collect payment details, then offer customers a free trial period before billing them, click the free trial tab below to learn more.

- If you want to provide users access to your service without asking them for any payment information (a freemium model), click the freemium tab below to learn more.

Pay-up-front model

In the pay-up-front model, you collect payment details and charge customers before provisioning access to your service. After the initial charge, you continue to charge customers the same fixed price for the same service at regular intervals. In this model, you use the Dashboard or Subscriptions API manage customer subscriptions. If you want to allow customers to modify their subscriptions directly, you need to integrate the customer portal.

[Subscriptions API](/api/subscriptions)

[customer portal](/customer-management)

For example, a photo hosting company that offers basic and premium service levels and charges customers on a monthly basis might have this setup:

- One product for the basic option

- One product for the premium option

- One price for the basic option (15 EUR per month)

- One price for the premium option (25 EUR per month)

A typical flow for this model would look like the following:

In step 3, the specific event you’re looking for is called checkout.session.completed. If you’re using Elements, provision access after receiving an invoice.paid event.

[checkout.session.completed](/billing/subscriptions/build-subscriptions#provision-and-monitor)

[Elements](/payments/elements)

[invoice.paid](/billing/subscriptions/build-subscriptions#provision-access)

In step 4, look for an event called invoice.paid.

- The customer chooses their plan (basic or premium).

- You collect payment information.

- You provision access to your service. You know when to do this by monitoring webhook events.

[webhook events](/webhooks)

- You continue to provision access for customers throughout the lifecycle of the subscription. Check regularly to make sure you’re not providing access if a customer’s payment has failed.

See the integration guide to learn how to build an integration with a low-code approach that uses a prebuilt and hosted page from Stripe Checkout or a custom version with Stripe Elements.

[integration guide](/billing/subscriptions/build-subscriptions)

[Stripe Checkout](/payments/checkout)

[Stripe Elements](/payments/elements)

[Metered billing](#metered-billing)

## Metered billing

If you need to meter usage, see metered billing. You need to do this when you create a price.

[metered billing](/products-prices/pricing-models#usage-based-pricing)

[create a price](/products-prices/manage-prices#create-price)

[Collect payment information](#collect-payment-info)

## Collect payment information

If you don’t want to write a lot of code, use Checkout, Stripe’s prebuilt, hosted payment page. See the subscriptions with Checkout integration guide to get started.

[Checkout](/payments/checkout)

[subscriptions with Checkout](/billing/subscriptions/build-subscriptions?ui=stripe-hosted)

If you want a more customized payment form that you can embed into your existing website, use Elements, a set of prebuilt UI elements that’s part of Stripe.js.

[Elements](/payments/elements)

[Stripe.js](/payments/elements)

[Display pricing information](#pricing-table)

## Display pricing information

Embed a pricing table on your website to show customers pricing information for subscriptions. When customers choose a subscription option, they’re taken directly to checkout. Configure, customize, and update directly in the Dashboard without writing any code.

[pricing table](/payments/checkout/pricing-table)

[Dashboard](https://dashboard.stripe.com/test/pricing-tables)

[Modify subscriptions](#modify-subs)

## Modify subscriptions

If you’re collecting payment information with Checkout, you can use the customer portal to allow customers to directly update their subscription details, like payment method and frequency. See the integration guide for detailed instructions on setting this up. (Before integrating, you should also be aware of the limitations of the portal.)

[customer portal](/customer-management)

[integration guide](/billing/subscriptions/build-subscriptions?ui=stripe-hosted)

[limitations](/customer-management)

If you’re integrating with Elements, you can add a form on the frontend to collect details about the plan they want to change (such as the price ID and their customer information) and send that to an endpoint on the backend. For more details and sample code, see the section about letting customers change their plans in the Elements quickstart.

[letting customers change their plans](/billing/subscriptions/build-subscriptions?ui=elements#change-price)

[Pricing models](#pricing-models)

## Pricing models

If you’re providing the same good every month and don’t expect that to change, use a simple fixed-price model. If the price varies depending on the number of users or units, you can use volume-based or tier-based prices. For a complete list of available models and a detailed description of each one, see examples of pricing models.

[examples of pricing models](/products-prices/pricing-models)

[Set up webhooks](#webhooks)

## Set up webhooks

Set up webhooks to receive notifications about subscription-related events. For example, when you see the invoice.paid=true notification, you can safely provision access to your service. See the subscription lifecycle for more information about webhook events. For a complete list of subscription-related events, see subscription events. To learn about managing access to your product’s feature, see the doc on integrating with entitlements.

[webhooks](/billing/subscriptions/webhooks)

[the subscription lifecycle](/billing/subscriptions/overview#subscription-lifecycle)

[webhook](/webhooks)

[subscription events](/billing/subscriptions/overview#subscription-events)

[integrating with entitlements](/billing/entitlements)

[OptionalOther considerations](#other-considerations)

## OptionalOther considerations
