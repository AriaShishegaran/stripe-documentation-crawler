htmlForwarding Request | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Forwarding RequestPreview feature

Instructs Stripe to make a request on your behalf using the destination URL. The destination URL is activated by Stripe at the time of onboarding. Stripe verifies requests with your credentials provided during onboarding, and injects card details from the payment_method into the request.

Stripe redacts all sensitive fields and headers, including authentication credentials and card numbers, before storing the request and response data in the forwarding Request object, which are subject to a 30-day retention period.

You can provide a Stripe idempotency key to make sure that requests with the same key result in only one outbound request. The Stripe idempotency key provided should be unique and different from any idempotency keys provided on the underlying third-party request.

Forwarding Requests are synchronous requests that return a response or time out according to Stripe’s limits.

Related guide: Forward card details to third-party API endpoints.

Endpoints
# The ForwardingRequest objectPreview feature

### Attributes

- idstringUnique identifier for the object.


- objectstringString representing the object’s type. Objects of the same type share the same value.


- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.


- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.


- payment_methodstringThe PaymentMethod to insert into the forwarded request. Forwarding previously consumed PaymentMethods is allowed.


- replacementsarray of enumsThe field kinds to be replaced in the forwarded request.

Possible enum values`card_cvc`Replace the card cvc field

`card_expiry`Replace the card expiry fields like month and year

`card_number`Replace the card number field

`cardholder_name`Replace the cardholder name field


- request_contextnullableobjectContext about the request from Stripe’s servers to the destination endpoint.

Show child attributes
- request_detailsnullableobjectThe request that was sent to the destination endpoint. We redact any sensitive fields.

Show child attributes
- response_detailsnullableobjectThe response that the destination endpoint returned to us. We redact any sensitive fields.

Show child attributes
- urlnullablestringThe destination URL for the forwarded request. Must be supported by the config.



The ForwardingRequest object`{  "id": "fwdreq_123",  "object": "forwarding.request",  "created": 1234567890,  "livemode": false,  "payment_method": "pm_456",  "request_details": {    "body": "{\"amount\":{\"value\":1000,\"currency\":\"usd\"},\"paymentMethod\":{\"number\":\"424242******4242\",\"expiryMonth\":\"03\",\"expiryYear\":\"2030\",\"cvc\":\"***\",\"holderName\":\"First Last\"},\"reference\":\"{{REFERENCE_ID}}\"}",    "headers": [      {        "name": "Destination-API-Key",        "value": "{{DESTINATION_API_KEY}}"      },      {        "name": "Destination-Idempotency-Key",        "value": "{{DESTINATION_IDEMPOTENCY_KEY}}"      },      {        "name": "Content-Type",        "value": "application/json"      }    ],    "http_method": "POST"  },  "request_context": {    "destination_ip_address": "35.190.113.80",    "destination_duration": 234  },  "response_details": {    "body": "{\"transactionId\":\"example1234\"}",    "headers": [      {        "name": "Content-Type",        "value": "application/json;charset=UTF-8"      }    ],    "status": 200  },  "url": "https://endpoint-url/v1/payments",  "replacements": [    "card_number",    "card_expiry",    "card_cvc",    "cardholder_name"  ]}`# Create a ForwardingRequest

Creates a ForwardingRequest object.

### Parameters

- payment_methodstringRequiredThe PaymentMethod to insert into the forwarded request. Forwarding previously consumed PaymentMethods is allowed.


- replacementsarray of enumsRequiredThe field kinds to be replaced in the forwarded request.

Possible enum values`card_cvc`Replace the card cvc field

`card_expiry`Replace the card expiry fields like month and year

`card_number`Replace the card number field

`cardholder_name`Replace the cardholder name field


- requestobjectRequiredThe request body and headers to be sent to the destination endpoint.

Show child parameters
- urlstringRequiredThe destination URL for the forwarded request. Must be supported by the config.



### Returns

Returns a ForwardingRequest object.

POST/v1/forwarding/requestsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/forwarding/requests \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  --data-urlencode url="https://endpoint-url/v1/payments" \  -d payment_method=pm_card_visa \  -d "replacements[0]"=card_number \  -d "replacements[1]"=card_expiry \  -d "replacements[2]"=card_cvc \  -d "replacements[3]"=cardholder_name \  --data-urlencode "request[body]"="{\"amount\":{\"value\":1000,\"currency\":\"usd\"},\"paymentMethod\":{\"number\":\"\",\"expiryMonth\":\"\",\"expiryYear\":\"\",\"cvc\":\"\",\"holderName\":\"\"},\"reference\":\"{{REFERENCE_ID}}\"}" \  -d "request[headers][0][name]"=Destination-API-Key \  -d "request[headers][0][value]"={{DESTINATION_API_KEY}} \  -d "request[headers][1][name]"=Destination-Idempotency-Key \  -d "request[headers][1][value]"={{DESTINATION_IDEMPOTENCY_KEY}}`Response`{  "id": "fwdreq_123",  "object": "forwarding.request",  "created": 1234567890,  "livemode": false,  "payment_method": "pm_456",  "request_details": {    "body": "{\"amount\":{\"value\":1000,\"currency\":\"usd\"},\"paymentMethod\":{\"number\":\"424242******4242\",\"expiryMonth\":\"03\",\"expiryYear\":\"2030\",\"cvc\":\"***\",\"holderName\":\"First Last\"},\"reference\":\"{{REFERENCE_ID}}\"}",    "headers": [      {        "name": "Destination-API-Key",        "value": "{{DESTINATION_API_KEY}}"      },      {        "name": "Destination-Idempotency-Key",        "value": "{{DESTINATION_IDEMPOTENCY_KEY}}"      },      {        "name": "Content-Type",        "value": "application/json"      }    ],    "http_method": "POST"  },  "request_context": {    "destination_ip_address": "35.190.113.80",    "destination_duration": 234  },  "response_details": {    "body": "{\"transactionId\":\"example1234\"}",    "headers": [      {        "name": "Content-Type",        "value": "application/json;charset=UTF-8"      }    ],    "status": 200  },  "url": "https://endpoint-url/v1/payments",  "replacements": [    "card_number",    "card_expiry",    "card_cvc",    "cardholder_name"  ]}`# Retrieve a ForwardingRequest

Retrieves a ForwardingRequest object.

### Parameters

No parameters.

### Returns

Returns a ForwardingRequest object.

GET/v1/forwarding/requests/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/forwarding/requests/fwdreq_123 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "fwdreq_123",  "object": "forwarding.request",  "created": 1234567890,  "livemode": false,  "payment_method": "pm_456",  "request_details": {    "body": "{\"amount\":{\"value\":1000,\"currency\":\"usd\"},\"paymentMethod\":{\"number\":\"424242******4242\",\"expiryMonth\":\"03\",\"expiryYear\":\"2030\",\"cvc\":\"***\",\"holderName\":\"First Last\"},\"reference\":\"{{REFERENCE_ID}}\"}",    "headers": [      {        "name": "Destination-API-Key",        "value": "{{DESTINATION_API_KEY}}"      },      {        "name": "Destination-Idempotency-Key",        "value": "{{DESTINATION_IDEMPOTENCY_KEY}}"      },      {        "name": "Content-Type",        "value": "application/json"      }    ],    "http_method": "POST"  },  "request_context": {    "destination_ip_address": "35.190.113.80",    "destination_duration": 234  },  "response_details": {    "body": "{\"transactionId\":\"example1234\"}",    "headers": [      {        "name": "Content-Type",        "value": "application/json;charset=UTF-8"      }    ],    "status": 200  },  "url": "https://endpoint-url/v1/payments",  "replacements": [    "card_number",    "card_expiry",    "card_cvc",    "cardholder_name"  ]}`# List all ForwardingRequests

Lists all ForwardingRequest objects.

### Parameters

- createdobjectSimilar to other List endpoints, filters results based on created timestamp. You can pass gt, gte, lt, and lte timestamp values.

Show child parameters
- ending_beforestringA pagination cursor to fetch the previous page of the list. The value must be a ForwardingRequest ID.


- limitintegerA limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.


- starting_afterstringA pagination cursor to fetch the next page of the list. The value must be a ForwardingRequest ID.



### Returns

Returns a list of ForwardingRequest objects.

GET/v1/forwarding/requestsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/forwarding/requests \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/forwarding/requests",  "has_more": false,  "data": [    {      "id": "fwdreq_123",      "object": "forwarding.request",      "created": 1234567890,      "livemode": false,      "payment_method": "pm_456",      "request_details": {        "body": "{\"amount\":{\"value\":1000,\"currency\":\"usd\"},\"paymentMethod\":{\"number\":\"424242******4242\",\"expiryMonth\":\"03\",\"expiryYear\":\"2030\",\"cvc\":\"***\",\"holderName\":\"First Last\"},\"reference\":\"{{REFERENCE_ID}}\"}",        "headers": [          {            "name": "Destination-API-Key",            "value": "{{DESTINATION_API_KEY}}"          },          {            "name": "Destination-Idempotency-Key",            "value": "{{DESTINATION_IDEMPOTENCY_KEY}}"          },          {            "name": "Content-Type",            "value": "application/json"          }        ],        "http_method": "POST"      },      "request_context": {        "destination_ip_address": "35.190.113.80",        "destination_duration": 234      },      "response_details": {        "body": "{\"transactionId\":\"example1234\"}",        "headers": [          {            "name": "Content-Type",            "value": "application/json;charset=UTF-8"          }        ],        "status": 200      },      "url": "https://endpoint-url/v1/payments",      "replacements": [        "card_number",        "card_expiry",        "card_cvc",        "cardholder_name"      ]    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`