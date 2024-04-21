- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# Delete a card

[Delete a card](/api/cards/delete)

You can delete cards from a customer. If you delete a card that is currently the default source, then the most recently added source will become the new default. If you delete a card that is the last remaining source on the customer, then the default_source attribute will become null.

For recipients: if you delete the default card, then the most recently added card will become the new default. If you delete the last remaining card on a recipient, then the default_card attribute will become null.

Note that for cards belonging to customers, you might want to prevent customers on paid subscriptions from deleting all cards on file, so that there is at least one default card for the next invoice payment attempt.

No parameters.
