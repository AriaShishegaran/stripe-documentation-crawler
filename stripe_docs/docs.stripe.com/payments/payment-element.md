# Stripe Payment Element

We’re developing a Payment Element integration that manages tax, discounts, shipping, and currency conversion. Read the Build a checkout page guide to learn more.

[Build a checkout page](/checkout/custom-checkout)

The Payment Element is a UI component for the web that accepts 40+ payment methods, validates input, and handles errors. Use it alone or with other elements in your web app’s frontend.

To try the Payment Element for yourself, start with one of these examples:

[QuickstartCode and instructions for accepting a payment using the Payment Element.](/payments/quickstart)

Code and instructions for accepting a payment using the Payment Element.

[Clone a sample app on GitHubHTML · React · Vue](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)

[API reference](/docs/js/element/payment_element)

## Create a Payment Element

This code creates a Payment Element and mounts it to the DOM:

[creates](/js/elements_object/create_payment_element)

[mounts](/js/element/mount)

[View full sample](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)

Accepting payments with the Payment Element requires additional backend code. See the quickstart or sample app to learn how this works.

[quickstart](/payments/quickstart)

[sample app](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)

## Combine elements

The Payment Element interoperates with other elements. For instance, this form uses one additional element to autofill checkout details, and another to collect the shipping address.

[autofill checkout details](/payments/link)

[collect the shipping address](/elements/address-element)

For the complete code for this Link example, see Add Link to an Elements integration.

[Add Link to an Elements integration](/payments/link/add-link-elements-integration)

## Payment methods

Stripe enables certain payment methods for you by default. We might also enable additional payment methods after notifying you. Use the Dashboard to enable or disable payment methods at any time. With the Payment Element, you can use Dynamic payment methods to:

[Dashboard](https://dashboard.stripe.com/settings/payment_methods)

[Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods)

- Manage payment methods in the Dashboard without coding

[Dashboard](https://dashboard.stripe.com/settings/payment_methods)

- Dynamically display the most relevant payment options based on factors such as location, currency, and transaction amount

For instance, if a customer in Germany is paying in EUR, they see all the active payment methods that accept EUR, starting with ones that are widely used in Germany.

Show payment methods in order of relevance to your customer

To further customize how payment methods render, such as by filtering card brands that you don’t want to support, see Customize payment methods. To add payment methods integrated outside of Stripe, see External payment methods.

[Customize payment methods](/payments/customize-payment-methods)

[External payment methods](/payments/external-payment-methods)

If your integration requires you to list payment methods manually, see Manually list payment methods.

[Manually list payment methods](/payments/payment-methods/integration-options#listing-payment-methods-manually)

## Layout

You can customize the Payment Element’s layout to fit your checkout flow. The following image is the same Payment Element rendered using different layout configurations.

Payment Element with different layouts.

The tabs layout displays payment methods horizontally using tabs. To use this layout, set the value for layout.type to tabs. You can also specify other properties, such as layout.defaultCollapsed.

[layout.type](/js/elements_object/create_payment_element#payment_element_create-options-layout-type)

[layout.defaultCollapsed](/js/elements_object/create_payment_element#payment_element_create-options-layout-defaultCollapsed)

[View full sample](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)

## Appearance

Use the Appearance API to control the style of all elements. Choose a theme or update specific details.

For instance, choose the “flat” theme and override the primary text color.

[View full sample](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)

See the Appearance API documentation for a full list of themes and variables.

[Appearance API](/elements/appearance-api)

## Options

Stripe elements support more options than these. For instance, display your business name using the business option.

[business](/js/elements_object/create_payment_element#payment_element_create-options-business)

[View full sample](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)

The Payment Element supports the following options. See each options’s reference entry for more information.

[layout](/js/elements_object/create_payment_element#payment_element_create-options-layout)

[defaultValues](/js/elements_object/create_payment_element#payment_element_create-options-defaultValues)

[business](/js/elements_object/create_payment_element#payment_element_create-options-business)

[paymentMethodOrder](/js/elements_object/create_payment_element#payment_element_create-options-business)

[fields](/js/elements_object/create_payment_element#payment_element_create-options-business)

[readOnly](/js/elements_object/create_payment_element#payment_element_create-options-readOnly)

[terms](/js/elements_object/create_payment_element#payment_element_create-options-terms)

[wallets](/js/elements_object/create_payment_element)
