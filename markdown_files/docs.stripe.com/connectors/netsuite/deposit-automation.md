htmlDeposit automation | Stripe Documentation[Skip to content](#main-content)Deposit automation[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fnetsuite%2Fdeposit-automation)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fnetsuite%2Fdeposit-automation)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[NetSuite](/docs/connectors/netsuite/overview)# Deposit automation

Use the connector to automate the bank reconciliation process.The Stripe Connector for NetSuite automates the bank reconciliation process by creating bank deposits in NetSuite for all of your Stripe payouts. The connector also automates fee calculation, the refund life cycle, the dispute life cycle, and handling of multiple currencies and subsidiaries. This means you only need to match the bank deposit record to the Stripe deposits on your bank statement. Every automated payment workflow that the connector supports includes deposit automation.

## How it works

When you use the connector, the automated bank reconciliation process occurs daily as follows:

1. The connector creates payments and refunds for each Stripe transaction, and posts these transactions in the Undeposited Funds account in NetSuite.
2. Stripe notifies the connector that a bank transfer (Stripe payout) has successfully arrived at your bank.
3. The connector creates a bank deposit record in NetSuite that contains all of the payments, refunds, and disputes from that day’s bank deposit.
4. The connector calculates any fees for processing, currency conversion, disputes, and refunds, and includes these as separate line items that post to your specified expense accounts.
5. The connector makes sure that the deposit total and deposit date match your bank statement.

## See also

- [Invoice automation](/connectors/netsuite/invoice-automation)
- [Invoice payment page](/connectors/netsuite/invoice-payment-page)
- [Customer payment page](/connectors/netsuite/customer-payment-page)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[How it works](#how-it-works)[See also](#see-also)Products Used[Invoicing](/invoicing)[Payments](/payments)[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`