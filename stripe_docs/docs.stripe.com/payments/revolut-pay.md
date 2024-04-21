# Revolut Pay payments

Revolut Pay, developed by Revolut, a global finance app, is a digital wallet payment method. Revolut Pay uses the customer’s stored balance or cards to fund the payment, and offers the option for non-Revolut customers to save their details after their first purchase.

[Revolut](https://www.revolut.com/business/revolut-pay/)

When customers select Revolut Pay as their payment method, Stripe redirects them to Revolut Pay’s website, where they have to authenticate with their account details or checkout as a first time user. After authenticating, Revolut Pay redirects customers back to your website.

- Customer locationsUK and EU customers

Customer locations

UK and EU customers

- Presentment currencyEUR, GBP

Presentment currency

EUR, GBP

- Payment confirmationCustomer-initiated

Payment confirmation

Customer-initiated

- Payment method familyDigital wallet

Payment method family

Digital wallet

- Recurring paymentsRequires approval

Recurring payments

Requires approval

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

[privacy policy](https://stripe.com/privacy)

## Payment flow

## Get started

You don’t actually have to integrate Revolut Pay and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

The following Stripe products also support adding Revolut Pay from the Dashboard:

- Invoicing

[Invoicing](/invoicing/quickstart-guide)

- Payment Links

[Payment Links](/payment-links)

- Subscriptions

[Subscriptions](/billing/subscriptions/overview)

If your integration requires manually listing payment methods, learn how to manually configure Revolut Pay as a payment.

[manually configure Revolut Pay as a payment](/payments/revolut-pay/accept-a-payment)

Check out the Revolut Pay sample on GitHub.

[sample on GitHub](https://github.com/stripe-samples/accept-a-payment)

[Refunds](#refunds)

## Refunds

Revolut Pay supports full and partial refunds. The refund period is up to 180 days after the purchase. Refunds for Revolut Pay payments are asynchronous and take up to 5 minutes to complete. We notify you of the final refund status using the charge.refund.updated webhook event. When a refund succeeds, the status of the Refund object transitions to succeeded. If a refund fails, the status of the Refund object transitions to failed and we return the amount to your Stripe balance. You then need to arrange an alternative way of providing a refund.

[webhook](/webhooks)

[Refund object](/api/refunds/object)

[Disputed payments](#disputed-payments)

## Disputed payments

Customers must authenticate Revolut Pay payments by logging into their Revolut account. This requirement helps reduce the risk of fraud or unrecognized payments. With Revolut’s Buyer Protection Policy, customers can file a dispute, which can result in a chargeback and funds being withdrawn from your Stripe account.

[Revolut’s Buyer Protection Policy](https://www.revolut.com/legal/buyer-protection-policy/)

Customers have up to 120 calendar days from the date of purchase to file a dispute. The dispute process works like this:

- After the customer initiates a dispute, Stripe notifies you through email, the Stripe Dashboard, and an API charge.dispute.created event (if your integration is set up to receive webhooks).

After the customer initiates a dispute, Stripe notifies you through email, the Stripe Dashboard, and an API charge.dispute.created event (if your integration is set up to receive webhooks).

[webhooks](/webhooks)

- Stripe holds back the disputed amount from your balance until Revolut resolves the dispute.

Stripe holds back the disputed amount from your balance until Revolut resolves the dispute.

- Stripe requests that you upload compelling evidence that you fulfilled the purchase order using the Stripe Dashboard. This evidence can include:A received return confirmation (for shipped goods returned from the customer to you)The tracking IDThe shipping dateA record of purchase for intangible goods, such as IP address or email receiptA record of purchase for services or physical goods, such as phone number or proof of receipt

Stripe requests that you upload compelling evidence that you fulfilled the purchase order using the Stripe Dashboard. This evidence can include:

[using the Stripe Dashboard](/disputes/responding#respond)

- A received return confirmation (for shipped goods returned from the customer to you)

- The tracking ID

- The shipping date

- A record of purchase for intangible goods, such as IP address or email receipt

- A record of purchase for services or physical goods, such as phone number or proof of receipt

- This information helps Revolut determine if a dispute is valid or if they need to reject it. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 14 calendar days. Revolut makes a decision within 35 calendar days of evidence submission. If Revolut resolves the dispute in your favor, Stripe returns the disputed amount to your Stripe balance. If Revolut rules in favor of the customer, the balance charge becomes permanent.

This information helps Revolut determine if a dispute is valid or if they need to reject it. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 14 calendar days. Revolut makes a decision within 35 calendar days of evidence submission. If Revolut resolves the dispute in your favor, Stripe returns the disputed amount to your Stripe balance. If Revolut rules in favor of the customer, the balance charge becomes permanent.

If you prefer to handle disputes programmatically, you can respond to disputes using the API.

[respond to disputes using the API](/disputes/api)

## Supported currencies

You can create Revolut Pay payments in the currencies that map to your country. Currently, we support gbp and eur. The default local currency for Revolut Pay UK customers is gbp and for other EU customers it’s eur.

## See also

- Accept a payment with Revolut Pay

[Accept a payment with Revolut Pay](/payments/revolut-pay/accept-a-payment)