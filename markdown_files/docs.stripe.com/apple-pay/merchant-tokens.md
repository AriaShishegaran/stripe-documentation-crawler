htmlApple Pay merchant tokens | Stripe Documentation[Skip to content](#main-content)Apple Pay merchant tokens[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fapple-pay%2Fmerchant-tokens)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fapple-pay%2Fmerchant-tokens)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Wallets](/docs/payments/wallets)[Apple Pay](/docs/apple-pay)# Apple Pay merchant tokens

Learn how to use Apple Pay merchant tokens for recurring, deferred, and automatic reload payments.An Apple Pay merchant token (MPAN) ties together a payment card, a business, and a customer, and enables the wallet holder to manage access to a card stored in their Apple wallet. Apple Pay’s latest guidelines recommend merchant tokens over device tokens (DPANs) because merchant tokens:

- Allow for continuity across multiple devices
- Enable recurring payments independent of a device
- Keep payment information active in a new device even when its removed from a lost or stolen device
- Come with lifecycle management features to monitor changes to a token or to see if a token has been revoked

## Merchant token types

You can use Apple Pay to request an MPAN in three ways. Each type of request has different parameters that affect how the user is presented with Apple Wallet. Almost all request types provide the option to supply a managementURL, which routes customers to a webpage to manage their payment methods. If you request an MPAN and the issuer supports MPAN generation, you receive an MPAN. Otherwise, you receive a DPAN.

MPAN request typeUse caseSupportRecurring[PKRecurringPaymentRequest](https://developer.apple.com/documentation/passkit/pkrecurringpaymentrequest)Issues an MPAN for use in a recurring payment such as a subscription.- [Apple Pay on the Web](https://developer.apple.com/documentation/apple_pay_on_the_web)
- iOS > v16.0

Automatic reload[PKAutomaticReloadPaymentRequest](https://developer.apple.com/documentation/passkit/pkautomaticreloadpaymentrequest)Issues an MPAN for use in a store card top-up or prepaid account. Supported parameters:- `automaticReloadBilling`shows billing details when you present Apple Pay.

- [Apple Pay on the Web](https://developer.apple.com/documentation/apple_pay_on_the_web)
- iOS > v16.0

Deferred payment[PKDeferredPaymentRequest](https://developer.apple.com/documentation/passkit/pkdeferredpaymentrequest)Issues an MPAN for use in reservations such as hotels. Supported parameters:- `freeCancellationDate`shows the cancellation deadline when you present Apple Pay.
- `billingAgreement`shows the terms of service when you present Apple Pay.

- [Apple Pay on the Web](https://developer.apple.com/documentation/apple_pay_on_the_web)
- Xcode 14.3
- iOS > v16.4

## Add Apple Pay merchant tokens

You can add a merchant token when presenting Apple Pay in the Express Checkout Element, web Payment Element, and mobile Payment Element. Stripe automatically handles merchant token requests in Stripe Checkout integrations.

Express Checkout ElementWeb Payment ElementMobile Payment Element### Using the Payment Request Button?

If you’re using the Payment Request Button for recurring payments, we recommend migrating to the Express Checkout Element for improved functionality and payment method support. See a comparison.

1. Set up[Express Checkout Element integration](/elements/express-checkout-element/accept-a-payment).
2. Implement an event handler for the`click`event on the Express Checkout Element.
3. Pass the`applePay`object relevant to your MPAN use case (choose from the drop-down to see use case code samples).
4. Include relevant parameters for your use case.

MPAN use case:Recurring paymentsAutomatic reloadDeferred paymentcheckout.js`expressCheckoutElement.on("click", (e) => {
  const options = {
    applePay: {
      recurringPaymentRequest: {
        paymentDescription: "Standard Subscription",
        regularBilling: {
          amount: 1000,
          label: "Standard Package",
          recurringPaymentStartDate: new Date("2023-03-31"),
          recurringPaymentEndDate: new Date("2024-03-31"),
          recurringPaymentIntervalUnit: "year",
          recurringPaymentIntervalCount: 1,
        },
        billingAgreement: "billing agreement",
        managementURL: "https://stripe.com",
      },
    },
  };
  e.resolve(options);
});`## Merchant token auth rate monitoring

For Sigma users, the charges table contains a card_token_type enum field to indicate the charge is using an mpan or dpan card. The following Sigma query example calculates the MPAN auth rate:

`-- deduplicated MPAN auth rate
select
  100.0 * count(
    case
      when charge_outcome in ('authorized', 'manual_review') then 1
    end
  ) / count(*) as deduplicated_auth_rate_pct,
  count(*) as n_attempts
from
  authentication_report_attempts a
  join charges c on c.id = a.charge_id
where
  c.created >= date('2021-01-01')
  and c.card_tokenization_method = 'apple_pay'
  -- The new field added to charges table.
  and c.card_token_type = 'mpan'
  -- deduplicate multiple manual retries to a single representative charge
  and is_final_attempt`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Merchant token types](#merchant-token-types)[Add Apple Pay merchant tokens](#add-apple-pay-merchant-tokens)[Merchant token auth rate monitoring](#merchant-token-auth-rate-monitoring)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`