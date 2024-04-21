htmlFunding Issuing balances with Connect | Stripe Documentation[Skip to content](#main-content)Connect funding[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fconnect%2Ffunding)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/issuing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fconnect%2Ffunding)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)
[Treasury](#)[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Issuing](/issuing)·[Home](/docs)[Banking as a service](/docs/financial-services)[Issuing cards](/docs/issuing)# Funding Issuing balances with Connect

Learn how to fund connected accounts for Issuing.Before an issued card can be used for transactions, you must first allocate funds to the connected account’s Issuing balance associated with the card. An Issuing balance holds funds reserved for the card and is safely separated from earnings, payouts, and funds from other Stripe products.

[Fund from a bank account](#fund-from-bank-account)You have two options for funding an Issuing balance from an external account that each have different setups: pull funding and push funding.

- Pull fundingis the default funding option in the US and isn’t available in the EU or the UK. You need to verify external bank accounts, which usually causes a delay in transferring funds (up to 5 business days). This option allows you to control and identify which bank your top-up originates from.
- Push fundingis available in the UK and EU and as a beta in the US. This options allows you to originate the funds from your own bank account to Stripe. You might be able to receive funds the same day with push funding, which depends on the process you use (for example, ACH or wire transfer).

Pull funding (US)Push funding (US)Push funding (Euro)Push funding (UK)Before you can top-up a connected account from your user’s bank account, you must first collect and verify their account information. Stripe provides the option of  collection through Stripe.js with verification using microdeposits.

### Collecting your users’ information

To debit the user’s bank account for funding, you will need to collect their bank account information and submit evidence of their authorization to debit their account. This is known as a mandate, and ensures both you and Stripe remain compliant with ACH network rules, as well as provide you with access to evidence to ease in any dispute resolution.

Create a form that captures:

- Name
- Routing number
- Account number

As your customers submit the mandate, you should record:

- IP address
- User agent
- Date

If instead you prefer to collect mandates from your users offline (such as via phone or a paper agreement), you won’t upload evidence of acceptance to Stripe. You should maintain your own record of the acceptance and provide us a contact email in case the evidence is requested.

### Creating the token and source

Create a token using the Bank Account Token API, and then use it to create a source. Create both the bank account token and source on the connected account you want to fund.

CautionStore these Source tokens in your own system where your integration can retrieve them. Stripe currently doesn’t provide a way to programmatically retrieve or list the tokens after they’re created.

Command Line[curl](#)`curl https://api.stripe.com/v1/tokens \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "bank_account[country]"=US \
  -d "bank_account[currency]"=usd \
  -d "bank_account[account_holder_name]"="Jenny Rosen" \
  -d "bank_account[account_holder_type]"=individual \
  -d "bank_account[routing_number]"=110000000 \
  -d "bank_account[account_number]"=000000000009`Create a source using the token you obtained:

Command Line[curl](#)`curl https://api.stripe.com/v1/sources \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d type=ach_debit \
  -d currency=usd \
  -d token={{TOKEN_ID}} \
  -d "owner[address][line1]"="510 Townsend Street" \
  -d "owner[address][city]"="San Francisco" \
  -d "owner[address][state]"=California \
  -d "owner[address][country]"=US \
  --data-urlencode "owner[email]"="jenny.rosen@example.com" \
  -d "owner[name]"="Jenny Rosen" \
  -d "owner[phone]"=5554443333`### Verifying sources with microdeposits

Two small deposits with the statement description ACCTVERIFY are sent to the bank account within 1-2 days. You should collect these two amounts from your user to verify the bank account.

Command Line[curl](#)`curl https://api.stripe.com/v1/sources/{{SOURCE_ID}}/verify \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "values[]"=32 \
  -d "values[]"=45`### Top-up a connected account’s Issuing balance

Fund the Issuing balance on your connected account with top-ups by passing in the source that was made and setting the destination_balance to issuing.

Command Line[curl](#)`curl https://api.stripe.com/v1/topups \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -H "Stripe-Account: {{CONNECTED_STRIPE_ACCOUNT_ID}}" \
  -d "amount"=2000 \
  -d "currency"="usd" \
  -d "description"="Top-up for week of May 31" \
  -d "destination_balance"="issuing" \
  -d "statement_descriptor"="Top-up" \
  -d "source"="{{SOURCE_ID}}"`[Fund from a connected account's Stripe balanceBeta](#fund-from-connected-account-balance)You must sign up for the Balance Transfer API private beta to transfer funds from your Stripe balance into your Issuing balance.

Command Line[curl](#)`curl https://api.stripe.com/v1/balance_transfers \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -H "Stripe-Account: {{CONNECTED_STRIPE_ACCOUNT_ID}}" \
  -d amount=1000 \
  -d currency=usd \
  -d "source_balance[type]"=payments \
  -d "destination_balance[type]"=issuing`Transfers from your connected account’s Stripe balance are instant and available 24x7 in the US, or take one business day in the UK and euro area countries. This allows you to quickly and easily utilize earned funds from Stripe Payments for spend with Stripe Issuing.

You can only move an amount up to the available Stripe balance. Funds won’t be available in the Issuing balance while the transfer is pending.

Use the retrieve balance endpoint to get your available Stripe balance amounts broken down by source_type.

### Request early access

Access to the Balance Transfer API is currently limited to beta users. You must be an Issuing customer to join the beta. To request access to the beta, log in to your Stripe account and refresh the page. Contact Stripe for more information.

[Retrieve an Issuing balance](#retrieve-an-issuing-balance)To check the current Issuing balance of a connected account, call the Balance API GET endpoint and pass the connected account ID into the header.

Command Line[curl](#)`curl https://api.stripe.com/v1/balance \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"`Thebalance object is returned with a corresponding issuing object that includes the current available balance:

`{
  "object": "balance",
...
    "issuing": {
    "available": [
      {
        "amount": 100,
        "currency": "usd"
      }
    ]
  },
  "livemode": false
}`[Pay out an Issuing balance to an external account](#pay-out-an-issuing-balance)The funds in an Issuing balance can also be paid out to a connected account’s external bank account using the Payouts API POST endpoint and specifying the source_balance of the payout as issuing.

Command Line[curl](#)`curl https://api.stripe.com/v1/payouts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d source_balance=issuing \
  -d amount=100 \
  -d currency=usd`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Fund from a bank account](#fund-from-bank-account)[Fund from a connected account's Stripe balance](#fund-from-connected-account-balance)[Retrieve an Issuing balance](#retrieve-an-issuing-balance)[Pay out an Issuing balance to an external account](#pay-out-an-issuing-balance)Products Used[Issuing](/issuing)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`