htmlSubscription upsells | Stripe Documentation[Skip to content](#main-content)Configure subscription upsells[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fupsells)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fupsells)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Checkout](/payments/checkout)·[Home](/docs)[Payments](/docs/payments)[Checkout](/docs/payments/checkout)# Subscription upsells

Enable customers to upgrade their subscription plan at checkout by using upsells.## Subscription upsells

Subscription upsells give customers the option to upgrade to a longer-term plan using Checkout. Upselling customers to longer subscription intervals (for example, from monthly to yearly) can increase your average order value and cash flow.

All recurring prices that aren’t metered are eligible to use subscription upsells. For any eligible price, you can set up a subscription upsell to another price that meets the following criteria:

- Prices must reference the same[Product](/api/prices/object#price_object-product).
- Prices must have the same[currency](/api/prices/object#price_object-currency).
- Prices must be`recurring`[type](/api/prices/object#price_object-type).
- If your prices use[tax behavior](/api/prices/object#price_object-tax_behavior), their values must be identical.
- If your price uses[tiers](/api/prices/object#price_object-tiers), the value for`up_to`in each tier must be identical.
- If using[quantity transformation](/api/prices/object#price_object-transform_quantity), the values for`divide_by`and`round`must be identical.

## Create a subscription upsell

Configure a subscription upsell in the Dashboard on the Price detail page (to view the details for a Price, click on a Product, then click a price that’s been added to a Product). In the Upsells section, select an upsell price from the dropdown menu. Upsells immediately apply to eligible Checkout Sessions that use that price.

![Configure a subscription upsell on the Price detail page](https://b.stripecdn.com/docs-statics-srv/assets/add-upsell.08bc9bf9425295edb1ada9ff297ee257.gif)

Configure a subscription upsell on the Price detail page.

## Checkout experience

During checkout, customers see an option to select the upsell with savings displayed, if applicable. For a Checkout Session to be eligible for upsells, it must:

- Be a subscription mode Checkout Session
- Have only one`type=recurring`price in the Checkout Session
- Have a valid configuration for the upsell price

Stripe calculates savings based on the amount the user would save in one billing cycle if they chose upsell pricing. For example, a monthly subscription of 100 USD that upsells to an annual subscription of 1000 USD shows savings of 200 USD. Savings are displayed as an amount or a percentage, depending on the character length of the savings.

Users can toggle between the initial price option and the upsell price option and then checkout.

![Toggle between the initial price option and the upsell price option](https://b.stripecdn.com/docs-statics-srv/assets/upsell-preview.2a43c1a8acb9f167178b7fda6a2b0796.gif)

Customer preview.

## Retrieve Checkout Session line items

After a customer selects an upsell, the line_items for the Checkout Session update to reflect the upsell price. When fulfilling your order using the checkout.session.completed webhook, make sure to retrieve the line items.

## Trial behavior

If a customer selects an upsell for a Checkout Session with a trial available, the trial length won’t change.

## Coupon behavior

If a coupon is passed into the discounts array of the Checkout Session, that coupon is also applied to the upsell price if a customer selects the upsell. For example, if a monthly subscription upsells to a yearly subscription, and you pass in a 50% off coupon with a duration of four months, the discount applies to all invoices in the four month period starting when the coupon is first applied. If the upsell is selected, the 50% discount applies to the entire yearly subscription because the yearly invoice is created during the coupon’s four month period.

## Remove a subscription upsell

To remove a subscription upsell, click the x below. After you remove a subscription upsell, that upsell won’t be available to any new Checkout Sessions.

![Remove an upsell](https://b.stripecdn.com/docs-statics-srv/assets/remove-upsell.36e5e59619f3c13f0aa94a3bd48bafdb.gif)

Remove an upsell.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Subscription upsells](#subscription-upsells)[Create a subscription upsell](#create-upsell)[Checkout experience](#checkout-experience)[Retrieve Checkout Session line items](#line-items)[Trial behavior](#trial-behavior)[Coupon behavior](#coupon-behavior)[Remove a subscription upsell](#remove-upsell)Products Used[Checkout](/payments/checkout)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`