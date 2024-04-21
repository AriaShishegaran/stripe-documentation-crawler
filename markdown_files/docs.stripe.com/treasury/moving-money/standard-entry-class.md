htmlACH Standard Entry Class handling | Stripe Documentation[Skip to content](#main-content)ACH Standard Entry Class handling[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoving-money%2Fstandard-entry-class)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoving-money%2Fstandard-entry-class)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)[Treasury](#)
[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Treasury](/treasury)·[Home](/docs)[Banking as a service](/docs/financial-services)[Treasury](/docs/treasury)[Working with SetupIntents, PaymentMethods, and BankAccounts](/docs/treasury/moving-money/working-with-bankaccount-objects)# ACH Standard Entry Class handling

Learn how SEC codes are determined for ACH transfers.Each ACH transaction has an associated Standard Entry Class (SEC) code that describes the accounts involved and how the transaction was authorized.

Stripe Treasury determines the SEC code based on whether the account receiving the ACH entry is owned by a company or an individual. You specify the account holder type in destination_payment_method_data.us_bank_account.account_holder_type when:

- You make[OutboundPayments](/treasury/moving-money/financial-accounts/out-of/outbound-payments)
- You set up a[stored PaymentMethod](/treasury/moving-money/working-with-bankaccount-objects#setupintents)

Only send InboundTransfers and OutboundTransfers to accounts owned by the FinancialAccount owner and with a company owner type.

SEC codes are determined based on the receiving account’s owner type as follows:

Money movementOwner typeSEC codeInboundTransfer`company``CCD`OutboundTransfer`company``CCD`OutboundPayment`company``CCD`OutboundPayment`individual``PPD`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`