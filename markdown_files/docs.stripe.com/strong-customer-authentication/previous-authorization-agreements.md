htmlPrevious authorization agreements | Stripe Documentation[Skip to content](#main-content)Previous authorization agreements[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstrong-customer-authentication%2Fprevious-authorization-agreements)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstrong-customer-authentication%2Fprevious-authorization-agreements)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)
[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)Regulation support[SCA readiness](/docs/strong-customer-authentication)# Previous authorization agreements

Learn which payments previous authorization agreements can be used for (sometimes referred to as grandfathering).WarningIf you’re affected by SCA, update your Stripe integration now, even if some of your payments can use previous authorization agreements. Stripe provides migration guides to help.

## Eligibility

Strong Customer Authentication requires an additional step of customer authentication, but sometimes you collect payments when your customer isn’t actively using your application. Even if they authenticated in the past, SCA may require your customer to come back online and re-authenticate. To reduce friction in these off-session payments, Stripe APIs enable upfront authentication—so you can authenticate your customer on-session once and reuse the card off-session repeatedly. As of September 14, 2019, you need to use these APIs to reduce the chance of failed payments when reusing cards or creating subscriptions and invoices.

However, you can use previous authorization agreements for off-session payments that meet the following criteria:

- Cards from EU customers saved before December 31, 2020
- Cards from UK customers saved before September 14, 2021

This means you don’t have to use Stripe’s new APIs to set up saved cards again, and your off-session payments can proceed normally—without re-authentication from customers.

## How it works

You can use previous authorization agreements for all off-session payments that meet both of these conditions, regardless of payment amount and frequency:

- You saved the card details before the[eligibility](#eligibility)cutoff
- You explicitly tell Stripe the transaction is off-session

Stripe automatically looks for a transaction made with the card prior to the eligibility cutoff. If found, Stripe uses the previous authorization agreement for the current transaction. If the bank accepts the previous authorization agreement, the transaction is categorized as out of scope for SCA and can proceed without additional authentication.

If the bank declines the previous authorization agreement, it’s like any other PaymentIntent failing the confirmation step. The PaymentIntent’s status changes to requires_payment_method, and you have to notify your customer to complete the payment.

## Saving cards after the eligibility period

Now that SCA has taken effect, save and reuse cards with the Payment Intents and Setup Intents APIs to qualify for off-session exemptions. You can also save cards using Stripe Checkout.

## Preparing your saved cards for SCA

For Stripe to reuse authorization agreements, you need to use PaymentIntents and tell Stripe the payment is off-session.

How you saved the card before the eligibility cutoffWhat to do after the eligibility periodBy passing a[token](/saving-cards),[source](/sources/cards), or[payment method](/payments/save-during-payment)to the`Customer`Create a PaymentIntent with[off-session flag](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)By creating a[SetupIntent](/payments/save-and-reuse)or using[setup_future_usage](/api/payment_intents/create#create_payment_intent-setup_future_usage)in a PaymentIntentCreate a PaymentIntent with[off-session flag](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)For subscriptions and invoices managed with Stripe Billing, refer to the Billing SCA guide.

## See also

- [Payment Intents Overview](/payments/payment-intents)
- [Payment Intents Migration Guide](/payments/payment-intents/migration)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Eligibility](#eligibility)[How it works](#how-it-works)[Saving cards after the eligibility period](#after-sca)[Preparing your saved cards for SCA](#preparing)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`