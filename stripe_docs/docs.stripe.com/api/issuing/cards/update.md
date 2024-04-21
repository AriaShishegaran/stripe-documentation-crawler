- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Update a card

[Update a card](/api/issuing/cards/update)

Updates the specified Issuing Card object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

- cancellation_reasonenumReason why the status of this card is canceled.Possible enum valueslostThe card was lost.stolenThe card was stolen.

Reason why the status of this card is canceled.

The card was lost.

The card was stolen.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- statusenumDictates whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to inactive. If this card is being canceled because it was lost or stolen, this information should be provided as cancellation_reason.Possible enum valuesactiveThe card can approve authorizations. If the card is linked to a cardholder with past-due requirements, you may be unable to change the card’s status to ‘active’.canceledThe card will decline authorizations, and no authorization object will be recorded. This status is permanent.inactiveThe card will decline authorizations with the card_inactive reason.

Dictates whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to inactive. If this card is being canceled because it was lost or stolen, this information should be provided as cancellation_reason.

The card can approve authorizations. If the card is linked to a cardholder with past-due requirements, you may be unable to change the card’s status to ‘active’.

The card will decline authorizations, and no authorization object will be recorded. This status is permanent.

The card will decline authorizations with the card_inactive reason.

- pinobject

- spending_controlsobject

Returns an updated Issuing Card object if a valid identifier was provided.

# Retrieve a card

[Retrieve a card](/api/issuing/cards/retrieve)

Retrieves an Issuing Card object.

No parameters.

Returns an Issuing Card object if a valid identifier was provided. When requesting the ID of a card that has been deleted, a subset of the card’s information will be returned, including a deleted property, which will be true.

# List all cards

[List all cards](/api/issuing/cards/list)

Returns a list of Issuing Card objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

- cardholderstringOnly return cards belonging to the Cardholder with the provided ID.

Only return cards belonging to the Cardholder with the provided ID.

- typeenumOnly return cards that have the given type. One of virtual or physical.Possible enum valuesphysicalA physical card will be printed and shipped. It can be used at physical terminals.virtualNo physical card will be printed. The card can be used online and can be added to digital wallets.

Only return cards that have the given type. One of virtual or physical.

A physical card will be printed and shipped. It can be used at physical terminals.

No physical card will be printed. The card can be used online and can be added to digital wallets.

[added to digital wallets](https://stripe.com/docs/issuing/cards/digital-wallets)

- createdobject

- ending_beforestring

- exp_monthinteger

- exp_yearinteger

- last4string

- limitinteger

- starting_afterstring

- statusenum

A dictionary with a data property that contains an array of up to limit cards, starting after card starting_after. Each entry in the array is a separate Issuing Card object. If no more cards are available, the resulting array will be empty.

# Deliver a testmode cardTest helper

[Deliver a testmode card](/api/issuing/cards/test_mode_deliver)

Updates the shipping status of the specified Issuing Card object to delivered.

No parameters.

Returns an updated Issuing Card object.

# Fail a testmode cardTest helper

[Fail a testmode card](/api/issuing/cards/test_mode_fail)

Updates the shipping status of the specified Issuing Card object to failure.

No parameters.

Returns an updated Issuing Card object.
