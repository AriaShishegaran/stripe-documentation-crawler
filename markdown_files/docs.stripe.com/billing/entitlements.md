htmlEntitlements | Stripe Documentation[Skip to content](#main-content)Entitlements[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fentitlements)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fentitlements)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)# Entitlements

Determine when you can grant or revoke product feature access to customers.Entitlements enable you to map the features of your internal service to Stripe products. After you map your features, Stripe notifies you about when to provision or de-provision access (according to your customer’s subscription status), and to what features, based on your mapping choices.

Use Entitlements to:

- Launch, change, and experiment with your pricing without needing to change your codebase
- Grant, revoke, and manage customer’s feature access
- Simplify your billing integration

Stripe Billing Entitlements API demo

## Before you begin

This guide assumes that you’re already using Stripe Subscriptions and Customer resources.

[Get started](#how-it-works)To get started with Entitlements:

- Set up your features: Create each feature in Stripe Billing using the[Feature API](/api/entitlements/feature/object). For example, “Email” or “SMS” are separate individual features.
- Add your features to products: Attach Features to corresponding Stripe Products. You can add a single feature to multiple products.
- Get customers’ active entitlements: When customers subscribe to your products, Stripe Billing entitles the customer to the product’s features. Listen to the[Active Entitlement Summary webhook](#webhooks)and use the[List Active Entitlements API](/api/entitlements/active-entitlement/list)for a given customer to execute your feature provisioning process.

![Diagram with Entitlements and its relationship with a Customer and Product's features](https://b.stripecdn.com/docs-statics-srv/assets/entitlements-diagram.de0913d5f1a652c0576999c1746d3e75.svg)

[Set up your features](#setup)Provide a name and a unique lookup_key for each feature you create. Because the lookup_key is unique to each feature, you can’t reuse it across different features.

Command Line[curl](#)`curl https://api.stripe.com/v1/entitlements/features \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d name="My feature" \
  -d lookup_key=myinternalfeaturecode`[Add your features to products](#assign)Assign your feature to one or more products.

NoteExisting subscriptions will create active entitlements for any product feature changes at the start of the next billing period.

Command Line[curl](#)`curl https://api.stripe.com/v1/products/{{PRODUCT_ID}}/features \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d entitlement_feature={{ENTITLEMENTS_FEATURE_ID}}`After you submit a request to attach your feature to your product, you receive a response similar to the following:

`{
  "id": "{{PRODUCT_FEATURE_ID}}",
  "object": "product_feature",
  "entitlement_feature": {
    "id": "{{ENTITLEMENTS_FEATURE_ID}}",
    "object": "entitlements.feature",
    "name": "My feature",
    "lookup_key": "myinternalfeaturecode"
  }
}`List the features attached to a product by paging through the list of product features:

Command Line[curl](#)`curl https://api.stripe.com/v1/products/{{PRODUCT_ID}}/features \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`And remove a feature from a specific product by deleting the product feature attachment:

Command Line[curl](#)`curl -X DELETE https://api.stripe.com/v1/products/{{PRODUCT_ID}}/features/{{PRODUCT_FEATURE_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`[Get customers' active entitlements](#entitlements)During the lifecycle of a customer’s subscription, from activation, through upgrades, downgrades, and so on, Stripe updates the customer’s entitlements based on your mapped features.

When a customer’s subscription is first activated, Stripe creates entitlements for the features that they’re subscribed to.

As long as a customer maintains an active subscription for a feature, they retain an active entitlement. Make sure you provision access in your system for any users entitled to this feature.

### Listen for webhook events

If your webhooks are enabled, we send the following webhook event to notify you when a customer’s entitlements change.

Limited entitlements available in summary webhookThe entitlement summary’s active_entitlements property only contains a maximum of 10 entitlements. We also provide a URL to retrieve the full, paginated list of the customer’s entitlements.

EventDescription`entitlements.active_entitlement_summary.updated`Occurs each time a customer’s active entitlements change.### Retrieve the list of all active entitlements for a customer

The list endpoint returns paginated view of a customer’s active entitlements.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/entitlements/active_entitlements \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}}`RecommendationWe recommend you persist these entitlements internally for faster resolution.

NoteSubscription pricing, plan, and entitlement changes might be subject to certain legal requirements. Consult with your legal counsel for advice specific to your business.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Get started](#how-it-works)[Set up your features](#setup)[Add your features to products](#assign)[Get customers' active entitlements](#entitlements)Products Used[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`