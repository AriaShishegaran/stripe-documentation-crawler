htmlPayment method integration options | Stripe Documentation[Skip to content](#main-content)Payment method integration options[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-methods%2Fintegration-options)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-methods%2Fintegration-options)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)# Payment method integration options

Learn about the different ways to integrate payment methods.The payment methods you can offer depend on the currency, country, and Stripe products you integrate with. Use this guide to make sure your chosen payment methods work for your business and to determine how you want to add payment methods.

## Choose your integration

To decide which integration works best for you, consider:

- The Stripe products and checkout options you want to use or are currently using.
- The payment methods you want to enable.

### No-code integrations

We offer several ways to get started with your integration using the Stripe Dashboard that don’t require any code:

- Payment Links: Redirect your customers to a Stripe-hosted payment page. This page dynamically displays the payment methods most relevant to the currency and customer’s location based on the payment methods you enabled in the Dashboard.


- Invoicing: Allows you to automatically charge your customer’s payment method on file, or email them the invoice with or without a link to a payment page. You can also create basic subscriptions from the Dashboard. To configure payment methods for invoices and subscriptions, see the Invoice template.



### Low-code integrations

If you’re looking for more control over your payments integration, Stripe offers several unique low-code offerings:

- Checkout: Lets you add an embeddable payment form to your site or redirect users to a Stripe-hosted checkout page. You can configure Checkout programmatically through the API or configure it in the Dashboard. Stripe selects enabled payment methods from your Dashboard by default. If you’re using the API, you can manually list payment methods using payment method types.


- Payment Element: A UI component that you embed into your website or app. When customers are ready to complete a purchase, you create a PaymentIntent or a SetupIntent and configure how you want to display payment methods. For the Payment Element, you can manage payment methods from the Dashboard. Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow.



With Checkout and the Payment Element, you can also use subscriptions or recurring charges. To manage customer subscriptions and payment methods for invoices and subscriptions, see Customer management. You can also list payment methods manually with payment method types.

## Payment method support

### Link and your integration

Link is a payment method network. With Link, users save their payment details once and can then pay any merchant on the Link network with one click.

Payment methods only support certain currencies, countries, and products. Make sure your chosen payment methods work for your scenario. Depending on your payments flows, some additional API options might restrict the payment methods you can offer.

If you’re seeing that a specific payment method isn’t appearing for a customer, use the Payment Methods review page in the Dashboard. This tool lets you troubleshoot the issue using an existing PaymentIntent ID or custom field.

All payment methods have specific requirements for their use and may contain additional restrictions that you must comply with, such as marketing guidelines, additional prohibited and restricted businesses, and information about handling disputes and refunds. These usage requirements and restrictions are described in the documentation for that payment method or in the applicable payment terms.

### Country and currency support

Refer to the following table to see where each payment method is supported and what presentment currencies it accepts. This table contains all of the supported currencies and countries for a given payment method. In some cases, not all of the countries listed can accept payments in all of the listed presentment currencies. For more details on exactly what currencies are accepted, see the individual payment method’s page.

### Payment method availability

### Product support

Refer to the following tables to determine which payment methods are supported by each Stripe product:

Checkout modesThere are three Checkout modes: payment, subscription, and setup. Unless specified otherwise, the payment method is available in all modes or any that remain.

### Bank debits

### Bank redirects

### Bank transfers

### Buy now, pay later

### Cards

### Link

### Real-time payments

### Vouchers

### Wallets

### Additional API support

The following tables detail additional payment method API support:

### Bank debits

### Bank redirects

### Bank transfers

### Buy now, pay later

### Cards

### Link

### Real-time payments

### Vouchers

### Wallets

## Add payment methods

Your customers see the available payment methods during the checkout process. You can either manage payment methods from the Dashboard or list payment methods manually in code. See the Accept a payment guide for detailed steps.

### Use dynamic payment methods

Stripe dynamically displays the most relevant payment methods to your customers based on the payment method preferences you set in the Dashboard and eligibility factors such as transaction amount, currency, and payment flow. To enable and manage your payment method preferences, go to the Dashboard. Stripe enables certain payment methods for you by default and might enable additional payment methods after notifying you.

Unless you have to list payment methods manually, we recommend using dynamic payment methods. Dynamic payment methods automatically determines whether to display payment methods according to set rules.

See Dynamic payment methods to learn more.

### Manually list payment methods

Listing payment methods manually requires some coding. Every payment method you want your PaymentIntent to accept must be added to payment_method_types. Unless your integration requires that you list payment methods manually, we recommend that you manage payment methods from the Dashboard. Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow.

CheckoutPayment Element`curl https://api.stripe.com/v1/checkout/sessions \
  -u sk_test_4eC39HqLyjWDarjtT1zdp7dc: \
  -d success_url="https://example.com/success" \
  -d cancel_url="https://example.com/cancel" \
  -d "line_items[0][price]"=price_H5ggYwtDq4fbrJ \
  -d "line_items[0][quantity]"=2 \
  -d “payment_method_types[]”=bancontact\
  -d “payment_method_types[]”=card\
  -d “payment_method_types[]”=eps\
  -d “payment_method_types[]”=giropay\
  -d “payment_method_types[]”=ideal\
  -d “payment_method_types[]”=p24\
  -d “payment_method_types[]”=sepa_debit\
  ...
  -d mode=payment`If multiple payment methods are passed, Checkout dynamically reorders them to prioritize the most relevant payment methods based on the customer’s location and other characteristics. The payments acceptance page prioritizes showing payment methods known to increase conversion for your customer’s location while lower priority payment methods are hidden in an overflow menu.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Choose your integration](#choose-integration)[Payment method support](#payment-method-product-support)[Add payment methods](#choose-how-to-add-payment-methods)Related Guides[Quickstart](/docs/payments/quickstart)[Accept a payment](/docs/payments/accept-a-payment)Products Used[Payments](/payments)[Checkout](/payments/checkout)[Elements](/payments/elements)[Payment Links](/payments/payment-links)[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`