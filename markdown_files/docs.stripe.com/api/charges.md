htmlCharges | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Charges

The Charge object represents a single attempt to move money into your Stripe account. PaymentIntent confirmation is the most common way to create Charges, but transferring money to a different Stripe account through Connect also creates Charges. Some legacy payment flows create Charges directly, which is not recommended for new integrations.

Endpoints
# The Charge object

### Attributes

- idstringUnique identifier for the object.


- amountintegerAmount intended to be collected by this payment. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or equivalent in charge currency. The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).


- balance_transactionnullablestringExpandableID of the balance transaction that describes the impact of this charge on your account balance (not including refunds or disputes).


- billing_detailsobjectBilling information associated with the payment method at the time of the transaction.

Show child attributes
- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- customernullablestringExpandableID of the customer this charge is for if one exists.


- descriptionnullablestringAn arbitrary string attached to the object. Often useful for displaying to users.


- disputedbooleanWhether the charge has been disputed.


- invoicenullablestringExpandableID of the invoice this charge is for if one exists.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- payment_intentnullablestringExpandableID of the PaymentIntent associated with this charge, if one exists.


- payment_method_detailsnullableobjectDetails about the payment method at the time of the transaction.

Show child attributes
- receipt_emailnullablestringThis is the email address that the receipt for this charge was sent to.


- refundedbooleanWhether the charge has been fully refunded. If the charge is only partially refunded, this attribute will still be false.


- shippingnullableobjectShipping information for the charge.

Show child attributes
- statement_descriptornullablestringFor card charges, use statement_descriptor_suffix instead. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. Must contain at least one letter, maximum 22 characters.


- statement_descriptor_suffixnullablestringProvides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.


- statusenumThe status of the payment is either succeeded, pending, or failed.



### More attributesExpand all

- objectstring
- amount_capturedinteger
- amount_refundedinteger
- applicationnullablestringExpandableConnect only
- application_feenullablestringExpandableConnect only
- application_fee_amountnullableintegerConnect only
- calculated_statement_descriptornullablestring
- capturedboolean
- createdtimestamp
- failure_balance_transactionnullablestringExpandable
- failure_codenullablestring
- failure_messagenullablestring
- fraud_detailsnullableobject
- livemodeboolean
- on_behalf_ofnullablestringExpandableConnect only
- outcomenullableobject
- paidboolean
- payment_methodnullablestring
- radar_optionsnullableobject
- receipt_numbernullablestring
- receipt_urlnullablestring
- refundsnullableobjectExpandable
- reviewnullablestringExpandable
- source_transfernullablestringExpandableConnect only
- transfernullablestringExpandableConnect only
- transfer_datanullableobjectConnect only
- transfer_groupnullablestringConnect only

The Charge object`{  "id": "ch_3MmlLrLkdIwHu7ix0snN0B15",  "object": "charge",  "amount": 1099,  "amount_captured": 1099,  "amount_refunded": 0,  "application": null,  "application_fee": null,  "application_fee_amount": null,  "balance_transaction": "txn_3MmlLrLkdIwHu7ix0uke3Ezy",  "billing_details": {    "address": {      "city": null,      "country": null,      "line1": null,      "line2": null,      "postal_code": null,      "state": null    },    "email": null,    "name": null,    "phone": null  },  "calculated_statement_descriptor": "Stripe",  "captured": true,  "created": 1679090539,  "currency": "usd",  "customer": null,  "description": null,  "disputed": false,  "failure_balance_transaction": null,  "failure_code": null,  "failure_message": null,  "fraud_details": {},  "invoice": null,  "livemode": false,  "metadata": {},  "on_behalf_of": null,  "outcome": {    "network_status": "approved_by_network",    "reason": null,    "risk_level": "normal",    "risk_score": 32,    "seller_message": "Payment complete.",    "type": "authorized"  },  "paid": true,  "payment_intent": null,  "payment_method": "card_1MmlLrLkdIwHu7ixIJwEWSNR",  "payment_method_details": {    "card": {      "brand": "visa",      "checks": {        "address_line1_check": null,        "address_postal_code_check": null,        "cvc_check": null      },      "country": "US",      "exp_month": 3,      "exp_year": 2024,      "fingerprint": "mToisGZ01V71BCos",      "funding": "credit",      "installments": null,      "last4": "4242",      "mandate": null,      "network": "visa",      "three_d_secure": null,      "wallet": null    },    "type": "card"  },  "receipt_email": null,  "receipt_number": null,  "receipt_url": "https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KOvG06AGMgZfBXyr1aw6LBa9vaaSRWU96d8qBwz9z2J_CObiV_H2-e8RezSK_sw0KISesp4czsOUlVKY",  "refunded": false,  "review": null,  "shipping": null,  "source_transfer": null,  "statement_descriptor": null,  "statement_descriptor_suffix": null,  "status": "succeeded",  "transfer_data": null,  "transfer_group": null}`# Create a chargeDeprecated

This method is no longer recommended—use the Payment Intents API to initiate a new payment instead. Confirmation of the PaymentIntent creates the Charge object used to request payment.

### Parameters

- amountintegerRequiredAmount intended to be collected by this payment. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or equivalent in charge currency. The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).


- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.


- customerstringThe ID of an existing customer that will be charged in this request.


- descriptionstringAn arbitrary string which you can attach to a Charge object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the description of the charge(s) that they are describing.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- receipt_emailstringThe email address to which this charge’s receipt will be sent. The receipt will not be sent until the charge is paid, and no receipts will be sent for test mode charges. If this charge is for a Customer, the email address specified here will override the customer’s email address. If receipt_email is specified for a charge in live mode, a receipt will be sent regardless of your email settings.


- shippingobjectShipping information for the charge. Helps prevent fraud on charges for physical goods.

Show child parameters
- sourcestringA payment source to be charged. This can be the ID of a card (i.e., credit or debit card), a bank account, a source, a token, or a connected account. For certain sources—namely, cards, bank accounts, and attached sources—you must also pass the ID of the associated customer.


- statement_descriptorstringFor card charges, use statement_descriptor_suffix instead. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. Must contain at least one letter, maximum 22 characters.


- statement_descriptor_suffixstringProvides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.



### More parametersExpand all

- application_fee_amountintegerConnect only
- captureboolean
- on_behalf_ofstringConnect only
- radar_optionsobject
- transfer_dataobjectConnect only
- transfer_groupstringConnect only

### Returns

Returns the charge object if the charge succeeded. This call raises an error if something goes wrong. A common source of error is an invalid or expired card, or a valid card with insufficient available balance.

POST/v1/chargesServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/charges \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d amount=1099 \  -d currency=usd \  -d source=tok_visa`Response`{  "id": "ch_3MmlLrLkdIwHu7ix0snN0B15",  "object": "charge",  "amount": 1099,  "amount_captured": 1099,  "amount_refunded": 0,  "application": null,  "application_fee": null,  "application_fee_amount": null,  "balance_transaction": "txn_3MmlLrLkdIwHu7ix0uke3Ezy",  "billing_details": {    "address": {      "city": null,      "country": null,      "line1": null,      "line2": null,      "postal_code": null,      "state": null    },    "email": null,    "name": null,    "phone": null  },  "calculated_statement_descriptor": "Stripe",  "captured": true,  "created": 1679090539,  "currency": "usd",  "customer": null,  "description": null,  "disputed": false,  "failure_balance_transaction": null,  "failure_code": null,  "failure_message": null,  "fraud_details": {},  "invoice": null,  "livemode": false,  "metadata": {},  "on_behalf_of": null,  "outcome": {    "network_status": "approved_by_network",    "reason": null,    "risk_level": "normal",    "risk_score": 32,    "seller_message": "Payment complete.",    "type": "authorized"  },  "paid": true,  "payment_intent": null,  "payment_method": "card_1MmlLrLkdIwHu7ixIJwEWSNR",  "payment_method_details": {    "card": {      "brand": "visa",      "checks": {        "address_line1_check": null,        "address_postal_code_check": null,        "cvc_check": null      },      "country": "US",      "exp_month": 3,      "exp_year": 2024,      "fingerprint": "mToisGZ01V71BCos",      "funding": "credit",      "installments": null,      "last4": "4242",      "mandate": null,      "network": "visa",      "three_d_secure": null,      "wallet": null    },    "type": "card"  },  "receipt_email": null,  "receipt_number": null,  "receipt_url": "https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KOvG06AGMgZfBXyr1aw6LBa9vaaSRWU96d8qBwz9z2J_CObiV_H2-e8RezSK_sw0KISesp4czsOUlVKY",  "refunded": false,  "review": null,  "shipping": null,  "source_transfer": null,  "statement_descriptor": null,  "statement_descriptor_suffix": null,  "status": "succeeded",  "transfer_data": null,  "transfer_group": null}`# Update a charge

Updates the specified charge by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

### Parameters

- customerstringThe ID of an existing customer that will be associated with this request. This field may only be updated if there is no existing associated customer with this charge.


- descriptionstringAn arbitrary string which you can attach to a charge object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the description of the charge(s) that they are describing.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.


- receipt_emailstringThis is the email address that the receipt for this charge will be sent to. If this field is updated, then a new email receipt will be sent to the updated address.


- shippingobjectShipping information for the charge. Helps prevent fraud on charges for physical goods.

Show child parameters

### More parametersExpand all

- fraud_detailsobject
- transfer_groupstringConnect only

### Returns

Returns the charge object if the update succeeded. This call will raise an error if update parameters are invalid.

POST/v1/charges/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/charges/ch_3MmlLrLkdIwHu7ix0snN0B15 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[shipping]"=express`Response`{  "id": "ch_3MmlLrLkdIwHu7ix0snN0B15",  "object": "charge",  "amount": 1099,  "amount_captured": 1099,  "amount_refunded": 0,  "application": null,  "application_fee": null,  "application_fee_amount": null,  "balance_transaction": "txn_3MmlLrLkdIwHu7ix0uke3Ezy",  "billing_details": {    "address": {      "city": null,      "country": null,      "line1": null,      "line2": null,      "postal_code": null,      "state": null    },    "email": null,    "name": null,    "phone": null  },  "calculated_statement_descriptor": "Stripe",  "captured": true,  "created": 1679090539,  "currency": "usd",  "customer": null,  "description": null,  "disputed": false,  "failure_balance_transaction": null,  "failure_code": null,  "failure_message": null,  "fraud_details": {},  "invoice": null,  "livemode": false,  "metadata": {    "shipping": "express"  },  "on_behalf_of": null,  "outcome": {    "network_status": "approved_by_network",    "reason": null,    "risk_level": "normal",    "risk_score": 32,    "seller_message": "Payment complete.",    "type": "authorized"  },  "paid": true,  "payment_intent": null,  "payment_method": "card_1MmlLrLkdIwHu7ixIJwEWSNR",  "payment_method_details": {    "card": {      "brand": "visa",      "checks": {        "address_line1_check": null,        "address_postal_code_check": null,        "cvc_check": null      },      "country": "US",      "exp_month": 3,      "exp_year": 2024,      "fingerprint": "mToisGZ01V71BCos",      "funding": "credit",      "installments": null,      "last4": "4242",      "mandate": null,      "network": "visa",      "network_token": {        "used": false      },      "three_d_secure": null,      "wallet": null    },    "type": "card"  },  "receipt_email": null,  "receipt_number": null,  "receipt_url": "https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KPDLl6UGMgawkab5iK86LBYtkq0XrhiQf1RsA2ubesH4GHiixEU8_1-Wp7h4oQEdfSUGiZpJwtQHBErT",  "refunded": false,  "refunds": {    "object": "list",    "data": [],    "has_more": false,    "total_count": 0,    "url": "/v1/charges/ch_3MmlLrLkdIwHu7ix0snN0B15/refunds"  },  "review": null,  "shipping": null,  "source_transfer": null,  "statement_descriptor": null,  "statement_descriptor_suffix": null,  "status": "succeeded",  "transfer_data": null,  "transfer_group": null}`# Retrieve a charge

Retrieves the details of a charge that has previously been created. Supply the unique charge ID that was returned from your previous request, and Stripe will return the corresponding charge information. The same information is returned when creating or refunding the charge.

### Parameters

No parameters.

### Returns

Returns a charge if a valid identifier was provided, and raises an error otherwise.

GET/v1/charges/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/charges/ch_3MmlLrLkdIwHu7ix0snN0B15 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "ch_3MmlLrLkdIwHu7ix0snN0B15",  "object": "charge",  "amount": 1099,  "amount_captured": 1099,  "amount_refunded": 0,  "application": null,  "application_fee": null,  "application_fee_amount": null,  "balance_transaction": "txn_3MmlLrLkdIwHu7ix0uke3Ezy",  "billing_details": {    "address": {      "city": null,      "country": null,      "line1": null,      "line2": null,      "postal_code": null,      "state": null    },    "email": null,    "name": null,    "phone": null  },  "calculated_statement_descriptor": "Stripe",  "captured": true,  "created": 1679090539,  "currency": "usd",  "customer": null,  "description": null,  "disputed": false,  "failure_balance_transaction": null,  "failure_code": null,  "failure_message": null,  "fraud_details": {},  "invoice": null,  "livemode": false,  "metadata": {},  "on_behalf_of": null,  "outcome": {    "network_status": "approved_by_network",    "reason": null,    "risk_level": "normal",    "risk_score": 32,    "seller_message": "Payment complete.",    "type": "authorized"  },  "paid": true,  "payment_intent": null,  "payment_method": "card_1MmlLrLkdIwHu7ixIJwEWSNR",  "payment_method_details": {    "card": {      "brand": "visa",      "checks": {        "address_line1_check": null,        "address_postal_code_check": null,        "cvc_check": null      },      "country": "US",      "exp_month": 3,      "exp_year": 2024,      "fingerprint": "mToisGZ01V71BCos",      "funding": "credit",      "installments": null,      "last4": "4242",      "mandate": null,      "network": "visa",      "three_d_secure": null,      "wallet": null    },    "type": "card"  },  "receipt_email": null,  "receipt_number": null,  "receipt_url": "https://pay.stripe.com/receipts/payment/CAcaFwoVYWNjdF8xTTJKVGtMa2RJd0h1N2l4KOvG06AGMgZfBXyr1aw6LBa9vaaSRWU96d8qBwz9z2J_CObiV_H2-e8RezSK_sw0KISesp4czsOUlVKY",  "refunded": false,  "review": null,  "shipping": null,  "source_transfer": null,  "statement_descriptor": null,  "statement_descriptor_suffix": null,  "status": "succeeded",  "transfer_data": null,  "transfer_group": null}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`