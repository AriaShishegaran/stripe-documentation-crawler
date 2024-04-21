htmlLet customers decide what to pay | Stripe Documentation[Skip to content](#main-content)Let customers decide what to pay[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fpay-what-you-want)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fpay-what-you-want)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Checkout](/payments/checkout)·[Home](/docs)[Payments](/docs/payments)[Checkout](/docs/payments/checkout)# Let customers decide what to pay

Accept tips and donations, or sell pay-what-you-want products and services.### Inline pricing

If you maintain your product catalog outside of Stripe, you might want to use inline pricing. With inline pricing, you set inline prices for products or services when you create a Checkout Session.

You can also use inline pricing to collect donations. However, unlike pay-what-you-want pricing, you can’t reuse or update inline prices, and they’re only available through the API.

You can use this feature to collect a tip for a service provided, accept donations for a cause, or give your customers the option to pay what they want for your product or service. Go to Stripe Support to learn more about Stripe’s requirements for accepting tips or donations.

Pay-what-you-want payments have the following limitations:

- You can’t add any other line items and the quantity can only be 1.
- You can’t use promotion codes or discounts with them.
- They don’t support recurring payments or cross-sells.

![Custom amounts](https://b.stripecdn.com/docs-statics-srv/assets/custom-amount.90b3e073081926616cbb75df7f4a145d.png)

[Set up your product catalog](#product-catalog)Stripe Checkout uses Products and Prices to structure pay-what-you-want payments. In the following example, Togethere is selling tickets to a fundraising dinner and wants to allow their customers to pay what they want for their tickets.

DashboardAPITo create a pay-what-you-want model on Stripe through the Dashboard, complete these steps:

1. Create the Fundraising dinner product.

  1. Go toMore>Product catalog.
  2. Click+Add product.
  3. Enter theNameof the product (`Fundraising dinner`).
  4. (Optional)Add aDescription. The customer sees the description at checkout.


2. Create the price for the Fundraising dinner product:

  1. SelectCustomer chooses pricefor thePricing model.
  2. (Optional)Add a suggested price.
  3. (Optional)Specify limits that the customer can input.
  4. ClickSave product.



[Create a Checkout Session](#create-checkout-session)To enable customers to change the amount on the payment page, use the price ID when you create a Checkout Session. If you select Customer chooses price as your pricing model, you can’t add any other line items and the quantity can only be 1.

Stripe-hosted pageEmbedded formCommand Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  --data-urlencode cancel_url="https://example.com" \
  -d "line_items[0][price]"={{PRICE_ID}} \
  -d "line_items[0][quantity]"=1 \
  -d mode=payment \
  --data-urlencode success_url="https://example.com"`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up your product catalog](#product-catalog)[Create a Checkout Session](#create-checkout-session)Products Used[Checkout](/payments/checkout)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`