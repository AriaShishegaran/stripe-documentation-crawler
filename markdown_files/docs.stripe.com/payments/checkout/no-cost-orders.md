htmlNo-cost orders | Stripe Documentation[Skip to content](#main-content)Let customers complete orders for free[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fno-cost-orders)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fno-cost-orders)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Checkout](/payments/checkout)·[Home](/docs)[Payments](/docs/payments)[Checkout](/docs/payments/checkout)# No-cost orders

Accept orders for no-cost line items, and apply 100% off discounts in payment mode.With Checkout, you can process no-cost orders for one-time payments. Use free line items or discounts for 100% off. If the total amount is 0, Checkout doesn’t collect a payment method from the customer.

NoteTo process no-cost orders using the Checkout API, make sure you’re on API version 2023-08-16 or later.

## Limitations

No-cost orders currently doesn’t support guest customers.

## Create a Checkout Session with no-cost line items

Create a Price with a unit_amount of 0, and pass it into the line items array of the Checkout Session. See Products and prices for more information on creating prices.

You can also use the price_data parameter of the line_items array to pass in a free price.

Stripe-hosted pageEmbedded formCommand Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "line_items[0][price_data][unit_amount]"=0 \
  -d "line_items[0][price_data][product_data][name]"="Free t-shirt" \
  -d "line_items[0][price_data][currency]"=usd \
  -d "line_items[0][quantity]"=1 \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success" \
  --data-urlencode cancel_url="https://example.com/cancel"`## Create a discount to allow customers to complete orders for free

### Coupons

Create a Coupon that makes your Checkout Session free. For example, you can create a 100% off coupon.

Command Line[curl](#)`curl https://api.stripe.com/v1/coupons \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d percent_off=100 \
  -d duration=once`To create a session with an applied discount, pass the coupon ID in the coupon parameter of the discounts array.

Stripe-hosted pageEmbedded formCommand Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "line_items[0][price_data][unit_amount]"=2000 \
  -d "line_items[0][price_data][product_data][name]"=T-shirt \
  -d "line_items[0][price_data][currency]"=usd \
  -d "line_items[0][quantity]"=1 \
  -d "discounts[0][coupon]"={{COUPON_ID}} \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success" \
  --data-urlencode cancel_url="https://example.com/cancel"`You can also create a free Checkout Session by applying a coupon for an amount equal to or exceeding the Checkout Session total.

### Promotion codes

Promotion codes are customer-facing codes created on top of coupons. You can share these codes with customers who can enter them into Checkout to apply a discount. Create a promotion code from a 100% off coupon to allow customers to create orders for free.

Command Line[curl](#)`curl https://api.stripe.com/v1/promotion_codes \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d coupon={{COUPON_ID}} \
  -d code=FREECODE`Enable user-redeemable promotion codes using the allow_promotion_codes parameter in a Checkout Session. This enables a field in Checkout to allow users to enter promotion codes.

Stripe-hosted pageEmbedded formCommand Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "line_items[0][price_data][unit_amount]"=2000 \
  -d "line_items[0][price_data][product_data][name]"=T-shirt \
  -d "line_items[0][price_data][currency]"=usd \
  -d "line_items[0][quantity]"=1 \
  -d mode=payment \
  -d allow_promotion_codes=true \
  --data-urlencode success_url="https://example.com/success" \
  --data-urlencode cancel_url="https://example.com/cancel"`Customers can also check out for free if they apply a promotion code for an amount equal to or exceeding the Checkout Session total.

For more ways to apply discounts, see Add discounts.

## Payment links and pricing tables Optional

Payment links and pricing tables support no-cost orders by default when your account is created after August 17, 2023. For accounts created before August 17, 2023, you can enable no-cost orders for your Payment links and pricing tables by visiting your Checkout settings in the Dashboard.

CautionWhen you enable this feature, it has a 3-day grace period in which you can turn it off. After 3 days, you can’t disable it. Before you enable it for your live payment links and pricing tables, test it with your fulfillment flow in test mode.

To use no-cost orders with a payment link in test mode, specify a prefilled_email URL parameter with an email whose local part includes the suffix +no_cost_orders. For example, `j.appleseed+no_cost_orders@example.com’. The resulting checkout session lets you apply a discount that reduces the order total to zero.

To use no-cost orders with a pricing table in test mode, set the pricing table’s customer-email property to an email whose local part includes the suffix +no_cost_orders. For example, `j.appleseed+no_cost_orders@example.com’. The resulting checkout session lets you apply a discount that reduces the order total to zero.

## Handling completed orders

After the Checkout Session completes, you can make a request for the finalized line items and their quantities. If your customer removes a line item, it also removes it from the line items response. See the Fulfillment guide to learn how to create an event handler to handle completed Checkout Sessions.

Common mistakeTo fulfill no-cost orders, make sure to handle the checkout.session.completed event rather than PaymentIntent events. Completed Checkout Sessions that are free won’t have an associated PaymentIntent.

You can see your completed no-cost orders in the Dashboard. The no-cost orders tab only appears if you have at least one completed no-cost order.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Limitations](#limitations)[Create a Checkout Session with no-cost line items](#no-cost-line-items)[Create a discount to allow customers to complete orders for free](#full-cost-discounts)[Payment links and pricing tables](#payment-links-and-pricing-tables)[Handling completed orders](#handling-orders)Products Used[Checkout](/payments/checkout)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`