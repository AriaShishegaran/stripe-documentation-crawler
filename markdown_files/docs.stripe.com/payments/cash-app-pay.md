htmlCash App Pay payments | Stripe Documentation[Skip to content](#main-content)Cash App Pay[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcash-app-pay)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcash-app-pay)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Wallets](/docs/payments/wallets)# Cash App Pay payments

Learn how to accept Cash App Pay, a digital wallet popular with US customers.Cash App is a popular consumer app in the US that allows customers to bank, invest, send, and receive money using their digital wallet.

Cash App Pay is a payment method available to all Cash App customers for single use and recurring payments to businesses. Cash App Pay uses the customer’s stored balance or linked debit card to fund the payment. The customer can confirm the payment in one of two ways:

- During checkout from a mobile device, your site redirects customers to the Cash App mobile application for authentication. The payment is authenticated during the redirect. No additional action is needed in the Cash App mobile application to complete the purchase. The customer is then redirected back to your site.
- During checkout from a desktop web application, the customer scans a QR code with their mobile device to authenticate the transaction.

Payment method propertiesCountry availability- Customer locations

US customers


- Presentment currency

USD


- Payment confirmation

Customer-initiated


- Payment method family

Digital wallet


- Billing support

Yes


- Payout timing

Standard payout timing applies


- Connect support

Yes


- Dispute support

Yes


- Refunds / Partial refunds

Yes / yes



## Payment flow

This demo shows the customer experience when using Cash App Pay.

## Get started

To get started, see Accept a payment.

You don’t actually have to integrate Cash App Pay and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- [Checkout](/checkout/quickstart): Our prebuilt, hosted checkout page.
- [Elements](/payments/quickstart): Our drop-in UI components.

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

### Other payment products

The following Stripe products also support adding Cash App Pay from the Dashboard:

- [Invoicing](/invoicing/quickstart-guide)
- [Payment Links](/payment-links)
- [Subscriptions](/billing/subscriptions/overview)

Boost conversion by letting your customers know you accept payments with Cash App Pay by including their approved brand assets on your website.

## Payment limits and options

While there are no business level minimum or maximum limits enforced, Cash App sets variable customer level limits for sending and receiving money. This limit is based on a number of factors such as verification status of the customer’s account and transaction history. Use Cash App Pay for lower value orders (for example, below  2000 USD) to reduce the likelihood of a decline.

Cash App Pay uses either the customer’s Cash App balance or linked debit card to fund the transaction. By default, Cash App Pay uses the customer’s Cash App balance if the balance can cover the entirety of the order amount. Otherwise, it uses the customer’s linked debit card. A Cash App customer can’t combine payment options for a single order (for example, using the balance for part of the order amount and debit card for the remainder).

## Prohibited and restricted business categories

In addition to the categories of businesses restricted from using Stripe overall, the following categories are prohibited from using Cash App Pay:

- B2B businesses
- Financial services
- Businesses accepting Cash App Pay for gift card purchases

Platforms focused on fundraising, donations, and alcohol sales must seek additional approvals from Stripe. Contact us for additional information.

## Refunds

Returns are subject to the return policy that you display on your website. If your business allows returns, you can refund Cash App Pay transactions as you normally would for card payments. Cash App Pay supports partial or full refunds for up to 90 days after the original purchase, and processes them asynchronously. After Stripe initiates a refund, Cash App Pay issues the refund to the customer’s original form of payment (either their Cash App balance or linked debit card).

Stripe notifies you of the final refund status using the charge.refund.updated webhook event. When a refund succeeds, the Refund object’s status transitions to succeeded. If the refund fails, the Refund object’s status transitions to failed and Stripe returns the amount to your Stripe balance. In these cases, you need to arrange an alternative way of providing your customer with a refund.

## Disputes and fraud

Customers must authenticate Cash App Pay payments by logging in to their Cash App account. This requirement helps reduce the risk of fraud or unrecognized payments. Cash App takes financial liability for any losses due to customer fraud.

Customers can dispute Cash App Pay payments in certain cases–for example, if they’re unaware of the transaction, don’t receive the goods or services, receive duplicate charges for the same transaction, or cancel the transaction without receiving a refund. Customers have 120 calendar days to file a dispute from the date of the original charge, or in situations where they didn’t receive goods, 120 calendar days from the expected receipt date.

If the Cash App Pay payment used the customer’s linked debit card as the underlying source for payment, customers can initiate a dispute in one of the following ways:

1. Directly with their issuing financial institution.
2. Directly with Cash App. This is the only option for payments that use the Cash App stored balance as the underlying source.

After the customer initiates a dispute, Stripe notifies you using:

- Email notification
- The Stripe Dashboard
- An API[charge.dispute.created](/api/events/types#event_types-charge.dispute.created)event (if your integration is set up to receive[webhooks](/webhooks))

When a customer creates a dispute, Stripe deducts the amount of the dispute and associated dispute fee from your Stripe balance until Cash App Pay resolves the dispute. Stripe requests that you upload compelling evidence that you fulfilled the purchase order using the Stripe Dashboard. This evidence can include:

- Received return confirmation (for shipped goods returned from the customer to you)
- Tracking ID
- Shipping date
- Record of purchase for intangible goods, such as IP address or email receipt
- Record of purchase for services or physical goods, such as phone number or proof of receipt

If you would rather handle disputes programmatically, you can respond to disputes using the API.

You must submit the requested information within 13 calendar days. Cash App Pay makes a decision within 58 calendar days of dispute creation. If Cash App Pay resolves the dispute with you winning, Stripe returns the disputed amount to your Stripe balance. If they rule in favor of the customer, the balance charge becomes permanent.

## Statement descriptors

Every Cash App Pay payment appears on the customer’s bank statement with the CashApp* prefix attached to the merchant name. The merchant name is set to the company.name field.

Unlike cards, Cash App Pay does not support a dynamic statement descriptor to be set at the transaction level. This means that the statement_descriptor value in a PaymentIntent request is ignored for Cash App Pay payments.

## Connect

If you use Connect, take the following into consideration before you enable and use Cash App Pay:

### Request Cash App Pay capabilities for your connected accounts

Set the cashapp_payments capability to active on your platform account, and for any connected accounts you want to enable for Cash App Pay. You can do this without code by navigating to the Stripe Dashboard and making sure Cash App Pay is on by default for your connected accounts, or you can request the account capability.

### Business of record and statement descriptors

The charge type of Connect payments might change the default statement descriptor and the business name that appears on the customer’s bank statement. The charge type can also change the business of record shown on:

- The Cash App customer interface
- Customer confirmation emails from Cash App
- The mandate when[saving payment details](/payments/cash-app-pay/set-up-payment)

Charge typeDescriptor taken fromDirectConnected AccountDestinationPlatformSeparate charge and transferPlatformDestination (with`on_behalf_of`using a platform saved payment method)PlatformSeparate charge and transfer (with`on_behalf_of`using a platform saved payment method)PlatformDestination (with`on_behalf_of`not using a platform saved payment method)Connected AccountSeparate charge and transfer (with`on_behalf_of`not using a platform saved payment method)Connected AccountNote- A “platform saved payment method” is a payment method created through PaymentIntent or SetupIntent without using the`on_behalf_of`param. Thus, the saved payment method belongs to the platform account.
- To save a customer from repeated authentications for Destination`on_behalf_of`charges, platforms often save a payment method for the customer, then use it for off session Destination`on_behalf_of`charges.

### PaymentMethod cloning

You can save a customer’s Cash App Pay payment method for recurring purchases but the saved Cash App Pay payment method can only be used with the business of record that the customer authorized off-session use for. This means that Connect users can’t clone Cash App Pay payment methods across different connected accounts when the connected accounts act as the business of record.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Payment flow](#payment-flow)[Get started](#get-started)[Payment limits and options](#payment-limits-and-options)[Prohibited and restricted business categories](#prohibited-and-restricted-busniess-categories)[Refunds](#refunds)[Disputes and fraud](#disputes-and-fraud)[Statement descriptors](#statement-descriptors)[Connect](#connect)Products Used[Payments](/payments)[Payment Links](/payments/payment-links)[Invoicing](/invoicing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`