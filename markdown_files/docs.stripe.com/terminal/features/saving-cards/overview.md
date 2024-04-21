htmlSave cards for online payments | Stripe Documentation[Skip to content](#main-content)Save cards for future use[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Fsaving-cards%2Foverview)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Fsaving-cards%2Foverview)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)# Save cards for online payments

Use your Stripe Terminal integration to collect card details for online reuse.Stripe Terminal lets you save payment methods (excluding mobile wallets) for online reuse. Use an in-person card to initiate an online subscription using Billing, save payment details to a customer’s online account, or defer payment.

## Save a card

You can collect reusable card details with Terminal:

- [Directly, without charging the card](/terminal/features/saving-cards/save-cards-directly)
- [After payment](/terminal/features/saving-cards/save-after-payment)US only

[Charge a saved card](#charging-saved-card)You can use previously saved card details to charge customers later.

For one-time use, create a PaymentIntent and attach the saved payment method. You can’t reuse an attached payment method unless you collect payment details again by saving a card from a PaymentIntent.

If the customer isn’t in your checkout flow when you charge the customer, set off_session to true. This causes the PaymentIntent to throw an error if customer authentication is required.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "payment_method_types[]"="card" \
  -d "amount"=1099 \
  -d "currency"="" \
  -d "customer"="{{CUSTOMER_ID}}" \
  -d "payment_method"="{{PAYMENT_METHOD_ID}}"`NoteWhen charging a saved card, you can’t use the confirmPaymentIntent method. Payments with generated cards are online payments and can’t be processed with Terminal SDK methods.

[Track customer behavior with card fingerprints](#fingerprints)Use the Stripe API to recognize repeat customers across online and retail channels by correlating transactions by the same card. Like card payment methods, each card_present payment method has a fingerprint attribute that uniquely identifies a particular card number. Cards from mobile wallets (for example, Apple Pay or Google Pay) don’t share a fingerprint with cards used online.

Starting with API version 2018-01-23, Connect platforms see a fingerprint on card_present and card PaymentMethods that’s uniform across all connected accounts. You can use this fingerprint to look up charges across your platform from a particular card.

[Compliance](#compliance)You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For example, the European Data Protection Board has issued guidance regarding saving payment details. These requirements generally apply if you want to save your customer’s payment method for future use, such as presenting a customer’s payment method to them in the checkout flow for a future purchase or charging them when they’re not actively using your website or app.

Add terms to your website or app that state how you plan to save payment method details and allow customers to opt in. If you plan to charge the customer while they’re offline, then at a minimum, make sure that your terms also cover the following:

- The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for instance, whether charges are for scheduled installment or subscription payments, or for unscheduled top-ups).
- How the payment amount is determined.
- Your cancellation policy, if you’re setting up the payment method for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

When you save a payment method, it can only be used for the specific usage that you included in your terms. If you want to charge customers when they’re offline and also save the customer’s payment method to present to them as a saved payment method for future purchases, you must explicitly collect consent from the customer. One way to do so is with a “Save my payment method for future use” checkbox.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Save a card](#save-a-card)[Charge a saved card](#charging-saved-card)[Track customer behavior with card fingerprints](#fingerprints)[Compliance](#compliance)Products Used[Terminal](/terminal)[Payments](/payments)[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`