# Payment Element integration best practices

Use the checklist on this page to make sure you build your Payment Element integration for optimal performance. The following features enable you to access additional integration options. For example, if you use Dynamic payment methods, you can use payment method rules to present payment methods with custom criteria.

[Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods)

[payment method rules](/payments/payment-method-rules)

## Integration checklist

- Choose a layoutChoose the Payment Element’s layout to match the style of your site, then run an A/B test to confirm the best choice. If you have over 4 payment methods, we recommend the accordion layout.

Choose the Payment Element’s layout to match the style of your site, then run an A/B test to confirm the best choice. If you have over 4 payment methods, we recommend the accordion layout.

[layout](/payments/payment-element#layout)

- Add stylingStyle the Payment Element to match the visual design of your website using the Appearance API. You can apply this style to any element you add to your integration.

Style the Payment Element to match the visual design of your website using the Appearance API. You can apply this style to any element you add to your integration.

[Style the Payment Element](/payments/payment-element#appearance)

- Choose how to collect a paymentConsider if you want to collect a payment before you create the PaymentIntent API call. To accept a payment, you must create a PaymentIntent that contains an amount and currency, and confirm that payment to trigger Stripe to make a charge. However, you can alternate the order that you collect the payment and create the PaymentIntent. We recommend that you collect the payment first.

Consider if you want to collect a payment before you create the PaymentIntent API call. To accept a payment, you must create a PaymentIntent that contains an amount and currency, and confirm that payment to trigger Stripe to make a charge. However, you can alternate the order that you collect the payment and create the PaymentIntent. We recommend that you collect the payment first.

[collect a payment](/payments/accept-a-payment-deferred?type=payment)

[accept a payment](/payments/accept-a-payment?platform=web&ui=elements)

[collect the payment first](/payments/accept-a-payment-deferred?type=payment)

- Send metadataSend metadata in your PaymentIntent to allow metadata to show up in your reports. This indexes your metadata to make sure that it’s searchable in the Stripe Dashboard. You can use this metadata to find and reference transactions.

Send metadata in your PaymentIntent to allow metadata to show up in your reports. This indexes your metadata to make sure that it’s searchable in the Stripe Dashboard. You can use this metadata to find and reference transactions.

[metadata](/api/payment_intents/create#create_payment_intent-metadata)

- Make sure to use the latest APICheck to make sure your PaymentIntent uses the latest API version.

Check to make sure your PaymentIntent uses the latest API version.

[latest API version](/upgrades#api-versions)

- Select the payment methods you want to displayUse Dynamic payment methods, part of the default Stripe integration, to present eligible payment methods to your customers. Stripe handles the logic for dynamically displaying the most relevant eligible payment methods to each customer to maximize conversion based on factors such as the amount, currency, location, and so on. Dynamic payment methods allow you to:Choose the payment methods that your customers can use from the Dashboard.Use additional features, such as payment method rules, which allows you to present payment methods using custom criteria.

Use Dynamic payment methods, part of the default Stripe integration, to present eligible payment methods to your customers. Stripe handles the logic for dynamically displaying the most relevant eligible payment methods to each customer to maximize conversion based on factors such as the amount, currency, location, and so on. Dynamic payment methods allow you to:

[Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods)

- Choose the payment methods that your customers can use from the Dashboard.

[payment methods](https://stripe.com/guides/payment-methods-guide)

[Dashboard](https://dashboard.stripe.com/settings/payment_methods)

- Use additional features, such as payment method rules, which allows you to present payment methods using custom criteria.

[payment method rules](/payments/payment-method-rules)

- Test payment methodsWhen your integration is complete, test and View how payment methods appear to customers. From the Review displayed payment methods form, enter a PaymentIntent ID to learn which payment methods were and weren’t available for that specific transaction. You can also simulate which payment methods display in a given scenario by changing factors such as the amount, currency, capture method, and future usage.

When your integration is complete, test and View how payment methods appear to customers. From the Review displayed payment methods form, enter a PaymentIntent ID to learn which payment methods were and weren’t available for that specific transaction. You can also simulate which payment methods display in a given scenario by changing factors such as the amount, currency, capture method, and future usage.

[View how payment methods appear to customers](https://dashboard.stripe.com/settings/payment_methods/review)

[PaymentIntent ID](/api/payment_intents/object#payment_intent_object-id)

## Additional features checklist

- Enable LinkAfter you integrate your UI and dynamic payment methods, enable Link in the Payment Method settings page. Link securely saves and fills in customer payment and shipping details. It supports various payment methods, including credit cards, debit cards, and US bank accounts. For logged-in customers that already use Link, this feature prefills their information, regardless of whether they initially saved it on the checkout page of another business.

After you integrate your UI and dynamic payment methods, enable Link in the Payment Method settings page. Link securely saves and fills in customer payment and shipping details. It supports various payment methods, including credit cards, debit cards, and US bank accounts. For logged-in customers that already use Link, this feature prefills their information, regardless of whether they initially saved it on the checkout page of another business.

[Link](/payments/link/payment-element-link)

[Payment Method settings page](https://dashboard.stripe.com/settings/payment_methods)

- Add the Link Authentication ElementTo collect and prefill shipping addresses and sell physical goods, we recommend using the Link Authentication Element to create a single email input field for both email collection and Link authentication.

To collect and prefill shipping addresses and sell physical goods, we recommend using the Link Authentication Element to create a single email input field for both email collection and Link authentication.

[Link Authentication Element](/payments/elements/link-authentication-element)

- Add the Address ElementThe Address Element streamlines collection of shipping and billing information during checkout. It integrates with other elements and prefills addresses with Link. It supports auto-suggestions for new address entry using free Google Autocomplete support.In shipping mode, customers have the option to use their shipping address as their billing address.In billing mode, Stripe hides billing fields within the Payment Element to make sure that customers only need to enter their details once.

The Address Element streamlines collection of shipping and billing information during checkout. It integrates with other elements and prefills addresses with Link. It supports auto-suggestions for new address entry using free Google Autocomplete support.

- In shipping mode, customers have the option to use their shipping address as their billing address.

- In billing mode, Stripe hides billing fields within the Payment Element to make sure that customers only need to enter their details once.

- Add the Payment Method Messaging ElementIf you choose to offer BNPLs, we recommend that you promote them ahead of checkout to help drive awareness, increase order value, and positively impact conversion using the Payment Method Messaging Element.You can display this unified embeddable component on product detail, cart, and payment pages.This element includes support for Affirm, Afterpay, and Klarna.

If you choose to offer BNPLs, we recommend that you promote them ahead of checkout to help drive awareness, increase order value, and positively impact conversion using the Payment Method Messaging Element.

[Payment Method Messaging Element](/payments/payment-method-messaging)

- You can display this unified embeddable component on product detail, cart, and payment pages.

- This element includes support for Affirm, Afterpay, and Klarna.

[Affirm](/payments/affirm)

[Afterpay](/payments/afterpay-clearpay)

[Klarna](/payments/klarna)

- Add the Express Checkout ElementUse the Express Checkout Element to show customers multiple one-click payment buttons in a single UI component, including Apple Pay, Google Pay, PayPal, and Link.

Use the Express Checkout Element to show customers multiple one-click payment buttons in a single UI component, including Apple Pay, Google Pay, PayPal, and Link.

[Express Checkout Element](/elements/express-checkout-element)

[Apple Pay](/apple-pay)

[Google Pay](/google-pay)

[PayPal](/payments/paypal)

[Link](/payments/link/express-checkout-element-link)

## Next steps

Accept a payment

[Accept a payment](/payments/accept-a-payment?platform=web&ui=elements)
