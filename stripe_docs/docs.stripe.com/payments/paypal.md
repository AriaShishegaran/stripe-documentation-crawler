# PayPal payments

PayPal is a payment method that enables customers in any country to pay using their PayPal account.

To pay using PayPal, customers are redirected from your website to PayPal. They choose a funding source: PayPal wallet, linked card or bank account, or buy now, pay later. Then they authenticate the payment. After successful authorization, the customer is redirected back to your website. You receive an immediate notification of the payment’s success or failure.

[immediate notification](/payments/payment-methods#payment-notification)

- Customer locationsWorldwide

Customer locations

Worldwide

- Presentment currencyEUR, GBP, USD, CHF, CZK, DKK, NOK, PLN, SEK, AUD, CAD, HKD, NZD, SGD

Presentment currency

EUR, GBP, USD, CHF, CZK, DKK, NOK, PLN, SEK, AUD, CAD, HKD, NZD, SGD

- Payment method familyWallets

Payment method family

Wallets

- Payment confirmationCustomer-initiated

Payment confirmation

Customer-initiated

- Payout timingStandard payout timing applies

Payout timing

Standard payout timing applies

[Standard payout timing](/payouts#payout-speed)

- Connect supportPartial (requires manual approval, see details below)

Connect support

Partial (requires manual approval, see details below)

- Recurring paymentsRequires approval

Recurring payments

Requires approval

- Dispute supportYes

Dispute support

Yes

- Refunds / Partial refundsYes / Yes

Refunds / Partial refunds

Yes / Yes

## Payment flow

Customer selects PayPal at checkout

[Customer](/api/customers)

Customer is redirected to PayPal and enters login details

Customer completes authorization process

Customer is notified that payment is complete

(Optional) Customer returns back to business’s site for payment confirmation

## Connect support

PayPal is available for online marketplaces using Stripe Connect. These online marketplaces include businesses such as Deliveroo and ManoMano that collect payments from customers, and later pay out to sub-accounts or service providers. PayPal isn’t available for platforms that onboard other businesses and enable them to accept payments directly, such as Shopify or Squarespace.

[Stripe Connect](https://stripe.com/connect)

Online marketplaces need to submit an onboarding request from the Stripe Dashboard to get access to PayPal. Stripe sends email updates about the progress of all requests, and the current status is also reflected on the Payment Method Settings page.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

[Payment Method Settings page](https://dashboard.stripe.com/settings/payment_methods)

The following Connect charges types, typically used by online marketplaces, are available to businesses using PayPal.

[Connect charges](/connect/charges)

## Get started

Add PayPal and other payment methods from the Stripe Dashboard without making updates to your code. For each customer, Stripe determines the list of supported payment methods most likely to drive conversion. Learn how to accept PayPal and other payment methods automatically with Checkout or Elements. To accept PayPal and other payment methods without any code, use Payment Links.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

[accept PayPal and other payment methods automatically](/payments/accept-a-payment)

[Payment Links](/payment-links)

When you’re ready to go live, follow the steps to activate PayPal payments.

[activate PayPal payments](/payments/paypal/connect-your-paypal-account)

## Disputed payments

Customers must authenticate payments with their PayPal accounts, helping to reduce the risk of fraud or unrecognized payments. However, customers can still dispute transactions after they complete payment. Some common reasons for disputes are customers determining that items weren’t as described, or not receiving items at all. You can submit evidence to contest a dispute directly from the Stripe Dashboard.

Learn how to manage PayPal disputes in the Dashboard.

[manage PayPal disputes](/payments/paypal/disputed-payments)

For certain dispute types, PayPal enables you communicate directly to customers to try resolving the dispute. Contacting customers directly must be handled through the PayPal dashboard, and not the Stripe Dashboard.

## Refunds

PayPal payments can be refunded up to 180 days after the original payment. Stripe uses either your Stripe balance or your PayPal balance to refund the payment, depending on the settlement preference you selected.

[settlement preference you selected](/payments/paypal/choose-settlement-preference)

You can use the Stripe Dashboard or API to initiate refund requests, as with other payment methods. If you choose to settle funds to Stripe, refunds will be withdrawn from the funds available in your Stripe account. If you choose to settle funds to PayPal, refunds funded using your PayPal balance or any other funding source available on your PayPal account.

## Reporting

PayPal fees are included in the Less fees sections of Balance and Balance Activity reports. PayPal fees aren’t included in your tax invoice from Stripe. You can access these documents from your PayPal dashboard.

[Balance and Balance Activity reports](https://dashboard.stripe.com/reports/balance)

[tax invoice from Stripe](https://dashboard.stripe.com/settings/documents)

## Seller protection

PayPal’s Seller Protection program offers coverage for sellers under eligible transactions. It includes scenarios such as unauthorized transactions or buyers’ claims of non-receipt of item. For more information on the Seller Protection program and eligibility, visit PayPal Seller Protection.

[PayPal Seller Protection](https://www.paypal.com/uk/legalhub/seller-protection)

## Prohibited business categories

In addition to the business categories restricted from using Stripe overall, PayPal requires pre-approval to accept payments for certain services. Refer to the PayPal Acceptable Use Policy for details.

[PayPal Acceptable Use Policy](https://www.paypal.com/us/legalhub/acceptableuse-full)

## Minimum and maximum charge amounts

PayPal doesn’t have a minimum charge amount, but Stripe enforces the same minimum and maximum charge amounts for PayPal as for other payment methods.

[minimum and maximum charge amounts](/currencies#minimum-and-maximum-charge-amounts)
