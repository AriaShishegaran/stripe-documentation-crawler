htmlAccept a bank transfer | Stripe Documentation[Skip to content](#main-content)Accept a payment[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbank-transfers%2Faccept-a-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbank-transfers%2Faccept-a-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank transfers](/docs/payments/bank-transfers)# Accept a bank transfer

Use the Payment Intents API to accept bank transfer payments.The first time you accept a bank transfer payment from a customer, Stripe generates a virtual bank account for them, which you can then share with them directly. All future bank transfer payments from this customer get sent to this bank account. In some countries, Stripe also provides you with a unique transfer reference number that your customer should include with each transfer to make it easier to match the transfer against outstanding payments. Some countries have limits on the number of virtual bank account numbers that you can create for free.

You can find an overview of the common steps when accepting a bank transfer payment in the following sequence diagram:

With InvoicesWithout Invoices## Handling underpayments and overpayments

With bank transfer payments, it’s possible that the customer sends you more or less than the expected payment amount. If the customer sends too little, Stripe partially funds an open payment intent. Invoices won’t be partially funded and remain open until incoming funds cover the full invoice amount.

If the customer sends more than the expected amount, Stripe attempts to reconcile the incoming funds against an open payment and keep the remaining excess amount in the customer cash balance. You can find more details on how Stripe handles reconciliation in the reconciliation section of our documentation.

With InvoicesWithout InvoicesWhen a customer underpays:

When a customer overpays:

## Handling multiple open payments or invoices

You might have multiple open payments or invoices which can be paid with a bank transfer. In the default setup, Stripe attempts to automatically reconcile the bank transfer by using information like the transfer’s reference code or the amount transferred.

You can disable automatic reconciliation and manually reconcile payments and invoices yourself. You can override the automatic reconciliation behavior on a per-customer basis by setting reconciliation mode to manual.

APICustom payment formPrebuilt checkout page[Set up StripeServer-side](#web-set-up-stripe)First, you need a Stripe account. Register now.

Use our official libraries for access to the Stripe API from your application:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`[Create or retrieve a CustomerServer-side](#web-create-a-customer)You must associate a Customer object to reconcile each bank transfer payment. If you have an existing Customer object, you can skip this step. Otherwise, create a new Customer object.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`[Create and confirm a PaymentIntentServer-side](#web-create-and-confirm-payment-intent)A PaymentIntent is an object that represents your intent to collect payment from a customer and tracks the lifecycle of the payment process through each stage. Create and confirm a PaymentIntent on the server, specifying the amount and currency you want to collect.

Manage payment methods from the DashboardList payment methods manuallyBefore creating a Payment Intent, make sure to turn Bank transfer on in the payment methods settings page of your Dashboard.

NoteWith Dynamic payment methods, Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow.

USUKEUJPMXCommand Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1099 \
  -d customer={{CUSTOMER_ID}} \
  -d currency=usd \
  -d "automatic_payment_methods[enabled]"=true \
  --data-urlencode return_url="https://example.com/return_url" \
  -d "payment_method_data[type]"=customer_balance \
  -d confirm=true`In the latest version of the API, specifying the automatic_payment_methods parameter is optional because Stripe enables its functionality by default.

If the customer already has a balance high enough to cover the payment amount, the PaymentIntent immediately succeeds with a succeeded status. Customers can accrue a balance when they accidentally overpay for a transaction—a common occurrence with bank transfers. You must reconcile customer balances within a certain period based on your location.

[Instruct the customer to complete a bank transferClient-side](#web-complete-bank-transfer)If the customer balance isn’t high enough to cover the request amount, the PaymentIntent shows a requires_action status. The response has a next_action field containing a type value of display_bank_transfer_instructions. The next_action[display_bank_transfer_instructions] hash contains information to display to your customer so that they can complete the bank transfer.

NoteIn live mode, Stripe supplies each customer with a unique set of bank transfer details. In contrast, Stripe offers invalid bank transfer details to all customers in test mode. Unlike live mode, these invalid details might not always be unique.

USUKEUJPMXFieldDescription[type](/api/payment_intents/object#payment_intent_object-next_action-display_bank_transfer_instructions-type)The type of bank transfer to use. Type must be`us_bank_transfer`in the US.[reference](/api/payment_intents/object#payment_intent_object-next_action-display_bank_transfer_instructions-reference)A unique reference code to identify the bank transfer. Instruct your customer to include this code in the reference field of their bank transfer.[amount_remaining](/api/payment_intents/object#payment_intent_object-next_action-display_bank_transfer_instructions-amount_remaining)The remaining amount that needs to be transferred to complete the payment. Instruct your customer to transfer this amount. This might be different from the PaymentIntent amount if pre-existing funds in the customer balance were applied to the PaymentIntent or if your customer underpaid.[currency](/api/payment_intents/object#payment_intent_object-next_action-display_bank_transfer_instructions-currency)The currency for the remaining amount.[financial_addresses](/api/payment_intents/object#payment_intent_object-next_action-display_bank_transfer_instructions)List of financial addresses for US bank accounts. Types include`aba`and`swift`. See below for details.[hosted_instructions_url](/api/payment_intents/object#payment_intent_object-next_action-display_bank_transfer_instructions-hosted_instructions_url)A link to a hosted page that guides your customer through completing the transfer.`aba`hash![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Example of an aba hash:

`{
  "aba": {
    "account_number": "111222333444",
    "bank_name": "Wells Fargo Bank, NA",
    "routing_number": "444555666"
  },
  "supported_networks": [
    "ach",
    "domestic_wire_us"
  ],
  "type": "aba"
}`FieldValue(s)Description`type``aba`The type of financial address.`supported_networks`- `ach`
- `domestic_wire_us`

The list of networks supported by this address.`aba.account_number`111222333444The ABA account number.`aba.routing_number`444555666The ABA routing number.`aba.bank_name`Wells Fargo Bank, NAThe name of the bank.`swift`hash![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Example of a swift hash:

`{
  "swift": {
    "account_number": "111222333444",
    "bank_name": "Wells Fargo Bank, NA",
    "swift_code": "AAAA-BB-CC-123"
  },
  "supported_networks": [
    "swift"
  ],
  "type": "swift"
}`FieldValue(s)Description`type``swift`The type of financial address.`supported_networks`- `swift`

The list of networks supported by this address.`swift.account_number`111222333444The SWIFT account number.`swift.swift_code`AAAA-BB-CC-123The SWIFT code.`swift.bank_name`Wells Fargo Bank, NAThe name of the bank.Settlement timing![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

After instructing your customer to initiate a transfer with their bank using the information you provide, it can take up to 5 days for the transfer to complete. The settlement timing depends on the banking rails that the transfer arrived through to Stripe:

- ACH transfers arrive within 1-3 business days.
- Domestic wire transfers (Fedwire) arrive on the same day (depending on whether the transfer is sent before the bank’s cut-off time).
- International wire transfers (SWIFT) arrive within 1-5 business days.

[Confirm the PaymentIntent succeeded](#web-confirm-success)The PaymentIntent stays in a requires_action status until funds arrive in the bank account. When funds are ready, the PaymentIntent status updates from requires_action to succeeded.

You need to set up your webhook endpoint to start receiving the payment_intent.partially_funded event.

You can add a webhook from the Dashboard.

Alternatively, you can use the Webhook Endpoints API to start receiving the payment_intent.partially_funded event.

Stripe sends the following events during the payment funding flow when we update the PaymentIntent.

EventDescriptionNext steps`payment_intent.requires_action`Sent during confirmation when the customer balance doesn’t have sufficient funds to reconcile the PaymentIntent, the PaymentIntent transitions to`requires_action`.Instruct your customer to send a bank transfer with the`amount_remaining`.`payment_intent.partially_funded`The customer sent a bank transfer that was applied to the PaymentIntent, but wasn’t enough to complete the payment. This might happen because the customer transferred an insufficient amount (because of a mistaken underpayment or fees charged by their bank) or because a remaining customer balance was applied to this PaymentIntent. PaymentIntents that are partially funded aren’t reflected in your account balance until the payment is complete.Instruct your customer to send another bank transfer with the new`amount_remaining`to complete the payment. If you want to complete the payment with the partially applied funds, you can update the`amount`and[confirm](/api/payment_intents/confirm)the PaymentIntent again.`payment_intent.succeeded`The customer’s payment succeeded.Fulfill the goods or services that the customer purchased.CautionWhen you change the amount of a partially funded PaymentIntent, the funds are returned to the customer balance. If other PaymentIntents are open, Stripe funds those automatically. If the customer is configured for manual reconciliation, you need to apply the funds again.

We recommend using webhooks to confirm the charge has succeeded and to notify the customer that the payment is complete.

### Sample code

[Ruby](#)`require 'json'

# Using Sinatra
post '/webhook' do
  payload = request.body.read
  event = nil

  begin
    event = Stripe::Event.construct_from(
      JSON.parse(payload, symbolize_names: true)`See all 38 lines### View pending payments in the Dashboard

You can view all pending bank transfer PaymentIntents in the Dashboard by applying the Waiting on funding filter to Status .

[Test your integration](#test-your-integration)You can test your integration by simulating an incoming bank transfer using either the Dashboard or an HTTP request.

### With the Dashboard

To simulate a bank transfer using the Dashboard, navigate to the customer’s page in the Dashboard. Under Payment methods, click Add and select Fund cash balance (testmode only).

### With the Stripe API

You can make an API call to simulate a bank transfer.

USUKEUJPMXCommand Line[curl](#)`curl https://api.stripe.com/v1/test_helpers/customers/ic_xxxxxxxxx/fund_cash_balance \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1000 \
  -d currency=usd \
  -d reference=REF-4242`[Handling temporary availability issues](#handling-temporary-availability-issues)The following error codes indicate temporary issues with the availability of the payment method:

CodeDescriptionHandling`payment_method_rate_limit_exceeded`Too many requests were made in quick succession for this payment method, which has stricter limits than the[API-wide rate limits](/rate-limits).These errors can persist for several API requests when many of your customers try to use the same payment method, such as during an ongoing sale on your website. In this case, ask your customers to choose a different payment method.CautionIf you anticipate heavy usage in general or because of an upcoming event, contact us as soon as you know about it.

[OptionalCollecting payment method options from your customer](#collect-payment-method-options)[OptionalSend payment instruction emails](#instruction-emails)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Handling underpayments and overpayments](#handling-underpayments-and-overpayments)[Handling multiple open payments or invoices](#handling-multiple-open-payments-or-invoices)[Set up Stripe](#web-set-up-stripe)[Create or retrieve a Customer](#web-create-a-customer)[Create and confirm a PaymentIntent](#web-create-and-confirm-payment-intent)[Instruct the customer to complete a bank transfer](#web-complete-bank-transfer)[Confirm the PaymentIntent succeeded](#web-confirm-success)[Test your integration](#test-your-integration)[Handling temporary availability issues](#handling-temporary-availability-issues)Products Used[Payments](/payments)[Invoicing](/invoicing)[Checkout](/payments/checkout)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`