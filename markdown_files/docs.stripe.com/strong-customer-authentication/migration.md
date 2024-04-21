htmlUpdate your integration for SCA | Stripe Documentation[Skip to content](#main-content)Update your integration[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstrong-customer-authentication%2Fmigration)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstrong-customer-authentication%2Fmigration)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)
[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)Regulation support[SCA readiness](/docs/strong-customer-authentication)# Update your integration for SCA

Learn how to update your integration to avoid declined payments due to Strong Customer Authentication (SCA).Updating your integration to support Strong Customer Authentication consists of the following steps:

1. Identify your payment flow
2. Determine your integration path
3. Implement the new integration path
4. Test dynamic authentication

Start updating your integration today. After your integration is live, 3D Secure authentication is displayed when required by SCA.

## 1. Identify your payment flow

First, identify the payment flow that most closely matches your business. Read more about various flows to design a payment flow for SCA.

Payment flowDescriptionExample Business ScenarioOne-time paymentsYou charge the customer’s cards immediately after they confirm payment.[E-commerce](https://stripe.com/guides/sca-payment-flows#e-commerce)Recurring paymentsYou charge the customer on a recurring basis.[Gym membership](https://stripe.com/guides/sca-payment-flows#gym-membership)for fixed-amount recurring charges, or[utility bill](https://stripe.com/guides/sca-payment-flows#utility-bill)for metered billingPayments with[separate authorize and capture](/payments/place-a-hold-on-a-payment-method)within 7 days.You separately authorize and capture card payments within 7 days after the customer confirms payment.[Ridesharing](https://stripe.com/guides/sca-payment-flows#ridesharing)Payment captured more than seven days after authorization.You charge the customer’s card more than 7 days after they submit payment details.[Crowdfunding](https://stripe.com/guides/sca-payment-flows#crowdfunding), or[car rental](https://stripe.com/guides/sca-payment-flows#car-rental)if final amount may change.Other off-session paymentsYou save the customer’s cards and charge some time later when the customer is not available to complete authentication.N/A## 2. Determine your integration path

Choose an integration option based on your payment flow below:

[One-time payments](#one-time)For one-time payments, you can complete the full integration today.

### Stripe Checkout

Get prebuilt, conversion-optimized checkout flows with minimal code. Choose this option if you prefer a low-maintenance integration. For this payment flow, you can complete the full integration, and handling exemptions doesn’t require any additional work.

- See[how to integrate Stripe Checkout](/payments/accept-a-payment?integration=checkout)to learn more.

### Payment Intents API

Build dynamic payment flows and custom checkout pages by migrating to the Payment Intents API with one of our client libraries:

- [Stripe.js & Elements](/payments/payment-intents/migration)
- [Stripe iOS SDK](/payments/accept-a-payment?platform=ios#setup-client-side)
- [Stripe Android SDK](/payments/accept-a-payment?platform=android#setup-client-side)

For this payment flow, you can complete the full integration, and handling exemptions requires no additional work.

- See[how to use the Payment Intents API](/payments/payment-intents)to learn more.

[Recurring payments](#recurring)SCA requires customers to complete 3D Secure for some payments. When this step is required by the bank, the customer must be online to complete authentication. ​​This introduces complexity for businesses that save cards and charge them later when the customer is no longer on the website or application and can’t complete authentication. This is also known as off-session payments. Examples of this include fixed-amount subscriptions, metered-billing subscriptions, crowdfunding campaigns, and car rentals.

Stripe products and APIs now allow merchants to meet SCA requirements for off-session payments:

1. Mandate collection. A mandate represents the agreement you have with the customer on how you plan to use their card in the future. In your checkout flow, add some consent text. State that by completing checkout, the customer consents to your initiation of payment on their behalf. State the anticipated frequency of payments. Explain how the amount of the payments will be determined.


2. Strong authentication of the first transaction. Merchants are required to authenticate the customer when the mandate is set up. This can either be done by the first payment with the card or when saving the card to a customer without making an initial payment.


3. Flagging subsequent transactions. Any payment made with a saved card when a user is off-session must be marked accordingly, with reference to the first authenticated transaction. Stripe handles this for you.



By updating your payments integration to use these new APIs and flows, Stripe can request exemptions such as fixed-amount subscriptions and merchant-initiated transactions to process later payments made with a saved card. However, banks can decide to reject a request for exemption. Build a way to notify customers that they need to return to your application and complete authentication if required.

### Stripe Billing with the new version of Checkout

Checkout is a prebuilt checkout page that lets you collect payments and manage simple subscriptions with a single integration.

- See[how to build subscriptions](/billing/subscriptions/build-subscriptions)to learn more.

### Stripe Billing

Take advantage of automated tools to protect your revenue and scale your business. Build your own custom checkout experience.

1. Update your client-side integration to[save and reuse cards](/payments/save-and-reuse).
2. Then,[implement SCA-changes for Stripe Billing](/billing/migration/strong-customer-authentication).

### Off-Session Payments with the Payment Intents API

Build your own off-session payments logic and handle getting users back on-session to complete re-authentication as needed. While this approach takes more work than using Stripe Billing, it provides more flexibility.

There are three parts to building an off-session payment flow:

1. Save a card to a customer.You can save a card to a customer[in a checkout flow](/payments/save-during-payment)(as the customeris making a payment) with the Payment Intents API, or[outside of the checkout flow](/payments/save-and-reuse)with the Setup IntentsAPI.  You can also use Stripe Checkout to save cards to a customer[in a checkout flow](/payments/checkout/customization)or[outside of the checkout flow](/payments/save-and-reuse?platform=checkout).
2. Use a saved card to make a payment.Once you have cards saved to acustomer, you can make both on-session or[off-session payments](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method).
3. Build a recovery flow.While Stripe requests exemptions to reduce theneed for customer reauthentication, there is always a risk that the cardholder’sbank will reject the exemption request. You should always build a[recovery flow](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)to bring a customer backon-session in case they need to authenticate again.

[Payments with separate authorize and capture within 7 days](#separate-auth-capture)For payments with separate authorize and capture, you can complete the full integration today.

### The new version of Stripe Checkout

Get prebuilt, conversion-optimized checkout flows with minimal code. Choose this option if you prefer a low-maintenance integration. For this payment flow, you can complete the full integration today, and no additional work will be needed to handle exemptions.Use Stripe Checkout with separate auth and capture

Use Stripe Checkout with separate auth and capture

### Payment Intents API

Build dynamic payment flows and custom checkout pages by migrating to the Payment Intents API with one of our client libraries:

- [Stripe.js & Elements](/payments/payment-intents/migration)
- [Stripe iOS SDK](/payments/accept-a-payment?platform=ios#setup-client-side)
- [Stripe Android SDK](/payments/accept-a-payment?platform=android#setup-client-side)

For this payment flow, you can complete the full integration, and handling exemptions requires no additional work.

- See[how to use the Payment Intents API](/payments/payment-intents)to learn more.

[Payment captured more than seven days after authorization](#deferred-auth)SCA requires customers to complete 3D Secure for some payments. When this step is required by the bank, the customer must be online to complete authentication. ​​This introduces complexity for businesses that save cards and charge them later when the customer is no longer on the website or application and can’t complete authentication. This is also known as off-session payments. Examples of this include fixed-amount subscriptions, metered-billing subscriptions, crowdfunding campaigns, and car rentals.

Stripe products and APIs now allow merchants to meet SCA requirements for off-session payments:

1. Mandate collection. A mandate represents the agreement you have with the customer on how you plan to use their card in the future. In your checkout flow, add some consent text. State that by completing checkout, the customer consents to your initiation of payment on their behalf. State the anticipated frequency of payments. Explain how the amount of the payments will be determined.


2. Strong authentication of the first transaction. Merchants are required to authenticate the customer when the mandate is set up. This can either be done by the first payment with the card or when saving the card to a customer without making an initial payment.


3. Flagging subsequent transactions. Any payment made with a saved card when a user is off-session must be marked accordingly, with reference to the first authenticated transaction. Stripe handles this for you.



By updating your payments integration to use these new APIs and flows, Stripe can request exemptions such as fixed-amount subscriptions and merchant-initiated transactions to process later payments made with a saved card. However, banks can decide to reject a request for exemption. Build a way to notify customers that they need to return to your application and complete authentication if required.

### Off-Session Payments with the Payment Intents API

Build your own off-session payments logic and handle getting users back on-session to complete re-authentication as needed. While this approach takes more work than using Stripe Billing, it provides more flexibility.

There are three parts to building an off-session payment flow:

1. Save a card to a customer.You can save a card to a customer[in a checkout flow](/payments/save-during-payment)(as the customeris making a payment) with the Payment Intents API, or[outside of the checkout flow](/payments/save-and-reuse)with the Setup IntentsAPI.  You can also use Stripe Checkout to save cards to a customer[in a checkout flow](/payments/checkout/customization)or[outside of the checkout flow](/payments/save-and-reuse?platform=checkout).
2. Use a saved card to make a payment.Once you have cards saved to acustomer, you can make both on-session or[off-session payments](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method).
3. Build a recovery flow.While Stripe requests exemptions to reduce theneed for customer reauthentication, there is always a risk that the cardholder’sbank will reject the exemption request. You should always build a[recovery flow](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)to bring a customer backon-session in case they need to authenticate again.

[Other off-session payments](#other-off-session)SCA requires customers to complete 3D Secure for some payments. When this step is required by the bank, the customer must be online to complete authentication. ​​This introduces complexity for businesses that save cards and charge them later when the customer is no longer on the website or application and can’t complete authentication. This is also known as off-session payments. Examples of this include fixed-amount subscriptions, metered-billing subscriptions, crowdfunding campaigns, and car rentals.

Stripe products and APIs now allow merchants to meet SCA requirements for off-session payments:

1. Mandate collection. A mandate represents the agreement you have with the customer on how you plan to use their card in the future. In your checkout flow, add some consent text. State that by completing checkout, the customer consents to your initiation of payment on their behalf. State the anticipated frequency of payments. Explain how the amount of the payments will be determined.


2. Strong authentication of the first transaction. Merchants are required to authenticate the customer when the mandate is set up. This can either be done by the first payment with the card or when saving the card to a customer without making an initial payment.


3. Flagging subsequent transactions. Any payment made with a saved card when a user is off-session must be marked accordingly, with reference to the first authenticated transaction. Stripe handles this for you.



By updating your payments integration to use these new APIs and flows, Stripe can request exemptions such as fixed-amount subscriptions and merchant-initiated transactions to process later payments made with a saved card. However, banks can decide to reject a request for exemption. Build a way to notify customers that they need to return to your application and complete authentication if required.

### Off-Session Payments with the Payment Intents API

Build your own off-session payments logic and handle getting users back on-session to complete re-authentication as needed. While this approach takes more work than using Stripe Billing, it provides more flexibility.

There are three parts to building an off-session payment flow:

1. Save a card to a customer.You can save a card to a customer[in a checkout flow](/payments/save-during-payment)(as the customeris making a payment) with the Payment Intents API, or[outside of the checkout flow](/payments/save-and-reuse)with the Setup IntentsAPI.  You can also use Stripe Checkout to save cards to a customer[in a checkout flow](/payments/checkout/customization)or[outside of the checkout flow](/payments/save-and-reuse?platform=checkout).
2. Use a saved card to make a payment.Once you have cards saved to acustomer, you can make both on-session or[off-session payments](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method).
3. Build a recovery flow.While Stripe requests exemptions to reduce theneed for customer reauthentication, there is always a risk that the cardholder’sbank will reject the exemption request. You should always build a[recovery flow](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)to bring a customer backon-session in case they need to authenticate again.

NoteIf you don’t use Stripe.js, the legacy version of Checkout, or our mobile SDKs to collect payment details, contact support or connect with our sales team.

## 3. Implement the new integration path

You need to make server-side and client-side changes.

### Server-side

Use the Payment Intents API to create a payment. A PaymentIntent tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by SCA.

Follow the migration guide to learn how to migrate from the Charges API to the Payment Intents API.

### Client-side

In order to dynamically display 3D Secure authentication for card payments, client-side changes are also required alongside server-side changes for the Payment Intents API.

Follow the guides to learn how to use the Payment Intents API with Stripe.js & Elements, iOS, and Android.

### Using Stripe Checkout

Follow the guides to integrate Checkout for one-time and subscriptions.

## 4. Test dynamic authentication

To verify that your updated integration handles 3D Secure correctly, be sure to test both successful and unsuccessful authentication flows, using the regulatory test cards.

By default, 3D Secure authentication is only shown when the customer’s bank requires it, so your checkout conversion isn’t negatively affected. As of September 14, 2019, your updated integration displays the 3D Secure authentication flow automatically whenever required by SCA.

## See also

- [Stripe Checkout Overview](/payments/checkout)
- [Payment Intents Overview](/payments/payment-intents)
- [Payment Intents Migration Guide](/payments/payment-intents/migration)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[1. Identify your payment flow](#step-1)[2. Determine your integration path](#step-2)[One-time payments](#one-time)[Recurring payments](#recurring)[Payments with separate authorize and capture within 7 days](#separate-auth-capture)[Payment captured more than seven days after authorization](#deferred-auth)[Other off-session payments](#other-off-session)[3. Implement the new integration path](#step-3)[4. Test dynamic authentication](#step-4)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`