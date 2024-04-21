# Amazon Pay payments

Amazon Pay is a wallet payment method that lets your customers check out the same way as on Amazon.com.

[Amazon Pay](https://pay.amazon.com/)

When customers select Amazon Pay as their payment method, Stripe redirects them to Amazon’s website, where they can check out using the shipping and payment information stored in their Amazon account. After completing the payment, Amazon redirects them back to your website.

- Customer locationsUnited States

Customer locations

United States

- Presentment currencyUSD

Presentment currency

USD

- Payment confirmationCustomer-initiated

Payment confirmation

Customer-initiated

- Payment method familyWallet

Payment method family

Wallet

- Recurring paymentsYes

Recurring payments

Yes

- Payout timingStandard payout timing applies

Payout timing

Standard payout timing applies

- Connect supportYes

Connect support

Yes

- Dispute supportYes

Dispute support

Yes

- Refunds / Partial refundsYes / yes

Refunds / Partial refunds

Yes / yes

## Payment flow

## Get started

You don’t actually have to integrate Amazon Pay and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

The following Stripe products also support adding Amazon Pay from the Dashboard:

- Payment Links

[Payment Links](/payment-links)

If your integration requires manually listing payment methods, learn how to manually configure Amazon Pay as a payment.

[manually configure Amazon Pay as a payment](/payments/amazon-pay/accept-a-payment)

[Refunds](#refunds)

## Refunds

Amazon Pay supports partial or full refunds for up to 90 days after the original purchase, and processes them asynchronously. After Stripe initiates a refund, Amazon Pay issues the refund to the customer’s original form of payment. We notify you of the final refund status using the charge.refund.updated webhook event. When a refund succeeds, the Refund object’s status transitions to succeeded. In the rare instance that a refund fails, the Refund object’s status transitions to failed and we return the amount to your Stripe balance. You then need to arrange an alternative way to provide your customer with a refund.

[webhook](/webhooks)

[Refund](/api/refunds/object)

[Disputed payments](#disputed-payments)

## Disputed payments

Customers must authenticate Amazon Pay payments by logging into their Amazon account. This requirement helps reduce the risk of fraud or unrecognized payments.

Customers have up to 240 calendar days from the date of purchase to file a dispute. The dispute process works like this:

- After the customer initiates a dispute, Stripe notifies you through email, the Stripe Dashboard, and an API charge.dispute.created event (if your integration is set up to receive webhooks).

After the customer initiates a dispute, Stripe notifies you through email, the Stripe Dashboard, and an API charge.dispute.created event (if your integration is set up to receive webhooks).

[webhooks](/webhooks)

- Stripe holds back the disputed amount from your balance until Amazon resolves the dispute.

Stripe holds back the disputed amount from your balance until Amazon resolves the dispute.

- Stripe requests that you upload compelling evidence that you fulfilled the purchase order using the Stripe Dashboard. This evidence can include:A received return confirmation (for shipped goods returned from the customer to you)The tracking IDThe shipping dateA record of purchase for intangible goods, such as IP address or email receiptA record of purchase for services or physical goods, such as phone number or proof of receipt

Stripe requests that you upload compelling evidence that you fulfilled the purchase order using the Stripe Dashboard. This evidence can include:

[using the Stripe Dashboard](/disputes/responding#respond)

- A received return confirmation (for shipped goods returned from the customer to you)

- The tracking ID

- The shipping date

- A record of purchase for intangible goods, such as IP address or email receipt

- A record of purchase for services or physical goods, such as phone number or proof of receipt

- This information helps Amazon determine if a dispute is valid or if it should be rejected. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 10 calendar days. Amazon Pay makes a decision within 90 calendar days of evidence submission. If Amazon resolves the dispute with you winning, Stripe returns the disputed amount to your Stripe balance. If Amazon rules in favor of the customer, the balance charge becomes permanent.

This information helps Amazon determine if a dispute is valid or if it should be rejected. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 10 calendar days. Amazon Pay makes a decision within 90 calendar days of evidence submission. If Amazon resolves the dispute with you winning, Stripe returns the disputed amount to your Stripe balance. If Amazon rules in favor of the customer, the balance charge becomes permanent.

If you prefer to handle disputes programmatically, you can respond to disputes using the API.

[respond to disputes using the API](/disputes/api)

## Supported currencies

You can create Amazon Pay payments in the currencies that map to your country. The default local currency for Amazon Pay is usd and customers also see their purchase amount in usd.

[Available payment methods](#available-payment-methods)

## Available payment methods

Use Amazon Pay to store card credentials. They support the following alternative payment methods:

## See also

Accept a payment with Amazon Pay

[Accept a payment with Amazon Pay](/payments/amazon-pay/accept-a-payment)
