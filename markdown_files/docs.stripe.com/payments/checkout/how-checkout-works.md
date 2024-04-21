htmlHow Checkout works | Stripe Documentation[Skip to content](#main-content)How Checkout works[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fhow-checkout-works)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fhow-checkout-works)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Checkout](/payments/checkout)·[Home](/docs)[Payments](/docs/payments)[Checkout](/docs/payments/checkout)# How Checkout works

Learn how to use Checkout to collect payments on your website.Stripe Checkout is a prebuilt payment form that allows businesses to securely accept payments online. Checkout’s built-in features allow you to reduce your development time. It supports 40+ payment methods, including Link, Stripe’s 1-click payment solution. You can accept payments by embedding Checkout directly into your website or directing customers to a Stripe-hosted payment page.

You can also customize Checkout and access additional functionality with the Checkout Session API and the Stripe Dashboard. For a complete list of features, see its built-in and customizable features.

Checkout supports payments for both one-time purchases and subscriptions.

## Checkout lifecycle

Stripe-hosted pageEmbedded form1. When customers are ready to complete their purchase, your application creates a new Checkout Session.
2. The Checkout Session provides a URL that redirects customers to a Stripe-hosted payment page.
3. Customers enter their payment details on the payment page and complete the transaction.
4. After the transaction, a[webhook](/webhooks)[fulfills the order](/payments/checkout/fulfill-orders)using the[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)event.

## Low-code integration

Checkout requires minimal coding and is the best choice for most integrations because of its prebuilt functionalities and customization options. You can integrate Checkout by creating a Checkout Session and collecting customer payment details. Collect payment by embedding a payment form in your website or redirecting customers to a Stripe-hosted payment page.

Compare Checkout to other Stripe payment options to determine the best one for you. Checkout displays a payment form to collect customer payment information, validates cards, handles errors, and so on.

## Built-in and customizable features

Stripe Checkout has the following built-in and customizable features:

### Built-in features

- PayPal, Google Pay, Apple Pay, and Link
- Responsive mobile design
- SCA-ready
- CAPTCHAs
- PCI compliance
- Card validation
- Error messaging
- [Adjustable quantities](/payments/checkout/adjustable-quantity)
- [Automatic tax collection](/tax/checkout)
- International language support
- [Adaptive Pricing](/payments/checkout/adaptive-pricing)

### Customizable features

- [Collect taxes](/payments/checkout/taxes)
- [Custom branding with colors, buttons, and font](/payments/checkout/customization)
- [Cross-sells](/payments/checkout/cross-sells)
- [Global payment methods](/payments/dashboard-payment-methods)
- [Subscription upsells](/payments/checkout/upsells)
- [Custom domains](/payments/checkout/custom-domains)(Stripe-hosted page only)
- [Email receipts](/receipts)
- [Apply discounts](/payments/checkout/discounts)
- [Custom success page](/payments/checkout/custom-success-page)
- [Recover abandoned carts](/payments/checkout/abandoned-carts)
- [Autofill payment details with Link](/payments/checkout/customization#link)
- [Collect Tax IDs](/tax/checkout/tax-ids)
- [Collect shipping information](/payments/collect-addresses?payment-ui=checkout)
- [Collect phone numbers](/payments/checkout/phone-numbers)
- [Set the subscription billing cycle date](/payments/checkout/billing-cycle)

### Custom branding

You can set fonts, colors, icons, and field styles for your Stripe-hosted Checkout page using your Stripe Dashboard’s Branding settings. Toggle between Stripe-hosted and embedded to see the branding options for the integration type you chose. For more information, see Customize your integration.

### Custom domains

If you use Stripe’s custom domain feature, you can serve Stripe-hosted Checkout pages on a subdomain of your custom domain. Custom domains are a paid feature. For information, see Pricing and fees.

## Checkout Session

Stripe-hosted pageEmbedded formThe Checkout Session is a programmatic representation of what your customers see on the payment form. After creating a Checkout Session, redirect your customers to the Session’s URL to complete the purchase. When customers complete their purchase, you can fulfill their orders by configuring webhooks on Checkout Session events. This code snippet from the quickstart guide is an example of how to create a Checkout Session in your application.

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "line_items[0][price]"={{PRICE_ID}} \
  -d "line_items[0][quantity]"=1 \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success"`### One-time and recurring payments

Allow customers to make one-time payments or subscribe to a product or service by setting the mode parameter in a Checkout Session.

ModePurchase typePaymentOne-time purchases[Subscription](/billing/subscriptions/overview)- Recurring purchases
- Mixed cart: Recurring purchases with one-time purchases

### Mixed cart

Create a mixed cart in Checkout that lets your customers purchase Subscription items and one-time purchase items at the same time. To create a mixed cart, set the mode parameter to subscription and include the Price IDs, or price_data, for each line_item in the line_items array. Price IDs come from Price objects created using the Stripe Dashboard or API and allow you to store information about your product catalog in Stripe.

You can also use price_data to reference information from an external database where you’re hosting price and product details without storing product catalog information on Stripe. For more information, see Build a subscriptions integration.

Stripe-hosted pageEmbedded formCommand Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "line_items[0][price]"={{RECURRING_PRICE_ID}} \
  -d "line_items[0][quantity]"=1 \
  -d "line_items[1][price]"={{ONE_TIME_PRICE_ID}} \
  -d "line_items[1][quantity]"=1 \
  -d mode=subscription \
  --data-urlencode success_url="https://example.com/success" \
  --data-urlencode cancel_url="https://example.com/cancel"`### Payment methods

You can view, enable, and disable different payment methods in the Stripe Dashboard at any time. Stripe enables certain payment methods for you by default. We might also enable additional payment methods after notifying you. View our complete list of payment methods.

### Save payment details and default payment methods

You can save payment details for future use by sending an API parameter when you create a Session. Options to save payment details include:

- Single payment—If your Checkout Session uses`payment`mode, set the[payment_intent_data.setup_future_usage](/payments/payment-intents#future-usage)parameter.
- Subscription payment—If your Checkout Session uses`subscription`mode, Stripe saves the payment method by default.
- Multiple saved payment methods—If a customer has multiple payment methods saved, you can store a default payment method to the Customer object’s[default_payment_method](/api/customers/object#customer_object-invoice_settings-default_payment_method)field. However, by default, these payment methods don’t appear for return purchases in Checkout.[(Learn more)](/payments/accept-a-payment?platform=web&ui=checkout#save-payment-method-details).

## Complete a transaction

Fulfill orders when a customer completes their purchase by running webhooks after the checkout.session.completed event sends a notification. Webhooks are HTTP calls that run when an event occurs. For example, if a customer doesn’t make a purchase and their cart expires, you can set a webhook on the checkout.session.expired event and return items to your inventory or you can send them a cart abandonment email.

## See also

- [Checkout quickstart](/checkout/quickstart)
- [Fulfill your orders](/payments/checkout/fulfill-orders)
- [Collect taxes in Checkout](/payments/checkout/taxes)
- [Manage limited inventory with Checkout](/payments/checkout/managing-limited-inventory)
- [Automatically convert to local currencies in Checkout with Adaptive Pricing](/payments/checkout/adaptive-pricing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Checkout lifecycle](#lifecycle)[Low-code integration](#low-code)[Built-in and customizable features](#features)[Checkout Session](#session)[Complete a transaction](#complete)[See also](#see-also)Related Guides[No-code options to accept payments on Stripe](/docs/no-code)[Prebuilt checkout page](/docs/checkout/quickstart)[Learn about payment methods](/docs/payments/payment-methods/overview)Products Used[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`