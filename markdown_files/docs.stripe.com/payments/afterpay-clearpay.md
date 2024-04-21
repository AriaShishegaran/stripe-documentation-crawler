htmlAfterpay and Clearpay payments | Stripe Documentation[Skip to content](#main-content)Afterpay / Clearpay[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fafterpay-clearpay)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fafterpay-clearpay)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Buy now, pay later](/docs/payments/buy-now-pay-later)# Afterpay and Clearpay payments

Offer your customers flexible financing while getting paid upfront with Afterpay (also known as Clearpay in the UK).Afterpay is a global payment method that allows your customers to split purchases into 4 interest-free installments, or longer term interest-bearing monthly installments (US only).

To pay with Afterpay, customers are redirected to Afterpay’s site, where they authorize the payment by agreeing to the terms of a payment plan, then return to your website to complete the order. Afterpay offers payment options based on factors such as customer credit, prior account history, order amount, and the type of goods or services being underwritten. After payment acceptance, the full amount of the order (minus fees) is made available to your Stripe account upfront, and Afterpay collects the purchase amount from your customer, who repays Afterpay directly over time. For more information, see Payment options and limits.

Payment method propertiesCountry availability- Customer locations

United States, Canada, United Kingdom, Australia, New Zealand


- Presentment currency

USD, CAD, GBP, AUD, or NZD


- Payment confirmation

Customer-initiated


- Payment method family

Buy Now, Pay Later


- Recurring payments

No


- Payout timing

Standard payout timing applies


- Connect support

Yes


- Refunds / Partial refunds

Yes / yes


- Dispute support

Yes



NoteAfterpay and Clearpay only support domestic transactions, meaning you can only sell to customers in the same country as your business. If you’re using Dynamic payment methods, Stripe handles a customer’s payment method eligibility automatically. If you use payment_method_types, you must either configure your integration so that it only presents Afterpay and Clearpay to eligible customers, or use dynamic payment methods.

## Payment flow

This demo shows the customer experience when using Afterpay.

## Get started

You don’t actually have to integrate Afterpay and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- [Checkout](/checkout/quickstart): Our prebuilt, hosted checkout page.
- [Elements](/payments/quickstart): Our drop-in UI components.

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

Payment Links also supports adding Afterpay from the Dashboard.

If you prefer to manually list payment methods, learn how to manually configure Afterpay as a payment.

You can also let customers know Afterpay payments are available by including the Payment Method Messaging Element on your product, cart, and payment pages. We recommend adding a site messaging Element to help drive conversion.

## Payment options and limits

Payment options vary by cart order size and country. In the US, Afterpay presents customers with Pay in 4, monthly installments, or both options. For all other markets, Afterpay presents customers with Pay in 4 only.

- Pay in 4: customers pay for purchases in four or fewer interest-free, bi-weekly payments over a 6 week term.
- Monthly installments: (US only) customers pay for purchases over a 6 or 12 month term that includes capped interest.

Afterpay collects the first installment from the customer immediately, and the next installment either 2 weeks or 1 month after, depending on the payment schedule. You can accept payments from customers in the same country that you registered your Stripe account. Payments must also match the local currency of the country.

The following table lists total transaction limits and installment schedules by country.

Stripe account and customer countryCurrencyTransaction limitsAustraliaAUD1 - 2,000 AUDCanadaCAD1 - 2,000 CADNew ZealandNZD1 - 2,000 NZDUnited KingdomGBP1 - 1,200 GBPUnited StatesUSD1 - 4,000 USD### United States

## Prohibited business categories

For more information about Afterpay eligibility for your account, navigate to your Payment methods settings.

In addition to the categories of businesses restricted from using Stripe overall, the following categories are prohibited from using Afterpay.

- Alcohol
- Donations
- Pre-orders
- NFTs
- B2B

For the complete list, see the terms of service.

## Adding Afterpay branding to your website

Let your customers know you accept payments with Afterpay by including the Payment Method Messaging Element on your product and cart pages.

Afterpay also provides static visual assets and branding guidance. In AU, CA, NZ and the US, consumers know Afterpay as ‘Afterpay’. In the UK, they know it as ‘Clearpay’. Make sure you pick the right location (see the footer in the Afterpay documentation) so that you get the appropriate assets. For Clearpay, see the UK assets and branding guidance.

## Disputed payments

Customers must authenticate Afterpay payments by logging into their Afterpay account. This requirement helps reduce the risk of fraud or unrecognized payments. Afterpay covers losses incurred from customer fraud or the inability to repay installments. However, Stripe might contact you on behalf of Afterpay and request to stop or pause a shipment before any losses are incurred. It’s important to comply promptly with these requests.

Customers can dispute Afterpay payments in certain cases—for example, if they don’t receive the goods they paid for. Customers have up to 120 calendar days from the date of purchase to file a dispute. The dispute process works like this:

After the customer initiates a dispute, Stripe notifies you using:

- Email
- The Stripe Dashboard
- An API`charge.dispute.created`event (if your integration is set up to receive[webhooks](/webhooks))

Stripe holds back the disputed amount from your balance until Afterpay resolves the dispute.

Stripe requests that you upload compelling evidence that you fulfilled the purchase order using the Stripe Dashboard. This evidence can include:

- A received return confirmation (for shipped goods returned from the customer to you)
- The tracking ID
- The shipping date
- A record of purchase for intangible goods, such as IP address or email receipt
- A record of purchase for services or physical goods, such as phone number or proof of receipt

If you prefer to handle disputes programmatically, you can respond to disputes using the API.

This information helps Afterpay determine if a dispute is valid or if they should reject it. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 14 calendar days. Afterpay makes a decision within 30 calendar days of evidence submission. If Afterpay resolves the dispute with you winning, Stripe returns the disputed amount to your Stripe balance. If Afterpay rules in favor of the customer, the balance charge becomes permanent.

## Refunds

You can refund Afterpay charges up to 120 days after the original payment. Refunds for Afterpay payments are asynchronous.

## Connect

You can use Stripe Connect with Afterpay to process payments on behalf of a connected account. Connect users can use Afterpay with the following charge types:

Charge types- [Direct](/connect/direct-charges)
- [Destination](/connect/destination-charges)
- [Separate Charges and Transfers](/connect/separate-charges-and-transfers)

Stripe and Afterpay rely on merchant category codes (MCC) to determine eligibility of the connected accounts against the Afterpay prohibited business categories. Make sure that you set correct MCCs for your connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Payment flow](#payment-flow)[Get started](#get-started)[Payment options and limits](#collection-schedule)[Prohibited business categories](#prohibited-business-categories)[Adding Afterpay branding to your website](#adding-afterpay-branding-to-your-website)[Disputed payments](#disputed-payments)[Refunds](#refunds)[Connect](#connect)Products Used[Payments](/payments)[Connect](/connect)[Payment Links](/payments/payment-links)[Checkout](/payments/checkout)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`