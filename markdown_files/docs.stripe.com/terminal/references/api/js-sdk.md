htmlJavaScript API reference | Stripe Documentation[Skip to content](#main-content)JavaScript API reference[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Freferences%2Fapi%2Fjs-sdk)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Freferences%2Fapi%2Fjs-sdk)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)[API references](/docs/terminal/references/api)# JavaScript API reference

Use our API reference to navigate the Stripe Terminal JavaScript SDK.[API methods](#api-methods)- [StripeTerminal.create()](#stripeterminal-create)
- [discoverReaders()](#discover-readers)
- [connectReader()](#connect-reader)
- [disconnectReader()](#disconnect)
- [getConnectionStatus()](#get-connection-status)
- [getPaymentStatus()](#get-payment-status)
- [clearCachedCredentials()](#clear-cached-credentials)
- [collectPaymentMethod()](#collect-payment-method)
- [cancelCollectPaymentMethod()](#cancel-collect-payment-method)
- [processPayment()](#process-payment)
- [collectSetupIntentPaymentMethod()](#collect-setup-intent-payment-method)
- [cancelCollectSetupIntentPaymentMethod()](#cancel-collect-setup-intent-payment-method)
- [confirmSetupIntent()](#confirm-setup-intent)
- [readReusableCard()](#read-reusable-card)
- [cancelReadReusableCard()](#cancel-read-reusable-card)
- [setReaderDisplay()](#set-reader-display)
- [clearReaderDisplay()](#clear-reader-display)
- [setSimulatorConfiguration()](#stripeterminal-setsimulatorconfig)
- [getSimulatorConfiguration()](#stripeterminal-getsimulatorconfig)
- [collectRefundPaymentMethod()](#stripeterminal-collectrefundpaymentmethod)
- [processRefund()](#stripeterminal-processrefund)
- [cancelCollectRefundPaymentMethod()](#stripeterminal-cancelcollectrefundpaymentmethod)

### StripeTerminal.create([options])

Creates an instance of StripeTerminal with the given options:

OptionDescriptiononFetchConnectionTokenAn event handler that[fetches a connection token](/terminal/payments/setup-integration?terminal-sdk-platform=js#connection-token)from your backend.onUnexpectedReaderDisconnectAn event handler called when a reader disconnects from your app.onConnectionStatusChangeoptionalAn event handler called when the SDK’s ConnectionStatus changes.onPaymentStatusChangeoptionalAn event handler called when the SDK’s PaymentStatus changes.readerBehavioroptionalAn object that sets the behavior on the reader throughout the lifecycle of the SDK. See below for readerBehavior configuration options.### Reader Behavior Configuration

Today, there is only one behavior configuration option:

BehaviorDescriptionallowCustomerCancel

A boolean that determines whether the customer can cancel collectPaymentMethod from the reader’s interface. Defaults to false.

Note: This property isn’t broadly available, and we’re not accepting users at this time.

### discoverReaders([options])

Begins discovering readers with the given options:

OptionDescriptionsimulatedoptionalA boolean value indicating whether to discover a[simulated reader](/terminal/references/testing#simulated-reader). If left empty, this value defaults to`false`.location optional

Return only readers assigned to the given location. This parameter is ignored when discovering a simulated reader.

For more information on using locations to filter discovered readers, see Manage locations.

Returns a Promise that resolves to an object with the following fields:

- `discoveredReaders`: A list of discovered[Reader](/api/terminal/readers/object)objects, if the command succeeded.
- `error`: An[error](/terminal/references/api/js-sdk#errors), if the command failed.

NoteBefore you can discover the Verifone P400 in your application, you must register the reader to your account.

### connectReader(reader, connectOptions)

Attempts to connect to the given reader with the given options:

OptionDescriptionfail_if_in_useoptionalA boolean value indicating that the connection fails if the reader is currently connected to a Terminal SDK. If left empty, this value defaults to`false`.Returns a Promise that resolves to an object with the following fields:

- `reader`: The connected[Reader](/api/terminal/readers/object), if the command succeeded.
- `error`: An[error](/terminal/references/api/js-sdk#errors), if the command failed.

NoteDon’t cache the Reader object in your application. Connecting to a stale Reader can fail if the reader’s IP address has changed.

### disconnectReader()

Disconnects from the connected reader.

### getConnectionStatus()

Returns the current connection status.

ConnectionStatus can be one of connecting, connected, or not_connected.

### getPaymentStatus()

Returns the reader’s payment status.

PaymentStatus can be one of not_ready, ready, waiting_for_input, or processing.

### clearCachedCredentials()

Clears the current ConnectionToken, and any other cached credentials.

Use this method to switch accounts in your application (for example, to switch between live and test Stripe API keys on your backend). To switch accounts, follow these steps:

1. If a reader is connected, call`disconnectReader`.
2. Configure your`onFetchConnectionToken`handler to return connection tokens for the new account.
3. Call`clearCachedCredentials`.
4. Reconnect to a reader. The SDK requests a new connection token from your`onFetchConnectionToken`handler.

### collectPaymentMethod(request, options)

Begins collecting a payment method for a PaymentIntent. This method takes one required parameter, request:

- `request`: The`clientSecret`field from a`PaymentIntent`object created on your backend. Learn how to[create a PaymentIntent and pass its client secret](/payments/accept-a-payment?platform=web&ui=elements#web-create-intent).
- `options`: An object containing additional payment parameters.

OptionDescriptionconfig_override optional

An object that allows you to specify configuration overrides per transaction. This object defaults to null.

skip_tipping

- Optional, defaults to false. If true, the reader skips the tipping screen.

tipping

- An object that allows you to specify tipping-related options per transaction. It’s described below.

update_payment_intent

- A boolean, when paired with`payment_intent_id`, instructs the call to update the`PaymentIntent`and return the attached`PaymentMethod`with card details.

payment_intent_id

- The`id`from the`PaymentIntent`object created on your backend.

enable_customer_cancellation

- Optional, defaults to false. If true, Android-based smart readers show a cancel button.

`{
  update_payment_intent: boolean,
  payment_intent_id: string,
  enable_customer_cancellation: boolean,
  skip_tipping: boolean,
  tipping: object
}`The following option is available for the tipping object:

OptionDescriptioneligible_amount optional

A number that allows you to specify the amount of a transaction that percentage-based tips are calculated against. Set this value to 0 or higher.

If it’s equal to 0, tipping is skipped regardless of the value of skip_tipping.

If it’s equal to the payment intent amount, the parameter is ignored and the tip is calculated based on the specified amount.

`{
  eligible_amount: number,
}`Returns a Promise that resolves to an object with the following fields:

- `paymentIntent`: The updated[PaymentIntent object](/api/payment_intents/object), if the command succeeded.
- `error`: An[error](/terminal/references/api/js-sdk#errors), if the command failed.

For more information on collecting payments, see our Collecting Payments guide.

### cancelCollectPaymentMethod()

Cancels an outstanding collectPaymentMethod command.

Returns a Promise that resolves to an empty object when command has been successfully canceled. If cancellation fails, the Promise resolves to an object with an error

### processPayment(paymentIntent, options)

Processes a payment after a payment method has been collected.

This method takes one required parameter, paymentIntent:

- `paymentIntent`: A`PaymentIntent`object obtained from a successful call to`collectPaymentMethod`.
- `options`: An object containing additional payment parameters.

Returns a Promise that resolves to an object with the following fields:

- `paymentIntent`: The confirmed[PaymentIntent object](/api/payment_intents/object), if the command succeeded.
- `error`: An[error](/terminal/references/api/js-sdk#errors), if the command failed. For more information, see[Handling processing failures](/terminal/payments/collect-payment#handling-failures).

### collectSetupIntentPaymentMethod(clientSecret, customerConsentCollected, config)

Begins collecting a payment method for online reuse for a SetupIntent.

The method takes two required parameters:

- clientSecret: The clientSecret field from a SetupIntent object created on your backend.


- customerConsentCollected: A boolean value indicating whether you have collected a customer’s consent to save their cards.


- config: an optional object containing collection configuration.



OptionDescriptionenable_customer_cancellation

Optional, defaults to false.

If true, Android-based smart readers show a cancel button.

Returns a Promise that resolves to an object with the following fields:

- `setupIntent`: The updated[SetupIntent object](/api/setup_intents/object), if the command succeeded.
- `error`: An[error](/terminal/references/api/js-sdk#errors), if the command failed.

For more information on saving cards, see our Saving cards for online payments guide.

### cancelCollectSetupIntentPaymentMethod()

Cancels an outstanding collectSetupIntentPaymentMethod command.

Returns a Promise that resolves to an empty object when the command has been successfully canceled. If cancellation fails, the Promise resolves to an object with an error

### confirmSetupIntent(setupIntent)

Confirms a SetupIntent after a payment method has been collected.

This method takes a single parameter, a SetupIntent object obtained from a successful call to collectSetupIntentPaymentMethod.

Returns a Promise that resolves to an object with the following fields:

- `setupIntent`: The confirmed[SetupIntent object](/api/setup_intents/object), if the command succeeded.
- `error`: An[error](/terminal/references/api/js-sdk#errors), if the command failed.

### readReusableCard()

Reads a card for online reuse.

Online payments initiated from Terminal do not benefit from the lower pricing and liability shift given to standard Terminal payments. Most integrations do not need to use readReusableCard. To only collect an in-person payment from a customer, use the standard flow.

Returns a Promise that resolves to an object with the following fields:

- `payment_method`: The[PaymentMethod object](/api/payment_methods/object), if the command succeeded.
- `error`: An[error](/terminal/references/api/js-sdk#errors), if the command failed.

NoteCurrently, you can’t use Stripe Terminal to save contactless cards and mobile wallets (for example, Apple Pay, Google Pay) for later reuse.

### cancelReadReusableCard()

Cancels an outstanding readReusableCard command.

Returns a Promise that resolves to an empty object when the command has been successfully canceled. If cancellation fails, the Promise resolves to an object with an error.

### setReaderDisplay(displayInfo)

Updates the reader display with cart details.

This method takes a DisplayInfo object as input.

`{
    type: 'cart',
    cart: {
      line_items: [
        {
          description: string,
          amount: number,
          quantity: number,
        },
      ],
      tax: number,
      total: number,
      currency: string,
    }
  }`Returns a Promise that resolves to an empty object if the command succeeds. If the command fails, the Promise resolves to an object with an error.

### clearReaderDisplay()

If the reader is displaying cart details set with setReaderDisplay, this method clears the screen and resets it to the splash screen.

Returns a Promise that resolves to an empty object if the command succeeds. If the command fails, the Promise resolves to an object with an error.

### setSimulatorConfiguration(configuration)

Sets the configuration object for the simulated card reader.

This method only takes effect when connected to the simulated reader; it performs no action otherwise.

The simulated reader will follow the specified configuration only until processPayment is complete. At that point, the simulated reader will revert to its default behavior.

Note that this method overwrites any currently active configuration object; to add specific key-value pairs to the object, make sure to use a combination of this method and getSimulatorConfiguration.

The configuration options available are:

FieldValuesDescriptiontestCardNumberRefer to the[Simulated test cards](/terminal/references/testing#simulated-test-cards)list.Configures the simulated reader to use a test card number as the payment method presented by the user. Use it to test different scenarios in your integration, such as payments with different card brands or processing errors like a declined charge.testPaymentMethodRefer to the[Simulated test cards](/terminal/references/testing#simulated-test-cards)list.Serves the same purpose as`testCardNumber`, but relies on test payment methods instead.tipAmountAny amount or null.Configures the simulated reader to simulate an on-reader tip amount selected by the customer.paymentMethodTypedeprecated- `card_present`(default)
- `interac_present`

Determine the type of payment method created by the simulated reader when`collectPaymentMethod`is called.### getSimulatorConfiguration()

Returns the currently active configuration object.

The Stripe Terminal JavaScript SDK may overwrite this value as necessary, including (but not limited to) resetting the value after processPayment is complete, and removing unknown key-value pairs.

### collectRefundPaymentMethod(charge_id, amount, currency, options, config)

Begins collecting a payment method to be refunded. The method takes two required parameters:

- `charge_id`, the ID of the charge that will be refunded.
- `amount`: a number that represents the amount, in cents, that will be refunded from the charge. This number must be less than or equal to the amount that was charged in the original payment.
- `currency`: Three-letter[ISO code for the currency](/currencies), in lowercase. Must be a[supported currency](/currencies).
- `options`: an optional object containing additional refund parameters.

OptionDescriptionrefund_application_fee

Optional, defaults to false. Connect only.

Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded.

An application fee can be refunded only by the application that created the charge.

reverse_transfer

Optional, defaults to false. Connect only.

Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount).

A transfer can be reversed only by the application that created the charge.

- `config`: an optional object containing collection configuration.

OptionDescriptionenable_customer_cancellation

Optional, defaults to false.

If true, Android-based smart readers show a cancel button.

Returns a Promise that resolves to either:

- an empty object if the payment method collection was successful, or
- an object with an[error](/terminal/references/api/js-sdk#errors)field if there was an error while collecting the refund payment method.

### processRefund()

Processes an in-progress refund. This method can only be successfully called after collectRefundPaymentMethod has returned successfully.

Returns a Promise that resolves to either:

- a refund object if the refund was successful, or
- an object with an[error](/terminal/references/api/js-sdk#errors)field if there was an error while processing the refund.

### cancelCollectRefundPaymentMethod()

Cancels an outstanding collectRefundPaymentMethod command.

Returns a Promise that resolves to an empty object if the cancellation was successful. If the cancellation fails, the Promise resolves to an object with an error field.

[Errors](#errors)Errors returned by the JavaScript SDK include an error code, as well as a human-readable message.

For methods involving a PaymentIntent like processPayment, the error may also include a payment_intent object.

Error codes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

CodeDescription`no_established_connection`The command failed because no reader is connected.`no_active_collect_payment_method_attempt``cancelCollectPaymentMethod`can only be called when`collectPaymentMethod`is in progress.`no_active_read_reusable_card_attempt``cancelCollectReusableCard`can only be called when`readReusableCard`is in progress.`canceled`The command was canceled.`cancelable_already_completed`Cancellation failed because the operation has already completed.`cancelable_already_canceled`Cancellation failed because the operation has already been canceled.`network_error`An unknown error occurred when communicating with the server or reader over the network. Refer to the error message for more information.`network_timeout`The request timed out when communicating with the server or reader over the network. Make sure both your device and the reader are connected to the network with stable connections.`already_connected``connectReader`failed because a reader is already connected.`failed_fetch_connection_token`Failed to fetch a connection token. Make sure your connection token handler returns a promise that resolves to the connection token.`discovery_too_many_readers``discoverReaders`returned too many readers. Use[Locations](/terminal/fleet/locations)to filter discovered readers by location.`invalid_reader_version`The reader is running an unsupported software version. Please allow the reader to update and try again.`reader_error`The reader returned an error while processing the request. Refer to the error message for more information.`command_already_in_progress`The action can’t be performed, because an in-progress action is preventing it.[Changelog](#changelog)If you’re using an earlier version of the JavaScript SDK (before June 7, 2019), update to the latest release by changing the URL of the script your integration includes.

`<script src="https://js.stripe.com/terminal/v1/"></script>`For more information on migrating from the Stripe Terminal beta, see the Terminal Beta Migration Guide.

v1![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Renamed`confirmPaymentIntent`to`processPayment`.
- Renamed the values for PaymentStatus. PaymentStatus can be one of`not_ready`,`ready`,`waiting_for_input`, or`processing`.
- Removed card details from the response to`collectPaymentMethod`, previously available in`response.paymentIntent.payment_method.card_payment`.
- Receipt information is now located in the`payment_intent.charges[0].payment_method_details.card_present`hash.
- Changed the API for discovering a simulated reader to`discoverReaders({ simulated: true })`.
- Renamed`readSource`to`readReusableCard`. A successful call to`readReusableCard`returns a[PaymentMethod](/api/payment_methods)instead of a Source. Payment Methods must be used with Payment Intents. For more information, see the[Payment Methods API](/payments/payment-methods)overview.
- Changed the response of`connectReader`to`{ reader: Reader }`, removing the wrapper`Connection`object.
- Removed the`startReaderDiscovery`and`stopReaderDiscovery`methods. To repeatedly discover readers, you can use the JavaScript`setInterval`method.
- Renamed`clearConnectionToken`to`clearCachedCredentials`.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[API methods](#api-methods)[Errors](#errors)[Changelog](#changelog)Products Used[Terminal](/terminal)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`