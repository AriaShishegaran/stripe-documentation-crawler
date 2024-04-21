htmleftpos Australia | Stripe Documentation[Skip to content](#main-content)eftpos Australia[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Feftpos-australia)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Feftpos-australia)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Cards](/docs/payments/cards)# eftpos Australia

Learn about eftpos Australia, a common payment method in Australia.Customer geography: Australia

Payment method type: Debit, and prepaid card

Presentment currency: AUD

Disputes: Yes

Refunds and partial refunds: Yes

Recurring payments: Yes

Eftpos is Australia’s local debit card network. More than 90% of eftpos cards are co-branded with either Visa or Mastercard, meaning you can process these cards over either network supported by the card.

Stripe processes co-branded eftpos cards over eftpos, plus either Visa or Mastercard, in accordance with least cost routing requirements and depending on the type of transaction.

NoteEftpos-only cards (also known as “proprietary eftpos cards”) only support in-person payments and can’t be used for online transactions.

## Availability

Eftpos is available to any business that uses Stripe in Australia, with the following exceptions:

- Massage parlors ([MCC](/connect/setting-mcc)7297)
- Financial institutions—manual cash disbursements ([MCC](/connect/setting-mcc)6010)
- Financial institutions—merchandise and services ([MCC](/connect/setting-mcc)6012)
- Non-financial institutions—foreign currency, money orders and travelers’ checks. ([MCC](/connect/setting-mcc)6051)
- Remote stored value load—merchant ([MCC](/connect/setting-mcc)6530)
- Stored value card purchase/load ([MCC](/connect/setting-mcc)6540)
- Wires, money orders ([MCC](/connect/setting-mcc)4829)

## Integration

If your integration can already accept card payments, you can also accept eftpos without additional updates.

Eftpos is the default network for payment. Unless you change the default network, you must inform your customers that whenever they use a dual-network debit card, their payments might be processed through the debit network, regardless of the logo that appears when they enter their payment information.

We recommend you notify your customers based on the type of payment transaction:

- For single payment transactions, display a notification to the customer before the completion of the checkout process.
- For new recurring payment transactions, display a notification to the customer at the time of setup.
- For existing recurring payment transactions, notify your customers in advance of future transactions.

You must notify your customers about how network routing functions, and how payments processing works. You can use the suggested notification message below:

NoteNotwithstanding the payment brand logo displayed when you enter your payment information, whenever you use a dual-network debit card displaying eftpos and another payment brand, your payment (including any future recurring debit payments authorized by you) might be processed through either network. See the [Terms and Conditions] or [FAQs] for more information.

We recommend that you provide further information in your Terms and Conditions or FAQs on how network routing functions and how payments processing works. For guidelines on best practices, see the Australian Payments Network MCR Online Notification Guidelines.

## Understand which network processes payments

Stripe dynamically routes between the international scheme (Visa or Mastercard) and eftpos, depending on the type of payment, technical availability and authorization rate considerations:

- If a payment requires[placing a hold on the card](/payments/place-a-hold-on-a-payment-method)(in other words, if there’s a delay between authorization and capture), or if it requires[3D Secure](/payments/3d-secure), Stripe always routes to the international scheme.
- For other types of payments, Stripe generally defaults to the eftpos network.

If you require that eftpos is never the default network for any payments, please contact support.

To identify which network a payment was processed on, inspect the network field on the Charge object associated with a successful Payment Intent:

`{
  "id": "ch_1Ff52K2eZvKYlo2CWe10i0s7",
  "object": "charge",
  ...
  "payment_method_details": {
    "card": {
      "brand": "visa",
      ...
      "network": "eftpos_au"
    },
    "type": "card"
  }
}`## See also

- [Migrating from Charges API to the Payment Intents API](/payments/payment-intents/migration)
- [Available eftpos test cards](/testing#cards)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Availability](#availability)[Integration](#integration-requirements)[Understand which network processes payments](#identify-which-network-a-payment-was-processed-on)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`