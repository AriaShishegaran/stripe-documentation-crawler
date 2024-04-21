# Collect a bank account to enhance Connect payouts

Not sure about which Financial Connections integration to use? See our overview of integration options.

[overview of integration options](/financial-connections/use-cases)

Financial Connections enables you to instantly collect tokenized account and routing numbers to facilitate payouts for your Custom connected accounts, which helps you:

[Custom connected accounts](/connect/custom-accounts)

- Increase onboarding conversion by eliminating the need for your connected accounts to leave your website or application to locate their account and routing numbers.

- Reduce payout failure rates by eliminating errors that result from manual entry of account and routing numbers.

- Make sure you don’t need to store sensitive data such as account and routing numbers on your server.

- Save development time by eliminating your need to build bank account manual entry forms.

- Enable your users to connect their accounts in fewer steps with Link, allowing them to save and quickly reuse their bank account details across Stripe merchants.

Enable your users to connect their accounts in fewer steps with Link, allowing them to save and quickly reuse their bank account details across Stripe merchants.

Optionally, Stripe platforms in the US can request permission from your Custom account to retrieve additional data on their Financial Connections account. Consider accessing balances, transactions, and ownership information to optimize your onboarding process.

[Financial Connections account](/api/financial_connections/accounts/object)

[balances](/financial-connections/balances)

[transactions](/financial-connections/transactions)

[ownership](/financial-connections/ownership)

Retrieving additional account data can help you:

- Mitigate fraud when onboarding accounts by verifying the ownership details of their bank account, such as the name and address of the account holder.

- Underwrite accounts for financial services that you might offer on your platform with balances and transactions data.

## Get started

For Custom account types, enable Stripe Financial Connections either within the Connect Onboarding for Custom Accounts web form or directly within your own onboarding flow.

[Connect Onboarding for Custom Accounts](/connect/payouts-bank-accounts)

[own onboarding flow](/connect/payouts-bank-accounts)

Standard and Express account onboarding always use Financial Connections. Access to additional bank account data is unavailable on these account types.
