# Create a charge

To accept a payment from a customer, you must first create a charge. The type of charge you create—direct, destination, or separate charges and transfers—determines how these funds are split among all parties involved, impacts how the charge appears on the customer’s bank or billing statement (with your platform’s information or your user’s), and determines which account Stripe debits for refunds and chargebacks.

[direct](#direct)

[destination](#destination)

[separate charges and transfers](#separate-charges-transfers)

## Charge types

There are many factors to consider when choosing a charge type, as listed in the table below. Your platform’s business model is particularly important because it can affect how funds flow through Stripe. To review charge type recommendations for your business, refer to your platform profile.

[platform profile](https://dashboard.stripe.com/connect/settings/profile)

[Direct charges](/connect/direct-charges)

- Customers directly transact with your connected account, often unaware of your platform’s existence.

- The transaction involves a single user.

- You’d like to choose if Stripe fees are debited from your connected accounts or your platform

- An e-commerce platform like Shopify or Squarespace

- An accounting platform that enables invoice payments like Freshbooks

[Destination charges](/connect/destination-charges)

- Customers transact with your platform for products or services provided by your connected account.

- The transaction involves a single user.

- Stripe fees are debited from your platform account.

- A ride-hailing service like Lyft

- A services platform like Thumbtack

[Separate charges and transfers](/connect/separate-charges-and-transfers)

- The transaction involves multiple users.

- A specific user isn’t known at the time of charge.

- Transfer can’t be made at the time of charge.

- Stripe fees and processing fees are debited from your platform account.

- An e-commerce marketplace that allows a single shopping cart for goods sold by multiple businesses

You can use a single approach, more than one approach, or switch approaches as appropriate for your organization.

When using Standard accounts, Stripe recommends that you create direct charges. Though uncommon, there are times when it’s appropriate to use direct charges on Express or Custom accounts.

[Standard](/connect/standard-accounts)

[direct charges](/connect/direct-charges)

[Express](/connect/express-accounts)

[Custom](/connect/custom-accounts)

With this charge type:

- You create a charge on your user’s account so the payment appears as a charge on the connected account, not in your account balance.

- The connected account’s balance increases with every charge.

- Funds always settle in the country of the connected account.

- Your account balance increases with application fees from every charge.

- The connected account’s balance is debited for refunds and chargebacks.

How are funds routed with direct charges?

Only connected accounts with the card_payments capability can be directly charged.

[card_payments capability](/connect/account-capabilities#card-payments)

When using Express or Custom accounts, Stripe recommends that you create destination charges.

[Express](/connect/express-accounts)

[Custom](/connect/custom-accounts)

[destination charges](/connect/destination-charges)

With this charge type:

- You create a charge on your platform’s account so the payment appears as a charge on your account. Then, you determine whether some or all of those funds are transferred to the connected account (see funds flow diagrams below).

- Your platform account balance is debited for the cost of the Stripe fees, refunds, and chargebacks.

Send the balance after platform fee to your connected account.

Send the full payment amount to your connected account, then charge your platform fee.

In most scenarios, destination charges are only supported if both your platform and the connected account are in the same region (for example, both in the US). For cross-region support, you can specify the settlement merchant to the connected account using the on_behalf_of attribute on the charge. For more information about cross-region support, see Cross-border transfers.

[settlement merchant](/connect/destination-charges#settlement-merchant)

[on_behalf_of](/api/payment_intents/object#payment_intent_object-on_behalf_of)

[Cross-border transfers](/connect/account-capabilities#transfers-cross-border)

For Express and Custom accounts, Stripe recommends that you create separate charges and transfers if destination charges don’t meet your business needs.

[Express](/connect/express-accounts)

[Custom](/connect/custom-accounts)

[separate charges and transfers](/connect/separate-charges-and-transfers)

With this charge type:

- You create a charge on your platform’s account first. Create a separate transfer to move funds to your connected account. The payment appears as a charge on your account and there’s also a transfer to a connected account (amount determined by you), which is withdrawn from your account balance.

[account balance](/connect/account-balances)

- You can transfer funds to multiple connected accounts.

- Your account balance is debited for the cost of the Stripe fees, refunds, and chargebacks.

Transfer funds to multiple connected accounts.

In most scenarios, your platform and any connected account must be in the same region. Attempting to transfer funds across a disallowed border returns an error. For information about cross-region support, see Cross-border transfers.

[Cross-border transfers](/connect/account-capabilities#transfers-cross-border)

Using separate charges and transfers requires a more complex Connect integration.

[Connect](/connect)

Use this charge type if your business has specific use cases:

- A one-to-many relationship. For example, a payment made to a delivery service needs to be split between the store (the source of the items being delivered) and the delivery person.

- A many-to-one relationship. For example, a carpool trip with a ride-hailing service.

- Charges created before the destination account is known. For example, a janitorial service could process a payment before deciding which janitor to assign to the job.

- Need to transfer funds before receiving a payment, or while the charge is pending. For example, an ad network needs to purchase ad space before they can sell ad time or before receiving any payment from customers.

- Transfer amounts greater than the associated payments. For example, a platform provides a discount to its customer but pays its user the full amount.

In some cases, the transfer amount can be greater than the charge amount, or the transfer is made before the payment is processed. You must monitor your account balance carefully to make sure it has enough available funds to cover the transfer amount. You can also associate a transfer with a charge so the transfer doesn’t occur until the funds from that charge are available.

To make the connected account the business of record for the payment use the on_behalf_of parameter.  When on_behalf_of is set to the ID of the connected account, Stripe automatically:

- Settles charges in the country of the specified account, thereby minimizing declines and avoiding currency conversions.

[currency conversions](/connect/currencies#currency-conversions)

- Uses the fee structure for the connected account’s country.

- Uses the connected account’s statement descriptor.

[connected account’s statement descriptor](/connect/statement-descriptors)

- If the account is in a different country than the platform, the connected account’s address and phone number shows up on the customer’s credit card statement (as opposed to the platform’s).

- The number of days that a pending balance is held before being paid out depends on the delay_days setting on the connected account.

[pending balance](/connect/account-balances)

## Stripe fees

There are two components to Stripe fees with Connect: which pricing plan applies to the payment and which account pays Stripe fees.

Direct charges use the connected account’s pricing plan and Stripe fees are assessed on the connected account.

Destination charges and separate charges and transfers typically use the platform’s pricing plan and are assessed on the platform. When the on_behalf_of field is set, the country of the connected account is used to determine the country specific fees charged to your platform account.

For more information on Connect fees and how to request custom pricing, please see Connect pricing.

[Connect pricing](https://stripe.com/connect/pricing)

## Refunds

You can issue a refund to pay back the money spent on the returned good or to compensate for unsatisfactory service. Below describes how refunds are handled for each charge type:

[refund](/api/refunds)

[creation time](/connect/direct-charges#issue-refunds)

[creation time](/connect/separate-charges-and-transfers#issue-refunds)

Destination charges

If your platform’s account balance is sufficiently negative at creation time, the refund object is set to a status of pending. When enough funds become available in your platform’s balance, Stripe automatically processes the refunds with a pending status and updates their status to successful.

[creation time](/connect/destination-charges#issue-refunds)

If the connected account’s balance is sufficiently negative and a refund request also attempts a transfer reversal, the refund request returns an error, instead of creating a refund with pending status.

## Disputes and chargebacks

For payments created using direct charges, Stripe debits the balance of the connected account for disputes. Funds are withdrawn from the connected account’s balance, not your platform’s balance.

[direct charges](/connect/direct-charges)

For disputes where payments were created on your platform using destination charges or separate charges and transfers, with or without on_behalf_of, your platform balance is automatically debited for the disputed amount and fee. When this happens, your platform can attempt to recover funds from the connected account by reversing the transfer either through the Dashboard or by creating a transfer reversal.

[destination charges](/connect/destination-charges)

[separate charges and transfers](/connect/separate-charges-and-transfers)

[Dashboard](https://dashboard.stripe.com/test/transfers)

[creating a transfer reversal](/api#create_transfer_reversal)

Creating payments using destination charges or separate charges or transfers, with or without on_behalf_of, always debits refund and disputed amounts from your platform balance, even when Stripe is liable for negative balances on your connected accounts.

[Stripe is liable for negative balances](/connect/risk-management)

If there’s a negative balance on the connected account, Stripe attempts to debit the external account on file for the connected account only if debit_negative_balances is set to true.

For more details, see Disputes and fraud and Dispute categories.

[Disputes and fraud](/disputes)

[Dispute categories](/disputes/categories)

## See also

- Create direct charges

[Create direct charges](/connect/direct-charges)

- Create destination charges

[Create destination charges](/connect/destination-charges)

- Create separate charges and transfers

[Create separate charges and transfers](/connect/separate-charges-and-transfers)

- Set statement descriptors

[Set statement descriptors](/connect/statement-descriptors)

- Supported payment methods

[Supported payment methods](https://stripe.com/payments/features#local-payment-methods)

- Integrate tax calculation and collection

[Integrate tax calculation and collection](/tax/connect)
