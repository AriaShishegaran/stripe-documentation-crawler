htmlCollect an account to build data-powered products | Stripe Documentation[Skip to content](#main-content)Other data-powered products[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Fother-data-powered-products)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ffinancial-connections%2Fother-data-powered-products)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)
[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Financial Connections](/financial-connections)·[Home](/docs)[Payments](/docs/payments)[Financial Connections](/docs/financial-connections)# Collect an account to build data-powered products

Collect your user's account and use data such as balances, ownership details, and transactions to build products.WebiOSAndroidReact NativeWebViewAvailable in:Not sure about which Financial Connections integration to use? See our overview of integration options.

Financial Connections lets your users securely share their financial data by linking their external financial accounts to your business. You can use Financial Connections to access user-permissioned financial data such as tokenized account and routing numbers, account balances, account owner information, and historical transactions.

Some common examples of how you can use Financial Connections to improve product experiences for your users include:

- Mitigate fraud when onboarding a customer or business by verifying the[ownership](/financial-connections/ownership)information of an account, such as the name and address of the bank account holder.
- Help your users track expenses, handle bills, manage their finances and take control of their financial well-being with[transactions](/financial-connections/transactions)data.
- Speed up underwriting and improve access to credit and other financial services with transactions and balances data.
- Enable your users to connect their accounts in fewer steps with Link, allowing them to save and quickly reuse their bank account details across Stripe merchants.



[Set up StripeServer-side](#setup-stripe)Register for Financial Connections after we approve your account for live-mode access.

Use our official libraries for access to the Stripe API from your application:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`[Create or retrieve an account holderServer-side](#create-a-customer)Create a Customer object when users create an account with your business. By providing an email address, Financial Connections can optimize the authentication flow by dynamically showing a streamlined user interface, for returning Link users.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d email={{CUSTOMER_EMAIL}} \
  -d name={{CUSTOMER_NAME}}`[Create a Financial Connections SessionServer-side](#create-a-session)Before you can retrieve data from a user’s bank account with Financial Connections, your user must authenticate their account with the authentication flow.

Your user begins the authentication flow when they want to connect their account to your site or application. Insert a button or link on your site or in your application, which allows a user to link their account—for example, your button might say “Link your bank account”.

Create a Financial Connections Session by posting to /v1/financial_connections/sessions:

Command Line[curl](#)`curl https://api.stripe.com/v1/financial_connections/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "account_holder[type]"=customer \
  -d "account_holder[customer]"={{CUSTOMER_ID}} \
  -d "permissions[]"=balances \
  -d "permissions[]"=ownership \
  -d "permissions[]"=payment_method \
  -d "permissions[]"=transactions`1. Set`account_holder[customer]`to the Customer`id`.
2. Set the data`permissions`parameter to include the data required to fulfill your use case.
3. (Optional)set the`prefetch`parameter for retrieving the data on account creation.

The permissions parameter controls which account data you can access. You must request at least one permission. When completing the authentication flow, your user can see the data you’ve requested access to, and provide their consent to share it.

Consider the data required to fulfill your use case and request permission to access only the data you need. Requesting permissions that go well beyond your application’s scope might erode your users’ trust in how you use their data. For example, if you’re building a personal financial management application or a lending product, you might request transactions data. If you’re mitigating fraud such as account takeovers, you might want to request ownership details.

After your user authenticates their account, you can expand data permissions only by creating a new Financial Connections Session and specifying a new value for the permissions parameter. Your user must complete the authentication flow again, where they’ll see the additional data you’ve requested permission to access, and provide consent to share their data.

The optional prefetch parameter controls which data you retrieve immediately after the user connects their account. Use this option if you know you always want a certain type of data. It removes the need to make an extra API call to initiate a data refresh.

To preserve the option to accept ACH Direct Debit payments, request the payment_method permission.

[Collect a Financial Connections accountClient-side](#collect-an-account)Use the returned client_secret with Stripe.js to allow your user to connect their accounts. A client_secret allows client-side Stripe SDKs to make changes to the Financial Connections Session. Don’t store it, log it, embed it in URLs, or expose it to anyone other than your end user. Make sure that you have TLS enabled on any page that includes the client secret.

Use collectFinancialConnectionsAccounts to collect an account.

`const stripe = new Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY')
const financialConnectionsSessionResult = await stripe.collectFinancialConnectionsAccounts({
  clientSecret: "{{SESSION_CLIENT_SECRET}}",
});`This method loads the authentication flow, the client-side Stripe.js UI that helps your users link their financial accounts to you and Stripe.

The return value of stripe.collectFinancialConnectionsAccounts is a Promise. When the user completes the authentication flow, the Promise resolves with an object that contains the list of connected accounts:

`{
  "financialConnectionsSession": {
    "id": "fcsess_123",
    "accounts": [
      {
        "id": "fca_456",
        "object": "financial_connections.account",
        "category": "Checking",
        "display_name": "Premium Checking",
        "institution_name": "Test Bank",
        "last4": "4242"
      }
    ]
  }
}`If the user connects no accounts, or exits the authentication flow early, the response contains an empty accounts array.

Successful completion of the authentication flow also sends one financial_connections.account.created webhook per account connected.

[Retrieve data on a Financial Connections accountServer-side](#retrieve-additional-data)After your user has successfully completed the authentication flow, access or refresh the account data you’ve specified in the permissions parameter of the Financial Connections Session.

To protect the privacy of your user’s data, account data accessible to you is limited to the data you’ve specified in the permissions parameter.

Follow the guides for balances, ownership and transactions to start retrieving account data.

[OptionalAccept an ACH Direct Debit payment from a Financial Connections account](#accept-ach-direct-debit)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up Stripe](#setup-stripe)[Create or retrieve an account holder](#create-a-customer)[Create a Financial Connections Session](#create-a-session)[Collect a Financial Connections account](#collect-an-account)[Retrieve data on a Financial Connections account](#retrieve-additional-data)Products Used[Financial Connections](/financial-connections)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`