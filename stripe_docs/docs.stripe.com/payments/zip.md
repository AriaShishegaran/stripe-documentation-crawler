# Zip payments

Zip gives your customers in Australia and the US (beta) a way to split purchases over a series of payments.

[Zip](https://zip.co/)

Customers who elect to pay with Zip are redirected to the Zip site, where they authorize the payment by agreeing to the terms of a payment plan. After payment terms acceptance, Zip transfers funds to your Stripe account up front and your customer repays Zip over time according to their agreement terms.

[authorize](/payments/payment-methods#customer-actions)

- Customer locationsAustralia, United States Beta

Customer locations

Australia, United States Beta

- Presentment currencyAUD, USD Beta

Presentment currency

AUD, USD Beta

- Payment confirmationCustomer-authenticated

Payment confirmation

Customer-authenticated

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

- Dispute supportYes

Dispute support

Yes

- Refunds / Partial refundsYes / yes

Refunds / Partial refunds

Yes / yes

[privacy policy](https://stripe.com/privacy)

## Payment flow

Below is a demonstration of the Zip payment flow from your checkout page:

This demo shows the customer experience when using Zip.

## Get started

You don’t actually have to integrate Zip and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

The following Stripe products also support adding Zip from the Dashboard:

- Payment Links

[Payment Links](/payment-links)

If you prefer to manually list payment methods, learn how to manually configure Zip as a payment.

[manually configure Zip as a payment](/payments/zip/accept-a-payment)

## Payment options

Available payment options vary by country. In Australia, Zip offers Zip Pay and Zip Money, which have flexible repayment plans. In the US, Zip offers a Pay in 4 plan that splits repayment into 4 installments over 6 weeks. Regardless of the payment option selected, Stripe makes the full amount of the funds (minus fees) available to you upfront and Zip collects the purchase amount from your customer, who repays Zip directly.

- Zip Pay: A line of credit up to 1000 AUD. Customers can select their repayment frequency, either weekly, bi-weekly, or monthly. Zip charges customers a monthly account fee, but waives it if the balance is repaid in full.

Zip Pay: A line of credit up to 1000 AUD. Customers can select their repayment frequency, either weekly, bi-weekly, or monthly. Zip charges customers a monthly account fee, but waives it if the balance is repaid in full.

[Zip Pay](https://zip.co/au/zip-pay)

- Zip Money: A line of credit between 1000 AUD and 5000 AUD, and potentially up to 50,000 AUD. Customers can adjust the installment period with no interest for 3-36 months, depending on the retailer. If you want to offer your customers interest-free repayment periods longer than 3 months, or credit limits higher than 5000 AUD, contact Stripe support. Zip charges customers an account establishment fee and a monthly fee, but waives the monthly fee when the account balance is zero.

Zip Money: A line of credit between 1000 AUD and 5000 AUD, and potentially up to 50,000 AUD. Customers can adjust the installment period with no interest for 3-36 months, depending on the retailer. If you want to offer your customers interest-free repayment periods longer than 3 months, or credit limits higher than 5000 AUD, contact Stripe support. Zip charges customers an account establishment fee and a monthly fee, but waives the monthly fee when the account balance is zero.

[Zip Money](https://zip.co/au/zip-money)

[contact Stripe support](https://support.stripe.com/contact/email?question=other&topic=payment_apis&subject=ZipPayments)

- Zip pay-in-4: Customers pay for purchases over 4 installments interest-free. Zip adds a finance charge based on the purchase amount, and splits the total amount into 4 equal installments. Customers pay the first installment at time of purchase, then make the 3 remaining repayments at 2-week intervals.

Zip pay-in-4: Customers pay for purchases over 4 installments interest-free. Zip adds a finance charge based on the purchase amount, and splits the total amount into 4 equal installments. Customers pay the first installment at time of purchase, then make the 3 remaining repayments at 2-week intervals.

[Zip pay-in-4](https://zip.co/us/how-it-works)

The following table lists total transaction limits, currency and payment options by country:

* If the purchase amount is greater than their available credit, customers can pay the rest with cards up front.

## Prohibited business categories

For information about whether your account is eligible to accept Zip payments, navigate to your Payment methods settings.

[Payment methods settings](https://dashboard.stripe.com/settings/payments)

In addition to standard Stripe business restrictions, the following business categories are prohibited from accepting Zip payments through Stripe:

[Stripe business restrictions](https://stripe.com/legal/restricted-businesses)

- Charity

- Insurance

For detailed information about Zip business restrictions, see the Zip help.

[Zip help](https://help.zip.co/hc/en-us/articles/6544802536591)

## Adding Zip branding to your website

Zip works closely with partners to constantly test and enhance the way Zip is presented to customers. Their integration and marketing requirements aim to improve customer experience and benefit businesses by converting more browsers into shoppers and increasing average basket sizes. Use their Best Practice Integration guide to increase awareness of your Zip offering.

[Best Practice Integration](https://developers.zip.co/docs/best-practice-implementation)

Zip also provides static visual assets and branding guidelines. You must use and display Zip’s branding according to this guidance.

[static visual assets and branding guidelines](https://developers.zip.co/docs/zip-marketing-assets)

## Disputes and fraud

Customers must authenticate Zip payments by logging into their Zip account. This requirement helps reduce the risk of fraud or unrecognized payments. While Zip covers losses incurred from customer fraud, Stripe might contact you on behalf of Zip and request to stop or pause shipment before any losses are incurred—make sure you comply promptly with these requests. You must use reasonable care to detect fraud or unauthorised transactions, and minimise disputes and unauthorized use of Zip payments.

Customers can dispute Zip payments in certain cases—for example, if they receive faulty goods or don’t receive them at all. Customers have up to 180 calendar days from the date of purchase to file a dispute. You must cooperate during Zip’s dispute process. Zip will investigate disputes in line with its disputes process. The dispute process works like this:

Zip requires customers to contact you directly to resolve the dispute first. If this doesn’t resolve it, the customer can initiate a dispute case with Zip after 14 days from the date of purchase, and Stripe notifies you using:

- Email notification

- Stripe Dashboard

- An API charge.dispute.created event (if your integration is set up to receive webhooks)

[webhooks](/webhooks)

Stripe holds back the disputed amount and fee of 15 AUD from your balance until Zip resolves the dispute, which can take up to 3 months after you submit the evidence. That said, Zip usually resolves the dispute within 30 days.

Stripe requests that you upload compelling evidence that you fulfilled the purchase order using the Stripe Dashboard. This evidence can include:

[using the Stripe Dashboard](/disputes/responding#respond)

- Received return confirmation (for shipped goods returned from the customer to you)

- Tracking ID

- Shipping date

- Record of purchase for intangible goods, such as an IP address or email receipt

- Record of purchase for services or physical goods, such as a phone number or proof of receipt

If you would rather handle disputes programmatically, you can respond to disputes using the API.

[respond to disputes using the API](/disputes/api)

This information helps Zip determine if a dispute is valid or if they need to reject it. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 9 business days. If Zip resolves the dispute with you winning, Stripe returns the disputed amount and dispute fee to your Stripe balance. If Zip rules in favor of the customer, the balance charge becomes permanent.

## Refunds

Payments made with Zip can only be submitted for refund within 180 calendar days from the date of the original charge. After 180 days, it’s no longer possible to refund the charge.

## Additional requirements

You acknowledge that:

- Zip decides if customers can use Zip for purchases and has the sole right to receive payment from Zip customers. Stripe acquires those purchases for you and settles the funds to you.

- You must not process a Zip transaction unless delivery will be completed within 60 days.

- You can’t give return credits in cash unless required by law.

- You can’t impose fees or higher prices for Zip purchases (that is, no surcharging).

- You can’t split a Zip transaction into multiple charges unless (i) the balance of the amount due is paid in cash or check or (ii) the goods or services are delivered at a later date and one charge is the deposit and the second is the balance payment at delivery.

- You must retain information about a Zip transaction for at least 18 months after the transaction.

- If a customer has questions about how Zip handles their information, you will refer them to Zip’s privacy policy.

- Zip can refuse or suspend transactions where (i) the transaction involves you reselling Zip services or (ii) you haven’t retained information about the transaction for at least 18 months after the transaction.
