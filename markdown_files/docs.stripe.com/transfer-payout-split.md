htmlTransfer Payout Split: Stripe-Version 2017-04-06 | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftransfer-payout-split)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftransfer-payout-split)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# Transfer Payout Split: Stripe-Version 2017-04-06

On April 6, 2017, Stripe split the /v1/transfers resource into /v1/transfers and /v1/payouts. This is a versioned change–your existing integrations don’t need to change.

Since Stripe was launched, we’ve used the word transfer to mean moving money out of Stripe and into your bank account or debit card. But when Connect was launched years later, we co-opted that term to also mean moving money between a platform and its connected accounts.

This ultimately turned out to be confusing. These are conceptually different flows of funds as they apply to a business. This made it difficult to document transfers, and also bloated the /v1/transfers API because the fields needed to support each flow of funds were different.

As of Stripe-Version 2017-04-06:

- Payoutswill mean moving money from Stripe to your bank account or debit card and will be represented by`/v1/payouts`.
- Transferswill mean moving money between Stripe accounts as part of Connect and will be represented by`/v1/transfers`.
- Relative to the legacy`/v1/transfers`resource, the new`/v1/transfers`resource won’t have these fields:  - `method`- this only applies to[payouts](/payouts).
  - `status`- this only applies to payouts.
  - `type`- this only applies to payouts.
  - `bank_account`- this only applies to payouts.
  - `card`- this only applies to payouts.
  - `failure_message`- this only applies to payouts.
  - `failure_code`- this only applies to payouts.
  - `description`- description was confusing because it applied to the transfer but not the resultant payment on the connected account. Use`metadata`to attach additional information to a transfer.
  - `application_fee`- application_fee is no longer necessary. See[Connect destination charges](/connect/destination-charges).


- Relative to the legacy`/v1/transfers`, the new`/v1/payouts`resource won’t have these fields:  - `reversals`- payouts can now be simply canceled.
  - `reversed`- refer to the payout status.
  - `application_fee`- this only applies to legacy transfers.
  - `destination_payment`- this only applies to transfers.
  - `source_transaction`- this only applies to legacy transfers.
  - `description`- description was removed because it didn’t provide enough value. Use metadata to attach additional information to a payout.


- On the`/v1/payouts`resource, the`date`field was renamed to`arrival_date`.
- To send a payout to your default bank account or debit card, instead of including the parameter`destination=default_for_currency`, simply omit the`destination`entirely.
- Canceling a payout is now done via`POST /v1/payouts/:id/cancel`. The balance transaction resulting from a cancellation is available via the`cancellation_balance_transaction`field on the payout. The`status`of a canceled payout is`canceled`.
- When creating a transfer, you can now only use a charge as the`source_transaction`. Previously, it was possible to use any transaction (such as an application fee, or an adjustment) as a`source_transaction`. This did not mesh well with the intended use case of tagging outgoing transfers with the incoming source of funds, so this is no longer supported on the new API version.
- Payouts now generate these events:`payout.created`,`payout.failed`,`payout.reversed`,`payout.paid`,`payout.updated`, which are the equivalent of the legacy`transfer.*`events.
- Transfers no longer generate these events:`transfer.paid`and`transfer.failed`.
- Balance transactions can have these types as they relate to payouts:`type`∈ {`payout`,`payout_failure`,`payout_cancel`}
- Balance transactions can have these types as they relate to transfers:`type`∈ {`transfer`,`transfer_refund`}
- Fields on the[Account API](/api/accounts)were renamed:  - `transfers_enabled`→`payouts_enabled`
  - `transfer_schedule`→`payout_schedule`
  - `transfer_statement_descriptor`→`payout_statement_descriptor`


- Transfers to deprecated Recipients API (link) are no longer represented on this version of the API. Use a legacy API version to access any transfers to recipients that you may have.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`