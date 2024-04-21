htmlExternal Account Cards | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# External Account Cards

External account cards are debit cards associated with a Stripe platform’s connected accounts for the purpose of transferring funds to or from the connected accounts Stripe balance.

Endpoints
# The External Account Card object

### Attributes

- idstringUnique identifier for the object.


- accountnullablestringExpandablecustom Connect onlyThe account this card belongs to. This attribute will not be in the card object if the card belongs to a customer or recipient instead.


- address_citynullablestringCity/District/Suburb/Town/Village.


- address_countrynullablestringBilling address country, if provided when creating card.


- address_line1nullablestringAddress line 1 (Street address/PO Box/Company name).


- address_line2nullablestringAddress line 2 (Apartment/Suite/Unit/Building).


- address_statenullablestringState/County/Province/Region.


- address_zipnullablestringZIP or postal code.


- address_zip_checknullablestringIf address_zip was provided, results of the check: pass, fail, unavailable, or unchecked.


- brandstringCard brand. Can be American Express, Diners Club, Discover, Eftpos Australia, JCB, MasterCard, UnionPay, Visa, or Unknown.


- countrynullablestringTwo-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you’ve collected.


- currencynullableenumcustom Connect onlyThree-letter ISO code for currency. Only applicable on accounts (not customers or recipients). The card can be used as a transfer destination for funds in this currency.


- cvc_checknullablestringIf a CVC was provided, results of the check: pass, fail, unavailable, or unchecked. A result of unchecked indicates that CVC was provided but hasn’t been checked yet. Checks are typically performed when attaching a card to a Customer object, or when creating a charge. For more details, see Check if a card is valid without a charge.


- default_for_currencynullablebooleancustom Connect onlyWhether this card is the default external account for its currency.


- exp_monthintegerTwo-digit number representing the card’s expiration month.


- exp_yearintegerFour-digit number representing the card’s expiration year.


- fingerprintnullablestringUniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card—one for India and one for the rest of the world.


- fundingstringCard funding type. Can be credit, debit, prepaid, or unknown.


- last4stringThe last four digits of the card.


- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- namenullablestringCardholder name.


- statusnullablestringFor external accounts that are cards, possible values are new and errored. If a payout fails, the status is set to errored and scheduled payouts are stopped until account details are updated.



### More attributesExpand all

- objectstring
- address_line1_checknullablestring
- available_payout_methodsnullablearray of enums
- customernullablestringExpandable
- dynamic_last4nullablestring
- tokenization_methodnullablestring
- walletnullableobjectPreview feature

The External Account Card object`{  "id": "card_1MvoiELkdIwHu7ixOeFGbN9D",  "object": "card",  "address_city": null,  "address_country": null,  "address_line1": null,  "address_line1_check": null,  "address_line2": null,  "address_state": null,  "address_zip": null,  "address_zip_check": null,  "brand": "Visa",  "country": "US",  "customer": "cus_NhD8HD2bY8dP3V",  "cvc_check": null,  "dynamic_last4": null,  "exp_month": 4,  "exp_year": 2024,  "fingerprint": "mToisGZ01V71BCos",  "funding": "credit",  "last4": "4242",  "metadata": {},  "name": null,  "tokenization_method": null,  "wallet": null}`# Create a card

When you create a new debit card, you must specify a Custom account to create it on.

If the account has no default destination card, then the new card will become the default. However, if the owner already has a default then it will not change. To change the default, you should set default_for_currency to true when creating a card for a Custom account.

### Parameters

- external_accountobject | stringRequiredA token, like the ones returned by Stripe.js or a dictionary containing a user’s card details (with the options shown below). Stripe will automatically validate the card.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- default_for_currencyboolean

### Returns

Returns the card object

POST/v1/accounts/:id/external_accountsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d external_account=tok_visa_debit`Response`{  "id": "card_1NAiaG2eZvKYlo2CDXvcMb6m",  "object": "card",  "account": "acct_1032D82eZvKYlo2C",  "address_city": null,  "address_country": null,  "address_line1": null,  "address_line1_check": null,  "address_line2": null,  "address_state": null,  "address_zip": null,  "address_zip_check": null,  "brand": "Visa",  "country": "US",  "cvc_check": "pass",  "dynamic_last4": null,  "exp_month": 8,  "exp_year": 2024,  "fingerprint": "Xt5EWLLDS7FJjR1c",  "funding": "credit",  "last4": "4242",  "metadata": {},  "name": null,  "redaction": null,  "tokenization_method": null,  "wallet": null}`# Update a card

If you need to update only some card details, like the billing address or expiration date, you can do so without having to re-enter the full card details. Stripe also works directly with card networks so that your customers can continue using your service without interruption.

### Parameters

- default_for_currencybooleanWhen set to true, this becomes the default external account for its currency.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- address_citystring
- address_countrystring
- address_line1string
- address_line2string
- address_statestring
- address_zipstring
- exp_monthstring
- exp_yearstring
- namestring

### Returns

Returns the card object.

POST/v1/accounts/:id/external_accounts/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/card_1NBLeN2eZvKYlo2CIq1o7Pzs \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "card_1NBLeN2eZvKYlo2CIq1o7Pzs",  "object": "card",  "address_city": null,  "address_country": null,  "address_line1": null,  "address_line1_check": null,  "address_line2": null,  "address_state": null,  "address_zip": null,  "address_zip_check": null,  "brand": "Visa",  "country": "US",  "cvc_check": "pass",  "dynamic_last4": null,  "exp_month": 8,  "exp_year": 2024,  "fingerprint": "Xt5EWLLDS7FJjR1c",  "funding": "credit",  "last4": "4242",  "metadata": {    "order_id": "6735"  },  "name": "Jenny Rosen",  "redaction": null,  "tokenization_method": null,  "wallet": null,  "account": "acct_1032D82eZvKYlo2C"}`# Retrieve a card

By default, you can see the 10 most recent external accounts stored on a connected account directly on the object. You can also retrieve details about a specific card stored on the account.

### Parameters

No parameters.

### Returns

Returns the card object.

GET/v1/accounts/:id/external_accounts/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/external_accounts/card_1NAinb2eZvKYlo2C1Fm9mZsu \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "card_1NAinb2eZvKYlo2C1Fm9mZsu",  "object": "card",  "address_city": null,  "address_country": null,  "address_line1": null,  "address_line1_check": null,  "address_line2": null,  "address_state": null,  "address_zip": null,  "address_zip_check": null,  "brand": "Visa",  "country": "US",  "cvc_check": "pass",  "dynamic_last4": null,  "exp_month": 8,  "exp_year": 2024,  "fingerprint": "Xt5EWLLDS7FJjR1c",  "funding": "credit",  "last4": "4242",  "metadata": {},  "name": null,  "redaction": null,  "tokenization_method": null,  "wallet": null,  "account": "acct_1032D82eZvKYlo2C"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`