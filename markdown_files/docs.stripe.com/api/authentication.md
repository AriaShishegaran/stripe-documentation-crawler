htmlAuthentication | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Authentication

The Stripe API uses API keys to authenticate requests. You can view and manage your API keys in the Stripe Dashboard.

Test mode secret keys have the prefix sk_test_ and live mode secret keys have the prefix sk_live_. Alternatively, you can use restricted API keys for granular permissions.

Your API keys carry many privileges, so be sure to keep them secure! Do not share your secret API keys in publicly accessible areas such as GitHub, client-side code, and so forth.

All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests without authentication will also fail.

- Relatedvideo:[Authentication](/docs/videos/developer-foundations?video=authentication)

Authenticated RequestServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)`curl https://api.stripe.com/v1/charges \  -u sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:# The colon prevents curl from asking for a password.`Your API KeyA sample test API key is included in all the examples here, so you can test any example right away. Do not submit any personally identifiable information in requests made with this key.

To test requests using your account, replace the sample API key with your actual API key or sign in.

# Connected Accounts

To act as connected accounts, clients can issue requests using the Stripe-Account special header. Make sure that this header contains a Stripe account ID, which usually starts with the acct_ prefix.

The value is set per-request as shown in the adjacent code sample. Methods on the returned object reuse the same account ID.

- Relatedguide:[Making API calls for connected accounts](/docs/connect/authentication)

Per-Request AccountServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)`curl https://api.stripe.com/v1/charges/ch_3LmjFA2eZvKYlo2C09TLIsrw \  -u sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \  -H "Stripe-Account: acct_1032D82eZvKYlo2C" \  -G`# Errors

Stripe uses conventional HTTP response codes to indicate the success or failure of an API request. In general: Codes in the 2xx range indicate success. Codes in the 4xx range indicate an error that failed given the information provided (e.g., a required parameter was omitted, a charge failed, etc.). Codes in the 5xx range indicate an error with Stripe’s servers (these are rare).

Some 4xx errors that could be handled programmatically (e.g., a card is declined) include an error code that briefly explains the error reported.

### Attributes

- typeenumThe type of error returned. One of api_error, card_error, idempotency_error, or invalid_request_error

Possible enum values`api_error``card_error``idempotency_error``invalid_request_error`
- codenullablestringFor some errors that could be handled programmatically, a short string indicating the error code reported.


- decline_codenullablestringFor card errors resulting from a card issuer decline, a short string indicating the card issuer’s reason for the decline if they provide one.


- messagenullablestringA human-readable message providing more details about the error. For card errors, these messages can be shown to your users.


- paramnullablestringIf the error is parameter-specific, the parameter related to the error. For example, you can use this to display a message near the correct form field.


- payment_intentnullableobjectThe PaymentIntent object for errors returned on a request involving a PaymentIntent.

Show child attributes

### MoreExpand all

- chargenullablestring
- payment_method_typenullablestring
- doc_urlnullablestring
- request_log_urlnullablestring
- setup_intentnullableobject
- sourcenullableobject
- payment_methodnullableobject

HTTP Status Code Summary200OKEverything worked as expected.400Bad RequestThe request was unacceptable, often due to missing a required parameter.401UnauthorizedNo valid API key provided.402Request FailedThe parameters were valid but the request failed.403ForbiddenThe API key doesn’t have permissions to perform the request.404Not FoundThe requested resource doesn’t exist.409ConflictThe request conflicts with another request (perhaps due to using the same idempotent key).429Too Many RequestsToo many requests hit the API too quickly. We recommend an exponential backoff of your requests.500, 502, 503, 504Server ErrorsSomething went wrong on Stripe’s end. (These are rare.)Error Types`api_error`API errors cover any other type of problem (e.g., a temporary problem with Stripe’s servers), and are extremely uncommon.`card_error`Card errors are the most common type of error you should expect to handle. They result when the user enters a card that can’t be charged for some reason.`idempotency_error`Idempotency errors occur when an`Idempotency-Key`is re-used on a request that does not match the first request’s API endpoint and parameters.`invalid_request_error`Invalid request errors arise when your request has invalid parameters.# Handling errors

Our Client libraries raise exceptions for many reasons, such as a failed charge, invalid parameters, authentication errors, and network unavailability. We recommend writing code that gracefully handles all possible API exceptions.

- Relatedguide:[Error Handling](/docs/error-handling)

Server-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)`# Select a client library to see examples of# handling different kinds of errors.`# Expanding Responses

Many objects allow you to request additional information as an expanded response by using the expand request parameter. This parameter is available on all API requests, and applies to the response of that request only. You can expand responses in two ways.

In many cases, an object contains the ID of a related object in its response properties. For example, a Charge might have an associated Customer ID. You can expand these objects in line with the expand request parameter. The expandable label in this documentation indicates ID fields that you can expand into objects.

Some available fields aren’t included in the responses by default, such as the number and cvc fields for the Issuing Card object. You can request these fields as an expanded response by using the expand request parameter.

You can expand recursively by specifying nested fields after a dot (.). For example, requesting invoice.subscription on a charge expands the invoice property into a full Invoice object, then expands the subscription property on that invoice into a full Subscription object.

You can use the expand parameter on any endpoint that returns expandable fields, including list, create, and update endpoints.

Expansions on list requests start with the data property. For example, you can expand data.customers on a request to list charges and associated customers. Performing deep expansions on numerous list requests might result in slower processing times.

Expansions have a maximum depth of four levels (for example, the deepest expansion allowed when listing charges is data.invoice.subscription.default_source).

You can expand multiple objects at the same time by identifying multiple items in the expand array.

- Relatedguide:[Expanding responses](/docs/expand)
- Relatedvideo:[Expand](https://www.youtube.com/watch?v=m8Vj_CEWyQc)

Server-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)`curl https://api.stripe.com/v1/charges/ch_3LmzzQ2eZvKYlo2C0XjzUzJV \  -u sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \  -d "expand[]"=customer \  -d "expand[]"="invoice.subscription" \  -G`Response`{  "id": "ch_3LmzzQ2eZvKYlo2C0XjzUzJV",  "object": "charge",  "customer": {    "id": "cu_14HOpH2eZvKYlo2CxXIM7Pb2",    "object": "customer",    // ...  },  "invoice": {    "id": "in_1LmzzQ2eZvKYlo2CpyWn8szu",    "object": "invoice",    "subscription": {      "id": "su_1LmzoG2eZvKYlo2Cpw6S7dAq",      "object": "subscription",      // ...    },    // ...  },  // ...}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`