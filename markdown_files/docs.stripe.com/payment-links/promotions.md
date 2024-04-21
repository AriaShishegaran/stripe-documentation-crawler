htmlPromotion codes, upsells and cross-sells | Stripe Documentation[Skip to content](#main-content)Promotion codes, cross-sells, and upsells[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayment-links%2Fpromotions)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayment-links%2Fpromotions)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)
[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Payment Links](/docs/payment-links)# Promotion codes, upsells and cross-sells

Work with promotion codes, upsells and cross-sells.Payment Links lets you offer discounts using promotion codes, motivate long-term commitments with subscription upsells, and market related items during checkout through cross-sells.

[Add promotion codes](#promotion-codes)When you create a payment link in the Stripe Dashboard, you have the option of adding promotion codes. Customers can enter these codes on their payment page to apply discounts on their purchases.

Create a promotion code in the Dashboard by creating a coupon and then turning it into a customer-facing promotion code. Use the prefilled_promo_code URL parameter to prefill a promotion code when sharing a payment link. Learn more about how to generate promotion codes for Checkout.

NoteBy default, payment links create guest customers for one-time payments. As a result, promotion codes that are only eligible for first-time orders won’t work as expected.

[Increase revenue with subscription upsells](#subscription-upsells)Subscription upsells give customers the option to upgrade to a longer-term plan during checkout, such as progressing from monthly to yearly. This strategy might enhance your average order value and improve your cash flow.

You can configure a subscription upsell in the Dashboard on the Price detail page. You can view the details for a price by clicking on one you’ve added to a product. You’ll see a list of eligible upsell prices in the dropdown menu. After you select an upsell, it immediately applies to eligible payment links that use that price.

To set up a subscription upsell:

1. Choose a subscription under[Subscriptions](https://dashboard.stripe.com/subscriptions), navigate down toPricing.
2. Use the overflow menu to selectView price details.
3. Navigate down to Upsells, and in theUpsells todropdown menu, select or add a price.

![](https://b.stripecdn.com/docs-statics-srv/assets/upsell-preview.2a43c1a8acb9f167178b7fda6a2b0796.gif)

[Offer cross-sells](#cross-sells)Use cross-sells to give your customers the option to purchase related products through payment links.

To configure a cross-sell:

1. Click the desired product in[Products](https://dashboard.stripe.com/test/products), then navigate down toCross-sells.
2. From the dropdown menu, pick the product you wish to cross-sell.

Once configured, any fitting payment link and checkout page will cross-sell the designated product from the dropdown menu.

![](https://b.stripecdn.com/docs-statics-srv/assets/cross-sell-preview.cc9b1a4716015a18004f62de760cf29a.gif)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Add promotion codes](#promotion-codes)[Increase revenue with subscription upsells](#subscription-upsells)[Offer cross-sells](#cross-sells)Related Guides[Subscription upsells](/docs/payments/checkout/upsells)Products Used[Payments](/payments)[Payment Links](/payments/payment-links)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`