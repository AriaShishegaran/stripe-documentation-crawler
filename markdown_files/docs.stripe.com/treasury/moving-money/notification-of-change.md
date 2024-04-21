htmlACH Notification of Change handling | Stripe Documentation[Skip to content](#main-content)ACH Notification of Change handling[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoving-money%2Fnotification-of-change)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoving-money%2Fnotification-of-change)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)[Treasury](#)
[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Treasury](/treasury)·[Home](/docs)[Banking as a service](/docs/financial-services)[Treasury](/docs/treasury)[Working with SetupIntents, PaymentMethods, and BankAccounts](/docs/treasury/moving-money/working-with-bankaccount-objects)# ACH Notification of Change handling

Learn how external account information is updated.When you originate an ACH transaction with Stripe (for example, using InboundTransfer, OutboundTransfer, or OutboundPayment objects with Treasury), the financial institution receiving the transaction might return a Notification of Change (NOC). This is a message indicating that new information is available about the destination account (such as a new account number or routing number).

ACH network rules require Stripe to update saved account information when we receive an NOC. We automatically process the NOC by updating the relevant PaymentMethod or BankAccount object and notify you through a webhook. You might want to monitor these webhooks to inform your users that account information has changed or to update account information that you’ve persisted outside of Stripe.

NOC typeFields updatedAccount number`account_number`,`last4`,`fingerprint`Routing number`routing_number`,`fingerprint`Account use (for example, checking or savings)`account_type`,`fingerprint`NOCs aren’t processed for OutboundPayment objects where payment method details are provided inline (using destination_payment_method_data) as there is no persisted PaymentMethod or BankAccount object in this case to update.

## NOC for a PaymentMethod

When we receive an NOC for a transaction originated with a PaymentMethod object:

- Stripe updates the`PaymentMethod`and triggers a`payment_method.updated`webhook.
- If the`PaymentMethod`is attached to a`Customer`(for use with`OutboundPayment`objects), Stripe triggers a`customer.source.updated`webhook.
- If the`PaymentMethod`is attached directly to a Stripe account (for use with`InboundTransfer`or`OutboundTransfer`objects), Stripe triggers an`account.external_account.updated`webhook.

## NOC for a BankAccount

When we receive an NOC for a transaction originated with a BankAccount object:

- Stripe updates the`BankAccount`object.
- If the`BankAccount`is attached to a`Customer`(for use with`OutboundPayment`objects), Stripe triggers a`customer.source.updated`webhook.
- If the`BankAccount`is attached directly to a Stripe account (for use with`InboundTransfer`or`OutboundTransfer`objects), Stripe triggers an`account.external_account.updated`webhook.

In cases where the BankAccount that’s set up as your platform’s primary external account is updated, Stripe also notifies you by email. We don’t send an email for updates to external accounts that are attached to your merchants’ Stripe accounts, or for updates to external accounts attached to Customer objects.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[NOC for a PaymentMethod](#noc-for-a-paymentmethod)[NOC for a BankAccount](#noc-for-a-bankaccount)Products Used[Treasury](/treasury)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`