htmlDesigning an integration | Stripe Documentation[Skip to content](#main-content)Design an integration[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fdesigning-integration)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fdesigning-integration)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Subscriptions](/docs/subscriptions)# Designing an integration

Learn what choices you need to make to integrate subscriptions into your business.Before you start building your subscription integration, you need to choose the right integration path, especially if you’re not writing the code yourself and need to collaborate with others. Use this guide to help you decide on the best way to build your integration, and follow the links to in-depth, step-by-step guides.

This guide is for users who aren’t necessarily writing code, but want to learn about the high-level subscription integration process so that they can create plans and organize resources.

If you already know how you’re going to build your integration, or if you want to start coding right away, see our integration builder.

[Subscription models](#subscription-models)You need to understand the available subscription models to help you make later choices, such as which pricing model and payment form to use. First, consider your business model:

- If you want customers to pay, then provision access to your service, click thepay up fronttab below to learn more.
- If you want to collect payment details, then offer customers a free trial period before billing them, click thefree trialtab below to learn more.
- If you want to provide users access to your service without asking them for any payment information (afreemiummodel), click thefreemiumtab below to learn more.

Pay up frontFree trialFreemium![Pay-up-front subscription model](https://b.stripecdn.com/docs-statics-srv/assets/sub_model_pay_up_front.6b48054ef005d5ea359d56a3a07b6085.svg)

Pay-up-front model

In the pay-up-front model, you collect payment details and charge customers before provisioning access to your service. After the initial charge, you continue to charge customers the same fixed price for the same service at regular intervals. In this model, you use the Dashboard or Subscriptions API manage customer subscriptions. If you want to allow customers to modify their subscriptions directly, you need to integrate the customer portal.

For example, a photo hosting company that offers basic and premium service levels and charges customers on a monthly basis might have this setup:

- One product for the basic option
- One product for the premium option
- One price for the basic option (15EURper month)
- One price for the premium option (25EURper month)

A typical flow for this model would look like the following:

### More about webhooks in the flow

In step 3, the specific event you’re looking for is called checkout.session.completed. If you’re using Elements, provision access after receiving an invoice.paid event.

In step 4, look for an event called invoice.paid.

1. The customer chooses their plan (basic or premium).
2. You collect payment information.
3. You provision access to your service. You know when to do this by monitoring[webhook events](/webhooks).
4. You continue to provision access for customers throughout the lifecycle of the subscription. Check regularly to make sure you’re not providing access if a customer’s payment has failed.

See the integration guide to learn how to build an integration with a low-code approach that uses a prebuilt and hosted page from Stripe Checkout or a custom version with Stripe Elements.

[Metered billing](#metered-billing)If you need to meter usage, see metered billing. You need to do this when you create a price.

[Collect payment information](#collect-payment-info)If you don’t want to write a lot of code, use Checkout, Stripe’s prebuilt, hosted payment page. See the subscriptions with Checkout integration guide to get started.

If you want a more customized payment form that you can embed into your existing website, use Elements, a set of prebuilt UI elements that’s part of Stripe.js.

[Display pricing information](#pricing-table)Embed a pricing table on your website to show customers pricing information for subscriptions. When customers choose a subscription option, they’re taken directly to checkout. Configure, customize, and update directly in the Dashboard without writing any code.

[Modify subscriptions](#modify-subs)If you’re collecting payment information with Checkout, you can use the customer portal to allow customers to directly update their subscription details, like payment method and frequency. See the integration guide for detailed instructions on setting this up. (Before integrating, you should also be aware of the limitations of the portal.)

If you’re integrating with Elements, you can add a form on the frontend to collect details about the plan they want to change (such as the price ID and their customer information) and send that to an endpoint on the backend. For more details and sample code, see the section about letting customers change their plans in the Elements quickstart.

[Pricing models](#pricing-models)If you’re providing the same good every month and don’t expect that to change, use a simple fixed-price model. If the price varies depending on the number of users or units, you can use volume-based or tier-based prices. For a complete list of available models and a detailed description of each one, see examples of pricing models.

[Set up webhooks](#webhooks)Set up webhooks to receive notifications about subscription-related events. For example, when you see the invoice.paid=true notification, you can safely provision access to your service. See the subscription lifecycle for more information about webhook events. For a complete list of subscription-related events, see subscription events. To learn about managing access to your product’s feature, see the doc on integrating with entitlements.

[OptionalOther considerations](#other-considerations)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Subscription models](#subscription-models)[Metered billing](#metered-billing)[Collect payment information](#collect-payment-info)[Display pricing information](#pricing-table)[Modify subscriptions](#modify-subs)[Pricing models](#pricing-models)[Set up webhooks](#webhooks)Products Used[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`