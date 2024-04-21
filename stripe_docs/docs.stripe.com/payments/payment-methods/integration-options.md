# Payment method integration options

The payment methods you can offer depend on the currency, country, and Stripe products you integrate with. Use this guide to make sure your chosen payment methods work for your business and to determine how you want to add payment methods.

[payment methods](#payment-method-availability)

## Choose your integration

To decide which integration works best for you, consider:

- The Stripe products and checkout options you want to use or are currently using.

- The payment methods you want to enable.

We offer several ways to get started with your integration using the Stripe Dashboard that don’t require any code:

- Payment Links: Redirect your customers to a Stripe-hosted payment page. This page dynamically displays the payment methods most relevant to the currency and customer’s location based on the payment methods you enabled in the Dashboard.

Payment Links: Redirect your customers to a Stripe-hosted payment page. This page dynamically displays the payment methods most relevant to the currency and customer’s location based on the payment methods you enabled in the Dashboard.

[Payment Links](/payment-links)

[Dashboard](https://dashboard.stripe.com/settings/payment_methods)

- Invoicing: Allows you to automatically charge your customer’s payment method on file, or email them the invoice with or without a link to a payment page. You can also create basic subscriptions from the Dashboard. To configure payment methods for invoices and subscriptions, see the Invoice template.

Invoicing: Allows you to automatically charge your customer’s payment method on file, or email them the invoice with or without a link to a payment page. You can also create basic subscriptions from the Dashboard. To configure payment methods for invoices and subscriptions, see the Invoice template.

[Invoicing](/invoicing/quickstart-guide)

[create basic subscriptions](https://dashboard.stripe.com/subscriptions/create)

[Invoice template](https://dashboard.stripe.com/settings/billing/invoice)

If you’re looking for more control over your payments integration, Stripe offers several unique low-code offerings:

- Checkout: Lets you add an embeddable payment form to your site or redirect users to a Stripe-hosted checkout page. You can configure Checkout programmatically through the API or configure it in the Dashboard. Stripe selects enabled payment methods from your Dashboard by default. If you’re using the API, you can manually list payment methods using payment method types.

Checkout: Lets you add an embeddable payment form to your site or redirect users to a Stripe-hosted checkout page. You can configure Checkout programmatically through the API or configure it in the Dashboard. Stripe selects enabled payment methods from your Dashboard by default. If you’re using the API, you can manually list payment methods using payment method types.

[Checkout](/payments/checkout)

[payment method types](/api/checkout/sessions/create#create_checkout_session-payment_method_types)

- Payment Element: A UI component that you embed into your website or app. When customers are ready to complete a purchase, you create a PaymentIntent or a SetupIntent and configure how you want to display payment methods. For the Payment Element, you can manage payment methods from the Dashboard. Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow.

Payment Element: A UI component that you embed into your website or app. When customers are ready to complete a purchase, you create a PaymentIntent or a SetupIntent and configure how you want to display payment methods. For the Payment Element, you can manage payment methods from the Dashboard. Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow.

[Payment Element](/payments/payment-element)

[PaymentIntent](/payments/payment-intents)

[SetupIntent](/api/setup_intents)

[Dashboard](https://dashboard.stripe.com/settings/payment_methods)

With Checkout and the Payment Element, you can also use subscriptions or recurring charges. To manage customer subscriptions and payment methods for invoices and subscriptions, see Customer management. You can also list payment methods manually with payment method types.

[subscriptions or recurring charges](/billing/subscriptions/build-subscriptions?ui=stripe-hosted)

[Customer management](/customer-management)

[payment method types](/api/payment_intents/create#create_payment_intent-payment_method_types)

## Payment method support

Link is a payment method network. With Link, users save their payment details once and can then pay any merchant on the Link network with one click.

[Link](/payments/link)

Payment methods only support certain currencies, countries, and products. Make sure your chosen payment methods work for your scenario. Depending on your payments flows, some additional API options might restrict the payment methods you can offer.

[additional API options](#additional-api-supportability)

If you’re seeing that a specific payment method isn’t appearing for a customer, use the Payment Methods review page in the Dashboard. This tool lets you troubleshoot the issue using an existing PaymentIntent ID or custom field.

[Payment Methods review](https://dashboard.stripe.com/settings/payment_methods/review)

All payment methods have specific requirements for their use and may contain additional restrictions that you must comply with, such as marketing guidelines, additional prohibited and restricted businesses, and information about handling disputes and refunds. These usage requirements and restrictions are described in the documentation for that payment method or in the applicable payment terms.

[documentation](/payments/payment-methods/overview)

[payment terms](https://stripe.com/payment-terms/legal)

Refer to the following table to see where each payment method is supported and what presentment currencies it accepts. This table contains all of the supported currencies and countries for a given payment method. In some cases, not all of the countries listed can accept payments in all of the listed presentment currencies. For more details on exactly what currencies are accepted, see the individual payment method’s page.

[payment method](/api/payment_methods/object#payment_method_object-type)

Refer to the following tables to determine which payment methods are supported by each Stripe product:

There are three Checkout modes: payment, subscription, and setup. Unless specified otherwise, the payment method is available in all modes or any that remain.

The following tables detail additional payment method API support:

## Add payment methods

Your customers see the available payment methods during the checkout process. You can either manage payment methods from the Dashboard or list payment methods manually in code. See the Accept a payment guide for detailed steps.

[Dashboard](https://dashboard.stripe.com/settings/payment_methods)

[Accept a payment](/payments/accept-a-payment)

Stripe dynamically displays the most relevant payment methods to your customers based on the payment method preferences you set in the Dashboard and eligibility factors such as transaction amount, currency, and payment flow. To enable and manage your payment method preferences, go to the Dashboard. Stripe enables certain payment methods for you by default and might enable additional payment methods after notifying you.

[Dashboard](https://dashboard.stripe.com/settings/payment_methods)

Unless you have to list payment methods manually, we recommend using dynamic payment methods. Dynamic payment methods automatically determines whether to display payment methods according to set rules.

See Dynamic payment methods to learn more.

[Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods)

Listing payment methods manually requires some coding. Every payment method you want your PaymentIntent to accept must be added to payment_method_types. Unless your integration requires that you list payment methods manually, we recommend that you manage payment methods from the Dashboard. Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow.

[Dashboard](https://dashboard.stripe.com/settings/payment_methods)

If multiple payment methods are passed, Checkout dynamically reorders them to prioritize the most relevant payment methods based on the customer’s location and other characteristics. The payments acceptance page prioritizes showing payment methods known to increase conversion for your customer’s location while lower priority payment methods are hidden in an overflow menu.
