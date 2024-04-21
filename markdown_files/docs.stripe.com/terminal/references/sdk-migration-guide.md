htmlTerminal SDK migration guide | Stripe Documentation[Skip to content](#main-content)SDK migration guide[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Freferences%2Fsdk-migration-guide)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Freferences%2Fsdk-migration-guide)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)# Terminal SDK migration guide

Learn how to migrate to the latest version of the Stripe Terminal SDK.The Stripe Terminal iOS and Android SDKs have been updated with a number of breaking changes in APIs and behavior, some of which require that you update your integration with the Stripe Terminal SDK. We regularly make changes in major version updates that may affect the way your integration works or behaves, to improve consistency between our SDKs andto simplify your application logic and integration. This guide walks you through the latest changes to help you upgrade your integration.

NoteBuilding a new Stripe Terminal integration? Visit our Design an integration page to learn how to get started.

## Migrate to version 3.0.0

Here are some things you need to know about the 3.0.0 Stripe Terminal iOS and Android SDKs:

- Support for processing offline paymentsBeta  - The offline mode feature is in private beta. To request access, please email[stripe-terminal-betas@stripe.com](mailto:stripe-terminal-betas@stripe.com). After we enable the changes in the backend for your account, you must disconnect and reconnect to your reader using the SDK for the updated configuration to take effect.


- Updates to minimum supported platform versions for iOS and Android
- Removal of deprecated features and properties

iOSAndroidIf your application currently uses an Terminal iOS SDK version prior to 3.0.0, there are a few changes you need to make to upgrade and accept card present payments globally. For a detailed list of the changes from version 2.23.1 to 3.0.0, please reference the SDK changelog.

### Update your minimum supported version to iOS 13 or higher

We regularly update the minimum supported version of our SDKs in order to focus on providing the best experience for our developers.

Existing 2.X versions of the Terminal iOS SDK will continue to support devices running iOS 11 and higher.

### Update your DiscoveryConfiguration usage to the specific DiscoveryConfiguration implementation

In order to support configuration for different discovery methods, SCPDiscoveryConfiguration is now a protocol that is implemented by several different types. Instead of providing a DiscoveryMethod, there are now individual classes to choose from in order to search for a specific type of reader:

Configuration ClassUsage[SCPBluetoothScanDiscoveryConfiguration](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPBluetoothScanDiscoveryConfiguration.html)Bluetooth-capable readers near this iOS device[SCPBluetoothProximityDiscoveryConfiguration](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPBluetoothProximityDiscoveryConfiguration.html)A subset of Bluetooth-capable readers near this iOS device[SCPInternetDiscoveryConfiguration](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPInternetDiscoveryConfiguration.html)Internet-connected readers registered to this account[SCPLocalMobileDiscoveryConfiguration](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPLocalMobileDiscoveryConfiguration.html)[Tap to Pay](/terminal/payments/setup-reader/tap-to-pay?platform=ios)using this iOS device’s NFC readerCreate the discovery configuration appropriate for your desired discovery method using the provided builder class and provide that to discoverReaders. The builder exposes setters for the properties that each configuration supports.

### Update your discoverReaders and connectReader usage

- Canceling`discoverReaders`now calls the completion block with an error with code`SCPErrorCanceled`, just like all other cancelable methods.
- `discoverReaders`is now completed successfully right when`connectReader`is called. If`connectReader`fails, your integration needs to make a new call to`discoverReaders`in order to resume discovering readers.
- `discoverReaders`is no longer required to be running for`connectReader`to work. You’re now able to call`connectReader`with a previously discovered reader instance or to retry connecting without restarting`discoverReaders`.

### Update your ReconnectionDelegate implementation

SCPReconnectionDelegate now provides the instance of the reader that is being reconnected to instead of the Terminal instance. If you implemented this delegate before you need to replace terminal in the method names with reader.

### Update Parameters and Configuration class usage to use Builders

The input classes like SCPCollectConfiguration and SCPPaymentIntentParameters are now immutable and have associated builders provided to create them. All builders have a build method that validates the inputs and creates the class it builds.

- In Swift,`build()`throws and should be checked for errors.
- In Objective-C, you provide an`NSError **`out-parameter to receive the error, if any.

[Swift](#)`let paymentParams = try PaymentIntentParametersBuilder(amount: 100, currency: "cad")
  .setCaptureMethod(.automatic)
  .build()`### Remove any dependency on SCPErrorBusy

SCPErrorBusy is removed. In SDK 3.0.0 and later, if you call a Terminal method while another is still in-progress the new calls now queue up. The commands are executed after all previous commands complete. If you were previously tracking state to prevent SCPErrorBusy, or were queuing your own commands to work around SCPErrorBusy, you can now make use of the command queue to simplify your code. If your application relied on SCPErrorBusy to know if a command is running, review your code to see if this could cause problems with queuing too many commands.

### Review support for Offline Payments

SCPPaymentIntent.stripeId is null for offline payments. If your integration only supports online payments, the stripeId will always be present and no changes are needed beyond checks to satisfy the presence of the ID. See Collect payments while offline for more details on how to process payments offline.

[Swift](#)`Terminal.shared.createPaymentIntent(params) { intent, error in
  if let error = error {
    // Placeholder for handling exception
  }
  guard let intentId = intent.stripeId else {
    // PaymentIntent was created offline without an id. See intent.offlineDetails.
    // This is only expected when offline mode is enabled.
  }
}`### Update your process calls to confirm

SCPTerminal.processPayment is renamed to SCPTerminal.confirmPaymentIntent and SCPTerminal.processRefund is renamed to SCPTerminal.confirmRefund. The parameters for these methods haven’t changed but the error types have also been renamed to SCPConfirmPaymentIntentError and SCPConfirmRefundError respectively.

### Update your readReusableCard usage to SetupIntents

SCPTerminal.readReusableCard is removed. SetupIntents are the recommended path for saving cards without charging. SetupIntents follow a similar pattern to PaymentIntents where you create, collect, and then confirm the SetupIntent in the SDK. See Save cards for online payments for more details.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`