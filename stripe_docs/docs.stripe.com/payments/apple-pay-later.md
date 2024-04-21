# Apple Pay Later

Apple Pay Later1 is a buy now, pay later feature of Apple Pay that allows customers in the United States to split purchases into multiple equal installments across six weeks. Apple backs and manages payments, and businesses are paid the full amount in the same manner as with Apple Pay.

[buy now, pay later](/payments/payment-methods/overview)

- Customer locationsUnited States

Customer locations

United States

- Presentment currencyUSD

Presentment currency

USD

- Payment confirmationCustomer-initiated

Payment confirmation

Customer-initiated

- Payment method familyBuy Now, Pay Later

Payment method family

Buy Now, Pay Later

- Recurring paymentsNo

Recurring payments

No

- Payout timingStandard

Payout timing

Standard

- Connect supportYes

Connect support

Yes

- Refunds / Partial refundsYes / yes

Refunds / Partial refunds

Yes / yes

- Dispute supportYes, by email from Stripe

Dispute support

Yes, by email from Stripe

## Payment flow

Customers that select Apple Pay during checkout see two payment options: Pay in Full and Pay Later. The first time a customer chooses Pay Later, they complete Apple’s application flow. If they’re a returning customer using Apple Pay Later, they can complete their Apple Pay Later payment directly in the UI.

[application flow](https://support.apple.com/en-us/HT212967)

## Get started

Apple Pay Later is a buy now, pay later payment method available for Apple Pay. It’s on by default if your integration accepts Apple Pay. See Mastercard Installments to learn how Apple Pay Later uses the Mastercard network.

[Mastercard Installments](https://support.stripe.com/questions/mastercard-installments-faq)

Apple Pay Later is one of several lenders using Mastercard Installments. Opting out of Mastercard Installments opts you out of all lenders including Apple Pay Later. Contact Stripe support to request an opt out of Apple Pay Later.

[Stripe support](https://support.stripe.com/contact/email?question=other&topic=payment_apis&subject=ApplePayLater)

## Payment options

Customers can use Apple Pay Later for purchases between 75 USD and 1,000 USD. Customers can split a purchase into four equal payments over six weeks, with a down payment due at the time of purchase, and with no interest or fees2, while businesses are paid upfront. Apple Pay Later prohibits adding surcharges to purchases. The Mastercard Installments program enables Apple Pay Later through your existing Stripe integration, so it requires no additional integration work for eligible businesses that already have Apple Pay.

Apple Pay Later is available for purchases made with an iPhone or iPad when customers check out with Apple Pay and tap the Pay Later option. It’s also built into Apple Wallet so customers can track payment schedules and manage returns.

## Prohibited business categories

In addition to the categories of businesses restricted from using Stripe overall, Apple Pay Later prohibits the following business and item categories:

[businesses restricted from using Stripe overall](https://stripe.com/legal/restricted-businesses)

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

## Refunds and disputed payments

Apple Pay Later has the same refund and payment dispute process as Apple Pay. See the Stripe disputes and fraud documentation for more information.

[disputes and fraud documentation](/disputes)



1Subject to eligibility and approval. Available only in the US. It might not be available in all states.

2A customer’s bank might charge the customer fees if their debit card account contains insufficient funds to make loan repayments.
