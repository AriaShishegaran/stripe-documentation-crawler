htmlDisputes | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Disputes

A dispute occurs when a customer questions your charge with their card issuer. When this happens, you have the opportunity to respond to the dispute with evidence that shows that the charge is legitimate.

Related guide: Disputes and fraud

Endpoints
# The Dispute object

### Attributes

- idstringUnique identifier for the object.


- amountintegerDisputed amount. Usually the amount of the charge, but it can differ (usually because of currency fluctuation or because only part of the order is disputed).


- chargestringExpandableID of the charge that’s disputed.


- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- evidenceobjectEvidence provided to respond to a dispute. Updating any field in the hash submits all fields in the hash for review.

Show child attributes
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- payment_intentnullablestringExpandableID of the PaymentIntent that’s disputed.


- reasonstringReason given by cardholder for dispute. Possible values are bank_cannot_process, check_returned, credit_not_processed, customer_initiated, debit_not_authorized, duplicate, fraudulent, general, incorrect_account_details, insufficient_funds, product_not_received, product_unacceptable, subscription_canceled, or unrecognized. Learn more about dispute reasons.


- statusenumCurrent status of dispute. Possible values are warning_needs_response, warning_under_review, warning_closed, needs_response, under_review, won, or lost.

Possible enum values`lost``needs_response``under_review``warning_closed``warning_needs_response``warning_under_review``won`

### More attributesExpand all

- objectstring
- balance_transactionsarray of objects
- createdtimestamp
- evidence_detailsobject
- is_charge_refundableboolean
- livemodeboolean
- payment_method_detailsnullableobject

The Dispute object`{  "id": "dp_1MtJUT2eZvKYlo2CNaw2HvEv",  "object": "dispute",  "amount": 1000,  "balance_transactions": [],  "charge": "ch_1AZtxr2eZvKYlo2CJDX8whov",  "created": 1680651737,  "currency": "usd",  "evidence": {    "access_activity_log": null,    "billing_address": null,    "cancellation_policy": null,    "cancellation_policy_disclosure": null,    "cancellation_rebuttal": null,    "customer_communication": null,    "customer_email_address": null,    "customer_name": null,    "customer_purchase_ip": null,    "customer_signature": null,    "duplicate_charge_documentation": null,    "duplicate_charge_explanation": null,    "duplicate_charge_id": null,    "product_description": null,    "receipt": null,    "refund_policy": null,    "refund_policy_disclosure": null,    "refund_refusal_explanation": null,    "service_date": null,    "service_documentation": null,    "shipping_address": null,    "shipping_carrier": null,    "shipping_date": null,    "shipping_documentation": null,    "shipping_tracking_number": null,    "uncategorized_file": null,    "uncategorized_text": null  },  "evidence_details": {    "due_by": 1682294399,    "has_evidence": false,    "past_due": false,    "submission_count": 0  },  "is_charge_refundable": true,  "livemode": false,  "metadata": {},  "payment_intent": null,  "reason": "general",  "status": "warning_needs_response"}`# Update a dispute

When you get a dispute, contacting your customer is always the best first step. If that doesn’t work, you can submit evidence to help us resolve the dispute in your favor. You can do this in your dashboard, but if you prefer, you can use the API to submit evidence programmatically.

Depending on your dispute type, different evidence fields will give you a better chance of winning your dispute. To figure out which evidence fields to provide, see our guide to dispute types.

### Parameters

- evidenceobjectEvidence to upload, to respond to a dispute. Updating any field in the hash will submit all fields in the hash for review. The combined character count of all fields is limited to 150,000.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- submitbooleanWhether to immediately submit evidence to the bank. If false, evidence is staged on the dispute. Staged evidence is visible in the API and Dashboard, and can be submitted to the bank by making another request with this attribute set to true (the default).



### Returns

Returns the dispute object.

POST/v1/disputes/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/disputes/dp_1MtJUT2eZvKYlo2CNaw2HvEv \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "dp_1MtJUT2eZvKYlo2CNaw2HvEv",  "object": "dispute",  "amount": 1000,  "balance_transactions": [],  "charge": "ch_1AZtxr2eZvKYlo2CJDX8whov",  "created": 1680651737,  "currency": "usd",  "evidence": {    "access_activity_log": null,    "billing_address": null,    "cancellation_policy": null,    "cancellation_policy_disclosure": null,    "cancellation_rebuttal": null,    "customer_communication": null,    "customer_email_address": null,    "customer_name": null,    "customer_purchase_ip": null,    "customer_signature": null,    "duplicate_charge_documentation": null,    "duplicate_charge_explanation": null,    "duplicate_charge_id": null,    "product_description": null,    "receipt": null,    "refund_policy": null,    "refund_policy_disclosure": null,    "refund_refusal_explanation": null,    "service_date": null,    "service_documentation": null,    "shipping_address": null,    "shipping_carrier": null,    "shipping_date": null,    "shipping_documentation": null,    "shipping_tracking_number": null,    "uncategorized_file": null,    "uncategorized_text": null  },  "evidence_details": {    "due_by": 1682294399,    "has_evidence": false,    "past_due": false,    "submission_count": 0  },  "is_charge_refundable": true,  "livemode": false,  "metadata": {    "order_id": "6735"  },  "payment_intent": null,  "reason": "general",  "status": "warning_needs_response"}`# Retrieve a dispute

Retrieves the dispute with the given ID.

### Parameters

No parameters.

### Returns

Returns a dispute if a valid dispute ID was provided. Raises an error otherwise.

GET/v1/disputes/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/disputes/dp_1MtJUT2eZvKYlo2CNaw2HvEv \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "dp_1MtJUT2eZvKYlo2CNaw2HvEv",  "object": "dispute",  "amount": 1000,  "balance_transactions": [],  "charge": "ch_1AZtxr2eZvKYlo2CJDX8whov",  "created": 1680651737,  "currency": "usd",  "evidence": {    "access_activity_log": null,    "billing_address": null,    "cancellation_policy": null,    "cancellation_policy_disclosure": null,    "cancellation_rebuttal": null,    "customer_communication": null,    "customer_email_address": null,    "customer_name": null,    "customer_purchase_ip": null,    "customer_signature": null,    "duplicate_charge_documentation": null,    "duplicate_charge_explanation": null,    "duplicate_charge_id": null,    "product_description": null,    "receipt": null,    "refund_policy": null,    "refund_policy_disclosure": null,    "refund_refusal_explanation": null,    "service_date": null,    "service_documentation": null,    "shipping_address": null,    "shipping_carrier": null,    "shipping_date": null,    "shipping_documentation": null,    "shipping_tracking_number": null,    "uncategorized_file": null,    "uncategorized_text": null  },  "evidence_details": {    "due_by": 1682294399,    "has_evidence": false,    "past_due": false,    "submission_count": 0  },  "is_charge_refundable": true,  "livemode": false,  "metadata": {},  "payment_intent": null,  "reason": "general",  "status": "warning_needs_response"}`# List all disputes

Returns a list of your disputes.

### Parameters

- chargestringOnly return disputes associated to the charge specified by this charge ID.


- payment_intentstringOnly return disputes associated to the PaymentIntent specified by this PaymentIntent ID.



### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit disputes, starting after dispute starting_after. Each entry in the array is a separate dispute object. If no more disputes are available, the resulting array will be empty.

GET/v1/disputesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/disputes \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/disputes",  "has_more": false,  "data": [    {      "id": "dp_1MtJUT2eZvKYlo2CNaw2HvEv",      "object": "dispute",      "amount": 1000,      "balance_transactions": [],      "charge": "ch_1AZtxr2eZvKYlo2CJDX8whov",      "created": 1680651737,      "currency": "usd",      "evidence": {        "access_activity_log": null,        "billing_address": null,        "cancellation_policy": null,        "cancellation_policy_disclosure": null,        "cancellation_rebuttal": null,        "customer_communication": null,        "customer_email_address": null,        "customer_name": null,        "customer_purchase_ip": null,        "customer_signature": null,        "duplicate_charge_documentation": null,        "duplicate_charge_explanation": null,        "duplicate_charge_id": null,        "product_description": null,        "receipt": null,        "refund_policy": null,        "refund_policy_disclosure": null,        "refund_refusal_explanation": null,        "service_date": null,        "service_documentation": null,        "shipping_address": null,        "shipping_carrier": null,        "shipping_date": null,        "shipping_documentation": null,        "shipping_tracking_number": null,        "uncategorized_file": null,        "uncategorized_text": null      },      "evidence_details": {        "due_by": 1682294399,        "has_evidence": false,        "past_due": false,        "submission_count": 0      },      "is_charge_refundable": true,      "livemode": false,      "metadata": {},      "payment_intent": null,      "reason": "general",      "status": "warning_needs_response"    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`