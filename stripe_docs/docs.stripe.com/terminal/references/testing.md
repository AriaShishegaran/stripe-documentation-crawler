# Test Stripe Terminal

Much of the process for testing Stripe Terminal is similar to that for testing online Stripe payments. Also, you can’t use Stripe Terminal with mobile wallets (for example, Apple Pay or Google Pay) in testmode. For more information, see the general Stripe testing guide.

[general Stripe testing guide](/testing)

The best way to achieve a successful Terminal deployment is to test every part of your integration. We provide testing tools for each stage:

- Before ordering a reader, test your integration with the reader simulator.

- Test your complete hardware integration with a physical test card.

## Simulated reader

- discoverReaders (JavaScript)

[discoverReaders (JavaScript)](/terminal/references/api/js-sdk#discover-readers)

- DiscoveryConfiguration (iOS)

[DiscoveryConfiguration (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPDiscoveryConfiguration.html)

- DiscoveryConfiguration (Android)

[DiscoveryConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-discovery-configuration/index.html)

- Discover Readers

[Discover Readers](/api/terminal/readers/list)

Stripe Terminal SDKs and server-driven integration come with a built-in simulated card reader, so you can develop and test your app without connecting to physical hardware. Whether your integration is complete or you’re still building it, use the simulated reader to emulate all the Terminal flows in your app.

Note that the simulated reader does not provide a UI. After connecting to it in your app, you can see it working when calls to the Stripe SDK or API succeed.

Simulated readers for SDKs automatically simulate card presentment as needed. For the server-driven integration, update your integration to simulate card presentment.

[simulate card presentment](/terminal/references/testing#simulated-card-presentment)

## Simulated test cards

The simulated reader can be configured to use a simulated test card, enabling you to test different flows within your point of sale application.

Before collecting a payment method, configure the simulated reader to use one of the following test card numbers or test payment methods to produce specific responses.

[cardholder_verification_method](/api/charges/object#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method)

[SCA](/strong-customer-authentication)

[cardholder_verification_method](/api/charges/object#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method)

[cardholder_verification_method](/api/charges/object#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method)

[SCA](/strong-customer-authentication)

[cardholder_verification_method](/api/charges/object#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method)

[decline_code](/declines/codes)

[decline_code](/declines/codes)

[decline_code](/declines/codes)

[refunding a captured charge fails](/refunds#failed-refunds)

[webhook](/api/events/types#event_types-charge.refund.updated)

Using these specific cards for Saving directly without charging and SetupIntents returns a setup_intent_authentication_failure response.

[Saving directly without charging](/terminal/features/saving-cards/save-cards-directly)

[SetupIntents](/api/setup_intents)

[setup_intent_authentication_failure](/error-codes#setup-intent-authentication-failure)

## Physical test cards

Test payments with your Stripe Terminal reader using a physical test card. You can purchase readers and physical test cards from the Terminal tab of the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/terminal/shop)

This physical test card supports both chip entry and contactless payments. It only works with Stripe’s pre-certified readers, and only against the Stripe API in test mode. If you attempt to use your physical test card in live mode, the Stripe API returns an error. Unless stated otherwise, use the PIN 1234 when prompted.

When creating payments using a physical test card, use amounts ending in the following values to produce specific responses:

For example, a payment processed using a physical test card for the amount $25.00 succeeds; a payment processed for the amount $10.05 is declined.

To test your Interac integration, you can use the simulated interac test card or an Interac physical test card. This can be ordered on the Terminal hardware shop in the Dashboard. The Stripe-branded physical test card can’t be used as an Interac card.

[Terminal hardware shop](https://dashboard.stripe.com/terminal/shop)

The Interac test card works for both interac_present payments and interac_present refunds. You can use the same test amounts you use for testing card_present payments. Unless stated otherwise, use the PIN 1234 when prompted. To test a declined refund, create a partial refund with an amount ending with the following decimal values: 01, 05, 55, 65, or 75.

[test amounts](/terminal/references/testing#physical-test-cards)

The Interac test card doesn’t support contactless payments.

To test your eftpos integration, you can use the simulated eftpos test card or an eftpos physical test card. This can be ordered on the Terminal hardware shop in the Dashboard. The Stripe-branded physical test card can’t be used as an eftpos card.

[Terminal hardware shop](https://dashboard.stripe.com/terminal/shop)

You can use the same test amounts you use for testing card_present payments. Unless stated otherwise, use the PIN 1234 when prompted.

[test amounts](/terminal/references/testing#physical-test-cards)

## Simulated card presentment

When using the server-driven integration, use the present_payment_method endpoint to simulate a cardholder tapping or inserting their card on the reader.

[present_payment_method](/api/terminal/readers/present_payment_method)

If you don’t specify parameters, the simulated payment defaults to a valid test card based on the payment method type of the PaymentIntent. Below are the default test cards for Terminal payment method types:

[test card](/terminal/references/testing#standard-test-cards)

With the standard test cards, you can also use test amounts to simulate failure scenarios

[standard test cards](/terminal/references/testing#standard-test-cards)

[test amounts](/terminal/references/testing#physical-test-cards)

## Simulated reader updates

During connection to a simulated Bluetooth reader, you can configure a simulated reader update.

Set the Terminal.shared.simulatorConfiguration.availableReaderUpdate to any of the following configurations. Calling connectBluetoothReader triggers a simulated reader update.

## See also

- Place orders

[Place orders](/terminal/fleet/placing-orders)

- Integration checklist

[Integration checklist](/terminal/references/checklist)
