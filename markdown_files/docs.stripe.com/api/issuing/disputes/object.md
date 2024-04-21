htmlThe Dispute object | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# The Dispute object

### Attributes

- idstringUnique identifier for the object.


- amountintegerDisputed amount in the card’s currency and in the smallest currency unit. Usually the amount of the transaction, but can differ (usually because of currency fluctuation).


- balance_transactionsnullablearray of objectsExpandableList of balance transactions associated with the dispute.

Show child attributes
- currencyenumThe currency the transaction was made in.


- evidenceobjectEvidence for the dispute. Evidence contains exactly two non-null fields: the reason for the dispute and the associated evidence field for the selected reason.

Show child attributes
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- statusenumCurrent status of the dispute.

Possible enum values`expired`The dispute has expired.

`lost`The dispute is lost.

`submitted`The dispute has been submitted to Stripe.

`unsubmitted`The dispute is pending submission to Stripe.

`won`The dispute is won.


- transactionstringExpandableThe transaction being disputed.



### More attributesExpand all

- objectstring
- createdtimestamp
- livemodeboolean

The Dispute object`{  "id": "idp_1MykdxFtDWhhyHE1BFAV3osZ",  "object": "issuing.dispute",  "amount": 100,  "created": 1681947753,  "currency": "usd",  "evidence": {    "fraudulent": {      "additional_documentation": null,      "dispute_explanation": null,      "explanation": "This transaction is fraudulent.",      "uncategorized_file": null    },    "reason": "fraudulent"  },  "livemode": false,  "metadata": {},  "status": "unsubmitted",  "transaction": "ipi_1MykXhFtDWhhyHE1UjsZZ3xQ"}`# Create a dispute

Creates an Issuing Dispute object. Individual pieces of evidence within the evidence object are optional at this point. Stripe only validates that required evidence is present during submission. Refer to Dispute reasons and evidence for more details about evidence requirements.

### Parameters

- evidenceobjectEvidence provided for the dispute.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- transactionstringThe ID of the issuing transaction to create a dispute for. For transaction on Treasury FinancialAccounts, use treasury.received_debit.



### More parametersExpand all

- amountinteger

### Returns

Returns an Issuing Dispute object in unsubmitted status if creation succeeds.

POST/v1/issuing/disputesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/issuing/disputes \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d transaction=ipi_1MykXhFtDWhhyHE1UjsZZ3xQ \  -d "evidence[reason]"=fraudulent \  -d "evidence[fraudulent][explanation]"="This transaction is fraudulent."`Response`{  "id": "idp_1MykdxFtDWhhyHE1BFAV3osZ",  "object": "issuing.dispute",  "amount": 100,  "created": 1681947753,  "currency": "usd",  "evidence": {    "fraudulent": {      "additional_documentation": null,      "dispute_explanation": null,      "explanation": "This transaction is fraudulent.",      "uncategorized_file": null    },    "reason": "fraudulent"  },  "livemode": false,  "metadata": {},  "status": "unsubmitted",  "transaction": "ipi_1MykXhFtDWhhyHE1UjsZZ3xQ"}`# Update a dispute

Updates the specified Issuing Dispute object by setting the values of the parameters passed. Any parameters not provided will be left unchanged. Properties on the evidence object can be unset by passing in an empty string.

### Parameters

- evidenceobjectEvidence provided for the dispute.

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- amountinteger

### Returns

Returns an updated Issuing Dispute object if a valid identifier was provided.

POST/v1/issuing/disputes/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/issuing/disputes/idp_1MykdxFtDWhhyHE1BFAV3osZ \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "evidence[reason]"=not_received \  -d "evidence[not_received][expected_at]"=1590000000 \  -d "evidence[not_received][explanation]"= \  -d "evidence[not_received][product_description]"="Baseball cap" \  -d "evidence[not_received][product_type]"=merchandise`Response`{  "id": "idp_1MykdxFtDWhhyHE1BFAV3osZ",  "object": "issuing.dispute",  "amount": 100,  "created": 1681947753,  "currency": "usd",  "evidence": {    "reason": "not_received",    "not_received": {      "expected_at": 1590000000,      "explanation": "",      "product_description": "Baseball cap",      "product_type": "merchandise"    }  },  "livemode": false,  "metadata": {},  "status": "unsubmitted",  "transaction": "ipi_1MykXhFtDWhhyHE1UjsZZ3xQ"}`# Retrieve a dispute

Retrieves an Issuing Dispute object.

### Parameters

No parameters.

### Returns

Returns an Issuing Dispute object if a valid identifier was provided.

GET/v1/issuing/disputes/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/issuing/disputes/idp_1MykdxFtDWhhyHE1BFAV3osZ \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "idp_1MykdxFtDWhhyHE1BFAV3osZ",  "object": "issuing.dispute",  "amount": 100,  "created": 1681947753,  "currency": "usd",  "evidence": {    "fraudulent": {      "additional_documentation": null,      "dispute_explanation": null,      "explanation": "This transaction is fraudulent.",      "uncategorized_file": null    },    "reason": "fraudulent"  },  "livemode": false,  "metadata": {},  "status": "unsubmitted",  "transaction": "ipi_1MykXhFtDWhhyHE1UjsZZ3xQ"}`# List all disputes

Returns a list of Issuing Dispute objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

### Parameters

- transactionstringSelect the Issuing dispute for the given transaction.



### More parametersExpand all

- createdobject
- ending_beforestring
- limitinteger
- starting_afterstring
- statusenum

### Returns

A dictionary with a data property that contains an array of up to limit disputes, starting after dispute starting_after. Each entry in the array is a separate Issuing Dispute object. If no more disputes are available, the resulting array will be empty.

GET/v1/issuing/disputesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/issuing/disputes \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/issuing/disputes",  "has_more": false,  "data": [    {      "id": "idp_1MykdxFtDWhhyHE1BFAV3osZ",      "object": "issuing.dispute",      "amount": 100,      "created": 1681947753,      "currency": "usd",      "evidence": {        "fraudulent": {          "additional_documentation": null,          "dispute_explanation": null,          "explanation": "This transaction is fraudulent.",          "uncategorized_file": null        },        "reason": "fraudulent"      },      "livemode": false,      "metadata": {},      "status": "unsubmitted",      "transaction": "ipi_1MykXhFtDWhhyHE1UjsZZ3xQ"    }    {...}    {...}  ],}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`