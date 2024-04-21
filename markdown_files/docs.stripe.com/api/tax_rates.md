htmlTax Rate | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Tax Rate

Tax rates can be applied to invoices, subscriptions and Checkout Sessions to collect tax.

Related guide: Tax rates

Endpoints
# The Tax Rate object

### Attributes

- idstringUnique identifier for the object.


- activebooleanDefaults to true. When set to false, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.


- countrynullablestringTwo-letter country code (ISO 3166-1 alpha-2).


- descriptionnullablestringAn arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.


- display_namestringThe display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.


- inclusivebooleanThis specifies if the tax rate is inclusive or exclusive.


- jurisdictionnullablestringThe jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.


- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- percentagefloatTax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.


- statenullablestringISO 3166-2 subdivision code, without country prefix. For example, “NY” for New York, United States.



### More attributesExpand all

- objectstring
- createdtimestamp
- effective_percentagenullablefloat
- jurisdiction_levelnullableenum
- livemodeboolean
- tax_typenullableenum

The Tax Rate object`{  "id": "txr_1MzS4RLkdIwHu7ixwvpZ9c2i",  "object": "tax_rate",  "active": true,  "country": null,  "created": 1682114687,  "description": "VAT Germany",  "display_name": "VAT",  "inclusive": false,  "jurisdiction": "DE",  "livemode": false,  "metadata": {},  "percentage": 16,  "state": null,  "tax_type": null}`# Create a tax rate

Creates a new tax rate.

### Parameters

- display_namestringRequiredThe display name of the tax rate, which will be shown to users.


- inclusivebooleanRequiredThis specifies if the tax rate is inclusive or exclusive.


- percentagefloatRequiredThis represents the tax rate percent out of 100.


- activebooleanFlag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.


- countrystringTwo-letter country code (ISO 3166-1 alpha-2).


- descriptionstringAn arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.


- jurisdictionstringThe jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- statestringISO 3166-2 subdivision code, without country prefix. For example, “NY” for New York, United States.



### More parametersExpand all

- tax_typeenum

### Returns

The created tax rate object.

POST/v1/tax_ratesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tax_rates \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d display_name=VAT \  -d description="VAT Germany" \  -d percentage=16 \  -d jurisdiction=DE \  -d inclusive=false`Response`{  "id": "txr_1MzS4RLkdIwHu7ixwvpZ9c2i",  "object": "tax_rate",  "active": true,  "country": null,  "created": 1682114687,  "description": "VAT Germany",  "display_name": "VAT",  "inclusive": false,  "jurisdiction": "DE",  "livemode": false,  "metadata": {},  "percentage": 16,  "state": null,  "tax_type": null}`# Update a tax rate

Updates an existing tax rate.

### Parameters

- activebooleanFlag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.


- countrystringTwo-letter country code (ISO 3166-1 alpha-2).


- descriptionstringAn arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.


- display_namestringThe display name of the tax rate, which will be shown to users.


- jurisdictionstringThe jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- statestringISO 3166-2 subdivision code, without country prefix. For example, “NY” for New York, United States.



### More parametersExpand all

- tax_typeenum

### Returns

The updated tax rate.

POST/v1/tax_rates/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tax_rates/txr_1MzS4RLkdIwHu7ixwvpZ9c2i \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d active=false`Response`{  "id": "txr_1MzS4RLkdIwHu7ixwvpZ9c2i",  "object": "tax_rate",  "active": false,  "country": null,  "created": 1682114687,  "description": "VAT Germany",  "display_name": "VAT",  "effective_percentage": 16,  "inclusive": false,  "jurisdiction": "DE",  "livemode": false,  "metadata": {},  "percentage": 16,  "state": null,  "tax_type": null}`# List all tax rates

Returns a list of your tax rates. Tax rates are returned sorted by creation date, with the most recently created tax rates appearing first.

### Parameters

- activebooleanOptional flag to filter by tax rates that are either active or inactive (archived).



### More parametersExpand all

- createdobject
- ending_beforestring
- inclusiveboolean
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit tax rates, starting after tax rate starting_after. Each entry in the array is a separate tax rate object. If no more tax rates are available, the resulting array will be empty.

GET/v1/tax_ratesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/tax_rates \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/tax_rates",  "has_more": false,  "data": [    {      "id": "txr_1MzS4RLkdIwHu7ixwvpZ9c2i",      "object": "tax_rate",      "active": true,      "country": null,      "created": 1682114687,      "description": "VAT Germany",      "display_name": "VAT",      "inclusive": false,      "jurisdiction": "DE",      "livemode": false,      "metadata": {},      "percentage": 16,      "state": null,      "tax_type": null    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`