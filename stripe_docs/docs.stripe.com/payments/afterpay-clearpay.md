# Afterpay and Clearpay payments

Afterpay is a global payment method that allows your customers to split purchases into 4 interest-free installments, or longer term interest-bearing monthly installments (US only).

To pay with Afterpay, customers are redirected to Afterpay’s site, where they authorize the payment by agreeing to the terms of a payment plan, then return to your website to complete the order. Afterpay offers payment options based on factors such as customer credit, prior account history, order amount, and the type of goods or services being underwritten. After payment acceptance, the full amount of the order (minus fees) is made available to your Stripe account upfront, and Afterpay collects the purchase amount from your customer, who repays Afterpay directly over time. For more information, see Payment options and limits.

[Payment options and limits](#collection-schedule)

- Customer locationsUnited States, Canada, United Kingdom, Australia, New Zealand

Customer locations

United States, Canada, United Kingdom, Australia, New Zealand

- Presentment currencyUSD, CAD, GBP, AUD, or NZD

Presentment currency

USD, CAD, GBP, AUD, or NZD

- Payment confirmationCustomer-initiated

Payment confirmation

Customer-initiated

- Payment method familyBuy Now, Pay Later

Payment method family

Buy Now, Pay Later

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

Afterpay and Clearpay only support domestic transactions, meaning you can only sell to customers in the same country as your business. If you’re using Dynamic payment methods, Stripe handles a customer’s payment method eligibility automatically. If you use payment_method_types, you must either configure your integration so that it only presents Afterpay and Clearpay to eligible customers, or use dynamic payment methods.

[Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods)

[payment_method_types](/api/payment_intents/object#payment_intent_object-payment_method_types)

## Payment flow

This demo shows the customer experience when using Afterpay.

## Get started

You don’t actually have to integrate Afterpay and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

Payment Links also supports adding Afterpay from the Dashboard.

[Payment Links](/payment-links)

If you prefer to manually list payment methods, learn how to manually configure Afterpay as a payment.

[manually configure Afterpay as a payment](/payments/afterpay-clearpay/accept-a-payment)

You can also let customers know Afterpay payments are available by including the Payment Method Messaging Element on your product, cart, and payment pages. We recommend adding a site messaging Element to help drive conversion.

[Payment Method Messaging Element](/payments/payment-method-messaging)

## Payment options and limits

Payment options vary by cart order size and country. In the US, Afterpay presents customers with Pay in 4, monthly installments, or both options. For all other markets, Afterpay presents customers with Pay in 4 only.

- Pay in 4: customers pay for purchases in four or fewer interest-free, bi-weekly payments over a 6 week term.

- Monthly installments: (US only) customers pay for purchases over a 6 or 12 month term that includes capped interest.

Afterpay collects the first installment from the customer immediately, and the next installment either 2 weeks or 1 month after, depending on the payment schedule. You can accept payments from customers in the same country that you registered your Stripe account. Payments must also match the local currency of the country.

The following table lists total transaction limits and installment schedules by country.

## Prohibited business categories

For more information about Afterpay eligibility for your account, navigate to your Payment methods settings.

[Payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

In addition to the categories of businesses restricted from using Stripe overall, the following categories are prohibited from using Afterpay.

[businesses restricted from using Stripe overall](https://stripe.com/restricted-businesses)

- Alcohol

- Donations

- Pre-orders

- NFTs

- B2B

For the complete list, see the terms of service.

[terms of service](https://stripe.com/afterpay-clearpay/legal#restricted-businesses)

## Adding Afterpay branding to your website

Let your customers know you accept payments with Afterpay by including the Payment Method Messaging Element on your product and cart pages.

[Payment Method Messaging Element](/payments/payment-method-messaging)

Afterpay also provides static visual assets and branding guidance. In AU, CA, NZ and the US, consumers know Afterpay as ‘Afterpay’. In the UK, they know it as ‘Clearpay’. Make sure you pick the right location (see the footer in the Afterpay documentation) so that you get the appropriate assets. For Clearpay, see the UK assets and branding guidance.

[visual assets and branding guidance](https://www.afterpay.com/retailer-resources)

[Afterpay documentation](https://www.afterpay.com/retailer-resources)

[UK assets and branding guidance](https://www.clearpay.co.uk/en-GB/retailer-resources)

## Disputed payments

Customers must authenticate Afterpay payments by logging into their Afterpay account. This requirement helps reduce the risk of fraud or unrecognized payments. Afterpay covers losses incurred from customer fraud or the inability to repay installments. However, Stripe might contact you on behalf of Afterpay and request to stop or pause a shipment before any losses are incurred. It’s important to comply promptly with these requests.

Customers can dispute Afterpay payments in certain cases—for example, if they don’t receive the goods they paid for. Customers have up to 120 calendar days from the date of purchase to file a dispute. The dispute process works like this:

After the customer initiates a dispute, Stripe notifies you using:

- Email

- The Stripe Dashboard

- An API charge.dispute.created event (if your integration is set up to receive webhooks)

[webhooks](/webhooks)

Stripe holds back the disputed amount from your balance until Afterpay resolves the dispute.

Stripe requests that you upload compelling evidence that you fulfilled the purchase order using the Stripe Dashboard. This evidence can include:

[using the Stripe Dashboard](/disputes/responding#respond)

- A received return confirmation (for shipped goods returned from the customer to you)

- The tracking ID

- The shipping date

- A record of purchase for intangible goods, such as IP address or email receipt

- A record of purchase for services or physical goods, such as phone number or proof of receipt

If you prefer to handle disputes programmatically, you can respond to disputes using the API.

[respond to disputes using the API](/disputes/api)

This information helps Afterpay determine if a dispute is valid or if they should reject it. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 14 calendar days. Afterpay makes a decision within 30 calendar days of evidence submission. If Afterpay resolves the dispute with you winning, Stripe returns the disputed amount to your Stripe balance. If Afterpay rules in favor of the customer, the balance charge becomes permanent.

## Refunds

You can refund Afterpay charges up to 120 days after the original payment. Refunds for Afterpay payments are asynchronous.

## Connect

You can use Stripe Connect with Afterpay to process payments on behalf of a connected account. Connect users can use Afterpay with the following charge types:

[Stripe Connect](/connect/overview)

[Connect](/connect)

- Direct

[Direct](/connect/direct-charges)

- Destination

[Destination](/connect/destination-charges)

- Separate Charges and Transfers

[Separate Charges and Transfers](/connect/separate-charges-and-transfers)

Stripe and Afterpay rely on merchant category codes (MCC) to determine eligibility of the connected accounts against the Afterpay prohibited business categories. Make sure that you set correct MCCs for your connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe.

[prohibited business categories](#prohibited-business-categories)

[correct MCCs](/connect/setting-mcc)
