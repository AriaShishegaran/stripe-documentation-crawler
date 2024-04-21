- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Card object

[The Card object](/api/cards/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- address_citynullable stringCity/District/Suburb/Town/Village.

City/District/Suburb/Town/Village.

- address_countrynullable stringBilling address country, if provided when creating card.

Billing address country, if provided when creating card.

- address_line1nullable stringAddress line 1 (Street address/PO Box/Company name).

Address line 1 (Street address/PO Box/Company name).

- address_line2nullable stringAddress line 2 (Apartment/Suite/Unit/Building).

Address line 2 (Apartment/Suite/Unit/Building).

- address_statenullable stringState/County/Province/Region.

State/County/Province/Region.

- address_zipnullable stringZIP or postal code.

ZIP or postal code.

- address_zip_checknullable stringIf address_zip was provided, results of the check: pass, fail, unavailable, or unchecked.

If address_zip was provided, results of the check: pass, fail, unavailable, or unchecked.

- brandstringCard brand. Can be American Express, Diners Club, Discover, Eftpos Australia, JCB, MasterCard, UnionPay, Visa, or Unknown.

Card brand. Can be American Express, Diners Club, Discover, Eftpos Australia, JCB, MasterCard, UnionPay, Visa, or Unknown.

- countrynullable stringTwo-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.

- customernullable stringExpandableThe customer that this card belongs to. This attribute will not be in the card object if the card belongs to an account or recipient instead.

The customer that this card belongs to. This attribute will not be in the card object if the card belongs to an account or recipient instead.

- cvc_checknullable stringIf a CVC was provided, results of the check: pass, fail, unavailable, or unchecked. A result of unchecked indicates that CVC was provided but hasn’t been checked yet. Checks are typically performed when attaching a card to a Customer object, or when creating a charge. For more details, see Check if a card is valid without a charge.

If a CVC was provided, results of the check: pass, fail, unavailable, or unchecked. A result of unchecked indicates that CVC was provided but hasn’t been checked yet. Checks are typically performed when attaching a card to a Customer object, or when creating a charge. For more details, see Check if a card is valid without a charge.

[Check if a card is valid without a charge](https://support.stripe.com/questions/check-if-a-card-is-valid-without-a-charge)

- exp_monthintegerTwo-digit number representing the card’s expiration month.

Two-digit number representing the card’s expiration month.

- exp_yearintegerFour-digit number representing the card’s expiration year.

Four-digit number representing the card’s expiration year.

- fingerprintnullable stringUniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.

Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.

- fundingstringCard funding type. Can be credit, debit, prepaid, or unknown.

Card funding type. Can be credit, debit, prepaid, or unknown.

- last4stringThe last four digits of the card.

The last four digits of the card.

- metadatanullable objectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- namenullable stringCardholder name.

Cardholder name.

- objectstring

- accountnullable stringExpandablecustom Connect only

- address_line1_checknullable string

- available_payout_methodsnullable array of enums

- currencynullable enumcustom Connect only

- dynamic_last4nullable string

- tokenization_methodnullable string

- walletnullable objectPreview feature

# Create a card

[Create a card](/api/cards/create)

When you create a new credit card, you must specify a customer or recipient on which to create it.

If the card’s owner has no default card, then the new card will become the default. However, if the owner already has a default, then it will not change. To change the default, you should update the customer to have a new default_source.

[update the customer](/api#update_customer)

- sourceobject | stringRequiredA token, like the ones returned by Stripe.js or a dictionary containing a user’s card details (with the options shown below). Stripe will automatically validate the card.Show child parameters

A token, like the ones returned by Stripe.js or a dictionary containing a user’s card details (with the options shown below). Stripe will automatically validate the card.

[Stripe.js](/js)

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

Returns the Card object.

# Update a card

[Update a card](/api/cards/update)

Updates a specified card for a given customer.

- address_citystringCity/District/Suburb/Town/Village.

City/District/Suburb/Town/Village.

- address_countrystringBilling address country, if provided when creating card.

Billing address country, if provided when creating card.

- address_line1stringAddress line 1 (Street address/PO Box/Company name).

Address line 1 (Street address/PO Box/Company name).

- address_line2stringAddress line 2 (Apartment/Suite/Unit/Building).

Address line 2 (Apartment/Suite/Unit/Building).

- address_statestringState/County/Province/Region.

State/County/Province/Region.

- address_zipstringZIP or postal code.

ZIP or postal code.

- exp_monthstringTwo digit number representing the card’s expiration month.

Two digit number representing the card’s expiration month.

- exp_yearstringFour digit number representing the card’s expiration year.

Four digit number representing the card’s expiration year.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- namestringCardholder name.

Cardholder name.

# Retrieve a card

[Retrieve a card](/api/cards/retrieve)

You can always see the 10 most recent cards directly on a customer; this method lets you retrieve details about a specific card stored on the customer.

No parameters.

Returns the Card object.

# List all cards

[List all cards](/api/cards/list)

You can see a list of the cards belonging to a customer. Note that the 10 most recent sources are always available on the Customer object. If you need more than those 10, you can use this API method and the limit and starting_after parameters to page through additional cards.

No parameters.

- ending_beforestring

- limitinteger

- starting_afterstring

Returns a list of the cards stored on the customer.
