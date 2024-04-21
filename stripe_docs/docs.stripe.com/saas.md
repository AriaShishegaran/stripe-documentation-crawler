# Integrate a SaaS business on Stripe

Many Stripe users have a SaaS business model that involves subscriptions or recurring payments. This guide describes the unique actions you need to take in your Stripe integration to support typical SaaS business models. To help get you started more quickly, this guide presents no-code options where available.

Product modeling

[Product modeling](#modeling)

Create a product to represent your service plan and configure a pricing model that reflects your recurring revenue model.

Learn more about the different pricing models that Stripe supports.

[different pricing models that Stripe supports](/products-prices/pricing-models)

Entitlements

[Entitlements](/billing/entitlements)

Use Entitlements to determine when you can grant or revoke product feature access to your customers.

Learn how to set up Entitlements.

[how to set up Entitlements](/billing/entitlements)

Pricing table

[Pricing table](#pricing)

Use a pricing table to show pricing information to your customers and take them to Checkout.

Learn more about pricing tables.

[pricing tables](/payments/checkout/pricing-table)

Trials

[Trials](#trials)

Offer customers a free trial of your service.

Learn more about how trials work with subscriptions.

[trials work with subscriptions](/billing/subscriptions/trials)

Discounts

[Discounts](#discounts)

Apply discounts to your products.

Learn how to apply discounts to your subscriptions with coupons and promotion codes.

[apply discounts to your subscriptions with coupons and promotion codes](/billing/subscriptions/coupons)

Subscription management

[Subscription management](#subscriptions)

Set up the customer portal to let your customers manage their subscriptions.

Learn how to set up the customer portal.

[set up the customer portal](/customer-management)

Invoices

[Invoices](#invoices)

Send invoices to customers for custom deals, one-off items, or to test pricing for new products.

Learn how to send invoices to your customers.

[send invoices to your customers](/invoicing/quickstart-guide)

Tax

[Tax](#tax)

Use Stripe Tax to automatically charge sales tax, value-added tax (VAT), and goods and services tax (GST).

Learn how to collect taxes for recurring payments.

[collect taxes for recurring payments](/tax)

Monitor subscription activity

[Monitor subscription activity](#monitor)

Set up webhook endpoints to listen to event notifications and handle upgrades, downgrades, payment failures, customer updates, and other scenarios.

Learn more about the relevant webhook events for subscriptions.

[relevant webhook events for subscriptions](/billing/subscriptions/webhooks)

Recover revenue

[Recover revenue](#retries)

Use recovery tools like Smart Retries and reminder emails to recover revenue that would be lost to involuntary churn.

Learn more about revenue recovery tools.

[revenue recovery tools](/billing/revenue-recovery)

Revenue recognition

[Revenue recognition](#recurring-revenue)

Set up revenue recognition to automate revenue reporting including compliance with accrual accounting rules.

Learn how Stripe Revenue Recognition automates revenue recognition from subscriptions and invoices.

[automates revenue recognition from subscriptions and invoices](/revenue-recognition)

Testing

[Testing](#test)

Test your integration to make sure it works as expected.

Learn how to test your integration using test clocks.

[test your integration using test clocks](/billing/testing)

[Product modeling](#modeling)

## Product modeling

Set up pricing structures for different products. Stripe Billing supports many types of pricing models, including:

- Flat rate-Good-better-best

- Per-seat

- Usage-based pricing

- Tiered pricing

- Multiple prices

- Multiple products in a subscription

Learn more about product modeling.

[product modeling](/products-prices/pricing-models)

[Display pricing information](#pricing)

## Display pricing information

The pricing table is an embeddable UI component that displays pricing models for different subscription options. With pricing tables, customers can view pricing information and select a subscription. After selecting a subscription, they can complete the purchase with Stripe Checkout. Learn more about pricing tables for SaaS businesses.

[pricing tables for SaaS businesses](/payments/checkout/pricing-table)

Embed a pricing table on your website to display pricing details and convert customers to checkout.

[Enable discounts](#discounts)

## Enable discounts

Use discounts to acquire new subscribers. You can create coupons and apply them to a subscription or create a customer-facing promotion code that customers can apply at checkout. Learn more about discounts for subscriptions.

[discounts for subscriptions](/billing/subscriptions/coupons)

[Offer trials](#trials)

## Offer trials

Let customers try your product before subscribing. With Stripe Checkout, they can sign up for a trial without submitting payment information. You can configure a subscription to automatically send a reminder email when the trial is about to expire. Learn more about trials.

[trials](/payments/checkout/free-trials)

[Manage subscriptions](#subscriptions)

## Manage subscriptions

The customer portal lets customers manage their subscriptions in a self-serve environment where they can:

- Update their subscription plan

- Cancel their subscription plan

- Add or update a payment method

- Update billing and shipping information

- Review their invoice history

Learn more about integrating the customer portal.

[integrating the customer portal](/customer-management)

Customer portal

[Set up invoices](#invoices)

## Set up invoices

Invoices represent how much money a customer owes, and Stripe automatically generates one for every period in a subscription billing cycle. You can also create an invoice manually for custom deals or one-time payments. When an invoice is due, Stripe tries to collect payment by either automatically charging the payment method on file, or emailing the invoice. Learn more about invoices.

[invoices](/invoicing)

Hosted Invoice Page

[Monitor subscription activity](#monitor)

## Monitor subscription activity

Monitor subscriptions in the Dashboard or set up webhook endpoints and listen for events. Learn more about subscriptions and webhooks.

[subscriptions and webhooks](/billing/subscriptions/webhooks)

[Reduce involuntary churn](#retries)

## Reduce involuntary churn

Use tools that can help prevent involuntary churn. Smart Retries and reminder emails are available as part of the Billing Scale plan. Learn more about revenue recovery tools.

[revenue recovery tools](/billing/revenue-recovery)

[Manage sales tax](#tax)

## Manage sales tax

After you register to collect taxes, Stripe Tax determines your customer’s location, and automatically calculates and collects the correct amount of tax at checkout. Stripe Tax supports sales tax, VAT, and GST. Learn more about Stripe Tax.

[Stripe Tax](/tax)

[Automate revenue recognition](#recurring-revenue)

## Automate revenue recognition

Use Stripe Revenue Recognition to automate revenue reporting and stay compliant with rules for accrual accounting. Stripe Revenue Recognition automates revenue accounting based on your payments and billing transactions.

Learn more about Revenue Recognition.

[Revenue Recognition](/revenue-recognition)

[Test your integration](#test)

## Test your integration

Test your integration to make sure it behaves as you expect. With test clocks, you can simulate how a subscription integration would handle events such as trials and payment failures over a billing cycle. Learn more about testing subscriptions integrations.

[testing subscriptions integrations](/billing/testing)
