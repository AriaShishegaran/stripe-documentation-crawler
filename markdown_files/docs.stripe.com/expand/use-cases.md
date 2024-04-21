htmlUse cases for expanding responses | Stripe Documentation[Skip to content](#main-content)Use cases[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fexpand%2Fuse-cases)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fexpand%2Fuse-cases)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)
[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)API[Expanding responses](/docs/expand)# Use cases for expanding responses

Learn how the expand attribute helps you perform common tasks.## See the Stripe fee for a given payment

In some cases, you may want to see the processing fees associated with a payment. You can only see the Stripe fees after a payment has been processed. After a payment succeeds, the fees are available on the associated Charge’s balance transaction. Rather than retrieving a balance transaction separately, you can retrieve it in a single call using expand, for example:

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents/pi_1Gpl8kLHughnNhxyIb1RvRTu \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "expand[]"="latest_charge.balance_transaction" \
  -G`Users on API version 2022-08-01 or older:

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents/pi_1Gpl8kLHughnNhxyIb1RvRTu \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "expand[]"="charges.data.balance_transaction" \
  -G`NoteA payment intent must be captured and have a status of succeeded for the Stripe fees to be available.

## See the charges included in a payout

Every automatic payout is tied to historical changes to the balance of your Stripe account. The API records these historical changes as balance transactions, which you can retrieve using List Balance Transactions. From a list of balance transactions, you can expand the source property to gather information on what triggered the change to the account balance (Charge, Refund, Transfer, and so on). For example:

Command Line[curl](#)`curl https://api.stripe.com/v1/balance_transactions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d payout=po_1Gl3ZLLHughnNhxyDrOia0vI \
  -d type=charge \
  -d "expand[]"="data.source" \
  -G`NoteYou can only retrieve balance transaction history on automatic payouts. If you have manual payouts enabled, you must track transaction history on your own.

If you’re using Connect with destination charges, you can retrieve the same information on behalf of your connected accounts. One difference is that destination charges involve both a transfer and a linked payment (in the form of a Charge object) to move funds to a connected account. So when listing the balance transactions bundled in your connected account’s payouts, each balance transaction’s source is linked to the transfer’s payment rather than the originating Charge. To retrieve the originating Charge, you need to expand a payment’s linked transfer through the source_transfer property; and from there, expand the transfer’s source_transaction property:

Command Line[curl](#)`curl https://api.stripe.com/v1/balance_transactions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d payout=po_1G7bnaD2wdkPsFGzdVOqU44u \
  -d type=payment \
  -d "expand[]"="data.source.source_transfer.source_transaction" \
  -H "Stripe-Account: acct_1G7PaoD2wdkPsFGz" \
  -G`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[See the Stripe fee for a given payment](#stripe-fee-for-payment)[See the charges included in a payout](#charges-in-payout)Products Used[Payments](/payments)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`