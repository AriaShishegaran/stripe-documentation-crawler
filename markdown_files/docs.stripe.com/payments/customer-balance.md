htmlCustomer balance | Stripe Documentation[Skip to content](#main-content)Customer balance[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcustomer-balance)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcustomer-balance)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank transfers](/docs/payments/bank-transfers)# Customer balance

Learn how to use the customer balance with payments.Your customers might have associated balances that contain two types of funds—cash and credit.

## Cash balances

A customer’s cash balance represents funds that they can use for payment. When they overpay or send an amount using a bank transfer that isn’t automatically reconciled with any outstanding payment, we add these funds to the customer cash balance. You can use these funds for later payments for the same customer, or initiate a refund from their cash balance to return the funds to their bank account, limited to the amount available in the customer balance.

You can’t add funds to the customer cash balance directly. This isn’t a balance that customers can top up and is only there as a reconciliation layer—it’s not a digital wallet or e-money. You can’t use the cash balance for any other purpose besides future payments, or returns to the customer it’s associated with.

## Credit balances

In contrast to a cash balance, a credit balance is an Invoices feature that represents liability between you and the customer. You can’t use credit balance funds for payment, but you can apply them to offset future invoices. You can update the customer credit balance by creating an adjustment Customer Balance Transaction. For more information on credit balances, refer to Customer Credit Balance.

## View the customer balance

You can find a customer’s balance with both the API and through the Stripe Dashboard. To view a customer’s balance using the API, first retrieve the customer and then expand the cash_balance field.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers/{{CUSTOMER_ID}}?expand[]=cash_balance \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \``{
  "id": "cus_HgrkK7bxHMy65g",
  "object": "customer",
  "address": null,
  "cash_balance": {
    "available": {
        "usd": 50,
    },
    "settings": {
      "reconciliation_mode": "automatic"
    },
    "livemode": "true",
    "object": "cash_balance",
  },
  "created": 1598918400,`See all 78 linesTo view a customer’s balance in the Dashboard, navigate to the Customer page. The customer’s balance appears in the Payment methods section.

## Make a payment from the cash balance

When your customer has a cash balance, you can use the funds immediately to make a payment up to the available amount. To do this, create a PaymentIntent using the customer_balance payment method type.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d amount=1099 \
  -d currency=usd \
  -d customer="{{CUSTOMER_ID}}" \
  -d "payment_method_types[]"=customer_balance \
  -d "payment_method_data[type]"=customer_balance \
  -d confirm=true`When your customer has a cash balance, you can use the funds immediately to make a payment up to the available amount. You can do this by using either the API or the Dashboard.

To make a payment using the API, create a PaymentIntent using the customer_balance payment method type.

The payment succeeds if the cash balance has sufficient funds, and fails otherwise.

To collect more funds from the customer when the cash balance is insufficient, use the customer balance with a bank transfer funding.

## List changes to the customer balance

Changes to the customer’s cash balance are modeled as a list of cash balance transactions. You can retrieve these transactions for a customer to see how their cash balance has changed over time.

## Cash balance transaction types

Cash balance transactions have a type value indicating the type of action that caused the cash balance to change.

TypeDescription`funded`The customer has funded their balance by making a bank transfer. Funds represented by these transactions might be automatically applied to payment intents and invoices depending on the[reconciliation](/payments/customer-balance/reconciliation)procedure. If these funds are applied automatically, you’ll see additional transactions of type`applied_to_payment`representing that.`applied_to_payment`Funds from the cash balance were applied to a payment intent, either by[reconciliation](/payments/customer-balance/reconciliation#cash-automatic-reconciliation)after funding arrives, or by[manual reconciliation](/payments/customer-balance/reconciliation#cash-manual-reconciliation).`unapplied_from_payment`A[partially funded](/payments/bank-transfers/accept-a-payment?payment-ui=direct-api#handling-underpayments-and-overpayments)payment intent was[modified](/api/payment_intents/update)or[canceled](/api/payment_intents/cancel), and the funds were returned to the customer’s cash balance. You can use these funds for future payments.`refunded_from_payment`A successful payment intent has been[refunded to the customer cash balance](/payments/customer-balance/refunding#refund-customer-balance-payment-customer-balance). You can use these funds for future payments.`return_initiated`Unspent funds are being returned to the customer’s bank account from their cash balance.`return_canceled`An attempt to return funds to the customer’s bank account has been canceled, either because you[canceled the refund before the customer submitted their bank details](/payments/customer-balance/refunding#create-return-dashboard-cancel), or we weren’t able to collect bank account details from the customer. For more information about refund state transitions, see[Refund bank transfer payments](/payments/customer-balance/refunding#refund-customer-balance-payment-bank-account).`transferred_to_balance`Funds have been moved from the cash balance to your Stripe balance due to failed refunds or insufficient refund details.[OptionalAccess to full sender IBAN for `funded` cash balance transactions](#access-full-sender-iban)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Cash balances](#cash)[Credit balances](#credit)[View the customer balance](#view-balance)[Make a payment from the cash balance](#make-cash-payment)[List changes to the customer balance](#cash-balance-transactions)[Cash balance transaction types](#types)Products Used[Payments](/payments)[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`