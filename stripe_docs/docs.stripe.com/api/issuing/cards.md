- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Cards

[Cards](/api/issuing/cards)

You can create physical or virtual cards that are issued to cardholders.

[create physical or virtual cards](/issuing/cards)

[POST/v1/issuing/cards](/api/issuing/cards/create)

[POST/v1/issuing/cards/:id](/api/issuing/cards/update)

[GET/v1/issuing/cards/:id](/api/issuing/cards/retrieve)

[GET/v1/issuing/cards](/api/issuing/cards/list)

[POST/v1/test_helpers/issuing/cards/:id/shipping/deliver](/api/issuing/cards/test_mode_deliver)

[POST/v1/test_helpers/issuing/cards/:id/shipping/fail](/api/issuing/cards/test_mode_fail)

[POST/v1/test_helpers/issuing/cards/:id/shipping/return](/api/issuing/cards/test_mode_return)

[POST/v1/test_helpers/issuing/cards/:id/shipping/ship](/api/issuing/cards/test_mode_ship)

# The Card object

[The Card object](/api/issuing/cards/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- cancellation_reasonnullable enumThe reason why the card was canceled.Possible enum valuesdesign_rejectedThe design of this card was rejected by Stripe for violating our partner guidelines.lostThe card was lost.stolenThe card was stolen.

The reason why the card was canceled.

The design of this card was rejected by Stripe for violating our partner guidelines.

[partner guidelines](/issuing/cards/physical#design-review)

The card was lost.

The card was stolen.

- cardholderobjectThe Cardholder object to which the card belongs.Show child attributes

The Cardholder object to which the card belongs.

[Cardholder](/api#issuing_cardholder_object)

- currencyenumThree-letter ISO currency code, in lowercase. Supported currencies are usd in the US, eur in the EU, and gbp in the UK.

Three-letter ISO currency code, in lowercase. Supported currencies are usd in the US, eur in the EU, and gbp in the UK.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

- exp_monthintegerThe expiration month of the card.

The expiration month of the card.

- exp_yearintegerThe expiration year of the card.

The expiration year of the card.

- last4stringThe last 4 digits of the card number.

The last 4 digits of the card number.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- statusenumWhether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to inactive.Possible enum valuesactiveThe card can approve authorizations. If the card is linked to a cardholder with past-due requirements, you may be unable to change the card’s status to ‘active’.canceledThe card will decline authorizations, and no authorization object will be recorded. This status is permanent.inactiveThe card will decline authorizations with the card_inactive reason.

Whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to inactive.

The card can approve authorizations. If the card is linked to a cardholder with past-due requirements, you may be unable to change the card’s status to ‘active’.

The card will decline authorizations, and no authorization object will be recorded. This status is permanent.

The card will decline authorizations with the card_inactive reason.

- typeenumThe type of the card.Possible enum valuesphysicalA physical card will be printed and shipped. It can be used at physical terminals.virtualNo physical card will be printed. The card can be used online and can be added to digital wallets.

The type of the card.

A physical card will be printed and shipped. It can be used at physical terminals.

No physical card will be printed. The card can be used online and can be added to digital wallets.

[added to digital wallets](https://stripe.com/docs/issuing/cards/digital-wallets)

- objectstring

- brandstring

- createdtimestamp

- cvcnullable stringExpandable

- livemodeboolean

- numbernullable stringExpandable

- personalization_designnullable stringPreview featureExpandable

- replaced_bynullable stringExpandable

- replacement_fornullable stringExpandable

- replacement_reasonnullable enum

- shippingnullable object

- spending_controlsobject

- walletsnullable object

# Create a card

[Create a card](/api/issuing/cards/create)

Creates an Issuing Card object.

- currencystringRequiredThe currency for the card.

The currency for the card.

- typeenumRequiredThe type of card to issue. Possible values are physical or virtual.Possible enum valuesphysicalA physical card will be printed and shipped. It can be used at physical terminals.virtualNo physical card will be printed. The card can be used online and can be added to digital wallets.

The type of card to issue. Possible values are physical or virtual.

A physical card will be printed and shipped. It can be used at physical terminals.

No physical card will be printed. The card can be used online and can be added to digital wallets.

[added to digital wallets](https://stripe.com/docs/issuing/cards/digital-wallets)

- cardholderstringRequiredThe Cardholder object with which the card will be associated.

The Cardholder object with which the card will be associated.

[Cardholder](/api#issuing_cardholder_object)

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- statusenumWhether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to inactive.Possible enum valuesactiveThe card can approve authorizations. If the card is linked to a cardholder with past-due requirements, you may be unable to change the card’s status to ‘active’.inactiveThe card will decline authorizations with the card_inactive reason.

Whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to inactive.

The card can approve authorizations. If the card is linked to a cardholder with past-due requirements, you may be unable to change the card’s status to ‘active’.

The card will decline authorizations with the card_inactive reason.

- personalization_designstringPreview feature

- pinobject

- replacement_forstring

- replacement_reasonenum

- second_linestring

- shippingobject

- spending_controlsobject

Returns an Issuing Card object if creation succeeds.

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
