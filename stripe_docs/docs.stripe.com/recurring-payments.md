# Recurring payments

Stripe offers several ways to charge customers on a recurring basis. This guide helps you understand which method or approach best supports your business.

This guide offers a few ways to understand your options:

- Use cases: Find the right use case for your business.

[Use cases](#use-cases)

- Types of recurring payments: See all the recurring payment types that Stripe supports.

[Types of recurring payments](#recurring-payment-types)

- Stripe products: Check which Stripe products support your recurring payment use case.

[Stripe products](#stripe-products)

[Use cases](#use-cases)

## Use cases

[Accept recurring paymentsLet customers pay you regularly and repeatedly through Stripe.](/recurring-payments#accept-recurring-payments)

Let customers pay you regularly and repeatedly through Stripe.

[Split purchases into a few paymentsCreate installment plans to let customers pay you a total amount in a limited number of partial payments.](/recurring-payments#installment-plans)

Create installment plans to let customers pay you a total amount in a limited number of partial payments.

[Enable customers to manage their own subscriptionsSet up the customer portal so your customers can create and manage their own subscriptions.](/recurring-payments#enable-customer-portal)

Set up the customer portal so your customers can create and manage their own subscriptions.

[Accept recurring donationsLet customers make donations to your organization on a regular basis.](/recurring-payments#recurring-donations)

Let customers make donations to your organization on a regular basis.

[Migrate existing subscriptions to StripeMove your existing subscriptions from a third-party service to Stripe.](/recurring-payments#migrate-subscriptions)

Move your existing subscriptions from a third-party service to Stripe.

[Types of recurring payments](#recurring-payment-types)

## Types of recurring payments

The following tabs describe the different types of recurring payments that Stripe supports.

Overview

Use Stripe Billing to create and manage your subscriptions through the Dashboard or programmatically through the API.

[Stripe Billing](/billing)

- Create a payment link with a recurring product.

[Create a payment link with a recurring product](/payment-links/create)

- Create a subscription through the Dashboard or build a subscriptions integration.

[Dashboard](https://dashboard.stripe.com/subscriptions)

[build a subscriptions integration](/billing/subscriptions/build-subscriptions)

- Create subscription schedules for complex subscription use cases.

[subscription schedules](/billing/subscriptions/subscription-schedules)

- If you use Connect, create subscriptions for connected accounts and end customers.

[create subscriptions](/connect/subscriptions)

- No coding required. (You can optionally use the Subscriptions API and prebuilt components like Stripe Checkout and Elements to build a programmatic subscriptions integration.)

- Customize appearance and behavior in your app.

- Supports multiple products and prices in different currencies.

- Supports responsive web and mobile native.

- Website required. You can use Stripe Elements to customize the appearance of payment forms.

- Accept payments from customers on a recurring basis

[Accept payments from customers on a recurring basis](#accept-recurring-payments)

- Accept recurring donations

[Accept recurring donations](#recurring-donations)

- Enable customers to manage their own subscriptions

[Enable customers to manage their own subscriptions](#enable-customer-portal)

- Migrate existing subscriptions to Stripe

[Migrate existing subscriptions to Stripe](#migrate-subscriptions)

[Stripe products for recurring payments](#stripe-products)

## Stripe products for recurring payments

The following table describes which Stripe products support recurring payments.

- No coding

- Customize branding

- One payment link for one or more products

- Mobile support for responsive web

- No website required; share link through SMS, email, or social media

- Stripe Tax support

[Stripe Tax](/tax)

- Accept recurring payments

[Accept recurring payments](#accept-recurring-payments)

- Enable customers to manage their own subscriptions

[Enable customers to manage their own subscriptions](#enable-customer-portal)

- Accept recurring donations

[Accept recurring donations](#recurring-donations)

- No coding required. (You can optionally use the Invoices API and prebuilt components like Stripe Checkout and Elements to build a programmatic invoicing integration.)

[Invoices API](/api/invoices)

- Customize branding and templates.

- One invoice for one or more products. Optionally combine one-time and recurring products.

- Mobile support for responsive web.

- No website required. Share invoices through customer portal, hosted invoice page, or as PDFs.

- Stripe Tax support.

[Stripe Tax](/tax)

- Accept recurring payments

[Accept recurring payments](#accept-recurring-payments)

- Enable customers to manage their own subscriptions

[Enable customers to manage their own subscriptions](#enable-customer-portal)

- Accept recurring donations

[Accept recurring donations](#recurring-donations)

- No coding required. (You can optionally use the Subscriptions API and prebuilt components like Stripe Checkout and Elements to build a programmatic subscriptions integration.)

[Subscriptions API](/api/subscriptions)

- Customize full appearance of payment forms and checkout experience.

- Multiple products, prices, pricing models, and currencies.

- Mobile support for responsive web.

- No website required. You can also add subscriptions to your site.

- Stripe Tax support.

[Stripe Tax](/tax)

- Accept recurring payments

[Accept recurring payments](#accept-recurring-payments)

- Enable customers to manage their own subscriptions

[Enable customers to manage their own subscriptions](#enable-customer-portal)

- Accept recurring donations

[Accept recurring donations](#recurring-donations)

- Minimal coding

- Customize branding

- Multiple products and prices in different currencies

- Mobile support for responsive web

- Website required, but Stripe hosts the payment page

- Stripe Tax support

[Stripe Tax](/tax)

- Accept recurring payments

[Accept recurring payments](#accept-recurring-payments)

- Enable customers to manage their own subscriptions

[Enable customers to manage their own subscriptions](#enable-customer-portal)

- Split purchases into a few payments

[Split purchases into a few payments](#installment-plans)

- Accept recurring donations

[Accept recurring donations](#recurring-donations)

- More coding

- Customize full appearance

- Multiple products and prices in different currencies

- Responsive web and mobile native

- Website required; you add Elements to your payment page

- Stripe Tax supported with your own tax integration

[Stripe Tax](/tax)

[tax integration](/tax/custom)

- Accept recurring payments

[Accept recurring payments](#accept-recurring-payments)

- Enable customers to manage their own subscriptions

[Enable customers to manage their own subscriptions](#enable-customer-portal)

- Split purchases into a few payments

[Split purchases into a few payments](#installment-plans)

- Accept recurring donations

[Accept recurring donations](#recurring-donations)

- Most coding

- Customize full appearance, accept payments through your own UI

- Multiple products and prices in different currencies

- Website required; accept payments through your own UI

- Stripe Tax supported with your own tax integration

[Stripe Tax](/tax)

[tax integration](/tax/custom)

- Accept recurring payments

[Accept recurring payments](#accept-recurring-payments)

- Enable customers to manage their own subscriptions

[Enable customers to manage their own subscriptions](#enable-customer-portal)

- Split purchases into a few payments

[Split purchases into a few payments](#installment-plans)

- Accept recurring donations

[Accept recurring donations](#recurring-donations)

[Accept recurring payments](#accept-recurring-payments)

## Accept recurring payments

Stripe offers several ways for you to accept recurring payments. Use Subscriptions with Stripe Billing, PaymentIntents, SetupIntents, or Invoicing.

[Split purchases into a few payments](#installment-plans)

## Split purchases into a few payments

Offer your customers payment plans in installments with Subscription Schedules API (part of Stripe Billing) or buy now, pay later methods. If your business is based in Mexico, you can offer card payments in installments.

[Subscription Schedules API](/api/subscription_schedules)

[Enable customers to manage their own subscriptions](#enable-customer-portal)

## Enable customers to manage their own subscriptions

If you want your customers to manage their own accounts and recurring subscriptions, use the customer portal. Stripe hosts the customer portal, which allows your customers to self-manage their payment details, download invoices, and manage their subscriptions in one place. Read the no-code customer portal guide for complete details.

[no-code customer portal guide](/customer-management/activate-no-code-customer-portal)

Integrate with the customer portal API

[Integrate with the customer portal API](/customer-management/integrate-customer-portal)

See what your customers can do in the customer portal

View demo

[View demo](https://billing.stripe.com/customer-portal-demo)

[Accept recurring donations](#recurring-donations)

## Accept recurring donations

You can accept recurring donations with Stripe, in the same way as recurring payments. For example, imagine a llama rescue organization, Llama House. They want to make it easy for supporters to choose an amount for a recurring, monthly donation. They use Payment Links to create a link that they can share on social media and email. From the same payment link, they also generate a QR code that they can add to flyers, and an embeddable buy button for their website–all from the Dashboard.

[Migrate existing subscriptions to Stripe](#migrate-subscriptions)

## Migrate existing subscriptions to Stripe

If you have existing subscriptions in another system, you can migrate them to Stripe Billing. Read the guide for more information.

[the guide](/billing/subscriptions/migrate-subscriptions)

## See also

- Get an overview of subscriptions

[Get an overview of subscriptions](/billing)

- Create a payment link

[Create a payment link](/payment-links/create)

- Add an Apple Pay merchant token for recurring payments

[Add an Apple Pay merchant token for recurring payments](/apple-pay/merchant-tokens)

- Get started with no-code invoices

[Get started with no-code invoices](/invoicing/quickstart-guide)

- Save payment details during a payment to set up future payments

[Save payment details during a payment to set up future payments](/payments/save-during-payment)

- Save card details to set up future payments

[Save card details to set up future payments](/payments/save-and-reuse)
