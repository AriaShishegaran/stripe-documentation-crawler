htmlLinked external accounts | Stripe Documentation[Skip to content](#main-content)Linked external accounts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Flinked-external-accounts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Flinked-external-accounts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)
Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Get started](/docs/get-started)Create an account# Linked external accounts

Manage your linked external accounts.When you first set up your Stripe account, we ask you to connect your bank account so that you can receive payouts. If you want Stripe to access additional account information, you can link a financial account. This allows Stripe to better serve your business needs and provide necessary information for credit and risk reviews. Linking your account also reduces the need for us to collect additional financial information in the future, potentially reducing the frequency of credit and other risk reviews.

Stripe might use your financial account information to:

- Link your financial account for[payouts](/payouts).
- Evaluate eligibility for loans or other Stripe products.
- Enable additional Stripe product features.
- Re-evaluate reserve balances during risk reviews.

NoteWe handle data from your linked financial accounts according to the Stripe Services Agreement, Stripe Privacy Policy and the partner terms. Stripe’s partner can only obtain financial account information as authorized by you. Stripe doesn’t sell your data to unaffiliated third parties.

## Financial account data

With your consent, we can access your linked account to retrieve the following information:

- Account details: Account type, account number, current balance, and historical balances.
- Contact information: Your name, email address, phone number, physical address, and other details held by your financial account.
- Account transactions: Each transaction’s amount, date, and description.

Here are a few Stripe products and services that rely on your financial account information:

- Payouts: Stripe uses your financial account information (specifically, the account number and routing number) to verify your account to enable[payouts](/payouts). You can link this account during onboarding, or at a later time by using yourLinked external accountssettings in the Stripe Dashboard.
- Risk: We analyze your financial account information to ascertain if a[reserve](https://support.stripe.com/topics/reserves)is required, and decide the appropriate amount for that reserve. Linking your financial account allows Stripe to continually reassess your risk profile, which could help reduce or eliminate the need for a reserve.
- Corporate Card: We use your financial account information during the underwriting process to determine your[Corporate Card](/issuing)credit limit. This limit can vary based on changes in your financial account information. If you unlink a financial account, it might affect your ability to use your Corporate Card.
- Capital:[Stripe Capital](/capital/eligibility)uses your financial account information to evaluate your loan eligibility and the details of your loan offer.

The type of data available to Stripe might vary based on your financial account or our technology partner. Go to your Linked external accounts settings to see the accounts you’ve linked to Stripe and what information you’ve shared with different Stripe products.

NoteWe have organizational, technical, and administrative measures in place to protect your financial account data from unauthorized access, destruction, loss, alteration, or misuse within our organization. Should you believe that your interaction with us is no longer secure (for instance, if you feel that the security of your account has been compromised), please contact us immediately.

## Link a financial account

If your Dashboard prompts you to Link your bank account to Stripe, follow these steps:

1. ClickLink bank accountin theLink your bank account to Stripebanner in your Dashboard.
2. ClickLink your account.
3. Choose your bank account provider and enter your bank account login details.
4. Select all accounts or specific accounts (such as checking or savings accounts) and clickLink accounts.
5. To add multiple bank accounts, clickLink another account. If not, clickDone.
6. You can verify the successful linking of bank accounts on the[Linked external accounts settings](https://dashboard.stripe.com/settings/linked-accounts).

You can also link your financial accounts directly from the Dashboard by following these steps:

1. Visit the[Linked external accounts settings](https://dashboard.stripe.com/settings/linked-accounts)in your Dashboard.
2. Click+ Add account.
3. Choose your bank account provider and enter your bank account login credentials.
4. Select all or specific accounts (such as checking or savings accounts) and clickLink Accounts.
5. To add multiple bank accounts, clickLink another account. If not, clickDone.
6. Check theLinked external accountspage to verify that the bank accounts were successfully linked.

## Data management

You can control which Stripe products use your account data. By default, when you link your financial accounts, this account data is shared with Stripe products as shown on the Link external accounts settings. From this page, you can control which Stripe products receive and use your data. You also have the option to opt out of sharing your financial account data, which might affect your ability to use certain products and features.

### Data retrieval frequency

How often Stripe accesses your data depends on the products you use. For instance, when assessing a risk reserve on your account, we might access your financial account information as often as daily because understanding your business’s risk profile requires this information.

For the Corporate Card, we might monitor your financial account data daily to assess if a change in your credit limit is necessary. For other products, such as Capital, we might get your financial account data once a week or once a month.

### Data retention duration

We retain your financial account information for as long as we’re providing services to you. We also keep this information to comply with our tax, accounting, and financial reporting obligations, to meet our contractual commitments to our financial partners, and where data retention is mandated by the payment methods we support. Even if you close your Stripe account, we might still need to retain your financial account information for a certain period following any limitation periods and record-keeping requirements imposed by applicable law.

### Data sharing

We use your financial account information as outlined in the Stripe Privacy Policy. We only use your data for internal purposes, such as offering additional products, services, or features. Stripe doesn’t sell or rent your financial account information to marketers or unaffiliated third parties. We might share your data with trusted entities (like service providers, business partners, third parties authorized by you to access this information, and for compliance purposes) as stated in our privacy policy.

### Revoke consent

At any time, you can revoke your consent by visiting your Link external accounts settings and clicking Remove account on any account you want to unlink. After you revoke your consent, we stop obtaining your account data. You can learn more about what happens when you disconnect an account.

Choosing not to link a financial account, or unlinking one, might make you ineligible to access or receive offers for additional products or services, enhancements to current products, or services. In some cases, we might request alternative information, such as financial statements.

## Trusted entity identification

When you link a financial account with Stripe, we become the primary recipient of your account data. Depending on the purpose for linking your account, we may also share this data with certain financial institutions or service providers involved in offering Stripe Capital and other financial services. For example, if you obtain a loan through Stripe Capital, we might share your account data with service providers that help manage your loan. Stripe only shares your data as set out in the Stripe Privacy Policy.

## Stripe’s technology partners

We work with third-party data aggregators, namely Finicity and MX, to obtain the data you’ve agreed to share with us and other reliable entities. When you enter your login credentials in the credential dialog, you might be sharing this information with Finicity and MX, or otherwise allowing these third-party data aggregators access to your accounts. Finicity and MX use your login details or your authorization to continually access your account data and provide this data to Stripe and other trusted entities authorized by you to receive it.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Financial account data](#financial-account-data)[Link a financial account](#link-financial-account)[Data management](#data-management)[Trusted entity identification](#trusted-entity-identification)[Stripe’s technology partners](#stripe-technology-partner)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`