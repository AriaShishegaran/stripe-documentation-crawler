# Replacement cards

You can replace cards that are expired, damaged, lost, or stolen. The process differs slightly for each kind of card replacement.

- Card expired: The card has reached its expiration date and is no longer valid.

- Card damaged: The cardholder requests a new card for a reason other than lost or stolen (for example, a physical card’s chip no longer reads properly).

- Card lost/stolen: The card is reported lost or stolen and a new card number, expiry, security code are issued.

Depending on the scenario, the replacement card might have a different card number, expiry, or security code from the original:

## Replacements for expired or damaged cards

Physical cards can get damaged, and both physical cards and virtual cards expire, but you can create replacement cards that have the same card number. The cardholder can continue to use the original card before the replacement card is activated, as long as the card isn’t too damaged or already expired. Activating the replacement card cancels the original card if it isn’t already canceled.

To create a replacement card for an expired or damaged card, create a Card with replacement_for using the expired or damaged Card ID and replacement_reason set to expired or damaged.

[Card](/api#issuing_card_object)

## Replacements for lost or stolen cards

Lost or stolen cards get new card numbers for security reasons. We need to cancel the original cards before we can create the replacement card.

To create a replacement card for a lost or stolen card:

- Cancel the lost or stolen card by using the update card endpoint to set its status to canceled and its cancellation_reason to lost or stolen.

Cancel the lost or stolen card by using the update card endpoint to set its status to canceled and its cancellation_reason to lost or stolen.

[update card](/api#update_issuing_card)

- Create a Card with replacement_for using the lost or stolen Card ID and replacement_reason set to lost or stolen.

Create a Card with replacement_for using the lost or stolen Card ID and replacement_reason set to lost or stolen.

[Card](/api#issuing_card_object)

## All replacements

All replacement cards have renewed expiration dates and new security codes. Authorizations made on the original cards are migrated to the replacements, but might still clear on the original cards. Like the originals, replacement cards must be activated before use.

## Card-on-file updating

For many of our card programs, Stripe automatically updates the card details on file with acquiring merchants, even when a card is completely reissued. This feature offers several benefits, including saving your cardholders the hassle of manually re-entering card details when their cards expire.

Updating the payment details for a card that has been replaced due to expiration ensures that recurring payments and stored payment details continue to function smoothly. This provides cardholders with a seamless experience even when their cards expire.

By default, Stripe updates merchants with the new card number, expiry, and security code of a replacement card, even when the card is lost or stolen.

If you prefer not to provide these details to acquiring merchants, cancel the lost or stolen card and issue a new one without specifying the replacement_for card. This prevents the replacement card from being explicitly tied to the card that’s been lost or stolen.
