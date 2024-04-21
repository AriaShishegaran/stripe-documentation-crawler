# Issuing spending controls

You can use spending controls to block merchant categories (for example, bakeries), countries, or merchant IDs, and to set spending limits such as 100 EUR per authorization or 3000 EUR per month. You can apply them to both Cards and Cardholders either by setting their spending_controls fields when you create them or by updating them later.

[merchant categories](/issuing/categories)

[countries](/api/issuing/authorizations/object#issuing_authorization_object-merchant_data-country)

[merchant IDs](/api/issuing/authorizations/object#issuing_authorization_object-merchant_data-network_id)

[Cards](/api/issuing/cards/object#issuing_card_object-spending_controls)

[Cardholders](/api/issuing/cardholders/object#issuing_cardholder_object-spending_controls)

The spending_controls object has the following structure:

[categories](/issuing/categories)

[categories](/issuing/categories)

[objects](/issuing/controls/spending-controls#spending-limits)

[countries](/api/issuing/authorizations/object#issuing_authorization_object-merchant_data-country)

[countries](/api/issuing/authorizations/object#issuing_authorization_object-merchant_data-country)

Spending controls run before real-time authorizations and can decline a purchase before the issuing_authorization.request is sent, resulting in a declined issuing_authorization.created event.

[real-time authorizations](/issuing/controls/real-time-authorizations)

Country and merchant ID spend controls are currently limited to beta users. You must be an Issuing customer to join the beta. To request access to the beta, Contact Stripe for more information.

## Spending limits

Spending limit rules limit the total amount of spending for categories over intervals of time.

The spending_limits field within spending_controls is a list of objects that have the following structure:

[smallest currency unit](/currencies#zero-decimal)

[Card spending_controls](/api/issuing/cards/object#issuing_card_object-spending_controls-spending_limits-interval)

[categories](/issuing/categories)

If you don’t set spending_limits, a default spending limit is applied to the newly created card in the amount of 500 EUR per day. Contact Support to disable this behavior.

[Contact Support](https://support.stripe.com/contact/login)

In addition to the configurable spending_limits, a default spending limit in the amount of 10000 EUR is also applied to each authorization. Contact Support to disable this behavior.

[Contact Support](https://support.stripe.com/contact/login)

A card’s spending limits apply across any cards it replaces (that is, its replacement_for card and that card’s replacement_for card, up the chain). A cardholder’s spending limits apply across all of their cards.

[replacement_for](/api/issuing/cards/object#issuing_card_object-replacement_for)

[replacement_for](/api/issuing/cards/object#issuing_card_object-replacement_for)

Each spending limit only applies to its own categories. Spending limits alone do not block categories and should be used with either allowed_categories or blocked_categories to restrict spending to specific business types.

If a cardholder has overlapping spending limits (for example, 100 EUR per authorization and 50 EUR per authorization for their card), the most restrictive spending control applies.

Additional tips and fees can be posted at a later time, causing a spending limit to be exceeded.

[posted at a later time](/issuing/purchases/transactions?issuing-capture-type=over_capture)

## Examples

The following examples demonstrate different uses of spending controls for cards and cardholders.
