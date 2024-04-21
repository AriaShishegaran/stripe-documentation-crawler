htmlRetrieve a product | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Retrieve a product

Retrieves the details of a Climate product with the given ID.

### Parameters

No parameters.

### Returns

Returns a Climate product object if a valid identifier was provided. Throws an error otherwise.

GET/v1/climate/products/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/climate/products/climsku_frontier_offtake_portfolio_2027 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "climsku_frontier_offtake_portfolio_2027",  "object": "climate.product",  "created": 1881439203,  "current_prices_per_metric_ton": {    "usd": {      "amount_fees": 1650,      "amount_subtotal": 55000,      "amount_total": 56650    }  },  "delivery_year": 2027,  "livemode": false,  "metric_tons_available": "18000",  "name": "Frontier's 2027 offtake portfolio",  "suppliers": [    {      "id": "climsup_charm_industrial",      "object": "climate.supplier",      "info_url": "https://frontierclimate.com/portfolio/charm-industrial",      "livemode": false,      "locations": [        {          "city": "San Francisco",          "country": "US",          "latitude": 37.7749,          "longitude": -122.4194,          "region": "CA"        }      ],      "name": "Charm Industrial",      "removal_pathway": "biomass_carbon_removal_and_storage"    }  ]}`# List products

Lists all available Climate product objects.

### Parameters

No parameters.

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit products, starting after product starting_after. Each entry in the array is a separate product object. If no more products are available, the resulting array is empty.

GET/v1/climate/productsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/climate/products \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/climate/products",  "has_more": false,  "data": [    {      "id": "climsku_frontier_offtake_portfolio_2027",      "object": "climate.product",      "created": 1881439203,      "current_prices_per_metric_ton": {        "usd": {          "amount_fees": 1650,          "amount_subtotal": 55000,          "amount_total": 56650        }      },      "delivery_year": 2027,      "livemode": false,      "metric_tons_available": "18000",      "name": "Frontier's 2027 offtake portfolio",      "suppliers": [        {          "id": "climsup_charm_industrial",          "object": "climate.supplier",          "info_url": "https://frontierclimate.com/portfolio/charm-industrial",          "livemode": false,          "locations": [            {              "city": "San Francisco",              "country": "US",              "latitude": 37.7749,              "longitude": -122.4194,              "region": "CA"            }          ],          "name": "Charm Industrial",          "removal_pathway": "biomass_carbon_removal_and_storage"        }      ]    }    {...}    {...}  ],}`# Climate Supplier

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