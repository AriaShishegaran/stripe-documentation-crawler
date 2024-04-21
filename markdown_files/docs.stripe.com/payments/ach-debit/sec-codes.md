htmlOverview of ACH SEC codes | Stripe Documentation[Skip to content](#main-content)SEC codes[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fach-debit%2Fsec-codes)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fach-debit%2Fsec-codes)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank debits](/docs/payments/bank-debits)[ACH Direct Debit](/docs/payments/ach-debit)# Overview of ACH SEC codes

Learn about different types of customer authorizations for ACH Direct Debit.A Standard Entry Class (SEC) code is a three letter code that describes how a customer or business authorized an ACH transaction. SEC codes are defined and maintained by Nacha, the governing body for the ACH network.

Businesses must make sure that the correct code is used when initiating debit transactions to make sure they comply with ACH Direct Debit rules and appropriate authorization evidence in the event of a dispute. The business is responsible under the ACH Direct Debit rules for indicating the appropriate SEC code for each ACH transaction.

Stripe currently supports four types of SEC codes for ACH Debits. If you don’t specify a mandate collection method, Stripe defaults to using WEB for consumer bank accounts and CCD for business bank accounts.

The mandate requirements under ACH Direct Debit rules and applicable law vary based on the type of mandate collected. The information on this page relating to your compliance with ACH mandate requirements is for your general guidance, and isn’t legal advice. If you’re unsure of the applicable mandate requirements, consult with a professional about your obligations.

## WEB (Internet Initiated/Mobile Entry)

This code is used to initiate entries to a consumer’s account when the internet or a mobile device is used to initiate the transaction. WEB is the default unless you indicate otherwise. Refunds processed for WEB transactions use the PPD SEC code.

## CCD (Corporate Credit or Debit Entry)

This code is used to facilitate business-to-business payments and is applied to charges to all PaymentMethods that have account_holder_type=company, regardless of the authorization type.

## PPD (Prearranged Payment and Deposit)

This code is used to initiate entries to a consumer’s account, based on standing or single-entry authorization from that customer in writing. Your customer’s authorization must be in writing and signed or otherwise authenticated (that is, confirm the customer’s identity and agreement such as using a phone for a previously provided written authorization). Authorizations need to include information required for online mandates and you must provide a copy of the authorization to your customer.

To initiate a PPD debit, you must create a mandate with offline customer acceptance. You can do so by confirming a PaymentIntent or a SetupIntent with offline customer acceptance and providing a collection_method=paper mandate option as shown below:

PaymentIntentSetupIntentCommand Line[curl](#)`curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/confirm \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "mandate_data[customer_acceptance][type]"=offline \
  -d "mandate_data[customer_acceptance][accepted_at]"=1647448692 \
  -d "payment_method_options[us_bank_account][mandate_options][collection_method]"=paper`## TEL (Telephone-Initiated Entry) Beta

This code is used to initiate debit transactions to a consumer’s account when authorization is given over the telephone. TEL debits are currently in private beta. Contact Stripe Support if you initiate bank debits to consumer accounts over the telephone.

### Requirements for Telephone-initiated payments

If your business accepts ACH payments over the telephone, Stripe supports single TEL ACH debit transactions. Don’t use a TEL entry where a standing authorization is in place or to support a recurring transaction. TEL entries have their own Nacha requirements that you need to meet prior to accepting and processing these payments.

Existing relationship![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You can only use a TEL entry if:

- You and the customer have an existing relationship, which means that:  - You and the customer have a written agreement in place for the provisionof goods or services; or
  - Your customer has purchased goods or services from you within the past 2years; or


- You don’t have an existing relationship with the customer, but the customerinitiated the telephone call to you.

Your customer’s pre-existing relationship with one of your affiliates is not sufficient to be an existing relationship between you and your customer.

Verifications![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You must establish and implement commercially reasonable procedures to verify the identity of the customer (for example, name, address, and telephone number). Additionally, you must establish and implement commercially reasonable procedures to verify that the routing numbers provided by your customers are valid.

Authorization requirements![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Your customer’s explicit oral authorization is needed prior to you initiating a debit entry to their account. Authorizations need to include information required for online mandates, along with a telephone number available to your customer for inquiries.

In addition, you must capture authorization by either an audio recording of the customer’s oral authorization (in accordance with applicable state law regarding the recording of calls) or providing written notice to the customer of their authorization before the first debit of their bank account.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[WEB (Internet Initiated/Mobile Entry)](#web-sec-code)[CCD (Corporate Credit or Debit Entry)](#ccd-sec-code)[PPD (Prearranged Payment and Deposit)](#ppd-sec-code)[TEL (Telephone-Initiated Entry)](#tel-sec-code)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`