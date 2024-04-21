- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The External Account Card object

[The External Account Card object](/api/external_account_cards/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- accountnullable stringExpandablecustom Connect onlyThe account this card belongs to. This attribute will not be in the card object if the card belongs to a customer or recipient instead.

The account this card belongs to. This attribute will not be in the card object if the card belongs to a customer or recipient instead.

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

- currencynullable enumcustom Connect onlyThree-letter ISO code for currency. Only applicable on accounts (not customers or recipients). The card can be used as a transfer destination for funds in this currency.

Three-letter ISO code for currency. Only applicable on accounts (not customers or recipients). The card can be used as a transfer destination for funds in this currency.

[ISO code for currency](https://stripe.com/docs/payouts)

- cvc_checknullable stringIf a CVC was provided, results of the check: pass, fail, unavailable, or unchecked. A result of unchecked indicates that CVC was provided but hasn’t been checked yet. Checks are typically performed when attaching a card to a Customer object, or when creating a charge. For more details, see Check if a card is valid without a charge.

If a CVC was provided, results of the check: pass, fail, unavailable, or unchecked. A result of unchecked indicates that CVC was provided but hasn’t been checked yet. Checks are typically performed when attaching a card to a Customer object, or when creating a charge. For more details, see Check if a card is valid without a charge.

[Check if a card is valid without a charge](https://support.stripe.com/questions/check-if-a-card-is-valid-without-a-charge)

- default_for_currencynullable booleancustom Connect onlyWhether this card is the default external account for its currency.

Whether this card is the default external account for its currency.

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

- statusnullable stringFor external accounts that are cards, possible values are new and errored. If a payout fails, the status is set to errored and scheduled payouts are stopped until account details are updated.

For external accounts that are cards, possible values are new and errored. If a payout fails, the status is set to errored and scheduled payouts are stopped until account details are updated.

[scheduled payouts](https://stripe.com/docs/payouts#payout-schedule)

- objectstring

- address_line1_checknullable string

- available_payout_methodsnullable array of enums

- customernullable stringExpandable

- dynamic_last4nullable string

- tokenization_methodnullable string

- walletnullable objectPreview feature

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
