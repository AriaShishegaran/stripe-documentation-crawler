# Issuing balance

To spend money using cards, add funds to the Issuing balance on your account. This balance represents funds reserved for Issuing and is safely separated from your earnings, payouts, and funds from other Stripe products.



Using the Stripe Dashboard or API, you can access the bank account and routing information you need to push funds from your from external bank account. When that account receives funds, they’re immediately available as a top-up to your Stripe account’s Issuing balance.

[top-up](/api/topups)

For a given currency, the provided bank account information will be unique and able to receive funds any number of times. Funds always arrive in your Issuing balance in the specified currency. In some cases, your bank might perform currency conversion.

Select region:

## Add funds using the Dashboard

Fund your Issuing balance from your Dashboard with the Add to balance button.

[Dashboard](https://dashboard.stripe.com/balance/overview)

Next, choose Fund your Issuing balance.

You can add funds from your existing Stripe balance or by initiating a SEPA Credit Transfer.

First, select the Issuing balance.

Add funds to your Issuing balance using a SEPA Credit Transfer.

## Create Funding Instructions with the API

This API is currently only available for users with an activated account in the Euro area or United Kingdom.

To access account information for pushing funds, use the create Funding Instruction endpoint.

This returns unique instructions for your merchant account or each Connect account to push funds to using a bank transfer.

If the request succeeds, it returns a response similar to the following:

## Test pushing funds with the Funding Instructions API

You can simulate a bank transfer to the Issuing balance through the test mode-only Fund endpoint. To specify the transfer amount, provide the amount parameter with a positive integer in the smallest currency unit. You must also specify the currency that you want the simulated funds to arrive in. For example, to create a test transfer of 1.00 EUR, use 100 as the amount, and eur as the currency.

[test mode](/test-mode)

[Fund endpoint](/api/issuing/funding_instructions/fund)

After simulating a bank transfer, the specified amount is then added to the Issuing balance in test mode. View your updated balance from your Dashboard or the retrieve balance endpoint. Each call to the test endpoint simulates a new bank transfer.

[Dashboard](https://dashboard.stripe.com/balance/overview#issuing-summary)

[retrieve balance](/api/balance/balance_retrieve)

If the request succeeds, it returns a response similar to the following:

## Enable notifications about your balance

You can enable email notifications to help monitor your Issuing balance from your settings. To configure these notifications:

- Visit your Balance notifications settings page.

[settings](https://dashboard.stripe.com/settings/issuing/balance-notifications)

- Choose from two types of alerting thresholds:Fixed amount: Receive an alert whenever your Issuing balance falls below this amount.Ratio of balance to rolling spend: Receive an alert whenever the ratio of your Issuing balance to your spend over the previous 24 hours falls below the threshold. For example, if you set your threshold to 80% and your spend over the past day is 100 USD, you receive an alert whenever your balance falls below 80 USD.

- Fixed amount: Receive an alert whenever your Issuing balance falls below this amount.

- Ratio of balance to rolling spend: Receive an alert whenever the ratio of your Issuing balance to your spend over the previous 24 hours falls below the threshold. For example, if you set your threshold to 80% and your spend over the past day is 100 USD, you receive an alert whenever your balance falls below 80 USD.
