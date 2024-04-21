- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Create a card

[Create a card](/api/external_account_cards/create)

When you create a new debit card, you must specify a Custom account to create it on.

[Custom account](/connect/managed-accounts)

If the account has no default destination card, then the new card will become the default. However, if the owner already has a default then it will not change. To change the default, you should set default_for_currency to true when creating a card for a Custom account.

- external_accountobject | stringRequiredA token, like the ones returned by Stripe.js or a dictionary containing a user’s card details (with the options shown below). Stripe will automatically validate the card.Show child parameters

A token, like the ones returned by Stripe.js or a dictionary containing a user’s card details (with the options shown below). Stripe will automatically validate the card.

[Stripe.js](/js)

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- default_for_currencyboolean

Returns the card object

# Update a card

[Update a card](/api/external_account_cards/update)

If you need to update only some card details, like the billing address or expiration date, you can do so without having to re-enter the full card details. Stripe also works directly with card networks so that your customers can continue using your service without interruption.

[continue using your service](https://stripe.com/docs/saving-cards#automatic-card-updates)

- default_for_currencybooleanWhen set to true, this becomes the default external account for its currency.

When set to true, this becomes the default external account for its currency.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- address_citystring

- address_countrystring

- address_line1string

- address_line2string

- address_statestring

- address_zipstring

- exp_monthstring

- exp_yearstring

- namestring

Returns the card object.

# Retrieve a card

[Retrieve a card](/api/external_account_cards/retrieve)

By default, you can see the 10 most recent external accounts stored on a connected account directly on the object. You can also retrieve details about a specific card stored on the account.

[connected account](/connect/accounts)

No parameters.

Returns the card object.

# List all cards

[List all cards](/api/external_account_cards/list)

You can see a list of the cards that belong to a connected account. The 10 most recent external accounts are available on the account object. If you need more than 10, you can use this API method and the limit and starting_after parameters to page through additional cards.

[connected account](/connect/accounts)

No parameters.

- ending_beforestring

- limitinteger

- objectstring

- starting_afterstring

Returns a list of the cards stored on the account.

# Delete a card

[Delete a card](/api/external_account_cards/delete)

You can delete cards from a Custom account.

[Custom account](/connect/custom-accounts)

There are restrictions for deleting a card with default_for_currency set to true. You cannot delete a card if any of the following apply:

- The card’s currency is the same as the connected account’s default_currency.

[default_currency](/api/accounts/object#account_object-default_currency)

- There is another external account (card or bank account) with the same currency as the card.

To delete a card, you must first replace the default external account by setting default_for_currency with another external account in the same currency.

No parameters.

Returns the deleted card object.
