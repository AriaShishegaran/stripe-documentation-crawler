htmlMoving money out of Treasury financial accounts | Stripe Documentation[Skip to content](#main-content)Moving money out of financial accounts[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoving-money%2Fmoving-money-out-of-financial-accounts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoving-money%2Fmoving-money-out-of-financial-accounts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)[Treasury](#)
[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Treasury](/treasury)·[Home](/docs)[Banking as a service](/docs/financial-services)[Treasury](/docs/treasury)# Moving money out of Treasury financial accounts

Learn the requests available to move money out of financial accounts.You can use a number of methods to move funds from a Treasury financial account to another account (either an external account or another Treasury financial account):

- Originate an`OutboundPayment`to move money to a third party’s external account or financial account throughACH,wire transfer, or the Stripe network.
- Originate an`OutboundTransfer`to move money to an external account belonging to the same user through ACH or wire transfer.
- Initiate a card transaction through Stripe Issuing to send money usingcard networks.
- Receive a`ReceivedDebit`(initiated by the owner of an external account) to pull money from the financial account through ACH.

### Money movement with PaymentMethods

Within Stripe, you can save payment method information using a PaymentMethod object. You might use PaymentMethods to save your vendors’ account data so you don’t have to re-enter and collect their information for every payment you make to them.

You can attach PaymentMethods containing bank account information to a customer (for sending money to a third party) or to a Stripe account (for sending money to a company’s own external bank account). In both cases, you create the PaymentMethod using SetupIntent endpoints.

The type of Treasury requests you make with a PaymentMethod depends on how they’re attached:

- For customer-attached, use`PaymentIntent`and`OutboundPayment`requests.
- For account-attached, use`InboundTransfer`and`OutboundTransfer`requests.

See Working with SetupIntents, PaymentMethods, and BankAccounts for more information.

## Handling returned funds

The destination for OutboundTransfers and OutboundPayments can reject the relative flow. For example, the destination address might not exist and the OutboundTransfer or OutboundPayment fails. This can occur over the ach and us_domestic_wire networks. CreditReversals can also return OutboundPayments over the stripe network. In the case of returned funds, the OutboundTransfer or OutboundPayment transitions to the returned status and Stripe creates a transaction to return the funds to the source financial account. Stripe also triggers a treasury.outbound_transfer.returned or treasury.outbound_payment.returned webhook.

## See also

- [Moving money with Treasury using OutboundPayment objects](/treasury/moving-money/financial-accounts/out-of/outbound-payments)
- [Moving money with Treasury using OutboundTransfer objects](/treasury/moving-money/financial-accounts/out-of/outbound-transfers)
- [Moving money with Treasury using ReceivedDebit objects](/treasury/moving-money/financial-accounts/out-of/received-debits)
- [Moving money with Treasury using DebitReversal objects](/treasury/moving-money/financial-accounts/out-of/debit-reversals)
- [Working with Stripe Issuing cards](/treasury/account-management/issuing-cards)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Handling returned funds](#handling-returned-funds)[See also](#see-also)Products Used[Treasury](/treasury)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`