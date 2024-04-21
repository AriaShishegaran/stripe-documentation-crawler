# BLIK payments

BLIK is a single use payment method that requires customers to authenticate their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form.

[single use](/payments/payment-methods#usage)

[authenticate](/payments/payment-methods#customer-actions)

The bank sends a push notification to your customer’s mobile phone asking to authorize the payment inside their banking application. The BLIK code is valid for 2 minutes; customers have 60 seconds to authorize the payment after starting a payment. After 60 seconds, it times out and they must request a new BLIK code. Customers typically approve BLIK payments in less than 10 seconds.

- Customer locationsPoland

Customer locations

Poland

- Presentment currencyPLN

Presentment currency

PLN

- Payment confirmationCustomer-initiated

Payment confirmation

Customer-initiated

- Payment method familyAuthenticated bank debit

Payment method family

Authenticated bank debit

- Recurring paymentsNo

Recurring payments

No

- Payout timingStandard payout timing applies

Payout timing

Standard payout timing applies

- Connect supportYes

Connect support

Yes

- Refunds / Partial refundsYes / yes

Refunds / Partial refunds

Yes / yes

- Dispute supportYes

Dispute support

Yes

## Payment flow

Customer selects BLIK at checkout.

Customer is directed to their mobile banking app to generate a 6-digit code.

Customer puts the code into the checkout.

Customer is notified that payment is complete.

## Get started

You don’t actually have to integrate BLIK and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

If you prefer to manually list payment methods, learn how to manually configure BLIK as a payment.

[manually configure BLIK as a payment](/payments/blik/accept-a-payment)

## Disputed payments

BLIK has a claims process that allows transaction disputes. Customers can open disputes for cases of suspected fraud, double payments, or a difference between an order and a transaction amount.

After the customer initiates a dispute, Stripe notifies you using:

- Email

- The Stripe Dashboard

- An API charge.dispute.created event (if your integration is set up to receive webhooks)

[webhooks](/webhooks)

Stripe holds back the disputed amount from your balance until BLIK resolves the dispute.

We request that you upload compelling evidence proving that you fulfilled the purchase order using the Stripe Dashboard. This evidence can include the:

[using the Stripe Dashboard](/disputes/responding#respond)

- Tracking ID

- Shipping date

- Record of purchase for intangible goods, such as IP address or email receipt

- Record of purchase for services or physical goods, such as phone number or proof of receipt

- Record of refund (for purchase you have already refunded)

To handle disputes programmatically, respond to disputes using the API.

[respond to disputes using the API](/disputes/api)

This information helps BLIK determine if a dispute is valid. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 12 calendar days. If BLIK resolves the dispute with you winning, we return the disputed amount to your Stripe balance. If BLIK rules in favor of the customer, the balance charge becomes permanent.

## Refunds

BLIK supports full and partial refunds. Depending on the bank, refunds are processed immediately or within a couple of hours.

## Connect

If you use Connect, you must consider the following before you enable and use BLIK.

[Connect](/connect)

Set the blik_payments capability to active on your platform account, and on any connected accounts you want to enable BLIK for. You can also request more account capabilities.

[request more account capabilities](/connect/account-capabilities#requesting-unrequesting)

The charge type of Connect payments might change the default statement descriptor and the merchant name that appears on the customer’s banking application and confirmation emails.

[charge type](/connect/charges)
