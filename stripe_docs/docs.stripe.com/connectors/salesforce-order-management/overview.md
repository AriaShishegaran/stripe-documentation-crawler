# How the Connector for Salesforce Order Management works

The managed package contains the following key components needed for a configuration. After installation you can verify this setup by running the queries either through the developer console or SOQL Builder in VS Code.

- StripeAPI the named credential.Execute the following query using the developer console or SOQL Builder in VSCode:SELECT Id, DeveloperName, Endpoint FROM NamedCredential WHERE DeveloperName = 'StripeAPI'

StripeAPI the named credential.

Execute the following query using the developer console or SOQL Builder in VSCode:

- Use the required Apex classes configured as the bridge between the Payments Platform in Salesforce and the Stripe Payment Gateway: StripeAdapter, StripeAsyncAdapter. These Apex classes for the synchronous and asynchronous adaptors respectively are for processing payments between Salesforce Order Management and Stripe.Execute the following query using the developer console or SOQL Builder in VS Code:SELECT Id, Name, NamespacePrefix FROM ApexClass WHERE Name IN ('StripeAdapter','StripeAsyncAdapter')

Use the required Apex classes configured as the bridge between the Payments Platform in Salesforce and the Stripe Payment Gateway: StripeAdapter, StripeAsyncAdapter. These Apex classes for the synchronous and asynchronous adaptors respectively are for processing payments between Salesforce Order Management and Stripe.

Execute the following query using the developer console or SOQL Builder in VS Code:

- Apply any required protected custom settings to store authentication secrets for the transactional calls to the Stripe Payment Gateway.

Apply any required protected custom settings to store authentication secrets for the transactional calls to the Stripe Payment Gateway.

- Use an invocable Apex method (getAccesToken) to obtain the OAuth token for integration purposes.

Use an invocable Apex method (getAccesToken) to obtain the OAuth token for integration purposes.

- Use Lightning Pages required to authorize the Salesforce Connector in the subscribing org and Stripe Payment Gateway.

Use Lightning Pages required to authorize the Salesforce Connector in the subscribing org and Stripe Payment Gateway.

## Next steps

- Installation Guide

[Installation Guide](/connectors/salesforce-order-management/installation)

- Operations and Maintenance

[Operations and Maintenance](/connectors/salesforce-order-management/operations-and-maintenance)

- Testing

[Testing](/connectors/salesforce-order-management/testing)
