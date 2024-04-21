htmlApplication Fee Refunds | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Application Fee Refunds

Application Fee Refund objects allow you to refund an application fee that has previously been created but not yet refunded. Funds will be refunded to the Stripe account from which the fee was originally collected.

Related guide: Refunding application fees

Endpoints
# The Application Fee Refund object

### Attributes

- idstringUnique identifier for the object.


- amountintegerAmount, in cents.


- currencyenumThree-letter ISO currency code, in lowercase. Must be a supported currency.


- feestringExpandableID of the application fee that was refunded.


- metadatanullableobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.



### More attributesExpand all

- objectstring
- balance_transactionnullablestringExpandable
- createdtimestamp

The Application Fee Refund object`{  "id": "fr_1MtJRpKbnvuxQXGuM6Ww0D24",  "object": "fee_refund",  "amount": 100,  "balance_transaction": null,  "created": 1680651573,  "currency": "usd",  "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",  "metadata": {}}`# Create an application fee refund

Refunds an application fee that has previously been collected but not yet refunded. Funds will be refunded to the Stripe account from which the fee was originally collected.

You can optionally refund only part of an application fee. You can do so multiple times, until the entire fee has been refunded.

Once entirely refunded, an application fee can’t be refunded again. This method will raise an error when called on an already-refunded application fee, or when trying to refund more money than is left on an application fee.

### Parameters

- amountintegerA positive integer, in cents, representing how much of this fee to refund. Can refund only up to the remaining unrefunded amount of the fee.


- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns the Application Fee Refund object if the refund succeeded. Raises an error if the fee has already been refunded, or if an invalid fee identifier was provided.

POST/v1/application_fees/:id/refundsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/application_fees/fr_1MtJRpKbnvuxQXGuM6Ww0D24/refunds \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "fr_1MtJRpKbnvuxQXGuM6Ww0D24",  "object": "fee_refund",  "amount": 100,  "balance_transaction": null,  "created": 1680651573,  "currency": "usd",  "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",  "metadata": {}}`# Update an application fee refund

Updates the specified application fee refund by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

This request only accepts metadata as an argument.

### Parameters

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns the application fee refund object if the update succeeded. This call will raise an error if update parameters are invalid.

POST/v1/application_fees/:id/refunds/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds/fr_1MtJRpKbnvuxQXGuM6Ww0D24 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "metadata[order_id]"=6735`Response`{  "id": "fr_1MtJRpKbnvuxQXGuM6Ww0D24",  "object": "fee_refund",  "amount": 100,  "balance_transaction": null,  "created": 1680651573,  "currency": "usd",  "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",  "metadata": {    "order_id": "6735"  }}`# Retrieve an application fee refund

By default, you can see the 10 most recent refunds stored directly on the application fee object, but you can also retrieve details about a specific refund stored on the application fee.

### Parameters

No parameters.

### Returns

Returns the application fee refund object.

GET/v1/application_fees/:id/refunds/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/application_fees/fee_1B73DOKbnvuxQXGuhY8Aw0TN/refunds/fr_1MtJRpKbnvuxQXGuM6Ww0D24 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "fr_1MtJRpKbnvuxQXGuM6Ww0D24",  "object": "fee_refund",  "amount": 100,  "balance_transaction": null,  "created": 1680651573,  "currency": "usd",  "fee": "fee_1B73DOKbnvuxQXGuhY8Aw0TN",  "metadata": {}}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`