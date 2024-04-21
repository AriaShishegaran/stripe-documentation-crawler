htmlPayments using the Mirakl connector | Stripe Documentation[Skip to content](#main-content)Payments[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fmirakl%2Fpayments)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fmirakl%2Fpayments)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Mirakl](/docs/connectors/mirakl)# Payments using the Mirakl connector

We categorize payment methods into seven families. Each family has similar features, a single integration, and common checkout experiences.

You can use one of our existing connectors or build your own integration to accept payments.

NoteWhen implementing payments, don’t use any of the Connect charge types. The connector takes care of splitting the funds based on your Mirakl orders.

## Payment creation

Choose the payment method families according to the order workflow most adapted to your use case.

FamilyPay on acceptancePay on deliveryPay on due date[Cards](/payments/accept-a-payment)[Bank debits](/payments/bank-debits)[Bank redirects](/payments/bank-redirects)[Credit transfers](/payments/sources/credit-transfers)[Buy now, pay later](/payments/buy-now-pay-later)[Vouchers](/payments/vouchers)[Wallets](/payments/wallets)Below are some additional guidelines for adapting your payment integration to your workflows.

### Pay on acceptance

For cards, set the value of capture_method option to manual when completing the PaymentIntent to authorize only. The connector captures the funds automatically as soon as all sellers have accepted or refused their respective orders. The orders must be accepted or refused within 7 days, the validity period of an authorization.

Because the payment confirmation is immediate for bank redirects, wallets and buy now, pay later, we recommend setting up your orders to be accepted automatically and using refunds when sellers can’t fulfill their order.

### Pay on delivery

For cards, you can authorize only during checkout if you have business rules in place to capture the payment within 7 days. Otherwise, save the card at checkout and authorize later.

For bank debits, you can save the bank account at checkout and initiate the payment after the seller accepts their order.

### Pay on due date

You can use Stripe Billing to send an invoice to your customers who can then pay using our hosted invoice page.

## Payment validation

To handle the payment validation of your Mirakl orders, you can rely on the built-in job or call the PA01 API yourself if you have specific needs such as offering coupons.

To enable the built-in job, you have to first map the Mirakl order with the successful Charge by updating the metadata:

Command Line`curl https://api.stripe.com/v1/charges/ch_1Hmloy2eZvKYlo2C2Tx3W00V \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "metadata[mirakl_commercial_order_id]"=123`The workflow starts when a seller accepts their logistic order.

1. The[payment validation job](/connectors/mirakl/reference#payment-validation)fetches newly accepted Mirakl orders.
2. The connector validates the payment in Mirakl.
3. For cards, the payment is captured when all the logistic orders are accepted or refused.

![](https://b.stripecdn.com/docs-statics-srv/assets/payment-validation.b4e38338cc8ca2b4b9a6b54381e11fb8.svg)

## Payment split

The workflow starts when the payment is validated on Mirakl and captured on Stripe.

1. The[payment split job](/connectors/mirakl/reference#payment-split)fetches newly validated Mirakl orders.
2. The connector transfers the order amount to the seller after deducting your commission.

![](https://b.stripecdn.com/docs-statics-srv/assets/payment-split.854d23364864078f73b0f85509048073.svg)

## Payment refund

The workflow starts when you request a refund on a Mirakl order.

1. The[payment refund job](/connectors/mirakl/reference#payment-refund)fetches newly refunded Mirakl orders.
2. The connector creates a refund on Stripe, validates the refund on Mirakl, and then reverses the transfer used to split the payment.

![](https://b.stripecdn.com/docs-statics-srv/assets/payment-refund.542699f87703a1899287530589e40614.svg)

## See also

- [Integration steps](/connectors/mirakl#integration-steps).

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Payment creation](#payment-creation)[Payment validation](#payment-validation)[Payment split](#payment-split)[Payment refund](#payment-refund)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`