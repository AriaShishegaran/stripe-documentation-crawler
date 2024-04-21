# Issuing authorizations

When a card is used to make a purchase, it generates an authorization request, which is approved or declined based on the following steps:

- Stripe checks that the balance used for Issuing has sufficient funds, that the card is active, and that your spending controls allow the authorization. Sometimes, Stripe immediately approves or declines the authorization request at this stage.

Stripe checks that the balance used for Issuing has sufficient funds, that the card is active, and that your spending controls allow the authorization. Sometimes, Stripe immediately approves or declines the authorization request at this stage.

[balance used for Issuing](/issuing/funding/balance)

[spending controls](/issuing/controls/spending-controls)

[immediately approves or declines the authorization request](#scenarios-without-a-real-time-authorization-request)

- Stripe sends an issuing_authorization.request event. If you don’t have a real-time authorization webhook, we approve the authorization without sending the issuing_authorization.request.Listen for Stripe eventsSet up a real-time authorization webhook to listen for this event so you can synchronously approve/decline Authorizations.

Stripe sends an issuing_authorization.request event. If you don’t have a real-time authorization webhook, we approve the authorization without sending the issuing_authorization.request.

Set up a real-time authorization webhook to listen for this event so you can synchronously approve/decline Authorizations.

[real-time authorization webhook](/issuing/controls/real-time-authorizations)

- You can approve or decline the authorization by responding directly to the webhook event. If you don’t approve or decline the issuing_authorization.request within 2 seconds, Stripe uses your webhook timeout settings to approve or decline the authorization.

You can approve or decline the authorization by responding directly to the webhook event. If you don’t approve or decline the issuing_authorization.request within 2 seconds, Stripe uses your webhook timeout settings to approve or decline the authorization.

[approve or decline](/issuing/controls/real-time-authorizations)

[webhook timeout settings](https://dashboard.stripe.com/settings/issuing)

- Stripe sends an issuing_authorization.created event, notifying you of the Authorization creation and decision.

Stripe sends an issuing_authorization.created event, notifying you of the Authorization creation and decision.

[Authorization](/api#issuing_authorization_object)

## Scenarios without a real-time authorization request

Sometimes, Stripe receives an authorization request from the card network and approves or declines it without sending you an issuing_authorization.request event:

- If Stripe decides that the authorization request can’t be approved (for example, because the card is inactive or your spending controls don’t allow it), we’ll decline it.

[spending controls](/issuing/controls/spending-controls)

- If you don’t have a real-time authorization webhook configured, and we don’t have a reason to decline the authorization request, we’ll approve it.

[real-time authorization webhook](/issuing/controls/real-time-authorizations)

When this occurs, Stripe still sends an issuing_authorization.created event, notifying you of the Authorization’s creation.

[Authorization’s](/api#issuing_authorization_object)

## Authorization updates

When Stripe receives an authorization request, we send an issuing_authorization.created webhook event. If you approve the authorization, we deduct the amount from your  Issuing balance  and hold it in reserve until the authorization is either captured, voided, or expired without capture. If you decline the authorization, the status is set to closed and we don’t place any holds.

[webhook](/webhooks)

When the authorization is captured, a transaction is created and the status of the authorization is set to closed.

[transaction](/issuing/purchases/transactions)

If the authorization request is voided, we send an issuing_authorization.updated webhook event with its status set to reversed and the amount as 0. We add the voided amount back  to your Issuing balance, essentially undoing the balance impact of the original authorization.

[webhook](/webhooks)

If the authorization request is expired without capture, we send an issuing_authorization.updated webhook event with its status set to reversed and the amount representing any remaining amount authorized for possible late captures. We add the expired amount back  to your Issuing balance, essentially undoing the balance impact of the original authorization.

[webhook](/webhooks)

## Purchases in different currencies

Cards can be used for purchases in any currency that the card network supports. Stripe automatically converts the currency of the purchase into the card’s currency when holding funds, using the card network’s daily rate.

The merchant_amount represents the cost of the purchase in the local currency. The amount field represents the expected amount of the Transaction in the card’s currency and is not final until the Authorization has been captured.

## Handling other authorizations

In addition to regular authorizations, there are a few other cases that you should be ready to handle.

Some authorizations are partially authorized to limit spending. This allows you to authorize a specific lower amount and is useful when there are not sufficient funds to cover the full purchase.

Fueling stations in the US are a special example of this. Learn more about fuel dispenser transactions.

[fuel dispenser transactions](/issuing/purchases/authorizations#fuel-dispenser-transactions)

When an authorization is partially authorized, the is_amount_controllable field on the authorization request is set to true. You can specify the amount you want to approve by setting the amount in the webhook response body or the approve call.

[approve](/api/issuing/authorizations/approve)

If you partially approve a cashback authorization, you must approve the full cashback amount. You can’t set the approved amount lower than the cashback_amount.

To simulate the creation of a new partial authorization, you can use the Authorization Create API in the Issuing test helpers.

[Authorization Create API](/api/issuing/authorizations/test_mode_create)

## Fuel dispenser transactions

When a cardholder attempts a purchase at a fuel dispenser (MCC 5542), an issuing_authorization.request for 1 USD is sent (called a “status check”). The default amount held is 100 USD to cover the unknown purchase amount. When the cardholder finishes pumping fuel, an issuing_authorization.updated event is sent to reflect the amount of the purchase.

[MCC 5542](/issuing/categories)

When the fuel dispenser allows a partial authorization by setting the field is_amount_controllable to true, you can respond with a lesser approved amount (for example, 50 USD). However, when a fuel dispenser doesn’t allow partial authorizations, you must either approve the network default amount (Stripe ignores any amount you specify), or decline the entire authorization.

[partial authorization](/issuing/purchases/authorizations?issuing-authorization-type=partial_authorization#handling-other-authorizations)

## Using with Stripe Treasury

Authorizations on cards that use funds stored in Treasury FinancialAccounts have a treasury field with references to Treasury resources: Treasury Transaction, ReceivedCredit, and ReceivedDebit.

[FinancialAccounts](/api/treasury/financial_accounts)

[treasury field](/api/issuing/authorizations/object#issuing_authorization_object-treasury)

[Transaction](/api/treasury/transactions)

[ReceivedCredit](/api/treasury/received_credits)

[ReceivedDebit](/api/treasury/received_debits)
