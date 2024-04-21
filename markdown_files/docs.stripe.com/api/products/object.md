htmlThe Product object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The Product object

### Attributes

- idstringUnique identifier for the object.


- activebooleanWhether the product is currently available for purchase.


- default_pricenullablestringExpandableThe ID of the Price object that is the default price for this product.


- descriptionnullablestringThe product’s description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- namestringThe product’s name, meant to be displayable to the customer.



### More attributesExpand all

- objectstring
- createdtimestamp
- imagesarray of strings
- livemodeboolean
- marketing_featuresarray of objects
- package_dimensionsnullableobject
- shippablenullableboolean
- statement_descriptornullablestring
- tax_codenullablestringExpandable
- unit_labelnullablestring
- updatedtimestamp
- urlnullablestring

The Product object`{  "id": "prod_NWjs8kKbJWmuuc",  "object": "product",  "active": true,  "created": 1678833149,  "default_price": null,  "description": null,  "images": [],  "features": [],  "livemode": false,  "metadata": {},  "name": "Gold Plan",  "package_dimensions": null,  "shippable": null,  "statement_descriptor": null,  "tax_code": null,  "unit_label": null,  "updated": 1678833149,  "url": null}`# Create a product

Creates a new product object.

### Parameters

- namestringRequiredThe product’s name, meant to be displayable to the customer.


- activebooleanWhether the product is currently available for purchase. Defaults to true.


- descriptionstringThe product’s description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.


- idstringAn identifier will be randomly generated by Stripe. You can optionally override this ID, but the ID must be unique across all products in your Stripe account.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- default_price_dataobject
- imagesarray of strings
- marketing_featuresarray of objects
- package_dimensionsobject
- shippableboolean
- statement_descriptorstring
- tax_codestring
- unit_labelstring
- urlstring

### Returns

Returns a product object if the call succeeded.

POST/v1/productsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/products \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d name="Gold Plan"`Response`{  "id": "prod_NWjs8kKbJWmuuc",  "object": "product",  "active": true,  "created": 1678833149,  "default_price": null,  "description": null,  "images": [],  "features": [],  "livemode": false,  "metadata": {},  "name": "Gold Plan",  "package_dimensions": null,  "shippable": null,  "statement_descriptor": null,  "tax_code": null,  "unit_label": null,  "updated": 1678833149,  "url": null}`# Update a product

Updates the specific product by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

### Parameters

- activebooleanWhether the product is available for purchase.


- default_pricestringThe ID of the Price object that is the default price for this product.


- descriptionstringThe product’s description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- namestringThe product’s name, meant to be displayable to the customer.



### More parametersExpand all

- imagesarray of strings
- marketing_featuresarray of objects
- package_dimensionsobject
- shippableboolean
- statement_descriptorstring
- tax_codestring
- unit_labelstring
- urlstring

### Returns

Returns the product object if the update succeeded.

POST/v1/products/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/products/prod_NWjs8kKbJWmuuc \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "prod_NWjs8kKbJWmuuc",  "object": "product",  "active": true,  "created": 1678833149,  "default_price": null,  "description": null,  "images": [],  "features": [],  "livemode": false,  "metadata": {    "order_id": "6735"  },  "name": "Gold Plan",  "package_dimensions": null,  "shippable": null,  "statement_descriptor": null,  "tax_code": null,  "unit_label": null,  "updated": 1678833149,  "url": null}`# Retrieve a product

Retrieves the details of an existing product. Supply the unique product ID from either a product creation request or the product list, and Stripe will return the corresponding product information.

### Parameters

No parameters.

### Returns

Returns a product object if a valid identifier was provided.

GET/v1/products/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/products/prod_NWjs8kKbJWmuuc \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "prod_NWjs8kKbJWmuuc",  "object": "product",  "active": true,  "created": 1678833149,  "default_price": null,  "description": null,  "images": [],  "features": [],  "livemode": false,  "metadata": {},  "name": "Gold Plan",  "package_dimensions": null,  "shippable": null,  "statement_descriptor": null,  "tax_code": null,  "unit_label": null,  "updated": 1678833149,  "url": null}`# List all products

Returns a list of your products. The products are returned sorted by creation date, with the most recently created products appearing first.

### Parameters

- activebooleanOnly return products that are active or inactive (e.g., pass false to list all inactive products).



### More parametersExpand all

- createdobject
- ending_beforestring
- idsarray of strings
- limitinteger
- shippableboolean
- starting_afterstring
- urlstring

### Returns

A dictionary with a data property that contains an array of up to limit products, starting after product starting_after. Each entry in the array is a separate product object. If no more products are available, the resulting array will be empty.

GET/v1/productsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/products \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/products",  "has_more": false,  "data": [    {      "id": "prod_NWjs8kKbJWmuuc",      "object": "product",      "active": true,      "created": 1678833149,      "default_price": null,      "description": null,      "images": [],      "features": [],      "livemode": false,      "metadata": {},      "name": "Gold Plan",      "package_dimensions": null,      "shippable": null,      "statement_descriptor": null,      "tax_code": null,      "unit_label": null,      "updated": 1678833149,      "url": null    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`