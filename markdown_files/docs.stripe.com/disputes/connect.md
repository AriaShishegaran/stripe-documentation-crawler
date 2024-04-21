htmlDisputes on Connect platforms | Stripe Documentation[Skip to content](#main-content)Disputes on Connect[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdisputes%2Fconnect)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdisputes%2Fconnect)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)
[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Radar](/radar)·[Home](/docs)[Get started](/docs/get-started)[Protect against fraud](/docs/radar)[Disputes and fraud](/docs/disputes)# Disputes on Connect platforms

Learn about the dispute responsibilities on Connect platforms.If you’re using Connect and Custom or Express accounts, your platform is ultimately responsible for any disputes that occur. For payments created on Standard accounts using direct charges, those accounts are responsible for disputes and any funds are withdrawn from their balance—not the platform.

When a disputed payment was made directly on an Express or Custom account, Stripe debits the disputed amount and dispute fee from that account’s balance. However, the platform account is ultimately liable. If Stripe can’t debit the disputed amount and fee from the connected account, we debit it from the platform account.

Security tipIf the connected account turns out to be fraudulent, it’s unlikely to have an available balance. In that case, Stripe deducts the disputed amount and fee from the platform account.

If the disputed payment was created through the platform using destination charges or separate charges and transfers with or without on_behalf_of, the platform account is automatically debited for the disputed amount and fee. When this happens, the platform can attempt to recover funds from the connected account by reversing the transfer either through the Dashboard or by creating a transfer reversal.

If there is a negative balance on the connected account, Stripe attempts to debit its card issuer account only if debit_negative_balances is set to true.

## See also

- [Responding to disputes](/disputes/responding)
- [Dispute categories](/disputes/categories)
- [Preventing disputes and fraud](/disputes/prevention)
- [Using Radar with Connect](/connect/radar)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`