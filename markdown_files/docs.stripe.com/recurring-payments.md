htmlRecurring payments | Stripe Documentation[Skip to content](#main-content)Recurring payments[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frecurring-payments)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frecurring-payments)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)
[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[About Stripe payments](/docs/payments/online-payments)# Recurring payments

Understand your options for charging customers on a recurring basis.Stripe offers several ways to charge customers on a recurring basis. This guide helps you understand which method or approach best supports your business.

This guide offers a few ways to understand your options:

- [Use cases](#use-cases): Find the right use case for your business.
- [Types of recurring payments](#recurring-payment-types): See all the recurring payment types that Stripe supports.
- [Stripe products](#stripe-products): Check which Stripe products support your recurring payment use case.

[Use cases](#use-cases)[Accept recurring paymentsLet customers pay you regularly and repeatedly through Stripe.](/recurring-payments#accept-recurring-payments)[Split purchases into a few paymentsCreate installment plans to let customers pay you a total amount in a limited number of partial payments.](/recurring-payments#installment-plans)[Enable customers to manage their own subscriptionsSet up the customer portal so your customers can create and manage their own subscriptions.](/recurring-payments#enable-customer-portal)[Accept recurring donationsLet customers make donations to your organization on a regular basis.](/recurring-payments#recurring-donations)[Migrate existing subscriptions to StripeMove your existing subscriptions from a third-party service to Stripe.](/recurring-payments#migrate-subscriptions)[Types of recurring payments](#recurring-payment-types)The following tabs describe the different types of recurring payments that Stripe supports.

SubscriptionsInstallmentsRecurring invoicesCharges on saved payment methodsOverview

Use Stripe Billing to create and manage your subscriptions through the Dashboard or programmatically through the API.

- [Create a payment link with a recurring product](/payment-links/create).
- Create a subscription through the[Dashboard](https://dashboard.stripe.com/subscriptions)or[build a subscriptions integration](/billing/subscriptions/build-subscriptions).
- Create[subscription schedules](/billing/subscriptions/subscription-schedules)for complex subscription use cases.
- If you use Connect,[create subscriptions](/connect/subscriptions)for connected accounts and end customers.

Features- No coding required. (You can optionally use the Subscriptions API and prebuilt components like Stripe Checkout and Elements to build a programmatic subscriptions integration.)
- Customize appearance and behavior in your app.
- Supports multiple products and prices in different currencies.
- Supports responsive web and mobile native.
- Website required. You can use Stripe Elements to customize the appearance of payment forms.

Use cases- [Accept payments from customers on a recurring basis](#accept-recurring-payments)
- [Accept recurring donations](#recurring-donations)
- [Enable customers to manage their own subscriptions](#enable-customer-portal)
- [Migrate existing subscriptions to Stripe](#migrate-subscriptions)

[Stripe products for recurring payments](#stripe-products)The following table describes which Stripe products support recurring payments.

ProductFeaturesUse casesPayment Links- No coding
- Customize branding
- One payment link for one or more products
- Mobile support for responsive web
- No website required; share link through SMS, email, or social media
- [Stripe Tax](/tax)support

- [Accept recurring payments](#accept-recurring-payments)
- [Enable customers to manage their own subscriptions](#enable-customer-portal)
- [Accept recurring donations](#recurring-donations)

Invoicing- No coding required. (You can optionally use the[Invoices API](/api/invoices)and prebuilt components like Stripe Checkout and Elements to build a programmatic invoicing integration.)
- Customize branding and templates.
- One invoice for one or more products. Optionally combine one-time and recurring products.
- Mobile support for responsive web.
- No website required. Share invoices through customer portal, hosted invoice page, or as PDFs.
- [Stripe Tax](/tax)support.

- [Accept recurring payments](#accept-recurring-payments)
- [Enable customers to manage their own subscriptions](#enable-customer-portal)
- [Accept recurring donations](#recurring-donations)

Subscriptions- No coding required. (You can optionally use the[Subscriptions API](/api/subscriptions)and prebuilt components like Stripe Checkout and Elements to build a programmatic subscriptions integration.)
- Customize full appearance of payment forms and checkout experience.
- Multiple products, prices, pricing models, and currencies.
- Mobile support for responsive web.
- No website required. You can also add subscriptions to your site.
- [Stripe Tax](/tax)support.

- [Accept recurring payments](#accept-recurring-payments)
- [Enable customers to manage their own subscriptions](#enable-customer-portal)
- [Accept recurring donations](#recurring-donations)

Checkout- Minimal coding
- Customize branding
- Multiple products and prices in different currencies
- Mobile support for responsive web
- Website required, but Stripe hosts the payment page
- [Stripe Tax](/tax)support

- [Accept recurring payments](#accept-recurring-payments)
- [Enable customers to manage their own subscriptions](#enable-customer-portal)
- [Split purchases into a few payments](#installment-plans)
- [Accept recurring donations](#recurring-donations)

Elements- More coding
- Customize full appearance
- Multiple products and prices in different currencies
- Responsive web and mobile native
- Website required; you add Elements to your payment page
- [Stripe Tax](/tax)supported with your own[tax integration](/tax/custom)

- [Accept recurring payments](#accept-recurring-payments)
- [Enable customers to manage their own subscriptions](#enable-customer-portal)
- [Split purchases into a few payments](#installment-plans)
- [Accept recurring donations](#recurring-donations)

API- Most coding
- Customize full appearance, accept payments through your own UI
- Multiple products and prices in different currencies
- Website required; accept payments through your own UI
- [Stripe Tax](/tax)supported with your own[tax integration](/tax/custom)

- [Accept recurring payments](#accept-recurring-payments)
- [Enable customers to manage their own subscriptions](#enable-customer-portal)
- [Split purchases into a few payments](#installment-plans)
- [Accept recurring donations](#recurring-donations)

[Accept recurring payments](#accept-recurring-payments)Stripe offers several ways for you to accept recurring payments. Use Subscriptions with Stripe Billing, PaymentIntents, SetupIntents, or Invoicing.

### Use subscriptions to accept recurring payments

### Save and reuse payment information for recurring charges

### Use invoices to automatically charge customers

[Split purchases into a few payments](#installment-plans)Offer your customers payment plans in installments with Subscription Schedules API (part of Stripe Billing) or buy now, pay later methods. If your business is based in Mexico, you can offer card payments in installments.

### Create an installment plan with Subscription Schedules

### Use a buy now, pay later payment method

### Accept card payments in installments

[Enable customers to manage their own subscriptions](#enable-customer-portal)If you want your customers to manage their own accounts and recurring subscriptions, use the customer portal. Stripe hosts the customer portal, which allows your customers to self-manage their payment details, download invoices, and manage their subscriptions in one place. Read the no-code customer portal guide for complete details.

Integrate with the customer portal API

### Set up the customer portal

See what your customers can do in the customer portal

View demo

[Accept recurring donations](#recurring-donations)You can accept recurring donations with Stripe, in the same way as recurring payments. For example, imagine a llama rescue organization, Llama House. They want to make it easy for supporters to choose an amount for a recurring, monthly donation. They use Payment Links to create a link that they can share on social media and email. From the same payment link, they also generate a QR code that they can add to flyers, and an embeddable buy button for their website–all from the Dashboard.

### Accept recurring donations with Payment Links

[Migrate existing subscriptions to Stripe](#migrate-subscriptions)If you have existing subscriptions in another system, you can migrate them to Stripe Billing. Read the guide for more information.

## See also

- [Get an overview of subscriptions](/billing)
- [Create a payment link](/payment-links/create)
- [Add an Apple Pay merchant token for recurring payments](/apple-pay/merchant-tokens)
- [Get started with no-code invoices](/invoicing/quickstart-guide)
- [Save payment details during a payment to set up future payments](/payments/save-during-payment)
- [Save card details to set up future payments](/payments/save-and-reuse)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Use cases](#use-cases)[Types of recurring payments](#recurring-payment-types)[Stripe products for recurring payments](#stripe-products)[Accept recurring payments](#accept-recurring-payments)[Split purchases into a few payments](#installment-plans)[Enable customers to manage their own subscriptions](#enable-customer-portal)[Accept recurring donations](#recurring-donations)[Migrate existing subscriptions to Stripe](#migrate-subscriptions)[See also](#see-also)Products Used[Billing](/billing)[Invoicing](/invoicing)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`