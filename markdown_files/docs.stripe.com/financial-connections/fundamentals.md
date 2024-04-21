htmlFinancial Connections fundamentals | Stripe Documentation[Skip to content](#main-content)Fundamentals[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Ffundamentals)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Ffundamentals)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)
[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Financial Connections](/financial-connections)·[Home](/docs)[Payments](/docs/payments)[Financial Connections](/docs/financial-connections)# Financial Connections fundamentals

Learn how Financial Connections works.The Stripe Financial Connections product has two main components: end user bank account collection through the authentication flow, and data retrieval on the collected accounts. There are a number of ways to integrate Financial Connections. In the following example, we assume you’re using a Financial Connections Session. However, the overall concepts and flow diagrams function similarly with payments integrations such as Setup or Payment Intents.

To initialize and complete the Financial Connections authentication flow:

1. Your user initiates the bank account linking process on your client.
2. Create a Financial Connections Session on your server to drive the authentication flow.
3. Return the session’s`client_secret`to your client.
4. Initiate the authentication flow using[collectFinancialConnectionsAccounts](/js/financial_connections/collect_financial_connections_accounts).
5. Your user completes the flow, which attaches[accounts](/api/financial_connections/accounts)to the session.

After you have your user’s authenticated accounts, you can initiate data refreshes from your server. When the refreshes are complete, you can retrieve the account data.

[Authentication flow](#authentication-flow)The authentication flow is the client-side UI that allows your user to consent to data sharing and link their financial accounts to you and Stripe.

Embed the UI in your client-side user flow. It works across all major browsers and platforms, including web, iOS, Android, and mobile web views.

![Authentication Flow](https://b.stripecdn.com/docs-statics-srv/assets/canonical-flow-v3.e0b5244b9d16ed2e03e6ed656e5ab1df.png)

Your user follows these steps during the authentication flow:

StepDescriptionGive consentUsers consent to share requested data.Select institutionUsers select their bank either from frequently chosen banks or by searching over more than 5,000 other supported banks.Log into bankUsers authenticate access to their accounts by logging into their bank.Select account(s)Users select which specific account(s) to link.SuccessUsers see a success screen after authentication completes successfully.For payments integrations such as Setup Intents, you can configure the authentication flow to use microdeposits as a fallback using the verification_method parameter.

### Return user optimization

Financial Connections enables your users to connect their accounts in fewer steps with Link, allowing them to save and quickly reuse their bank account details across Stripe merchants.

![Authentication Flow](https://b.stripecdn.com/docs-statics-srv/assets/return-user-flow-v3.5a17b62098a2cfb95d42bfe37f641d1e.png)

To enable return user optimization, you must launch the Financial Connections authentication flow with a Customer that has an email address. See our guide for examples of how to do this for your specific use case.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d email={{CUSTOMER_EMAIL}}`[How Stripe links financial accounts](#how-stripe-links-financial-accounts)During the authentication flow, your user logs into their bank through either an OAuth (bank-hosted) or non-OAuth flow to authenticate access to their accounts. Stripe typically defaults the authentication flow to OAuth if it’s available at the financial institution. Your integration doesn’t need to treat OAuth accounts differently than non-OAuth accounts.

OAuth is a standardized protocol that allows users to grant applications (for example, Stripe) access to their information within other applications (for example, bank apps). This protocol eliminates the need for users to share their login credentials.

Here’s how OAuth and Financial Connections function together:

- When your user selects their bank in the Financial Connections authentication flow, they’re sent to their bank’s website or mobile app.
- Your user logs into their bank and grants the bank permission to share account data (such as balances or transactions) with Stripe.
- The bank redirects your user back to the authentication flow, passing a token that allows Stripe access to approved bank account information.
- Your user never shares their login credentials with Stripe.

In non-OAuth flows, end users provide credentials directly to Stripe or one of our trusted partners.

[Financial Connections Account](#financial-connections-account)Successful completion of the authentication flow creates one Financial Connections Account for each account authorized by your user. The Financial Connections Account is the API object you use to access additional account data, such as balances and transactions. They represent external financial accounts such as checking, savings, loan, or credit card accounts. See the account_subcategory field on the account for a list of all account types we support. Only cash-based accounts, such as checking and savings accounts, allow ACH (Automated Clearing House) transfers.

[Data permissions](#data-permissions)After collecting an account, you immediately receive access to the following information:

- Last four digits of the account number
- Account category such as checking or savings
- Account nickname, if available

To access additional account data such as balances or transactions, you must request access with data permissions. You configure data permissions on server-side objects such as the Financial Connections Session using the permissions parameter.

Data AvailablePermissionsDescriptionAccount details`payment_method`Tokenized account and routing number (required for money movement)Account owners`ownership`Account owner names and mailing addressesBalances`balances`Current and available balancesTransactions`transactions`Pending and posted transactionsConsider the data required to fulfill your use case and request permission to access only the data you need. Requesting permissions that go well beyond your application’s scope may erode your users’ trust in how you use their data. For example, if you’re building a personal financial management application or a lending product, you might request transactions data. If you’re mitigating fraud such as account takeovers, you might want to request ownership details.

During the authentication flow, your users can see the data types that you’ve requested access to. They must provide their consent to share this data. To expand the data types you have access to, your user needs to complete the authentication flow again with the new data permissions.

Consult the balances integration guide for an example of how to access financial account data, or learn more about use cases for the different data types.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Authentication flow](#authentication-flow)[How Stripe links financial accounts](#how-stripe-links-financial-accounts)[Financial Connections Account](#financial-connections-account)[Data permissions](#data-permissions)Products Used[Financial Connections](/financial-connections)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`