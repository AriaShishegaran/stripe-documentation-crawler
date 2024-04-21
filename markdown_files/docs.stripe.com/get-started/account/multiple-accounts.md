htmlMultiple accounts | Stripe Documentation[Skip to content](#main-content)Multiple separate accounts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fmultiple-accounts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fmultiple-accounts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)
Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Get started](/docs/get-started)Create an account# Multiple accounts

Learn how to create and manage multiple Stripe accounts.You can create additional Stripe accounts associated with your email address. You might create some accounts yourself, or you might be given access to other accounts as a team member. To create a new account, click on the name of your current Stripe account in the upper-left corner, and select New account. To switch the account you’re currently viewing in the Dashboard, click on the name of your current Stripe account in the upper-left corner and then select the account to switch to.

You must use separate Stripe accounts for projects, websites, or businesses that operate independently from one another. When you activate a new account, it’s subject to Stripe’s standard policies and pricing—it doesn’t inherit any special status or other similar considerations that might apply to your existing account.

Using additional accounts has a number of benefits:

- Separate tax and legal entity information: You can only associate each account with the tax ID and legal entity of one business. If you operate multiple businesses that have separate tax ID information (for example, separate legal entities), you must create additional accounts for each.


- Unique statement descriptor and public business information: Using the same Stripe account for separate businesses can cause confusion as the public business information used is the same for both. For example, a customer who purchases from your business “XYZ” might see a charge from your business “ABC” on their statement, potentially resulting in a dispute. Each additional account has its own public information to accurately describe your business and payments.


- Reporting and reconciliation: Separating the payments processed by your businesses helps you find payments, create and export reports, and reconcile payouts to your bank account.


- Payouts to separate bank accounts: Each additional account can use a separate bank account for payouts (although you can use the same bank account if you want).



If your business requires multiple separate accounts for local acquiring or maintaining separate business lines, you can create an organization for centralized reporting and management.

When you have multiple projects or businesses that operate under the same legal entity, you can use the same tax ID and business information across multiple accounts. Make sure to provide suitable public business information to avoid customer confusion.

## See also

- [Start a team](/get-started/account/teams)
- [User roles](/get-started/account/teams/roles)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`