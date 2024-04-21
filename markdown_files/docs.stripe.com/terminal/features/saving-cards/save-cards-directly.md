htmlSave directly without charging | Stripe Documentation[Skip to content](#main-content)Save directly without charging[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Fsaving-cards%2Fsave-cards-directly)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Fsaving-cards%2Fsave-cards-directly)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)[Save cards for future use](/docs/terminal/features/saving-cards/overview)# Save directly without charging

Save card details for online reuse from an in-person transaction.Server-drivenJavaScriptiOSAndroidReact NativeUse SetupIntents to collect card details without charging the card. Saving cards with Stripe Terminal using SetupIntents requires you to:

1. Create or retrieve a[Customer](/api/customers)object.
2. Create a[SetupIntent](/api/setup_intents)object to track the process.
3. Collect a payment method after collecting the customer’s consent.
4. Submit the payment method details to Stripe.

## Availability

You can use SetupIntents to collect card details on Visa, Mastercard, American Express, Discover, and co-branded eftpos cards. Interac cards, single-branded eftpos cards, and mobile wallets (for example, Apple Pay or Google Pay) aren’t supported.

NoteThe server-driven-based SetupIntents API is compatible with BBPOS WisePOS E and Stripe Reader S700.

[Create or retrieve a customer](#create-customer)To charge a card saved with Stripe, you must attach it to a Customer.

When you include a customer in your SetupIntent before confirming, Stripe automatically attaches the generated card payment method to the Customer object you provide.

Include the following code on your server to create a new Customer.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`[Create a SetupIntent](#create-setupintent)NoteWe recommend providing a customer ID while creating a SetupIntent—doing so attaches the card payment method to the Customer upon successful setup. If you don’t provide a customer ID, you must attach the payment method in a separate call.

A SetupIntent is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this setup process. For Terminal, this includes collecting and recording cardholder consent.

### API Reference

- [Create a SetupIntent](/api/setup_intents/create)

You must create the SetupIntent on your server and include card_present on the payment_method_types parameter.

The SetupIntent contains a client secret, which is a key that’s unique to the individual SetupIntent. You must obtain the client secret from the SetupIntent on your server and pass it to the client side.

[Ruby](#)`post '/create_setup_intent' do
  intent = # ... Create or retrieve the SetupIntent
  {id: intent.id, client_secret: intent.client_secret}.to_json
end`[Collect a payment method for saving cards](#collect-payment-method)### API Reference

- [process_setup_intent](/api/terminal/readers/process_setup_intent)

After you create a SetupIntent, you need to collect a payment method with the SDK and collect customer consent. If the customer provides the required form of agreement or consent, set the  customer_consent_collected  boolean to true.

NoteCollect customer consent verbally or with a checkbox in your application. You must comply with all applicable laws, rules, and regulations in your region.

You must call the process_setup_intent endpoint, which handles both collecting and confirming the SetupIntent. If the customer provides consent, set the customer_consent_collected boolean to true.

Command Line[curl](#)`curl https://api.stripe.com/v1/terminal/readers/{{READER_ID}}/process_setup_intent \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d setup_intent={{SETUP_INTENT_ID}} \
  -d customer_consent_collected=true`This method collects encrypted payment method data using the connected card reader, and associates the encrypted data with the SetupIntent.

### API Reference

- [cancel_action](/api/terminal/readers/cancel_action)

### Cancel collection

Programmatic cancellation![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You can cancel collecting a payment method by calling cancel_action.

CautionCollecting a payment method happens locally and requires no authorization or updates to the SetupIntent object until the next step.

[Submit the payment method details to Stripe](#submit-payment-method)Your previous call to process_setup_intent handles the confirm for you, so no further action is necessary.

A successful setup returns a succeeded value for the SetupIntent’s status property, along with a generated_card, which is a reusable card payment method you can use for online payments.

NoteThe setup_intent.payment_method is a card_present PaymentMethod that represents the tokenization of the card in-store and isn’t chargeable online.

The generated_card payment method automatically attaches to the customer you provided during SetupIntent creation. You can retrieve the generated_card payment method by expanding the SetupIntent’s latest_attempt property.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/setup_intents/{{SETUP_INTENT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "expand[]"=latest_attempt`Alternatively, you can retrieve the attached payment method by fetching the list of payment methods that gets attached to the customer.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/customers/{{CUSTOMER_ID}}/payment_methods \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d type=card`If you didn’t provide a customer during SetupIntent creation, you can attach the generated_card to a Customer object in a separate call.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_methods/{{PAYMENT_METHOD_ID}}/attach \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}}`If the setup isn’t successful, inspect the returned error to determine the cause. For example, failing to collect and notify Stripe of customer consent results in an error.

## Compliance

You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For example, the European Data Protection Board has issued guidance regarding saving payment details. These requirements generally apply if you want to save your customer’s payment method for future use, such as presenting a customer’s payment method to them in the checkout flow for a future purchase or charging them when they’re not actively using your website or app.

Add terms to your website or app that state how you plan to save payment method details and allow customers to opt in. If you plan to charge the customer while they’re offline, then at a minimum, make sure that your terms also cover the following:

- The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for instance, whether charges are for scheduled installment or subscription payments, or for unscheduled top-ups).
- How the payment amount is determined.
- Your cancellation policy, if you’re setting up the payment method for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

When you save a payment method, it can only be used for the specific usage that you included in your terms. If you want to charge customers when they’re offline and also save the customer’s payment method to present to them as a saved payment method for future purchases, you must explicitly collect consent from the customer. One way to do so is with a “Save my payment method for future use” checkbox.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Availability](#availability)[Create or retrieve a customer](#create-customer)[Create a SetupIntent](#create-setupintent)[Collect a payment method for saving cards](#collect-payment-method)[Submit the payment method details to Stripe](#submit-payment-method)[Compliance](#compliance)Products Used[Terminal](/terminal)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`