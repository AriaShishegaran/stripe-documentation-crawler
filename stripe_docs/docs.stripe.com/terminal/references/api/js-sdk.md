# JavaScript API reference

[API methods](#api-methods)

## API methods

- StripeTerminal.create()

[StripeTerminal.create()](#stripeterminal-create)

- discoverReaders()

[discoverReaders()](#discover-readers)

- connectReader()

[connectReader()](#connect-reader)

- disconnectReader()

[disconnectReader()](#disconnect)

- getConnectionStatus()

[getConnectionStatus()](#get-connection-status)

- getPaymentStatus()

[getPaymentStatus()](#get-payment-status)

- clearCachedCredentials()

[clearCachedCredentials()](#clear-cached-credentials)

- collectPaymentMethod()

[collectPaymentMethod()](#collect-payment-method)

- cancelCollectPaymentMethod()

[cancelCollectPaymentMethod()](#cancel-collect-payment-method)

- processPayment()

[processPayment()](#process-payment)

- collectSetupIntentPaymentMethod()

[collectSetupIntentPaymentMethod()](#collect-setup-intent-payment-method)

- cancelCollectSetupIntentPaymentMethod()

[cancelCollectSetupIntentPaymentMethod()](#cancel-collect-setup-intent-payment-method)

- confirmSetupIntent()

[confirmSetupIntent()](#confirm-setup-intent)

- readReusableCard()

[readReusableCard()](#read-reusable-card)

- cancelReadReusableCard()

[cancelReadReusableCard()](#cancel-read-reusable-card)

- setReaderDisplay()

[setReaderDisplay()](#set-reader-display)

- clearReaderDisplay()

[clearReaderDisplay()](#clear-reader-display)

- setSimulatorConfiguration()

[setSimulatorConfiguration()](#stripeterminal-setsimulatorconfig)

- getSimulatorConfiguration()

[getSimulatorConfiguration()](#stripeterminal-getsimulatorconfig)

- collectRefundPaymentMethod()

[collectRefundPaymentMethod()](#stripeterminal-collectrefundpaymentmethod)

- processRefund()

[processRefund()](#stripeterminal-processrefund)

- cancelCollectRefundPaymentMethod()

[cancelCollectRefundPaymentMethod()](#stripeterminal-cancelcollectrefundpaymentmethod)

Creates an instance of StripeTerminal with the given options:

[fetches a connection token](/terminal/payments/setup-integration?terminal-sdk-platform=js#connection-token)

Today, there is only one behavior configuration option:

allowCustomerCancel

A boolean that determines whether the customer can cancel collectPaymentMethod from the reader’s interface. Defaults to false.

Note: This property isn’t broadly available, and we’re not accepting users at this time.

Begins discovering readers with the given options:

[simulated reader](/terminal/references/testing#simulated-reader)

location optional

Return only readers assigned to the given location. This parameter is ignored when discovering a simulated reader.

For more information on using locations to filter discovered readers, see Manage locations.

[Manage locations](/terminal/fleet/locations)

Returns a Promise that resolves to an object with the following fields:

- discoveredReaders: A list of discovered Reader objects, if the command succeeded.

[Reader](/api/terminal/readers/object)

- error: An error, if the command failed.

[error](/terminal/references/api/js-sdk#errors)

Before you can discover the Verifone P400 in your application, you must register the reader to your account.

[register](/terminal/payments/connect-reader?reader-type=internet#register-reader)

Attempts to connect to the given reader with the given options:

[connect](/terminal/payments/connect-reader?reader-type=internet#connect-reader)

Returns a Promise that resolves to an object with the following fields:

- reader: The connected Reader, if the command succeeded.

[Reader](/api/terminal/readers/object)

- error: An error, if the command failed.

[error](/terminal/references/api/js-sdk#errors)

Don’t cache the Reader object in your application. Connecting to a stale Reader can fail if the reader’s IP address has changed.

Disconnects from the connected reader.

Returns the current connection status.

ConnectionStatus can be one of connecting, connected, or not_connected.

Returns the reader’s payment status.

PaymentStatus can be one of not_ready, ready, waiting_for_input, or processing.

Clears the current ConnectionToken, and any other cached credentials.

[ConnectionToken](/terminal/payments/setup-integration?terminal-sdk-platform=js#connection-token)

Use this method to switch accounts in your application (for example, to switch between live and test Stripe API keys on your backend). To switch accounts, follow these steps:

- If a reader is connected, call disconnectReader.

- Configure your onFetchConnectionToken handler to return connection tokens for the new account.

- Call clearCachedCredentials.

- Reconnect to a reader. The SDK requests a new connection token from your onFetchConnectionToken handler.

Begins collecting a payment method for a PaymentIntent. This method takes one required parameter, request:

[collecting a payment method](/terminal/payments/collect-payment#collect-payment)

- request: The clientSecret field from a PaymentIntent object created on your backend. Learn how to create a PaymentIntent and pass its client secret.

[create a PaymentIntent and pass its client secret](/payments/accept-a-payment?platform=web&ui=elements#web-create-intent)

- options: An object containing additional payment parameters.

config_override optional

An object that allows you to specify configuration overrides per transaction. This object defaults to null.

skip_tipping

- Optional, defaults to false. If true, the reader skips the tipping screen.

tipping

- An object that allows you to specify tipping-related options per transaction. It’s described below.

update_payment_intent

- A boolean, when paired with payment_intent_id, instructs the call to update the PaymentIntent and return the attached PaymentMethod with card details.

payment_intent_id

- The id from the PaymentIntent object created on your backend.

enable_customer_cancellation

- Optional, defaults to false. If true, Android-based smart readers show a cancel button.

The following option is available for the tipping object:

eligible_amount optional

A number that allows you to specify the amount of a transaction that percentage-based tips are calculated against. Set this value to 0 or higher.

If it’s equal to 0, tipping is skipped regardless of the value of skip_tipping.

If it’s equal to the payment intent amount, the parameter is ignored and the tip is calculated based on the specified amount.

Returns a Promise that resolves to an object with the following fields:

- paymentIntent: The updated PaymentIntent object, if the command succeeded.

[PaymentIntent object](/api/payment_intents/object)

- error: An error, if the command failed.

[error](/terminal/references/api/js-sdk#errors)

For more information on collecting payments, see our Collecting Payments guide.

[Collecting Payments](/terminal/payments/collect-payment)

Cancels an outstanding collectPaymentMethod command.

[collectPaymentMethod](/terminal/references/api/js-sdk#collect-payment-method)

Returns a Promise that resolves to an empty object when command has been successfully canceled. If cancellation fails, the Promise resolves to an object with an error

[error](/terminal/references/api/js-sdk#errors)

Processes a payment after a payment method has been collected.

[Processes](/terminal/payments/collect-payment#process-payment)

[collected](/terminal/payments/collect-payment#collect-payment)

This method takes one required parameter, paymentIntent:

- paymentIntent: A PaymentIntent object obtained from a successful call to collectPaymentMethod.

- options: An object containing additional payment parameters.

Returns a Promise that resolves to an object with the following fields:

- paymentIntent: The confirmed PaymentIntent object, if the command succeeded.

[PaymentIntent object](/api/payment_intents/object)

- error: An error, if the command failed. For more information, see Handling processing failures.

[error](/terminal/references/api/js-sdk#errors)

[Handling processing failures](/terminal/payments/collect-payment#handling-failures)

Begins collecting a payment method for online reuse for a SetupIntent.

[collecting a payment method for online reuse](/terminal/features/saving-cards/overview)

[SetupIntent](/api/setup_intents/object)

The method takes two required parameters:

- clientSecret: The clientSecret field from a SetupIntent object created on your backend.

clientSecret: The clientSecret field from a SetupIntent object created on your backend.

- customerConsentCollected: A boolean value indicating whether you have collected a customer’s consent to save their cards.

customerConsentCollected: A boolean value indicating whether you have collected a customer’s consent to save their cards.

- config: an optional object containing collection configuration.

config: an optional object containing collection configuration.

enable_customer_cancellation

Optional, defaults to false.

If true, Android-based smart readers show a cancel button.

Returns a Promise that resolves to an object with the following fields:

- setupIntent: The updated SetupIntent object, if the command succeeded.

[SetupIntent object](/api/setup_intents/object)

- error: An error, if the command failed.

[error](/terminal/references/api/js-sdk#errors)

For more information on saving cards, see our Saving cards for online payments guide.

[Saving cards for online payments](/terminal/features/saving-cards/overview)

Cancels an outstanding collectSetupIntentPaymentMethod command.

[collectSetupIntentPaymentMethod](#collect-setup-intent-payment-method)

Returns a Promise that resolves to an empty object when the command has been successfully canceled. If cancellation fails, the Promise resolves to an object with an error

[error](/terminal/references/api/js-sdk#errors)

Confirms a SetupIntent after a payment method has been collected.

[Confirms](/terminal/features/saving-cards/save-cards-directly#submit-payment-method)

[collected](/terminal/features/saving-cards/save-cards-directly#collect-payment-method)

This method takes a single parameter, a SetupIntent object obtained from a successful call to collectSetupIntentPaymentMethod.

Returns a Promise that resolves to an object with the following fields:

- setupIntent: The confirmed SetupIntent object, if the command succeeded.

[SetupIntent object](/api/setup_intents/object)

- error: An error, if the command failed.

[error](/terminal/references/api/js-sdk#errors)

Reads a card for online reuse.

[online reuse](/terminal/features/saving-cards/overview)

Online payments initiated from Terminal do not benefit from the lower pricing and liability shift given to standard Terminal payments. Most integrations do not need to use readReusableCard. To only collect an in-person payment from a customer, use the standard flow.

[lower pricing](https://stripe.com/terminal#pricing)

[standard Terminal payments](/terminal/payments/collect-payment)

[standard flow](/terminal/payments/collect-payment)

Returns a Promise that resolves to an object with the following fields:

- payment_method: The PaymentMethod object, if the command succeeded.

[PaymentMethod object](/api/payment_methods/object)

- error: An error, if the command failed.

[error](/terminal/references/api/js-sdk#errors)

Currently, you can’t use Stripe Terminal to save contactless cards and mobile wallets (for example, Apple Pay, Google Pay) for later reuse.

Cancels an outstanding readReusableCard command.

[readReusableCard](/terminal/references/api/js-sdk#read-reusable-card)

Returns a Promise that resolves to an empty object when the command has been successfully canceled. If cancellation fails, the Promise resolves to an object with an error.

[error](/terminal/references/api/js-sdk#errors)

Updates the reader display with cart details.

[cart details](/terminal/features/display)

This method takes a DisplayInfo object as input.

Returns a Promise that resolves to an empty object if the command succeeds. If the command fails, the Promise resolves to an object with an error.

[error](/terminal/references/api/js-sdk#errors)

If the reader is displaying cart details set with setReaderDisplay, this method clears the screen and resets it to the splash screen.

Returns a Promise that resolves to an empty object if the command succeeds. If the command fails, the Promise resolves to an object with an error.

[error](/terminal/references/api/js-sdk#errors)

Sets the configuration object for the simulated card reader.

[simulated card reader](/terminal/references/testing#simulated-reader)

This method only takes effect when connected to the simulated reader; it performs no action otherwise.

The simulated reader will follow the specified configuration only until processPayment is complete. At that point, the simulated reader will revert to its default behavior.

Note that this method overwrites any currently active configuration object; to add specific key-value pairs to the object, make sure to use a combination of this method and getSimulatorConfiguration.

The configuration options available are:

[Simulated test cards](/terminal/references/testing#simulated-test-cards)

[Simulated test cards](/terminal/references/testing#simulated-test-cards)

- card_present (default)

- interac_present

Returns the currently active configuration object.

The Stripe Terminal JavaScript SDK may overwrite this value as necessary, including (but not limited to) resetting the value after processPayment is complete, and removing unknown key-value pairs.

Begins collecting a payment method to be refunded. The method takes two required parameters:

- charge_id, the ID of the charge that will be refunded.

- amount: a number that represents the amount, in cents, that will be refunded from the charge. This number must be less than or equal to the amount that was charged in the original payment.

- currency: Three-letter ISO code for the currency, in lowercase. Must be a supported currency.

[ISO code for the currency](/currencies)

[supported currency](/currencies)

- options: an optional object containing additional refund parameters.

refund_application_fee

Optional, defaults to false. Connect only.

Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded.

An application fee can be refunded only by the application that created the charge.

reverse_transfer

Optional, defaults to false. Connect only.

Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount).

A transfer can be reversed only by the application that created the charge.

- config: an optional object containing collection configuration.

enable_customer_cancellation

Optional, defaults to false.

If true, Android-based smart readers show a cancel button.

Returns a Promise that resolves to either:

- an empty object if the payment method collection was successful, or

- an object with an error field if there was an error while collecting the refund payment method.

[error](/terminal/references/api/js-sdk#errors)

Processes an in-progress refund. This method can only be successfully called after collectRefundPaymentMethod has returned successfully.

Returns a Promise that resolves to either:

- a refund object if the refund was successful, or

- an object with an error field if there was an error while processing the refund.

[error](/terminal/references/api/js-sdk#errors)

Cancels an outstanding collectRefundPaymentMethod command.

Returns a Promise that resolves to an empty object if the cancellation was successful. If the cancellation fails, the Promise resolves to an object with an error field.

[Errors](#errors)

## Errors

Errors returned by the JavaScript SDK include an error code, as well as a human-readable message.

For methods involving a PaymentIntent like processPayment, the error may also include a payment_intent object.

[processPayment](/terminal/payments/collect-payment#handling-failures)

[Locations](/terminal/fleet/locations)

[Changelog](#changelog)

## Changelog

If you’re using an earlier version of the JavaScript SDK (before June 7, 2019), update to the latest release by changing the URL of the script your integration includes.

[https://js.stripe.com/terminal/v1/](https://js.stripe.com/terminal/v1/)

For more information on migrating from the Stripe Terminal beta, see the Terminal Beta Migration Guide.

[Terminal Beta Migration Guide](/terminal/references/sdk-migration-guide)

- Renamed confirmPaymentIntent to processPayment.

- Renamed the values for PaymentStatus. PaymentStatus can be one of not_ready, ready, waiting_for_input, or processing.

- Removed card details from the response to collectPaymentMethod, previously available in response.paymentIntent.payment_method.card_payment.

- Receipt information is now located in the payment_intent.charges[0].payment_method_details.card_present hash.

- Changed the API for discovering a simulated reader to discoverReaders({ simulated: true }).

- Renamed readSource to readReusableCard. A successful call to readReusableCard returns a PaymentMethod instead of a Source. Payment Methods must be used with Payment Intents. For more information, see the Payment Methods API overview.

[PaymentMethod](/api/payment_methods)

[Payment Methods API](/payments/payment-methods)

- Changed the response of connectReader to { reader: Reader }, removing the wrapper Connection object.

- Removed the startReaderDiscovery and stopReaderDiscovery methods. To repeatedly discover readers, you can use the JavaScript setInterval method.

- Renamed clearConnectionToken to clearCachedCredentials.
