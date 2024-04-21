htmlSet up a subscription with Cash App Pay | Stripe Documentation[Skip to content](#main-content)Cash App Pay[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fcash-app-pay)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fcash-app-pay)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Subscriptions](/docs/subscriptions)[Manage subscription cycles](/docs/billing/subscriptions/change)[Set payment methods for subscriptions](/docs/billing/subscriptions/payment-methods-setting)# Set up a subscription with Cash App Pay

Learn how to create and charge for a subscription with Cash App Pay.Use this guide to set up a subscription using Cash App Pay as a payment method.

Use SetupIntents APIUse Subscriptions APIPrebuilt checkout pageCreate and confirm a subscription using two API calls. The first API call uses the Setup Intents API to set Cash App Pay as a payment method. The second API call sends customer, product, and payment method information to the Subscriptions API to create a Subscription and confirm a payment in one call.

[Create a product and priceDashboard](#create-product-plan-code)Products represent the item or service you’re selling. Prices define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15 USD monthly subscription. To model this:

1. Navigate to the[Add a product](https://dashboard.stripe.com/test/products/create)page.
2. Enter aNamefor the product.
3. Enter15for the price.
4. SelectUSDas the currency.
5. ClickSave product.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: price_G0FvDp6vZvdwRZ.

[Create a SetupIntentServer-side](#create-setup-intent)Create a SetupIntent to save a customer’s payment method for future payments. The SetupIntent tracks the steps of this setup process.

Command Line[curl](#)`curl https://api.stripe.com/v1/setup_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d confirm=true \
  --data-urlencode return_url="https://www.stripe.com" \
  -d usage=off_session \
  -d "payment_method_data[type]"=cashapp \
  -d "payment_method_types[]"=cashapp \
  -d "mandate_data[customer_acceptance][type]"=online \
  -d "mandate_data[customer_acceptance][online][ip_address]"="127.0.0.0" \
  -d "mandate_data[customer_acceptance][online][user_agent]"=device`The returned SetupIntent includes a client secret, which the client side uses to securely complete the setup instead of passing the entire SetupIntent object. You can use different approaches to pass the client secret to the client side. The SetupIntent response also includes a payment method ID that you need to use in the next step to confirm a PaymentIntent.

The SetupIntent response includes the status requires_action, which means your users must perform another action to complete the SetupIntent. Use the next_action.cashapp_handle_redirect_or_display_qr_code object from the SetupIntent response to redirect your users to a Stripe hosted page that displays the QR code, or render the QR code directly. To authenticate users, follow the instructions to confirm SetupIntent and save a payment method. After they authenticate, the Cash App mobile application redirects users to the return_url on their mobile device, and the SetupIntent moves to a succeeded state.

[Create a subscriptionServer-side](#create-subscription)Create a subscription that has a price and customer. Set the value of the default_payment_method parameter to the PaymentMethod ID from the SetupIntent response.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscriptions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d "items[0][price]"={{PRICE_ID}} \
  -d default_payment_method={{PAYMENT_METHOD_ID}}`Included in the response is the subscription’s first PaymentIntent, containing the client secret, which you use on the client side to securely complete the payment process instead of passing the entire PaymentIntent object. Return the client_secret to the frontend to complete payment.

NoteTo create a subscription with a free trial period, see Subscription trials.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a product and price](#create-product-plan-code)[Create a SetupIntent](#create-setup-intent)[Create a subscription](#create-subscription)Products Used[Billing](/billing)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`