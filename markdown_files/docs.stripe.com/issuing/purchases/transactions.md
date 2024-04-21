htmlIssuing transactions | Stripe Documentation[Skip to content](#main-content)Transactions[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fpurchases%2Ftransactions)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/issuing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fpurchases%2Ftransactions)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)
[Treasury](#)[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Issuing](/issuing)·[Home](/docs)[Banking as a service](/docs/financial-services)[Issuing cards](/docs/issuing)# Issuing transactions

Learn how to use Issuing to handle transactions.After an authorization is approved and is captured, the status on the authorization is set to closed and a Transaction object is created. This normally happens within 24 hours; however hotels, airlines, and car rental companies are able to capture up to 31 days after authorization.

When an authorization is captured, two things happen.

- The`status`on the authorization is set to`closed`, releasing the purchase amount held by that authorization. A[balance transaction](/reports/balance-transaction-types)of type`issuing_authorization_release`is created to represent this.
- A new transaction object of type`capture`is created. The purchase amount is deducted from the[balance you’re using for Issuing](/issuing/funding/balance).

Spending controls, real time authorization controls, and card status (whether a card is active or not) don’t apply for capture. They can be used to determine whether authorizations are approved, but captures for approved authorizations always succeed.

## Handling other transactions

In addition to regular transactions, there are a few other cases that you should be ready to handle.

RefundsPartial captureOver captureMulti captureForce captureRefunds are transactions with type of refund.

When we create a transaction representing a refund or credit, we try to link it to the original payment authorization. Refunds aren’t necessarily tied to the original payment transaction or authorization, so linking them is an inexact science. As a result, we might link to an unrelated authorization or be unable to link to an authorization at all (for example, if the card is credited rather than refunded). In these cases, the authorization field of the transaction is set to null, and the transaction won’t be linked to the authorization. We process all refunds and credits the same way, regardless of their linkage to a payment authorization.

`{
  "id": "ipi_1GTG10EEsyYlpYZ9VJn2xV3B",
  "object": "issuing.transaction",
  "amount": 100,
  "authorization": "iauth_1GBZQyEEsyYlpYZ9255L8GQC",
  "balance_transaction": null,
  "card": "ic_1GBZQJEEsyYlpYZ99v6rq38S",
  "cardholder": null,
  "created": 1585783834,
  "currency": "eur",
  "livemode": false,
  "merchant_amount": 100,
  "merchant_currency": "eur",
  "merchant_data": {
    "category": "taxicabs_limousines",
    "city": "Berlin",
    "country": "DE",
    "name": "Rocket Rides",
    "network_id": "1234567890",
    "postal_code": "45276",
    "url": null
  },
  "metadata": {},
  "type": "refund",
}`### Testing

To simulate the creation of a refund transaction, you can use the Transaction Refund API in the Issuing test helpers.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/test_helpers/issuing/transactions/{{TRANSACTION_ID}}/refund \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`To create a refund transaction that doesn’t link to an authorization, use the Create Unlinked Refund API in the Issuing test helpers.

Command Line[curl](#)`curl https://api.stripe.com/v1/test_helpers/issuing/transactions/create_unlinked_refund \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d card={{CARD_ID}} \
  -d amount=1000`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`