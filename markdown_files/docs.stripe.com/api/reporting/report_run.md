htmlReport Runs | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Report Runs

The Report Run object represents an instance of a report type generated with specific run parameters. Once the object is created, Stripe begins processing the report. When the report has finished running, it will give you a reference to a file where you can retrieve your results. For an overview, see API Access to Reports.

Note that certain report types can only be run based on your live-mode data (not test-mode data), and will error when queried without a live-mode API key.

Endpoints
# The Report Run object

### Attributes

- idstringUnique identifier for the object.


- parametersobjectParameters of this report run.

Show child attributes
- report_typestringThe ID of the report type to run, such as "balance.summary.1".


- resultnullableobjectThe file object representing the result of the report run (populated when status=succeeded).

Show child attributes
- statusstringStatus of this report run. This will be pending when the run is initially created. When the run finishes, this will be set to succeeded and the result field will be populated. Rarely, we may encounter an error, at which point this will be set to failed and the error field will be populated.



### More attributesExpand all

- objectstring
- createdtimestamp
- errornullablestring
- livemodeboolean
- succeeded_atnullabletimestamp

The Report Run object`{  "id": "frr_1MrQwrLkdIwHu7ixUov4x2b3",  "object": "reporting.report_run",  "created": 1680203749,  "error": null,  "livemode": false,  "parameters": {    "interval_end": 1680100000,    "interval_start": 1680000000  },  "report_type": "balance.summary.1",  "result": null,  "status": "pending",  "succeeded_at": null}`# Create a Report Run

Creates a new object and begin running the report. (Certain report types require a live-mode API key.)

### Parameters

- report_typestringRequiredThe ID of the report type to run, such as "balance.summary.1".


- parametersobjectParameters specifying how the report should be run. Different Report Types have different required and optional parameters, listed in the API Access to Reports documentation.

Show child parameters

### Returns

Returns the new ReportRun object.

POST/v1/reporting/report_runsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/reporting/report_runs \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d report_type="balance.summary.1" \  -d "parameters[interval_start]"=1680000000 \  -d "parameters[interval_end]"=1680100000`Response`{  "id": "frr_1MrQwrLkdIwHu7ixUov4x2b3",  "object": "reporting.report_run",  "created": 1680203749,  "error": null,  "livemode": false,  "parameters": {    "interval_end": 1680100000,    "interval_start": 1680000000  },  "report_type": "balance.summary.1",  "result": null,  "status": "pending",  "succeeded_at": null}`# Retrieve a Report Run

Retrieves the details of an existing Report Run.

### Parameters

No parameters.

### Returns

Returns the specified ReportRun object if found, and raises an error otherwise.

GET/v1/reporting/report_runs/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/reporting/report_runs/frr_1MrQwrLkdIwHu7ixUov4x2b3 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "frr_1MrQwrLkdIwHu7ixUov4x2b3",  "object": "reporting.report_run",  "created": 1680203749,  "error": null,  "livemode": false,  "parameters": {    "interval_end": 1680100000,    "interval_start": 1680000000  },  "report_type": "balance.summary.1",  "result": null,  "status": "pending",  "succeeded_at": null}`# List all Report Runs

Returns a list of Report Runs, with the most recent appearing first.

### Parameters

- createdobjectOnly return Report Runs that were created during the given date interval.

Show child parameters

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit Report Runs, starting after the argument starting_after if it is provided. Each entry in the array is a separate ReportRun object. If no more Report Runs are available, the resulting array will be empty.

GET/v1/reporting/report_runsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/reporting/report_runs \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/reporting/report_runs",  "has_more": false,  "data": [    {      "id": "frr_1MrQwrLkdIwHu7ixUov4x2b3",      "object": "reporting.report_run",      "created": 1680203749,      "error": null,      "livemode": false,      "parameters": {        "interval_end": 1680100000,        "interval_start": 1680000000      },      "report_type": "balance.summary.1",      "result": null,      "status": "pending",      "succeeded_at": null    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`