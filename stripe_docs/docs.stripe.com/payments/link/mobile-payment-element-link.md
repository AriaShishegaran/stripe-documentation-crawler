# Link in the Mobile Payment Element

Let your customer check out faster by using Link in the Mobile Payment Element. You can autofill information for any customer already using Link, regardless of whether they initially saved their information in Link with another business. The default Mobile Payment Element integration includes a Link prompt in the card form.

[Link](/payments/link/what-is-link)

[Mobile Payment Element](/payments/accept-a-payment?platform=ios&mobile-ui=payment-element)

Add Link to your iOS integration

## Enable Link

To offer Link in your mobile app:

- Integrate the Mobile Payment Element using the latest version of the Stripe Mobile SDK.

[Integrate the Mobile Payment Element](/payments/accept-a-payment?platform=ios&mobile-ui=payment-element)

- Enable Link in your Payment Method settings.

[Payment Method settings](https://dashboard.stripe.com/settings/payment_methods)

- Enable Dynamic payment methods by using the latest version of the API or by adding the automatic_payment_methods parameter when creating your PaymentIntent.

[Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods)

[latest version of the API](/upgrades)

[automatic_payment_methods](/api/payment_intents/object#payment_intent_object-automatic_payment_methods)

- (Optional) Pass in your customer’s email address.

[Pass in your customer’s email address](#pass-email)

## Pass in a customer’s email address

Link authenticates a customer using their email address. We recommend prefilling as much information as possible to streamline the checkout process.

To prefill the customer’s name, email address, and phone number, supply defaultBillingDetails with your customer information after initializing PaymentSheet.Configuration.

## Test your integration

You can create test mode accounts for Link using any valid email address. When prompted for a one-time passcode, enter 000000.

## See also

- Stripe Mobile SDKs

[Stripe Mobile SDKs](/libraries#stripe-mobile-sdks)
