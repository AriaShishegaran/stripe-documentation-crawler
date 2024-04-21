# Bank transfer payments

To turn on bank transfer payments, navigate to your Payment methods settings.

[Payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

Bank transfers provide a safe way for customers to send money over bank rails. When accepting bank transfers with Stripe, you provide customers with a virtual bank account number that they can push money to from their own online bank interface or in-person bank branch. Stripe uses this virtual account number to automate reconciliation and prevent exposing your real account details to customers.

## Get started

You don’t actually have to integrate Bank Transfers and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

The following Stripe products also support adding Bank Transfers from the Dashboard:

- Invoicing

[Invoicing](/invoicing/quickstart-guide)

- Subscriptions

[Subscriptions](/billing/subscriptions/overview)

If you prefer to manually list payment methods, or want to learn more about how bank transfers work with invoicing and subscriptions, see the following guides:

- Accept a bank transfer payment

[Accept a bank transfer payment](/payments/bank-transfers/accept-a-payment)

- Send an invoice with bank transfer instructions

[Send an invoice with bank transfer instructions](/invoicing/bank-transfer)

- Set up a subscription with bank transfers as a payment method

[Set up a subscription with bank transfers as a payment method](/billing/subscriptions/bank-transfer)

## Customer balance

Unlike most payment methods, bank transfers don’t allow you to control the amount a customer sends to you, which means that customers might send too much or too little money by accident. To manage common overpayment and underpayment issues, Stripe holds your customer’s bank transfers in a customer balance that you can reconcile payments from. This allows you to track how much your customers owe, regardless of how much or how often they send funds. If funds are held in the customer balance for more than 75 days, Stripe automatically attempts to return the funds to the customer’s bank account. For further information on what happens when funds remain unreconciled, see the reconciliation documentation.

[customer balance](/payments/customer-balance)

[reconciliation documentation](/payments/customer-balance/reconciliation#cash-unreconciled-funds)

## International payments

Bank transfers users in the United States can accept international wire transfers (SWIFT). International wire transfers may incur fees on the way to Stripe, which can result in an amount received that’s less than what the customer originally sent. Stripe-incurred fees appear on the balances page in the Dashboard, alongside other relevant Stripe fees. The amount shown in the cash balance is the amount that Stripe received from the customer.

Stripe doesn’t support refunds for international wires. You’re responsible for executing any refunds related to these payments.

## Refunds

You can refund customer balance payments:

- Directly to the customer’s bank account

- Back to the customer’s cash balance, where the refund can be used towards another customer balance payment

To refund to the customer’s bank account, Stripe requires the customer’s bank account details. In some cases, Stripe receives these details when the customer transfers funds. When these details aren’t available, Stripe sends an email to the customer to collect bank account details and initiate a transfer when we receive those details.

If your customer has excess funds in their customer balance, you can initiate a return of funds through the Dashboard or the API. For more information, see Refund bank transfer payments.

[Refund bank transfer payments](/payments/customer-balance/refunding)

## Recalls

When a customer in the SEPA region asks their bank to undo a payment made with bank transfer, the bank issues a recall request to Stripe and we show the recall as a dispute inquiry in your Stripe Dashboard.

[recall](/payments/customer-balance/recalls)

Refer to the guidelines in Recall requests to either accept or reject a recall inquiry.

[Recall requests](/payments/customer-balance/recalls)

## Funding instructions

If you need to show bank account details to your customer before they make their first payment (for example, when they create their account), you can use the Funding Instructions API.

[Funding Instructions API](/payments/customer-balance/funding-instructions)

## Sender information

You can determine the sender details of an incoming bank transfer through either the Dashboard or the API. Those details can include the name of the sender, the reference, and the network through which the transfer arrived.

- In the Dashboard, navigate to the customer’s page.

[Dashboard](https://dashboard.stripe.com/customers)

- Under Payment Methods, expand the cash balance tab.

- Open the Cash Balance page by clicking View balance details.

Payment methods section

On the cash balance page, the Transactions section displays a list of the customer’s incoming and outgoing cash balance transactions.

List of all customer cash balance transactions

Incoming transfers have type Funding. Find the transfer you’re interested in and open its details page by clicking its description.

Funding details sender information

## Connect

Stripe Connect can be used with bank transfers to process payments on behalf of connected accounts. Connect platforms can use bank transfers with any type of charges.

[Stripe Connect](/connect/overview)

[Connect](/connect)

[any type of charges](/connect/charges#types)

The on_behalf_of attribute isn’t supported.

[on_behalf_of attribute](/api/payment_intents/object#payment_intent_object-on_behalf_of)

Direct charges require the connected account itself (not the platform) to have activated the bank transfers payment method—Connect platforms can use the bank_transfer_payments capability to determine whether this is the case for a connected account. Standard Connect accounts can request the capability from their Stripe Dashboard.

[Direct charges](/connect/direct-charges)

[bank_transfer_payments capability](/connect/account-capabilities#payment-methods)

[Standard Connect accounts](/connect/standard-accounts)

The process varies by country, but in general for bank transfer payments, the required information is the same as what’s necessary to activate a Stripe account for payments. If the account doesn’t fulfill all the required information, the capability remains inactive with any issues highlighted on the capability object in the requirements.currently_due and requirements.disabled_reason fields until these issues have been addressed. After all the highlighted issues are resolved, the capability’s status changes to active, unless there are issues activating the account in general, in which case Stripe sends the Connect platform owner an email.

[required information](/connect/required-verification-information)

[capability object](/api/capabilities/object)

## Unsupported businesses

Stripe can’t accept payments for certain types of businesses. In addition to the Restricted Business list, Stripe doesn’t support bank transfers if your business falls into any of the following categories:

[Restricted Business list](https://stripe.com/restricted-businesses)

- Automated Cash Disburse

- Manual Cash Disburse

- Miscellaneous and Specialty Retail Stores

## Unsupported products and features

Bank transfers don’t support Payment Links or International transfers.

[privacy policy](https://stripe.com/privacy)
