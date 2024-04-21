# Issuing and Treasury sample app

In addition to a full suite of documentation and SDKs for Stripe Issuing and Treasury, we offer a Next.js sample app.

See a demo of our sample app at baas.stripe.dev, or check out the GitHub repository.

[baas.stripe.dev](https://baas.stripe.dev)

[GitHub repository](https://github.com/stripe-samples/issuing-treasury)

## Accessing code

The sample app is a Next.js app that leverages TypeScript, React, and Material UI. You can fork the project from the Stripe samples GitHub repository and use the included components as a starting point for your own app.

[Stripe samples GitHub repository](https://github.com/stripe-samples/issuing-treasury)

## App features

The app provides many how-to examples, including:

- Leverage Stripe Connect Onboarding to collect Know Your Customer (KYC) information for onboarding users compliantly

- Display account information and balance

- Display transactions on the Treasury Financial Account

- Simulate sending funds to an external account using ACH or wire

- Simulate receiving an ACH credit

- Visualize the volume of inbound and outbound money flows using ApexCharts

[ApexCharts](https://github.com/apexcharts/apexcharts.js)

- Create cardholders compliantly

- Create cards using the Treasury Financial Account as an issuable balance

- Show sensitive card numbers in a PCI-compliant way

- Simulate card authorizations

- Get paid through a payment link, then transfer funds from your Stripe payments balance to the Financial Account

- Use test helpers to simulate actions impacting the account

## Component breakdown

The following sections provide an overview of how each component in the sample app works.

You can learn more about Issuing APIs and features or Treasury APIs and features.

[Issuing APIs and features](/issuing)

[Treasury APIs](/api/treasury/financial_accounts)

[features](/treasury)

The account creation flow consists of four steps:

- Create a custom connected account with the following capabilities: transfers, card_issuing, and treasury.

[custom connected account](/treasury/account-management/connected-accounts)

- Create a Stripe Treasury Financial Account.

[Financial Account](/treasury/account-management/financial-accounts)

- Create a Connect Onboarding link and use it to redirect new users to collect the necessary profile information for the requested capabilities.

The account balance card uses only the stripe.treasury.financialAccounts.list API.

The payload of the above command contains a balance object consisting of the current ‘balance’ (cash) and outbound funds.

[‘balance’](/treasury/account-management/working-with-balances-and-transactions)

The funds movement chart uses only the stripe.treasury.transactions.list API.

The responses are grouped by positive or negative balances and creation date. The data is then ported into ApexCharts to create a dynamic display of the funds flow.

[ApexCharts](https://github.com/apexcharts/apexcharts.js)

The transaction list uses the stripe.treasury.transactions.list API.

The columns in the transactions table are parsed from the transaction object using the following mapping:

- created → Date

- amount → Amount / Currency

- flow_type → Type

- status → Status

- description → Description

The money sending feature in the sample app uses the Stripe Treasury OutboundPayment feature. You can use OutboundPayments to send money to a third party’s external account.

[OutboundPayments](/treasury/moving-money/financial-accounts/out-of/outbound-payments)

You must create a Cardholder before you can issue a card using Stripe Issuing to spend funds from the Treasury Financial Account. Use the stripe.issuing.cardholders.create API to create cardholders.

After you create a Cardholder, you can issue a card to the Cardholder using the stripe.issuing.cards.create API.

The cards list renders using data from the stripe.issuing.cards.list API.

Use the stripe.issuing.authorizations.list API to retrieve authorizations for a specific card. The following example limits the list to the 10 most recent authorizations.

The columns in the authorization table are parsed from the response object using the following mapping:

- created → Date

- amount → Amount / Amount Currency

- card.cardholder.name → Name on Card

- card.last4 → Last 4

- approved → Approved

- status → Status

- merchant_data.name → Merchant

- merchant_data.category → Merchant Category

## Test mode helpers

The sample app features test mode helpers that enable you to perform certain actions, such as funding your account, creating a payment link to collect funds in a connected account, and paying out funds to the Financial Account. You can access most of the test helpers by clicking the Generate Test Data button or clicking Test Data.

In test mode, you can add funds to a Treasury Financial Account using the ReceivedCredit Test Helpers. This test helper simulates receiving a transfer from an external bank account into your Financial Account.

[ReceivedCredit Test Helpers](/api/treasury/received_credits/test_mode_create)

You can use payment links to add funds to the connected account that’s associated with a Financial Account:

- Create a Price that determines the amount deposited into the connected account after completion of payment.

- After obtaining the price, Stripe creates a PaymentLink, and you redirect the user to complete the payment. Use the Price id from the previous step to set the value for the price parameter. Alternatively, you can exclude the parameter to use a default value instead.

Payouts can send funds from a connected account’s payments balance to their Treasury Financial Account. Do the following to execute a payout:

[Payouts](/treasury/moving-money/payouts#payouts)

- Check if there is an external account configured for the connected account. To do so, use the accounts.retrieve API to obtain the account object and verify if the external_account property is populated.

[accounts.retrieve](/api/accounts/retrieve)

[account object](/api/accounts/object)

- If there isn’t an existing external account, the user can set up the Treasury Financial Account as the connected account’s external account.

- Initiate a payout to the connected account’s external account. In this case, the external account is the Treasury Financial Account.
