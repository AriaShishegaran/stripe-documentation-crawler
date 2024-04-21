htmlPayment Element and Card Element comparison | Stripe Documentation[Skip to content](#main-content)Card Element comparison[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-card-element-comparison)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-card-element-comparison)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)
[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Elements](/payments/elements)·[Home](/docs)[Payments](/docs/payments)[Web Elements](/docs/payments/elements)[Payment Element](/docs/payments/payment-element)# Payment Element and Card Element comparison

Learn more about the Payment Element and Card Element so you can decide which to use in your integration.Previously, each payment method (cards, iDEAL, etc.) required integrating a separate Element. Now, you can use the Payment Element to accept payments from one or multiple payment methods. Since this also includes cards, you have the option to integrate the Card Element or the Payment Element to accept card payments.

For most users, the Payment Element is the best option to process cards. The integration effort is the same as the Card Element and it supports all the common payment flows. It also gives you instant access to additional payment methods, including Google Pay and Apple Pay. Accepting more payment methods can help your business expand its global reach and improve checkout conversion.

If you’re already using the Card Element and want to migrate to the Payment Element, follow our migration guide.

NoteYou can have a single line Card Element or use split Elements, such as Card Number, Expiry, and CVC. When referring to the Card Element, the information below applies to both styles.

FeaturesPayment ElementCard ElementAccepts card paymentsAccepts card payments using Wallets (e.g., Apple Pay, Google Pay)Accepts payments with other payment methodsEnables faster checkout with[Link](/payments/link)Customizable look and feelHandles all[Stripe supported card brands](/payments/cards#supported-card-brands)Handles[3D Secure authentication](/payments/3d-secure)Input style*SplitSplit and single-line* Using split input fields is more accessible than using a single line input

## Advanced scenarios

Advanced scenariosPayment ElementCard Element[Set up future payments](/payments/save-and-reuse)[Save payment details during payment](/payments/save-during-payment)Updating a customer’s saved payment details[Place a hold on a payment method](/payments/place-a-hold-on-a-payment-method)[Credit card installments](/payments/mx-installments)Charge a different[application fee amount](/api/payment_intents/object#payment_intent_object-application_fee_amount)based on the card brand, country, or payment methodCharging differently based on payment method selectedDisplaying a review page after collecting payment details[Brand choice for cobranded cards](/co-badged-cards-compliance)Collecting card information so that you can run a validation for verification purposesIf you want to use the Card Element, see our guide on accepting a payment.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`