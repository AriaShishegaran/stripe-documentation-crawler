# Accept installment card payments in Mexico

Installments (meses sin intereses) are a type of credit card payment in Mexico that allows customers to split purchases over multiple billing statements. You receive the full amount (minus a fee) as if it were a normal charge, and the customer’s bank handles collecting the money over time.

Stripe supports installment payments for Stripe Mexico accounts using the Payment Intents and Payment Methods APIs, Checkout, Invoicing, Payment Element, and Payment Links.

Get started with accepting installments.

[installments](/payments/meses-sin-intereses/accept-a-payment)

## Connect compatibility

You can use Stripe Connect with installments to process payments on behalf of connected accounts. As a platform, you can set the default installment configuration for your connected accounts in Mexico. Standard connected accounts can override these settings in the Dashboard.

[Stripe Connect](/connect/overview)

## Connectors and plugins

A variety of connectors and plugins that integrate with Stripe also support installments. These connectors provide no-code and low-code solutions for accepting a wide range of local payment methods using Stripe, including installments.

For example, the latest version of the Stripe Connector for Adobe Commerce has built-in support for accepting payments with installments. For information regarding setup instructions and features for specific plugins, contact the plugin developers directly.

[latest version of the Stripe Connector for Adobe Commerce](/connectors/adobe-commerce/install#upgrade)

If you use a plugin that doesn’t yet support installments, you can contact our support team to let us know, and we’ll do our best to see if we can enable installments for that plugin.

[contact our support team](https://support.stripe.com/)

## Fees

When you accept a payment with installments, an additional fee is added to the standard credit card transaction fee. The fee varies according to the number of installments, or months, applied to the transaction.

## Requirements

There are restrictions on which transactions and cards can use meses sin intereses. You don’t need to implement these rules yourself. Stripe automatically determines meses sin intereses eligibility after you set up the payment method.

- Stripe only supports installments for Stripe Mexico accounts.

- The payment method must be a credit card issued in Mexico.

- The card must be a consumer card–installments don’t support corporate cards.

- The card must be issued by one of our supported issuers.

[supported issuers](/payments/mx-installments#supported-cards)

- The currency value must be MXN (pesos).

- The total payment amount must be above a minimum transaction amount. Stripe provides a minimum transaction amount based on the number of months in the plan selected. You can specify which installment plans you want to enable and define your own custom minimum and maximum transaction amounts by configuring custom installment settings in the Dashboard.

[minimum transaction amount](/payments/mx-installments#fees)

[configuring custom installment settings](/payments/meses-sin-intereses/accept-a-payment#custom-settings)

## Supported cards

You can accept payments in Installments on cards from the following issuers:

- Afirme

- American Express

- BanBajío

- Banjercito

- BBVA

- Banca Mifel

- Banco Azteca

- Banco Famsa

- Banco Invex

- Banco Multiva

- Banorte

- Banregio

- Citibanamex (3-, 6-, 9-, and 12-month plans only)

- Falabella

- Hey Banco

- HSBC

- Inbursa

- Konfio

- Liverpool

- NanoPay

- Nubank

- RappiCard

- Santander

- Scotiabank
