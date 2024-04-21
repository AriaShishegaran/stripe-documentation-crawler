htmlTransfer Reversals | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Transfer Reversals

Stripe Connect platforms can reverse transfers made to a connected account, either entirely or partially, and can also specify whether to refund any related application fees. Transfer reversals add to the platform’s balance and subtract from the destination account’s balance.

Reversing a transfer that was made for a destination charge is allowed only up to the amount of the charge. It is possible to reverse a transfer_group transfer only if the destination account has enough balance to cover the reversal.

Related guide: Reverse transfers

Endpoints
# The Transfer Reversal object

### Attributes

- idstringUnique identifier for the object.


- amountintegerAmount, in cents.


- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.


- transferstringExpandableID of the transfer that was reversed.



### More attributesExpand all

- objectstring
- balance_transactionnullablestringExpandable
- createdtimestamp
- destination_payment_refundnullablestringExpandable
- source_refundnullablestringExpandable

The Transfer Reversal object`{  "id": "trr_1Mio2eLkdIwHu7ixN5LPJS4a",  "object": "transfer_reversal",  "amount": 400,  "balance_transaction": "txn_1Mio2eLkdIwHu7ixosfrbjhW",  "created": 1678147568,  "currency": "usd",  "destination_payment_refund": "pyr_1Mio2eQ9PRzxEwkZYewpaIFB",  "metadata": {},  "source_refund": null,  "transfer": "tr_1Mio2dLkdIwHu7ixsUuCxJpu"}`# Create a transfer reversal

When you create a new reversal, you must specify a transfer to create it on.

When reversing transfers, you can optionally reverse part of the transfer. You can do so as many times as you wish until the entire transfer has been reversed.

Once entirely reversed, a transfer can’t be reversed again. This method will return an error when called on an already-reversed transfer, or when trying to reverse more money than is left on a transfer.

### Parameters

- amountintegerA positive integer in cents representing how much of this transfer to reverse. Can only reverse up to the unreversed amount remaining of the transfer. Partial transfer reversals are only allowed for transfers to Stripe Accounts. Defaults to the entire transfer amount.


- descriptionstringAn arbitrary string which you can attach to a reversal object. It is displayed alongside the reversal in the Dashboard. This will be unset if you POST an empty value.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### More parametersExpand all

- refund_application_feeboolean

### Returns

Returns a transfer reversal object if the reversal succeeded. Raises an error if the transfer has already been reversed or an invalid transfer identifier was provided.

POST/v1/transfers/:id/reversalsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/transfers/tr_1Mio2dLkdIwHu7ixsUuCxJpu/reversals \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d amount=400`Response`{  "id": "trr_1Mio2eLkdIwHu7ixN5LPJS4a",  "object": "transfer_reversal",  "amount": 400,  "balance_transaction": "txn_1Mio2eLkdIwHu7ixosfrbjhW",  "created": 1678147568,  "currency": "usd",  "destination_payment_refund": "pyr_1Mio2eQ9PRzxEwkZYewpaIFB",  "metadata": {},  "source_refund": null,  "transfer": "tr_1Mio2dLkdIwHu7ixsUuCxJpu"}`# Update a reversal

Updates the specified reversal by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

This request only accepts metadata and description as arguments.

### Parameters

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns the reversal object if the update succeeded. This call will raise an error if update parameters are invalid.

POST/v1/transfers/:id/reversals/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/transfers/tr_1Mio2dLkdIwHu7ixsUuCxJpu/reversals/trr_1Mio2eLkdIwHu7ixN5LPJS4a \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "trr_1Mio2eLkdIwHu7ixN5LPJS4a",  "object": "transfer_reversal",  "amount": 400,  "balance_transaction": "txn_1Mio2eLkdIwHu7ixosfrbjhW",  "created": 1678147568,  "currency": "usd",  "destination_payment_refund": "pyr_1Mio2eQ9PRzxEwkZYewpaIFB",  "metadata": {    "order_id": "6735"  },  "source_refund": null,  "transfer": "tr_1Mio2dLkdIwHu7ixsUuCxJpu"}`# Retrieve a reversal

By default, you can see the 10 most recent reversals stored directly on the transfer object, but you can also retrieve details about a specific reversal stored on the transfer.

### Parameters

No parameters.

### Returns

Returns the reversal object.

GET/v1/transfers/:id/reversals/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/transfers/tr_1Mio2dLkdIwHu7ixsUuCxJpu/reversals/trr_1Mio2eLkdIwHu7ixN5LPJS4a \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "trr_1Mio2eLkdIwHu7ixN5LPJS4a",  "object": "transfer_reversal",  "amount": 400,  "balance_transaction": "txn_1Mio2eLkdIwHu7ixosfrbjhW",  "created": 1678147568,  "currency": "usd",  "destination_payment_refund": "pyr_1Mio2eQ9PRzxEwkZYewpaIFB",  "metadata": {},  "source_refund": null,  "transfer": "tr_1Mio2dLkdIwHu7ixsUuCxJpu"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`