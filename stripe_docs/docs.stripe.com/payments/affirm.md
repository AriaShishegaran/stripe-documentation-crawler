# Affirm payments

Affirm is a popular payment method in the US and Canada that gives your customers a way to split purchases over a series of payments. Pay in 4 interest-free installments or in monthly installments of up to 36 months.

[Affirm](https://www.affirm.com/)

To pay with Affirm, customers are redirected to Affirm’s site, where they authorize the payment by agreeing to the terms of a payment plan, then return to your website to complete the order. Affirm offers payment options based on factors such as customer credit, prior account history, order amount, and the type of goods or services being underwritten. After payment acceptance, the full amount of the order (minus fees) is made available to your Stripe account upfront, and Affirm collects the purchase amount from your customer, who repays Affirm directly over time.

[authorize](/payments/payment-methods#customer-actions)

- Customer locationsUnited States, Canada

Customer locations

United States, Canada

- Presentment currencyUSD or CAD

Presentment currency

USD or CAD

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

Affirm only supports domestic transactions, meaning you can only sell to customers in the same country as your business. If you’re using Dynamic payment methods, Stripe handles a customer’s payment method eligibility automatically. If you use payment_method_types, you must either configure your integration so that it only presents Affirm to eligible customers, or use dynamic payment methods.

[Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods)

[payment_method_types](/api/payment_intents/object#payment_intent_object-payment_method_types)

## Payment flow

This demo shows the customer experience when using Affirm.

## Get started

You don’t actually have to integrate Affirm and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

Payment Links also supports adding Affirm from the Dashboard.

[Payment Links](/payment-links)

If you prefer to manually list payment methods, learn how to manually configure Affirm as a payment.

[manually configure Affirm as a payment](/payments/affirm/accept-a-payment)

You can also let customers know Affirm payments are available by including the Payment Method Messaging Element on your product, cart, and payment pages. We recommend adding a site messaging Element to help drive conversion.

[Payment Method Messaging Element](/payments/payment-method-messaging)

## Payment options

Depending on the cart order size, Affirm presents customers with Pay in 4, monthly installments, or both.

- Pay in 4: customers pay for purchases in four or fewer interest-free, bi-weekly payments over an 8 week term. Available for cart sizes between $50 and $250*.

- Monthly Installments: customers pay for purchases over a longer term of up to 36 months, which might include interest. Available for cart sizes between 100 USD and 30,000 USD*.

* Term lengths and cart ranges are determined by Affirm and might change at their discretion.

## Prohibited and restricted business categories

For more information about Affirm eligibility for your account, navigate to your Payment methods settings.

[Payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

In addition to the categories of businesses restricted from using Stripe overall, the following categories are prohibited from using Affirm.

[businesses restricted from using Stripe overall](https://stripe.com/restricted-businesses)

- Business to business services

- Home improvement services, including contractors and special trade contractors

- Titled goods and auto loans, including entire cars, boats, and other motor vehicles (parts and services allowed)

- Professional services (including legal, consulting, and accounting)

- NFTs

- Pre-orders

Healthcare services are approved to use Affirm, however they’re subject to additional requirements. For the complete list of prohibited businesses and additional requirements, see the Affirm Payment Terms.

[the Affirm Payment Terms](https://stripe.com/legal/affirm)

## Adding Affirm branding to your website

Use the Payment Method Messaging Element on your site to let customers know that you offer Affirm ahead of checkout. You must comply with Affirm’s marketing compliance guides and use the Affirm toolkit that relates to the Affirm payment options you offer your customers.

[Payment Method Messaging Element](/payments/payment-method-messaging)

[marketing compliance guides](https://docs.affirm.com/developers/docs/compliance_and_guidelines)

[toolkit](https://businesshub.affirm.com/hc/en-us/articles/10653174159636-Affirm-Marketing-Compliance-Guides)

## Refunds

Returns are subject to the return policy that you display on your website. If your business allows returns, you can refund Affirm transactions as you normally would for card payments. Affirm supports partial or full refunds for up to 120 days after the original purchase, and processes them asynchronously. After Stripe initiates a refund, Affirm pauses the customer’s payment plan and refunds the customer for any payments they’ve already made, minus any interest paid. Stripe doesn’t credit back the processing fees in the event of a refund.

[refund](/refunds)

## Disputes and fraud

Customers must authenticate Affirm payments by logging into their Affirm account. This requirement helps reduce the risk of fraud or unrecognized payments. While Affirm covers losses incurred from customer fraud, Stripe might contact you on behalf of Affirm and request to stop or pause shipment before any losses are incurred. Comply promptly with these requests.

Customers can dispute Affirm payments in certain cases—for example, if they receive faulty goods or don’t receive them at all. Customers have up to 60 calendar days from the date of purchase to file a dispute. The dispute process works like this:

After the customer initiates a dispute, Stripe notifies you using:

- Email notification

- Stripe Dashboard

- An API charge.dispute.created event (if your integration is set up to receive webhooks)

[webhooks](/webhooks)

Stripe holds back the disputed amount from your balance until Affirm resolves the dispute, which can take a maximum of 30 calendar days from dispute creation.

Stripe requests that you upload compelling evidence that you fulfilled the purchase order using the Stripe Dashboard. This evidence can include:

[using the Stripe Dashboard](/disputes/responding#respond)

- Received return confirmation (for shipped goods returned from the customer to you)

- Tracking ID

- Shipping date

- Record of purchase for intangible goods, such as IP address or email receipt

- Record of purchase for services or physical goods, such as phone number or proof of receipt

If you would rather handle disputes programmatically, you can respond to disputes using the API.

[respond to disputes using the API](/disputes/api)

This information helps Affirm determine if a dispute is valid or if they should reject it. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 15 calendar days. Affirm makes a decision within 15 calendar days of evidence submission. If Affirm resolves the dispute with you winning, Stripe returns the disputed amount to your Stripe balance. If Affirm rules in favor of the customer, the balance charge becomes permanent.

## Customer emails

After a customer uses Affirm to make a purchase, Affirm emails the customer with updates. These updates include information about the following events:

- Affirm confirms or denies a loan. Affirms sends these updates when the payment_intent succeeds or when Affirm denies the loan.

- A refund completes.

[refund](/refunds)

- A payment is cancelled, which results in Affirm cancellling the loan.

- The customer completes a payment as part of the payment plan.

Affirm only sends email updates about Affirm’s loan issuance to your customer. You should continue to separately send emails related to the purchase such as order confirmation and shipping updates.

## Connect

You can use Stripe Connect with Affirm to process payments on behalf of a connected account. Connect users can use Affirm with the following charge types:

[Stripe Connect](/connect)

[Connect](/connect)

- Direct

[Direct](/connect/direct-charges)

- Destination

[Destination](/connect/destination-charges)

- Separate Charges and Transfers

[Separate Charges and Transfers](/connect/separate-charges-and-transfers)

Make sure you request the affirm_payments capability and it’s set to active on both your platform account and any connected accounts you want to enable.

[request](/connect/account-capabilities#requesting-unrequesting)

Stripe and Affirm rely on merchant category codes (MCC) to determine eligibility of the connected accounts against the Affirm prohibited business categories. Make sure that you set correct MCCs for your connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe.

[prohibited business categories](/payments/affirm#prohibited-and-restricted-business-categories)

[correct MCCs](/connect/setting-mcc)

The charge type of Connect payments might change the merchant name that appears on Affirm’s website or app during the redirect. The merchant of record determines the Stripe account authorized to create payments with a particular PaymentMethod.

[charge type](/connect/charges)

[PaymentMethod](/api/payment_methods/object)
