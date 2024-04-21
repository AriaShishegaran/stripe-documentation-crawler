htmlTest Clocks | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Test ClocksTest helper

A test clock enables deterministic control over objects in testmode. With a test clock, you can create objects at a frozen time in the past or future, and advance to a specific future time to observe webhooks and state changes. After the clock advances, you can either validate the current state of your scenario (and test your assumptions), change the current state of your scenario (and test more complex scenarios), or keep advancing forward in time.

Endpoints
# The Test Clock objectTest helper

### Attributes

- idstringUnique identifier for the object.


- objectstringString representing the object’s type. Objects of the same type share the same value.


- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.


- deletes_aftertimestampTime at which this clock is scheduled to auto delete.


- frozen_timetimestampTime at which all objects belonging to this clock are frozen.


- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.


- namenullablestringThe custom name supplied at creation.


- statusenumThe status of the Test Clock.

Possible enum values`advancing`In the process of advancing time for the test clock objects.

`internal_failure`Failed to advance time. Future requests to advance time will fail.

`ready`All test clock objects have advanced to the frozen_time.



The Test Clock object`{  "id": "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",  "object": "test_helpers.test_clock",  "created": 1680112806,  "deletes_after": 1680717606,  "frozen_time": 1577836800,  "livemode": false,  "name": null,  "status": "ready"}`# Create a test clockTest helper

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

GET/v1/test_helpers/test_clocksServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/test_helpers/test_clocks \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/test_helpers/test_clocks",  "has_more": false,  "data": [    {      "id": "clock_1Mr3I22eZvKYlo2Ck0rgMqd7",      "object": "test_helpers.test_clock",      "created": 1680112806,      "deletes_after": 1680717606,      "frozen_time": 1577836800,      "livemode": false,      "name": null,      "status": "ready"    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`