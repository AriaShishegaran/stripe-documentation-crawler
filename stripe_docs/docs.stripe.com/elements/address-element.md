# Address Element

## Overview

The Address Element is an embeddable UI component for accepting complete addresses. Use it to collect shipping addresses, or when you need a complete billing address, such as for tax purposes.

Features include:

- Global support: Support 236 regional address formats, including right-to-left address formats

- Autocomplete: Decrease checkout time, reduce validation errors, and increase checkout conversion with built-in address autocomplete

- Prefill saved addresses: Prefill addresses at page load when you already have an address saved for your customer

- Customized appearance: Customize the Address Element to match your page design with the Appearance API

[Appearance API](/elements/appearance-api)

- Seamless Elements integration: Reuse an existing Elements instance to save time, and pass data automatically with the Payment Element and Link

- Support for any device: Available for web, iOS, Android, and React Native mobile SDKs



## Start with examples

To see the Address Element in action, start with one of these examples:

[Collect customer addressesCode and instructions for saving an address using the Address Element.](/elements/address-element/collect-addresses?platform=react-native)

Code and instructions for saving an address using the Address Element.

[Clone a sample app on GitHubHTML · React](https://github.com/stripe-samples/link)

## Create an Address Element

When you create an Address Element, specify whether to use it in shipping or billing mode.

In shipping mode, the element does two things:

- Collect a shipping address.

- Offer the customer the option to use it as a billing address too.

[View full sample](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)

## Use an address

The Address Element automatically works with the Payment or Express Checkout Element. When a customer provides an address and a payment method, Stripe combines them into a single PaymentIntent with the address in the correct field.

[Payment](/payments/payment-element)

[PaymentIntent](/payments/payment-intents)

The element’s default behavior depends on its mode.

In shipping mode, the address is stored in these fields:

- It appears in the shipping field.

[shipping](/api/payment_intents/confirm#confirm_payment_intent-shipping)

- If the customer indicates it is also the billing address, it also appears in the billing_details field.

[billing_details](/api/payment_intents/confirm#confirm_payment_intent-payment_method_data-billing_details)

To enable combining information, create all elements from the same Elements object, as in this example:

[View full sample](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)

Normally, the Address Element’s default behavior is enough. But in a complex payment flow, you might need to write custom responses to the customer’s input. For information, see Listen for address input.

[Listen for address input](/elements/address-element/collect-addresses)

## Autocomplete

The Address Element can autocomplete addresses for 25 countries. If your customer selects a supported country for their address, then they see the autocomplete options. These are the supported countries for autocomplete:

If you use the Address Element and the Payment Element together, Stripe enables autocomplete with no configuration required.

If you use the Address Element alone, you must use your own Google Maps API Places Library key, which is managed separately from your Stripe account. Pass the key in the autocomplete.apiKey option.

[Google Maps API Places Library key](https://developers.google.com/maps/documentation/javascript/places)

[autocomplete.apiKey](/js/elements_object/create_address_element#address_element_create-options-autocomplete-apiKey)

## Autofill with Link

Link saves and autofills payment and shipping information. When a returning Link customer authenticates, Stripe autofills their shipping information in the Address element.

[Link](/payments/link)

Create a payment form using multiple Elements

To enable autofill, create all elements from the same Elements object, as in this example:

[View full sample](https://github.com/stripe-samples/link/blob/main/client/html/index.js)

## Appearance

You can use the Appearance API to control the style of all elements. Choose a theme or update specific details.

For instance, choose the “flat” theme and override the primary text color.

[View full sample](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)

See the Appearance API documentation for a full list of themes and variables.

[Appearance API](/elements/appearance-api)
