htmlBank transfer payments | Stripe Documentation[Skip to content](#main-content)Bank transfers[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbank-transfers)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbank-transfers)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)# Bank transfer payments

Learn about bank transfers and managing payments with the customer balance.Available in:### Turn on bank transfers

To turn on bank transfer payments, navigate to your Payment methods settings.

Bank transfers provide a safe way for customers to send money over bank rails. When accepting bank transfers with Stripe, you provide customers with a virtual bank account number that they can push money to from their own online bank interface or in-person bank branch. Stripe uses this virtual account number to automate reconciliation and prevent exposing your real account details to customers.

## Get started

You don’t actually have to integrate Bank Transfers and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- [Checkout](/checkout/quickstart): Our prebuilt, hosted checkout page.
- [Elements](/payments/quickstart): Our drop-in UI components.

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

### Other payment products

The following Stripe products also support adding Bank Transfers from the Dashboard:

- [Invoicing](/invoicing/quickstart-guide)
- [Subscriptions](/billing/subscriptions/overview)

If you prefer to manually list payment methods, or want to learn more about how bank transfers work with invoicing and subscriptions, see the following guides:

- [Accept a bank transfer payment](/payments/bank-transfers/accept-a-payment)
- [Send an invoice with bank transfer instructions](/invoicing/bank-transfer)
- [Set up a subscription with bank transfers as a payment method](/billing/subscriptions/bank-transfer)

## Customer balance

Unlike most payment methods, bank transfers don’t allow you to control the amount a customer sends to you, which means that customers might send too much or too little money by accident. To manage common overpayment and underpayment issues, Stripe holds your customer’s bank transfers in a customer balance that you can reconcile payments from. This allows you to track how much your customers owe, regardless of how much or how often they send funds. If funds are held in the customer balance for more than 75 days, Stripe automatically attempts to return the funds to the customer’s bank account. For further information on what happens when funds remain unreconciled, see the reconciliation documentation.

## International payments

Bank transfers users in the United States can accept international wire transfers (SWIFT). International wire transfers may incur fees on the way to Stripe, which can result in an amount received that’s less than what the customer originally sent. Stripe-incurred fees appear on the balances page in the Dashboard, alongside other relevant Stripe fees. The amount shown in the cash balance is the amount that Stripe received from the customer.

Stripe doesn’t support refunds for international wires. You’re responsible for executing any refunds related to these payments.

## Refunds

You can refund customer balance payments:

- Directly to the customer’s bank account
- Back to the customer’s cash balance, where the refund can be used towards another customer balance payment

To refund to the customer’s bank account, Stripe requires the customer’s bank account details. In some cases, Stripe receives these details when the customer transfers funds. When these details aren’t available, Stripe sends an email to the customer to collect bank account details and initiate a transfer when we receive those details.

If your customer has excess funds in their customer balance, you can initiate a return of funds through the Dashboard or the API. For more information, see Refund bank transfer payments.

## Recalls

When a customer in the SEPA region asks their bank to undo a payment made with bank transfer, the bank issues a recall request to Stripe and we show the recall as a dispute inquiry in your Stripe Dashboard.

Refer to the guidelines in Recall requests to either accept or reject a recall inquiry.

## Funding instructions

If you need to show bank account details to your customer before they make their first payment (for example, when they create their account), you can use the Funding Instructions API.

## Sender information

You can determine the sender details of an incoming bank transfer through either the Dashboard or the API. Those details can include the name of the sender, the reference, and the network through which the transfer arrived.

DashboardAPI1. In the[Dashboard](https://dashboard.stripe.com/customers), navigate to the customer’s page.
2. UnderPayment Methods, expand the cash balance tab.
3. Open the Cash Balance page by clickingView balance details.

![Payment methods section](https://b.stripecdn.com/docs-statics-srv/assets/payment-methods-section.98d98636d90fbf8ea6e5834dcdde1133.png)

Payment methods section

On the cash balance page, the Transactions section displays a list of the customer’s incoming and outgoing cash balance transactions.

![List of all customer cash balance transactions](https://b.stripecdn.com/docs-statics-srv/assets/transactions-list.f8e2bee93047bd6c85021cfb3db52348.png)

List of all customer cash balance transactions

Incoming transfers have type Funding. Find the transfer you’re interested in and open its details page by clicking its description.

![Funding details sender information](https://b.stripecdn.com/docs-statics-srv/assets/funding-details-sender-info.b78a278b7f04e003480c0d4308af206b.png)

Funding details sender information

## Connect

Stripe Connect can be used with bank transfers to process payments on behalf of connected accounts. Connect platforms can use bank transfers with any type of charges.

The on_behalf_of attribute isn’t supported.

### Accepting bank transfer payments as the connected account

Direct charges require the connected account itself (not the platform) to have activated the bank transfers payment method—Connect platforms can use the bank_transfer_payments capability to determine whether this is the case for a connected account. Standard Connect accounts can request the capability from their Stripe Dashboard.

### Activation process

The process varies by country, but in general for bank transfer payments, the required information is the same as what’s necessary to activate a Stripe account for payments. If the account doesn’t fulfill all the required information, the capability remains inactive with any issues highlighted on the capability object in the requirements.currently_due and requirements.disabled_reason fields until these issues have been addressed. After all the highlighted issues are resolved, the capability’s status changes to active, unless there are issues activating the account in general, in which case Stripe sends the Connect platform owner an email.

## Unsupported businesses

Stripe can’t accept payments for certain types of businesses. In addition to the Restricted Business list, Stripe doesn’t support bank transfers if your business falls into any of the following categories:

EUUK- Automated Cash Disburse
- Manual Cash Disburse
- Miscellaneous and Specialty Retail Stores

## Unsupported products and features

Bank transfers don’t support Payment Links or International transfers.

Interested in getting early access to cross-border bank transfers?This feature allows you to accept bank transfers in currencies outside of your region. Please provide your email address for us to review your suitability and our team will contact you soon.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Get started](#get-started)[Customer balance](#customer-balance)[International payments](#international-payments)[Refunds](#refunds)[Recalls](#recalls)[Funding instructions](#funding-instructions)[Sender information](#sender-information)[Connect](#connect)[Unsupported businesses](#unsupported-businesses)[Unsupported products and features](#unsupported-products-features)Products Used[Payments](/payments)[Connect](/connect)[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`