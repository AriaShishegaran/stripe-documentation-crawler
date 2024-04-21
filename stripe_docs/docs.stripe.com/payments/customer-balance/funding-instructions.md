# Funding instructions

This guide describes how to retrieve instructions for funding the customer’s cash balance without creating a PaymentIntent. Funding instructions are typically useful if you’re accepting payments from larger companies who require these details before you send them an invoice or request for payment.

[invoice](/api/invoices)

Most users rely on this API for a first-time customer signup flow.  If a customer selects bank transfers as their preferred payment method, you can call this endpoint to get the funding instructions right away rather than waiting for the first PaymentIntent or Invoice to be created.

The funding instructions will always be the same for a given customer across both the Customer Balance Funding Instructions API and the PaymentIntents API. As with PaymentIntents, you can request funding instructions using the bank transfer type and currency that best fits your customer.

[PaymentIntents API](/payments/bank-transfers/accept-a-payment)

[Create or retrieve funding instructionsServer-side](#create-funding-instructions)

## Create or retrieve funding instructionsServer-side

Use the Customer Balance Funding Instructions API to retrieve a set of financial_addresses that can receive funds from the customer. Provide these bank account details to your customer so that they can initiate a bank transfer using any of the supported_networks.

In live mode, Stripe supplies each customer with a unique set of bank transfer details. In contrast, Stripe offers invalid bank transfer details to all customers in test mode. Unlike live mode, these invalid details might not always be unique.

[test mode](/test-mode)

The response contains the following fields:

- aba hash

- swift hash

- ach

- domestic_wire_us

[Download confirmation of account ownership](#vban-confirmation-letters)

## Download confirmation of account ownership

Some customers might request additional assurance that the account they’re transferring money into is yours, because the account might be listed as owned by Stripe. To provide this assurance, you can generate a letter confirming your ownership of the account to the customer. In this letter, Stripe confirms that you’re the owner of the virtual bank account corresponding to the account details you have passed to that customer.

To download a letter confirming account ownership:

- Navigate to the Customers page in the Dashboard.

Navigate to the Customers page in the Dashboard.

[Customers page](https://dashboard.stripe.com/customers)

- Select the customer who has requested additional verification that you own the account.

Select the customer who has requested additional verification that you own the account.

- Navigate to their cash balance details. This page shows the account details that the customer must use to pay you by bank transfer.

Navigate to their cash balance details. This page shows the account details that the customer must use to pay you by bank transfer.

- Click the button to download a confirmation letter in a PDF format with today’s date.

Click the button to download a confirmation letter in a PDF format with today’s date.

Download confirmation of account ownership
