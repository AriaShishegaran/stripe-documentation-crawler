htmlRetrieve a quote | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Retrieve a quote

Retrieves the quote with the given ID.

### Parameters

No parameters.

### Returns

Returns a quote if a valid quote ID was provided. Raises an error otherwise.

GET/v1/quotes/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/quotes/qt_1Mr7wVLkdIwHu7ixJYSiPTGq \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "qt_1Mr7wVLkdIwHu7ixJYSiPTGq",  "object": "quote",  "amount_subtotal": 2198,  "amount_total": 2198,  "application": null,  "application_fee_amount": null,  "application_fee_percent": null,  "automatic_tax": {    "enabled": false,    "liability": null,    "status": null  },  "collection_method": "charge_automatically",  "computed": {    "recurring": null,    "upfront": {      "amount_subtotal": 2198,      "amount_total": 2198,      "total_details": {        "amount_discount": 0,        "amount_shipping": 0,        "amount_tax": 0      }    }  },  "created": 1680130691,  "currency": "usd",  "customer": "cus_NcMfB0SSFHINCV",  "default_tax_rates": [],  "description": null,  "discounts": [],  "expires_at": 1682722691,  "footer": null,  "from_quote": null,  "header": null,  "invoice": null,  "invoice_settings": {    "days_until_due": null,    "issuer": {      "type": "self"    }  },  "livemode": false,  "metadata": {},  "number": null,  "on_behalf_of": null,  "status": "draft",  "status_transitions": {    "accepted_at": null,    "canceled_at": null,    "finalized_at": null  },  "subscription": null,  "subscription_data": {    "description": null,    "effective_date": null,    "trial_period_days": null  },  "subscription_schedule": null,  "test_clock": null,  "total_details": {    "amount_discount": 0,    "amount_shipping": 0,    "amount_tax": 0  },  "transfer_data": null}`# List all quotes

Returns a list of your quotes.

### Parameters

- customerstringThe ID of the customer whose quotes will be retrieved.


- statusenumThe status of the quote.



### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring
- test_clockstring

### Returns

A dictionary with a data property that contains an array of up to limit quotes, starting after quote starting_after. Each entry in the array is a separate quote object. If no more quotes are available, the resulting array will be empty.

GET/v1/quotesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/quotes \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/quotes",  "has_more": false,  "data": [    {      "id": "qt_1Mr7SqLkdIwHu7ixpI1ClZ6z",      "object": "quote",      "amount_subtotal": 2198,      "amount_total": 2198,      "application": null,      "application_fee_amount": null,      "application_fee_percent": null,      "automatic_tax": {        "enabled": false,        "liability": null,        "status": null      },      "collection_method": "charge_automatically",      "computed": {        "recurring": null,        "upfront": {          "amount_subtotal": 2198,          "amount_total": 2198,          "total_details": {            "amount_discount": 0,            "amount_shipping": 0,            "amount_tax": 0          }        }      },      "created": 1680128852,      "currency": "usd",      "customer": "cus_NcMBZUWCIOEgEW",      "default_tax_rates": [],      "description": null,      "discounts": [],      "expires_at": 1682720852,      "footer": null,      "from_quote": null,      "header": null,      "invoice": null,      "invoice_settings": {        "days_until_due": null,        "issuer": {          "type": "self"        }      },      "livemode": false,      "metadata": {},      "number": "QT-5B9DA057-0001-1",      "on_behalf_of": null,      "status": "open",      "status_transitions": {        "accepted_at": null,        "canceled_at": null,        "finalized_at": 1680128853      },      "subscription": null,      "subscription_data": {        "description": null,        "effective_date": null,        "trial_period_days": null      },      "subscription_schedule": null,      "test_clock": null,      "total_details": {        "amount_discount": 0,        "amount_shipping": 0,        "amount_tax": 0      },      "transfer_data": null    }    {...}    {...}  ],}`# Accept a quote

Accepts the specified quote.

### Parameters

No parameters.

### Returns

Returns an accepted quote and creates an invoice, subscription or subscription schedule. Raises an error otherwise.

POST/v1/quotes/:id/acceptServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/quotes/qt_1Mr7YsLkdIwHu7ixoRgFs97D/accept \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "qt_1Mr7YsLkdIwHu7ixoRgFs97D",  "object": "quote",  "amount_subtotal": 2198,  "amount_total": 2198,  "application": null,  "application_fee_amount": null,  "application_fee_percent": null,  "automatic_tax": {    "enabled": false,    "liability": null,    "status": null  },  "collection_method": "charge_automatically",  "computed": {    "recurring": null,    "upfront": {      "amount_subtotal": 2198,      "amount_total": 2198,      "total_details": {        "amount_discount": 0,        "amount_shipping": 0,        "amount_tax": 0      }    }  },  "created": 1680129226,  "currency": "usd",  "customer": "cus_NcMHflMGStIAoB",  "default_tax_rates": [],  "description": null,  "discounts": [],  "expires_at": 1682721226,  "footer": null,  "from_quote": null,  "header": null,  "invoice": "in_1Mr7YtLkdIwHu7ixzgJJpJ3L",  "invoice_settings": {    "days_until_due": null,    "issuer": {      "type": "self"    }  },  "livemode": false,  "metadata": {},  "number": "QT-7F68F7D2-0001-1",  "on_behalf_of": null,  "status": "accepted",  "status_transitions": {    "accepted_at": 1680129227,    "canceled_at": null,    "finalized_at": 1680129227  },  "subscription": null,  "subscription_data": {    "description": null,    "effective_date": null,    "trial_period_days": null  },  "subscription_schedule": null,  "test_clock": null,  "total_details": {    "amount_discount": 0,    "amount_shipping": 0,    "amount_tax": 0  },  "transfer_data": null}`# Cancel a quote

Cancels the quote.

### Parameters

No parameters.

### Returns

Returns a canceled quote. Raises an error otherwise.

POST/v1/quotes/:id/cancelServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/quotes/qt_1Mr7ZYLkdIwHu7ixvsdZr97I/cancel \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "qt_1Mr7ZYLkdIwHu7ixvsdZr97I",  "object": "quote",  "amount_subtotal": 2198,  "amount_total": 2198,  "application": null,  "application_fee_amount": null,  "application_fee_percent": null,  "automatic_tax": {    "enabled": false,    "liability": null,    "status": null  },  "collection_method": "charge_automatically",  "computed": {    "recurring": null,    "upfront": {      "amount_subtotal": 2198,      "amount_total": 2198,      "total_details": {        "amount_discount": 0,        "amount_shipping": 0,        "amount_tax": 0      }    }  },  "created": 1680129268,  "currency": "usd",  "customer": "cus_NcMIIkPfQZQEHR",  "default_tax_rates": [],  "description": null,  "discounts": [],  "expires_at": 1682721268,  "footer": null,  "from_quote": null,  "header": null,  "invoice": null,  "invoice_settings": {    "days_until_due": null,    "issuer": {      "type": "self"    }  },  "livemode": false,  "metadata": {},  "number": "QT-FF4741D9-0001-1",  "on_behalf_of": null,  "status": "canceled",  "status_transitions": {    "accepted_at": null,    "canceled_at": 1680129269,    "finalized_at": 1680129269  },  "subscription": null,  "subscription_data": {    "description": null,    "effective_date": null,    "trial_period_days": null  },  "subscription_schedule": null,  "test_clock": null,  "total_details": {    "amount_discount": 0,    "amount_shipping": 0,    "amount_tax": 0  },  "transfer_data": null}`# Download quote PDF

Download the PDF for a finalized quote. Explanation for special handling can be found here

### Parameters

No parameters.

### Returns

The PDF file for the quote.

GET/v1/quotes/:id/pdfServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://files.stripe.com/v1/quotes/qt_0J1EnX589O8KAxCGEdmhZY3r/pdf \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`