htmlMigrate to latest flexible payment scenarios | Stripe Documentation[Skip to content](#main-content)Migrate from beta[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fflexible-features-migration)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fflexible-features-migration)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)
[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[More payment scenarios](/docs/payments/more-payment-scenarios)[Flexible payment scenarios](/docs/payments/flexible-payments)# Migrate to latest flexible payment scenarios

Adapt your beta advanced payment scenarios to the general release.Stripe now supports several flexible payment scenarios for non-card-present transactions. If you’ve already integrated the private beta version of any of these features, this guide provides details to upgrade to the general release. For new integrations, use see the following guides for the features that interest you:

- [Increment an Authorization](/payments/incremental-authorization)
- [Capture more than the Authorized Amount](/payments/overcapture)
- [Place an Extended Hold on an Online Card Payment](/payments/extended-authorization)
- [Capture a Payment Multiple Times](/payments/multicapture)

We’ve incorporated the following feedback-driven improvements to these features:

- Detailed control over the features at the[PaymentIntent](/payments/payment-intents)level.
- Clearer expectations regarding feature availability and usage after a[confirmation](/api/payment_intents/confirm)phase.

Each of the flexible payment features has different requirements from its private beta integration. Choose the feature you need to upgrade and refer to the note at the top for changes and requirements specific to that feature.

Incremental authorizationOvercaptureExtended authorizationMulticaptureChanges from betaThe first step of this integration is now mandatory.

[Request incremental authorization](#request-incremental-auth)Your PaymentIntent must include a request for incremental authorization before confirmation.

WarningThis formerly optional step is now mandatory.

BeforeAfterCommand Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1000 \
  -d currency=usd \
  -d "payment_method_types[]"=card \
  -d payment_method=pm_card_debit_incrementalAuthAuthorized \
  -d confirm=true \
  -d capture_method=manual \
  -d "expand[]"=latest_charge \
  -d "payment_method_options[card][request_incremental_authorization_support]"=true`Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1000 \
  -d currency=usd \
  -d "payment_method_types[]"=card \
  -d payment_method=pm_card_debit_incrementalAuthAuthorized \
  -d confirm=true \
  -d capture_method=manual \
  -d "expand[]"=latest_charge \
  -d "payment_method_options[card][request_incremental_authorization]"=if_available`The response now returns the status of the incremental authorization request in the payment_method_details.card.incremental_authorization.status property of the latest_charge. The status values is available or unavailable depending on the customer’s payment method.

BeforeAfter`// PaymentIntent Response
{
  "id": "pi_ANipwO3zNfjeWODtRPIg",
  "object": "payment_intent",
  "amount": 1000,
  "amount_capturable": 1000,
  "amount_received": 0,
  ...
  // if latest_charge is expanded
  {
    "latest_charge": {
        "amount": 1000,
        "payment_method_details": {
          "card": {
            "incremental_authorization_supported": true // or false
          }
        }
        ...
      }
  }
}``// PaymentIntent Response
{
  "id": "pi_ANipwO3zNfjeWODtRPIg",
  "object": "payment_intent",
  "amount": 1000,
  "amount_capturable": 1000,
  "amount_received": 0,
  ...
  // if latest_charge is expanded
  {
    "latest_charge": {
        "amount": 1000,
        "payment_method_details": {
          "card": {
            "incremental_authorization": {
                "status": "available" // or "unavailable"
            }
          }
        }
        ...
      }
  }
}`[Incrementally modify the authorized amount](#use-incremental-auth)No changes have been made to this step in comparison to the beta version.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents/pi_ANipwO3zNfjeWODtRPIg/increment_authorization \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1500`## Choose how to capture more than initially authorized amount

Two of the flexible payment features allow you to capture an amount larger than initially authorized:

- Over capture up to a certain limit ([Capture more than the authorized amount on a payment](/payments/overcapture))
- Increment the existing authorization and then capture the newly authorized amount ([Increment an authorization](/payments/incremental-authorization))

The example below showcases how these features can complement each other in the generally available version.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1000 \
  -d currency=usd \
  -d "payment_method_types[]"=card \
  -d payment_method=pm_card_visa \
  -d confirm=true \
  -d capture_method=manual \
  -d "expand[]"=latest_charge \
  -d "payment_method_options[card][request_incremental_authorization]"=if_available \
  -d "payment_method_options[card][request_overcapture]"=if_available``// PaymentIntent Response
{
  "object": "payment_intent",
  "amount": 1000,
  ...
  // if latest_charge is expanded
  {
    "latest_charge": {
      "payment_method_details": {
        "card": {
          "incremental_authorization": {
              "status": "available" // or "unavailable"
          },
          "overcapture": {
              "status": "available", // or "unavailable"
              "maximum_capturable_amount": 1200
          }
        }
      }
      ...
    }
  }
}`Upon confirmation of the PaymentIntent, if both features are available, you have options on the next steps to capture a larger amount than initially authorized:

1. Overcapture if the desired amount is equal or below the`maximum_capturable_amount`.
2. Perform an incremental authorization to the desired amount, then capture.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Request incremental authorization](#request-incremental-auth)[Incrementally modify the authorized amount](#use-incremental-auth)[Choose how to capture more than initially authorized amount](#choose-how-to-capture-more-than-initially-authorized-amount)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`