htmlDisputed PayPal payments | Stripe Documentation[Skip to content](#main-content)Disputed payments[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpaypal%2Fdisputed-payments)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpaypal%2Fdisputed-payments)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Wallets](/docs/payments/wallets)[PayPal](/docs/payments/paypal)# Disputed PayPal payments

Learn how dispute management works for PayPal, a digital wallet popular with businesses in Europe.The risk of fraud or unrecognized PayPal payments is low because the customer must authenticate the payment with their PayPal account.

## Overview

Customers must authenticate any payment with their PayPal account to decrease the risk of fraud. However, customers can dispute PayPal payments if for example:

- They don’t receive the goods they paid for
- The received goods don’t match their description

Note that your settlement choice when activating PayPal affects the funds flow for PayPal disputes. See Choose settlement preference for more context.

## Dispute process

Customers can file a dispute on PayPal up to 180 calendar days from the date of purchase. They can also file a dispute through the payment instrument they used to complete the PayPal purchase (such as their bank).

After the customer initiates a dispute, Stripe notifies you through:

- Email
- The[Stripe Dashboard](https://dashboard.stripe.com/disputes)
- An API`charge.dispute.created`event (if your integration is set up to receive[webhooks](/webhooks))
- Push notification (if you’ve subscribed)

Depending on the type of dispute and where it was filed, PayPal might offer the ability for you to communicate directly with the customer in an attempt to resolve the dispute before countering it. Currently, Stripe doesn’t offer this functionality and requests that you turn to PayPal to contact the customer.

If no agreement is reached, you can either accept or counter the dispute. If you choose to counter, Stripe requests that you submit evidence that you fulfilled the purchase order in the Stripe Dashboard. This evidence helps PayPal determine if a dispute is valid or if they should reject it. The evidence you provide must contain as much detail as possible from what the customer provided at checkout. You must submit the requested information within 19 calendar days. PayPal aims to make a decision within 30 calendar days of evidence submission.

If you prefer to handle disputes programmatically, you can respond to disputes using the API.

## Dispute resolution

If PayPal resolves the dispute with you winning, the disputed amount will be returned to your balance.

If PayPal rules in favor of the customer, the dispute is lost and the balance charge becomes permanent.

In some cases, PayPal will allow a lost dispute to be appealed. Currently, Stripe does not support appeals and requests that you turn to PayPal to file an appeal. In these cases, the dispute will remain open on Stripe until a final resolution has been reached by PayPal. Please refer to PayPal to be notified on when a dispute becomes appealable.

Read more about disputes on how disputes work and best practices for responding to disputes.

## Fees

PayPal might charge fees for disputes. The terms and amount of PayPal dispute fees are set by PayPal. Stripe does not charge any additional fees for PayPal disputes.

## Testing your integration

Stripe allows you to simulate a disputed transaction by specifying email values that match the patterns described in test scenarios when you create a PaymentIntent (as part of the billing details). You can choose from the different test scenarios to simulate disputes of all relevant categories.

For example, creating the PaymentIntent server-side and simulating a disputed transaction where the buyer claims they didn’t receive the product looks like:

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1099 \
  -d currency=eur \
  -d "payment_method_types[]"=paypal \
  -d "payment_method_data[type]"=paypal \
  --data-urlencode "payment_method_data[billing_details][email]"="dispute_not_received@example.com"`If using Checkout or Payment Links, you can enter the email in the checkout form. Shortly after the payment has been completed, it will be disputed as product_not_received.

### Test scenarios

The table below displays the scenarios available to test. Each scenario produces a dispute shortly after a payment has been completed.

.* represents any valid character in an email. For example, the pattern .*dispute_duplicate@.* is matched by an email such as my_dispute_duplicate@mycompany.com.

Email patternScenario`.*dispute_credit_not_processed@.*`Tests a dispute for a payment where the customer claims they’re entitled to a full or partial refund because they returned the purchased product or didn’t fully use it, or the transaction was otherwise canceled or not fully fulfilled, but you haven’t yet provided a refund or credit.`.*dispute_duplicate@.*`The customer claims they were charged multiple times for the same product or service.`.*dispute_fraudulent@.*`The customer claims that the transaction is fraudulent and they did not authorize the transaction.`.*dispute_general@.*`Tests a dispute for a payment where an uncategorized dispute has been opened.`.*dispute_not_received@.*`The customer claims that they have not received the product or service they purchased.`.*dispute_product_unacceptable@.*`The customer claims that the product or service they purchased was unacceptable or otherwise not as described.`.*dispute_subscription_cancelled@.*`The customer claims that they were charged for a subscription after it was canceled.### Evidence

To simulate winning or losing the dispute, respond with one of the evidence values from the table below.

- If you[respond using the API](/disputes/api), pass the value from the table as[uncategorized_text](/api/disputes/update#update_dispute-evidence-uncategorized_text).
- If you[respond in the Dashboard](/disputes/responding), enter the value from the table in theAdditional informationfield. Then, clickSubmit evidence.

EvidenceDescription`winning_evidence`The dispute is closed and marked as won. Your account is credited the amount of the charge.`losing_evidence`The dispute is closed and marked as lost. Your account isn’t credited.Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Overview](#overview)[Dispute process](#dispute-process)[Dispute resolution](#dispute-resolution)[Fees](#fees)[Testing your integration](#testing-your-integration)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`