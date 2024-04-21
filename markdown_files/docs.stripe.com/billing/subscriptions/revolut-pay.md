htmlSet up a subscription with Revolut Pay | Stripe Documentation[Skip to content](#main-content)Revolut Pay[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Frevolut-pay)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Frevolut-pay)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Subscriptions](/docs/subscriptions)[Manage subscription cycles](/docs/billing/subscriptions/change)[Set payment methods for subscriptions](/docs/billing/subscriptions/payment-methods-setting)# Set up a subscription with Revolut PayBeta

Learn how to create and charge for a subscription with Revolut Pay.Use this guide to set up a subscription using Revolut Pay as a payment method.

NoteCurrently, only gated businesses have access to use this payment method. Email us at revolutpay-beta@stripe.com to gain access.

SetupIntents APISubscriptions APIPrebuilt checkout pageYou can use the Checkout API to create and confirm a subscription with a prebuilt checkout page.

[Create a product and priceDashboard](#create-product-plan-code)Products represent the item or service you’re selling. Prices define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15 GBP monthly subscription. To model this:

1. Navigate to the[Add a product](https://dashboard.stripe.com/test/products/create)page.
2. Enter aNamefor the product.
3. Enter15for the price.
4. SelectGBPas the currency.
5. ClickSave product.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: price_G0FvDp6vZvdwRZ.

[Create a Checkout SessionServer-side](#web-create-checkout-session)Your customer must authorize you to use their Revolut account for future payments through Stripe Checkout. This allows you to accept Revolut payments. Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

index.html`<html>
  <head>
    <title>Checkout</title>
  </head>
  <body>
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>`Create a Checkout Session in subscription mode to collect the required information. After creating the Checkout Session, redirect your customer to the URL that the response returns.

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  --data-urlencode success_url="https://example.com/success" \
  --data-urlencode cancel_url="https://example.com/cancel" \
  -d "line_items[0][price]"={{RECURRING_PRICE_ID}} \
  -d "line_items[0][quantity]"=1 \
  -d "payment_method_types[0]"=card \
  -d "payment_method_types[1]"=revolut_pay \
  -d mode=subscription`[Test your integrationServer-side](#web-test-integration)Select Revolut Pay as the payment method and tap Subscribe. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent transitions from requires_action to succeeded.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a product and price](#create-product-plan-code)[Create a Checkout Session](#web-create-checkout-session)[Test your integration](#web-test-integration)Products Used[Billing](/billing)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`