htmlApple Pay Later | Stripe Documentation[Skip to content](#main-content)Apple Pay Later[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fapple-pay-later)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fapple-pay-later)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Buy now, pay later](/docs/payments/buy-now-pay-later)# Apple Pay Later

Learn about Apple Pay Later, a US payment method for customers to buy now and pay later.Apple Pay Later1 is a buy now, pay later feature of Apple Pay that allows customers in the United States to split purchases into multiple equal installments across six weeks. Apple backs and manages payments, and businesses are paid the full amount in the same manner as with Apple Pay.

Payment method propertiesCountry availability- Customer locations

United States


- Presentment currency

USD


- Payment confirmation

Customer-initiated


- Payment method family

Buy Now, Pay Later


- Recurring payments

No


- Payout timing

Standard


- Connect support

Yes


- Refunds / Partial refunds

Yes / yes


- Dispute support

Yes, by email from Stripe



## Payment flow

Customers that select Apple Pay during checkout see two payment options: Pay in Full and Pay Later. The first time a customer chooses Pay Later, they complete Apple’s application flow. If they’re a returning customer using Apple Pay Later, they can complete their Apple Pay Later payment directly in the UI.

![Apple Pay Later shown in the Apple Pay UI](https://b.stripecdn.com/docs-statics-srv/assets/apple-pay-later-flow-demo.3c9dd818d34c692a854e6a268656b0fb.png)

## Get started

Apple Pay Later is a buy now, pay later payment method available for Apple Pay. It’s on by default if your integration accepts Apple Pay. See Mastercard Installments to learn how Apple Pay Later uses the Mastercard network.

Apple Pay Later is one of several lenders using Mastercard Installments. Opting out of Mastercard Installments opts you out of all lenders including Apple Pay Later. Contact Stripe support to request an opt out of Apple Pay Later.

## Payment options

Customers can use Apple Pay Later for purchases between 75 USD and 1,000 USD. Customers can split a purchase into four equal payments over six weeks, with a down payment due at the time of purchase, and with no interest or fees2, while businesses are paid upfront. Apple Pay Later prohibits adding surcharges to purchases. The Mastercard Installments program enables Apple Pay Later through your existing Stripe integration, so it requires no additional integration work for eligible businesses that already have Apple Pay.

Apple Pay Later is available for purchases made with an iPhone or iPad when customers check out with Apple Pay and tap the Pay Later option. It’s also built into Apple Wallet so customers can track payment schedules and manage returns.

## Prohibited business categories

In addition to the categories of businesses restricted from using Stripe overall, Apple Pay Later prohibits the following business and item categories:

- Gambling
- Public administration (for example, tax, alimony, or bail)
- Money transfer
- Funding transactions
- Quasi cash
- Merchandise and services: customer financial institution
- Payment transaction
- MoneySend

## Handle ineligible payments

Apple Pay Later doesn’t support recurring payments, future payments, or payments for prohibited items. Depending on your integration, you can make sure Apple Pay Later doesn’t appear as an available payment method in these cases for devices on iOS17 or later. We recommend making updates to the applePayLaterAvailability parameter as shown below to avoid having payments fail if a customer chooses Apple Pay Later for one of these payments.

applePayLaterAvailabilityDescriptionavailable(default) Apple Pay Later is available.unavailableItemIneligibleApple Pay Later is unavailable because one or more ineligible or prohibited items are in the shopping cart, such as gift cards.unavailableRecurringTransactionApple Pay Later is unavailable because there’s a recurring payment or subscription in the shopping cart.### Express Checkout Element

### Payment Request Button

### Payment Element

### Mobile Payment Element

### Direct integration with Apple Pay

## Refunds and disputed payments

Apple Pay Later has the same refund and payment dispute process as Apple Pay. See the Stripe disputes and fraud documentation for more information.



1Subject to eligibility and approval. Available only in the US. It might not be available in all states.

2A customer’s bank might charge the customer fees if their debit card account contains insufficient funds to make loan repayments.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Payment flow](#payment-flow)[Get started](#get-started)[Payment options](#payment-options)[Prohibited business categories](#prohibited-business-categories)[Handle ineligible payments](#handle-ineligible-payments)[Refunds and disputed payments](#refunds-and-disputed-payments)Products Used[Payments](/payments)[Connect](/connect)[Payment Links](/payments/payment-links)[Checkout](/payments/checkout)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`