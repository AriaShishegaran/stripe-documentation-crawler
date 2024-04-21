htmlIssuing balance | Stripe Documentation[Skip to content](#main-content)Balance[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Ffunding%2Fbalance)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/issuing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Ffunding%2Fbalance)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)
[Treasury](#)[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Issuing](/issuing)·[Home](/docs)[Banking as a service](/docs/financial-services)[Issuing cards](/docs/issuing)# Issuing balance

Learn how to make funds available to your cards.To spend money using cards, add funds to the Issuing balance on your account. This balance represents funds reserved for Issuing and is safely separated from your earnings, payouts, and funds from other Stripe products.



Push fundingFunding from Stripe BalancePull funding (US-only)Using the Stripe Dashboard or API, you can access the bank account and routing information you need to push funds from your from external bank account. When that account receives funds, they’re immediately available as a top-up to your Stripe account’s Issuing balance.

For a given currency, the provided bank account information will be unique and able to receive funds any number of times. Funds always arrive in your Issuing balance in the specified currency. In some cases, your bank might perform currency conversion.

RegionPayment SchemeCurrency SupportedSpeedMaximum amount acceptedUnited StatesBetaWire TransferUSDA few minutes to 1 business dayVaries by bank, usually many millionsACHCredit TransferUSDSeveral hours to several business daysVaries by bank, usually less than $25kEuro areaSEPA Credit TransferEURAbout a day€999,999,999.99United KingdomFPSGBPAbout 2 hours during a bank’s business hours, or at the start of the next banking day.£1 millionBACSGBP2-3 business days£20 millionSelect region:

United States (beta)Euro areaUnited Kingdom## Add funds using the Dashboard

Fund your Issuing balance from your Dashboard with the Add to balance button.

![Balances overview page in the Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/default-eu-balance.d004b2b9885b392730d9f2ce6f6a2219.png)

Next, choose Fund your Issuing balance.

You can add funds from your existing Stripe balance or by initiating a SEPA Credit Transfer.

![Options to fund your Stripe balance](https://b.stripecdn.com/docs-statics-srv/assets/top-up-issuing-balance-balance-transfer-eu-3.401d2d32d77bb32d0edf9591cb8f65d8.png)

First, select the Issuing balance.

![Add funds to your Issuing balance via a SEPA Credit Transfer.](https://b.stripecdn.com/docs-statics-srv/assets/top-up-issuing-balance-from-bank-eu-4.82dca301da0a9e785209daa8aa3dbbd6.png)

Add funds to your Issuing balance using a SEPA Credit Transfer.

## Create Funding Instructions with the API

NoteThis API is currently only available for users with an activated account in the Euro area or United Kingdom.

To access account information for pushing funds, use the create Funding Instruction endpoint.

This returns unique instructions for your merchant account or each Connect account to push funds to using a bank transfer.

Command Line`curl https://api.stripe.com/v1/issuing/funding_instructions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "funding_type"="bank_transfer" \
  -d "bank_transfer[type]"="eu_bank_transfer" \
  -d "currency"="eur"`If the request succeeds, it returns a response similar to the following:

`{
  "object": "funding_instructions",
  "bank_transfer": {
    "country": "DE",
    "financial_addresses": [
      {
        "iban": {
          "account_holder_name": "Stripe Technology Europe Limited",
          "bic": "SXPYDEHH",
          "country": "DE",
          "iban": "DE00000000000000000001"
        },
        "supported_networks": [
          "sepa"
        ],
        "type": "iban"
      }
    ],
    "type": "eu_bank_transfer"
  },
  "currency": "eur",
  "funding_type": "bank_transfer",
  "livemode": false
}`## Test pushing funds with the Funding Instructions API

You can simulate a bank transfer to the Issuing balance through the test mode-only Fund endpoint. To specify the transfer amount, provide the amount parameter with a positive integer in the smallest currency unit. You must also specify the currency that you want the simulated funds to arrive in. For example, to create a test transfer of 1.00 EUR, use 100 as the amount, and eur as the currency.

After simulating a bank transfer, the specified amount is then added to the Issuing balance in test mode. View your updated balance from your Dashboard or the retrieve balance endpoint. Each call to the test endpoint simulates a new bank transfer.

Command Line`curl https://api.stripe.com/v1/test_helpers/issuing/fund_balance \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "amount"=100 \
  -d "currency"="eur"`If the request succeeds, it returns a response similar to the following:

`{
  "object": "funding_instructions",
  "bank_transfer": {
    "country": "DE",
    "financial_addresses": [
      {
        "iban": {
          "account_holder_name": "Stripe Technology Europe Limited",
          "bic": "SXPYDEHH",
          "country": "DE",
          "iban": "DE00000000000000000001"
        },
        "supported_networks": [
          "sepa"
        ],
        "type": "iban"
      }
    ],
    "type": "eu_bank_transfer"
  },
  "currency": "eur",
  "funding_type": "bank_transfer",
  "livemode": false
}`## Enable notifications about your balance

You can enable email notifications to help monitor your Issuing balance from your settings. To configure these notifications:

1. Visit your Balance notifications[settings](https://dashboard.stripe.com/settings/issuing/balance-notifications)page.
2. Choose from two types of alerting thresholds:  - Fixed amount: Receive an alert whenever your Issuing balance falls below this amount.
  - Ratio of balance to rolling spend: Receive an alert whenever the ratio of your Issuing balance to your spend over the previous 24 hours falls below the threshold. For example, if you set your threshold to 80% and your spend over the past day is 100 USD, you receive an alert whenever your balance falls below 80 USD.



Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`