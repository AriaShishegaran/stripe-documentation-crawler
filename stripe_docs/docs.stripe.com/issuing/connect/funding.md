# Funding Issuing balances with Connect

Before an issued card can be used for transactions, you must first allocate funds to the connected account’s Issuing balance associated with the card. An Issuing balance holds funds reserved for the card and is safely separated from earnings, payouts, and funds from other Stripe products.

[Issuing balance](/issuing/funding/balance)

[payouts](/payouts)

[Fund from a bank account](#fund-from-bank-account)

## Fund from a bank account

You have two options for funding an Issuing balance from an external account that each have different setups: pull funding and push funding.

- Pull funding is the default funding option in the US and isn’t available in the EU or the UK. You need to verify external bank accounts, which usually causes a delay in transferring funds (up to 5 business days). This option allows you to control and identify which bank your top-up originates from.

- Push funding is available in the UK and EU and as a beta in the US. This options allows you to originate the funds from your own bank account to Stripe. You might be able to receive funds the same day with push funding, which depends on the process you use (for example, ACH or wire transfer).

Before you can top-up a connected account from your user’s bank account, you must first collect and verify their account information. Stripe provides the option of  collection through Stripe.js with verification using microdeposits.

[Stripe.js](/payments/elements)

To debit the user’s bank account for funding, you will need to collect their bank account information and submit evidence of their authorization to debit their account. This is known as a mandate, and ensures both you and Stripe remain compliant with ACH network rules, as well as provide you with access to evidence to ease in any dispute resolution.

[mandate](/api/sources/create#create_source-mandate)

Create a form that captures:

- Name

- Routing number

- Account number

As your customers submit the mandate, you should record:

- IP address

- User agent

- Date

If instead you prefer to collect mandates from your users offline (such as via phone or a paper agreement), you won’t upload evidence of acceptance to Stripe. You should maintain your own record of the acceptance and provide us a contact email in case the evidence is requested.

Create a token using the Bank Account Token API, and then use it to create a source. Create both the bank account token and source on the connected account you want to fund.

[Bank Account Token API](/api/tokens/create_bank_account)

Store these Source tokens in your own system where your integration can retrieve them. Stripe currently doesn’t provide a way to programmatically retrieve or list the tokens after they’re created.

Create a source using the token you obtained:

Two small deposits with the statement description ACCTVERIFY are sent to the bank account within 1-2 days. You should collect these two amounts from your user to verify the bank account.

Fund the Issuing balance on your connected account with top-ups by passing in the source that was made and setting the destination_balance to issuing.

[Fund from a connected account's Stripe balanceBeta](#fund-from-connected-account-balance)

## Fund from a connected account's Stripe balanceBeta

You must sign up for the Balance Transfer API private beta to transfer funds from your Stripe balance into your Issuing balance.

[sign up for the Balance Transfer API private beta](#request-early-access)

Transfers from your connected account’s Stripe balance are instant and available 24x7 in the US, or take one business day in the UK and euro area countries. This allows you to quickly and easily utilize earned funds from Stripe Payments for spend with Stripe Issuing.

You can only move an amount up to the available Stripe balance. Funds won’t be available in the Issuing balance while the transfer is pending.

Use the retrieve balance endpoint to get your available Stripe balance amounts broken down by source_type.

[retrieve balance](/api/balance/balance_retrieve)

[source_type](/api/balance/balance_object#balance_object-available-source_types)

Access to the Balance Transfer API is currently limited to beta users. You must be an Issuing customer to join the beta. To request access to the beta, log in to your Stripe account and refresh the page. Contact Stripe for more information.

[Contact Stripe](https://stripe.com/contact/sales)

[Retrieve an Issuing balance](#retrieve-an-issuing-balance)

## Retrieve an Issuing balance

To check the current Issuing balance of a connected account, call the Balance API GET endpoint and pass the connected account ID into the header.

[Balance API](/api/balance/balance_retrieve)

Thebalance object is returned with a corresponding issuing object that includes the current available balance:

[Pay out an Issuing balance to an external account](#pay-out-an-issuing-balance)

## Pay out an Issuing balance to an external account

The funds in an Issuing balance can also be paid out to a connected account’s external bank account using the Payouts API POST endpoint and specifying the source_balance of the payout as issuing.

[external bank account](/api/external_accounts)

[Payouts API](/api/payouts/create)
