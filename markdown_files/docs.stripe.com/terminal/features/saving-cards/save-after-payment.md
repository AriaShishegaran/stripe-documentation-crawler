htmlSave card details after payment | Stripe Documentation[Skip to content](#main-content)Save after payment[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Fsaving-cards%2Fsave-after-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Fsaving-cards%2Fsave-after-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)[Save cards for future use](/docs/terminal/features/saving-cards/overview)# Save card details after payment

Save card details from an in-person transaction for deferred payments.Available in:Use Stripe Terminal to save card details for online reuse while processing in-person transactions.

When you successfully confirm a payment, the returned object contains a successful charge ID. This charge contains a generated_card ID, which represents the ID of a card PaymentMethod that’s used to charge the saved card.

The initial, in-person payment benefits from the liability shift (and in certain markets, lower pricing given to standard Terminal payments). But subsequent payments happen online and they’re treated as card-not-present. For example, a gym customer pays for an initial session in person and begins a membership in the same transaction. Or a clothing store collects a customer’s email address and payment method at the checkout counter during purchase, and the customer can log in later and use it again.

You can automatically attach the generated_card PaymentMethod to a customer object to easily retrieve saved card details in the future. When creating a PaymentIntent, provide a customer ID and set the setup_future_usage parameter to indicate you intend to make future payments with the payment method.

NoteUnless your business is a car rental service or hotel, you can’t save mobile wallets (for example, Apple Pay or Google Pay) for later reuse while transacting. We have a limited private beta available for users with a car rental service or hotel. To request access, please contact stripe-terminal-betas@stripe.com.

### Client-side

With the iOS, Android, and React Native SDKs, you can create a PaymentIntent client-side and provide the customer and set setup_future_usage.

JavaScriptiOSAndroidReact Native.NETBetaNoteClient-side PaymentIntent creation is possible with the iOS or Android SDKs. If you’re using the JavaScript SDK for Stripe Terminal, create a PaymentIntent server-side.

### Server-side

The JavaScript SDK and server-driven integration require you to create the PaymentIntent on your server. For iOS or Android, you can create the PaymentIntent on your server if the information required to start a payment isn’t readily available in your app.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "payment_method_types[]"=card_present \
  -d amount=1099 \
  -d currency=usd \
  -d customer={{CUSTOMER_ID}} \
  -d setup_future_usage=off_session`You can retrieve the saved card details by listing the card payment methods associated with that customer.

### Compliance

You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For example, the European Data Protection Board has issued guidance regarding saving payment details. These requirements generally apply if you want to save your customer’s payment method for future use, such as presenting a customer’s payment method to them in the checkout flow for a future purchase or charging them when they’re not actively using your website or app.

Add terms to your website or app that state how you plan to save payment method details and allow customers to opt in. If you plan to charge the customer while they’re offline, then at a minimum, make sure that your terms also cover the following:

- The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for instance, whether charges are for scheduled installment or subscription payments, or for unscheduled top-ups).
- How the payment amount is determined.
- Your cancellation policy, if you’re setting up the payment method for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

When you save a payment method, it can only be used for the specific usage that you included in your terms. If you want to charge customers when they’re offline and also save the customer’s payment method to present to them as a saved payment method for future purchases, you must explicitly collect consent from the customer. One way to do so is with a “Save my payment method for future use” checkbox.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`