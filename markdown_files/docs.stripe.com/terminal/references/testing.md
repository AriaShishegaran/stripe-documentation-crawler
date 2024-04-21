htmlTest Stripe Terminal | Stripe Documentation[Skip to content](#main-content)Testing[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Freferences%2Ftesting)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Freferences%2Ftesting)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)# Test Stripe Terminal

Learn how to effectively test your Terminal integration.NoteMuch of the process for testing Stripe Terminal is similar to that for testing online Stripe payments. Also, you can’t use Stripe Terminal with mobile wallets (for example, Apple Pay or Google Pay) in testmode. For more information, see the general Stripe testing guide.

The best way to achieve a successful Terminal deployment is to test every part of your integration. We provide testing tools for each stage:

1. Before ordering a reader, test your integration with the reader simulator.
2. Test your complete hardware integration with a physical test card.

## Simulated reader

### Reference

- [discoverReaders (JavaScript)](/terminal/references/api/js-sdk#discover-readers)
- [DiscoveryConfiguration (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPDiscoveryConfiguration.html)
- [DiscoveryConfiguration (Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-discovery-configuration/index.html)
- [Discover Readers](/api/terminal/readers/list)

Stripe Terminal SDKs and server-driven integration come with a built-in simulated card reader, so you can develop and test your app without connecting to physical hardware. Whether your integration is complete or you’re still building it, use the simulated reader to emulate all the Terminal flows in your app.

Note that the simulated reader does not provide a UI. After connecting to it in your app, you can see it working when calls to the Stripe SDK or API succeed.

Simulated readers for SDKs automatically simulate card presentment as needed. For the server-driven integration, update your integration to simulate card presentment.

## Simulated test cards

The simulated reader can be configured to use a simulated test card, enabling you to test different flows within your point of sale application.

Before collecting a payment method, configure the simulated reader to use one of the following test card numbers or test payment methods to produce specific responses.

### Standard test cards

Test Card NumberTest Payment MethodBrand4242424242424242`visa`Visa4000056655665556`visa_debit`Visa (debit)5555555555554444`mastercard`Mastercard5200828282828210`mastercard_debit`Mastercard (debit)5105105105105100`mastercard_prepaid`Mastercard (prepaid)378282246310005`amex`American Express371449635398431`amex2`American Express6011111111111117`discover`Discover6011000990139424`discover2`Discover3056930009020004`diners`Diners Club36227206271667`diners_14digits`Diners Club (14 digit card)3566002020360505`jcb`JCB6200000000000005`unionpay`UnionPay4506445006931933`interac`Interac6280000360000978`eftpos_au_debit`eftpos Australia4000050360000001`eftpos_au_visa_debit`eftpos Australia/Visa5555050360000080`eftpos_au_mastercard_debit`eftpos Australia/Mastercard### Test cards for specific success cases

Test Card NumberTest Payment MethodResult4001007020000002`offline_pin_cvm`Simulates the cardholder being prompted for and entering anoffline PIN. The resulting charge has[cardholder_verification_method](/api/charges/object#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method)set to`offline_pin`.4000008260000075`offline_pin_sca_retry`Simulates an[SCA](/strong-customer-authentication)-triggered retry flow where a cardholder’s initial contactless charge fails and the reader then prompts the user to insert their card and enter theiroffline PIN.The resulting charge has[cardholder_verification_method](/api/charges/object#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method)set to`offline_pin`.4001000360000005`online_pin_cvm`Simulates a cardholder being prompted for and entering anonline PIN. The resulting charge has[cardholder_verification_method](/api/charges/object#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method)set to`online_pin`.4000002760000008`online_pin_sca_retry`Simulates an[SCA](/strong-customer-authentication)-triggered retry flow where a cardholder’s initial contactless charge fails and the reader then prompts the user to input theironline PIN.The final charge has[cardholder_verification_method](/api/charges/object#charge_object-payment_method_details-card_present-receipt-cardholder_verification_method)set to`online_pin`.### Test cards for specific error cases

Test Card NumberTest Payment MethodResult4000000000000002`charge_declined`Charge is declined with a`card_declined`code.4000000000009995`charge_declined_insufficient_funds`Charge is declined with a`card_declined`code. The[decline_code](/declines/codes)attribute is`insufficient_funds`.4000000000009987`charge_declined_lost_card`Charge is declined with a`card_declined`code. The[decline_code](/declines/codes)attribute is`lost_card`.4000000000009979`charge_declined_stolen_card`Charge is declined with a`card_declined`code. The[decline_code](/declines/codes)attribute is`stolen_card`.4000000000000069`charge_declined_expired_card`Charge is declined with an`expired_card`code.4000000000000119`charge_declined_processing_error`Charge is declined with a`processing_error`code.4000000000005126`refund_fail`Charge succeeds but[refunding a captured charge fails](/refunds#failed-refunds)asynchronously with a`failure_reason`of`expired_or_canceled_card`.Note that because refund failures are asynchronous, the refund will appear to be successful at first and will only have the`failed`status on subsequent fetches.We also notify you of refund failures using the`charge.refund.updated`[webhook](/api/events/types#event_types-charge.refund.updated)event.This simulated error is only supported in the JavaScript SDK.NoteUsing these specific cards for Saving directly without charging and SetupIntents returns a setup_intent_authentication_failure response.

## Physical test cards

Test payments with your Stripe Terminal reader using a physical test card. You can purchase readers and physical test cards from the Terminal tab of the Stripe Dashboard.

This physical test card supports both chip entry and contactless payments. It only works with Stripe’s pre-certified readers, and only against the Stripe API in test mode. If you attempt to use your physical test card in live mode, the Stripe API returns an error. Unless stated otherwise, use the PIN 1234 when prompted.

When creating payments using a physical test card, use amounts ending in the following values to produce specific responses:

DecimalResult00Payment is approved.01Payment is declined with a`call_issuer`code.02When using readers featuring a cardholder-facing screen, insert the test card (if you’re outside the US you can also tap the card) and follow the on-screen prompts to complete the transaction. If a PIN is required, enter`1234`. The payment might decline with an`offline_pin_required`code if the card requires a PIN and the reader doesn’t have a cardholder-facing screen.03When using readers featuring a cardholder-facing screen, insert the test card (if you’re outside the US you can also tap the card) and follow the on-screen prompts to complete the transaction. If a PIN is required, enter any 4-digit PIN. The payment might decline with an`online_or_offline_pin_required`code if the card requires a PIN and the reader doesn’t have a cardholder-facing screen.05Payment is declined with an`generic_decline`code.55Payment is declined with an`incorrect_pin`code.60Payment is declined with an`online_or_offline_pin_required`code.65Payment is declined with an`withdrawal_count_limit_exceeded`code.75Payment is declined with an`pin_try_exceeded`code.For example, a payment processed using a physical test card for the amount $25.00 succeeds; a payment processed for the amount $10.05 is declined.

### Interac test cards Canada only

To test your Interac integration, you can use the simulated interac test card or an Interac physical test card. This can be ordered on the Terminal hardware shop in the Dashboard. The Stripe-branded physical test card can’t be used as an Interac card.

The Interac test card works for both interac_present payments and interac_present refunds. You can use the same test amounts you use for testing card_present payments. Unless stated otherwise, use the PIN 1234 when prompted. To test a declined refund, create a partial refund with an amount ending with the following decimal values: 01, 05, 55, 65, or 75.

NoteThe Interac test card doesn’t support contactless payments.

### eftpos test cards Australia only

To test your eftpos integration, you can use the simulated eftpos test card or an eftpos physical test card. This can be ordered on the Terminal hardware shop in the Dashboard. The Stripe-branded physical test card can’t be used as an eftpos card.

You can use the same test amounts you use for testing card_present payments. Unless stated otherwise, use the PIN 1234 when prompted.

## Simulated card presentment

When using the server-driven integration, use the present_payment_method endpoint to simulate a cardholder tapping or inserting their card on the reader.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/test_helpers/terminal/readers/tmr_xxx/present_payment_method \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"``{
  "id": "tmr_xxx",
  "object": "terminal.reader",
  "action": {
    "failure_code": null,
    "failure_message": null,
    "process_payment_intent": {
      "payment_intent": "pi_xxx"
    },
    "status": "succeeded",
    "type": "process_payment_intent"
  },
  …
}`If you don’t specify parameters, the simulated payment defaults to a valid test card based on the payment method type of the PaymentIntent. Below are the default test cards for Terminal payment method types:

Payment Method TypeTest Card NumberTest Payment Method`card_present`4242424242424242`visa``card_present`and`interac_present`4242424242424242`visa``interac_present`4506445006931933`interac`With the standard test cards, you can also use test amounts to simulate failure scenarios

## Simulated reader updates

During connection to a simulated Bluetooth reader, you can configure a simulated reader update.

iOSAndroidReact NativeSet the Terminal.shared.simulatorConfiguration.availableReaderUpdate to any of the following configurations. Calling connectBluetoothReader triggers a simulated reader update.

Update ConfigurationResult`SimulateReaderUpdateNone`No update, no need to communicate anything to your user.`SimulateReaderUpdateRequired`A required update is available and takes 1 minute. Your`BluetoothReaderDelegate`receives the`didStartInstallingUpdate`callback.`SimulateReaderUpdateAvailable`An optional update is available.  Communicate to the user that an update is available and highlight the`requiredAt`date.`SimulateReaderUpdateLowBattery`An update attempts and fails due to the reader running low on battery.`SimulateReaderUpdateRandom`A random selection of the above scenarios.## See also

- [Place orders](/terminal/fleet/placing-orders)
- [Integration checklist](/terminal/references/checklist)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Simulated reader](#simulated-reader)[Simulated test cards](#simulated-test-cards)[Physical test cards](#physical-test-cards)[Simulated card presentment](#simulated-card-presentment)[Simulated reader updates](#simulated-reader-updates)[See also](#see-also)Products Used[Terminal](/terminal)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`