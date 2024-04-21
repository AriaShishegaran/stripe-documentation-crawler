# Alma paymentsBeta

[privacy policy](https://stripe.com/privacy)

Alma is a Buy Now, Pay Later payment method available in France that gives your customers flexibility.

[Alma](https://almapay.com/)

When customers select Alma as their payment method, Stripe redirects them to Alma’s website, where they get the ability to choose between 2, 3, or 4 installments to complete their purchase. You are paid immediately.

- Customer locationsFrance

Customer locations

France

- Presentment currencyEUR

Presentment currency

EUR

- Payment confirmationCustomer-initiated

Payment confirmation

Customer-initiated

- Payment method familyBuy Now, Pay Later

Payment method family

Buy Now, Pay Later

- Recurring paymentsNo

Recurring payments

No

- Payout timingT+3

Payout timing

T+3

- Connect supportConnected accounts that use the Stripe Dashboard

Connect support

Connected accounts that use the Stripe Dashboard

- Dispute supportYes

Dispute support

Yes

- Refunds / Partial refundsYes / yes

Refunds / Partial refunds

Yes / yes

## Payment flow

## Get started

You don’t actually have to integrate Alma and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

The following Stripe products also support adding Alma from the Dashboard:

- Payment Links

[Payment Links](/payment-links)

If your integration requires manually listing payment methods, learn how to manually configure Alma as a payment.

[manually configure Alma as a payment](/payments/alma/accept-a-payment)

## Prohibited business categories

In addition to the industry and business categories listed in Prohibited and restricted business, Alma prohibits the following categories:

[Prohibited and restricted business](https://stripe.com/restricted-businesses)

- Sole proprietorships or individual accounts

- Business to Business Services

- Educational services

- Professional services (including, but not limited to, legal, consulting, and accounting)

- Transportation services

- Travel services

- Telecommunication services and utilities

- Veterinary services

See a full list of prohibited activities. Even if an activity isn’t listed as prohibited, your business might still be ineligible for Alma due to risk-related reasons.

[full list of prohibited activities](https://help.almapay.com/hc/en-gb/articles/360006779359-Which-activities-are-not-eligible-for-payment-with-Alma)

[Refunds](#refunds)

## Refunds

Alma supports full and partial refunds. The refund period is up to 180 days after the purchase. Refunds for Alma payments are asynchronous and take up to 5 minutes to complete. We will notify you of the final refund status using the charge.refund.updated webhook event. When a refund succeeds, the Refund object’s status transitions to succeeded. In the rare instance that a refund fails, the Refund object’s status will transition to failed and we will return the amount to your Stripe balance. You will then need to arrange an alternative way of providing your customer with a refund.

[webhook](/webhooks)

[Refund](/api/refunds/object)

[Disputed payments](#disputed-payments)

## Disputed payments

Customers must authenticate Alma payments by logging into their Alma account. This requirement helps reduce the risk of fraud or unrecognized payments. While Alma covers losses incurred from customer fraud, Alma might contact you and request to stop or pause shipment before incurring any losses. Please comply promptly with these requests.

Customers have up to 120 calendar days from the date of purchase to file a dispute. The dispute process works like this:

- After the customer initiates a dispute, Stripe notifies you through email, the Stripe Dashboard, and an API charge.dispute.created event (if your integration is set up to receive webhooks).

After the customer initiates a dispute, Stripe notifies you through email, the Stripe Dashboard, and an API charge.dispute.created event (if your integration is set up to receive webhooks).

[webhooks](/webhooks)

- Stripe holds back the disputed amount from your balance until Alma resolves the dispute.

Stripe holds back the disputed amount from your balance until Alma resolves the dispute.

- Stripe requests that you upload compelling evidence that you fulfilled the purchase order using the Stripe Dashboard. This evidence can include:A received return confirmation (for shipped goods returned from the customer to you)The tracking IDThe shipping dateA record of purchase for intangible goods, such as IP address or email receiptA record of purchase for services or physical goods, such as phone number or proof of receipt

Stripe requests that you upload compelling evidence that you fulfilled the purchase order using the Stripe Dashboard. This evidence can include:

[using the Stripe Dashboard](/disputes/responding#respond)

- A received return confirmation (for shipped goods returned from the customer to you)

- The tracking ID

- The shipping date

- A record of purchase for intangible goods, such as IP address or email receipt

- A record of purchase for services or physical goods, such as phone number or proof of receipt

- This information helps Alma determine if a dispute is valid or if it should be rejected. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 14 calendar days. Alma makes a decision within 25 calendar days of evidence submission. If Alma resolves the dispute with you winning, Stripe returns the disputed amount to your Stripe balance. If Alma rules in favor of the customer, the balance charge becomes permanent.

This information helps Alma determine if a dispute is valid or if it should be rejected. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 14 calendar days. Alma makes a decision within 25 calendar days of evidence submission. If Alma resolves the dispute with you winning, Stripe returns the disputed amount to your Stripe balance. If Alma rules in favor of the customer, the balance charge becomes permanent.

Alma requires merchants to maintain reasonable fraud and dispute rates. Increases to your fraud and dispute rates might result in losing access to Alma.

If you prefer to handle disputes programmatically, you can respond to disputes using the API.

[respond to disputes using the API](/disputes/api)

## Supported currencies

You can create Alma payments in the currencies that map to your country. The default local currency for Alma is eur and customers also see their purchase amount in eur.

## See also

Accept a payment with Alma

[Accept a payment with Alma](/payments/alma/accept-a-payment)
