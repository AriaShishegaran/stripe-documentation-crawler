htmlZip payments | Stripe Documentation[Skip to content](#main-content)Zip[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fzip)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fzip)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Buy now, pay later](/docs/payments/buy-now-pay-later)# Zip payments

Learn about Zip, a popular payment method in Australia and the US for customers to buy now and pay later.Zip gives your customers in Australia and the US (beta) a way to split purchases over a series of payments.

Customers who elect to pay with Zip are redirected to the Zip site, where they authorize the payment by agreeing to the terms of a payment plan. After payment terms acceptance, Zip transfers funds to your Stripe account up front and your customer repays Zip over time according to their agreement terms.

Payment method propertiesCountry availability- Customer locations

Australia, United States Beta


- Presentment currency

AUD, USD Beta


- Payment confirmation

Customer-authenticated


- Payment method family

Buy Now, Pay Later


- Recurring payments

No


- Payout timing

Standard


- Connect support

Yes


- Dispute support

Yes


- Refunds / Partial refunds

Yes / yes



Interested in getting early access to Zip in the US?In the United States, Zip is currently limited to beta users. If you're interested in trying it out, enter your email address below.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.## Payment flow

Below is a demonstration of the Zip payment flow from your checkout page:

This demo shows the customer experience when using Zip.

## Get started

You don’t actually have to integrate Zip and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- [Checkout](/checkout/quickstart): Our prebuilt, hosted checkout page.
- [Elements](/payments/quickstart): Our drop-in UI components.

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

### Other payment products

The following Stripe products also support adding Zip from the Dashboard:

- [Payment Links](/payment-links)

If you prefer to manually list payment methods, learn how to manually configure Zip as a payment.

## Payment options

Available payment options vary by country. In Australia, Zip offers Zip Pay and Zip Money, which have flexible repayment plans. In the US, Zip offers a Pay in 4 plan that splits repayment into 4 installments over 6 weeks. Regardless of the payment option selected, Stripe makes the full amount of the funds (minus fees) available to you upfront and Zip collects the purchase amount from your customer, who repays Zip directly.

- Zip Pay: A line of credit up to 1000 AUD. Customers can select their repayment frequency, either weekly, bi-weekly, or monthly. Zip charges customers a monthly account fee, but waives it if the balance is repaid in full.


- Zip Money: A line of credit between 1000 AUD and 5000 AUD, and potentially up to 50,000 AUD. Customers can adjust the installment period with no interest for 3-36 months, depending on the retailer. If you want to offer your customers interest-free repayment periods longer than 3 months, or credit limits higher than 5000 AUD, contact Stripe support. Zip charges customers an account establishment fee and a monthly fee, but waives the monthly fee when the account balance is zero.


- Zip pay-in-4: Customers pay for purchases over 4 installments interest-free. Zip adds a finance charge based on the purchase amount, and splits the total amount into 4 equal installments. Customers pay the first installment at time of purchase, then make the 3 remaining repayments at 2-week intervals.



The following table lists total transaction limits, currency and payment options by country:

Stripe account and customer countryCurrencyTransaction limitsZip PayZip MoneyZip pay-in-4AustraliaAUD1 - 50,000*United StatesBetaUSD35 - 1,500* If the purchase amount is greater than their available credit, customers can pay the rest with cards up front.

## Prohibited business categories

For information about whether your account is eligible to accept Zip payments, navigate to your Payment methods settings.

In addition to standard Stripe business restrictions, the following business categories are prohibited from accepting Zip payments through Stripe:

- Charity
- Insurance

For detailed information about Zip business restrictions, see the Zip help.

## Adding Zip branding to your website

Zip works closely with partners to constantly test and enhance the way Zip is presented to customers. Their integration and marketing requirements aim to improve customer experience and benefit businesses by converting more browsers into shoppers and increasing average basket sizes. Use their Best Practice Integration guide to increase awareness of your Zip offering.

Zip also provides static visual assets and branding guidelines. You must use and display Zip’s branding according to this guidance.

## Disputes and fraud

Customers must authenticate Zip payments by logging into their Zip account. This requirement helps reduce the risk of fraud or unrecognized payments. While Zip covers losses incurred from customer fraud, Stripe might contact you on behalf of Zip and request to stop or pause shipment before any losses are incurred—make sure you comply promptly with these requests. You must use reasonable care to detect fraud or unauthorised transactions, and minimise disputes and unauthorized use of Zip payments.

Customers can dispute Zip payments in certain cases—for example, if they receive faulty goods or don’t receive them at all. Customers have up to 180 calendar days from the date of purchase to file a dispute. You must cooperate during Zip’s dispute process. Zip will investigate disputes in line with its disputes process. The dispute process works like this:

Zip requires customers to contact you directly to resolve the dispute first. If this doesn’t resolve it, the customer can initiate a dispute case with Zip after 14 days from the date of purchase, and Stripe notifies you using:

- Email notification
- Stripe Dashboard
- An API`charge.dispute.created`event (if your integration is set up to receive[webhooks](/webhooks))

Stripe holds back the disputed amount and fee of 15 AUD from your balance until Zip resolves the dispute, which can take up to 3 months after you submit the evidence. That said, Zip usually resolves the dispute within 30 days.

Stripe requests that you upload compelling evidence that you fulfilled the purchase order using the Stripe Dashboard. This evidence can include:

- Received return confirmation (for shipped goods returned from the customer to you)
- Tracking ID
- Shipping date
- Record of purchase for intangible goods, such as an IP address or email receipt
- Record of purchase for services or physical goods, such as a phone number or proof of receipt

If you would rather handle disputes programmatically, you can respond to disputes using the API.

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

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Payment flow](#payment-flow)[Get started](#get-started)[Payment options](#payment-options)[Prohibited business categories](#prohibited-business-categories)[Adding Zip branding to your website](#adding-zip-branding-to-your-website)[Disputes and fraud](#disputes-and-fraud)[Refunds](#refunds)[Additional requirements](#additional-requirements)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`