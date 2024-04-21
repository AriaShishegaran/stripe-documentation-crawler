htmlCards | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Cards

You can store multiple cards on a customer in order to charge the customer later. You can also store multiple debit cards on a recipient in order to transfer to those cards later.

Related guide: Card payments with Sources

Endpoints
# The Card object

### Attributes

- idstringUnique identifier for the object.


- address_citynullablestringCity/District/Suburb/Town/Village.


- address_countrynullablestringBilling address country, if provided when creating card.


- address_line1nullablestringAddress line 1 (Street address/PO Box/Company name).


- address_line2nullablestringAddress line 2 (Apartment/Suite/Unit/Building).


- address_statenullablestringState/County/Province/Region.


- address_zipnullablestringZIP or postal code.


- address_zip_checknullablestringIf address_zip was provided, results of the check: pass, fail, unavailable, or unchecked.


- brandstringCard brand. Can be American Express, Diners Club, Discover, Eftpos Australia, JCB, MasterCard, UnionPay, Visa, or Unknown.


- countrynullablestringTwo-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.


- customernullablestringExpandableThe customer that this card belongs to. This attribute will not be in the card object if the card belongs to an account or recipient instead.


- cvc_checknullablestringIf a CVC was provided, results of the check: pass, fail, unavailable, or unchecked. A result of unchecked indicates that CVC was provided but hasn’t been checked yet. Checks are typically performed when attaching a card to a Customer object, or when creating a charge. For more details, see Check if a card is valid without a charge.


- exp_monthintegerTwo-digit number representing the card’s expiration month.


- exp_yearintegerFour-digit number representing the card’s expiration year.


- fingerprintnullablestringUniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.


- fundingstringCard funding type. Can be credit, debit, prepaid, or unknown.


- last4stringThe last four digits of the card.


- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- namenullablestringCardholder name.



### More attributesExpand all

- objectstring
- accountnullablestringExpandablecustom Connect only
- address_line1_checknullablestring
- available_payout_methodsnullablearray of enums
- currencynullableenumcustom Connect only
- dynamic_last4nullablestring
- tokenization_methodnullablestring
- walletnullableobjectPreview feature

The Card object`{  "id": "card_1MvoiELkdIwHu7ixOeFGbN9D",  "object": "card",  "address_city": null,  "address_country": null,  "address_line1": null,  "address_line1_check": null,  "address_line2": null,  "address_state": null,  "address_zip": null,  "address_zip_check": null,  "brand": "Visa",  "country": "US",  "customer": "cus_NhD8HD2bY8dP3V",  "cvc_check": null,  "dynamic_last4": null,  "exp_month": 4,  "exp_year": 2024,  "fingerprint": "mToisGZ01V71BCos",  "funding": "credit",  "last4": "4242",  "metadata": {},  "name": null,  "tokenization_method": null,  "wallet": null}`# Create a card

When you create a new credit card, you must specify a customer or recipient on which to create it.

If the card’s owner has no default card, then the new card will become the default. However, if the owner already has a default, then it will not change. To change the default, you should update the customer to have a new default_source.

### Parameters

- sourceobject | stringRequiredA token, like the ones returned by Stripe.js or a dictionary containing a user’s card details (with the options shown below). Stripe will automatically validate the card.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns the Card object.

POST/v1/customers/:id/sourcesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/customers/cus_9s6XGDTHzA66Po/sources \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d source=tok_visa`Response`{  "id": "card_1NGTaT2eZvKYlo2CZWSctn5n",  "object": "card",  "address_city": null,  "address_country": null,  "address_line1": null,  "address_line1_check": null,  "address_line2": null,  "address_state": null,  "address_zip": null,  "address_zip_check": null,  "brand": "Visa",  "country": "US",  "customer": "cus_9s6XGDTHzA66Po",  "cvc_check": "pass",  "dynamic_last4": null,  "exp_month": 8,  "exp_year": 2024,  "fingerprint": "Xt5EWLLDS7FJjR1c",  "funding": "credit",  "last4": "4242",  "metadata": {},  "name": null,  "redaction": null,  "tokenization_method": null,  "wallet": null}`# Update a card

Updates a specified card for a given customer.

### Parameters

- address_citystringCity/District/Suburb/Town/Village.


- address_countrystringBilling address country, if provided when creating card.


- address_line1stringAddress line 1 (Street address/PO Box/Company name).


- address_line2stringAddress line 2 (Apartment/Suite/Unit/Building).


- address_statestringState/County/Province/Region.


- address_zipstringZIP or postal code.


- exp_monthstringTwo digit number representing the card’s expiration month.


- exp_yearstringFour digit number representing the card’s expiration year.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- namestringCardholder name.



### Returns

POST/v1/customers/:id/sources/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/customers/acct_1032D82eZvKYlo2C/sources/card_1NBLeN2eZvKYlo2CIq1o7Pzs \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d name="Jenny Rosen"`Response`{  "id": "card_1NBLeN2eZvKYlo2CIq1o7Pzs",  "object": "card",  "address_city": null,  "address_country": null,  "address_line1": null,  "address_line1_check": null,  "address_line2": null,  "address_state": null,  "address_zip": null,  "address_zip_check": null,  "brand": "Visa",  "country": "US",  "cvc_check": "pass",  "dynamic_last4": null,  "exp_month": 8,  "exp_year": 2024,  "fingerprint": "Xt5EWLLDS7FJjR1c",  "funding": "credit",  "last4": "4242",  "metadata": {},  "name": "Jenny Rosen",  "redaction": null,  "tokenization_method": null,  "wallet": null,  "account": "acct_1032D82eZvKYlo2C"}`# Retrieve a card

You can always see the 10 most recent cards directly on a customer; this method lets you retrieve details about a specific card stored on the customer.

### Parameters

No parameters.

### Returns

Returns the Card object.

GET/v1/customers/:id/cards/:idcURL[](#)[](#)`curl https://api.stripe.com/v1/customers/cus_NhD8HD2bY8dP3V/cards/card_1MvoiELkdIwHu7ixOeFGbN9D \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "card_1MvoiELkdIwHu7ixOeFGbN9D",  "object": "card",  "address_city": null,  "address_country": null,  "address_line1": null,  "address_line1_check": null,  "address_line2": null,  "address_state": null,  "address_zip": null,  "address_zip_check": null,  "brand": "Visa",  "country": "US",  "customer": "cus_NhD8HD2bY8dP3V",  "cvc_check": null,  "dynamic_last4": null,  "exp_month": 4,  "exp_year": 2024,  "fingerprint": "mToisGZ01V71BCos",  "funding": "credit",  "last4": "4242",  "metadata": {},  "name": null,  "tokenization_method": null,  "wallet": null}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`