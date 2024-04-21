htmlStripe Connect and the Charges API | Stripe Documentation[Skip to content](#main-content)Charges with Connect[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcharges-api%2Fconnect)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcharges-api%2Fconnect)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)
[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[About the APIs](/docs/payments-api/tour)[Older APIs](/docs/payments/older-apis)[Charges](/docs/payments/charges-api)# Stripe Connect and the Charges API

Legacy APIThe content of this section refers to a Legacy feature. Use the PaymentIntents API instead.

The Charges API doesn’t support the following features, many of which are required for credit card compliance:

- Merchants in India
- [Bank requests for card authentication](/payments/cards/overview)
- [Strong Customer Authentication](/strong-customer-authentication)

Learn how Connect lets you make charges and issue transfers for connected accounts. How you configure these options determines your Stripe fees.

Connect supports three approaches to creating payments for a connected account. For more information about the different types of Connect charges, see the documentation on choosing an approach. Stripe fees are determined by how you configure these options.

This page explains only how to make calls to the Charges API for connected accounts. Check the linked pages for more information about calls to other APIs for related operations.

## Direct charges

To create a direct charge on the connected account, create a Charge object and add the Stripe-Account header with a value of the connected account ID:

Command Line[curl](#)`curl https://api.stripe.com/v1/charges \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d amount=1000 \
  -d currency=usd \
  -d source=tok_visa`This example uses a test token—tok_visa—but you could tokenize a test card using Stripe.js and Elements instead.

See Accept a payment for more details.

### Collect application fees on direct charges

With Connect, your platform can take an application fee on direct charges. To assess an application fee on a charge, pass an optional application_fee_amount value as a positive integer:

Command Line[curl](#)`curl https://api.stripe.com/v1/charges \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d amount=1000 \
  -d currency=usd \
  -d source=tok_visa \
  -d application_fee_amount=123`See Direct charges for information on transfer availability, refunds, and so on.

## Destination charges

To create a destination charge, pass the connected account’s ID in the transfer_data[destination] attribute:

Command Line[curl](#)`curl https://api.stripe.com/v1/charges \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1000 \
  -d currency=usd \
  -d source=tok_visa \
  -d "transfer_data[destination]"={{CONNECTED_ACCOUNT_ID}}`This example uses a test token—tok_visa—but you could tokenize a test card using Stripe.js and Elements instead.

See Accept a payment for more details.

### Collect fees on destination charges with application_fee_amount

When creating destination charges with an application_fee_amount, the full charge amount is immediately transferred from the platform to the transfer_data[destination] account after the charge is captured. The application_fee_amount (capped at the full amount of the charge) is then transferred back to the platform.

CautionAs of September 2019, a regulation called Strong Customer Authentication (SCA) requires businesses in Europe to request additional authentication for online payments. Businesses based in the European Economic Area (EEA) with customers in the EEA should follow the accept a payment guide to use the Payment Intents API to meet these rules.

Command Line[curl](#)`curl https://api.stripe.com/v1/charges \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1000 \
  -d currency=usd \
  -d source=tok_visa \
  -d application_fee_amount=123 \
  -d "transfer_data[destination]"={{CONNECTED_ACCOUNT_ID}}`To provide a better reporting experience, an application fee object is created after the application fee is collected. Use the amount property on the application fee object for reporting. You can then access these objects with the Application Fees endpoint.

### Collect fees on destination charges with transfer_data[amount]

You can also take a fee by using transfer_data[amount].

The transfer_data[amount] is a positive integer reflecting the amount of the charge that’s transferred to the transfer_data[destination]. You subtract your platform’s fees from the charge amount, then pass the result of this calculation as the transfer_data[amount]:

Command Line[curl](#)`curl https://api.stripe.com/v1/charges \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1000 \
  -d currency=usd \
  -d source=tok_visa \
  -d "transfer_data[amount]"=877 \
  -d "transfer_data[destination]"={{CONNECTED_ACCOUNT_ID}}`See Destination charges for information on transfer availability, refunds, and so on.

## Separate charges and transfers

CautionYou can only use separate charges and transfers if both your platform and the connected account are in the same region. For example, if your platform account is in Europe, the connected needs to be in Europe too.

To create a charge and set up the associated transfer, create a transfer_group and assign the charge to the transfer_group.

Command Line[curl](#)`# Create a Charge:
curl https://api.stripe.com/v1/charges \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "amount"=10000 \
  -d "currency"="usd" \
  -d "source"="tok_visa" \
  -d "transfer_group"="{ORDER10}"`Command Line[curl](#)`# Create a Transfer to a connected account (later):
curl https://api.stripe.com/v1/transfers \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "amount"=7000 \
  -d "currency"="usd" \
  -d "destination"="{{CONNECTED_STRIPE_ACCOUNT_ID}}" \
  -d "transfer_group"="{ORDER10}"`Command Line[curl](#)`# Create a second Transfer to another connected account (later):
curl https://api.stripe.com/v1/transfers \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "amount"=2000 \
  -d "currency"="usd" \
  -d "destination"="{{OTHER_CONNECTED_STRIPE_ACCOUNT_ID}}" \
  -d "transfer_group"="{ORDER10}"`This example uses a test token—tok_visa—but you could tokenize a test card using Stripe.js and Elements instead.

See Accept a payment for more information.

### Using on_behalf_of with separate charges and transfers

With separate charges and transfers, by default:

- Charges are settled in the platform’s country
- The fee structure for the platform’s country is used
- The platform’s information is displayed on the customer’s credit card statement

To use the connected account’s country and to display their information instead, use the on_behalf_of argument.

CautionYou can only use on_behalf_of with separate charges and transfers for connected accounts with the card_payments capability.

Command Line[curl](#)`curl https://api.stripe.com/v1/charges \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1000 \
  -d currency=usd \
  -d source=tok_visa \
  -d on_behalf_of={{CONNECTED_ACCOUNT_ID}}`See Creating separate charges and transfers for information on transfer availability, refunds, and so on.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Direct charges](#direct-charges)[Destination charges](#destination-charges)[Separate charges and transfers](#separate-charges-and-transfers)Products Used[Connect](/connect)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`