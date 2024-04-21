htmlCreate a test clock | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Create a test clockTest helper

Creates a new test clock that can be attached to new customers and quotes.

### Parameters

- frozen_timetimestampRequiredThe initial frozen time for this test clock.


- namestringThe name for this test clock.



### Returns

The newly created TestClock object is returned upon success. Otherwise, this call raises an error.

POST/v1/test_helpers/test_clocksServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/test_helpers/test_clocks \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d frozen_time=1577836800`Response`{  "id": "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",  "object": "test_helpers.test_clock",  "created": 1680112806,  "deletes_after": 1680717606,  "frozen_time": 1577836800,  "livemode": false,  "name": null,  "status": "ready"}`# Retrieve a test clockTest helper

Retrieves a test clock.

### Parameters

No parameters.

### Returns

Returns the TestClock object. Otherwise, this call raises an error.

GET/v1/test_helpers/test_clocks/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/test_helpers/test_clocks/clock_1Mr3I22eZvKYlo2Ck0rgMqd7 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",  "object": "test_helpers.test_clock",  "created": 1680112806,  "deletes_after": 1680717606,  "frozen_time": 1577836800,  "livemode": false,  "name": null,  "status": "ready"}`# List all test clocksTest helper

Returns a list of your test clocks.

### Parameters

No parameters.

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit test clocks, starting after starting_after. Each entry in the array is a separate test clock object. If no more test clocks are available, the resulting array will be empty.

GET/v1/test_helpers/test_clocksServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/test_helpers/test_clocks \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/test_helpers/test_clocks",  "has_more": false,  "data": [    {      "id": "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",      "object": "test_helpers.test_clock",      "created": 1680112806,      "deletes_after": 1680717606,      "frozen_time": 1577836800,      "livemode": false,      "name": null,      "status": "ready"    }    {...}    {...}  ],}`# Delete a test clockTest helper

Deletes a test clock.

### Parameters

No parameters.

### Returns

The deleted TestClock object is returned upon success. Otherwise, this call raises an error.

DELETE/v1/test_helpers/test_clocks/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X DELETE https://api.stripe.com/v1/test_helpers/test_clocks/clock_1Mr3I22eZvKYlo2Ck0rgMqd7 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",  "object": "test_helpers.test_clock",  "deleted": true}`# Advance a test clockTest helper

Starts advancing a test clock to a specified time in the future. Advancement is done when status changes to Ready.

### Parameters

- frozen_timetimestampRequiredThe time to advance the test clock. Must be after the test clock’s current frozen time. Cannot be more than two intervals in the future from the shortest subscription in this test clock. If there are no subscriptions in this test clock, it cannot be more than two years in the future.



### Returns

A TestClock object with status Advancing is returned upon success. Otherwise, this call raises an error.

POST/v1/test_helpers/test_clocks/:id/advanceServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/test_helpers/test_clocks/clock_1Mr3I22eZvKYlo2Ck0rgMqd7/advance \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d frozen_time=1680199613`Response`{  "id": "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",  "object": "test_helpers.test_clock",  "created": 1680112806,  "deletes_after": 1680717606,  "frozen_time": 1577836800,  "livemode": false,  "name": null,  "status": "advancing"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`