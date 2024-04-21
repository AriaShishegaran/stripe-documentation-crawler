htmlPayPal payments | Stripe Documentation[Skip to content](#main-content)PayPal[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpaypal)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpaypal)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Wallets](/docs/payments/wallets)# PayPal payments

Learn about PayPal, a digital wallet popular with businesses in Europe.PayPal is a payment method that enables customers in any country to pay using their PayPal account.

To pay using PayPal, customers are redirected from your website to PayPal. They choose a funding source: PayPal wallet, linked card or bank account, or buy now, pay later. Then they authenticate the payment. After successful authorization, the customer is redirected back to your website. You receive an immediate notification of the payment’s success or failure.

Payment method propertiesCountry availability- Customer locations

Worldwide


- Presentment currency

EUR, GBP, USD, CHF, CZK, DKK, NOK, PLN, SEK, AUD, CAD, HKD, NZD, SGD


- Payment method family

Wallets


- Payment confirmation

Customer-initiated


- Payout timing

Standard payout timing applies


- Connect support

Partial (requires manual approval, see details below)


- Recurring payments

Requires approval


- Dispute support

Yes


- Refunds / Partial refunds

Yes / Yes



## Payment flow

![](https://b.stripecdn.com/docs-statics-srv/assets/checkout.4af16ecfd4f0a3f4044c56d6100c4a42.svg)

Customer selects PayPal at checkout

![](https://b.stripecdn.com/docs-statics-srv/assets/redirect.f6e6ccf58078e0a25815560086204c24.svg)

Customer is redirected to PayPal and enters login details

![](https://b.stripecdn.com/docs-statics-srv/assets/pincode-sms.d10a5a14a3a7e5d3c00942531f9143cd.svg)

Customer completes authorization process

![](https://b.stripecdn.com/docs-statics-srv/assets/redirect-success.740e23b33b6f52a746e8ec50285e2805.svg)

Customer is notified that payment is complete

![](https://b.stripecdn.com/docs-statics-srv/assets/success.1ee3b6d34d944693e654e84f6d1be9f3.svg)

(Optional) Customer returns back to business’s site for payment confirmation

## Connect support

PayPal is available for online marketplaces using Stripe Connect. These online marketplaces include businesses such as Deliveroo and ManoMano that collect payments from customers, and later pay out to sub-accounts or service providers. PayPal isn’t available for platforms that onboard other businesses and enable them to accept payments directly, such as Shopify or Squarespace.

NoteOnline marketplaces need to submit an onboarding request from the Stripe Dashboard to get access to PayPal. Stripe sends email updates about the progress of all requests, and the current status is also reflected on the Payment Method Settings page.

The following Connect charges types, typically used by online marketplaces, are available to businesses using PayPal.

Destination chargesSeparate charges and transfersDirect chargeson_behalf_of## Get started

Add PayPal and other payment methods from the Stripe Dashboard without making updates to your code. For each customer, Stripe determines the list of supported payment methods most likely to drive conversion. Learn how to accept PayPal and other payment methods automatically with Checkout or Elements. To accept PayPal and other payment methods without any code, use Payment Links.

When you’re ready to go live, follow the steps to activate PayPal payments.

## Disputed payments

Customers must authenticate payments with their PayPal accounts, helping to reduce the risk of fraud or unrecognized payments. However, customers can still dispute transactions after they complete payment. Some common reasons for disputes are customers determining that items weren’t as described, or not receiving items at all. You can submit evidence to contest a dispute directly from the Stripe Dashboard.

Learn how to manage PayPal disputes in the Dashboard.

For certain dispute types, PayPal enables you communicate directly to customers to try resolving the dispute. Contacting customers directly must be handled through the PayPal dashboard, and not the Stripe Dashboard.

## Refunds

PayPal payments can be refunded up to 180 days after the original payment. Stripe uses either your Stripe balance or your PayPal balance to refund the payment, depending on the settlement preference you selected.

You can use the Stripe Dashboard or API to initiate refund requests, as with other payment methods. If you choose to settle funds to Stripe, refunds will be withdrawn from the funds available in your Stripe account. If you choose to settle funds to PayPal, refunds funded using your PayPal balance or any other funding source available on your PayPal account.

## Reporting

PayPal fees are included in the Less fees sections of Balance and Balance Activity reports. PayPal fees aren’t included in your tax invoice from Stripe. You can access these documents from your PayPal dashboard.

## Seller protection

PayPal’s Seller Protection program offers coverage for sellers under eligible transactions. It includes scenarios such as unauthorized transactions or buyers’ claims of non-receipt of item. For more information on the Seller Protection program and eligibility, visit PayPal Seller Protection.

## Prohibited business categories

In addition to the business categories restricted from using Stripe overall, PayPal requires pre-approval to accept payments for certain services. Refer to the PayPal Acceptable Use Policy for details.

## Minimum and maximum charge amounts

PayPal doesn’t have a minimum charge amount, but Stripe enforces the same minimum and maximum charge amounts for PayPal as for other payment methods.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Payment flow](#payment-flow)[Connect support](#connect)[Get started](#get-started)[Disputed payments](#disputed-payments)[Refunds](#refunds)[Reporting](#reporting)[Seller protection](#seller-protection)[Prohibited business categories](#prohibited-business-categories)[Minimum and maximum charge amounts](#minimum-and-maximum-charge-amounts)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`