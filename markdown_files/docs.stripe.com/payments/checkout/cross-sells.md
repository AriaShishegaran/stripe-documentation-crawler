htmlCross-sells | Stripe Documentation[Skip to content](#main-content)Configure cross-sells[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcross-sells)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcross-sells)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Checkout](/payments/checkout)·[Home](/docs)[Payments](/docs/payments)[Checkout](/docs/payments/checkout)# Cross-sells

Enable customers to purchase complementary products at checkout by using cross-sells.![Cross-sell product in Checkout](https://b.stripecdn.com/docs-statics-srv/assets/cross-sell-session.32236b96e980634a6c0060050eea5dbf.png)

A cross-sell is a product that you can add to an order using Checkout.

Cross-sells enable customers to optionally purchase other related products using Checkout. Cross-sells can increase your average order value and revenue.

For Checkout to offer a product as a cross-sell, the product must meet the following criteria:

- The product must be associated with only a single[Price](/api/prices/object#price_object-product).
- The[currency](/api/prices/object#price_object-currency)of the cross-sell product’s price must match the currency of the other prices in the Checkout Session.
- If the cross-sell product’s price[type](/api/prices/object#price_object-type)is`recurring`, the Checkout Session must be in subscription mode and its recurring interval must match the recurring interval of the other prices in the Checkout Session.
- If you’re using[subscription upsells](/payments/checkout/upsells), cross-sells only support products with non-recurring prices. For example, you can cross-sell a one-time setup fee while also upselling a monthly subscription to annual billing.
- If you’re using[automatic taxes](/tax), cross-sells only support products with prices with specified[tax behavior](/tax/products-prices-tax-codes-tax-behavior#tax-behavior). You can either[set tax behavior for a price](/tax/products-prices-tax-codes-tax-behavior#setting-tax-behavior-on-a-price-(optional))or set the default tax behavior for all prices under[Tax Settings](https://dashboard.stripe.com/test/settings/tax)in the Stripe Dashboard.

## Create a cross-sell

![Configure a cross-sell on the Product detail page](https://b.stripecdn.com/docs-statics-srv/assets/add-cross-sell.685564769c217a27f88b9ab9605d9c65.gif)

Configure a cross-sell on the Product detail page.

You can configure a cross-sell in the Dashboard on the Product details page. Visit the Product details page for the product from which you want to cross-sell another complementary product. You’ll see a Cross-sells section with a dropdown menu containing your other Products. Select a Product with a single Price. After you configure it, all eligible Checkout Sessions cross-sell the product selected from the dropdown menu. For example, a customer purchasing a ‘Togethere Professional’ subscription would be cross-sold the ‘Professional Services: Deployment’ product.

## Checkout experience

In Checkout, buyers see an option to add the cross-sell to their purchase. If buyers add the cross-sell to the Checkout Session, they can also remove it. If they remove it, the option to add the cross-sell appears again.

NoteThe quantity of cross-sell line items cannot be adjusted. The current maximum is 1.

![Customer preview of a cross-sell on the Product detail page](https://b.stripecdn.com/docs-statics-srv/assets/cross-sell-preview.cc9b1a4716015a18004f62de760cf29a.gif)

Customer preview.

## Retrieve Checkout Session line items

After a customer adds a cross-sell, the line_items for the Checkout Session update to reflect the addition. When fulfilling your order using the checkout.session.completed webhook, make sure to retrieve the line items.

## Remove a cross-sell

To remove a cross-sell, click the x next to it. After you remove it, the product won’t be offered to any new Checkout Sessions.

![Remove a cross-sell from the Product detail page](https://b.stripecdn.com/docs-statics-srv/assets/remove-cross-sell.a08765b1278a8187c282964f89641b92.gif)

Remove a cross-sell.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a cross-sell](#create-cross-sell)[Checkout experience](#checkout-experience)[Retrieve Checkout Session line items](#line-items)[Remove a cross-sell](#remove-cross-sell)Products Used[Checkout](/payments/checkout)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`