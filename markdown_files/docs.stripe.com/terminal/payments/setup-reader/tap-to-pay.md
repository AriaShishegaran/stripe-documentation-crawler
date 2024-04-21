htmlTap to Pay | Stripe Documentation[Skip to content](#main-content)Tap to Pay[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fpayments%2Fsetup-reader%2Ftap-to-pay)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Fpayments%2Fsetup-reader%2Ftap-to-pay)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)[Select your reader](/docs/terminal/payments/setup-reader)# Tap to Pay

Accept contactless payments on a compatible iPhone or Android device with the Stripe Terminal SDK.iOSAndroidUse Tap to Pay on iPhone to accept in-person contactless payments with a compatible iPhone and the Stripe Terminal SDK. Tap to Pay on iPhone includes support for Visa, Mastercard, American Express contactless cards, and NFC-based mobile wallets (Apple Pay, Google Pay, and Samsung Pay). PIN entry is supported in eligible markets. Discover support is also included in the US only. Stripe includes Tap to Pay on iPhone in the Terminal iOS SDK and enables payments directly in your iOS mobile app.

NoteFor platforms, use of Tap to Pay on iPhone is subject to the Apple Acceptance Platform User Terms and Conditions.

### Availability

AustraliaUnited KingdomUnited States### Available in Beta

FranceNetherlandsNotePlatforms and businesses located outside the US, Australia, and the United Kingdom aren’t permitted to use Tap to Pay on iPhone unless participating in our international beta program. If you’re interested in joining the beta program, please contact us.

## Get started

Tap to Pay on iPhone requires the latest version of the Terminal iOS SDK, and introduces a connectLocalMobileReader method and an SCPDiscoveryMethodLocalMobile discovery option.

You must first set up the Terminal iOS SDK. After you’re familiar with the iOS SDK, you can start supporting Tap to Pay on iPhone within your application.

### Entitlements and build file

To use Tap to Pay on iPhone to accept payments, your application must request and configure the Tap to Pay on iPhone entitlement from your Apple Developer account. Instructions for requesting this entitlement can be found here.

After you add an entitlements file to your app build target, add the following:

Key`com.apple.developer.proximity-reader.payment.acceptance`Value type`boolean`Value`true`or`1`## Supported devices

Tap to Pay on iPhone requires:

- An iPhone XS or later running iOS 16.0 or later in the United States.
- An iPhone XS or later running iOS 16.4 or later in Australia and the United Kingdom.
- An iPhone XS or later running iOS 17.0 or later in France and the Netherlands.

We recommend asking your users to update to the latest iOS version for the best performance.

NoteTap to Pay won’t work on beta releases of iOS.

## Cardholder verification limits and fallback

Some contactless card transactions above certain amounts might require additional cardholder verification methods (CVM) such as PIN entry. Tap to Pay on iPhone supports PIN entry for devices running iOS 16.4+. NFC wallet payments (Apple Pay, Google Pay, and Samsung Pay) might not be subject to these same limits.

In the UK, some cards might be required to be inserted into a device due to Strong Customer Authentication requirements, which depend on your issuer. In that case, the payment will be declined before the PIN screen appears with the reason offline_pin_required. In that scenario, we recommend instructing the customer to use a different card or another method to collect payment, such as a Terminal card reader or sending a Stripe Payment Link.

## Best practices and promotion guidelines

Follow the Human Interface Guidelines for Tap to Pay on iPhone to ensure of an optimal user experience and successful review process with Apple.

Consider the following:

- Connect to the reader in the background on app startup to reduce wait times when collecting a payment.
- Reconnect to the reader when the app comes to the foreground to reduce wait times.
- Provide merchant education to guide your users on how to accept contactless payments on a compatible iPhone, including in-product promotion and text or email alerts. See Apple’s[developer marketing guidance](https://developer.apple.com/tap-to-pay/marketing-guidelines/)and[merchant education](https://developer.apple.com/tap-to-pay/how-to-accept-payments/)for more ideas.
- Launch and promote your Tap to Pay on iPhone marketing campaigns using our messaging templates and design assets following[Apple’s brand guidelines](https://developer.apple.com/tap-to-pay/marketing-guidelines/#editorial-guidelines). Become a Stripe Partner[here](https://stripe.com/partners/become-a-partner)to access these assets in the[partner portal](https://portal.stripe.partners/s).

## Next steps

- [Set up your integration](/terminal/payments/setup-integration)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Get started](#get-started)[Supported devices](#supported-devices)[Cardholder verification limits and fallback](#fallback)[Best practices and promotion guidelines](#best-practices)[See also](#next-steps)Products Used[Terminal](/terminal)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`