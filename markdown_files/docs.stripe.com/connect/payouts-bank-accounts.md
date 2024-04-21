htmlManage payout accounts for connected accounts | Stripe Documentation[Skip to content](#main-content)Manage payout accounts for connected accounts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fpayouts-bank-accounts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fpayouts-bank-accounts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Manage payout accounts for connected accounts

Learn how to manage external bank accounts and debit cards for connected accounts### Account types

Connect platforms can work with three different[account types](https://stripe.com/docs/connect/accounts).This content applies only to Express and Custom accounts.Payout accounts can be bank accounts or debit cards. Stripe recommends collecting external account details with the Connect Onboarding web form, which helps you:

- Save design and development time.
- Eliminate the need to store sensitive data such as account and routing numbers on your server.
- Eliminate the need to build form validations when users enter account details.

In the US, we also recommend using Stripe Financial Connections, which lets your users securely link their financial accounts to your business. It helps you:

- Increase onboarding conversion by preventing your accounts from having to interrupt the process to locate their account and routing numbers.
- Reduce first payout failure rates by eliminating errors that result from manual entry of account and routing numbers.
- Eliminate the need to store sensitive data such as account and routing numbers on your server.
- Eliminate the need to build form validations when accounts enter account details in custom onboarding forms.
- Enable your accounts to authenticate in fewer steps by reusing bank account details they’ve saved to[Link](https://support.stripe.com/questions/link-for-financial-connections-support-for-businesses). Accounts that save their account information at any of the Stripe businesses using Link can share their account details with your platform the next time they use Financial Connections.
- Access additional information on an account’s external bank account, such as[balances](/financial-connections/balances),[ownership details](/financial-connections/ownership), and[transactions](/financial-connections/transactions). You can mitigate fraud during onboarding by verifying that information, such as the name and address of the external bank account holder.

Financial Connections is free when you include Link. Otherwise, using it incurs fees.

Alternatively, if you use API onboarding for your connected accounts, you can collect payout account details with a custom form in your account onboarding flow.

Stripe-hosted onboardingDirect API calls from a custom formStripe-hosted onboarding for connected accounts uses a web form hosted by Stripe to collect the information required to onboard connected accounts. You can use Financial Connections with Stripe-hosted onboarding to collect external bank account details, but not debit card details.

Use Stripe Financial ConnectionsEnable manual entry of bank account details### Available in

United StatesStripe platforms in the US can enable Stripe Financial Connections within the Stripe-hosted onboarding form by following these steps:

1. Navigate to your[External Account settings](https://dashboard.stripe.com/settings/connect/payouts/external_accounts), where you manage optional Connect onboarding features.
2. For connected accounts where your platform collects account information when requirements change, including for Custom accounts, you must allow Stripe-hosted onboarding to collect external account details. UnderStripe-hosted onboarding for Custom accounts, allow Stripe to collect external account information by turning on the toggle.
3. UnderHow will bank account details be collected?, selectFinancial Connections.
4. (Optional)Request permission to access additional data on the accounts instantly verified with Financial Connections, such as balances, ownership details, and transactions. If you opt to request this additional information, you’ll be prompted to sign up for Stripe Financial Connections.

When external account detail collection is enabled, all connected accounts are prompted to authenticate their bank account using the Stripe-hosted modal UI embedded within the onboarding form.

![Image showing a Connect onboarding flow using Stripe Financial Connections to collect a payout account.](https://b.stripecdn.com/docs-statics-srv/assets/connect-custom-onboarding-financial-connections-onboarding.8937a023f6682c90bab8c0b39873909a.png)

A Connect onboarding flow using Stripe Financial Connections to collect a payout account.

If a connected account can’t instantly verify their bank account using Financial Connections, the verification process automatically falls back to manual entry:

![Image showing a Connect onboarding flow using the Stripe Financial Connections modal to collect a payout account using manual entry.](https://b.stripecdn.com/docs-statics-srv/assets/connect-custom-onboarding-financial-connections-manual-entry.930da1e01c9026b9014008d75958bc8c.png)

A Connect onboarding flow using the Stripe Financial Connections modal to collect a payout account using manual entry.

After onboarding, the specified bank account automatically attaches to the connected account.

### Retrieve data on a Financial Connections account Server-side

You can determine if your user linked a Financial Connections Account by retrieving any linked Financial Connections Accounts using their connected account ID. Be sure to specify their account ID in the Stripe-Account header.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/financial_connections/accounts \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "account_holder[account]"={{CONNECTED_ACCOUNT_ID}}`This returns an API response similar to the following:

`{
  "object": "list",
  "data": [
    {
      "id": "fca_zbyrdjTrwcYZJZc6WBs6GPid",
      "object": "financial_connections.account",
      "account_holder": {
        "account": '{{CONNECTED_ACCOUNT_ID}}',
        "type": "account"
      },
      ...
      "supported_payment_method_types": [
        "us_bank_account"
      ]
    }
    ...
  ]
}`If any Financial Connections accounts are listed, it indicates that the connected account linked them during the onboarding process. You can use the id value to access or refresh the data you specified in your External Account settings. To protect the privacy of your connected account’s data, you can only access the data you specified.

To start retrieving account data, follow the guides for balances, ownership, and transactions. On all subsequent account retrieval and refresh requests, be sure to include the Stripe-Account header with the connected account ID:

Command Line[curl](#)`curl https://api.stripe.com/v1/financial_connections/accounts/fca_zbyrdjTrwcYZJZc6WBs6GPid/refresh \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "features[]"=balance`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`