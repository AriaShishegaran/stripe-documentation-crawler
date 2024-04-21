# Issuing beta migration guide

Stripe Issuing recently became generally available for all US businesses. When we exited our beta, we released pricing and changes to our API, which include features and updates to support its long-term evolution. Depending on your integration, some of these API changes will be breaking, so pay extra attention to every item in this guide.

We will be discontinuing the beta API on March 1, 2021. Below we have outlined all the changes to the API to help with your migration. Please contact support with any questions.

[support](mailto:support-issuing@stripe.com)

## Compatibility

As noted in each section, we recommend supporting both the old and new API until you’ve officially switched over. We also recommend creating a new Issuing account to test out the new API before switching over on your main account.

For beta users, both legacy and new attributes are currently available on all Issuing objects. Renamed attributes point to the same backend value as their legacy counterpart. When the beta is discontinued, only the new attributes will be available.

To prepare, we recommend switching reads to support both the old and new attribute until you have successfully switched over to the new API.

For renamed parameters, either the legacy or new name can be used but not both. When the beta is discontinued, only the new parameters will be accepted.

To prepare, we recommend switching writes to support both the old and new param until you have successfully switched over to the new API.

Transitioning to new enum values will be slightly more complicated. New values can be written and read back but old, existing values will continue to be returned until the beta is officially discontinued.

For example, the Cardholder type of business_entity has been renamed company. Existing cardholder objects will continue to show the old value, business_entity. New objects can be created with business_entity or company and whichever value is provided will be returned when read back.

[type](/api/issuing/cardholders/object#issuing_cardholder_object-type)

To prepare, we recommend switching writes to the new value (for example, when creating a new cardholder set type to company) and handling either value on reads.

## API Changes

- Replaced held_amount with amount. amount will always be the total sum authorized or denied for capture in the cardholder currency. Unlike held_amount, it will not drop to zero upon capture.Amount held by an authorization can be obtained by sum of its balance_transactions amounts.

- Amount held by an authorization can be obtained by sum of its balance_transactions amounts.

[balance_transactions](/api/issuing/authorizations/object#issuing_authorization_object-balance_transactions)

- Renamed held_currency to currency.

- Replaced authorized_amount with merchant_amount. merchant_amount will always be the total sum authorized or denied for capture in the merchant currency. Unlike authorized_amount, merchant_amount can be reduced by reversals.

- Renamed authorized_currency to merchant_currency.

- Renamed held_amount to amount in the approve an authorization endpoint.

[approve an authorization](/api/issuing/authorizations/approve)

- Added a pending_request hash. This will only be populated during a synchronous webhook request for real-time authorizations.Replaced pending_held_amount with pending_request.amount.Replaced pending_authorized_amount with pending_request.merchant_amount.Replaced is_held_amount_controllable with pending_request.is_amount_controllable.

[pending_request](/api/issuing/authorizations/object#issuing_authorization_object-pending_request)

[synchronous webhook](/issuing/controls/real-time-authorizations)

- Replaced pending_held_amount with pending_request.amount.

- Replaced pending_authorized_amount with pending_request.merchant_amount.

- Replaced is_held_amount_controllable with pending_request.is_amount_controllable.

- Renamed attributes of hashes in request_history:Renamed request_history.held_amount to request_history.amount.Renamed request_history.held_currency to request_history.currency.Renamed request_history.authorized_amount to request_history.merchant_amount.Renamed request_history.authorized_currency to request_history.merchant_currency.Removed request_history.violated_authorization_controls.

[request_history](/api/issuing/authorizations/object#issuing_authorization_object-request_history)

- Renamed request_history.held_amount to request_history.amount.

- Renamed request_history.held_currency to request_history.currency.

- Renamed request_history.authorized_amount to request_history.merchant_amount.

- Renamed request_history.authorized_currency to request_history.merchant_currency.

- Removed request_history.violated_authorization_controls.

- Discontinued several values for request_history.reason.authentication_failed, incorrect_cvc, and incorrect_expiry have been consolidated into verification_failed. For more detail, use authorization.verification_data.account_compliance_disabled and account_inactive have been replaced with account_disabled.authorization_controls was renamed spending_controls to be consistent with the renamed attributes in the Card and Cardholder resources.

[request_history.reason](/api/issuing/authorizations/object#issuing_authorization_object-request_history-reason)

- authentication_failed, incorrect_cvc, and incorrect_expiry have been consolidated into verification_failed. For more detail, use authorization.verification_data.

[authorization.verification_data](/api/issuing/authorizations/object#issuing_authorization_object-verification_data)

- account_compliance_disabled and account_inactive have been replaced with account_disabled.

- authorization_controls was renamed spending_controls to be consistent with the renamed attributes in the Card and Cardholder resources.

[Card](/api/issuing/cards/object#issuing_card_object-spending_controls)

[Cardholder](/api/issuing/cardholders/object#issuing_cardholder_object-spending_controls)

- Discontinued verification_data.authentication enum in favor of the more descriptive verification_data.three_d_secure hash.three_d_secure.result, which replaces authentication, contains more values than before. A full overview of the new values can be found here.This attribute will only be visible to users enrolled in the 3D Secure feature.

- three_d_secure.result, which replaces authentication, contains more values than before. A full overview of the new values can be found here.

[here](/issuing/3d-secure#prevent-fraud)

- This attribute will only be visible to users enrolled in the 3D Secure feature.

- Renamed verification_data.address_zip_check to verification_data.address_postal_code_check.

[verification_data.address_postal_code_check](/api/issuing/authorizations/object#issuing_authorization_object-verification_data-address_postal_code_check)

- Renamed wallet_provider attribute to wallet.

- Removed the following type values since they were uncommon and can be represented in other ways:cash_withdrawal (now capture)refund_reversal (now refund with negative amount)dispute and dispute_loss. A Disputes API is under development.

[type](/api/issuing/transactions/object#issuing_transaction_object-type)

- cash_withdrawal (now capture)

- refund_reversal (now refund with negative amount)

- dispute and dispute_loss. A Disputes API is under development.

- Stopped creating a second Transaction of type dispute to represent a won Dispute’s money movement. Instead, we will add balance_transactions directly to the Dispute.Consequently, there will be no issuing_transaction.created event for Dispute money movement. Instead, we’ll have a new event which will send the updated Dispute with balance_transactions.

- Consequently, there will be no issuing_transaction.created event for Dispute money movement. Instead, we’ll have a new event which will send the updated Dispute with balance_transactions.

- Removed dispute query param from list all transactions endpoint.

[list all transactions](/api/issuing/transactions/list)

- Restricted settlement query param from list all transactions endpoint to Settlement feature users.

[list all transactions](/api/issuing/transactions/list)

- Added purchase_details for enhanced transaction data.

- Removed the is_default attribute. As a consequence, cardholder is a required parameter when creating a new card. The list all cardholders endpoint no longer accepts is_default as a query parameter.

[list all cardholders](/api/issuing/cardholders/list)

- Renamed type from business_entity to company to better align with hashes that contain additional information.

[type](/api/issuing/cardholders/object#issuing_cardholder_object-type)

- Removed billing.name since it’s always the same as the top-level name attribute on the resource.

- Renamed authorization_controls to spending_controls.

[spending_controls](/api/issuing/cardholders/object#issuing_cardholder_object-spending_controls)

- Removed lost and stolen card statuses. These are represented as canceled with an optional cancellation_reason provided.

[canceled](/api/issuing/cards/object#issuing_card_object-status)

[cancellation_reason](/api/issuing/cards/object#issuing_card_object-cancellation_reason)

- Renamed authorization_controls to spending_controls.

[spending_controls](/api/issuing/cards/object#issuing_card_object-spending_controls)

- Renamed replacement_reason values:loss to losttheft to stolendamage to damagedexpiration to expired

[replacement_reason](/api/issuing/cards/object#issuing_card_object-replacement_reason)

- loss to lost

- theft to stolen

- damage to damaged

- expiration to expired

- Removed name. Please refer to cardholder.name instead.

[cardholder.name](/api/issuing/cards/object#issuing_card_object-cardholder)

- Renamed shipping.speed enum to shipping.service. The overnight value has been renamed priority.

[shipping.service](/api/issuing/cards/object#issuing_card_object-shipping-service)

- Added replaced_by, to point to the card that replaced the current card.

[replaced_by](/api/issuing/cards/object#issuing_card_object-replaced_by)

- Renamed authorization_controls to spending_controls and removed max_approvals, max_amount , and currency. We recommend using amount-based limits for more accurate control over card spend.

[spending_controls](/api/issuing/cards/object#issuing_card_object-spending_controls)

- merchant_data.url will only be available to users enrolled in 3D Secure feature.

- pin will only be available to users enrolled in PIN management feature.

- The list all cards endpoint will no longer accept source and name parameters.

[list all cards](/api/issuing/cards/list)

- The retrieve card details endpoint has been discontinued. Instead, number and cvc can be expanded from the retrieve endpoint.

[retrieve card details](/api/issuing/cards/retrieve_details)

[number](/api/issuing/cards/object#issuing_card_object-number)

[cvc](/api/issuing/cards/object#issuing_card_object-cvc)

[retrieve](/api/issuing/cards/retrieve)

- Renamed disputed_transaction to transaction.

- Added balance_transactions which will contain all BalanceTransactions associated with a Dispute.Each BalanceTransaction will have a new type, source, description and reporting_category corresponding to an Issuing Dispute as follows:type: "issuing_dispute"source: "idp_1FMjf1GprvsjVv9gffmDmLGx"description: "Issuing dispute"reporting_category: "Issuing Dispute"

[BalanceTransactions](/api/balance_transactions)

- Each BalanceTransaction will have a new type, source, description and reporting_category corresponding to an Issuing Dispute as follows:type: "issuing_dispute"source: "idp_1FMjf1GprvsjVv9gffmDmLGx"description: "Issuing dispute"reporting_category: "Issuing Dispute"

- type: "issuing_dispute"

- source: "idp_1FMjf1GprvsjVv9gffmDmLGx"

- description: "Issuing dispute"

- reporting_category: "Issuing Dispute"

- We will send a new event, issuing_dispute.funds_reinstated, with the updated Dispute and new BalanceTransaction when a  Dispute has been won.

- The following events are restricted to users enrolled in the Settlement feature:issuing_settlement.createdissuing_settlement.updated

- issuing_settlement.created

- issuing_settlement.updated

- The issuing.pending balance has been removed from the Balance object. Please refer to the issuing.available balance instead.

[Balance](/api/balance/balance_object#balance_object)

[issuing.available](/api/balance/balance_object#balance_object-issuing-available)
