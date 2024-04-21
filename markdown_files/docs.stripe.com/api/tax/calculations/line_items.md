htmlRetrieve a calculation's line items | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Retrieve a calculation's line items

Retrieves the line items of a persisted tax calculation as a collection.

### Parameters

- ending_beforestringA cursor for use in pagination. ending_before is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_bar, your subsequent call can include ending_before=obj_bar in order to fetch the previous page of the list.


- limitintegerA limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.


- starting_afterstringA cursor for use in pagination. starting_after is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include starting_after=obj_foo in order to fetch the next page of the list.



### Returns

A list of Line Item objects if the Tax calculation is found. Otherwise returns a ‘not found’ error.

GET/v1/tax/calculations/:id/line_itemsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/tax/calculations/taxcalc_1NpJD42eZvKYlo2CUti522cz/line_items \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/tax/calculations/taxcalc_1NpJD42eZvKYlo2CUti522cz/line_items",  "has_more": false,  "data": [    {      "object": "list",      "url": "/v1/tax/calculations/taxcalc_1NpJD42eZvKYlo2CUti522cz/line_items",      "has_more": false,      "data": [        {          "id": "tax_li_OcYJb5mQOSSSWD",          "object": "tax.calculation_line_item",          "amount": 1499,          "amount_tax": 148,          "livemode": false,          "product": null,          "quantity": 1,          "reference": "Pepperoni Pizza",          "tax_behavior": "exclusive",          "tax_code": "txcd_40060003"        }      ]    }    {...}    {...}  ],}`# Calculate tax

Calculates tax based on input and returns a Tax Calculation object.

### Parameters

- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.


- line_itemsarray of objectsRequiredA list of items the customer is purchasing.

Show child parameters
- customer_detailsobjectRequired unless customer providedDetails about the customer, including address and tax IDs.

Show child parameters
- shipping_costobjectShipping cost details to be used for the calculation.

Show child parameters

### More parametersExpand all

- customerstringRequired unless customer_details provided
- tax_dateinteger

### Returns

A Tax Calculation object if calculation succeeds. Otherwise, an error (for example, indicating that the customer address was invalid).

POST/v1/tax/calculationsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/tax/calculations \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d currency=usd \  -d "customer_details[address][line1]"="920 5th Ave" \  -d "customer_details[address][city]"=Seattle \  -d "customer_details[address][state]"=WA \  -d "customer_details[address][postal_code]"=98104 \  -d "customer_details[address][country]"=US \  -d "customer_details[address_source]"=shipping \  -d "line_items[0][amount]"=1499 \  -d "line_items[0][tax_code]"=txcd_10000000 \  -d "line_items[0][reference]"="Music Streaming Coupon" \  -d "shipping_cost[amount]"=300 \  -d "expand[0]"=line_items`Response`{  "id": "taxcalc_1OduxkBUZ691iUZ4iWvpMApI",  "object": "tax.calculation",  "amount_total": 1953,  "currency": "usd",  "customer": null,  "customer_details": {    "address": {      "city": "Seattle",      "country": "US",      "line1": "9205thAve",      "line2": null,      "postal_code": "98104",      "state": "WA"    },    "address_source": "shipping",    "ip_address": null,    "tax_ids": [],    "taxability_override": "none"  },  "expires_at": 1706708005,  "line_items": {    "object": "list",    "data": [      {        "id": "tax_li_PSqf3RMNZa23H4",        "object": "tax.calculation_line_item",        "amount": 1499,        "amount_tax": 154,        "livemode": false,        "product": null,        "quantity": 1,        "reference": "Music Streaming Coupon",        "tax_behavior": "exclusive",        "tax_code": "txcd_10000000"      }    ],    "has_more": false,    "total_count": 1,    "url": "/v1/tax/calculations/taxcalc_1OduxkBUZ691iUZ4iWvpMApI/line_items"  },  "livemode": false,  "ship_from_details": null,  "shipping_cost": {    "amount": 300,    "amount_tax": 0,    "tax_behavior": "exclusive",    "tax_code": "txcd_92010001"  },  "tax_amount_exclusive": 154,  "tax_amount_inclusive": 0,  "tax_breakdown": [    {      "amount": 154,      "inclusive": false,      "tax_rate_details": {        "country": "US",        "percentage_decimal": "10.25",        "state": "WA",        "tax_type": "sales_tax"      },      "taxability_reason": "standard_rated",      "taxable_amount": 1499    },    {      "amount": 0,      "inclusive": false,      "tax_rate_details": {        "country": "DE",        "percentage_decimal": "0.0",        "state": null,        "tax_type": "vat"      },      "taxability_reason": "zero_rated",      "taxable_amount": 300    }  ],  "tax_date": 1706535204}`# Tax Registrations

A Tax Registration lets us know that your business is registered to collect tax on payments within a region, enabling you to automatically collect tax.

Stripe doesn’t register on your behalf with the relevant authorities when you create a Tax Registration object. For more information on how to register to collect tax, see our guide.

Related guide: Using the Registrations API

Endpoints
Show

# Tax Transactions

A Tax Transaction records the tax collected from or refunded to your customer.

Related guide: Calculate tax in your custom payment flow

Endpoints
Show

# Tax Settings

You can use Tax Settings to manage configurations used by Stripe Tax calculations.

Related guide: Using the Settings API

Endpoints
Show

# Verification Session

A VerificationSession guides you through the process of collecting and verifying the identities of your users. It contains details about the type of verification, such as what verification check to perform. Only create one VerificationSession for each verification in your system.

A VerificationSession transitions through multiple statuses throughout its lifetime as it progresses through the verification flow. The VerificationSession contains the user’s verified data after verification checks are complete.

Related guide: The Verification Sessions API

Endpoints
Show

# Verification Report

A VerificationReport is the result of an attempt to collect and verify data from a user. The collection of verification checks performed is determined from the type and options parameters used. You can find the result of each verification check performed in the appropriate sub-resource: document, id_number, selfie.

Each VerificationReport contains a copy of any data collected by the user as well as reference IDs which can be used to access collected images through the FileUpload API. To configure and create VerificationReports, use the VerificationSession API.

Related guides: Accessing verification results.

Endpoints
Show

# Crypto Onramp Session

A Crypto Onramp Session represents your customer’s session as they purchase cryptocurrency through Stripe. Once payment is successful, Stripe will fulfill the delivery of cryptocurrency to your user’s wallet and contain a reference to the crypto transaction ID.

You can create an onramp session on your server and embed the widget on your frontend. Alternatively, you can redirect your users to the standalone hosted onramp.

Related guide: Integrate the onramp

Endpoints
Show

# Crypto Onramp Quotes

Crypto Onramp Quotes are estimated quotes for onramp conversions into all the different cryptocurrencies on different networks. The Quotes API allows you to display quotes in your product UI before directing the user to the onramp widget.

Related guide: Quotes API

Endpoints
Show

# Climate Order

Orders represent your intent to purchase a particular Climate product. When you create an order, the payment is deducted from your merchant balance.

Endpoints
Show

# Climate Product

A Climate product represents a type of carbon removal unit available for reservation. You can retrieve it to see the current price and availability.

Endpoints
Show

# Climate Supplier

A supplier of carbon removal.

Endpoints
Show

# Forwarding RequestPreview feature

Instructs Stripe to make a request on your behalf using the destination URL. The destination URL is activated by Stripe at the time of onboarding. Stripe verifies requests with your credentials provided during onboarding, and injects card details from the payment_method into the request.

Stripe redacts all sensitive fields and headers, including authentication credentials and card numbers, before storing the request and response data in the forwarding Request object, which are subject to a 30-day retention period.

You can provide a Stripe idempotency key to make sure that requests with the same key result in only one outbound request. The Stripe idempotency key provided should be unique and different from any idempotency keys provided on the underlying third-party request.

Forwarding Requests are synchronous requests that return a response or time out according to Stripe’s limits.

Related guide: Forward card details to third-party API endpoints.

Endpoints
Show

# Webhook Endpoints

You can configure webhook endpoints via the API to be notified about events that happen in your Stripe account or connected accounts.

Most users configure webhooks from the dashboard, which provides a user interface for registering and testing your webhook endpoints.

Related guide: Setting up webhooks

Endpoints
Show

Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`