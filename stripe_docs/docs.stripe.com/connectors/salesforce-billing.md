# Stripe Connector for Salesforce Billing

Stripe Connector for Salesforce Billing is a managed package that you install on top of Salesforce CPQ and Salesforce Billing. It allows users to process payments through the Salesforce Payment Gateway using Stripe payment service to complete transactions.

Stripe exposes four transaction types directly from the Salesforce Billing UI:

- Tokenization—Create a new payment method on an account and set it as the default.

- Charge Transaction—Charge a specific amount to an account.

- Refund Transaction—Refund a specific amount to an account.

- Bidirectional Data Sync-See related transactions in both Salesforce and Stripe dashboards.

In addition to the UI-based transaction types, Stripe also offers API-based transaction types, which developers can use to create methods that take advantage of the features on the Stripe payment service:

- Void Token—Remove a payment method from an account.

- Authorize Transaction—Allocate a specific amount to an account pending a charge.

- Capture Transaction—Complete a charge on an authorized transaction.

- Void Transaction—Void a charge on an authorized transaction.

- Get Payment Status—Return the status of a specific charge.

- Get Refund Status—Return the status of a specific refund.

The UI-based transaction types (tokenization, charge, refund) are also supported through the API.

The Following Payment Methods are supported:

- Cards—Support for global and local card networks

- ACH—ACH Direct Debit payments from customers with a US bank account

## Next steps

- Install Stripe for Salesforce Billing

[Install Stripe for Salesforce Billing](/connectors/salesforce-billing/install)

- Configure Stripe for Salesforce Billing

[Configure Stripe for Salesforce Billing](/connectors/salesforce-billing/configuration)
