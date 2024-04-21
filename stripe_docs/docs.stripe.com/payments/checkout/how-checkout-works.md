# How Checkout works

Stripe Checkout is a prebuilt payment form that allows businesses to securely accept payments online. Checkout’s built-in features allow you to reduce your development time. It supports 40+ payment methods, including Link, Stripe’s 1-click payment solution. You can accept payments by embedding Checkout directly into your website or directing customers to a Stripe-hosted payment page.

[Link](/payments/link)

You can also customize Checkout and access additional functionality with the Checkout Session API and the Stripe Dashboard. For a complete list of features, see its built-in and customizable features.

[Checkout Session API](/api/checkout/sessions)

[built-in and customizable features](/payments/checkout/how-checkout-works#features)

Checkout supports payments for both one-time purchases and subscriptions.

[one-time purchases](/payments/online-payments)

[subscriptions](/subscriptions)

## Checkout lifecycle

- When customers are ready to complete their purchase, your application creates a new Checkout Session.

- The Checkout Session provides a URL that redirects customers to a Stripe-hosted payment page.

- Customers enter their payment details on the payment page and complete the transaction.

- After the transaction, a webhook fulfills the order using the checkout.session.completed event.

[webhook](/webhooks)

[fulfills the order](/payments/checkout/fulfill-orders)

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

## Low-code integration

Checkout requires minimal coding and is the best choice for most integrations because of its prebuilt functionalities and customization options. You can integrate Checkout by creating a Checkout Session and collecting customer payment details. Collect payment by embedding a payment form in your website or redirecting customers to a Stripe-hosted payment page.

[embedding a payment form](/payments/accept-a-payment?platform=web&ui=embedded-form)

[Stripe-hosted payment page](/payments/accept-a-payment?platform=web&ui=stripe-hosted)

Compare Checkout to other Stripe payment options to determine the best one for you. Checkout displays a payment form to collect customer payment information, validates cards, handles errors, and so on.

[Compare Checkout](/payments/online-payments#compare-features-and-availability)

## Built-in and customizable features

Stripe Checkout has the following built-in and customizable features:

- PayPal, Google Pay, Apple Pay, and Link

- Responsive mobile design

- SCA-ready

- CAPTCHAs

- PCI compliance

- Card validation

- Error messaging

- Adjustable quantities

[Adjustable quantities](/payments/checkout/adjustable-quantity)

- Automatic tax collection

[Automatic tax collection](/tax/checkout)

- International language support

- Adaptive Pricing

[Adaptive Pricing](/payments/checkout/adaptive-pricing)

- Collect taxes

[Collect taxes](/payments/checkout/taxes)

- Custom branding with colors, buttons, and font

[Custom branding with colors, buttons, and font](/payments/checkout/customization)

- Cross-sells

[Cross-sells](/payments/checkout/cross-sells)

- Global payment methods

[Global payment methods](/payments/dashboard-payment-methods)

- Subscription upsells

[Subscription upsells](/payments/checkout/upsells)

- Custom domains (Stripe-hosted page only)

[Custom domains](/payments/checkout/custom-domains)

- Email receipts

[Email receipts](/receipts)

- Apply discounts

[Apply discounts](/payments/checkout/discounts)

- Custom success page

[Custom success page](/payments/checkout/custom-success-page)

- Recover abandoned carts

[Recover abandoned carts](/payments/checkout/abandoned-carts)

- Autofill payment details with Link

[Autofill payment details with Link](/payments/checkout/customization#link)

- Collect Tax IDs

[Collect Tax IDs](/tax/checkout/tax-ids)

- Collect shipping information

[Collect shipping information](/payments/collect-addresses?payment-ui=checkout)

- Collect phone numbers

[Collect phone numbers](/payments/checkout/phone-numbers)

- Set the subscription billing cycle date

[Set the subscription billing cycle date](/payments/checkout/billing-cycle)

You can set fonts, colors, icons, and field styles for your Stripe-hosted Checkout page using your Stripe Dashboard’s Branding settings. Toggle between Stripe-hosted and embedded to see the branding options for the integration type you chose. For more information, see Customize your integration.

[Branding settings](https://dashboard.stripe.com/settings/branding/checkout)

[Customize your integration](/payments/checkout/customization)

If you use Stripe’s custom domain feature, you can serve Stripe-hosted Checkout pages on a subdomain of your custom domain. Custom domains are a paid feature. For information, see Pricing and fees.

[custom domain feature](/payments/checkout/custom-domains)

[Pricing and fees](https://stripe.com/pricing)

## Checkout Session

The Checkout Session is a programmatic representation of what your customers see on the payment form. After creating a Checkout Session, redirect your customers to the Session’s URL to complete the purchase. When customers complete their purchase, you can fulfill their orders by configuring webhooks on Checkout Session events. This code snippet from the quickstart guide is an example of how to create a Checkout Session in your application.

[fulfill their orders](/payments/checkout/fulfill-orders)

[quickstart guide](/checkout/quickstart)

[https://example.com/success](https://example.com/success)

Allow customers to make one-time payments or subscribe to a product or service by setting the mode parameter in a Checkout Session.

[mode](/api/checkout/sessions/create#create_checkout_session-mode)

[Subscription](/billing/subscriptions/overview)

- Recurring purchases

- Mixed cart: Recurring purchases with one-time purchases

Create a mixed cart in Checkout that lets your customers purchase Subscription items and one-time purchase items at the same time. To create a mixed cart, set the mode parameter to subscription and include the Price IDs, or price_data, for each line_item in the line_items array. Price IDs come from Price objects created using the Stripe Dashboard or API and allow you to store information about your product catalog in Stripe.

[line_items](/api/checkout/sessions/create#create_checkout_session-line_items)

You can also use price_data to reference information from an external database where you’re hosting price and product details without storing product catalog information on Stripe. For more information, see Build a subscriptions integration.

[price_data](/api/checkout/sessions/create#create_checkout_session-line_items-price_data)

[Build a subscriptions integration](/billing/subscriptions/build-subscriptions)

You can view, enable, and disable different payment methods in the Stripe Dashboard at any time. Stripe enables certain payment methods for you by default. We might also enable additional payment methods after notifying you. View our complete list of payment methods.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

[complete list of payment methods](/payments/payment-methods/overview)

You can save payment details for future use by sending an API parameter when you create a Session. Options to save payment details include:

[save payment details for future use](/payments/save-and-reuse)

- Single payment—If your Checkout Session uses payment mode, set the payment_intent_data.setup_future_usage parameter.

[payment_intent_data.setup_future_usage](/payments/payment-intents#future-usage)

- Subscription payment—If your Checkout Session uses subscription mode, Stripe saves the payment method by default.

- Multiple saved payment methods—If a customer has multiple payment methods saved, you can store a default payment method to the Customer object’s default_payment_method field. However, by default, these payment methods don’t appear for return purchases in Checkout. (Learn more).

[default_payment_method](/api/customers/object#customer_object-invoice_settings-default_payment_method)

[(Learn more)](/payments/accept-a-payment?platform=web&ui=checkout#save-payment-method-details)

## Complete a transaction

Fulfill orders when a customer completes their purchase by running webhooks after the checkout.session.completed event sends a notification. Webhooks are HTTP calls that run when an event occurs. For example, if a customer doesn’t make a purchase and their cart expires, you can set a webhook on the checkout.session.expired event and return items to your inventory or you can send them a cart abandonment email.

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

[checkout.session.expired](/api/events/types#event_types-checkout.session.expired)

[abandonment](/payments/checkout/abandoned-carts)

## See also

- Checkout quickstart

[Checkout quickstart](/checkout/quickstart)

- Fulfill your orders

[Fulfill your orders](/payments/checkout/fulfill-orders)

- Collect taxes in Checkout

[Collect taxes in Checkout](/payments/checkout/taxes)

- Manage limited inventory with Checkout

[Manage limited inventory with Checkout](/payments/checkout/managing-limited-inventory)

- Automatically convert to local currencies in Checkout with Adaptive Pricing

[Automatically convert to local currencies in Checkout with Adaptive Pricing](/payments/checkout/adaptive-pricing)
