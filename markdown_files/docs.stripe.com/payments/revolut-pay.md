htmlRevolut Pay payments | Stripe Documentation[Skip to content](#main-content)Revolut Pay[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Frevolut-pay)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Frevolut-pay)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Wallets](/docs/payments/wallets)# Revolut Pay payments

Learn about Revolut Pay, a digital wallet payment method used in the United Kingdom and the European Union.Revolut Pay, developed by Revolut, a global finance app, is a digital wallet payment method. Revolut Pay uses the customer’s stored balance or cards to fund the payment, and offers the option for non-Revolut customers to save their details after their first purchase.

When customers select Revolut Pay as their payment method, Stripe redirects them to Revolut Pay’s website, where they have to authenticate with their account details or checkout as a first time user. After authenticating, Revolut Pay redirects customers back to your website.

Payment method propertiesCountry availability- Customer locations

UK and EU customers


- Presentment currency

EUR, GBP


- Payment confirmation

Customer-initiated


- Payment method family

Digital wallet


- Recurring payments

Requires approval


- Payout timing

Standard payout timing applies


- Connect support

Yes


- Dispute support

Yes


- Refunds / Partial refunds

Yes / yes



Interested in getting access to Revolut Pay in Europe?To express interest in enabling Revolut Pay in Europe, enter your email address below.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you!## Payment flow

## Get started

You don’t actually have to integrate Revolut Pay and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- [Checkout](/checkout/quickstart): Our prebuilt, hosted checkout page.
- [Elements](/payments/quickstart): Our drop-in UI components.

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

### Other payment products

The following Stripe products also support adding Revolut Pay from the Dashboard:

- [Invoicing](/invoicing/quickstart-guide)
- [Payment Links](/payment-links)
- [Subscriptions](/billing/subscriptions/overview)

If your integration requires manually listing payment methods, learn how to manually configure Revolut Pay as a payment.

Check out the Revolut Pay sample on GitHub.

[Refunds](#refunds)Revolut Pay supports full and partial refunds. The refund period is up to 180 days after the purchase. Refunds for Revolut Pay payments are asynchronous and take up to 5 minutes to complete. We notify you of the final refund status using the charge.refund.updated webhook event. When a refund succeeds, the status of the Refund object transitions to succeeded. If a refund fails, the status of the Refund object transitions to failed and we return the amount to your Stripe balance. You then need to arrange an alternative way of providing a refund.

[Disputed payments](#disputed-payments)Customers must authenticate Revolut Pay payments by logging into their Revolut account. This requirement helps reduce the risk of fraud or unrecognized payments. With Revolut’s Buyer Protection Policy, customers can file a dispute, which can result in a chargeback and funds being withdrawn from your Stripe account.

Customers have up to 120 calendar days from the date of purchase to file a dispute. The dispute process works like this:

- After the customer initiates a dispute, Stripe notifies you through email, the Stripe Dashboard, and an API charge.dispute.created event (if your integration is set up to receive webhooks).


- Stripe holds back the disputed amount from your balance until Revolut resolves the dispute.


- Stripe requests that you upload compelling evidence that you fulfilled the purchase order using the Stripe Dashboard. This evidence can include:

  - A received return confirmation (for shipped goods returned from the customer to you)
  - The tracking ID
  - The shipping date
  - A record of purchase for intangible goods, such as IP address or email receipt
  - A record of purchase for services or physical goods, such as phone number or proof of receipt


- This information helps Revolut determine if a dispute is valid or if they need to reject it. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 14 calendar days. Revolut makes a decision within 35 calendar days of evidence submission. If Revolut resolves the dispute in your favor, Stripe returns the disputed amount to your Stripe balance. If Revolut rules in favor of the customer, the balance charge becomes permanent.



NoteIf you prefer to handle disputes programmatically, you can respond to disputes using the API.

## Supported currencies

You can create Revolut Pay payments in the currencies that map to your country. Currently, we support gbp and eur. The default local currency for Revolut Pay UK customers is gbp and for other EU customers it’s eur.

CurrencyCountry`gbp`United Kingdom`eur`Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden## See also

- [Accept a payment with Revolut Pay](/payments/revolut-pay/accept-a-payment)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Payment flow](#payment-flow)[Get started](#get-started)[Refunds](#refunds)[Disputed payments](#disputed-payments)[Supported currencies](#supported-currencies)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`